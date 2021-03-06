from matplotlib import pyplot as plt



# Bar Graph- basically used to compare things between different groups
# - it is used for categorical variables


plt.bar([1,3,5,7,9],[5,2,7,8,2],label="Example One")

plt.bar([2,4,6,8,10],[8,6,2,5,6],label="Example Two", color='g')
plt.legend()

plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Info')

plt.show()