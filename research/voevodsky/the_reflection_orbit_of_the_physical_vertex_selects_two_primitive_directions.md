# The reflection orbit of the physical vertex selects two primitive directions

## Question

How much of the primitive pyramid is selected by transporting the anchored physical \(e_6\) vertex through the constructed fixed-pencil reflection?

## Claim boundary

This packet computes the integral orbit lattice. It does not identify the reflection-odd orbit direction with \(v_{\rm alg}\).

## Orbit of the anchor

Choose the physical infinity component difference as

\[
d_1=(1,1,1)
\]

in the primitive frame \((\alpha_{12},\alpha_{13},\alpha_{14})\). The global \(b\)-reflection acts by

\[
r_b=\operatorname{diag}(1,-1,-1),
\]

so

\[
r_b(d_1)=d_2=(1,-1,-1).
\]

The normalized orbit sum and difference are integral:

\[
\frac{d_1+d_2}{2}=\alpha_{12},
\qquad
\frac{d_1-d_2}{2}=
\alpha_{13}+\alpha_{14}.
\]

They are orthogonal and have squares

\[
\alpha_{12}^2=-2,
\qquad
(\alpha_{13}+\alpha_{14})^2=-4.
\]

Thus the physical anchor and its reflected image select a primitive rank-two sublattice

\[
L_{\rm orbit}
=
\mathbb Z\alpha_{12}
\oplus
\mathbb Z(\alpha_{13}+\alpha_{14}).
\]

## Remaining direction

The unique primitive line not contained in the rational span of the orbit is

\[
eta_\perp=\alpha_{13}-\alpha_{14}.
\]

It is also reflection-odd and has square \(-4\). Hence the \(b\)-reflection character alone cannot distinguish the orbit-odd direction

\[
eta_{\rm orbit}=
\alpha_{13}+\alpha_{14}
\]

from the transverse odd direction \(\beta_\perp\).

The three vectors

\[
\alpha_{12},
\quadeta_{\rm orbit},
\quadeta_\perp
\]

generate an index-two sublattice of \(A_1^3\). Equivalently, recovering \(\alpha_{13}\) and \(\alpha_{14}\) separately requires a parity choice beyond the reflected anchor orbit.

## Role in the flow

The established information flow is now

\[
d_1
\xrightarrow{r_b}
d_2
\xrightarrow{\text{half-sum/half-difference}}
\bigl(
\alpha_{12},
\beta_{\rm orbit}
\bigr).
\]

This supplies one invariant and one odd primitive direction. If the physical response plane \(\langle e_6,v_{\rm alg}\rangle\) is the orbit plane, then \(v_{\rm alg}\) must be proportional to \(\beta_{\rm orbit}\) modulo the anchored coordinate. If it is not, the missing component lies along \(\beta_\perp\).

A single period evaluation on \(r_b(d_1)\), expressed in the \((e_6,v_{\rm alg})\) frame, distinguishes these cases.

## Disposition

The global reflection transports the physical vertex far enough to select a canonical rank-two orbit plane. The remaining comparison is reduced to one test: compute the marked period column of the reflected physical component difference and check whether its \(v_{\rm alg}\) coordinate is nonzero. No full four-vertex Picard matrix is required for that decision.

Verification:

- `research/voevodsky/checkers/check_reflected_physical_vertex_orbit.py`
- `research/voevodsky/results/reflected_physical_vertex_orbit.json`
