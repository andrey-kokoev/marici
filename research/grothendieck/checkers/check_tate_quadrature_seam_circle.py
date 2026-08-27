#!/usr/bin/env python3
"""Numerical identity check for the exact local Tate seam circle."""

from math import cos, pi, sin, sqrt


for p in (2, 3, 5, 7, 11, 101):
    a = 1.0 / sqrt(p)
    for j in range(65):
        theta = 2.0 * pi * j / 64.0
        symmetric = 2.0 * (1.0 - a * cos(theta))
        odd_real = 2.0 * a * sin(theta)
        assert abs((symmetric - 2.0) ** 2 + odd_real**2 - 4.0 / p) < 1.0e-12
        assert symmetric >= 2.0 * (1.0 - a) > 0.0

print("seam_quadrature_orbit=(T-2)^2+B^2=4/p")
print("circle_center=(2,0)")
print("circle_radius=2/sqrt(p)")
print("origin_excluded_for_every_prime=true")
print("local_winding_about_origin=0")
