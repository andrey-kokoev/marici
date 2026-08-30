# Full Yoneda Probing Stabilizes; Restricted Probing Produces Quotients

The first bounded tower experiment uses finite vector spaces over
\(\mathbf F_2\).  Let \(V=W=\mathbf F_2^2\).  Every linear map
\(f:V\to W\) induces a natural transformation

\[
\operatorname{Hom}(-,V)
\longrightarrow
\operatorname{Hom}(-,W),
\qquad
g\longmapsto f\circ g.
\]

The identity probe recovers the map:

\[
f=\eta_V(1_V).
\]

Conversely, naturality along each probe \(g:A\to V\) forces

\[
\eta_A(g)=\eta_V(1_V)\circ g.
\]

Thus the second rung contains exactly the original map data.  It is a lossless
relational re-expression, not a new independent substance.

The exact finite audit checks all 16 maps \(V\to W\), all probes from objects
of dimensions \(0,1,2\), and every change of probe among those objects.  All
16 natural profiles are distinct and recovered by the identity component.

Restricted probing behaves differently.  The single covector
\(p_0(x,y)=x\) turns four states into only two observable profiles and has a
two-state kernel.  Adding the independent probe \(p_1(x,y)=y\) restores four
profiles and joint faithfulness.

Software translation: a complete lawful client-behavior profile reconstructs
the service operation.  A UI model exposing only one field creates a quotient
of the remote entity; adding an independent view field restores the missing
distinction.

The bounded result supports the conjecture:

> Full Yoneda rotation stabilizes the tower up to equivalence.  Genuine
> quotients and repair coherences arise from restricted probe families, not
> from iterating the complete representable construction.

This is a finite model and an instance of Yoneda, not evidence that Marici's
actual admissible probe family is complete.

The exact dependency-free checker passes 7/7 gates.

Artifacts:

- `research/nima/yoneda-tower-stabilization-finite-test.md`
- `research/nima/checkers/check_yoneda_tower_stabilization_f2.py`
- `research/nima/results/yoneda-tower-stabilization-f2.json`

Sequence claim: `seqclaim-835a36f4df0fab8c7fc408a0`.
