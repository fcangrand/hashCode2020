from pizza import Pizza

fname = "a_example.in"
x = 0

# Partie Lecture fichier
with open("input/" + fname) as f :
   for line in f :
      if x == 0:
        maxSlices, pizzaTypes = line.split( )
        maxSlices = int(maxSlices)
      elif x == 1:
        allPizza = []
        allPizzaSlice = line.split( )
        for i in range(len(allPizzaSlice)):
          allPizza.append(Pizza(i, allPizzaSlice[i]))
      x += 1


# Partie Algo...
#print('maxSlices', maxSlices)
#print('pizzaTypes', pizzaTypes)
#print('allPizza', allPizza)

# Tri tableau par pizaa avec le plus de parts
pizza_sorted = sorted(allPizza , reverse=True)
print(pizza_sorted)
allPizza.sort(key=lambda x: x.slices, reverse=True)

print('allPizza', allPizza)
currentSlices = 0
i = 0
pizzaTaken = []
while (i < len(allPizza)):
  currentSlice = allPizza[i].slices
  if (currentSlice + currentSlices <= maxSlices):
    currentSlices = currentSlice + currentSlices
    pizzaTaken.append(allPizza[i].index)
  i += 1
   
#print(pizzaTaken)

# Partie Ecriture Sortie
fichier = open("output/" + fname, "w+")
fichier.write(str(len(pizzaTaken)) + "\n")
for pizz in pizzaTaken:
  fichier.write(str(pizz) + " ")
fichier.close()
