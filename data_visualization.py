from matplotlib import pyplot as plt

years = [1,2,3,4,5]
income = [3200,2000,5800,4300,5000]
income2 = [3200,2300,4900,3000,2000]

plt.plot(years, income, marker= "o", color = "forestgreen")
plt.plot(years, income2, marker= "o", color = "darkorange")

plt.xlabel("\nYears")
plt.ylabel("Income\n")
plt.ylabel("Income2\n")
plt.title("Income variation\n")
plt.legend(["Ahmed", "Talha" ])
plt.grid()
plt.show()