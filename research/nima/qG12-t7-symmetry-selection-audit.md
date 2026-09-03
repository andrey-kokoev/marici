# `q_G12` `T7` symmetry-selection audit

## Question

Do the frozen source symmetries select a unique absolute lift of the sewn physical shared-wall cocycle from its rank-seven `T7` torsor?

## Claim boundary

The literal post-residue source form canonically determines a relative/open class `rho_phys`, independent of the IBP generating basis. It does not determine an absolute `T7` projection: the frozen localization artifact explicitly records that a section or retraction of the localization sequence is absent.

The exact sequence has ranks

\[
0\longrightarrow M_9\longrightarrow M_{15}\longrightarrow Q_6\longrightarrow0.
\]

After imposing zero elliptic quotient, lifts of the physical cocycle form a torsor under the rank-seven algebraic kernel `T7`. To test symmetry selection one needs an affine action on this torsor, hence both a linear action on `T7` and the translation cocycle determined by transport of a reference lift.

## Frozen symmetry evidence

The only explicit frozen action on the full algebraic `T7` sector found in the relevant source-normalized artifacts is generic nonsoft total-energy monodromy. It acts as the identity on `T7`. Therefore its fixed subspace has rank seven and it cannot select a unique lift.

The wall data do supply cyclicly related equations, oriented Čech closure, and a canonical relative source class. They do not supply a cyclic/permutation transport matrix on a common absolute `T7` basis, nor the affine translation cocycle for the physical lift torsor. Cyclic invariance of the quotient class does not induce an absolute equivariant section.

## Strongest falsification attempt

Demand invariance under every frozen symmetry already defined on `T7`. The only fully typed relevant action is identity monodromy, whose invariant subspace is all of `T7`. The uniqueness claim therefore fails: seven absolute directions survive.

A stronger cyclic test is undefined rather than failed because no common-basis `T7` cyclic transport and no reference-lift translation are present. Wall-by-wall coordinate formulas cannot be compared as an affine action without these maps.

## First missing arrow

The first missing datum is an equivariant localization splitting

\[
s:Q_6^{\rm phys}\longrightarrow M_{15}
\]

or, equivalently, a common-basis affine representation

\[
(R_g,c_g):T7\longrightarrow T7
\]

for each source symmetry generator, with cocycle identities and compatibility with the quotient map. Only then can one solve `(R_g-I)v=-c_g` and compute the dimension of the invariant affine locus.

## Acceptance test

1. freeze a common absolute `T7` basis and a reference lift;
2. provide exact cyclic/permutation matrices `R_g` and translations `c_g`;
3. verify group and affine-cocycle identities;
4. verify compatibility with the canonical relative class and source sewing;
5. solve the simultaneous fixed-point equations exactly;
6. exhibit a nonzero homogeneous invariant as a deliberate failure if uniqueness does not hold.

## Disposition

Known symmetry does not select the lift: identity monodromy preserves the full rank-seven ambiguity. Selection by cyclic symmetry is currently untyped because the required affine `T7` transport is absent. Physical lower-graph factorization cannot use symmetry as a substitute for a source-derived localization section.

## Evidence

- `research/benincasa/source-bases-localization-fiber.json`
- `research/benincasa/physical_shared_wall_no_canonical_t7_lift.py`
- `research/benincasa/total-energy-nine-master-residue.json`
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
