package aoc2024

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindMulSimple(t *testing.T) {
	testString := "mul(12,13)"
	result := FindMul(testString)
	assert.True(t, reflect.DeepEqual(result, []Mul{{12, 13}}))
}

func TestFindMulTwo(t *testing.T) {
	testString := "mul(13,13)mul(14,15)"
	assert.True(t, reflect.DeepEqual(FindMul(testString), []Mul{{13, 13}, {14, 15}}))
}

func TestFindMulTwoErr(t *testing.T) {
	testString := "mul(13,13)cacacacafjhdfmul(14,15)"
	assert.True(t, reflect.DeepEqual(FindMul(testString), []Mul{{13, 13}, {14, 15}}))
}

func TestMulSum(t *testing.T) {
	testString := "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
	assert.Equal(t, MulSum(testString), 161)
}
