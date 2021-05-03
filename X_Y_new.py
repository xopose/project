import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import tkinter as tk
import random

def E(q, r0, x, y):
    """Return the electric field vector E=(Ex,Ey) due to charge q at r0."""
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

fields = 'X', 'Y', 'q_count', 'manual_x', 'manual_y', 'counter'

def makeform(root, fields):
  entries = []
  for field in fields:
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text=field, anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=15, pady=15)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    entries.append((field, ent))
    
  return entries

def show(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        number = int(text)
        if (field == "X"):
          M = number
        elif (field == "Y"):
          N = number
        elif (field == "q_count"): # количество зарядов
          nq = number
        elif (field == "manual_x"): # количество зарядов
          manual_x = number
        elif (field == "manual_y"): # количество зарядов
          manual_y = number
        elif (field == "counter"): # количество зарядов
          counter = number

    
    # Grid of x, y points
    nx, ny = 16*M, 16*N
    x = np.linspace(0, M, nx)
    y = np.linspace(0, N, ny)
    X, Y = np.meshgrid(x, y)
    
    # Create a multipole with nq charges of alternating sign, equally spaced
    # on the unit circle.
    charges = []
    for num in range(nq):
        if (check.get() == 1):
              q = random.choice([-1, 1]) #выбор знака заряда
              qx, qy = random.uniform(0, N), random.uniform(0, M) #выбор рандомной позиции
              charges.append((q, (qx, qy)))
        else:
            q = counter
            qx, qy = manual_x, manual_y #выбор ручной позиции
            charges.append((q, (qx, qy)))
            check.set(1)


    # Electric field vector, E=(Ex, Ey), as separate components
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        Ex += ex
        Ey += ey

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot the streamlines with an appropriate colormap and arrow style
    color = 2 * np.log(np.hypot(Ex, Ey))
    ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                  density=2, arrowstyle='->', arrowsize=1.5)

    # Add filled circles for the charges themselves
    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for q, pos in charges:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q>0]))

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0,M)
    ax.set_ylim(0,N)
    ax.set_aspect('equal')
    #plt.axis('off')
    plt.show()


root = tk.Tk()
root.title('Входные данные')

ents = makeform(root, fields)

check = tk.IntVar()
c1 = tk.Checkbutton(root, text='Random_pos',variable=check, onvalue=1, offvalue=0)
c1.pack()

b1 = tk.Button(root, text='Построить', command=(lambda e=ents: show(e)), height = 2,width = 14)

b1.pack(side=tk.BOTTOM, padx=20, pady=5)
root.mainloop()



