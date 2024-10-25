TARGET=image_converter
VENV=my-venv

all: Processing

# Preprocessing:
# 	$(TARGET)
# 	@echo "Running the image converter..."
# 	@read -p "Enter input image path: " input && \
# 	read -p "Enter output image path (with .jpg extension): " output && \
# 	./$(TARGET) $$input $$output


Processing: 
	mkdir -p ../out
	. ../$(VENV)/bin/activate; python3 ../model.py ../ ../out/out.pkl ../ft_resnet_10e.pt


# Postprocessing: python3 main.py predict --input data/input_data.json --output data/output_predictions.json


clean:        rm -f data/output_predictions.json