package main

import (
	"fmt"
	"image"
	"image/jpeg"
	"log"
	"os"
	"path/filepath"

	_ "image/png"
)

// convertImageToJPG конвертирует изображение в формат JPEG.
func convertImageToJPG(inputPath string, outputPath string) error {
	// Открываем входной файл
	inputFile, err := os.Open(inputPath)
	if err != nil {
		return err
	}
	defer inputFile.Close()

	// Декодируем изображение
	img, _, err := image.Decode(inputFile)
	if err != nil {
		return err
	}

	// Создаем выходной файл
	outputFile, err := os.Create(outputPath)
	if err != nil {
		return err
	}
	defer outputFile.Close()

	// Кодируем изображение в формате JPEG
	if err := jpeg.Encode(outputFile, img, nil); err != nil {
		return err
	}

	return nil
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run main.go <input_image> <output_image>")
		return
	}

	inputPath := os.Args[1]
	outputPath := os.Args[2]

	// Проверяем расширение выходного файла
	if filepath.Ext(outputPath) != ".jpg" && filepath.Ext(outputPath) != ".jpeg" {
		log.Fatalf("Output file must have .jpg or .jpeg extension")
	}

	// Конвертируем изображение
	if err := convertImageToJPG(inputPath, outputPath); err != nil {
		log.Fatalf("Failed to convert image: %v", err)
	}

	if _, err := os.Stat(outputPath); os.IsNotExist(err) {
    log.Fatalf("Output file not created: %v", outputPath)
}

	fmt.Printf("Successfully converted %s to %s\n", inputPath, outputPath)
}
