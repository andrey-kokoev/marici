# Moving prolate placement and volume split into an exact source cocycle and an asymptotically natural boundary

## Objective

Resolve the first residual channel in the physical seam audit: the moving
ordered cutoff placement and its volume term.

## Exact source-derived volume coordinate

For the semilocal scaling von Neumann algebra, the canonical Plancherel trace
satisfies

\[
\tau_S(\lambda_S(g)^*\lambda_S(g))=\|g\|_2^2,
\qquad
\tau_S(\lambda_S(h))=h(1)
\]

for \(h=g*g^*\). Consequently the divergent term in Connes's cutoff formula is
not an arbitrary subtraction:

\[
2\log\Lambda\,h(1)
=
2\log\Lambda\,\tau_S(\lambda_S(h)).
\]

For logarithmic cutoff \(L=\log\Lambda\), define

\[
\mathcal V_L(h)=2L\tau_S(\lambda_S(h)).
\]

Then cutoff succession is an exact additive cocycle:

\[
\boxed{
\mathcal V_{L'}(h)-\mathcal V_L(h)
=2(L'-L)\tau_S(\lambda_S(h)).}
\]

and for \(L\le L'\le L''\),

\[
\mathcal V_{L''}-\mathcal V_L
=(\mathcal V_{L''}-\mathcal V_{L'})
 +(\mathcal V_{L'}-\mathcal V_L).
\]

Thus the volume coordinate has strict source-authorized \(k\)-dynamics. It is
an affine/cocycle coordinate, not a stationary vector coordinate.

## Exact transport of ordered placement

Characterwise, the physical-to-Hardy unitary \(\mathcal U_\chi\) transports

\[
P_\Lambda(Q_\Lambda^T-Q_\Lambda^0)A_g
\]

exactly to

\[
\Pi(Q_{L,\chi}^T-Q_L^0)M_{m_{g,\chi}}.
\]

The finite physical regulator is transported as the actual operator

\[
\widetilde Z=\mathcal U_\chi Z^{\rm physical}\mathcal U_\chi^*,
\]

without replacing it by a symmetric model cutoff or commuting it through the
observer. Unitary invariance gives equality of the finite regulated traces.
Hence presentation transport of the moving placement is exact at every finite
regulator.

## Recentered placement

Let

\[
U_L=M_{e^{2iLs}},
\qquad
\Delta Q_L=U_L\Delta Q_0U_L^*.
\]

Because Mellin observer multipliers commute with \(U_L\), cyclic transport
puts all cutoff motion into one left Hardy projection:

\[
\operatorname{Tr}(M_f\Pi\Delta Q_L)
=
\operatorname{Tr}(M_f\Pi_L^{\rm left}\Delta Q_0),
\qquad
\Pi_L^{\rm left}=U_L^*\Pi U_L.
\]

For the Connes orientation,

\[
\Pi_L^{\rm left}\xrightarrow{s}I.
\]

On the admitted observer core where

\[
T_f=M_f\Delta Q_0\in\mathcal S_1,
\]

strong convergence of the uniformly bounded projections implies

\[
\| (\Pi_L^{\rm left}-I)T_f\|_1\to0.
\]

Therefore

\[
\boxed{
\operatorname{Tr}(M_f\Pi\Delta Q_L)
\longrightarrow
\operatorname{Tr}(M_f\Delta Q_0).}
\]

The polarized two-observer statement follows identically for
\(M_{m_h}^*\Delta Q_0M_{m_g}\in\mathcal S_1\).

## Seam object

Retain the physical cutoff readout as the pair

\[
\mathcal P_L(h)=
\left(
\mathcal V_L(h),
\mathcal B_L(h)
\right),
\]

where \(\mathcal B_L\) is the ordered relative boundary trace. The successor
from \(L\) to \(L'\) is

\[
(\mathcal V_L,\mathcal B_L)
\longmapsto
\left(
\mathcal V_L+2(L'-L)\tau_S,
\mathcal B_{L'}
\right).
\]

The first coordinate is strictly cocyclic. The second is exactly transported
at finite regulator and converges in trace norm to the stationary relative
boundary. Hence it defines a strict morphism in the asymptotic quotient by
trace-norm-null families.

More explicitly, let two cutoff families be equivalent when their difference
tends to zero in the observer-localized trace norm. Then

\[
[\mathcal B_L]=[\mathcal B_\infty]
\]

and every cutoff-successor square commutes in that quotient. No prolate
eigenvalue asymptotic is used.

## Relation to the eight-leg realization

The ordered placement is not the triple compression
\(P\Delta Q_LP\). The exact eight-leg cross-polarized feature retains both
\(PA_g\) and \(A_g\), and its off-diagonal fundamental symmetry realizes the
symmetrized ordered product. With the transported finite regulator, unequal
left and right observer legs are retained exactly. Therefore the placement
channel has a typed positive dilation without suppressing its sewing block.

This supplies a realization of the placement, not positivity of the signed
finite part.

## Status change

The phrase “moving prolate placement/volume remains unconstructed” is too
coarse. The correct status is:

- **volume successor:** closed exactly as the Plancherel-trace cocycle;
- **finite regulated presentation transport:** closed exactly by \(\mathcal U_\chi\);
- **ordered placement seam:** closed on the trace-class observer core in the
  asymptotic quotient;
- **finite unregulated equality:** not asserted;
- **positivity:** not implied by relative subtraction.

## Remaining interface

To insert this result into the physical four-phase helix, the fourth
presentation must retain both the affine volume coordinate and the relative
boundary coordinate. Collapsing them prematurely to one finite-part scalar
erases the strict successor cocycle.

After this retyping, residual channel 1 is closed at the natural asymptotic
strength. The next independent residual is the prolate-to-Tate bulk-removal
intertwiner.

## Sources in the repository

- `the-semifinite-plancherel-trace-exactly-represents-the-volume-counterterm-but-the-relative-boundary-functional-is-not-automatically-positive.md`
- `exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md`
- `translation-covariance-makes-the-left-hardy-placement-converge-to-the-full-relative-projection-trace.md`
- `an-eight-leg-cross-polarized-positive-dilation-realizes-the-exact-left-cutoff-relative-product-placement.md`
