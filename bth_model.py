#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:00:41 2022

@author: pjmateus@fc.ul.pt
"""

def bth_model(lat, doy, pvu=3.5):
    '''Lookup-table-model for tropopause determination
    INPUT
    lat : latitude, in degrees [-90..90]  (can be an array)
    doy : day-of-year          [1..366]   (can be an array, same size as lat)
    pvu : PVU value            [1.5..3.5]
    OUTPUT
    z   : tropopause height, in km
    
    For details see:
    Global empirical models for tropopause height determination
    Pedro Mateus, Virgílio B. Mendes, and Carlos A.L. Pires
    Instituto Dom Luiz, Faculdade de Ciências, Universidade de Lisboa, Lisbon, Portugal
    pjmateus@fc.ul.pt; vmendes@fc.ul.pt; clpires@fc.ul.pt
    Submitted to Atmospheric Research Journal
    '''   
    #from numpy import shape, linspace, array, polyfit, polyval
    #from scipy.interpolate import RegularGridInterpolator
    if len( shape(lat) ) == 0:
        lat = [lat]
        doy = [doy]    
    
    if shape(lat) != shape(doy):
        print('The lat and doy vector must be the same size!!!')
        return
        
    bands = [-85, -75, -65, -55, -45, -37.5, -32.5, -27.5, -22.5, -17.5, -10, \
             0, 10, 17.5, 22.5, 27.5, 32.5, 37.5, 45, 55, 65, 75, 85]   
    doys = linspace(16, 350, 12)

    Tpvu35 = array([\
    [8.295,	8.522,	8.689,	9.281,	11.333,	12.995,	14.791,	15.916,	16.275,	16.368,	16.409,	16.418,	16.406,	16.380,	16.334,	15.796,	13.238,	10.937,	10.099,	9.457,	9.085,	8.879,	8.767],
    [8.060,	8.333,	8.562,	9.370,	11.485,	13.103,	14.961,	16.034,	16.334,	16.393,	16.413,	16.425,	16.417,	16.395,	16.338,	15.833,	12.998,	10.867,	10.063,	9.415,	9.002,	8.738,	8.555],
    [8.017,	8.195,	8.501,	9.468,	11.402,	12.680,	14.540,	15.920,	16.285,	16.381,	16.414,	16.434,	16.420,	16.368,	16.308,	15.829,	12.690,	11.190,	10.310,	9.489,	8.932,	8.545,	8.347],
    [8.295,	8.326,	8.608,	9.529,	11.162,	12.142,	13.502,	15.542,	16.199,	16.363,	16.419,	16.450,	16.413,	16.342,	16.249,	15.455,	12.879,	11.739,	10.686,	9.719,	9.023,	8.465,	8.265],
    [8.764,	8.759,	8.940,	9.606,	10.811,	11.628,	12.600,	15.191,	16.147,	16.299,	16.408,	16.462,	16.395,	16.301,	16.130,	15.302,	13.856,	12.357,	11.102,	10.035,	9.282,	8.657,	8.355],
    [9.245,	9.268,	9.333,	9.751,	10.538,	11.213,	12.268,	15.141,	16.080,	16.211,	16.281,	16.288,	16.262,	16.156,	16.014,	15.716,	15.003,	13.566,	11.535,	10.378,	9.771,	9.125,	8.612],
    [9.565,	9.612,	9.618,	9.834,	10.422,	10.980,	12.388,	15.357,	16.019,	16.142,	16.184,	16.142,	16.037,	15.923,	15.884,	15.745,	15.395,	14.564,	12.236,	10.684,	10.164,	9.515,	9.030],
    [9.857,	9.793,	9.736,	9.889,	10.366,	10.876,	12.420,	15.402,	16.011,	16.144,	16.190,	16.137,	16.068,	15.962,	15.908,	15.764,	15.377,	14.571,	12.349,	10.688,	10.025,	9.485,	9.036],
    [9.831,	9.774,	9.675,	9.778,	10.372,	11.037,	12.529,	15.268,	15.950,	16.130,	16.198,	16.178,	16.136,	16.087,	16.031,	15.832,	15.268,	14.203,	11.956,	10.349,	9.642,	9.220,	8.772],
    [9.591,	9.452,	9.268,	9.603,	10.573,	11.380,	12.721,	15.248,	16.056,	16.203,	16.260,	16.257,	16.248,	16.207,	16.129,	15.805,	14.938,	13.207,	11.435,	9.992,	9.294,	8.887,	8.536],
    [9.173,	9.107,	8.981,	9.476,	10.802,	11.821,	13.193,	15.327,	16.118,	16.271,	16.368,	16.401,	16.359,	16.277,	16.178,	15.796,	14.415,	12.287,	10.870,	9.679,	9.078,	8.800,	8.560],
    [8.532,	8.713,	8.787,	9.380,	11.050,	12.395,	14.097,	15.674,	16.186,	16.322,	16.397,	16.418,	16.388,	16.342,	16.262,	15.838,	13.897,	11.557,	10.361,	9.526,	9.066,	8.821,	8.754]])

    Tpvu30 = array([\
    [8.101,	8.339,	8.485,	9.020,	11.016,	12.568,	13.961,	15.559,	16.213,	16.369,	16.409,	16.418,	16.406,	16.380,	16.325,	15.554,	12.746,	10.624,	9.816,	9.172,	8.803,	8.590,	8.457],
    [7.900,	8.147,	8.348,	9.088,	11.165,	12.612,	14.130,	15.681,	16.262,	16.393,	16.413,	16.425,	16.417,	16.395,	16.338,	15.576,	12.460,	10.583,	9.786,	9.126,	8.717,	8.452,	8.249],
    [7.831,	8.011,	8.279,	9.168,	11.097,	12.278,	13.665,	15.563,	16.235,	16.381,	16.414,	16.434,	16.420,	16.368,	16.307,	15.495,	12.270,	10.931,	10.035,	9.202,	8.653,	8.261,	8.060],
    [8.065,	8.114,	8.362,	9.224,	10.873,	11.850,	12.869,	15.060,	16.135,	16.364,	16.419,	16.450,	16.413,	16.342,	16.207,	15.050,	12.484,	11.482,	10.408,	9.447,	8.761,	8.211,	8.032],
    [8.510,	8.506,	8.670,	9.312,	10.542,	11.361,	12.168,	14.611,	16.072,	16.299,	16.408,	16.462,	16.395,	16.302,	16.068,	15.019,	13.410,	12.080,	10.833,	9.784,	9.039,	8.444,	8.141],
    [8.935,	8.956,	9.033,	9.462,	10.274,	10.954,	11.845,	14.669,	16.035,	16.211,	16.281,	16.288,	16.262,	16.157,	15.970,	15.489,	14.552,	13.132,	11.271,	10.150,	9.562,	8.915,	8.430],
    [9.217,	9.282,	9.309,	9.540,	10.152,	10.699,	11.802,	14.941,	15.984,	16.142,	16.184,	16.142,	16.037,	15.924,	15.842,	15.554,	15.026,	14.179,	11.901,	10.477,	9.976,	9.329,	8.837],
    [9.514,	9.463,	9.421,	9.597,	10.090,	10.583,	11.774,	14.996,	15.977,	16.144,	16.190,	16.137,	16.068,	15.962,	15.890,	15.613,	15.026,	14.166,	11.995,	10.480,	9.843,	9.322,	8.828],
    [9.479,	9.437,	9.355,	9.479,	10.073,	10.725,	11.807,	14.747,	15.899,	16.131,	16.198,	16.178,	16.136,	16.087,	15.984,	15.598,	14.829,	13.744,	11.599,	10.099,	9.452,	9.037,	8.579],
    [9.262,	9.121,	8.944,	9.285,	10.271,	11.070,	12.090,	14.728,	15.982,	16.204,	16.260,	16.257,	16.248,	16.207,	16.084,	15.554,	14.367,	12.706,	11.089,	9.718,	9.073,	8.672,	8.282],
    [8.899,	8.812,	8.695,	9.167,	10.501,	11.506,	12.570,	14.823,	16.035,	16.272,	16.368,	16.401,	16.359,	16.277,	16.153,	15.489,	13.663,	11.814,	10.556,	9.380,	8.820,	8.551,	8.298],
    [8.317,	8.482,	8.549,	9.097,	10.748,	12.049,	13.273,	15.245,	16.127,	16.322,	16.397,	16.418,	16.388,	16.342,	16.247,	15.529,	13.279,	11.150,	10.061,	9.228,	8.789,	8.543,	8.470]])   

    Tpvu25 = array([\
    [7.923,	8.128,	8.249,	8.727,	10.669,	12.179,	13.320,	14.921,	15.963,	16.332,	16.409,	16.418,	16.406,	16.380,	16.267,	15.068,	12.052,	10.281,	9.503,	8.853,	8.488,	8.266,	8.126],
    [7.705,	7.952,	8.139,	8.784,	10.813,	12.182,	13.446,	15.023,	15.963,	16.334,	16.414,	16.425,	16.417,	16.395,	16.294,	15.076,	11.812,	10.270,	9.478,	8.810,	8.397,	8.124,	7.920],
    [7.659,	7.804,	8.051,	8.846,	10.760,	11.915,	12.914,	14.838,	16.009,	16.364,	16.414,	16.434,	16.420,	16.368,	16.255,	14.904,	11.777,	10.636,	9.722,	8.886,	8.338,	7.951,	7.766],
    [7.840,	7.869,	8.095,	8.889,	10.545,	11.541,	12.277,	14.376,	15.952,	16.360,	16.419,	16.450,	16.413,	16.343,	16.100,	14.569,	12.128,	11.196,	10.091,	9.146,	8.471,	7.941,	7.765],
    [8.248,	8.225,	8.367,	8.979,	10.231,	11.073,	11.693,	13.846,	15.862,	16.300,	16.408,	16.462,	16.395,	16.300,	15.905,	14.604,	12.917,	11.775,	10.536,	9.496,	8.779,	8.207,	7.951],
    [8.573,	8.605,	8.699,	9.132,	9.966,	10.662,	11.367,	13.993,	15.884,	16.212,	16.281,	16.288,	16.262,	16.128,	15.769,	15.076,	14.156,	12.697,	10.982,	9.891,	9.334,	8.685,	8.233],
    [8.777,	8.884,	8.952,	9.207,	9.833,	10.388,	11.080,	14.131,	15.829,	16.143,	16.184,	16.142,	16.037,	15.894,	15.658,	15.196,	14.675,	13.758,	11.543,	10.244,	9.763,	9.107,	8.599],
    [9.098,	9.052,	9.045,	9.261,	9.778,	10.272,	10.983,	14.182,	15.822,	16.144,	16.190,	16.137,	16.068,	15.943,	15.717,	15.202,	14.603,	13.757,	11.622,	10.241,	9.645,	9.121,	8.600],
    [9.062,	9.039,	8.984,	9.137,	9.754,	10.393,	11.107,	13.843,	15.710,	16.127,	16.198,	16.178,	16.136,	16.029,	15.736,	15.126,	14.419,	13.217,	11.236,	9.828,	9.237,	8.819,	8.323],
    [8.872,	8.741,	8.593,	8.936,	9.936,	10.746,	11.440,	13.777,	15.740,	16.197,	16.260,	16.257,	16.248,	16.184,	15.855,	14.991,	13.763,	12.215,	10.727,	9.412,	8.825,	8.420,	8.026],
    [8.573,	8.501,	8.376,	8.824,	10.165,	11.180,	11.931,	13.943,	15.767,	16.261,	16.368,	16.401,	16.359,	16.278,	16.015,	14.953,	12.879,	11.405,	10.211,	9.052,	8.528,	8.268,	8.012],
    [8.057,	8.237,	8.280,	8.784,	10.416,	11.715,	12.606,	14.416,	15.873,	16.306,	16.397,	16.418,	16.388,	16.342,	16.153,	15.039,	12.537,	10.770,	9.724,	8.896,	8.471,	8.229,	8.147]])    

    Tpvu20 = array([\
    [7.719,	7.894,	8.004,	8.415,	10.264,	11.765,	12.724,	14.250,	15.407,	16.077,	16.389,	16.418,	16.406,	16.379,	16.020,	14.172,	11.191,	9.912,	9.137,	8.487,	8.112,	7.874,	7.730],
    [7.480,	7.716,	7.887,	8.458,	10.408,	11.746,	12.783,	14.410,	15.442,	16.068,	16.391,	16.425,	16.417,	16.396,	16.125,	14.317,	11.094,	9.920,	9.121,	8.447,	8.026,	7.743,	7.542],
    [7.389,	7.549,	7.796,	8.490,	10.363,	11.522,	12.344,	14.015,	15.454,	16.161,	16.407,	16.434,	16.420,	16.370,	16.055,	14.073,	11.209,	10.295,	9.356,	8.526,	7.978,	7.588,	7.387],
    [7.564,	7.575,	7.798,	8.515,	10.144,	11.190,	11.809,	13.221,	15.430,	16.268,	16.420,	16.450,	16.413,	16.333,	15.747,	13.590,	11.644,	10.854,	9.723,	8.794,	8.139,	7.619,	7.428],
    [7.884,	7.865,	8.007,	8.587,	9.852,	10.735,	11.273,	12.897,	15.445,	16.259,	16.408,	16.462,	16.395,	16.241,	15.521,	13.920,	12.428,	11.420,	10.180,	9.168,	8.477,	7.926,	7.658],
    [8.122,	8.180,	8.295,	8.750,	9.598,	10.307,	10.870,	12.890,	15.484,	16.181,	16.281,	16.288,	16.248,	15.926,	15.324,	14.617,	13.726,	12.201,	10.638,	9.590,	9.055,	8.421,	7.971],
    [8.265,	8.397,	8.528,	8.828,	9.475,	10.029,	10.585,	12.964,	15.439,	16.090,	16.184,	16.142,	16.008,	15.640,	15.195,	14.795,	14.266,	13.237,	11.148,	9.975,	9.510,	8.832,	8.360],
    [8.545,	8.555,	8.609,	8.875,	9.414,	9.917,	10.461,	12.872,	15.383,	16.076,	16.190,	16.137,	16.032,	15.720,	15.300,	14.794,	14.186,	13.249,	11.211,	9.964,	9.416,	8.856,	8.320],
    [8.540,	8.553,	8.545,	8.730,	9.388,	10.028,	10.652,	12.673,	15.286,	16.047,	16.199,	16.178,	16.101,	15.805,	15.324,	14.717,	13.951,	12.595,	10.837,	9.514,	8.967,	8.531,	8.039],
    [8.428,	8.311,	8.175,	8.525,	9.547,	10.376,	11.011,	12.638,	15.225,	16.103,	16.261,	16.257,	16.240,	16.013,	15.409,	14.449,	13.141,	11.702,	10.316,	9.062,	8.510,	8.119,	7.726],
    [8.176,	8.128,	8.009,	8.426,	9.773,	10.816,	11.516,	12.840,	15.129,	16.113,	16.369,	16.401,	16.359,	16.210,	15.610,	14.088,	12.244,	10.976,	9.802,	8.680,	8.191,	7.934,	7.677],
    [7.792,	7.953,	7.981,	8.435,	10.021,	11.348,	12.128,	13.559,	15.237,	16.098,	16.391,	16.418,	16.388,	16.323,	15.784,	14.005,	11.746,	10.354,	9.335,	8.522,	8.105,	7.854,	7.761]])    

    Tpvu15 = array([\
    [7.330,	7.543,	7.656,	8.020,	9.758,	11.278,	12.072,	13.499,	14.804,	15.551,	16.243,	16.418,	16.407,	16.297,	15.433,	12.926,	10.510,	9.463,	8.678,	8.010,	7.629,	7.349,	7.186],
    [7.012,	7.332,	7.528,	8.043,	9.898,	11.246,	12.069,	13.654,	14.849,	15.520,	16.246,	16.425,	16.417,	16.357,	15.611,	12.998,	10.379,	9.476,	8.669,	7.970,	7.540,	7.221,	7.007],
    [6.915,	7.090,	7.406,	8.044,	9.845,	11.055,	11.744,	13.210,	14.788,	15.686,	16.306,	16.434,	16.420,	16.309,	15.373,	12.502,	10.611,	9.855,	8.903,	8.056,	7.507,	7.081,	6.889],
    [7.091,	7.116,	7.382,	8.050,	9.630,	10.745,	11.320,	12.402,	14.476,	15.909,	16.395,	16.450,	16.414,	16.199,	15.037,	12.431,	11.235,	10.414,	9.265,	8.360,	7.709,	7.155,	6.976],
    [7.398,	7.383,	7.544,	8.101,	9.362,	10.291,	10.812,	11.746,	14.439,	16.005,	16.404,	16.462,	16.378,	15.917,	14.646,	13.164,	11.909,	10.972,	9.734,	8.757,	8.094,	7.534,	7.263],
    [7.554,	7.627,	7.763,	8.244,	9.137,	9.869,	10.401,	11.704,	14.488,	15.916,	16.276,	16.288,	16.139,	15.493,	14.821,	14.099,	13.168,	11.605,	10.204,	9.209,	8.698,	8.064,	7.568],
    [7.625,	7.777,	7.967,	8.327,	9.027,	9.578,	10.077,	11.835,	14.507,	15.785,	16.161,	16.143,	15.868,	15.282,	14.798,	14.329,	13.724,	12.523,	10.687,	9.626,	9.178,	8.479,	7.994],
    [7.895,	7.925,	8.034,	8.366,	8.962,	9.460,	9.938,	11.782,	14.464,	15.744,	16.159,	16.138,	15.893,	15.394,	14.915,	14.323,	13.616,	12.567,	10.728,	9.618,	9.091,	8.494,	7.925],
    [7.896,	7.947,	7.973,	8.208,	8.910,	9.570,	10.144,	11.656,	14.327,	15.698,	16.167,	16.178,	15.981,	15.449,	14.910,	14.189,	13.320,	11.869,	10.351,	9.114,	8.595,	8.156,	7.604],
    [7.889,	7.768,	7.643,	8.007,	9.061,	9.913,	10.530,	11.700,	14.122,	15.690,	16.229,	16.257,	16.158,	15.612,	14.825,	13.821,	12.388,	11.116,	9.805,	8.626,	8.126,	7.700,	7.219],
    [7.695,	7.656,	7.534,	7.926,	9.278,	10.353,	11.043,	12.096,	14.116,	15.648,	16.323,	16.401,	16.326,	15.849,	14.787,	13.315,	11.552,	10.469,	9.293,	8.213,	7.756,	7.476,	7.153],
    [7.400,	7.571,	7.577,	8.001,	9.528,	10.902,	11.604,	12.822,	14.490,	15.596,	16.290,	16.418,	16.386,	16.097,	14.960,	12.983,	11.097,	9.854,	8.845,	8.037,	7.636,	7.355,	7.228]])

    F = RegularGridInterpolator((bands, doys), Tpvu35.T, method='linear')
    z35 = F((lat, doy))
    F = RegularGridInterpolator((bands, doys), Tpvu30.T, method='linear')
    z30 = F((lat, doy))
    F = RegularGridInterpolator((bands, doys), Tpvu25.T, method='linear')
    z25 = F((lat, doy))
    F = RegularGridInterpolator((bands, doys), Tpvu20.T, method='linear')
    z20 = F((lat, doy))
    F = RegularGridInterpolator((bands, doys), Tpvu15.T, method='linear')
    z15 = F((lat, doy))
           
    z = [] 
    for k in range(0, len(lat)): 
        p = polyfit([1.5, 2.0, 2.5, 3.0, 3.5], [z15[k],z20[k],z25[k],z30[k],z35[k]], 1)
        z.append(polyval(p, pvu))
        
    return array(z)