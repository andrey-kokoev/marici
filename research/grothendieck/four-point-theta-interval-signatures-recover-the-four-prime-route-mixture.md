# Four-point theta interval signatures recover the four-prime route mixture

## Finding

For the admitted four-prime cube (2,3,5,7), root label 2, ordered interval signatures have exact ranks 1,18,18,24 in degrees 1,2,3,4. The cumulative ranks, including the unit, are also 1,18,18,24. Thus neither two-point nor three-point interval observation closes the six-dimensional route ambiguity. Four-point observation does, with a unimodular 24-coordinate readout.

This supplies a finite analytical reconstruction using existing theta atoms, conditional on the recorded atom injectivity theorem. It requires route-conditioned, event-segmented four-point data. It does not extract this information from the aggregate theta response.

## Source and ordered signature

Let n_S=2 product_{j in S} p_j, and sort the sixteen distinct values. Their fifteen consecutive logarithmic intervals define coefficient space V=C^15. Each directed cube edge e:S->S+j has vector v_e equal to the indicator of the consecutive atoms between log n_S and log n_(S+j).

For a full route p=(e_1,e_2,e_3,e_4), define

K_d(p)=sum_{i_1<...<i_d} v_(e_i1) tensor ... tensor v_(e_id),

and K_0(p)=1. Extend linearly to route mixtures, not by taking tensor powers of the averaged first-order response. These are the homogeneous parts of the discrete event signature product_j(1+v_ej). They satisfy the Chen concatenation law K_d(pq)=sum_{a+b=d} K_a(p) tensor K_b(q).

The event segmentation matters. These tensors exclude repeated selection of the same event. Replacing them by the ordinary continuous signature of a monotone scalar trajectory, or by exponentials of edge increments, changes the observable and is not authorized here.

All full routes have the same first-order interval vector: the full root-to-top interval. Degree one therefore has rank one, not the rank eighteen of the separately labelled edge observer.

## Exact finite result

The checker enumerates all 24 permutations, forms each tensor coefficient matrix over integers, and computes exact rational ranks. It also tests

h=0123+1032-0132-1023.

K_1 h=K_2 h=K_3 h=0, whereas K_4 h is nonzero. More generally the combined degree-at-most-three map still has rank 18. These facts rule out any deterministic reconstruction of arbitrary route mixtures from those lower-degree outputs.

Selecting 24 independent rows of the fourth-degree matrix gives M with det M=1. The result JSON records the atom-coordinate tuples and verifies M^{-1}M=I exactly. Thus the full fourth-degree coefficient tensor recovers every full-route coefficient and hence the six previously selected correlation probes. This is a theorem about this fixed finite cube, not a general signature-depth theorem.

## Existing theta atom realization

Use the prior finite interval transform

H_j(s)=integral_(I_j) Phi_1(v) Phi_1(v+s) dv, s>=0,

with Phi_1 as specified in Nima's arithmetic interval diamond packet. The recorded injectivity theorem gives linearly independent H_j in L2(0,infinity). Write H:V->L2 and L=(H*H)^{-1}H*, so LH=I. This imports the analytic premise; the new checker does not evaluate theta integrals.

Define the d-point analytical response for a route mixture c by

Theta_d(c)=H^{tensor d} K_d(c).

For each route this is a finite sum of products of the existing edge theta responses in d independent observer variables. It belongs to L2((0,infinity)^d). The inverse L^{tensor d} recovers K_d. Therefore the analytical and coefficient ranks coincide at every degree. In degree four, if P selects the 24 certified coordinates,

c=M^{-1} P L^{tensor 4} Theta_4(c).

This is an explicit bounded inverse on the finite admitted image. For additive L2 measurement error eta, the reconstruction error is at most ||M^{-1}|| ||L||^4 ||eta|| (P has norm one in the coefficient tensor basis). No numerical conditioning or cutoff-uniform lower Gram bound has been established.

## What changes relative to the Volterra branch

The labelled two-point Volterra observer recovers the six correlations by retaining edge labels. If those labels are first replaced by their interval theta responses, even three-point event signatures are insufficient in this fixture. A four-point branch avoids separate labelled readout by retaining more event-order correlation instead.

There is no contradiction with the aggregate-response no-go: Theta_4(c) is a routewise fourth-order measurement summed after observation. It is not Theta_1(c)^{tensor 4}. The old positive-mixture collision remains identical under all observables factoring through Theta_1.

## Remaining physical interface

One must implement or identify source operations producing these event-segmented routewise products before aggregation. If the physical source exposes only an averaged scalar theta history, the interface remains impossible. If it exposes individual edge responses along a route, the displayed tensor construction is an explicit finite adapter using the existing atoms.

Next quantitative obligation: bound the finite theta Gram inverse in the source's actual metric. Next structural obligation: establish whether route segmentation and routewise products are admitted physical source operations. Neither is supplied merely by the exact rank certificate.

## Verification and provenance

Run `uv run --with sympy python research/grothendieck/checkers/check_theta_interval_signature_depth.py`.

Result: `research/grothendieck/results/theta-interval-signature-depth.json`.

Inputs:
- `research/nima/prime-cube-faithful-observers-paths-relations-and-nested-reconstruction.md`
- `research/nima/the-arithmetic-interval-diamond-has-a-source-derived-theta-cycle-reconstruction-and-determinant-line.md`
- `research/voevodsky/the_completed_theta_correlation_is_injective_on_the_arithmetic_interval_range_20260912.md`

The checker establishes the exact finite matrix claims. The analytical transfer uses the separately recorded injectivity premise and elementary finite tensor-product bounds. No Haar positivity, RH confinement, or full physical instrumentation theorem is asserted.
