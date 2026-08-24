"""
Lab 1: The Multi-Paradigm Tour -- verification harness.

Run: python verify_tour.py
Requires: stats.py, stats.c compiled to stats_c (or stats_c.exe on
Windows), and stats.go compiled to stats_go (or stats_go.exe), all in
this directory. Compile C/Go yourself first:
  gcc -O2 -o stats_c stats.c
  go build -o stats_go stats.go

Prints the Success Token only if all three implementations produce
byte-identical output across all five test vectors.
"""

import base64
import hashlib
import os
import subprocess
import sys
import time

ASSIGNMENT_ID = "LAB01"

TEST_VECTORS = [
    [4, 8, 15, 16, 23, 42],
    [1, 1, 1, 1],
    [7, 2, 7, 2, 9],         # mode tie (7 and 2 both appear twice) -- must resolve to the smaller value, 2
    [10],
    [-5, -1, 0, 1, 5, 100],
]


def get_student_id() -> str:
    """Prompt for the student's USI username; baked into the Success Token
    so a copied/shared token decodes to someone else's name, not yours."""
    student_id = input("Enter your USI username (e.g. cwill): ").strip()
    while not student_id:
        student_id = input("Username cannot be blank. Enter your USI username: ").strip()
    return student_id


def generate_token(assignment_id: str, student_id: str) -> str:
    digest = hashlib.sha256(f"CS379-{assignment_id}-{student_id}-VERIFIED".encode()).hexdigest()[:16]
    raw = f"CS379|{assignment_id}|{student_id}|PASS|{digest}"
    return base64.b64encode(raw.encode()).decode()


def print_success_banner(assignment_id: str) -> None:
    student_id = get_student_id()
    token = generate_token(assignment_id, student_id)
    print("\n" + "=" * 60)
    print(f"  ALL CHECKS PASSED -- {assignment_id}")
    print(f"  STUDENT: {student_id}")
    print("  SUCCESS TOKEN (paste this into Blackboard):")
    print(f"  {token}")
    print("=" * 60 + "\n")


def check(label: str, condition: bool, failures: list) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    if not condition:
        failures.append(label)


def find_binary(*candidates: str):
    for name in candidates:
        if os.path.isfile(name):
            # Use an absolute path -- on Windows, subprocess.run can fail to
            # resolve a bare relative filename like "stats_c.exe" even when
            # it's sitting right in the current directory (WinError 2), so a
            # relative name isn't safe to hand to subprocess directly.
            return os.path.abspath(name)
    return None


def run_impl(command: list, args: list) -> str:
    result = subprocess.run(command + [str(a) for a in args], capture_output=True, text=True, timeout=10)
    return result.stdout


def main() -> int:
    failures: list = []

    py_cmd = [sys.executable, "stats.py"]
    c_bin = find_binary("stats_c", "stats_c.exe", "./stats_c")
    go_bin = find_binary("stats_go", "stats_go.exe", "./stats_go")

    check("stats.py is present", os.path.isfile("stats.py"), failures)
    check("stats_c (compiled from stats.c) is present -- run: gcc -O2 -o stats_c stats.c", c_bin is not None, failures)
    check("stats_go (compiled from stats.go) is present -- run: go build -o stats_go stats.go", go_bin is not None, failures)

    if failures:
        print(f"\n{len(failures)} setup check(s) failed -- compile all three implementations first. No token issued.")
        return 1

    implementations = {"Python": py_cmd, "C": [c_bin], "Go": [go_bin]}

    print("Running all three implementations against 5 test vectors...\n")
    for vector in TEST_VECTORS:
        outputs = {}
        for name, cmd in implementations.items():
            try:
                outputs[name] = run_impl(cmd, vector)
            except Exception as e:
                check(f"{name} runs on {vector} (raised {e})", False, failures)
                outputs[name] = None
        if all(v is not None for v in outputs.values()):
            all_match = len(set(outputs.values())) == 1
            check(f"all three implementations agree on {vector}", all_match, failures)
            if not all_match:
                for name, out in outputs.items():
                    print(f"      {name}: {out!r}")

    if failures:
        print(f"\n{len(failures)} check(s) failed. No token issued.")
        return 1

    print("\nMeasuring executable size and cold-start latency...\n")
    sizes = {
        "Python (source)": os.path.getsize("stats.py"),
        "C (binary)": os.path.getsize(c_bin),
        "Go (binary)": os.path.getsize(go_bin),
    }
    latencies = {}
    for name, cmd in implementations.items():
        start = time.perf_counter()
        for _ in range(20):
            subprocess.run(cmd + ["1", "2", "3"], capture_output=True, text=True, timeout=10)
        latencies[name] = (time.perf_counter() - start) / 20 * 1000  # ms

    print(f"{'Language':<10}{'Size (bytes)':<16}{'Avg cold-start (ms)':<22}")
    for name, size_key in [("Python", "Python (source)"), ("C", "C (binary)"), ("Go", "Go (binary)")]:
        print(f"{name:<10}{sizes[size_key]:<16}{latencies[name]:<22.2f}")

    print()
    print_success_banner(ASSIGNMENT_ID)
    return 0


if __name__ == "__main__":
    sys.exit(main())
