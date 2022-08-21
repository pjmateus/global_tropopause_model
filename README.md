# global tropopause models
**Global empirical models for tropopause height determination**

<img src="https://github.com/pjmateus/global_tropopause_model/blob/cb0211b1d1560d1cdad78d64feae5db4988f5d2b/logos.png" width="350">

The models were developed at the Dom Luiz Institute (IDL), Faculty of Sciences of the University of Lisbon (FCUL), by Pedro Mateus (pjmateus@fc.ul.pt), Virgílio Mendes (vmendes@fc.ul.pt) and Carlos Pires (clpires@fc.ul.pt).
The same code is available in two programming languages, Matlab and Python. The following code contains guidelines for running each of these codes.

Matlab example code to call the **lookup-table-model** (BTH) function
```Matlab
lat = 38.5519;  % latitude, in degrees [-90..90]  (can be an array)
doy = 150;      % day-of-year          [1..366]   (can be an array, same size as lat)
pvu = 3.5;      % PVU value            [1.5..3.5] (optional, not an array)
z = bth_model(lat, doy, pvu)
```

Matlab example code to call the **sigmoid-model** (STH) function
```Matlab
z = sth_model(lat, doy, pvu)
```

Python code to call the **lookup-table-model** (BTH) function 
```Python
lat = 38.5519;  # latitude, in degrees [-90..90]  (can be an array)
doy = 150;      # day-of-year          [1..366]   (can be an array, same size as lat)
pvu = 3.5;      # PVU value            [1.5..3.5] (optional, not an array)
z = bth_model(lat, doy, pvu)
```

Python example code to call the **sigmoid-model** (STH) function
```Python
z = sth_model(lat, doy, pvu)
```

**If you have any questions do not hesitate to contact me by email pjmateus@fc.ul.pt**
