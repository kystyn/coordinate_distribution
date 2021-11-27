from pathlib import Path
import argparse
import pandas as pd
from pandas import DataFrame
from scipy.fft import dct

def read_csv(input_file):
    if not Path(input_file).exists():
        raise RuntimeError('Input file ' + input_file + ' does not exist')

    return pd.read_csv(input_file, delimiter='\t', header=None)

def print_csv(output_file, xy_df: DataFrame):
    xy_df.to_csv(output_file, header=None, index=None, sep='\t')

def main():
    parser = argparse.ArgumentParser(description='Fast Fourier transformation.')
    parser.add_argument('--input', '-i', help='path to input CSV file')
    parser.add_argument('--output', '-o', help='path to output CSV file')

    args = parser.parse_args()
    inp_file = args.input
    out_file = args.output

    try:
        df = read_csv(inp_file)
        df = df.astype(float)
        df[1] = dct(df[1].to_numpy())
        print_csv(out_file, df)
    except RuntimeError as e:
        print('Runtime error: ' + str(e))
    except Exception as e:
        print('Another exception: ' + str(e))

if __name__ == '__main__':
    main()