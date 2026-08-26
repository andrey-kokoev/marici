# The H1 Tail–Seam Cut Is an Exact Isometric Correspondence

## Boundary-bearing state

The Mellin–Parseval analysis identifies the missing finite seam as an interval, not merely an endpoint scalar. This suggests the source map

\[
C_Lf=left(T_Lf,R_Lf\right)
=
\left(f(\,\cdot+L),f|_{[0,L]}\right).
\]

Take the source graph space to be (H^1(0,\infty)). Its norm contains both bulk amplitude and one derivative:

\[
\|f\|_{H^1}^2
=
\int_0^\infty\left(|f|^2+|f'|^2\right)dy.
\]

Then (C_L) is an exact isometry onto its incidence-constrained image:

\[
\|f\|_{H^1(0,\infty)}^2
=
\|T_Lf\|_{H^1(0,\infty)}^2
+
\|R_Lf\|_{H^1(0,L)}^2.
\]

The image condition is the interface trace equality

\[
(R_Lf)(L)=(T_Lf)(0).
\]

Both traces are continuous on their (H^1) spaces. Thus the seam is retained as a genuine state component and the cut has closed image.

## Prime composition is interval concatenation

For lengths (L,M>0), cutting first at (L) and then cutting the translated tail at (M) gives

\[
f|_{[0,L]},
\qquad
f(L+\,\cdot)|_{[0,M]},
\qquad
f(L+M+\,\cdot).
\]

The two seam pieces concatenate canonically because their interface traces agree. Their energies add exactly, producing (f|_{[0,L+M]}). Therefore

\[
C_{L+M}
\cong
(C_M\oplus 1)C_L
\]

after the source-derived concatenation identification.

For (L=\log p) and (M=\log r), commutation of prime resegmentation is now ordinary associativity of cutting one interval at two marked positions. No braid anomaly survives.

## Completion at infinite cutoff

As (L\to\infty), the translated tail energy tends to zero for every fixed (f\in H^1(0,\infty)), while the seam energy increases to the full source energy:

\[
\|T_Lf\|_{H^1}^2\longrightarrow0,
\qquad
\|R_Lf\|_{H^1(0,L)}^2\longrightarrow\|f\|_{H^1}^2.
\]

Nothing disappears. Energy migrates from the tail component into the expanding seam component. This is the exact repair of the earlier completion-at-infinity witness where the visible tail vanished while seam energy remained nonzero.

The direct system of seam intervals completes back to (H^1(0,\infty)). Hence the family of cut correspondences is uniformly isometric even though the tail projections alone are not bounded below.

## What this proves and does not prove

This gives a source-derived, boundary-bearing topology with:

- continuous wall traces;
- exact finite prime seams;
- canonical resegmentation;
- no loss of graph energy at infinite cutoff.

It does not yet prove that the full Pearson operator, primitive and square currents, or theta modular reflection preserve this graph space. Nor does it orient the canonical split Clifford pairing. Those are the next source-specific gates.

## Next falsifier

Act with the Pearson differential expression and the Clark shear on the cut state. Compute whether

\[
C_LD-\left(D_{\mathrm{tail}}\oplus D_{\mathrm{seam}}\right)C_L
\]

is supported only at the declared interface trace. Any bulk residual closes this graph-rigging route; a pure interface distribution is the expected boundary current.

## Verification

The dependency-free exact-rational checker `research/grothendieck/checkers/h1_tail_seam_cut_isometry.py` verifies one-cut and two-cut energy identities, seam concatenation, and interface trace matching on a polynomial witness.
