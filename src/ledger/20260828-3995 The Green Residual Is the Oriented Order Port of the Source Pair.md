# Scope Correction: The Green Residual Is an Autocorrelation Separation Port

Ledger entry 3995 originally misclassified the signed Green residual as an
independent oriented-order port. The exact identity

\[
\operatorname{sgn}(x)\sinh(zx)=\sinh(z|x|)
\]

shows instead that

\[
K_f(z)=2\int_0^\infty A_f(x)\sinh(zx)\,dx,
\qquad
A_f(x)=\int_0^\infty f(q)f(q+x)\,dq.
\]

Thus the full one-sided autocorrelation reconstructs \(K_f\) exactly. The
residual is a separation port, not an exchange-odd orientation port.

The correct exchange-odd candidate needs two independently typed histories:

\[
L_{f,g}(z)=\iint f(q)g(v)\sinh\!\bigl(z(v-q)\bigr)\,dq\,dv,
\]

with \(L_{g,f}=-L_{f,g}\) and \(L_{f,f}=0\). Its relevance depends on deriving
both histories from the theta source rather than introducing them to fit the
desired antisymmetry.

Artifact:

- research/grothendieck/the-green-residual-is-the-oriented-order-port-of-the-source-pair.md
# The Green Residual Is the Oriented Order Port of the Source Pair

Grothendieck identified the mixed smoothed Green residual as genuinely new
relational information.

For the half-line source (f),

\[
\mathcal K(z)
=\int\!\!\int
f(q)f(v)\operatorname{sgn}(v-q)
\sinh(z(v-q)),dq,dv.
\]

The inserted order sign records which source point comes first. Without it,
the full-plane odd separation transform vanishes by swap symmetry. Thus the
ordinary unordered autocorrelation and its self-adjoint Hankel realization
cannot reconstruct this port.

For real (z), positivity of the source fixes the sign of
(mathcal K(z)). For complex (z), the oscillatory cosine factor can reverse
that orientation.

The mixed residual is therefore the first genuinely new port after static
saturation, but it remains diagnostic until reciprocal modular sewing links
scalar nullity to its ordered orientation.

Artifact:

- research/grothendieck/the-green-residual-is-the-oriented-order-port-of-the-source-pair.md

Falsifier:

- a positive reciprocal source with the same declared scalar completion and
  an off-seam zero whose order port has the forbidden orientation.
