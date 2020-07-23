from matplotlib import pyplot as pyp

continents = ["Africa", "Asia", "Oceania", "South America", "North America", "Europe"]
population = [11.6, 50.6, 11.7, 10, 12.5, 9.7]

explode = (0,0.1,0,0,0,0.1) #to cut a slice of pi chart
colors = ["skyblue", "grey", "orange", "red", "pink", "forestgreen"]
pyp.pie(population, autopct="%1.1f%%", labels=continents, explode=explode, colors = colors)
pyp.legend(continents)
pyp.axis("equal")

pyp.show()