/*
 * Lab 1: The Multi-Paradigm Tour -- C implementation.
 *
 * Compile: gcc -O2 -o stats_c stats.c
 * Run:     ./stats_c 4 8 15 16 23 42
 *
 * Complete the TODO section. See the assignment,
 * Part B, for the full shared contract (all three language versions
 * must match it exactly, including the tie-breaking mode rule).
 */

#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b) {
    int int_a = *(const int *)a;
    int int_b = *(const int *)b;
    return (int_a > int_b) - (int_a < int_b);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    int n = argc - 1;
    int *nums = malloc(n * sizeof(int));
    if (nums == NULL) {
        return 1;
    }
    for (int i = 0; i < n; i++) {
        nums[i] = atoi(argv[i + 1]);
    }

    /* TODO: compute mean, median, and mode from `nums` (length n).
     * - median: for even n, average the two middle values of the SORTED array.
     * - mode: most frequent value; on a tie, the SMALLEST tied value.
     * A sorted copy (via qsort + compare_ints) is useful for the median;
     * a simple O(n^2) frequency count is fine for mode at this input size.
     */
    double mean = 0.0;
    double median = 0.0;
    int mode = 0;

    printf("Mean: %.2f\n", mean);
    printf("Median: %.2f\n", median);
    printf("Mode: %d\n", mode);

    free(nums);
    return 0;
}
