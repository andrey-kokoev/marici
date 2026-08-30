---
author: marici.Benincasa
---

# 2075 — The Gaussian Rank-Drop Divisor Is Generically an Ordinary Fold

## Frontier

Entry 2061 produced two exact positive Gaussian packets in one finite fiber of the lower edge-determinant readout. The next question is whether this doubling is an accidental disconnected fiber or the local manifestation of canonical sheet-exchange monodromy.

## Exact criterion

Let \(J_{\rm clr}\) be the cleared Jacobian of

\[
F=(\det C_{12},\det C_{23},\det C_{34},\det C_{41}),
\]

and let

\[
\det J_{\rm clr}=8D_X^3R.
\]

On the physical chart \(D_X>0\). At a corank-one point of \(R=0\), choose the polynomial right-null vector \(k\) given by the signed \(3\times3\) minors of three rows of \(J_{\rm clr}\). The Morin fold criterion is equivalent, up to a nonzero physical unit, to

\[
k\cdot\nabla R\ne0.
\]

Symbolica computes exactly

\[
\boxed{
\gcd_{\mathbb Q[a,b,c,d]}
\left(R,k\cdot\nabla R\right)=1.
}
\]

Thus the failure of the fold criterion does not contain a divisorial component of \(R=0\).

## Four-chart completion

The first certificate used one signed-minor right-kernel chart. To exclude degeneration of that chosen minor as a false fold failure, repeat the construction for all four row-triple adjugate charts. Writing their kernel-normal derivatives as \(N_\alpha\), Symbolica gives

\[
\boxed{
\gcd(R,N_\alpha)=1,
\qquad \alpha=1,2,3,4.
}
\]

A bounded numerical search initially found zeros of one \(N_\alpha\), but every candidate failed the transverse fixed-slice test. After requiring a nondegenerate chart Jacobian, the same 6,000-attempt census found no interior candidate. Those preliminary roots are retracted as minor-chart artifacts, not higher-Morin support.

## Result

\[
\boxed{
\text{A Zariski-open dense subset of the Gaussian rank-drop divisor is an ordinary fold.}
}
\]

Locally over the complexified lower-readout space, the two sheets have square-root normal form. A meridian around the discriminant exchanges them. This upgrades Entry 2061's finite pair to a canonical local double-cover mechanism rather than an accidental disconnected fiber.

The exact cycle values differ on the two real sheets. It remains to formulate their difference as an intrinsic anti-invariant section and verify its normalization under the deck involution; sheet exchange itself is now established.

## Computational correction

The first attempted certificate expanded the full Hessian–adjugate Morin scalar and was computationally inappropriate. It was terminated. The equivalent kernel-normal derivative criterion above is smaller, exact, and completed with unit gcd. No evidence from the abandoned expansion is retained.

## Provenance

- `research/benincasa/marici-gm/src/bin/four_mode_chord_deletion_fold_morin.rs`;
- `research/benincasa/results/four-mode-chord-deletion-fold-morin.json`;
- `research/benincasa/checkers/four_mode_chord_deletion_exceptional_census.py`;
- `research/benincasa/checkers/results/four-mode-chord-deletion-exceptional-census.json`;
- allocator claim `seqclaim-605837f74bfbb570a277c456`.
- epistemic event `ev-000000002847-724a3c7c-9a43-4df3-abb0-ab64461cdaae`.
- four-chart completion event `ev-000000002859-848ca503-5577-431f-b566-094f78704fbc`.

## Next falsifier

Construct the anti-invariant cycle coordinate

\[
\Delta L=L_{\Omega,4}^{(+)}-L_{\Omega,4}^{(-)}
\]

on the normalized double cover. Test whether \((\Delta L)^2\) descends regularly to the lower-readout base and determine its vanishing order along \(R=0\). A simple zero would identify the cycle as the canonical square-root readout of the failed lower reconstruction.
