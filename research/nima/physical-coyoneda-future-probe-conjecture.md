# The physical co-Yoneda future-probe conjecture

## Provenance

This conjecture was not introduced as a categorical analogy. It arose after
the exact UDW–QND comparison and capability-fiber calculation established:

1. physically different instruments can induce the same complete one-use
   outcome law;
2. they leave different successor states;
3. controlled future probes distinguish those successors;
4. an informationally complete family of future probes reconstructs the
   successor ray.

The Operator then reported:

> “Yoneda Lemma is what I was going to mention in some future, but I sense
> it has arrived at us itself.”

This is an operator intuition and recognition report, not mathematical
evidence. Its bounded consequence is to formulate and falsify the weakest
precise Yoneda-shaped claim already demanded by the calculation.

## Exact result already established

For the fixed click effect

[
E_1=s^2|1anglelangle1|,
]

the compatible rank-one click capabilities include

[
K_1(psi)=-is|psianglelangle1|,
qquad [psi]inmathbb{CP}^1.
]

One-use probabilities are independent of ([psi]). Sequential (X,Y,Z)
analyzer probes recover the Bloch coordinates of ([psi]). Thus, in this
bounded model,

[
	ext{same present record law}

otRightarrow
	ext{same capability},
]

but

[
	ext{same responses to an informationally complete future-probe family}
Rightarrow
	ext{same capability ray}.
]

This finite statement is verified in
`research/nima/checkers/check_instrument_capability_fiber.py`.

## Categorical typing

Let (mathcal C_{m phys}) be a category whose objects are typed physical
states or situations and whose morphisms are admissible interactions.
Classical record systems form distinguished target objects or a record
functor. For a successor object (X), outgoing future probes define the
covariant representable functor

[
h^X=operatorname{Hom}_{mathcal C_{m phys}}(X,-).
]

This is the **co-Yoneda** orientation: future probes leave (X). The ordinary
incoming representable (operatorname{Hom}(-,X)) is equally legitimate, but
it describes preparations or past interventions rather than future probing.

The unrestricted co-Yoneda embedding is fully faithful. Physics, however,
usually exposes only an admissible probe subcategory
(mathcal Psubseteqmathcal C_{m phys}), and often only a record-valued
image of each Hom-set. Therefore Yoneda's lemma alone does not prove
operational distinguishability.

## Weakest falsifiable conjecture

### Physical co-Yoneda future-probe conjecture

For each physically admitted sector, there exists a source-derived class of
future probes (mathcal P_S) and a coherent record functor such that two
successor capabilities are physically equivalent exactly when their induced
record histories are naturally equivalent under every probe in
(mathcal P_S):

[
Xsimeq_{m phys}Y
quadLongleftrightarrowquad
mathsf{Rec},operatorname{Hom}(X,P)
simeq
mathsf{Rec},operatorname{Hom}(Y,P)
quad	ext{naturally for all }Pinmathcal P_S.
]

For two interaction morphisms (f,g:A	o X), the corresponding relative
claim is that they are physically equivalent exactly when every admissible
postcomposition produces naturally identical record histories.

The words **source-derived**, **naturally**, and **every admissible** are
essential. A fitted probe family, an arbitrary tomography basis, or
presentation-dependent equality would not establish the conjecture.

## What it would explain

If true, the conjecture explains why composition has repeatedly been
indispensable in Marici:

- present records are lossy projections;
- successor states encode counterfactual future possibilities;
- composition converts those possibilities into later records;
- naturality makes the identification independent of presentation;
- physical identity is extensional with respect to all admissible
  interactions.

In civic language:

[
oxed{
	ext{what an event is includes what every legitimate future interaction
can make of it.}
}
]

The future does not alter the past. Later probes reveal distinctions in the
past interaction's successor state that its immediate public record erased.

## Falsifiers

The conjecture fails, sector by sector, if any of the following occurs:

1. **Nonseparation:** two inequivalent source capabilities remain
   indistinguishable under every source-admissible future probe.
2. **Nonnaturality:** the distinguishing histories depend on chart, gauge,
   framing, or representative.
3. **Nonclosure:** admissible probes do not compose into admissible histories.
4. **Record collapse:** the physical record functor identifies capabilities
   that the theory itself requires to remain distinct.
5. **Extra-probe dependence:** separation requires an analyzer or coupling
   not derived from the physical source.
6. **Contextual inconsistency:** probe histories cannot be glued across their
   overlap contexts.

The UDW–QND pilot establishes separation only after adding controlled analyzer
probes. It does not yet prove that Marici's Carrier derives those probes, so
the current status is:

[
oxed{
	ext{finite supporting model}
+	ext{precise cross-sector conjecture},
quad
	ext{not a Carrier theorem}.
}
]

## Next bounded test

Use a sector whose source already supplies sequential operations. Construct:

1. its category of states and interaction morphisms;
2. its source-admissible future-probe subcategory;
3. its record functor;
4. a candidate pair of inequivalent successor capabilities;
5. the finite probe-signature matrix.

Then test whether that matrix separates the capabilities and whether the
separation descends through every declared sector equivalence. The radiative
memory sector is a useful negative control because its current “detectors” are
dual pairings, not yet state-transforming apparatuses.
