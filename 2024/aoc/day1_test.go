package aoc2024

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDistance(t *testing.T) {
	assert.Equal(t, 4, Distance(3, 7))
	assert.Equal(t, 6, Distance(9, 3))
}

func TestSort(t *testing.T) {
	idList := []int{3, 4, 2, 1, 3, 3}
	Sort(idList)
	assert.True(t, reflect.DeepEqual(idList, []int{1, 2, 3, 3, 3, 4}))
}

func TestReconcileDistance(t *testing.T) {
	idList1 := []int{3, 4}
	idList2 := []int{7, 6}
	reconcileDist := ReconcileDistance(idList1, idList2)
	assert.Equal(t, 6, reconcileDist)
	idList1 = []int{3, 4, 2, 1, 3, 3}
	idList2 = []int{4, 3, 5, 3, 9, 3}
	assert.Equal(t, 11, ReconcileDistance(idList1, idList2))
}

func TestCountDictionary(t *testing.T) {
	idList1 := []int{3, 4, 2, 1, 3, 3}
	countDic := ConstructCountDictionary(idList1)
	var wantedResult = CountDictionary{
		3: 3,
		4: 1,
		2: 1,
		1: 1,
	}
	assert.True(t, reflect.DeepEqual(countDic, wantedResult))
}

func TestSimilarityScore(t *testing.T) {
	idList1 := []int{2, 2, 8, 8}
	idList2 := []int{8, 1, 3, 2}
	score := SimilarityScore(idList1, idList2)
	assert.Equal(t, 20, score)
	idList1 = []int{3, 4, 2, 1, 3, 3}
	idList2 = []int{4, 3, 5, 3, 9, 3}
	assert.Equal(t, 31, SimilarityScore(idList1, idList2))
}
