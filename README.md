# global tropopause models
**Global empirical models for tropopause height determination**

<img src="https://github.com/pjmateus/global_tropopause_model/blob/cb0211b1d1560d1cdad78d64feae5db4988f5d2b/logos.png" width="350">

The same code is available in two programming languages, Matlab and Python. The header contains guidelines for running each of these codes.

Matlab example code to call the **lookup-table-model** (BTH) function
```Matlab
lat = 38.5519;  % latitude, in degrees [-90..90]  (can be an array)
doy = 150;      % day-of-year          [1..366]   (can be an array, same size as lat)
pvu = 3.5;      % PVU value            [1.5..3.5] (optional)
z = bth_model(lat, doy, pvu)
```

Matlab example code to call the **sigmoid-model** (STH) function
```Matlab
lat = 38.5519;  % latitude, in degrees [-90..90]  (can be an array)
doy = 150;      % day-of-year          [1..366]   (can be an array, same size as lat)
pvu = 3.5;      % PVU value            [1.5..3.5] (optional)
z = sth_model(lat, doy, pvu)
```


Python code to call the hgpt function 
```Python
from hgpt import hgpt
y0 = 38.5519  # Latitude, degrees
x0 = -9.0147  # Longitude, degrees
z0 = 25       # Orthometric height, m
dt = 58119.5  # MJD
P, T, Tm, ZHD = hgpt(dt, x0, y0, z0, 'orth')
```
