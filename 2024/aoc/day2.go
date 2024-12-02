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

func (report *Report) IsSafe() bool {

	previousValue := -1
	direction := -2

	for index, value := range *report {
		if index == 0 {
			previousValue = value
			continue
		}
		delta := value - previousValue

		if direction == -2 {
			direction = IntSign(delta)
		} else if direction != IntSign(delta) {
			return false
		}

		absDelta := IntAbs(delta)

		if absDelta < 1 || absDelta > 3 {
			return false
		}
		previousValue = value

	}

	return true
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

func (reports *Reports) SafeCount() int {
	count := 0
	for _, report := range *reports {
		if report.IsSafe() {
			count++
		}
	}
	return count
}
