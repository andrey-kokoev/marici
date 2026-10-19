# F41 disposition: one rejected representative, one positive opposite-type factor

## Question and claim boundary

The preregistered prediction in `hodge-fourth-prime-controls-v1.md` was that BOTH tested sources have no additional geometric E_i at41. The fresh counts refute that prediction for(2,-1554,2), while establishing CM absence for(2,3087,2). This packet audits the positive factor rather than deleting the failed prediction or treating it as a complex lift.

The first count receipt is `results/hodge-fourth-prime-controls-v1.json`. The follow-up is `results/hodge-fourth-prime-type-audit-v1.json`. The latter recomputes exact polynomial/type/projector algebra from the first receipt; it does not independently replay extension fields. Neither packet changes the main net at iteration51/pins v54.

## Disposition

| Actual source | a mod41 | extra geometric E_i multiplicity | consequence |
|---|---|---|---|
|(2,3087,2)|12|0|excluded even up to unpolarized Y3 isogeny|
|(2,-1554,2)|4|1|necessary typed screen survives; no complex axis supplied|

The extra factor at a4 has OPPOSITE native type, not the same type. The full cyclotomic certificate has only order1, multiplicity2 in the norm polynomial; Gaussian native GCDs have degrees0 for beta and1 for conjugate(beta). Its eigenvalue is gamma=5-4i, with beta=5+4i.

For a4 the sevenfold Gaussian polynomial has descending coefficients

    [(1,0),(1,0),(-55,20),(-191,-44),(779,-984),
     (14555,-4920),(-8405,6724),(-344605,275684)].

For a12 they are

    [(1,0),(1,0),(-23,-12),(1,-140),(-565,-696),
     (2747,-6232),(-8405,6724),(-344605,275684)].

Their rational traces through degree5 are respectively

    [-2,222,814,3182,-48802], [-2,94,-146,6254,-54242].

The fifth traces are fresh controls, not reconstruction inputs. At a12 the full55-order ratio certificate has no positive cyclotomic factor. Injective good specialization excludes the two-E_i complex target, as proved in the count packet. This supplies the algebraic integral residue boxes(2,12,2) and(2,12,39) at41. It does NOT exclude every lift of the previous mod8177 class3087, nor every lift of class6623 represented by-1554.

## Polarization audit of the positive control

The full P8 polynomial is f8=(T-beta)f7. Construct the unique opposite-line spectral idempotent e=r/r(gamma), where f8=(T-gamma)r. Exact rank-one, idempotent, eigenvalue and Rosati self-adjoint identities hold with T^dagger=41/T. The derivative is

    r(gamma)=2899968-1413120i,
    Norm(r(gamma))=10406722535424,
    v3(Norm(r(gamma)))=2.

Its polynomial coefficients are not all3-integral, but3e has integral coefficients. A nonintegral polynomial presentation does not prove that the actual lattice projector is nonintegral. Consequently this is not the unit-projector veto.

Under the additional hypothesis that a primitive opposite complex elliptic axis exists, specialization puts its saturated Tate lattice in this unique opposite line. In the perfect ambient lattice, restriction to its dual is onto; the orthogonal projector image is d^(-1)M up to a unit, where d is the restricted elliptic theta degree. Integrality of3e gives0<=v3(d)<=1.

Under the further hypothesis of an unpolarized isogeny to the FIXED Y3, the retained norm-parity argument requires v3(d) odd: source P8 is principal, its actual known axis has degree4, and the fixed sixfold has End^0=Q(i), signature(3,3), and Hermitian determinant class-3. The argument allows either K embedding and does not assume the target isogeny K-linear; sixfold polarization rescaling changes its determinant by a sixth power. Hence the conditional necessary value is v3(d)=1. This is not existence, full degree6, a joint kernel or identification of the residual sixfold.

## Scoped CRT refinement

On the integral a line with lambda2,b2, lift the old mod8177 partition to modulus335257=8177*41. Exclude the old negative classes and the new a41=12 class. Jointly certify a necessary class only when the old three-prime model/screen is certified and a41=4. The complete partition of this INTEGER residue domain is

    331257 excluded (100 more than the lifted old rule);
         2 jointly certified necessary classes:297459,333703;
        78 old-certified classes with41 uncounted;
      3920 old-uncertified classes not excluded by41.

Thus3998 classes remain uncertified or uncounted; the two joint certificates do not exhaust possible complex sources. Their centered representatives are-37798 and-1554. The least-absolute jointly certified representative stays-1554. In particular the old class3087 is not eliminated: its lift-37798 now has the counted41 profile a4. The checker retains a classification hash and reconstruction rule, not a claim that all41 models have been counted.

## Residual

The actual source(2,-1554,2) has now survived the necessary CM/type/polarization tests at13,17,37,41. The failed absence prediction is retained as a falsification, not converted into target evidence. The first missing geometric object is still an actual opposite-action complex map/axis. An alternative executable test is the remaining41 profiles of the previous necessary classes; only a4/a12 have been counted here. The98 prior model-uncertified classes and other parameter/source routes are not disposed of by these two counts.

No Hodge proof/refutation, target cycle, source End/simplicity computation or fixed-X6 match is claimed. SCC verifies the declared computation and dependency scope, not these missing constructions.
