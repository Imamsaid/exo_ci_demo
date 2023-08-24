import requests
import pandas as pd

def download_file(url, file_path='dataset.csv'):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

""" def clean_data (file_path, choix_valeur_manquante='sup'):
    df=pd.read_csv(file_path)
    numericals = df.select_dtypes(include=['int64','float63']).columns
    categoricals =df.select_dtypes(include=['object']).columns
    #suppression de la duplication
    df.drop_duplicates(inplace=True)
    #traitement des valeurs manquantes
    #choix du methode à user
    #Pour le choix de la suppression
    if(choix_valeur_manquante =='sup'):
        df.dropna(inplace=True)

    #choix de replacer les valeurs manquantes
        # Choix de remplacer les valeurs manquantes
    elif (choix_valeur_manquante == 'remp'):
        # On remplace les valeurs des colonnes numériques par la moyenne
        for col in numericals:
            df[col].fillna(df[col].mean(), inplace=True)
              # Choix de remplacer les valeurs des colonnes catégoriques par le mode
        for col in categoricals:
            df[col].replace(np.nan, df[col].mode()[0], inplace=True)

    # On enlève les colonnes qui ont plus de 50% de valeurs manquantes
    elif (choix_valeur_manquante == 'percent'):
        is_na = df.isna().sum() / df.shape[0] * 100
        df = df[is_na[is_na < 50].index.tolist()]

    else:
        print('votre choix n\'est pas applicable')

    return df

def removeUnusedColumns(dataset_path='./data.csv', columns=[]):
    df = pd.read_csv(dataset_path)
    toRemoves = [col for col in columns if col in df.columns]

    if (len(toRemoves) > 0):
        df.drop(columns=toRemoves, inplace=True)
    else:
        print('le jeu de données n\'inclu pas ces colonnes')

    return df """
