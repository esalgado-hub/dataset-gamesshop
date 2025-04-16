import pandas as pd
import os

# Caminho para a pasta com os dados processados
arquivo = 

# Verifica se o caminho é válido
if not os.path.isdir(data_folder):
    print(f"Erro: O caminho especificado não é uma pasta válida: {data_folder}")
    exit()

# Lista para armazenar os DataFrames
dataframes = []

# Carregar todos os arquivos CSV da pasta
for file_name in os.listdir(data_folder):
    if file_name.endswith('.xlsx'):  # Verifica se o arquivo é CSV
        file_path = os.path.join(data_folder, file_name)
        try:
            df = pd.read_csv(file_path)
            dataframes.append(df)
        except Exception as e:
            print(f"Erro ao carregar o arquivo {file_name}: {e}")

# Concatenar todos os DataFrames em um único
if dataframes:  # Verifica se há DataFrames para concatenar
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Exibir informações gerais sobre os dados
    print("Informações gerais:")
    print(combined_df.info())

    # Exibir estatísticas descritivas
    print("\nEstatísticas descritivas:")
    print(combined_df.describe())

    # Salvar o DataFrame combinado em um arquivo CSV
    output_file = os.path.join(data_folder, 'combined_data.csv')
    combined_df.to_csv(output_file, index=False)
    print(f"\nDados combinados salvos em: {output_file}")
else:
    print("Nenhum arquivo CSV encontrado na pasta especificada.")