

<h1>Вычисление вектора Е</h1>
<img src="https://user-images.githubusercontent.com/30976652/114514306-cc581a80-9c43-11eb-86c4-c4020d228f23.png" width=150px height=100px>

<p>Я рассчитывал вектор напряженности с помощью треугольника, получая тем самым проекции на оси x и y.</p>

<img src="https://user-images.githubusercontent.com/30976652/114445876-3edfe080-9bd9-11eb-8983-a51e1d5ed4b1.png" width=400px height=400px>

<p>Из подобия следует, что радиуса вектора от заряда до  r и длинны вектора напряженности E равно отношению проекций этих векторов</p>
R/E = x/dx = y/dy
<p>Формуля результирующего вектора</p>

![image](https://user-images.githubusercontent.com/30976652/114446408-e0673200-9bd9-11eb-9a45-ea7799d2be35.png)


<p></p>
<p></p>
<p></p>

![image](https://user-images.githubusercontent.com/30976652/114444105-28388a00-9bd7-11eb-8682-49dd93af8f70.png)

<p></p>
<p>Поля X и Y - Выбор размера поля(Произвольное значение)</p>
     <p>q_count - количество зарядов(Значение не должно превышать X*Y)</p>
     <p>manual_x(y) - выбор позиции заряда вручную(manual_x(y)<=X(Y))</p>
     <p>counter - Выбор знака заряда(-1 или 1)</p>
     <p>Random_pos - Выбор режима выставления заряда</p>
 
 
 
![image](https://user-images.githubusercontent.com/30976652/114444832-fbd13d80-9bd7-11eb-90fb-25e0cfd6db2b.png)


<p>В итоговом результате</p>
     <p>Чем более желтая стрелка тем больше плотность линий</p>
     <p>Чем более фиолетовая тем меньше</p>




<h6>В ходе лабораторной работы был использован следующий код найденный на просторах интернета</h6>
<h6>
     
        Q=array[c]
        R=((xs-Q[0])**2+(ys-Q[1])**2)**0.5
        Ev=(k*Q[2])/r**2
        Ex=(xs-Q[0])*(dEv/r)*l
        Ey=(ys-Q[1])*(dEv/r)*l
     
        Ex+=Ex1
        Ey+=Ey1
    return Ex, Ey

</h6>
