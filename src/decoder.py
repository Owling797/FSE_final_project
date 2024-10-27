"""converts .pkl output to .json"""
import pickle
import json
import sys


def main():
    """main loop"""
    if len(sys.argv) < 3:
        print(
            "Usage: python convert_pickle_to_json.py <input_pickle_file> <output_json_file>"
        )
        return 1

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".pkl"):
        print("Error: The input file must have a .pkl extension.")
        return 1

    if not output_file.endswith(".json"):
        print("Error: The output file must have a .json extension.")
        return 1

    with open(input_file, "rb") as file:
        data = pickle.load(file)

    data = {k: float(v[0]) for k, v in data.items()}

    with open(output_file, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file)

    print(f"Conversion complete: {input_file} -> {output_file}")

    return 0


if __name__ == "__main__":
    main()
