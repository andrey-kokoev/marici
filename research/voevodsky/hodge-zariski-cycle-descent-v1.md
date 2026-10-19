# Hodge descent test: actual cycles glue, local Chow classes lose information

## Question

Construct an actual algebraic-source comparison instead of waiting for a Hodge cotower. Test whether compatible local algebraic realizations can fail to glue, and locate an information-loss step with a known algebraic control. SCC obligations: restriction functoriality, matching, then quotient/readout descent. The target X and alpha of the base net are unchanged; P1 below is a falsifier, not a replacement target.

## Source operation and types

For a smooth complex algebraic variety X and a finite Zariski open cover (U_i), use the genuine cycle groups Z^p(U)_Q: finite rational sums of irreducible codimension-p closed subvarieties. Open restriction sends [Z] to [Z intersect U] if nonempty and to zero otherwise. It is flat pullback for this open immersion and has no degree shift. This extends the prior restricted operation list by a standard explicitly typed map.

There is a matching diagram

    Z^p(X)_Q -> product_i Z^p(U_i)_Q
                       -> product_(i<j) Z^p(U_i intersect U_j)_Q,

where the last map is the difference of the two restrictions. No quotient by rational equivalence has yet been taken.

## All-cycle necessity and effective gluing at this scope

Every compatible tuple of actual local cycles has a UNIQUE global cycle. Proof: an irreducible local support has a unique irreducible closure Z in X, with the same codimension. For each global Z define S_Z={i: Z intersects U_i}. Each nonempty Z intersect U_i is open in irreducible Z. Every finite intersection for indices in S_Z is therefore nonempty. Compatibility on overlaps forces one coefficient for Z throughout S_Z. Use that coefficient globally. Only finitely many global closures occur because the cover and each local cycle are finite. Restriction recovers the given tuple, and the covering property gives uniqueness.

Consequently the matching map onto compatible local ACTUAL cycles is surjective in every p. Its fibers are singletons. Singular supports and rational coefficients of either sign cause no exception; irreducibility of each component, not smoothness of the support, supplies the overlap argument. Bare Zariski gluing of already compatible actual cycles cannot yield the desired empty alpha fiber.

The augmented Cech complex is also exact for this finite cover. Decompose by global irreducible support Z. Its coefficient complex is the augmented simplex cochain complex on the nonempty set S_Z, contracted by choosing an index in S_Z. Direct sums preserve exactness over Q; finite cover products commute with these direct sums. This proves the result independently of finite numerical samples. It is a statement about cycle groups, not Chow groups or cohomology classes.

## Where a genuine loss occurs: quotient before matching

Restriction descends to CH^p(U)_Q, but the presheaf U -> CH^p(U)_Q is not generally a sheaf. Actual-cycle equality on overlaps and equality modulo rational equivalence are different matching conditions.

A concrete control is X=P1_C with U0=P1 minus infinity and U1=P1 minus zero. Both are affine lines; their overlap is G_m. In codimension one,

    CH^1(P1)_Q = Q,
    CH^1(U0)_Q = CH^1(U1)_Q = CH^1(G_m)_Q = 0.

A point has degree one and nonzero global class, yet both local Chow classes vanish. Thus passing to local Chow classes loses global information for an indisputably algebraic divisor. It is not an empty-realization example or failure of Hodge: all these local zeros have a global zero representative as well as the point's global class after restriction.

The retained gluing datum is visible in the line-bundle description. On the overlap, invertible regular functions are c*t^k. Units on either affine chart are constants, so transition exponents k survive changes of regular trivialization. The transition t represents a degree plus or minus one line bundle according to chart convention; its nonzero absolute degree is what matters. Algebraic Picard descent retains the transition and cocycle data that the list of local isomorphism classes discards. For this two-chart cover there is no independent triple-overlap condition with distinct indices; this does not erase the transition datum.

Likewise H^2(P1(C),Q)=Q while H^2(C,Q)=H^2(C*,Q)=0. Cohomological descent uses complexes/hypercohomology and lower-degree overlap data, not just the sheaf of degree-two groups. The omitted overlap contribution cannot be inferred absent from a zero local degree-two readout.

Imported standard facts here: open flat restriction of cycles, Picard/CH^1 identification on smooth varieties, Pic(P1)=Z, Pic(A1)=Pic(G_m)=0, the stated unit groups, and singular cohomology of the sphere/affine line/punctured line. The checker validates the finite incidence and exponent arithmetic; it does not formalize these algebraic theorems.

## What changes in the conjecture net

This supplies an actual source map and a universal all-cycle gluing theorem at a narrow scope. It refutes the candidate that strict compatible local cycles themselves fail Zariski gluing. It also exhibits a source-grounded loss at the passage to local quotient CLASSES, already in p=1. Neither result rejects the broad domain-erasure or higher-matching conjectures.

The next concrete test is to retain the rational-equivalence witnesses rather than the local Chow quotients: start with divisors of rational functions and their relations, formulate the comparison with the cycle-class complex, and determine what a genuine missing filler would mean. For codimension three the relevant candidate is the higher-cycle/localization complex, not a demand for arbitrary Chow representatives to be recoverable. This is a construction task with existing cycle-theoretic operations, not an external-data request. No higher-cycle obstruction on alpha is asserted yet.

## Issue-level disposition

Problem: source-bound local-to-global obstruction beyond cohomological readout.
Candidate: actual cycle restrictions can match locally but fail globally.
Rivals: strict cycle descent is effective; quotienting before descent forgets gluing witnesses; the forgotten witness is present even for algebraic classes.
Risky test: derive the support-wise matching complex and test a nonzero algebraic class with zero local Chow readouts.
Result: strict cycle descent closes, while the P1 quotient control loses degree. Requiring local quotient readout faithfulness would therefore wrongly exclude a known divisor.
Residual: compare witness-retaining cycle complexes with cohomology; no nonzero rational class-level Hodge obstruction has been found.

Verification: exact simplex cochain matrices for all nonempty support patterns in covers of size one through five, deliberate mismatched-overlap controls, and transition-exponent arithmetic. No proof-assistant certification or independent review.
