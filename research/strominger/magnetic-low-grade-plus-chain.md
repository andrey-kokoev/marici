# The unresolved low-grade block is an aligned plus-polynomial chain

Write `q=g+d` with `d>0`.  Every positive-depth minus column begins at

\[
-g-a\le-g-2.
\]

Every plus column begins at `d-a>=-g-1`; when `m=0`, the `B0` coefficient
vanishes and the actual support begins one row later.
Thus the minus valuations are strictly separated from the plus sector.  In
any kernel relation, the lowest surviving row recursively forces every
positive-depth minus coefficient to vanish.

The depth-zero plus column has the private target row `q`; every positive-depth
plus column ends at or below `q-1`.  Its coefficient also vanishes.

Consequently the entire low-grade kernel question reduces to

\[
(0,-)
\quad+\quad
\text{positive-depth plus columns}.
\]

The obstruction inside that plus sector is source shortening.  For even
`a>=4`,

\[
\deg C_{g,a}=\min(g,a-4).
\]

In the range `4<=a<=g+4`, the magnetic degree is `a-3`.  Since the translated
support begins at `d-a`, its upper row is

\[
(d-a)+(a-3)=d-3,
\]

independent of `a`.  The coefficient at this common top contains the factor

\[
d-g-3.
\]

Hence a growing family of plus columns generically shares one upper endpoint.
On the divisor

\[
d=g+3,
\qquad q=2g+3,
\]

the entire top observation vanishes and every column drops coherently to row
`d-4`.  This is a presentation transition of the aligned chain.  In either
chart, common-endpoint alignment is why raw degree-one peeling stalls.

After reversing the exponent coordinate about `d-3`, these columns become
polynomials of strictly increasing degree with a common constant endpoint.
The missing elimination theorem is therefore specific:

\[
\boxed{
\text{construct the source-oriented finite-difference basis of the aligned
plus polynomials and compute its final two or three boundary responses.}
}
\]

This is narrower than a general banded-determinant problem.  The local
collision minors already computed are the expected terminal responses of
that basis change; what remains is to derive them from the complete aligned
chain.
