# RG-completion debt

## Question

What is the smallest currently proved source-coordinate packet that must be
completed before a fixed point or invariant manifold can carry authority to
select WP543's \(t\)-direction?

## Conservative coordinate census

WP491-WP499 establish five disjoint unresolved sectors:

- ten messenger tensor normalizations;
- three radial leaf-leaf portals,
  \(F^2H^2\), \(F^2R^2\), and \(H^2R^2\);
- one connector-adjoint alignment coupling;
- one pure-adjoint Gram coupling;
- three independent directions completing the retained connector
  radial/frame span to the five-dimensional \(O(2)\)-invariant quartic space.

The total is

\[
10+3+1+1+3=18.
\]

The sectors have different field content or tensor contractions, so their
coordinates are not double counted. WP496 proves that the parity-even
delta-contracted pure-adjoint quartic sector closes after the Gram coordinate
is added, preventing an artificial extra count there.

## Scope of the lower bound

The number 18 counts only coordinates explicitly proved necessary and still
unresolved. It excludes:

- already-present source couplings;
- Standard Model gauge and Yukawa coordinates;
- quadratic masses;
- scheme and evanescent coordinates;
- possible higher-loop invariants;
- all 29 WP544 scale, twist, renormalization, and threshold controls.

Eighteen is therefore a lower bound on completion debt, not the dimension of
the final beta system.

## Selector-authority gate

A candidate beta zero or invariant manifold may select \(t\) only if:

1. the complete declared action is closed on at least the 18-coordinate
   unresolved packet plus inherited and Standard Model couplings;
2. every beta component and finite threshold map is derived in one declared
   scheme;
3. the candidate is stable on its admitted domain;
4. its constraint Jacobian has nonzero contraction with WP543's tangent
   \((2,-1,0,0)\);
5. no flavor readout or WP544 instrument control is used as a source equation.

A zero computed after omitting any tagged coordinate is a zero of a non-closed
truncation. It has no numerical-selector authority.

## Smallest falsifier

Omitting only the connector-adjoint alignment coupling already fails closure.
WP494's parallel and orthogonal configurations share all radial data but
produce distinct gauge counterterms. This one-coordinate omission is enough
to invalidate a purported complete beta system.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp545_rg_completion_debt.py

The generated result is
research/flavor/results/wp545_rg_completion_debt.json.

The reviewed graph admission is
ev-000000004897-a5853d77-0a23-4d33-aae3-796369e9f875.
