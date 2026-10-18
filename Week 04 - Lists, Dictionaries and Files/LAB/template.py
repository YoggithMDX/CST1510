"""
RECORD CHECK  -  my version
===========================

Name  :  Yoggith 
Lane  :  AI 
Date  :  17/10/2026 

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Return the rows missing, the percentage loaded and the status."""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one dataset."""
    print()
    print("=" * 40)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 40)
    print(f"  Rows loaded    : {value:>10.2f}")
    print(f"  Rows expected  : {limit:>10.2f}")
    print(f"  Rows missing   : {difference:>10.2f}")
    print(f"  Percent loaded : {percent:>10.2f} %")
    print(f"  Status         : {status:>10}")
    print("=" * 40)


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dictionaries."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

try:
    records = load_records("datasets.txt")
except FileNotFoundError:
    print("datasets.txt was not found, starting with an empty list.")
    records = []


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

over_count = 0

with open("results.txt", "w") as out:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        if status == "OVER LIMIT":
            over_count += 1
        print_report(record["label"], record["value"], record["limit"], difference, percent, status)
        out.write(f"{record['label']},{status}\n")

print()
print(f"Records OVER LIMIT: {over_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job

