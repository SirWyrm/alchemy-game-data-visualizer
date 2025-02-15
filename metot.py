import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# veri.csv olarak istediğiniz dosyayı ekleyin. 'Bileşik Nesne', 'Bileşen 1', 'Bileşen 2', 'Bileşen 3 şeklinde veriyi gruplayın.
def oluştur(dosya):
    dfm = pd.read_csv(dosya)
    dfm.to_csv('Geçicidosya.csv', index=False, columns=['Bileşik Nesne', 'Bileşen 1', 'Bileşen 2', 'Bileşen 3'])


def switch(Aralik, df): # int ve df yerleştirilir hangi bloğun işleneceğini hesaplar.
    match (Aralik):
        case 0:
            seçili_veri = df[(df['Bileşen 1'].isnull()) & (df['Bileşen 2'].isnull()) & (df['Bileşen 3'].isnull())]
            #seçili_veri.to_csv('Test.csv', index=False, columns=['Bileşik Nesne', 'Bileşen 1', 'Bileşen 2', 'Bileşen 3'])
            print(seçili_veri)
            return seçili_veri
        case 1:
            seçili_veri = df[(df['Bileşen 1'].notnull()) & (df['Bileşen 2'].isnull()) & (df['Bileşen 3'].isnull())]
            #seçili_veri.to_csv('Test.csv', index=False, columns=['Bileşik Nesne', 'Bileşen 1', 'Bileşen 2', 'Bileşen 3'])
            print(seçili_veri)
            return seçili_veri
        case 2:
            seçili_veri = df[(df['Bileşen 1'].notnull()) & (df['Bileşen 2'].notnull()) & (df['Bileşen 3'].isnull())]
            #seçili_veri.to_csv('Test.csv', index=False, columns=['Bileşik Nesne', 'Bileşen 1', 'Bileşen 2', 'Bileşen 3'])
            print(seçili_veri)
            return seçili_veri
        case 3:
            seçili_veri = df[(df['Bileşen 1'].notnull()) & (df['Bileşen 2'].notnull()) & (df['Bileşen 3'].notnull())]
            #seçili_veri.to_csv('Test.csv', index=False, columns=['Bileşik Nesne', 'Bileşen 1', 'Bileşen 2', 'Bileşen 3'])
            print(seçili_veri)
            return seçili_veri
# Her satır için döngü
def diz_normal(df):
    for index, row in df.iterrows():
        hedef = row['Bileşik Nesne']
        kaynak_listesi = [row['Bileşen 1'], row['Bileşen 2'], row['Bileşen 3']]
        if kaynak_listesi.notnull():
            for kaynak in kaynak_listesi:
                if pd.notna(kaynak):  # Boş değilse ekle
                    G.add_edge(kaynak, hedef)
        else: # 3 satır boşsa sadece hedefleri ekle
            G.add_node (hedef) 
    return (G)
def diz_değişken(seçili_veri):
    for index, row in seçili_veri.iterrows():
        hedef = row['Bileşik Nesne']
        kaynak_listesi = [row['Bileşen 1'], row['Bileşen 2'], row['Bileşen 3']]
        for kaynak in kaynak_listesi:
        # Boş değer kontrolü
            if pd.notna(kaynak):  # Boş değilse ekle
                G.add_edge(kaynak, hedef)
        else: # 3 satır boşsa sadece hedefleri ekle
            G.add_node (hedef)      
    return (G)