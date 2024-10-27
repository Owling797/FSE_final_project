import pickle
import argparse
import warnings

def main():
    warnings.filterwarnings("ignore")
    parser = argparse.ArgumentParser(description="Smokers postproc")
    parser.add_argument("inpath", type=str, help="Input file with predictions")
    parser.add_argument("outpath", type=str, help="Output file with predictions")
    args = parser.parse_args()

    inpath = str(args.inpath)
    print(inpath)
    with open(inpath, 'rb') as f:
        data = pickle.load(f)

    outpath = str(args.outpath)
    print(outpath)
    with open(outpath, 'w') as file:
        for key, val in data.items():
            file.write(f'{key}\t{val[0]}\n')


if __name__ == "__main__":
    main()