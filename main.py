from pizza import Pizza

fname = "a_example.in"
x = 0

# Partie Lecture fichier
with open("input/" + fname) as f :
   for line in f :
      if x == 0:
        maxSlices, pizzaTypes = line.split( )
      elif x == 1:
        allPizza = []
        allPizzaSlice = line.split( )
        for i in range(len(allPizzaSlice)):
          allPizza.append(Pizza(i, allPizzaSlice[i]))
      x += 1


# Partie Algo...
print('maxSlices', maxSlices)
print('pizzaTypes', pizzaTypes)
print('allPizza', allPizza)



# Partie Ecriture Sortie
fichier = open("output/" + fname, "w+")
fichier.write(maxSlices)
for pizz in allPizza:
  fichier.write("\n"+str(pizz))
fichier.close()
