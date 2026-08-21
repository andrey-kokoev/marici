"""Directed point profile for the implicit critical graph in the tail chart."""

from __future__ import annotations
from decimal import Decimal
from hyperbolic_limiting_tail_certificate import I,evaluate


def root(z:Decimal)->Decimal:
    left,right=Decimal("0.45"),Decimal("0.85")
    for _ in range(90):
        middle=(left+right)/2;q=evaluate(I.point(z),I.point(middle))[0].v
        if q.lo>0:left=middle
        else:right=middle
    return (left+right)/2


def geometry(z:Decimal)->tuple[Decimal,I,I]:
    holding=root(z);q=evaluate(I.point(z),I.point(holding))[0]
    slope=-q.z/q.l
    curvature=-(q.zz+I.point(2)*q.zl*slope+q.ll*slope*slope)/q.l
    return holding,slope,curvature


def main()->None:
    slope_lo=slope_hi=curvature_lo=curvature_hi=None
    for index in range(19):
        z=Decimal("0.09")*Decimal(index)/Decimal(18);holding,slope,curvature=geometry(z)
        slope_lo=slope.lo if slope_lo is None else min(slope_lo,slope.lo);slope_hi=slope.hi if slope_hi is None else max(slope_hi,slope.hi)
        curvature_lo=curvature.lo if curvature_lo is None else min(curvature_lo,curvature.lo);curvature_hi=curvature.hi if curvature_hi is None else max(curvature_hi,curvature.hi)
        print(z,holding,slope,curvature)
    print(f"slope_range=({slope_lo},{slope_hi})")
    print(f"curvature_range=({curvature_lo},{curvature_hi})")


if __name__=="__main__":main()
