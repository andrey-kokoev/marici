# Two calibrated momentum ports reconstruct the finite boundary response: WP770

## Question

Can the finite-energy response fiber of WP769 be removed by an
experimentally typed probe family rather than by declaring boundary kinetic
terms absent?

## Response coordinate

At fixed calibrated (m=\ell=1), the complete quadratic boundary dependence
enters through

\[
s=r_0+r_L,
\qquad
t=r_0r_L.
\]

For a spacelike momentum magnitude (p), define

\[
\mu=\sqrt{1+p^2}
\]

and subtract the known bulk inverse response:

\[
Y(p)=G(p)^{-1}-\mu\sinh\mu.
\]

Then

\[
Y(p)=p^2\cosh\mu\,s
+\frac{p^4\sinh\mu}{\mu}\,t.
\]

This is a detector-calibrated linear response in the two invariants that
actually affect boundary-to-boundary propagation.

## Minimal port rank

One momentum supplies one row and leaves an affine fiber. For (p_1=1), let
(A_1) and (B_1) denote the two response coefficients. The packets

\[
(s,t)=(2,1)
\]

and

\[
(s,t)=\left(2+B_1/A_1,0\right)
\]

have exactly the same first response.

Adding (p_2=2) gives the response matrix

\[
J=
\begin{pmatrix}
A_1&B_1\\
A_2&B_2
\end{pmatrix}.
\]

Its determinant is nonzero. The two ports therefore reconstruct (s) and
(t) exactly. They determine the unordered endpoint pair as the roots of

\[
z^2-sz+t=0.
\]

No labelled-endpoint ontology is inferred, and none is needed for the
symmetric transfer function.

## Instrument typing

The admitted experiment injects the source-defined boundary current at two
independently calibrated spacelike momentum magnitudes and records the
amplitude and phase of the opposite-boundary response in the same detector
units. The momentum and amplitude standards are reference ports. They define
a new relational experiment; they do not reveal absolute boundary
coefficients outside it.

This supplies a jointly faithful formal instrument on the quadratic boundary
response packet. It does not yet prove that the actual flavor production and
decay channels realize the two ports with a nonsingular uncertainty-completed
Jacobian.

## Classification

WP770 repairs WP769's finite-readout kernel conditionally: two calibrated
momentum ports reconstruct every response-relevant boundary coefficient. It
is a readout, not a selector. The source must still fix (m\ell), the gauge
normalization, and an isolated RG trajectory, after which the transfer
observables must descend to `physical16` and survive detector uncertainty.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp770_two_momentum_boundary_response_tomography.py

Generated result:
research/flavor/results/wp770_two_momentum_boundary_response_tomography.json
