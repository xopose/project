import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import random
import math

np.seterr(divide='ignore', invalid='ignore')
fields = 'X', 'Y', 'q_count'

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
      #Обработка входных данных
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
    # plot coordinates
    X = np.arange(0, M, 1)
    Y = np.arange(0, N, 1)
    X, Y = np.meshgrid(X, Y)
    # strength
    Ex = np.zeros((N, M))
    Ey = np.zeros((N, M))
   

    # вычисление положения зарядов и отрисовка
    qq = [[], []]  
    for dummy in range(nq):
        q = random.choice([-1, 1]) #выбор знака заряда
        qx, qy = random.randrange(1, N), random.randrange(1, M) #выбор позиции
        qq[0].append(qy)
        qq[1].append(qx)
        for i in range(N):
             for j in range(M):
                denom = ((i - qx) ** 2 + (j - qy) ** 2) ** 1.5
                if denom != 0: 
                    Ex[i, j] += q * (j - qy) / denom
                    Ey[i, j] += q * (i - qx) / denom

    # arrows color
    C = np.hypot(Ex, Ey) #цвет стрелок SQRT(х * х + у * у)
    # нормализованные значения для стрелок
    E = (Ex ** 2 + Ey ** 2) ** .5
    Ex = Ex / E
    Ey = Ey / E

    # отрисовка
    plt.figure(figsize=(12, 8))
    # заряды
    plt.plot(*qq, 'bo')
    # поле
    plt.quiver(X, Y, Ex, Ey, C, pivot='mid')
    # цветная шкала для стрелок
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Шкала плотности линий магнитного поля')

    #отрисовка основного окна
    plt.title('Моделирование магнитных линий')
    plt.axis('equal')
    plt.axis('off')
    plt.show()
root = tk.Tk()
root.title('Входные данные')
ents = makeform(root, fields)
b1 = tk.Button(root, text='Построить', command=(lambda e=ents: show(e)), height = 2,width = 14)
b1.pack(side=tk.BOTTOM, padx=20, pady=5)
root.mainloop()

