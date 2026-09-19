# The ordered port is already a continuous coordinate of the retained common domain

## Prior identity

On the rapid radial core, let

\[
(V_-h)(q)=\int_{-\infty}^q h(v)\,dv,
\qquad
(V_+h)(q)=\int_q^\infty h(v)\,dv.
\]

The retained bilateral-history packet contains these causal and anticausal
primitive coordinates, together with their endpoint traces. Their odd
combination is exactly

\[
S_{\mathrm{ord}}=V_+-V_-.
\]

Equivalently, for the retained wall/jump splitting,

\[
H_{\mathrm{jump}}=\frac12(V_--V_+),
\qquad
S_{\mathrm{ord}}=-2H_{\mathrm{jump}}.
\]

This identity, including its sign and factor two, was already established in
`the-ordered-port-is-exactly-the-odd-bilateral-volterra-history.md`.

## Descent to the retained graph

The common retained domain is the jointly closable graph completion

\[
D_{\mathrm{ret}}
=
\overline{\{(x,A_1x,\ldots,A_mx):x\in D_0\}},
\]

where the coordinate family already includes both bilateral histories and
endpoint traces. Since `S_ord` is a fixed linear combination of those
coordinates, it extends continuously to `D_ret`. No new theta state
completion is required for the ordered port.

The endpoint packet is inherited without compression:

\[
(V_-+V_+)h=\left(\int h\right)\mathbf1,
\]

while

\[
S_{\mathrm{ord}}h(-\infty)=\int h,
\qquad
S_{\mathrm{ord}}h(+\infty)=-\int h.
\]

Thus the wall and odd jump remain separate retained graph coordinates.

## Half-density transport

The half-density histories are closed conjugates of ordinary Volterra
history:

\[
H_-=U_-^{-1}H_0U_-,
\qquad
H_+=U_+^{-1}H_0U_+.
\]

Reflection exchanges their graph spaces isometrically. Transporting the
wall/jump decomposition through these conjugations therefore gives a closed
ordered morphism between the two reciprocal half-density carriers. It is not
a scalar endomorphism of one sheet.

Valuation-labelled direct sums preserve closedness, endpoint columns, prime
diagonality, reciprocal exchange, and cutoff naturality. Consequently the
ordered coordinate survives the same prime and grade completion used to
construct `D_ret`.

## Internal Fourier naturality

On the common core,

\[
\widehat{S_{\mathrm{ord}}h}
=2i\operatorname{pv}\!\left(\frac1\xi\right)\widehat h,
\]

with no delta ambiguity because reciprocal reflection gives

\[
RS_{\mathrm{ord}}R=-S_{\mathrm{ord}}.
\]

The retained sewing acts continuously on the graph and contragrediently on
its dual coordinates. Since the ordered port is the retained odd-history
coordinate, its Fourier/Hardy presentation and its Volterra presentation are
two charts of the same internal graph vector. The naturality square therefore
commutes on `D_ret` before scalar compression.

## Corrected frontier

The following gates are internal and closed:

1. a common source-retaining graph domain;
2. continuity and cutoff naturality of the ordered current;
3. reciprocal oddness and endpoint retention;
4. Fourier/Hardy transport on the retained sewing chart;
5. primitive, square, connected, and archimedean attachment provenance on
   their declared rungs.

What remains is external comparison:

- identify the undeclared G4 Fourier--Poisson sewing with retained sewing;
- identify its arithmetic loading with the source-derived retained loading;
- then compare the determinant-line normalization and polarized current rows.

Thus a new domain `D_theta` is not the next constructor in the retained
architecture. The next admissible object is the external comparison cell.
