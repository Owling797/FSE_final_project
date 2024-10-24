TARGET=image_converter

Preprocessing:
	$(TARGET)
	@echo "Running the image converter..."
	@read -p "Enter input image path: " input && \
	read -p "Enter output image path (with .jpg extension): " output && \
	./$(TARGET) $$input $$output


Processing: python3 main.py evaluate


Postprocessing: python3 main.py predict --input data/input_data.json --output data/output_predictions.json

==
clean:        rm -f data/output_predictions.json