# Bilateral Clark sewing reduces the tail-flow defect from two lines to one

Status: exact defect identification; arithmetic repair positivity remains open

Nima's faithful tail feature

\[
 G(q,z)=e^{-(1/2+iz)q}\int_q^\infty\phi(v)e^{izv}dv
\]

and positive forcing

\[
 f(q)=e^{-q/2}\phi(q)>0
\]

obey the exact Green identity

\[
 \begin{aligned}
 i(\bar w-z)\int_0^\infty G(q,z)\overline{G(q,w)}dq
 ={}&\int_0^\infty(G(q,z)+f(q))
 \overline{(G(q,w)+f(q))}dq\\
 &-\|f\|_2^2-G(0,z)\overline{G(0,w)}.                \tag{1}
 \end{aligned}
\]

Thus the continuous scale flow is a positive bulk with two complex rank-one
defect channels.

## Agreement with the finite-tail obstruction

The earlier finite canonical compression found a real rank-four connection
defect and required at least two auxiliary symplectic pairs.  Equation (1)
explains that rank count:

\[
 \boxed{
 2\text{ complex defect lines}=4\text{ real symplectic directions}.
 }                                                     \tag{2}
\]

Compressing them to the vanishing tail moments `C,D` produced the invariant
terminal pole.  Retaining the complete function `G(q,z)` keeps both defect
lines regular.  The finite no-go and the continuous Green identity therefore
describe the same obstruction at different resolutions.

## Clark differential identifies the seam feature

Let

\[
 \mathcal C_a=1+ia\partial_z.
\]

At the modular seam,

\[
 G(0,z)=\int_0^\infty\phi(v)e^{izv}dv,                \tag{3}
\]

and hence

\[
 \boxed{
 \mathcal C_aG(0,z)
 =\int_0^\infty(1-av)\phi(v)e^{izv}dv
 =H_{1,a}(z).
 }                                                     \tag{4}
\]

The seam defect is therefore exactly the primitive `n=1` signed Clark
feature already isolated by the arithmetic commutator decomposition.  It is
not a new boundary artifact.

## Reflection cancels the primitive norm line

The second Clark chamber is obtained by `z -> -z` with the reflected fold
orientation.  The de Branges current is the antisymmetric comparison of the
two chamber outputs.  The defect

\[
 -\|f\|_2^2                                            \tag{5}
\]

is independent of both spectral arguments.  The Clark differential leaves a
constant kernel unchanged, and the same line occurs in the reflected chamber.
Consequently it cancels identically in the chamber antisymmetrization.

Thus, before arithmetic sampling introduces any further polarization, the
two-line continuous defect descends to

\[
 \boxed{
 \text{one complex seam line carried by }H_{1,a}.
 }                                                     \tag{6}
\]

This cancellation must be implemented at the denominator-free kernel level;
dividing by a chamber transform before subtraction can turn the common
constant line into spurious poles.

## Exact remaining architecture

The arithmetic commutator theorem gives

\[
 (1-au)\Phi
 =\sum_{n\ge1}S_n[(1-au)\phi_1]
 +a\sum_{n\ge2}\log n\,S_n\phi_1.                   \tag{7}
\]

Equation (4) identifies the first term's primitive generator with the sole
surviving Green defect.  The second term is the forced positive logarithmic
cocycle.  Therefore the desired proof has become

\[
 \boxed{
 \text{positive tail-flow bulk}
 +\text{positive arithmetic cocycle}
 -\text{one primitive seam line}
 \ge0.
 }                                                     \tag{8}
\]

The prime-two analogy is now exact in rank: after the automatic reflection
cancellation, there is one unstable complex channel and one source-derived
repair hierarchy.

## Scope and next falsifier

Equation (6) concerns the explicit defect lines in (1).  Applying
`C_a` to the full Green identity also differentiates the spectral factor
`bar(w)-z` and the bulk features; those induced terms must be retained in the
final calculation.  No claim is made that (8) is already a proved positive
identity.

The next exact calculation is to perform the two-variable Clark differential
and reflection antisymmetrization on (1), then sample only the completed tail
features at `q=log n`.  The mechanism is falsified if this operation creates
an additional independent negative channel or if the logarithmic cocycle
fails to dominate the single seam line.
