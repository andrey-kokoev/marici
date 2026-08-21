# 1329 — Kummer-Resolved Affine IBP First Closes at Quadratic Primitive Degree

> **RETRACTED.** The degree-two consistency occurred only at modular rank-drop fibers over \(\mathbf F_{1009}\) and \(\mathbf F_{1013}\). A later generic-rank scan found full rank 961 and inconsistency at three fibers over \(\mathbf F_{1019}\), with independent confirmation over \(\mathbf F_{1021}\). The claimed affine closure is not a characteristic-zero candidate. Retained as provenance; see the next correction entry.

## Question

Entries 1320 and 1326 allowed only primitives pulled back from the scalar base. The five-site form itself occupies all 32 Kummer characters. Test instead

\[
V_i
=
\sum_{S\subseteq\{1,\ldots,5\}}
P_{i,S}(u)\,y_S,
\qquad
y_S=\prod_{e\in S}y_e,
\]

in

\[
\partial_z\Omega+a(z)\Omega
=
\sum_i\partial_{u_i}(V_i\Omega).
\]

All labelled characters are retained independently.

## Full-deck result

At both

\[
(p,z)=(1009,7),\qquad(1013,11),
\]

the exact finite-field systems give

\[
\begin{array}{c|c|c}
\deg P_{i,S} & \text{unknowns} & \text{status}\\
\hline
0 & 97 & \text{inconsistent}\\
1 & 385 & \text{inconsistent}\\
2 & 961 & \text{consistent}.
\end{array}
\]

At degree two the consistency remains after setting \(a(z)=0\):

\[
\boxed{
\partial_z\Omega
=
d_u\Xi^{(2)}_{\rm Kum}
}
\]

on the affine Kummer cover.

The degree-two ranks are 800 and 768 at the two specialized fibers. The nonuniqueness is expected: the affine primitive has a large exact/gauge kernel.

## Meaning

Occurrence resolution is mathematically active. A scalar-base primitive does not close through degree five, whereas the complete Kummer-character primitive closes already at quadratic degree.

But this is not yet a physical period identity. Since

\[
\partial_z\Pi(z)\ne0,
\]

the affine primitive must have a nonzero image in the relative boundary complex:

\[
\operatorname{Res}_{\infty}(\Xi^{(2)}_{\rm Kum})\ne0
\]

or an equivalent supported boundary contribution.

Thus the surviving architecture is

\[
\boxed{
\text{affine Kummer exactness}
+
\text{projective supported obstruction}
=
\text{physical Gauss--Manin variation}.
}
\]

## Next finite test

Do not choose one primitive from the large affine solution space. Construct the linear boundary map on the entire degree-two solution module:

\[
R_\infty:
\operatorname{Sol}^{(2)}_{\rm Kum}
\longrightarrow
\mathcal B_\infty.
\]

Then determine whether any solution lies in \(\ker R_\infty\).

- If yes, the physical derivative would vanish, contradicting the independently verified period; such a result falsifies the boundary model.
- If no, the cokernel class of \(\partial_z\Omega\) is the first typed five-site Gauss--Manin generator.

This is a relative-module calculation, not a primitive-selection problem.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`

Allocator claim: `seqclaim-ce979d801765c1dab5a699a4`.
