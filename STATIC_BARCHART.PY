import matplotlib.pyplot as plt

# Subjects and marks
subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'Computer']
marks = [85, 78, 92, 74, 88]

# Create bar chart
plt.bar(subjects, marks, color='green', edgecolor='black')

# Labels and title
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks Obtained in Subjects')

# Show graph
plt.show()
