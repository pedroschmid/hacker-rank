package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

var first_range = []int{2, 3, 4, 5}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	NTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	N := int32(NTemp)

	solve(N)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func solve(n int32) {
	if n%2 != 0 {
		fmt.Println("Weird")
	}

	if n%2 == 0 {
		for _, v := range first_range {
			if int(n) == v {
				fmt.Println("Not Weird")
			}
		}
	}

	if n%2 == 0 {
		for i := 6; i < 21; i++ {
			if int(n) == i {
				fmt.Println("Weird")
			}
		}
	}

	if n%2 == 0 && n > 20 {
		fmt.Println("Not Weird")
	}

}
