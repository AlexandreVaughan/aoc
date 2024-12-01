package main

import (
	"fmt"

	"github.com/AlexandreVaughan/aoc2024"
)

func main() {
	// Get a greeting message and print it.
	idList1, idList2 := aoc2024.ReadLists("./day1.txt")
	reconcileDistance := aoc2024.ReconcileDistance(idList1, idList2)
	similarityScore := aoc2024.SimilarityScore(idList1, idList2)
	fmt.Println("Day1 - Reconcile distance is : ", reconcileDistance)
	fmt.Println("Day1 - Similarity score is : ", similarityScore)
}
