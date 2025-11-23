import re

SECRET_PATTERNS = {
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "AWS Secret Key": re.compile(r"(?i)aws(.{0,20})?(secret|key)['\"]?\s*[:=]\s*['\"][A-Za-z0-9/+=]{40}['\"]"),
    "Google API Key": re.compile(r"AIza[0-9A-Za-z\-_]{35}"),
    "JWT Token": re.compile(r"eyJ[A-Za-z0-9\-_]+?\.[A-Za-z0-9\-_]+?\.[A-Za-z0-9\-_]+"),
    "Generic Password": re.compile(r"(?i)(password|passwd|pwd)['\"]?\s*[:=]\s*['\"].+['\"]")
}
