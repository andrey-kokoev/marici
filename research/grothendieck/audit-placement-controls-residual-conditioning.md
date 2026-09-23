# Audit placement controls residual conditioning

## Result

On the owning symbolic tail boxes, exact atom audits can either improve or
severely worsen reconstruction stability. The effect is controlled by the
remaining slopes and capacities, not just the number of audited coordinates.

The conditional greedy section remains within an additive one of the best
possible global Lipschitz constant for every audit placement. Its unavoidable
vertical constant is exactly computable. When the largest-slope atom is
pinned, or when at most two atoms remain free, sharper formulas give exact
global optimality.

For a budget leaving two free coordinates, the exact optimal placement is to
retain atoms 0 and m-1 as free and audit all intermediate atoms. The worst
placement leaves atoms m-2 and m-1 free; its conditioning is worse by the
exact factor (128^(m-1)-1)/127.

## Frozen accuracy contract

Use b_j=100+2j, r_j=128^-j and the owning normalized observations

    U=sum t_j, V=sum r_j t_j.

Pinned values are supplied exactly and remain fixed. Subtract their moment
contributions, leaving a box on the ordered free index set I. Measure source
error by L1 on the free coordinates and moment error by absolute
|delta U|+|delta V| in the ORIGINAL owning normalization. No rescaling of V
after removing an early slope is allowed in this comparison.

This is an audit-coordinate COUNT budget, not a bit budget: exact pin indices
and values remain retained information. No noisy-pin model, physical sensing
cost or authenticated acquisition claim is supplied.

Changing the exact pin values only translates the residual observable base;
it does not change this full residual box's conditioning. Additional retained
visible evidence can restrict that domain further; then the upper bound
remains valid, but lower-bound endpoint pairs might no longer be admitted.

## General residual law

For at least two free coordinates let h_I(U),l_I(U) be their greedy profiles,
H_I,L_I their weighted values, and alpha the largest remaining slope. Set

    R_I = sup_U ||h_I(U)-l_I(U)||_1 / (H_I(U)-L_I(U)).

Distinct slopes force unique lifts at both extreme values for each U, so
every conditional section has global Lipschitz constant at least R_I.
The conditional greedy section satisfies

    Lip(s_I) <= max(R_I, 1+alpha*R_I) <= R_I+1.

This follows from the same derivative argument as the unpinned section, but
with weighted profile derivatives bounded by alpha rather than 1. The bound
is for the complete residual polygon, including its tips by continuity.

R_I is computed EXACTLY: the profiles are clamps whose coordinate differences
have a fixed sign. Their L1 difference and weighted gap are affine between
free-capacity prefix and complementary-prefix breakpoints. The ratio has no
strict interior extremum. Check those finitely many rational points and the
tip limit 2/(r_max-r_min).

If atom 0 is pinned, alpha<=1/128 and R_I>=2/alpha. Therefore
1+alpha*R_I<=R_I. The upper and lower bounds coincide: the implemented
conditional greedy section is globally optimal in the declared norms.

This law concerns full remaining boxes with exact pins. It does not treat
arbitrary hidden restrictions as if they left an independent box.

## Rank transitions and exact low-dimensional design

- No free atom: the source is fixed; the Lipschitz constant is zero.
- One free atom i: the image is a segment, with exact inverse constant
  1/(1+r_i). The best choice is i=0, giving 1/2.
- Two free atoms i<j: the inverse of the two moment equations is unique.
  Its L1 operator norm is exactly 2/(r_i-r_j), since r_i+r_j<=2.

Hence for two free atoms the maximum slope separation is the optimal design:

    best: {0,m-1},       L_best=2/(1-128^(-(m-1))),
    worst: {m-2,m-1},    L_worst=2*128^(m-2)/(1-1/128).

Their exact ratio is (128^(m-1)-1)/127. This is an all-m statement, not an
extrapolation of the enumeration. The capacities affect available domains
but not this unique linear inverse's norm.

The transition from two nearly parallel free directions to a single free
direction can sharply improve conditioning: U alone then determines the
remaining atom, and V becomes a consistency constraint rather than a second
coordinate needed for inversion.

## More audits do not imply a smaller reconstruction constant

At m=3 with no pins, R is approximately 2.079482 and the actual greedy
section has a certified global upper bound 3.079482. Pin only atom 0. The
remaining slopes are 1/128 and 1/16384, so every conditional section now has
exact best constant

    32768/127 = 258.015748...

The new unavoidable constant exceeds the old constructive upper bound by a
factor greater than 83.78. Thus this is not merely a comparison of loose
upper estimates.

There is no contradiction with information increasing: the admitted fibers
shrink. But the old section was free to use the high-leverage first coordinate
in choosing a witness. The conditional section must preserve that supplied
value, leaving two nearly parallel directions to resolve. A stronger fidelity
requirement can make a residual inverse less stable.

## Finite design synthesis and its exact limits

All 1,368 audit subsets are enumerated for m=3,4,6,8,10, giving 36 fixed-budget
design comparisons. At each budget, minimize the exact R_I. If R_* is that
minimum, the selected placement and greedy section provide a global design
with constant at most R_*+1, while no design at that budget can beat R_*.

For zero, one or two free coordinates the reported global design is exact.
For larger free sets the result is an additive-one global design sandwich,
not a claim that the chosen placement minimizes the exact global constant.
The search is exhaustive, not a polynomial-time optimization claim.

Some m=8 optimal VERTICAL designs illustrate why a single sorting heuristic
would be premature:

| Audited count | Best free indices | Exact R_I, approximately |
| --- | --- | ---: |
| 0 | 0,1,2,3,4,5,6,7 | 8.174338 |
| 1 | 0,1,2,3,4,5,6 | 6.547409 |
| 2 | 0,1,2,5,6,7 | 6.071234 |
| 3 | 0,1,2,3,4 | 4.246135 |
| 4 | 0,1,6,7 | 4.008061 |
| 5 | 0,1,2 | 2.079482 |
| 6 | 0,7 | 2.000000 |

Capacity balance and intermediate slopes matter once more than two coordinates
remain. For example {0,1,7} and {0,6,7} have the same number of free atoms and
the same extreme slopes, but different certified R_I values.

## Implementation and verification

The producer freshly replays both the owning tail-face verifier and Nima's
independent audited-section verifier. It invokes the actual AuditedGenerator
at optimal and worst placements, using nonzero exact pins. All 62 runtime
controls retain their audits, obey caps and reproduce both moments.

The separate verifier imports neither the constructor nor the query engine.
It independently expands free greedy profiles, checks every breakpoint ratio,
reconstructs all fixed-budget minima and maxima, checks the actual returned
conditional lifts, proves the strict monotonicity counterexample, and rejects
an understated conditioning certificate.

    uv run --with python-flint python research/grothendieck/checkers/check_audit_conditioning_design.py
    python research/grothendieck/checkers/verify_audit_conditioning_design.py

Contract: `results/audit-conditioning-design-contract.json`.
Packet: `results/audit-conditioning-design.json`.

## Structural synthesis

Preserving an audit, retaining fewer possibilities and reconstructing stably
are different obligations. The audit-aware section solves the first two;
this result quantifies the third and makes audit choice a constructive design
problem with matching obstructions.

It does not infer the actual source from a selected lift, weaken any retained
audit, or change the full-tail midpoint status. Moment uncertainty and noisy
audit values would require a separately declared joint error model.
