package main

import (
	"fmt"

	"rsc.io/quote"

	"example.com/greetings"
)

func main() {
	fmt.Println(quote.Go())
	message := greetings.Hello("Gladys")
	fmt.Println(message)
}
