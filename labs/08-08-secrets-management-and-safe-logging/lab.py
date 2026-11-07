"""Safe log redaction for invented test values only."""
import re

PATTERN = re.compile(r"(?i)\b(DEMO_TOKEN|DEMO_PASSWORD)=([^\s;]+)")
def redact(line):
    return PATTERN.sub(lambda m: m.group(1) + "=[REDACTED]", line)

original = "event=auth DEMO_TOKEN=example-value user=test"
safe = redact(original)
assert "example-value" not in safe
assert "user=test" in safe
assert redact("event=health status=ok") == "event=health status=ok"
print(safe)
print("Reminder: general-purpose secret detection needs stronger controls.")
