import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import metot as m # fonksiyon kütüphanem

# İşlemler
#m.oluştur("veri.csv") # Farklı bir veriniz varsa veri.csv olarak kaydetip bu metotu çalıştırabilirsiniz.
df = pd.read_csv('Geçicidosya.csv') # Dosyayı oku
# G = nx.DiGraph() # Boş bir grafik oluştur
m.diz_değişken(m.switch(0,df))
m.diz_değişken(m.switch(2,df))
m.diz_değişken(m.switch(3,df))

# Ayarlar
Düğüm_ayari = {"node_color": "skyblue","node_size": 50, "alpha": 0.5} 
Kenar_ayari = {"width": .50, "alpha": .5, "edge_color": "black"}
Etiket_ayari = {"font_size": 8}

#pos = nx.spring_layout(m.G) # Sıkı düzenleme
#pos = nx.circular_layout(m.G) # Dairesel düzenleme
pos = nx.kamada_kawai_layout(m.G) # Daha dengeli düzenleme

# Grafiği çiz
nx.draw_networkx_nodes(m.G, pos, **Düğüm_ayari)
nx.draw_networkx_edges(m.G, pos, **Kenar_ayari)
nx.draw_networkx_labels(m.G, pos, **Etiket_ayari)

# Yazdır
plt.show() #ekranı açıp görmek için
#plt.show(block=False) # Bu kısım çıktı almak için önce bunu ve alt satırı açın
#plt.savefig("Grafik.png", format="PNG", dpi = 600, bbox_inches='tight')