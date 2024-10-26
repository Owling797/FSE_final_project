package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func OutJSON(inputPath string) error {

	data, err := os.ReadFile(inputPath)
	if err != nil {
		log.Fatalf("Failed to read JSON file: %v", err)
	}

	var images map[string]float64

	err = json.Unmarshal(data, &images)
	if err != nil {
		log.Fatalf("Failed to parse JSON data: %v", err)
	}

	for filename, score := range images {
		fmt.Printf("File Name: %s — Score: %.4f\n", filename, score)
	}

	return nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <input_json>")
		return
	}

	inputPath := os.Args[1]

	if filepath.Ext(inputPath) != ".json" {
		log.Fatalf("Output file must have .json extension")
	}

	if err := OutJSON(inputPath); err != nil {
		log.Fatalf("Failed to make an output: %v", err)
	}

}
