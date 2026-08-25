"""
Lab 1: The Multi-Paradigm Tour -- Python implementation.

Run: python stats.py 4 8 15 16 23 42
Complete compute_stats() below. See the assignment,
Part B, for the full shared contract (all three language versions
must match it exactly).
"""

import sys
from typing import List, Tuple


def compute_stats(nums: List[int]) -> Tuple[float, float, int]:
    """
    Return (mean, median, mode).
    - median: for an even count, average the two middle values after sorting.
    - mode: the most frequent value; on a tie, the SMALLEST tied value.
    """

    "Mean"

    mean = sum(nums) / len(nums)

    "Median"

    "Sort the numbers to find the median"
    NumOrdered = sorted(nums)
    "Find the middle index by dividing the length by 2"
    n = len(NumOrdered)
    mid = n // 2
    "If the length is even, average the two middle values. If the length is odd, take the middle value"
    if n % 2 == 0:
        median = (NumOrdered[mid - 1] + NumOrdered[mid]) / 2
    else:
        median = NumOrdered[mid]

    "Mode"

    "Create a dictionary to count the occurrences of each number"
    counts = {}
    "For each number in the list, increment it's count everytime it shows in the list."
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    "Highest count is the max value in the counts dictionary."
    HighNum = max(counts.values())

    mode = None

    for num, count in counts.items():
        if count == HighNum:
            if mode is None or num < mode:
                mode = num

    "Runtime errors when Mode is None, although it's not. Used assert to clear errors."
    assert mode is not None
    return mean, median, mode


def main() -> int:
    if len(sys.argv) < 2:
        return 1
    nums = [int(a) for a in sys.argv[1:]]
    mean, median, mode = compute_stats(nums)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
