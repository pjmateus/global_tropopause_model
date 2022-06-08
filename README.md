# global tropopause models
**Global empirical models for tropopause height determination**

<img src="https://github.com/pjmateus/global_tropopause_model/blob/cb0211b1d1560d1cdad78d64feae5db4988f5d2b/logos.png" width="350">

The same code is available in two programming languages, Matlab and Python. The header contains guidelines for running each of these codes.

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
from numpy import shape, linspace, array, polyfit, polyval
from scipy.interpolate import RegularGridInterpolator
lat = 38.5519;  % latitude, in degrees [-90..90]  (can be an array)
doy = 150;      % day-of-year          [1..366]   (can be an array, same size as lat)
pvu = 3.5;      % PVU value            [1.5..3.5] (optional, not an array)
z = bth_model(lat, doy, pvu)
```

Python example code to call the **sigmoid-model** (STH) function
```Python
z = sth_model(lat, doy, pvu)
```
