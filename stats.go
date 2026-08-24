// Lab 1: The Multi-Paradigm Tour -- Go implementation.
//
// Compile: go build -o stats_go stats.go
// Run:     ./stats_go 4 8 15 16 23 42
//
// Complete the TODO section. See the assignment,
// Part B, for the full shared contract (all three language versions
// must match it exactly, including the tie-breaking mode rule).

package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
)

func computeStats(nums []int) (float64, float64, int) {
	// TODO: compute mean, median, and mode from nums.
	// - median: for an even count, average the two middle values of a SORTED copy.
	// - mode: most frequent value; on a tie, the SMALLEST tied value.
	// sort.Ints(sortedCopy) and a map[int]int frequency count will help.
	var mean float64
	var median float64
	var mode int
	return mean, median, mode
}

func main() {
	if len(os.Args) < 2 {
		os.Exit(1)
	}

	nums := make([]int, 0, len(os.Args)-1)
	for _, arg := range os.Args[1:] {
		n, err := strconv.Atoi(arg)
		if err != nil {
			os.Exit(1)
		}
		nums = append(nums, n)
	}

	mean, median, mode := computeStats(nums)
	fmt.Printf("Mean: %.2f\n", mean)
	fmt.Printf("Median: %.2f\n", median)
	fmt.Printf("Mode: %d\n", mode)
	_ = sort.Ints // keep import used even before TODO is filled in
	os.Exit(0)
}
