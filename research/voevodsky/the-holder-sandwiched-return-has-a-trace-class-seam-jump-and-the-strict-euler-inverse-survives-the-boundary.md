# The Holder sandwiched return has a trace-class seam jump and the strict Euler inverse survives the boundary

Let `A` be the translation generator and let

\[
R(z)=B^\dagger(A-z)^{-1}B.
\]

The incidence calculation gives a trace-class-valued spectral density

\[
G(\lambda)=\beta(\lambda)^*\beta(\lambda)
\]

which is locally Holder continuous of every order below `1/2` and integrable
with the source weight.  Vector-valued Plemelj theory therefore yields
trace-norm boundary values

\[
R_\pm(\lambda)
=\operatorname{PV}\int
\frac{G(\xi)}{i\xi-i\lambda}\,d\xi
\;\mathbin{\pm}\;\text{the convention-fixed }\pi G(\lambda)
\]

for every real `lambda` in the declared chart.  In convention-independent
form, the two boundary values have a finite-rank/trace-class jump equal to
`2 pi` times `G(lambda)`, with the factor `i` determined by whether the
resolvent is written for `partial_q`, `-i partial_q`, or the centered skew
coordinate.

The arithmetic Schur atom remains strictly contractive on the seam:

\[
S_p(\lambda)=p^{-1/2}e^{i(\log p)\lambda},
\qquad |S_p(\lambda)|=p^{-1/2}\le2^{-1/2}.
\]

Consequently

\[
\|(I-L(\lambda))^{-1}\|
\le(1-2^{-1/2})^{-1}
\]

also on the boundary.  Therefore

\[
K_\pm(\lambda)=(I-L(\lambda))^{-1}R_\pm(\lambda)
\]

is trace class and locally trace-norm continuous on the seam, and its Fredholm
determinant has two well-defined boundary values.

This corrects the earlier claim that the Euler inverse necessarily loses its
strict bound at the seam.  What remains is not existence of the boundary
operator, but selection of the physical Green side/sign, compatibility of the
two boundary determinant frames, and comparison with the Xi determinant line.
