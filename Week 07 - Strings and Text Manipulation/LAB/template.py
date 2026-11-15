"""
RECORD CHECK  -  my version
===========================

Name  :  Yoggith Premnath 
Lane  :  AI
Date  :  14/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """Clean one messy survey line and return it as a dict."""
    line = raw_line.strip()
    dataset_part, rest = line.split(",", 1)
    record = {"dataset": dataset_part.strip().lower()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip().lower()] = float(value.strip())
    return record


def status_of(rating):
    """Return FLAGGED for a low rating (2 or below), otherwise OK."""
    if rating <= 2:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []
with open("survey_records.txt") as f:
    for line in f:
        if line.strip():
            raw_records.append(line)

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["rating"])
    if status == "FLAGGED":
        flagged += 1
    print(record, status)

print(f"{len(raw_records)} records checked, {flagged} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] Run it with a value that will not convert to a number - write the
#        error down
#        ValueError: could not convert string to float: 'abc'
#    [x] Check every function does one job, with a docstring
