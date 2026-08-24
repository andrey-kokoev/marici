"""Fit and hostile-test a polynomial predictor for the compact root sheet."""

import json
import math
import numpy as np

from hyperbolic_boundary_unimodality_sweep import boundary_derivative


U0,U1=math.log(5),math.log(10)
DEGREE=4
POWERS=[(i,j) for i in range(DEGREE+1) for j in range(DEGREE+1-i)]


def root_m(u,c):
    p=math.exp(-u);q=c*p
    lo,hi=0.0,1.0
    while boundary_derivative(p,q,hi)>0:hi*=2
    for _ in range(65):
        mid=(lo+hi)/2
        if boundary_derivative(p,q,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2-2*u


def row(x,c):return [x**i*c**j for i,j in POWERS]


matrix=[];values=[]
for ui in range(41):
    x=ui/40;u=U0+(U1-U0)*x
    for ci in range(41):
        c=ci/40
        matrix.append(row(x,c));values.append(root_m(u,c))
coefficients=np.linalg.lstsq(np.asarray(matrix),np.asarray(values),rcond=None)[0]

largest=(0.0,None)
for ui in range(201):
    x=ui/200;u=U0+(U1-U0)*x
    for ci in range(201):
        c=ci/200
        actual=root_m(u,c)
        predicted=sum(coefficient*term for coefficient,term in zip(coefficients,row(x,c)))
        residual=actual-predicted
        if abs(residual)>largest[0]:largest=(abs(residual),(x,c,actual,predicted,residual))

print(json.dumps({
    "degree":DEGREE,
    "powers":POWERS,
    "coefficients":[float(value) for value in coefficients],
    "validation_grid":[201,201],
    "largest_absolute_residual":largest,
},indent=2))
