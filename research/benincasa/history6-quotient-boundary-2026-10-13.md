# History6 endpoint/boundary iteration 5 — actual quotient corner extraction

Freshly read the intrinsic cross-ratio receipt, F6 corner checker and current work-net (pins v31). The Y-dependent quotient coefficient is now actually pulled back to F6, not replaced by an independent external spinor weight:

    c6(CZ,Z) = b3*(b2+b3+b4)/((b2+b3)*(b3+b4)),
    1-c6 = b2*b4/((b2+b3)*(b3+b4)).

This identity holds for any invertible six-active-label external basis: each quotient bracket is det(Z_support) times its complementary source minor, with sign fixed by its ordered labels. The checker derives the generic basis pullbacks and verifies all four symbolic pullbacks at both positive moment-curve Z fixtures. The common det cancels, not a fitted scalar.

## Positive common-corner localization

At b2=b4=0, retain b1,b3,b5,b6,b7,b8>0. Both original quotient denominators are nonzero (their source factors are b5*b7*(b2+b3) and b6*b8*(b3+b4), times nonzero external determinants). Thus c6 is regular and equals 1, and 1-c6 vanishes. There is no coefficient Laurent pole correction on this localized corner. The simultaneous closed locus b3=0 is excluded from this calculation, not assigned an extrapolated value.

In source deletion order b2 then b4, parity -1, the six-dlog coefficients are (-1,0) for proposed quotient-weighted K0/B22. The preceding reference transition determinant -1 gives reference coefficients (+1,0). Both target fixtures have ambient rank eight, tangent rank six and invertible ordered normal Jacobian. Source residue then pushforward, mixed source/target residue, and top pushforward then target iterated residue agree. K0 corner densities are exactly the earlier F6 densities; B22 corner densities are zero. Three composites plus this quotient K0 give zero at both fixtures. Reversing its orientation produces nonzero defects.

This differs from the previous independent external-base module, where c6(t) was fixed while taking residues and K0-only replacement left (c6(t)-1)*D. Those residuals remain valid for that different module; they have not been erased or reinterpreted as tests of the Y-dependent coefficient.

## Added poles and another executable boundary

On meromorphic continuation, b2+b3=0 and b3+b4=0 are actual added simple poles. Relative to the corresponding remaining seven-dlog order, residues for quotient K0 are respectively b4/(b3+b4) and b2/(b2+b3); B22 residues are their negatives. Their sums vanish. These loci do not occur in the strictly positive chart, but must remain in rational/domain accounting. No physical channel or ordinary canonical boundary is assigned merely from those pole equations.

At b3=0 with b2,b4 nonzero, the source K0 residue is zero and B22 carries coefficient +1 of the remaining seven-dlog form. This is a source calculation only. Next substantive step: construct its actual target normal/rank/localized differential square, without interpreting source zero as a contracted target residue; separately type the bosonized-supercomponent compatibility map required for a physical extraction theorem.

## Scope

The local differential boundary extraction of the specified quotient coefficient is now constructed. It is still a proposed rational coefficient-weighted realization, not an ordinary unit canonical admission, normalized nine-to-sector map or global BCFW chain/covering theorem. The full physical boundary-supercomponent identification remains open. All scientific node verdicts stay unchanged.

Evidence: `checkers/check_history6_quotient_boundary.py`, `results/history6_quotient_boundary.json`. Successor pins v32 and structural net/SCC checks are distinct from the actual quotient/Laurent computations. A nonredundant executable continuation remains.
