#include <opencv2/opencv.hpp>
#include <iostream>

void convertImageToJpeg(const std::string& inputFilename, const std::string& outputFilename) {

    cv::Mat image = cv::imread(inputFilename);

    if (image.empty()) {
        std::cerr << "Could not open or find the image: " << inputFilename << std::endl;
        return;
    }

    if (!cv::imwrite(outputFilename, image)) {
        std::cerr << "Could not write the image to: " << outputFilename << std::endl;
    }
    else {
        std::cout << "Image converted and saved as: " << outputFilename << std::endl;
    }
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input_image> <output_image.jpg>" << std::endl;
        return 1;
    }
    convertImageToJpeg(argv[1], argv[2]);
    return 0;
}