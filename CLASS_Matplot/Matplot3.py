# Ejercicio 4 de Matplotlib
# Autor: Goz
# Descripción: Gráfica sencilla con matplotlib
#              Utilizaremos la biblioteca matplotlib
#              https://matplotlib.org/

# Importamos la biblioteca matplotlib
import matplotlib.pyplot as plt

pib = [5.0000000024334,4.66441466819312,8.10688692769648,11.9054807682312,
       7.09999999585864,6.09613930404728,5.85492487760943,9.42327881833562,
       3.41862002555953,6.5024840333226,3.76246768583204,8.22880731164975,
       7.86111986077987,5.77682722978703,5.74448504962173,4.4174441350436,
       3.39063970677674,8.95694232825602,9.69817013786907,9.23325198388645,
       8.52560666281634,-0.520808041863248,-3.48642180362442,3.41081413532642,
       2.18769311647023,-3.07895537526313,1.72243931164817,1.28326099740492,
       4.10550933059433,5.17576838619527,4.21475483867759,3.54110241594962,
       1.94115584773009,4.94108067568743,-6.29123082110115,6.77325869445045,
       6.8468522786243,5.16392516795146,2.75355424748236,4.94245371467422,
       -5.28574413681748,5.11811814321162,3.66300792950094,3.64232267941347,
       1.35409196151679,2.80434012838097,3.28799159933094,2.92161516530298,
       2.06971518465136,1.99420681652698]


plt.plot(pib)
plt.show()
years = range(1961, 2019)
plt.plot(years, pib, marker='o', linewidth=2.6)
plt.show()


usa = [2.29999999999959,6.10000000000004,4.40000000000001,5.80000000000027,
       6.39999999999968,6.50000000000033,2.49999999999997,4.7999999999997,
       3.10000000000004,-0.254079592763361,3.29336237989513,5.2588953573494,
       5.64571947000461,-0.540546528852801,-0.205464013975075,5.38813922864261,
       4.62415920523873,5.53530269342748,3.16615027139846,-0.256751930206136,
       2.53771869588535,-1.80287445303816,4.58392731645819,7.2366199947577,
       4.16965595327123,3.46265171340774,3.45957255522859,4.17704638422782,
       3.67265632875832,1.88596032242019,-0.108259105278819,3.5224424944773,
4.44721634281531,4.48140755494944,4.75323598915602,4.12748401255413,
       0.998340795722612,1.7416952495761,2.86121076695474,3.79889112654006,
       3.51321379694016,2.85497229206358,1.87617145780585,-0.136579805372577,
       -2.53675706551407,2.56376655847168,1.55083550620974,2.24954585216848,
       1.8420810704697,2.4519730360895,2.88091046576689,1.56721516988685,
       2.21701033035224,2.8569878160516]

years = range(1961, 2019)
plt.plot(years, pib, years, usa)
plt.show()



years = range(1961, 2019)
plt.plot(years, pib)
plt.plot(years, usa)
plt.legend(['México', 'Estados Unidos'])
plt.title('PIB Anual - Datos del Banco Mundial')
plt.xlabel('Año')
plt.ylabel('Crecimiento del PIB (% anual)')
plt.show()



