acidez = float(input("Ingresar acidez: "))
materiaOrganica = float(input("Ingresar materia organica: "))
catAcidez = ""
catMateria = ""

if 5.6 <= acidez <= 6.5:
    catAcidez = "SUMAMENTE APTO"
elif 6.6 <= acidez <= 7.0 or 5.1 <= acidez <= 5.5:
    catAcidez = "MODERADAMENTE APTO"
elif 7.1 <= acidez <= 8.0 or 4.5 <= acidez <= 5.0:
    catAcidez = "MARGINALMENTE APTO"
elif acidez > 8.0 or acidez < 4.5:
    catAcidez = "NO APTO"
# categoria materia organica
if 0 <= materiaOrganica <= 100:
    if materiaOrganica > 5:
        catMateria = "SUMAMENTE APTO"
    elif 4.1 <= materiaOrganica <= 5:
        catMateria = "MODERADAMENTE APTO"
    elif 3 <= materiaOrganica <= 4:
        catMateria = "MARGINALMENTE APTO"
    elif materiaOrganica < 3:
        catMateria = "NO APTO"
else:
    print("porcentaje no valido")
# Salida
if catMateria == catAcidez:
    print(catMateria)
else:
    if acidez < materiaOrganica:
        print(catAcidez)
    else:
        print(catMateria)