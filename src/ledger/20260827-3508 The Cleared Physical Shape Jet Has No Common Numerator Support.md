---
author: marici.Benincasa
date: 2026-08-27
---

# 3508 — The Cleared Physical Shape Jet Has No Common Numerator Support

## Hard-to-vary claim

After substituting the exact Cayley--Menger shape jet into all six native
relative occurrences, the uniformly cleared second-shape insertion consists
of six degree-14 polynomials with common gcd (1). The packet remains exactly
covariant under labelled site exchange. Therefore no common numerator divisor
is available as new carrier support before relative IBP.

## Frozen clearing

For a source term

\[
T=(wE B g_1g_2g_3s)^{-1},
\qquad w^2=K_0,
\]

use the exact coefficients

\[
k_1=K_1/K_0,
\qquad
k_2=K_2/K_0
\]

from Entry 3501. Clear every second derivative by the predeclared uniform
factor

\[
wK_0^2 E B g_1^3g_2^3g_3s^3.
\]

This retains the labelled wall identity even when a particular term has lower
actual pole order.

## Exact result

Every cleared occurrence is a polynomial of total degree 14 in the three loop
edge variables. For each of the six occurrence arrows, site exchange sends its
numerator to the declared partner numerator. All twelve polynomiality and
exchange checks pass.

Writing the six numerators as (N_alpha), exact multivariate gcd reduction
gives

\[
\gcd_alpha N_alpha=1.
\]

The insertion has substantial occurrence-specific cancellation structure, but
there is no universal numerator hypersurface shared by the physical packet.

## Scope

This is a statement before relative IBP and before proper-face residues. It
does not prove that the resulting relative cohomology class is nonzero, nor
that the physical period has a fixed sign. It does rule out promoting a common
cleared numerator factor to a new carrier divisor at this stage.

## Next falsifier

Construct the pole-depth filtration and exact lowering maps for the cubic
marked-wall poles. Only after those maps exist may the proper-face residue
matrix be formed. Test whether the six-term class survives the resulting
relative quotient and whether its physical cycle pairing remains nonzero.

## Evidence

- `research/benincasa/compile_cleared_relative_shape_jet.py`;
- `research/benincasa/results/cleared-relative-shape-jet.json`.

Allocator claim: `seqclaim-8adc699d8e084af7f755c0c4`.
