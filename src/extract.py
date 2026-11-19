import pandas as pd

#Arquivo Extract: contém a extração dos dados e verificação sobre eles

def extract(file):
    #carregando o dataset
    df = pd.read_csv(file)
    
    '''
    #verificando o tamanho do dataset
    print(df.shape)
    
    #verificando as variáveis 
    inventario = pd.DataFrame({
    "variavel": df.columns,
    "tipo_dado": df.dtypes.astype(str).values,
    "valores_unicos": df.nunique().values,
    "valores_ausentes": df.isna().sum().values
    })
    
    print(inventario)
    
    #verificando os  15 primeiros registros
    for coluna in df.columns:
        print(f"\n{coluna}")
        print(df[coluna].value_counts(dropna=False).head(15))
    '''
    
    return df