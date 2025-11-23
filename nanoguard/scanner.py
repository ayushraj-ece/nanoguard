import os
from .rules import SECRET_PATTERNS

def scan_path(path):
    findings = []

    for root, _, files in os.walk(path):
        for file in files:
            full = os.path.join(root, file)

            try:
                with open(full, "r", errors="ignore") as f:
                    content = f.read()
            except:
                continue

            for name, regex in SECRET_PATTERNS.items():
                matches = regex.findall(content)
                if matches:
                    findings.append({
                        "file": full,
                        "type": name,
                        "count": len(matches)
                    })

    return findings
