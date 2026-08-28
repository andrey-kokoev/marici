# The Quarter-Density Makes the Dilation Generator Skew but Restores the Infinite Raising Wall

Under

\[
y=e^{2u}-1,
\qquad
h=(1+y)^{1/4}\psi,
\]

the logarithmic generator becomes

\[
A=2(1+y)\partial_y+\frac12.
\]

The quarter-density is exact: with measure

\[
d\nu=\frac12(1+y)^{-1/2}dy,
\]

`A` is skew modulo the seam evaluation boundary. But on
`e_j=y^j exp(-lambda y)` it acts as

\[
A e_j
=2j e_{j-1}
+\left(2j-2\lambda+\frac12\right)e_j
-2\lambda e_{j+1}.
\]

Thus every finite top grade leaks outward. The positive three-state theta
packet immediately generates degree three, and adjoining it generates degree
four indefinitely. The coordinate rotation moved the infinite raising wall;
it did not eliminate it.

Research packet:
`research/grothendieck/the-quarter-density-makes-the-dilation-generator-skew-but-restores-the-infinite-raising-wall.md`

Checker:
`research/grothendieck/checkers/check_transported_dilation_jordan_raising_wall.py`

The checker passes 5/5 gates.
