package main

import "testing"

func TestCalculateTip(t *testing.T) {
	got := calculateTip(100.0, 10)
	want := float64(10)

	if got != want {
		t.Errorf("got %g want %g", got, want)
	}
}

func TestSplitBill(t *testing.T) {
	got := splitBill(100, 3)
	want := float64(33.33)

	if got != want {
		t.Errorf("got %g want %g", got, want)
	}
}
