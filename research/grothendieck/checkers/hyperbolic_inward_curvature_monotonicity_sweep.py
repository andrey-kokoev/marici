"""Hostile test that normalized critical curvature increases inward from p=1."""

from __future__ import annotations

import math
import random

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature, state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative
from hyperbolic_unit_slope_limiting_family import critical as limiting_critical


def actual_curvature(epsilon: float, k: float) -> float:
    p, q = 1.0-epsilon, 1.0-(1.0+k)*epsilon
    left, right = 1e-8, 1.0
    while boundary_derivative(p,q,right)>0.0:right*=2.0
    for _ in range(45):
        midpoint=(left+right)/2.0
        if boundary_derivative(p,q,midpoint)>0.0:left=midpoint
        else:right=midpoint
    holding=(left+right)/2.0;t,r=state(p,q,holding)
    return -directional_curvature(t,r,p,q)/(p*p*(1.0-p*p)**2)


def main()->None:
    generator=random.Random(20260821);trials=3000;worst=(math.inf,None);failures=0
    for _ in range(trials):
        epsilon=10.0**generator.uniform(-5.0,-0.05)
        maximum_k=1.0/epsilon-1.0
        k=math.expm1(generator.random()*math.log1p(min(maximum_k,1000.0)))
        actual=actual_curvature(epsilon,k);limit=limiting_critical(k)[1];gap=actual-limit
        if gap<worst[0]:worst=(gap,(epsilon,k,actual,limit))
        if gap < -2e-5:failures+=1;break
    print(f"trials={trials}\nfailures_below_minus_2e_5={failures}\nminimum_gap={worst}")


if __name__=="__main__":main()
