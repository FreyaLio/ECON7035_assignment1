import pandas as pd

def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    # Merge the two input data files
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged_df = merged_df.drop('id', axis=1)
    # Drop any rows with missing values
    merged_df = merged_df.dropna()
    # Drop rows where 'job' column contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    return merged_df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Data file1 (CSV)')
    parser.add_argument('input', help='Data file2 (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input, args.input)
    cleaned.to_csv(args.output, index=False)
    print(cleaned.shape)
