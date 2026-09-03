# G4 arithmetic loading: convex nonselection DPC

## Question

Can convergence and commutation with the oriented radial codiagonal select G4's canonical loading from the mixed primitive-square and Euler-to-theta coefficients?

## Claim boundary

This packet derives a conditional nonselection theorem from the linear weighted-majorant criterion stated in `research/nima/arithmetic-loading-commutes-with-the-oriented-radial-codiagonal-under-one-explicit-prime-majorant.md`. It does not identify G4's canonical coefficient and does not edit the owning packet.

## Governing conjecture

The shared analytic admissibility and codiagonal-commutation conditions contain enough structure to choose one of the two known coefficients.

## Typed reconstruction

Both candidates are label-diagonal coefficient families \(\omega=(\omega_p)_p\) in the same weighted sequence space

\[
A=\left\{\omega:\sum_p |\omega_p|s_{K,j}(X_p)<\infty\text{ for every declared }K,j\right\}.
\]

Thus this is not a type mismatch, mate relation, or readout projection. The comparison is defined directly in \(A\).

For \(0\le t\le1\), set

\[
\omega^{(t)}=t\omega^{\rm mix}+(1-t)\omega^{\rm E\theta}.
\]

The triangle inequality gives

\[
\sum_p|\omega_p^{(t)}|s_{K,j}(X_p)
\le t\|\omega^{\rm mix}\|_{K,j}+(1-t)\|\omega^{\rm E\theta}\|_{K,j}<\infty.
\]

Assembly and the oriented codiagonal are linear, so their commutation identity also holds for every \(\omega^{(t)}\).

## Risky consequence

The mixed coefficient has the power-law form \(\tfrac12p^{-3/2-\sigma}\), while the source packet states that the Euler-to-theta coefficient has superexponential prime-power decay. These asymptotic classes cannot define the same nonzero prime sequence. The existing criteria therefore admit an entire injective interval of coefficients, not merely two rivals, and cannot define a unique canonical loading.

## Falsification attempt

The checker uses exact rational coefficient families on three prime labels, verifies distinct endpoints, weighted admissibility, linear codiagonal commutation, injectivity of five rational interpolation points, and the majorant inequality. A deliberately nonlinear selector distinguishes the endpoints, confirming the precise kind of extra source law required; it is not derived from admissibility.

## Rivals

1. The two coefficients occupy different structural roles.
2. One is excluded by convergence or codiagonal commutation.
3. Shared analytic properties uniquely select one endpoint.
4. The current conditions define a convex admissible family and selection requires an additional non-affine or source-normalized gate.

## Residual

The source packet supplies distinct asymptotic classes and admits both candidates, so the convex family is nontrivial. The remaining gap is not endpoint distinctness but source authority: no existing G4 premise singles out one point of that family.

## Disposition

Rivals 1–3 are rejected by the declared criterion and asymptotics. Rival 4 is retained. The obstruction is now localized: G4 lacks a source-derived normalization, extremality principle, multiplicative law, or physical readout condition that is not preserved by convex interpolation.

## Explanation

The new equipment/module analysis does not transform one loading into the other. It shows that both already inhabit the same coefficient object and pass the same linear transport gates. The unresolved choice is therefore a source-law obstruction, not a coherence defect.

## Disposition

Do not search for stronger convergence estimates to select the coefficient. Seek a source-derived condition that breaks convex closure and test both endpoints plus interpolants against it.
