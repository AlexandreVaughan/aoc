package aoc2024

import (
	"io"
	"os"
	"strconv"
	"strings"
)

type Mul struct {
	operand1 int
	operand2 int
}

func FindMul(corruptedString string) []Mul {
	indexStart := 0

	workingString := corruptedString
	startstring := "mul("
	endstring := ")"

	var result []Mul

	for {
		initialString := workingString
		indexStart = strings.Index(workingString, startstring) // Find the first occurrence of the substring
		if indexStart == -1 {
			break // No more occurrences
		} // Store the occurrence index
		indexStart += len(startstring)
		workingString = workingString[indexStart:]
		indexEnd := strings.Index(workingString, endstring)
		if indexEnd == -1 {
			continue // No more occurrences
		} // Store the occurrence index
		indexEnd += indexStart
		stringPair := initialString[indexStart:indexEnd]
		fields := strings.Split(stringPair, ",")
		if len(fields) != 2 {
			continue
		}
		var mul Mul
		intVal, err := strconv.Atoi(fields[0])
		if err != nil {
			continue
		}
		mul.operand1 = intVal
		intVal, err = strconv.Atoi(fields[1])
		if err != nil {
			continue
		}
		mul.operand2 = intVal
		result = append(result, mul)
		workingString = workingString[indexEnd-indexStart+len(endstring):]

	}
	return result
}

func (mul *Mul) value() int {
	return mul.operand1 * mul.operand2
}

func MulSum(corruptedString string) int {
	muls := FindMul(corruptedString)
	sum := 0
	for _, mul := range muls {
		sum += mul.value()
	}
	return sum
}

func ReadMulSum(filePath string) int {
	file, _ := os.Open(filePath)
	content, _ := io.ReadAll(file)
	return MulSum(string(content))
}
