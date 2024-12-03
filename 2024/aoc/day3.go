package aoc2024

import (
	"io"
	"os"
	"strconv"
	"unicode"
)

type Mul struct {
	operand1 int
	operand2 int
}

type State int

const (
	InitialState State = iota
	DoState
	DontState
	MulState
)

func ParseMul(input string, ignoreDont bool) []Mul {
	var muls []Mul
	state := InitialState
	i := 0
	length := len(input)

	for i < length {
		if i+4 <= length && input[i:i+4] == "do()" {
			state = DoState
			i += 4
			continue
		}

		if i+7 <= length && input[i:i+7] == "don't()" {
			state = DontState
			i += 7
			continue
		}

		if i+4 <= length && input[i:i+4] == "mul(" {
			j := i + 4 // Start looking for numbers inside `mul(`
			closingIndex := j
			for closingIndex < length && input[closingIndex] != ')' {
				closingIndex++
			}

			if closingIndex < length && input[closingIndex] == ')' {
				// Extract arguments
				args := input[j:closingIndex]
				nums := parseMulArguments(args)

				if len(nums) == 2 {
					if !ignoreDont || state != DontState {
						state = MulState
						muls = append(muls, Mul{nums[0], nums[1]})
					}
					i = closingIndex + 1
				} else {
					i++
				}
				continue
			} else {
				i++
				continue
			}
		}

		i++
	}
	return muls
}

func parseMulArguments(args string) []int {
	var nums []int
	parts := splitArgsByComma(args)
	for _, part := range parts {
		if hasNonNumeric(part) {
			return []int{}
		}
		if num, err := strconv.Atoi(part); err == nil {
			nums = append(nums, num)
		}
	}
	return nums
}

func splitArgsByComma(args string) []string {
	var parts []string
	current := ""
	for _, ch := range args {
		if ch == ',' {
			parts = append(parts, current)
			current = ""
		} else {
			current += string(ch)
		}
	}
	if current != "" {
		parts = append(parts, current)
	}
	return parts
}

func hasNonNumeric(s string) bool {
	for _, ch := range s {
		if !unicode.IsDigit(ch) {
			return true
		}
	}
	return false
}

func (mul *Mul) value() int {
	return mul.operand1 * mul.operand2
}

func MulSum(corruptedString string, ignoreDont bool) int {
	muls := ParseMul(corruptedString, ignoreDont)
	sum := 0
	for _, mul := range muls {
		sum += mul.value()
	}
	return sum
}

func ReadMulSum(filePath string, ignoreDont bool) int {
	file, _ := os.Open(filePath)
	content, _ := io.ReadAll(file)
	return MulSum(string(content), ignoreDont)
}
