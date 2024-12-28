import pandas as pd
import matplotlib.pyplot as plt
import re

# list
all_dh_data = []
years = [year for year in range(1950, 2025) if year != 2020]

for year in years:
    # path
    path_batting = f'./excel/batting_{year}.xlsx'
    try:
        # read data
        data = pd.read_excel(path_batting)
        #print(data.head())

        # DH data
        dh_data = data[data['Pos'].str.contains(r'\*D', na=False)]
        dh_data['Year'] = year
        all_dh_data.append(dh_data)

    except FileNotFoundError:
        print(f"{year}年のファイルを検出できませんでした\n")

# all DH data
all_dh_data_combined = pd.concat(all_dh_data, ignore_index=True)
all_dh_data_combined['WAR'] = pd.to_numeric(all_dh_data_combined['WAR'], errors='coerce')
all_dh_data_combined = all_dh_data_combined.dropna(subset=['WAR'])

# result
all_dh_data_sort = all_dh_data_combined.sort_values(by='WAR', ascending=False)
print(all_dh_data_sort)

# 大谷のデータを抽出
ohtani_data = all_dh_data_sort[
    all_dh_data_sort['Player'].str.contains('Shohei Ohtani', na=False)
]
print(ohtani_data)

# save
all_dh_data_sort.to_excel('batting_dh_1950_2024.xlsx', index=False)
ohtani_data.to_excel('batting_ohtani.xlsx', index=False)