# Correction: the centered joint cut column has a bounded common mode, not an unbounded outgoing wall column

## Defect found by independent reread

Two recent diagnostics treated the seam component

\[
h_a(t)=\mathbf1_{0\le t\le a}\Phi(a-t)
\]

as an isolated vector in one fixed uncentered history coordinate. That is not
the source-authorized completed column. The retained construction uses the
joint tail--seam atom, translated graph weights, reciprocal orientations, and
the centered seam identification before all-prime synthesis.

The existing weighted-adjoint theorem gives the actual decomposition

\[
b_p=p^{-1/2}\Phi+r_p,
\qquad
r_p=-p^{-1/2}\Phi\mathbf1_{(\log p,\infty)}
\]

in the common centered history carrier, with the seam endpoint retained as a
separate boundary port.

## Bounded common mode

The common primitive synthesis functional is

\[
\ell_{\rm prim}(x)
=
\sum_pp^{-1/2}x_p.
\]

On

\[
\|x\|_U^2
=
\sum_p(\log p)|x_p|^2,
\]

its dual norm is finite:

\[
\|\ell_{\rm prim}\|^2
=
\sum_p\frac1{p\log p}<\infty.
\]

Thus the common-mode incidence

\[
x\longmapsto\Phi\ell_{\rm prim}(x)
\]

is bounded rank one.

The residual synthesis is Hilbert--Schmidt because theta tail decay gives

\[
\sum_p\frac{\|r_p\|_{\mathcal H}^2}{\log p}<\infty.
\]

Therefore the complete centered incidence is bounded and has no outgoing wall
column with coefficients \(1/\log p\).

## Why the uncentered calculation failed

Pairing only \(h_a\) with the growing representative \(H_-\Phi\) produces an
\(e^{a/2}\) term. In the completed constructor this is not a standalone mixed
block. The other cut channel, translated exponential conjugator, endpoint wall
port, and reciprocal orientation participate in the relative Green pairing.

Dropping those components before pairing destroys the source joint graph and
manufactures a non-summable column. The calculation is valid only as a
falsifier for that isolated uncentered seam component, not as an audit of the
completed G4 incidence.

## Limiting-absorption correction

The polynomial graph weight is translated with each label before direct-sum
assembly. Labelwise histories are isometric copies of one centered seam pair.
Consequently the estimate

\[
\|u_{\log p}\|_{L^2_\sigma}
\asymp(\log p)^\sigma
\]

in one fixed uncentered coordinate is not the norm used by the retained
carrier.

The previously claimed incompatibility between \(\sigma<1/2\) and the
standard \(\sigma>1/2\) limiting-absorption threshold therefore does not apply
to the centered translated-weight graph. A seam boundary theorem remains
open, but this endpoint argument does not obstruct it.

## Determinant-line correction

Because the formal \(1/\log p\) wall packet was an artifact of the incomplete
pairing, it cannot be identified with the primitive determinant anomaly. The
primitive anomaly continues to come from the degree-one Euler cumulant and
its endpoint coboundary. Any comparison between trace subtraction and that
anomaly still requires an explicit source map.

## Restored status

Restored:

- bounded common primitive incidence on the seam-length coefficient space;
- Hilbert--Schmidt residual incidence;
- trace-class centered boundary returns through bounded propagators;
- eligibility of the mixed theta/arithmetic block for a centered seam theorem.

Still open:

- the actual limiting-absorption or relative boundary-value theorem;
- the complement-energy transfer estimate (the unweighted range angle is zero);
- determinant-line descent;
- the identity \(F_\theta=E_\theta\tau\);
- kernel-state and multiplicity preservation.

## Disposition

The uncentered outgoing-growth obstruction and its derived unbounded wall
cocycle are withdrawn for the completed joint cut constructor. They remain
warnings against isolating one seam component before centered reciprocal
assembly. No RH conclusion is authorized.
