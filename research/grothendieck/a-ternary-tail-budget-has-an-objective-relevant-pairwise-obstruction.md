# A ternary tail budget has an objective-relevant pairwise obstruction

## DPC disposition: corroborated on an owning analytical relaxation

This is not another invented parity fixture. The source carrier is a frozen
rational moment relaxation derived from the already proved Chebyshev majorant
and the actual combined signed kernel at N=1e6.

Take Mangoldt masses x_1,x_2,x_3 in the three bins

    (7,000,000,7,500,000],
    (7,500,000,8,000,000],
    (8,000,000,8,500,000].

Nonnegativity, elementary atom bounds, and the owning Chebyshev inequality
supply

    0<=x_i<=c_i,
    x_1<=B_1, x_1+x_2<=B_2, x_1+x_2+x_3<=B_3,

where c_i is an outward rational upper bound on bin width times log of its
right endpoint, and B_i is an outward rational upper bound on
U(right endpoint)-psi(N). Omitting earlier tail mass only weakens these
prefix bounds. The finite carrier is independently declared by these valid
inequalities BEFORE computing its pair projections.

It is a moment relaxation, not the exact prime-realizable source. Source
lifts below mean lifts into this declared carrier. This distinction is
necessary: no claim is made that arbitrary admitted bin masses are prime
masses or even realize every unretained microscopic tail constraint.

## Exact local views and the obstruction

Every inequality has nonnegative coefficients. Therefore the existential
projection onto a pair is EXACTLY obtained by setting the third coordinate
to zero in the inequalities: restriction is necessary, and zero extension
supplies a lift for every admitted pair.

The pairwise intersection admits approximately

    (5,045,392.439781386,
     5,045,392.439781386,
     5,738,539.6809659535).

Its exact form is (B_2/2,B_2/2,B_3-B_2/2). Each pair has an exported full-carrier
lift with the missing coordinate zero. All overlaps use identical masses.
But the triple has total B_3+B_2/2>B_3. It has no common lift.

The obstruction is the independently justified ternary cumulative budget.
Exact local projection and coherent overlap equality do not reconstruct it.

## The obstruction changes an owning signed bound

The certified single-valley theorem gives extrema of K_plus+K_minus on
each bin from its endpoints and, in the third bin, its unique minimum.
Let [l_i,u_i] be the resulting rational kernel enclosures. Actual block
pairings satisfy

    sum l_i x_i <= block pairing <= sum u_i x_i.

Exact LP primal/dual packets compute the minima of sum l_i x_i over both
the full carrier and the pairwise relaxation. The full minimum is about

    -5.7586402562280044e-8.

The pairwise optimizer has even its UPPER kernel-box objective at about

    -8.304536908966596e-8.

Hence the gap is robust to every coefficient choice within the certified
kernel boxes, with lower bound

    2.5458966527385913e-8.

The frozen BLOCK threshold -7e-8 lies strictly between them. This was declared
before numerical evaluation. It is not the original full-tail midpoint
threshold, and no full-tail task status is changed by this local experiment.

The exact LP optima are for the rational stepwise lower functional, not an
assertion that the exact signed-kernel moment problem was solved sharply.
The robust upper-versus-lower separation establishes that coefficient
uncertainty cannot explain the obstruction.

## Small certificate, rather than optimizer authority

The full optimum uses only the third bin's atom-cap row and the total-budget
row in its nonzero dual. Its primal assigns x_1=0, x_3=c_3 and
x_2=B_3-c_3. Every prefix and atom bound is checked.

The pairwise optimum is supported by the three pair-budget rows. Its three
zero-extended pair lifts and its violating total mass are checked with exact
rational arithmetic. Both LP packets satisfy primal feasibility, dual
feasibility and equality of objectives. The optimizer is not trusted as
an admission authority.

## A sufficient cut interface and its omission witness

After the first two bins, retain the remaining total budget

    B_3-(x_1+x_2)

and the accumulated objective. Once earlier constraints have been validated,
the third mass is admitted exactly when

    0<=x_3<=min(c_3,B_3-x_1-x_2).

This is a sufficient cut representation for the frozen scalar lower
functional. It does not claim universal minimality for additional queries.

If only the pair budgets are tested, the allowed upper bound instead becomes

    min(c_3,B_3-x_1,B_3-x_2).

The exported candidate lies between these two upper bounds. This is the
requested omission witness: dropping the higher-arity remaining-budget
constraint admits a completion that the full analytical carrier excludes.
The issue is constraint completeness, not any nontrivial defect in the
coordinate overlap maps.

## Structural synthesis

The result links three previously separate obligations on an owning analytic
example:

1. Local views can be exact, yet their compatible tuples can miss a global
   source constraint.
2. The missing constraint can change a certified signed objective bound,
   rather than merely exclude irrelevant configurations.
3. A cut interface must transport that constraint's residual budget before
   any continuation minimization is sound.

The existing full Chebyshev tail methods already retain the global budget;
this experiment does not discover a new prime-distribution fact. It measures
what is lost by replacing that known relation with its pairwise projections.
It advances the structural synthesis, not the full-tail numerical cutoff.

## Reproduction

    uv run --with python-flint --with sympy python research/grothendieck/checkers/check_ternary_tail_budget_dpc.py
    uv run --with python-flint python research/grothendieck/checkers/verify_ternary_tail_budget_dpc.py

Contract: `results/ternary-tail-budget-dpc-contract.json`.
Certificate: `results/ternary-tail-budget-dpc.json`.

The producer freshly replays the owning single-valley proof. The separate
verifier imports no LP optimizer; it rechecks capacity formulas at a different
precision, source bindings, exact projections/lifts, both primal/dual packets,
the robust gap and the cut omission. It rejects promotion of a pairwise
candidate to a full lift and a corrupted dual. It relies on the owning
hash-bound interval kernel proof rather than independently reimplementing it.
