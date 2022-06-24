package main

import (
	"fmt"
	"math"
)

func calculateTip(totalBill float64, tipPercent int) float64 {
	result := totalBill * float64(tipPercent) / 100
	return result
}

func splitBill(totalBill float64, numPeople int) float64 {
	result := math.Round(totalBill/float64(numPeople)*100) / 100
	return result
}

func main() {
	var totalBill float64
	var tipPercent int
	var numPeople int
	fmt.Println("Welcome to the tip calculator.")
	fmt.Println("What was the total bill?")
	fmt.Scanln(&totalBill)
	fmt.Println("What percentage tip would you like to give? 10, 12, or 15?")
	fmt.Scanln(&tipPercent)
	fmt.Println("How many people to split the bill?")
	fmt.Scanln(&numPeople)

	subTotal := totalBill + calculateTip(totalBill, tipPercent)
	splitAmount := splitBill(subTotal, numPeople)

	fmt.Printf("Each person should pay: $%.2f\n", splitAmount)

}
