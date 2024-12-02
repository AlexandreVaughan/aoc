package aoc2024

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

type Report []int

func IntSign(n int) int {
	if n > 0 {
		return 1
	} else if n < 0 {
		return -1
	}
	return 0
}

func (report *Report) removeAndCopy(index int) Report {
	if index < 0 || index >= len(*report) {
		// Return a copy of the original slice if the index is invalid
		result := make([]int, len(*report))
		copy(result, *report)
		return result
	}

	// Create a new slice with the element removed
	result := append([]int{}, (*report)[:index]...) // Copy the part before the index
	result = append(result, (*report)[index+1:]...) // Append the part after the index
	return result
}

func (report *Report) IsSafe(allowError bool) bool {

	previousValue := -1
	previousDirection := -2

	for index, value := range *report {
		if previousValue == -1 {
			previousValue = value
			continue
		}
		isSafe, direction := isSafeValue(value, previousValue, previousDirection)
		if !isSafe {
			if !allowError {
				return false
			}
			report1 := report.removeAndCopy(index)
			report2 := report.removeAndCopy(index - 1)
			report3 := report.removeAndCopy(index - 2)
			return report1.IsSafe(false) || report2.IsSafe(false) || report3.IsSafe(false)
		}

		previousValue = value
		previousDirection = direction
	}

	return true
}

func isSafeValue(value int, previousValue int, previousDirection int) (bool, int) {
	delta := value - previousValue
	absDelta := IntAbs(delta)
	direction := IntSign(delta)

	if previousDirection != -2 && previousDirection != direction {
		return false, direction
	}
	if absDelta < 1 || absDelta > 3 {
		return false, direction
	}
	return true, direction
}

type Reports []Report

func ReadReports(fileName string) Reports {
	file, _ := os.Open(fileName)
	defer file.Close()

	var reports []Report

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)

		report := Report{}

		for _, val := range parts {
			intVal, _ := strconv.Atoi(val)
			report = append(report, intVal)
		}

		reports = append(reports, report)
	}

	return reports
}

func (reports *Reports) SafeCount(allowError bool) int {
	count := 0
	for _, report := range *reports {
		if report.IsSafe(allowError) {
			count++
		}
	}
	return count
}
