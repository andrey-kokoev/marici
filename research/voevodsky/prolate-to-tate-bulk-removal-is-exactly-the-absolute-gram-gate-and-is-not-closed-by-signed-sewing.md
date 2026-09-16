# Prolate-to-Tate bulk removal is exactly the absolute-Gram gate and is not closed by signed sewing

## Objective

Resolve or sharply type residual channel 2 of the physical seam: comparison of
the orthogonally bulk-removed prolate feature with the global Tate boundary
legs.

## Two distinct forms

Let

\[
R_\Lambda:\mathcal D_S\to\mathcal H_\Lambda^{\rm res}
\]

be the physical residual after a cutoff-dependent orthogonal bulk projection,
and let \(J_\Lambda\) be its signed readout. It determines two source forms:

\[
K_\Lambda=R_\Lambda^*R_\Lambda\succeq0,
\qquad
C_\Lambda=R_\Lambda^*J_\Lambda R_\Lambda.
\]

The target Tate feature is

\[
F_Sg=(A_{S,+}^{1/2}\mathcal M_Sg,
      A_{S,-}^{1/2}\mathcal M_Sg),
\]

with

\[
F_S^*F_S=|A_S|,
\qquad
F_S^*JF_S=A_S.
\]

Existing centered trace comparison controls the signed form

\[
C_\Lambda\to A_S.
\]

The physical intertwiner requires the positive form

\[
\boxed{K_\Lambda\to|A_S|.}
\]

These statements are inequivalent.

## Smallest exact hostile

Even in one source dimension, fix the signed target \(A_S=1\). For any
\(d_\Lambda\ge0\), take a two-leg residual vector

\[
R_\Lambda(1)=
\left(\sqrt{1+d_\Lambda},\sqrt{d_\Lambda}\right),
\qquad
J=\operatorname{diag}(1,-1).
\]

Then

\[
C_\Lambda=(1+d_\Lambda)-d_\Lambda=1=A_S
\]

exactly for every cutoff, while

\[
K_\Lambda=(1+d_\Lambda)+d_\Lambda=1+2d_\Lambda.
\]

Taking \(d_\Lambda=1\), or \(d_\Lambda\to\infty\), proves that exact signed
sewing neither fixes nor bounds the absolute Gram. The missing information is
positive mass common to the two polarities and invisible to their difference.

Thus channel 1's exact finite-part and placement results cannot close channel
2.

## Necessary and sufficient finite-packet theorem

On a finite observer packet \(E\), the following are equivalent.

1. There are isometries from the physical residual feature ranges into the Tate
   two-leg carrier such that
   \[
   V_\Lambda R_\Lambda g\to F_Sg
   \]
   for every \(g\in E\).
2. The physical absolute Grams converge in matrix norm:
   \[
   K_\Lambda|_E\to |A_S||_E.
   \]

Necessity follows by preservation of inner products. For sufficiency, positive
square-root continuity gives

\[
K_\Lambda^{1/2}\to|A_S|^{1/2},
\]

and polar decomposition identifies the canonical source-coordinate square root
with the physical feature range. Spectral sign splitting of \(A_S\) then gives
the two Tate legs.

Hence the absolute-Gram statement is not merely one possible estimate; it is
the exact acceptance criterion for the physical intertwiner.

## What prior research does provide

### Orthogonal bulk removal is correctly typed

The regulated positive feature admits a cutoff-dependent bulk embedding
\(J_{\alpha,S}\Xi_S\). Projecting orthogonally away from that embedded bulk
produces a positive residual feature. This is the correct construction;
entrywise finite-part subtraction is not positive.

### Signed scalar comparison is advanced

Exact regulator transport, left-placement convergence, and centered
Tate-relative trace comparison identify the signed limiting form on admitted
observer cores.

### Abstract finite-packet legs exist

For each fixed finite packet, Jordan functional calculus applied directly to
the centered matrix constructs canonical positive and negative square-root
legs converging to the finite Weil/Tate matrix legs.

Those are abstract source-coordinate features. Compression does not commute
with positive parts, so they are not packet-natural and are not identified with
the physical prolate residual operators.

### Reference leading bulk is shared

Bounded centered relative-Gram convergence transfers the reference Widom
leading edge law to the Tate regulator. This identifies the common leading
positive bulk scale, but not the finite absolute residual after that bulk is
removed.

## Reduced analytic obligations

The regulator comparison packet reduces scalar sewing to two
Hilbert--Schmidt leg limits plus one summable angular majorant. For the physical
positive intertwiner, these must be strengthened or reorganized to prove:

1. construction of the actual orthogonal residual \(R_\Lambda\) with the same
   bulk convention in reference and Tate channels;
2. convergence of every polarized entry of \(K_\Lambda\) to \(|A_S|\) on a
   bounded packet;
3. uniformity over bounded observer packets and conductor truncations;
4. Mosco convergence of the closed forms for the completed-domain theorem;
5. treatment of the exact intersection atom separately, rather than burying it
   in the residual Gram.

Item 5 is residual channel 3 and should not be folded into the present gate.

## Status

Residual channel 2 is **not closed** by prior research. It has, however, been
reduced to one precise theorem:

\[
\boxed{
R_\Lambda^*R_\Lambda
\xrightarrow[\Lambda\to\infty]{}
|A_S|
}
\]

on the common form core, first in finite-packet matrix norm and ultimately in
Mosco form convergence.

No further scalar finite-part calculation can decide this gate. The next
nonredundant execution must calculate or estimate the positive residual Gram,
not its signed difference.

## Repository dependencies

- `the-physical-prolate-to-tate-boundary-intertwiner-is-equivalent-to-absolute-gram-convergence-with-a-balanced-sonin-pair.md`
- `a-positive-relative-boundary-exists-exactly-after-orthogonal-bulk-feature-removal-not-entrywise-finite-part-subtraction.md`
- `regulator-comparison-reduces-to-two-hilbert-schmidt-leg-limits-and-one-angular-dominated-convergence-bound.md`
- `bounded-relative-gram-convergence-transfers-the-reference-widom-law-to-the-tate-regulator.md`
- `every-finite-observer-packet-has-a-canonical-convergent-two-polarity-positive-boundary-from-the-centered-gram-matrix.md`
