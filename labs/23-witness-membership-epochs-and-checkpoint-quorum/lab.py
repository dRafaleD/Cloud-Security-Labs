"""Offline audit witnesses: quorum depends on the CURRENT membership epoch."""
from dataclasses import dataclass
from hashlib import sha256
import hmac
import json

KEYS = {"a": b"fictional-a", "b": b"fictional-b", "c": b"fictional-c"}
STATE = {"epoch": 1, "active": {"a", "b", "c"}}
CHECKPOINT = (4, "a" * 64)
OTHER = (4, "b" * 64)

@dataclass(frozen=True)
class Attestation:
    member: str
    epoch: int
    height: int
    digest: str
    tag: str

def message(member, epoch, height, digest):
    return json.dumps({"member": member, "epoch": epoch,
                       "height": height, "digest": digest},
                      sort_keys=True, separators=(",", ":")).encode()

def issue(member: str, checkpoint: tuple[int, str], epoch: int) -> Attestation:
    height, digest = checkpoint
    tag = hmac.new(KEYS[member], message(member,epoch,height,digest),sha256).hexdigest()
    return Attestation(member, epoch, height, digest, tag)

def valid(item: Attestation) -> bool:
    if item.member not in STATE["active"] or item.epoch != STATE["epoch"]:
        return False
    if type(item.height) is not int or item.height < 0 or not isinstance(item.tag,str):
        return False
    expected = hmac.new(KEYS[item.member],
                        message(item.member,item.epoch,item.height,item.digest),
                        sha256).hexdigest()
    return hmac.compare_digest(expected,item.tag)

def classify(items: list[Attestation]) -> str:
    accepted = [item for item in items if valid(item)]
    if not accepted:
        return "INSUFFICIENT"
    by_member = {}
    for item in accepted:
        by_member.setdefault(item.member,set()).add((item.height,item.digest))
    if any(len(v) > 1 for v in by_member.values()):
        return "WITNESS_CONFLICT"
    checkpoints = {next(iter(v)) for v in by_member.values()}
    if len(checkpoints) > 1:
        return "CONFLICTING_VIEWS"
    return "QUORUM" if len(by_member) >= 2 else "INSUFFICIENT"

def rotate(new_members: set[str]) -> None:
    if len(new_members) < 2 or not new_members <= KEYS.keys():
        raise ValueError("invalid witness membership")
    STATE["epoch"] += 1
    STATE["active"] = set(new_members)

def main():
    checks = []
    old_a = issue("a",CHECKPOINT,1)
    old_b = issue("b",CHECKPOINT,1)
    checks.append(("two active witnesses",classify([old_a,old_b]),"QUORUM"))
    checks.append(("forwarded duplicate",classify([old_a,old_a]),"INSUFFICIENT"))
    checks.append(("conflicting digest",classify([old_a,issue("b",OTHER,1)]),"CONFLICTING_VIEWS"))
    rotate({"b","c"})
    checks.append(("retired witness no longer votes",classify([old_a]),"INSUFFICIENT"))
    checks.append(("old membership epoch invalid",classify([old_b]),"INSUFFICIENT"))
    new_b = issue("b",CHECKPOINT,2)
    new_c = issue("c",CHECKPOINT,2)
    checks.append(("fresh epoch quorum",classify([new_b,new_c]),"QUORUM"))
    checks.append(("old plus current no quorum",classify([old_a,new_b]),"INSUFFICIENT"))
    checks.append(("new conflicting votes",classify([new_b,issue("c",OTHER,2)]),"CONFLICTING_VIEWS"))
    forged = Attestation("c",2,4,"a"*64,"0"*64)
    checks.append(("forged tag discarded",classify([new_b,forged]),"INSUFFICIENT"))
    for name, actual, expected in checks:
        assert actual == expected, (name,actual)
        print(f"{name:31} {actual}")
    assert STATE["epoch"] == 2 and STATE["active"] == {"b","c"}
    print("10/10 synthetic membership checks passed")

if __name__ == "__main__":
    main()
