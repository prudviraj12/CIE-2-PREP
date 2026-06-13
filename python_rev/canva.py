# from tkinter import *

# root = Tk()
# root.title("Student Form")

# Label(root, text="Name").grid(row=0, column=0)
# Label(root, text="Age").grid(row=1, column=0)

# e1 = Entry(root)
# e2 = Entry(root)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# Button(root, text="Submit").grid(row=2, column=0)
# Button(root, text="Reset").grid(row=2, column=1)

# root.mainloop()
# import numpy as np
# import plotly.express as px
# import scipy

# a = np.array([1,2,3,4,5])

# print("Array =", a)
# print("Mean =", np.mean(a))

# fig = px.line(x=[1,2,3], y=[10,20,30])
# fig.show()

# print("SciPy Imported Successfully")
# from tkinter import *

# def draw_rectangle(canvas):
#     canvas.create_rectangle(50, 50, 200, 150)

# root = Tk()

# canvas = Canvas(root, width=300, height=200)
# canvas.pack()

# draw_rectangle(canvas)

# root.mainloop()
word = input("Enter a word: ")
print(",".join(word))