"""Directed sign certificate for the exact endpoint Taylor jet of G."""

from __future__ import annotations
from decimal import Decimal
from theta_inner_interval_certificate import I


def main()->None:
    x=I(Decimal("1.0986"),Decimal("1.0987"))
    p0=I.point(33)*x+I.point(280)
    p1=-I.point(209996)+I.point(10350)*x.power(2)+I.point(62895)*x
    p2=-I.point(27543774)*x+I.point(811269)*x.power(3)+I.point(3069306)*x.power(2)+I.point(39882098)
    p3=-I.point(1703144338)-I.point(589615995)*x.power(2)+I.point(14121972)*x.power(4)+I.point(22723668)*x.power(3)+I.point(1797386012)*x
    assert p0.lo>0 and p1.hi<0 and p2.lo>0 and p3.hi<0
    print(f"log3_bracket={x}")
    print(f"g0_shape={p0}")
    print(f"g1_negative_inner_shape={p1}")
    print(f"g2_shape={p2}")
    print(f"g3_negative_inner_shape={p3}")
    print("endpoint_taylor_jet_strictly_positive=True")


if __name__=="__main__":main()
