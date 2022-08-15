import matplotlib.pyplot as plt

years = range(1961, 2019)

plt.style.use('Solarize_Light2')
plt.plot(years, pib)
plt.plot(years, usa)
plt.legend(['México', 'Estados Unidos'])
plt.title('PIB Anual - Datos del Banco Mundial')
plt.xlabel('Año')
plt.ylabel('Crecimiento del PIB (% anual)')

#['seaborn-pastel', 'seaborn-muted', 'fast', 'tableau-colorblind10',
# 'seaborn-darkgrid', 'seaborn-white', 'dark_background', '_classic_test',
# 'seaborn-ticks', 'seaborn', 'bmh', 'Solarize_Light2', 'grayscale',
# 'seaborn-paper', 'seaborn-poster', 'fivethirtyeight', 'ggplot',
# 'seaborn-bright', 'seaborn-whitegrid', 'seaborn-colorblind',
# 'seaborn-notebook', 'seaborn-talk', 'classic', 'seaborn-dark',
# 'seaborn-dark-palette', 'seaborn-deep']

plt.savefig(path + 'pibs.png')
plt.show()
