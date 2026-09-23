# A constructive generic section repairs four-pair fibre elimination

## Question

Can the failed canonical `C0=[Y Z_(1..6)^-1|0|0]` kernel-area quadratic be repaired CONSTRUCTIVELY for generic rank-six external `Z` and target `Y`, rather than choosing a numerical shift ad hoc?

## Universal identity and selector

Write `C=C0+(S+T)K`, `K Z=0`, where `S=[[p,r],[v,t]]`, `T=[[a,b],[c,d]]`, and `κ_i=det(K_pair_i)` for the four adjacent pairs. Let `L_1,L_2,L_3` be the first three rows of coefficients of `(a,b,c,d)` in the paired minors for the UNshifted canonical section. The fourth row is zero because `C0` has zero columns 7 and 8. For any shift, the FULL four-by-four coefficient matrix is

    M(S) = [L_1; L_2; L_3; 0] + κ · (t,-v,-r,p),
    det M(S) = κ_4 det([L_1; L_2; L_3; (t,-v,-r,p)]).

The second identity is an exact symbolic four-by-four determinant calculation, not a fit to sampled targets. If `rank([L_1;L_2;L_3])=3` and `κ_4≠0`, AT LEAST ONE of `S=E11,E12,E21,E22` yields `det M(S)≠0`: their four added row vectors are signed coordinate basis vectors. Choose the first passing shift. This selects a rational transversal section using a maximum of four exact rank tests. Two distinct positive rational nine-point target witnesses satisfy the rank-three condition; thus it defines a nonempty generic Zariski-open locus in external/target space. It does NOT assert full image coverage.

On this locus the four linearized paired equations give `T(q)` and the remaining relation gives a genuine degree-two `P(q)`, whose two roots provide the complete algebraic fibre. In principle the target eight-form coefficient is the field trace of the intrinsic source-form coefficient divided by the oriented target Jacobian. This specifies an elimination procedure, NOT an evaluated or simplified global rational numerator. Section covariance and the previously certified `d^8B=(det U_L)^-6 d^8U` are required before any sourced `Y0`/nilpotent substitution.

## Disposition

The global-elimination TRANSVERSALITY gate is resolved on a certified nonempty generic open set. The remaining form-trace leaf must construct/evaluate the target field-trace expression, prove any `Y0`-chart cancellation before Berezin extraction, and compare a complete sourced component and a pole residue. The nine-point generalized-R history and positive image coverage are separate open tasks.

Checker: `research/nima/checkers/check_four_pair_transversal_section_selector.py`; result: `research/nima/results/four-pair-transversal-section-selector.json`.
