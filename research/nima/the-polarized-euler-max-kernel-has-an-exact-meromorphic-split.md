# The polarized Euler max kernel has an exact meromorphic split

The diagonal mismatch does not yet identify the missing finite return. The
correct next object is the polarized kernel.

For primitive exponents (a,b), define

[
T(a,b)=
sum_{n,mge1}
rac{e^{-rac12|log(n/m)|}}
{n^{1/2+a}m^{1/2+b}}.
]

Splitting the lattice along (nge m) and (mge n) gives the exact identity

[
T(a,b)
=
sum_{nge1}rac{H_n^{(b)}}{n^{1+a}}
+
sum_{nge1}rac{H_n^{(a)}}{n^{1+b}}
-
zeta(1+a+b).
]

Introduce the Euler–Maclaurin remainder

[
R_b(n)
=
H_n^{(b)}
-rac{n^{1-b}}{1-b}
-zeta(b)
-rac12n^{-b}.
]

Then direct substitution yields

[
egin{aligned}
T(a,b)
={}&
zeta(a+b)
left(
rac1{1-a}+rac1{1-b}
ight)\
&+zeta(b)zeta(1+a)
+zeta(a)zeta(1+b)\
&+sum_{nge1}rac{R_b(n)}{n^{1+a}}
+sum_{nge1}rac{R_a(n)}{n^{1+b}}.
end{aligned}
]

The two half-endpoint terms combine to (+zeta(1+a+b)) and cancel the
subtracted diagonal exactly. The remainder sums are locally normally
convergent near the open seam (a+b=1).

Consequently the polar coefficient is not determined by the diagonal alone:

[
operatorname*{Res}_{a+b=1}T(a,b)
=
rac1{1-a}+rac1{1-b}.
]

On the seam (b=1-a), this is

[
rac1a+rac1{1-a}
=
rac1{a(1-a)}.
]

At (a=b=1/2) it reduces to (4), recovering the previous diagonal
calculation.

## Consequence for the finite correction

The scalar discrepancy found on the diagonal fixes only

[
F(1/2,1/2),
]

where (F(a,b)) is the missing finite comparison kernel. It does not authorize
a scalar, rank-one, Todd, endpoint, or archimedean correction away from that
point.

The comparison cell must first match the complete polarized residue

[
rac{1}{a(1-a)}
]

along the seam, including its tangential dependence. Only after subtracting
that sourced polar family may one compare finite parts and ask whether the
remaining kernel is supplied by Todd, endpoint, or gamma data.

This produces a sharper falsifier: a proposed correction can reproduce the
number (0.2419315360) at the central diagonal while having the wrong
tangential derivatives. Such a correction is scalar-shadow correct but not a
polarized constructor.

The next calculation is therefore the normal finite part of the displayed
meromorphic split at fixed seam coordinate (a), followed by comparison with
the polarized quarter-heat/archimedean cell.
