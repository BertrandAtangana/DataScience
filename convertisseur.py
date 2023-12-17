"""Pour cet exercice, vous allez créer un programme de conversion d'unités, qui sera capable de 
convertir des pouces (inch) en centimètres (cm), et vice-versa.
1 pouce = 2.54 cm
1 cm = 0.394 pouces
Exemple :
Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)
Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme.
Nombres à virgule :
Vous connaissez surement les données numériques avec Python, notamment avec le type "int" 
qui concerne les nombres entiers (sans virgules).
Pour cet exercice, vous allez être amené à manipuler des nombres à virgule. Il s'agit du type 
“float".
         """
         
         
print("Ce programme vous permet d'effectuer des conversions d'unités")
print("1-pouces vers cm")
print("2-cm vers pouces")
choice = input("Votre choix:(1 ou 2): ")
if choice == "1":
 valeur_str =   input("Conversion pouces->cm. Donner la valeur en pouces : ")  
 valeur_float = float(valeur_str)
 valeur_convertie = round(valeur_float*2.54,2)
 print(f"Resultat converti: {valeur_float}pouces = {valeur_convertie}cm")



