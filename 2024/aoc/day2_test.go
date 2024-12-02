package aoc2024

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsSafe(t *testing.T) {
	report := Report{1, 2, 3}
	assert.True(t, report.IsSafe())

	report = Report{7, 6, 4, 2, 1}
	assert.True(t, report.IsSafe())

	report = Report{1, 2, 7, 8, 9}
	assert.False(t, report.IsSafe())

	report = Report{9, 7, 6, 2, 1}
	assert.False(t, report.IsSafe())

	report = Report{1, 3, 2, 4, 5}
	assert.False(t, report.IsSafe())

	report = Report{8, 6, 4, 4, 1}
	assert.False(t, report.IsSafe())

	report = Report{1, 3, 6, 7, 9}
	assert.True(t, report.IsSafe())
}

func TestSafeCount(t *testing.T) {
	reports := Reports{
		Report{7, 6, 4, 2, 1},
		Report{1, 2, 7, 8, 9},
		Report{9, 7, 6, 2, 1},
		Report{1, 3, 2, 4, 5},
		Report{8, 6, 4, 4, 1},
		Report{1, 3, 6, 7, 9},
	}
	assert.Equal(t, reports.SafeCount(), 2)

}
