TARGET=../image_converter
VENV=my-venv

all: Processing

Preprocessing:
	 @echo "Running the image converter..."
		@if [ -z "$(input)" ] || [ -z "$(output)" ]; then \
				echo "Error: 'input' and 'output' variables are required."; \
				echo "Usage: make Preprocessing input=<input_image> output=<output_image>"; \
				exit 1; \
		else \
				echo "Using input: $(input)"; \
				echo "Using output: $(output)"; \
				./$(TARGET) $(input) $(output); \
        fi


Processing: 
	mkdir -p ../out
	. ../$(VENV)/bin/activate; python3 ../model.py ../images ../out/out.pkl ../ft_resnet_10e.pt; python3 ../converter.py ../out/out.pkl ../out/out.txt


Postprocessing: 
	. ../$(VENV)/bin/activate; python3 ../converter.py ../out/out.pkl ../out/out.txt



bash:
	@/bin/bash


clean:        rm -f data/output_predictions.json