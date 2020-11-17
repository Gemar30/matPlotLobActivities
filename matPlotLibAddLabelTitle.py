# Matplotplib is a python package used for 2d graphics

#Types of Plot
# Bar Graph
# Histogram
# Scatterplot
# Pieplot
# Hexagonal Bin Plot
# Area Plot

from matplotlib import pyplot as plt
# Plotting to our canvas

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# Showing what we plotted
plt.show()