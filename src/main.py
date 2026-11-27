from extract import extract
from transform import transform
from load import load

if __name__ == "__main__":
    file = "./data/raw/diabetic_data.csv"
    df = extract(file)
    df_transformed = transform(df)
    load(df_transformed, "./data/processed/diabetic_data.csv")
