countries = ["Paises Bajos","Chile","Groenlandia","Inglaterra","Sudafrica","Canada","Nueva Zelanda","China","Brasil","Mexico"]
def modcountries():
    repcountries = ["Rusia","Armenia","Cuba"]
    inscountries = ["Mongolia","Argentina"]
    del countries[:3]
    for n in range(len(repcountries)):
        countries.insert(n, repcountries[n])
    del countries[-3:]
    halflist = round(len(countries)/2)
    for n in range(len(inscountries)):
        countries.insert(halflist+n, inscountries[n])
    return countries
print(modcountries())