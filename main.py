from script import download_file, clean_data, removeUnusedColumns

#url = 'https://data.humdata.org/dataset/955ab54d-7369-441b-8d39-a2cdb14a14a1/resource/46940d42-d135-4837-823a-50cd3097c8fe/download/millennium_development_goals_mdgs_indicators_sen.csv'

url = 'https://docs.google.com/spreadsheets/d/1hNJGk3T9lp1e4jQsczf3T_IE9rDVvzvqI3HVz_9GWMA/edit#gid=0'
file_path = 'dataset.csv'
df=download_file(url, file_path)

# Prétraitement des données
choix_valeur_manquante = 'sup'
preprocessed_data = clean_data(file_path, choix_valeur_manquante)

# Suppression des colonnes inutilisées
columns_to_remove = [' StdDev', 'Comments','StdErr','StdDev']
cleaned_data = removeUnusedColumns(file_path, columns_to_remove)

# Affichage des premières lignes du DataFrame prétraité
print(preprocessed_data.head())

# Affichage des premières lignes du DataFrame avec les colonnes inutilisées supprimées
print(cleaned_data.head())


