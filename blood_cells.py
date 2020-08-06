from matplotlib import pyplot as plt
import math

#Production_eq = b*v*((x/v)**s)*(math.exp(-1*s*x/(v*r)))
#Production = 4.62*10**10
#Destruction = 4.62*10**10
#max_Production = 4.62*10**11

def model1():
    c = 0.14 # Destruction Coefficient Rate
    b = 1.1 * 10**6
    s = 8
    r = 0.5

    t = 0
    v = 3.3 * 10**11 # Cells/KG
    BC = 2.2 * 10**11

    t_List = [] # Time List
    BC_List = [] # Blood Cells Count
    BC_Produced = [] # Blood Cells Produced per KG
    BC_Destroyed = [] # Blood Cells Destroyed per KG

    dt = 6
    n = (100/dt)

    for i in range(int(n)):
        destruction = c * BC
        production = b*v*((BC/v)**s)*(math.exp(-1*s*BC/(v*r)))
        BC = BC + (production - destruction)/6
        t_List.append(i*dt)
        BC_List.append(BC)
        BC_Produced.append(production)
        BC_Destroyed.append(destruction)

    plt.plot(t_List, BC_List, 'r')
    plt.show()
    plt.plot(t_List, BC_Produced, 'b')
    plt.show()
    plt.plot(t_List, BC_Destroyed, 'g')
    plt.show()

#model1()


def model2():
    c = 0.6 # Destruction Coefficient Rate
    b = 8.7
    r = 0.37

    t = 0
    v = 8.2 * 10**9 # Cells/KG
    BC = v/100

    t_List = [] # Time List
    BC_List = [] # Blood Cells Count
    BC_Produced = [] # Blood Cells Produced per KG
    BC_Destroyed = [] # Blood Cells Destroyed per KG
    max_Production = (4.92*10**9)*2
    production = 0
    destruction = 0

    dt = 6
    n = (300/dt)

    flag = 0

    for i in range(int(n)):
        BC_List.append(BC)
        BC_Produced.append(production)
        BC_Destroyed.append(destruction)
        t_List.append(i*dt)
        destruction = c * BC
        production = b*BC*(math.exp(-1*BC/(v*r)))
        BC = BC + (production - destruction)/dt
        # if ( i*dt > 75 ):
        #     c += 0.5


    plt.plot(t_List, BC_List, 'r')
    plt.show()
    plt.plot(t_List, BC_Produced, 'b')
    plt.plot(t_List, BC_Destroyed, 'g')
    plt.show()

#model2()


def model3():
    c = 0.14 # Destruction Coefficient Rate
    b = 1.73*6
    m = 2.2
    a = 3.22*10**8

    t = 0
    v = 8.2 * 10**9 # Cells/KG
    BC = v/10

    t_List = [] # Time List
    BC_List = [] # Blood Cells Count
    BC_Produced = [] # Blood Cells Produced per KG
    BC_Destroyed = [] # Blood Cells Destroyed per KG
    max_Production = c * v * 2  # 2.296*10**9

    dt = 6
    n = (700/dt)

    for i in range(int(n)):
        destruction = c * BC
        production = (b*a**m*BC) / (a**m + BC**m)
        BC = BC + (production - destruction)/dt
        BC_List.append(BC)
        BC_Produced.append(production)
        BC_Destroyed.append(destruction)
        t_List.append(i*dt)


    plt.plot(t_List, BC_List, 'r')
    plt.show()
    plt.plot(t_List, BC_Destroyed, 'b')
    plt.show()
    plt.plot(t_List, BC_Produced, 'g')
    plt.show()

#model3()


def model4():
    #z = 0.68 # normal
    z = 4.7 # ill
    c = z*0.16*6 # Destruction Coefficient Rate
    b = z*1.43*6
    m = 3
    #a = 3.22*10**8 # normal
    a = 9.22*10**9 # ill

    t = 0
    v = a*(1.43/0.16-1)**(1/m) # Cells/KG
    BC = v/10

    t_List = [] # Time List
    BC_List = [] # Blood Cells Count
    BC_Produced = [] # Blood Cells Produced per KG
    BC_Destroyed = [] # Blood Cells Destroyed per KG
    max_Production = v * 150

    dt = 6
    n = (200/dt)

    for i in range(int(n)):
        destruction = c * BC
        production = (b*a**m*BC) / (a**m + BC**m)
        BC = BC + (production - destruction)/dt
        BC_List.append(BC)
        BC_Produced.append(production)
        BC_Destroyed.append(destruction)
        t_List.append(i*dt)


    plt.plot(t_List, BC_List, 'r')
    plt.show()
    #plt.plot(t_List, BC_Produced, 'b')
    #plt.show()
    #plt.plot(t_List, BC_Destroyed, 'g')
    #plt.show()

model4()
