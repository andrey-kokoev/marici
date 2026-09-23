# Certified audit elimination needs pair coverage, not just valid cuts

## Exact elimination contract

Given rational rows a_i U+b_i V+c_i h<=d_i, eliminate h. Retain every c_i=0 row. For each negative c_i and positive c_j, add their positive combination cancelling h. Canonicalize positive multiples and deduplicate exactly.

Each emitted row has nonnegative original-row multipliers, proving that no old possibility is excluded. That implication proof alone is insufficient: an empty list of cuts would also exclude no old possibility. The verifier additionally checks coverage of EVERY lower/upper pair and every h-independent row.

## Constructive reverse direction

At a summarized point, negative-coefficient rows give lower bounds on h and positive-coefficient rows give upper bounds. Complete pair coverage says every lower bound is at most every upper bound. Choose the maximum lower bound when present; otherwise choose the minimum upper bound, or zero when neither exists. This satisfies every original row. Thus the summary equals the exact existential projection, including contradictory and one-sided cases.

This is classical Fourier--Motzkin elimination with an explicit certificate/coverage boundary, not a new elimination theorem. Its relevance is that implication-only certificates cannot justify replacing retained evidence by a summary.

## Source-relative control and scope

The first fixture retains U=h, 0<=h<=1 and V=U. Its projection is precisely V=U, 0<=U<=1. It has an owning tail-box lift (U,0,...,0), with h=x_0, admitted for all m>=2. Hence every summarized visible possibility has an old-compatible source filling, not merely an abstract h witness.

The second fixture is a separate bounded linear elimination control with three lower and three upper h bounds and four visible-square rows. It tests expansion, not a newly admitted tail evidence family. In general, eliminating evidence rows alone can ignore hidden source compatibility. One must include an exact source-image presentation (such as the joint-audit dictionary) or provide an additional source-relative lift proof. This prototype does not yet integrate arbitrary owning dictionary rows.

## Size result: no demonstrated net compression

The segment fixture changes 24 rational coefficient fields to 18 but keeps six rows, including redundant consequences. Its summary plus row derivations uses 288 JSON bytes versus 114 bytes for the original string-encoded rows. The coupled fixture grows from ten rows to thirteen: 40 rational fields become 39, while the summary with derivations uses 661 bytes versus 186 for the old rows.

These are literal local encoding measurements, not minimal-description lower bounds. They exclude the full envelope, original-row retention and any external trust anchor; including those cannot establish savings for these packets. Verification must have access to the expected original rows. Discarding those rows after a trusted check is a different operational policy from keeping a self-contained replayable proof.

Thus exact retirement and some coefficient-count reduction are demonstrated, but net proof-carrying storage compression is NOT demonstrated. Redundancy removal and proof amortization remain separate obligations. A short-lived migration proof may be worthwhile even if it is larger than the long-lived summary; that must be stated and measured under an explicit retention policy.

## Verification

Two presentations pass independent implication and pair-coverage checks, with 35 rational reverse-lift controls. Omitted summary rows and negative multipliers are rejected. The general completeness argument is the lower/upper-bound construction, not finite sampling. The verifier imports no producer or LP solver and requires assertions enabled.

    python research/voevodsky/checkers/check_certified_linear_audit_elimination.py
    python research/voevodsky/checkers/verify_certified_linear_audit_elimination.py

Artifacts:

- `results/certified-linear-audit-elimination.json`
- `results/certified-linear-audit-elimination-verification.json`

## Disposition

The useful next gate is to eliminate one audit from the owning uniform joint dictionary plus retained frames, independently certify source-relative completeness, and test redundancy removal under a declared proof-retention policy. The present result supplies the exact elimination certificate contract; it does not yet claim that gate or a general compact projection algorithm is complete.
