package aoc2024

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Abs returns the absolute value of x.
func intAbs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Distance(x, y int) int {
	return intAbs(x - y)
}

func Sort(idList []int) {
	sort.Slice(idList, func(i int, j int) bool {
		return idList[i] < idList[j]
	})
}

func ReconcileDistance(idList1 []int, idList2 []int) int {
	sum := 0
	Sort(idList1)
	Sort(idList2)
	for i := 0; i < len(idList1); i++ {
		val1 := idList1[i]
		val2 := idList2[i]
		sum += Distance(val1, val2)
	}
	return sum
}

type CountDictionary = map[int]int

func ConstructCountDictionary(idList []int) CountDictionary {
	var countDic CountDictionary = make(CountDictionary)
	for _, id := range idList {
		countDic[id] += 1
	}
	return countDic
}

func SimilarityScore(idList1 []int, idList2 []int) int {
	countDic1 := ConstructCountDictionary(idList1)
	countDic2 := ConstructCountDictionary(idList2)
	sum := 0
	for id, countList1 := range countDic1 {
		countList2 := countDic2[id]
		sum += id * countList1 * countList2
	}
	return sum
}

func ReadLists(fileName string) ([]int, []int) {
	file, _ := os.Open(fileName)
	defer file.Close()

	var idList1 []int
	var idList2 []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)

		id1, _ := strconv.Atoi(parts[0])
		id2, _ := strconv.Atoi(parts[1])

		idList1 = append(idList1, id1)
		idList2 = append(idList2, id2)
	}

	return idList1, idList2
}
