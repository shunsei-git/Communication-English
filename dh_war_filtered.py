import pandas as pd
import matplotlib.pyplot as plt
import re

# list
all_dh_data = []
years = [year for year in range(2000, 2025) if year != 2020]

for year in years:
    # path
    path_batting = f'./excel/batting_{year}.xlsx'
    try:
        # read data
        data = pd.read_excel(path_batting)
        #print(data.head())
        filtered_data = []
        for _, row in data.iterrows():
            pos_info = row['Pos']
            if not isinstance(pos_info, str):
                continue
            if re.search(r'\*D', pos_info):
                other_positions = re.findall(r'[^/D*](\d+)', pos_info)
                if all(int(games) < 10 for games in other_positions):
                    filtered_data.append(row)

        year_data = pd.DataFrame(filtered_data)
        year_data['Year'] = year
        all_dh_data.append(year_data)


    except FileNotFoundError:
        print(f"{year}年のファイルを検出できませんでした\n")

# all DH data
all_dh_data_combined = pd.concat(all_dh_data, ignore_index=True)
all_dh_data_combined['WAR'] = pd.to_numeric(all_dh_data_combined['WAR'], errors='coerce')
all_dh_data_combined = all_dh_data_combined.dropna(subset=['WAR'])

# result
all_dh_data_sort = all_dh_data_combined.sort_values(by='WAR', ascending=False)
print(all_dh_data_sort)

# save
all_dh_data_sort.to_excel('batting_dh_filtered_2000_2024.xlsx', index=False)