# Blood Cell Populations Turnover & Turmoil - Simulation

1. Develop a model for a red blood cell population using the following production function, which is a variation of Equation 3: p(x) = bv(x/v)^(s) e^(-sx/(vr)), wherev is the normal red-cell count, b = 1.1 × 106, s = 8, and r = 0.5 (Gearhart and Martelli 1990). Account for the (approximate) 6-day maturation of cells, perhaps using a conveyor; and determine reasonable constants by referring to the “Model Parameters” section. Graph blood cells per kilogram, blood cells produced per kilogram, and blood cells destroyed per kilogram versus time. Find analytically where the maximum occurs and the maximum for the production function in Equation 3, and verify that your model approximately agrees with this value. 

----------------

2. Develop a model for a type of white blood cell (granulocyte) populationusing a destruction coefficient of 0.6 for a time step of 6 days and a production function of p(x) = bxe^(-x/(vr)), where the steady state is about v = 8.2×10^9 granulocytes/kg (Gearhart and Martelli 1990). Considering steady-state and maximum productions, determine reasonable constants. Alternatively, for p, use graphical input where p(0) = 0, p increases initially to a maximum and then decreases to 0. Graph blood cells per kilogram, blood cells produced per kilogram, and blood cells destroyed per kilogram versus time.

----------------

3. Develop a model for granulocytes, a type of white blood cell. Use the following production function by Mackey and Glass (1977), where b, a, and m are positive constants (Gearhart and Martelli 1990): p(x) = (ba^(m)*x) / (a^(m)+x^(m)) The units of a are cells/kilogram, while b and m are unitless. Determine reasonable constants by referring to the “Model Parameters” section. Graph blood cells per kilogram, blood cells produced per kilogram, and blood cells destroyed per kilogram versus time.

----------------

4. Complete Project 3. Show that we can use this work to model chronic myelogenous leukemia (CML), a cancer resulting in an overproduction of the white blood cells. In CML, the white cell count may be 150 times the normal, and counts can oscillate around the elevated level with a period of 30 to 70 da. As Gearhart and Martelli (1990) indicates, the following are parameters for a normal person: c = µ∂ with µ = 0.16/day , b = β∂ with β = 1.43/da , a = 3.22 × 10^8 cells/kg , m = 3, and the delay in production, ∂, is 0.68 day. Show that increasing a can result in a gain in white blood cell count, and increasing ∂ can cause the indicated periodicity. Find appropriate values for a and ∂ that match the abnormal variations in white blood cell counts of CML.
