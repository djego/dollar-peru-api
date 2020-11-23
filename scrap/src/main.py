from scrapping import KambistaScrap, CambioSeguroScrap

scrap_cambio = CambioSeguroScrap(url="https://cambioseguro.com/")

print("Cambio seguro")
print(scrap_cambio.extract())

scrap_kambista = KambistaScrap(url="https://kambista.com/")
print("Kambista")
print(scrap_kambista.extract())