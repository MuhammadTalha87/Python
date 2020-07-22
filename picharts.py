from matplotlib import pyplot as pyp

continents = ["Africa", "Asia", "Oceania", "South America", "North America", "Europe"]

population = [11.6, 50.6, 11.7, 10, 12.5, 9.7]

pyp.pie(population, autopct="%1.1f%%", labels=continents)
pyp.legend(continents)

pyp.show()