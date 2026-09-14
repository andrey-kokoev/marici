# The physical sheet rule explains why a component difference is not yet a period

## Fresh source clue

Ledger entry `20260815-181 Positive-Sheet Resolution and Vanishing Generic-Q Physical Variation` contains the missing conceptual distinction.

For every forced-square face support \(L\), the cover restricts as

\[
D_L^\pm=\{L=0,\ W=\pm R_L\}.
\]

But the physical positive-sheet chain does **not** equal the global algebraic difference \([D_L^+]-[D_L^-]\). On a real boundary segment it obeys

\[
\Gamma_{\rm phys}\cap L\subset D_L^{\operatorname{sign}R_L},
\]

because \(W=+\sqrt{\overline K}=|R_L|\). It switches algebraic component only where \(R_L=W=0\).

## Consequence for the pyramid

The pyramid vertices

\[
d_i=[C_i^+]-[C_i^-]
\]

are integral Picard classes and transport coherently under \(r_b\), but they are not themselves physical chain segments. A physical period requires a comparison that combines:

1. the algebraic component marking \(C_i^\pm\);
2. the sign chamber of the square root \(R_i\);
3. the relative-chain orientation across sheet-switch points;
4. the de Rham residue covector.

This is precisely the missing coherence comparison. Its role is not merely to discard one rank from \(A_1^3\); it converts a global algebraic difference marking into the segmentwise positive-sheet relative cycle before period evaluation.

## Information flow

The corrected flow is

\[
\{d_i\}
\longrightarrow
\text{coherent integral routes}
\longrightarrow
\text{component/chamber comparison}
\longrightarrow
\Gamma_{\rm phys}^{\rm res}
\longrightarrow
\text{local residue pairing}.
\]

The PDF residue formula from `Cosmology meets cohomology`, Appendix A, applies only after the third arrow fixes the correct supported dual boundary class.

## Additional theorem already available

The same ledger entry proves, for the generic nonsoft \(q_{\mathcal G_{12}}\) residue sector across the algebraic divisor \(\mathcal Q=0\), that the marked resolved pair extends smoothly and

\[
T_{\mathcal Q}=1,
\qquad
N_{\mathcal Q}=0,
\qquad
\operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys}^{\rm res})=0.
\]

This is a genuine physical-nullity statement, but it concerns variation across \(\mathcal Q=0\), not the four split-fiber route kernel. It therefore cannot identify \(K_{\rm route}\) directly.

## Remaining literal datum

The current repositories serialize \(v_{\rm alg}\) only as the master-coordinate combination

\[
v_{\rm alg}=x^2y^2((x^2-y^2)e_7+2e_8-2e_9).
\]

They do not serialize logarithmic differential-form representatives for \(e_7,e_8,e_9\). Consequently the local residue computation cannot yet be run. The next required datum is one literal integrand/form dictionary for those three masters, not another abstract lattice calculation.
