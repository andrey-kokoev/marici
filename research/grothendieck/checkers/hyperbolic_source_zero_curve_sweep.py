"""Hostile topology and monotonicity sweep of the source-selected G=0 curve."""

import json
import math

from hyperbolic_boundary_critical_curvature_sweep import state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


def critical_holding(p, q):
    lo, hi = 0.0, 1.0
    while boundary_derivative(p,q,hi)>0:
        hi*=2
    for _ in range(70):
        mid=(lo+hi)/2
        if boundary_derivative(p,q,mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def defect(p,q):
    a,b=math.atanh(p),math.atanh(q)
    return (p*(a-b)-math.log(math.cosh(a))+math.log(math.cosh(b)))/2


def g_at_x(p,q,x):
    t=math.tanh(x)
    r=math.tanh(p*x-defect(p,q))
    slope_sum,product=p+q,p*q
    nt=(4*t**3+2*t*product-2*t*(2+product)*r*r
        -slope_sum*r*(1-r*r))
    nr=(-t*slope_sum+2*(1-2*t*t-t*t*product)*r
        +3*t*slope_sum*r*r)
    return (1-t*t)*nt+p*(1-r*r)*nr


rows=[]
failures=[]
largest_linear_deviation=(0.0,None)
largest_rapidity_deviation=(0.0,None)
largest_bregman_deviation=(0.0,None)
for pi in range(1,100):
    p=pi/100
    endpoint_x=[]
    for q in (0.0,p):
        holding=critical_holding(p,q)
        t,_=state(p,q,holding)
        endpoint_x.append(math.atanh(t))
    xlo,xhi=sorted(endpoint_x)
    previous_q=None
    smallest_drop=math.inf
    maximum_roots=0
    for xi in range(101):
        x=xlo+(xhi-xlo)*xi/100
        brackets=[]
        previous_value=g_at_x(p,0.0,x)
        previous_coordinate=0.0
        for qi in range(1,401):
            q=p*qi/400
            value=g_at_x(p,q,x)
            if previous_value==0 or previous_value*value<0:
                brackets.append((previous_coordinate,q))
            previous_coordinate,previous_value=q,value
        roots=[]
        for lo,hi in brackets:
            sign=g_at_x(p,lo,x)
            for _ in range(60):
                mid=(lo+hi)/2
                if g_at_x(p,mid,x)*sign>0: lo=mid
                else: hi=mid
            roots.append((lo+hi)/2)
        maximum_roots=max(maximum_roots,len(roots))
        if len(roots)==1:
            qroot=roots[0]
            normalized=qroot/p
            deviation=normalized-(1-xi/100)
            if abs(deviation)>largest_linear_deviation[0]:
                largest_linear_deviation=(abs(deviation),(p,xi/100,normalized,deviation))
            rapidity=math.atanh(qroot)/math.atanh(p)
            rapidity_deviation=rapidity-(1-xi/100)
            if abs(rapidity_deviation)>largest_rapidity_deviation[0]:
                largest_rapidity_deviation=(abs(rapidity_deviation),(p,xi/100,rapidity,rapidity_deviation))
            defect0=defect(p,0.0)
            bregman=defect(p,qroot)/defect0 if defect0 else 0.0
            bregman_deviation=bregman-xi/100
            if abs(bregman_deviation)>largest_bregman_deviation[0]:
                largest_bregman_deviation=(abs(bregman_deviation),(p,xi/100,bregman,bregman_deviation))
            if previous_q is not None:
                smallest_drop=min(smallest_drop,previous_q-qroot)
            previous_q=qroot
        elif xi not in (0,100):
            failures.append((p,x,len(roots),roots))
    rows.append((p,xlo,xhi,maximum_roots,smallest_drop))

print(json.dumps({
    "p_slices":len(rows),
    "failure_count":len(failures),
    "first_failures":failures[:10],
    "maximum_q_roots":max(row[3] for row in rows),
    "smallest_discrete_q_drop":min(rows,key=lambda row:row[4]),
    "largest_deviation_from_normalized_line":largest_linear_deviation,
    "largest_deviation_in_rapidity_coordinate":largest_rapidity_deviation,
    "largest_deviation_in_bregman_coordinate":largest_bregman_deviation,
},indent=2))
