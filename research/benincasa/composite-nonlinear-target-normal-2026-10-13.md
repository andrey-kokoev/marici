# History 5: actual nonlinear target normal from a rational inverse — 2026-10-13

## Iteration 4 and disposition

Freshly read the net's recommendation: construct an inverse-branch target normal for a rank-seven alpha4=0 image without replacing it by a tangent plane.

Constructed an actual rational inverse circuit for history 5's twisted H chart at each of the two fixed positive external Z. It defines the target normal whose source pullback is alpha4, reproduces the full source chart on exact rational transverse arcs, and verifies the oriented local residue square.

## Source-authorized inverse constraints

The matched H cell has zero column 7 and parallel pairs (3,4) and (6,8). Choose the left inverse L of Z supported in columns 1..6 and the one-dimensional kernel row k of the active seven-label Z, embedded with k7=0.

Then

    LZ=I6,  kZ=0,
    C=YL+(u,v)^T k,

so CZ=Y and C7=0 identically. The two parallel-minor conditions

    Delta34(C)=0, Delta68(C)=0

are affine linear in u,v: their quadratic contribution vanishes because both columns use the same vector (u,v). Write the resulting system A(Y)q+constant(Y)=0. On det A !=0,

    q=-adj(A)*constant/det A.

The checker retains the symbolic polynomial matrix, constant and determinant and proves the adjugate identity exactly. This is an explicit rational inverse circuit, not an unspecified implicit function, a fitted matrix, or an expanded all-variable expression selected from the desired residue.

## Actual normal and localization

Recover the canonical H gauge in column order (3,4,5,6,8,-1,-2). In the recovered fiber,

    b(Y)=Delta35(C) Delta12(C) / [Delta23(C) Delta13(C)].

This is the source alpha4 coordinate expressed as a rational target function. Source chart extraction also recovers the other seven alpha parameters, with explicit denominator checks.

Required localizations include the target pivot, fiber-system determinant and gauge/source minors Delta23, Delta35, Delta36 and Delta13. They are all nonzero at the selected boundary points. The full target differential is invertible there.

For the exact rational source arc obtained by fixing every alpha except alpha4=t, the inverse recovers all eight source parameters identically, reconstructs the entire H chart, and gives

    b(target_arc(t))=t.

This identity holds on the declared rational localization, not only to first order. The target normal gradient pulls back to the unit alpha4 covector.

## Residue square and hostile

Using b as the target normal and seven independent target tangent entries, source deletion at alpha4 has sign -1. Both source residue then local pushforward and top pushforward then b-residue have exactly the same density at both samples.

Reversing orientation gives a nonzero residual. A second hostile uses only the linear tangent covector as a proposed defining normal. On the same transverse arc its value differs from t by a nonzero rational function. This rejects first-order agreement as a substitute for the actual normal.

## Implementation failures retained

The initial multivariate inverse expansion timed out after 240 seconds. The final checker retains the same inverse as a rational arithmetic circuit and specializes it exactly to univariate arcs/directions, avoiding full expression expansion. The scientific criterion was not weakened.

An intermediate adjugate identity check used polynomial expansion after substituting rational target arcs and failed to cancel denominators. It was corrected to rational cancellation. The underlying linear system, normal and expected equalities were unchanged.

## Scope and next action

Established: an explicit symbolic inverse circuit for this cell at two fixed Z, exact full source-arc reconstruction, a nonlinear target normal and two oriented local residue-square equalities.

Not established: classification or physical interpretation of the nonlinear divisor globally, the completed BCFW chain's orientation anchor/positive covering, target supercomponent extraction, or weighted cross-history cancellation. No missing full atlas was regenerated.

Next: extend actual inverse-normal constructions to histories 8 and 9, retaining their different support/parallel-class constraints. Alternatively compare shared composite facets in common target coordinates. Local differential normal construction is now demonstrated, so repeating its tangent-rank audit is redundant.

## Reproduction

    python research/benincasa/checkers/check_composite_nonlinear_target_normal.py

Receipt: `research/benincasa/results/composite_nonlinear_target_normal.json`.

Nine grouped controls pass. Prior receipt/source hashes are verified. Evidence is symbolic rational fiber algebra, exact source arcs and local differential algebra, not a kernel proof or a full weighted-descent theorem.
