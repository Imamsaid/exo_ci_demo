from script import download_file

#url = 'https://data.humdata.org/dataset/955ab54d-7369-441b-8d39-a2cdb14a14a1/resource/46940d42-d135-4837-823a-50cd3097c8fe/download/millennium_development_goals_mdgs_indicators_sen.csv'

url = 'https://data.humdata.org/dataset/955ab54d-7369-441b-8d39-a2cdb14a14a1/resource/46940d42-d135-4837-823a-50cd3097c8fe/download/millennium_development_goals_mdgs_indicators_sen.csv'
file_path = './data/dataset.csv'
download_file(url, file_path)
