import numpy as np
import math

def chi_square_fit(x1, y1, err1):
    
    def f(g):
        return math.log(g)
    def h(yi,j):
        return math.sqrt(math.log(yi))*j
    
    f1 = np.vectorize(f)
    f2 = np.vectorize(f)
    h1 = np.vectorize(h)
    
    x = f1(x1)
    y = f2(y1)
    err = h1(y1, err1)
    
    n = len(x)
    if n < 2 :
        print ('Error! Need at least 2 data points!')
        exit()
    S = np.sum(1/err**2)
    if abs(S) < 0.00001 :
        print ('Error! Denominator S is too small!')
        exit()
    S_x = np.sum(x/err**2)
    S_y = np.sum(y/err**2)
    t = (x - S_x/S) / err
    S_tt = np.sum(t**2)
    if abs(S_tt) < 0.00001 :
        print ('Error! Denominator S is too small!')
        exit()
    b = np.sum(t*y/err) / S_tt
    a = (S_y - S_x * b) / S
    sigma_a2 = (1 + S_x**2/S/S_tt) / S
    sigma_b2 = 1/S_tt
    if sigma_a2 < 0.0 or sigma_b2 < 0.0 :
        print ('Error! About to pass a negative to sqrt')
        exit()
    sigma_a = np.sqrt(sigma_a2)
    sigma_b = np.sqrt(sigma_b2)
    chi_square = np.sum(((y - a - b*x) / err)**2)
    return(a, b, sigma_a, sigma_b, chi_square)

