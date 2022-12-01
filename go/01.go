package main

// Every solution is run along with utils.go
// e.g `go run 01.go utils.go`

import (
	"fmt"
	"strconv"
	"sort"
)

func getElfs(input_strings []string) []int {
	var elfs []int
	var elf int = 0
	for _, s := range input_strings {
		num, err := strconv.Atoi(s)
		if err == nil {
			elf += num
		} else {
			elfs = append(elfs, elf)
			elf = 0
		}
	}
	return elfs
}

func part_one(input_strings []string) int {
	return arrayMax(getElfs(input_strings))
}

func part_two(input_strings []string) int {
	var elfs []int = getElfs(input_strings)
	sort.Ints(elfs)
	return arraySum(elfs[len(elfs)-3:])
}

func main() {
	lines := getInputLines("data/01.txt")

	fmt.Println(part_one(lines))
	fmt.Println(part_two(lines))
}
