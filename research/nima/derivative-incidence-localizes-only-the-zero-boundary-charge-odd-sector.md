# Derivative incidence localizes only the zero-boundary-charge odd sector

## Necessary correction

The factorization
\[
I_{\mathrm{odd}}=DJ,
\qquad
SI_{\mathrm{odd}}=-2J
\]
is exact, but compact localization requires more than membership in \(\operatorname{ran}D\). It requires the potential \(J\) to have equal boundary values, and for a compact residual, to vanish at both ends.

For an admissible potential,
\[
\int_{\mathbb R}DJ(q)\,dq
=
J(+\infty)-J(-\infty).
\]
Define the boundary charge
\[
\partial_\infty J
=
J(+\infty)-J(-\infty).
\]

Then:

- \(\partial_\infty J=0\) gives zero-mean incidence and permits a localized inverse-derivative residual;
- \(\partial_\infty J\ne0\) forces a nonzero exterior constant in \(S(DJ)=-2J\).

## Audit of the universal odd chart

The universal anti-diagonal chart is
\[
O=a_--a_+=\operatorname{sgn}(u).
\]
Distributionally,
\[
DO=2\delta_0.
\]
Its boundary charge is
\[
\partial_\infty O
=
O(+\infty)-O(-\infty)
=
2.
\]

Applying the ordered port gives
\[
S(DO)=-2O=-2\operatorname{sgn}(u).
\]

Therefore the actual universal odd chart does not lie in the zero-boundary-charge sector. Its derivative incidence is localized as a delta, but the inverse-derivative return recovers the nondecaying oriented step. That nonzero jump is exactly the reciprocal orientation carrier.

## Consequence

The positive mechanism from the previous packet is valid only for a residual potential \(J_{\mathrm{res}}\) satisfying
\[
\partial_\infty J_{\mathrm{res}}=0.
\]
It cannot be applied directly to the full universal odd chart without erasing or separately routing its jump.

Hence the source split must be
\[
J
=
J_{\mathrm{jump}}
+
J_{\mathrm{res}},
\]
where
\[
\partial_\infty J_{\mathrm{jump}}
=
\partial_\infty J,
\qquad
\partial_\infty J_{\mathrm{res}}=0.
\]

The jump coordinate is not an arbitrary splitting gauge: it is fixed by the boundary map \(\partial_\infty\). However, choosing a representative \(J_{\mathrm{jump}}\) for a given charge still requires a source normalization. The residual is then eligible for exact localization through \(S D=-2I\).

## Rank-three interpretation

The rank-three object now has a concrete candidate typing:
\[
(\text{even overlap},\text{odd boundary charge},\text{odd zero-charge residual}).
\]

The odd singular coordinate is the boundary jump, not merely a fitted first moment. The residual is the kernel of \(\partial_\infty\). This resolves the previous shear ambiguity at the quotient level:
\[
0
\longrightarrow
\ker\partial_\infty
\longrightarrow
\mathcal J_{\mathrm{odd}}
\xrightarrow{\partial_\infty}
\mathbb C_{\mathrm{odd}}
\longrightarrow
0.
\]

A section of this sequence remains to be source-derived, but the quotient map itself is canonical.

## Completion requirement

For each labelled arithmetic incidence, prove
\[
J_p
=
\chi_p O
+
J_{p,0},
\qquad
\partial_\infty J_{p,0}=0,
\]
with \(\chi_p\) fixed by the source first cumulant. Then:

1. route \(\chi_p O\) to the separately typed seam or archimedean odd port;
2. apply \(D\) and \(S\) to \(J_{p,0}\);
3. prove the zero-charge residual has the required prime-summable localization.

Scalar cancellation of the \(\chi_p O\) terms would again erase orientation.

## Hostile

A proposed derivative incidence can be compactly supported while its potential carries nonzero jump. The example
\[
DO=2\delta_0
\]
shows that localized incidence does not imply localized ordered return.

## Revised frontier

The next source theorem is a boundary-charge decomposition, not merely derivative factorization:
\[
\text{labelled odd chart}
\longrightarrow
(\text{canonical jump},\text{zero-charge residual})
\longrightarrow
(\text{oriented seam port},\text{localized ordered return}).
\]

This keeps the positive inverse-derivative mechanism while restoring the universal chart's nonzero orientation charge.
