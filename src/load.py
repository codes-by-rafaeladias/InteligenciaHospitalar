from database import engine

#Arquivo Load: exportação dos dados para um arquivo CSV e uma tabela em um banco de dados relacional

def load(df, path):
    df.to_csv(path, index=False)
    df.to_sql(
        name="readmissoes_diabetes",
        con=engine,
        if_exists="replace",
        index=False
    )