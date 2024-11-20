import pandas as pd
import matplotlib.pyplot as plt

'''
1年分の選手データを読み込むプログラム．
'''

# path
year = input('year: ')
batting_path = f'./excel/batting_{year}.xlsx'

# read data
data = pd.read_excel(batting_path)
#print(data.head())

dh_data = data[data['Pos'].str.contains(r'\*D', na=False)]
dh_data_sort = dh_data.sort_values(by='WAR', ascending=False)

print(dh_data_sort)