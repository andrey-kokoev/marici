# Seed constraints do not select the exchange interaction kernel

## Question and controlled comparison

Reuse the existing conservative exchange event

    delta_i=w_i-u_i^T q,
    q'=q+u_i delta_i,
    w_i'=w_i-delta_i.

Test whether endpoint incidence, retained primitive roles, unit features, reversible budget-preserving events and seed relabelling symmetry determine the seam's mixed response.

`check_seed_exchange_kernel_freedom.py` constructs two exact COUNTERMODELS. They are not proposed physical realizations and no parameter is fit to a desired measured result. Both use seven carrier coordinates, six primitive-labelled record coordinates and the same initial state: q=0, w_AB=1, all other w=0. Selecting that preparation is a test input, not a source-derived physical preparation.

Each feature has the form

    u_i=a*e_shared+b*e_i, a^2+b^2=1.

The two cases are (a,b)=(0,1) and (3/5,4/5). Both have six linearly independent unit features because b is nonzero. All distinct feature overlaps equal a^2. A common feature coordinate and a positive common overlap are modelling freedoms; the seed does not supply their magnitude.

## Constraints shared by both cases

- Exactly the same six primitive labels and actual seam path words are used.
- Each path action is the chronological product of the same exchange rule instantiated with its primitive feature.
- Every event is an exact orthogonal involution. The complete numerical state reconstructs by reversing the event word, and each corner retains unit quadratic budget for the common test preparation.
- The same seed automorphism exchanges carrier-feature coordinates and record labels. The event actions intertwine with this relabelling.
- No identity between direct and indirect paths or between AB and BA is imposed.
- Histories are the retained input words; no output equality is used to erase them. These tests concern the four words with no repeated primitive inside a word, not a global freshness/event-emission protocol.

These are requirements of the tested conditional exchange interpretation, not all purportedly forced by seed incidence. In particular, unit norms and a quadratic budget come from the reused event law. The result holds even AFTER granting those extra constraints.

## Exact outcome

Let X0,X1 be the direct/indirect forward word actions and Y0,Y1 the return actions. The checker verifies

    Delta_H = Y1 X1 - Y0 X1 - Y1 X0 + Y0 X0
            = (Y1-Y0)(X1-X0).

| Distinct feature overlap | Mixed operator | Mixed output on identical preparation |
|---|---|---|
|0|Exactly zero|Exactly zero|
|9/25|Nonzero|Nonzero|

In the orthogonal case, forward and return labels act on disjoint carrier/record coordinates; their difference operators have disjoint support. In the second case shared carrier overlap permits cross-response. The complete mixed output vector is tested, not a fitted scalar measurement. Its squared norm is not declared a physical energy or a new conserved quantity.

This difference cannot be removed by a common orthogonal coordinate change: such a change preserves the feature Gram matrix. The two models have different Gram matrices. Their agreement on endpoint incidence and labelled paths does not make their response interpretations equivalent.

## Synthesis

The existing exchange law can generate a mixed seam effect, but the seed constraints tested here neither require nor forbid one. Even nondegenerate feature families and symmetry leave both possibilities. The absent source item is the carrier-feature/metric coupling, not a further history-recovery lemma.

A source construction could supply additional constraints and select a kernel; this test does not rule that out. Nor does it show that arbitrary kernels are physically admissible. It prevents promoting the existence of a flexible reversible exchange model into a derivation of the seed interaction.

## Verification

    python research/nima/checkers/check_seed_exchange_kernel_freedom.py

Fresh exact rational checks pass for all twelve event matrices, four corner actions in each model, inverse reconstruction, budget preservation, mixed factorization, common preparation and seed covariance. No new numerical physical model, constant fit or native source admission was claimed.
