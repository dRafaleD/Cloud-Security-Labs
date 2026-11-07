"""Run all offline lab scripts from the repository root with the same interpreter."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
labs = sorted((ROOT / "labs").glob("*/lab.py"))
if len(labs) != 13:
    raise SystemExit(f"Expected 13 lab.py scripts, found {len(labs)}")
failed = []
for lab in labs:
    try:
        run = subprocess.run([sys.executable, str(lab)], cwd=lab.parent,
                             capture_output=True, text=True, timeout=15, check=False)
        ok = run.returncode == 0
        print(("[PASS] " if ok else "[FAIL] ") + str(lab.relative_to(ROOT)))
        if not ok:
            failed.append((str(lab.relative_to(ROOT)), run.stderr or run.stdout))
    except subprocess.TimeoutExpired:
        failed.append((str(lab.relative_to(ROOT)), "timeout"))
for path, err in failed:
    print(path + ": " + err, file=sys.stderr)
if failed:
    raise SystemExit(1)
print("13/13 offline smoke checks passed.")
