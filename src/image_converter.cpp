#define cimg_display 0  // Disable display if you don't have X11
#include "CImg.h"
#include <iostream>
#include <string>

using namespace cimg_library;

int main(int argc, char** argv) {
    // Check for correct number of arguments
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input_image> <output_image.jpg>" << std::endl;
        return 1;
    }

    std::string input_image = argv[1];     // Input image file
    std::string output_image = argv[2];    // Output image file (should be .jpg)

    try {
        // Load the input image
        CImg<unsigned char> img(input_image.c_str());

        // Save the image as JPEG
        img.save(output_image.c_str());

        std::cout << "Image converted successfully: " << output_image << std::endl;
    } catch (CImgException& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}