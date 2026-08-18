# Entry 510 — The Strict Cartier Action Respects the Stable Cutoff Filtration

Entry 508 defines the strict source action

\[
(f,p)\longmapsto(a^2f,a^2p-h(f)).
\]

For this to induce the proposed map from cutoff (D) to cutoff (D+2),
every admitted exact column must satisfy

\[
h(f)\in P_{D-2},
\]

because its principal boundary is (Kh(f)), with (K) of filtered degree
four.  This bound is not automatic from a target-only truncation.

The complete sector calculation gives no failures.  The numbers of admitted
(q)-columns at (D=12,16,20,24) are respectively

\[
113,quad265,quad481,quad761,
\]

and every one satisfies (deg h(f)le D-2).  Therefore

\[
\boxed{M_{a^2}^{\rm corr}:C_D\longrightarrow C_{D+2}}
\]

is a well-defined filtered chain map without boundary-window corrections.

## Consequence

On the target quotient its action is ordinary multiplication by (a^2);
the term (-h(f)) is retained on the labelled principal source precisely to
make that target action descend.  The remaining computation may therefore
use fixed (D\to D+2) windows, provided the labelled source and principal
degree of Entry 509 are kept.

## Next gate

Compute (H(C_D,u)) for the labelled principal/gradient cone and the rank of
the induced target multiplication map into (H(C_{D+2},u)).

Verified by
`research/voevodsky/check_soft_axis_a2_filtered_strict_action.py`.
