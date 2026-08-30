# Constructor equivalence is enriched-Yoneda faithfulness

**Owner:** marici.Kitaev  
**Status:** bounded closure theorem  
**Question:** Can complete contextual behavior reconstruct a constructor rather than merely its scalar shadows?

## 1. Resource-enriched constructor category

Let \(\mathcal K\) be the frozen constructor category enriched in a base \(\mathcal V\).

The enrichment may retain:

- attainable resource grades;
- ordered capability sets;
- error bounds;
- typed implementation spaces;
- or another source-authorized hom-object.

For objects \(X,Y\), the enriched hom-object is

\[
\mathcal K(X,Y)\in\mathcal V.
\]

Composition is a morphism in \(\mathcal V\), so resource and capability composition are part of the category rather than external annotations.

## 2. Enriched Yoneda theorem

Associate to every object \(X\) its representable contextual profile

\[
Y_X=mathcal K(-,X).
\]

Every constructor \(f:X\to Y\) induces a natural transformation

\[
Y_f:Y_X\Longrightarrow Y_Y
\]

by postcomposition.

The enriched Yoneda theorem gives

\[
\mathcal K(X,Y)
\cong
\operatorname{Nat}_{\mathcal V}(Y_X,Y_Y).
\]

Therefore a constructor is completely determined, within the frozen enriched category, by its natural action on every representable source context.

This is constructor-level faithfulness. It retains composition and enrichment, not only final outcomes.

## 3. Why scalar testers are weaker

A scalar tester applies an outcome functor after contextual composition.

Different natural transformations can have identical images under that outcome functor.

Examples already present in the programme include:

- destructive and nondemolition instruments with the same outcome law;
- operator lifts with identical scalar Tate sections;
- central readouts that agree while block actions differ;
- distinct ordered holonomies with the same trace or determinant;
- constructor routes with equal final cost but different catalyst return.

Thus scalar equality is a quotient of the representable contextual profile.

Enriched Yoneda applies before that quotient.

## 4. Bounded probe families and density

Let \(\mathcal P\subseteq\mathcal K\) be a selected probe subcategory. The restricted nerve is

\[
N_{\mathcal P}(X)=\mathcal K(-,X)|_{\mathcal P}.
\]

The selected probes reconstruct objects and constructors exactly when this nerve is fully faithful. This is a density condition on \(\mathcal P\).

Therefore “the finite tester family is complete” should mean:

> The restricted enriched nerve on the declared candidate category is fully faithful.

Injectivity on one labelled packet is a weaker, packet-specific result.

## 5. Input and output contexts

Some sectors probe by preparation before the constructor; others probe by observations after it.

A two-sided context profile can be represented by the action on hom-objects

\[
\mathcal K(P,X),
\qquad
\mathcal K(Y,Q),
\]

for admitted preparation objects \(P\) and observation objects \(Q\).

A bounded family must be dense or codense in the direction required by the claim. If both preparation and observation are restricted, their combined profunctor must be jointly faithful.

SCC should not use “tomographically complete” without specifying this variance.

## 6. Cross-sector readings

### Toric code

Syndrome probes are not dense on logical sectors. Adding two noncontractible loop probes is jointly faithful on the four logical classes, but this is packet-level faithfulness, not reconstruction of every physical operator.

### D(S3)

Central character probes see only the center. They are not dense for the endpoint block algebra. A transposition and a three-cycle port generate the full endpoint algebra, giving the finite algebraic analogue of a dense probe family on that declared object.

### Classical finite-state behavior

Words up to the product-state bound form a finite separating family for bounded machines. The representation bound makes the restricted behavioral nerve faithful.

### Instruments

Outcome probabilities alone are not dense for instrument semantics. The classical branch register and conditional transformations must remain in the enriched profile.

## 7. Self-closure of the tester tower

The full representable tower is faithful by theorem.

A bounded tester tower self-closes when a density theorem shows that every representable profile is reconstructed from the bounded probes.

This separates two proof obligations:

1. **Yoneda faithfulness:** complete contexts reconstruct the constructor.
2. **Finite density:** the selected bounded contexts reconstruct complete contexts.

The first is categorical. The second is sector-specific.

## 8. Authority and reality boundary

Yoneda reconstructs objects and morphisms of \(\mathcal K\). It cannot prove that \(\mathcal K\) contains every physically possible constructor.

A physical representation theorem must still establish that the frozen category is adequate for the claimed world.

Likewise, choosing a richer enrichment can manufacture faithfulness by storing the desired answer. Every enriched coordinate requires source occurrence and authority.

## 9. Hostile suite

1. **Outcome quotient:** distinct natural transformations have equal scalar outputs.
2. **Non-dense probes:** selected probes identify distinct constructors.
3. **Wrong variance:** preparations are complete but observations are not, or conversely.
4. **Packet overreach:** injectivity on one finite packet is promoted to full categorical density.
5. **Enrichment erasure:** minimal cost agrees while implementation, fault, or catalyst data differ.
6. **Unauthorized enrichment:** a new hom-coordinate is added solely to restore faithfulness.
7. **Physical incompleteness:** Yoneda is faithful internally while the category omits a real constructor.
8. **Completion failure:** finite density constants collapse in the completed enriched category.

## 10. SCC certificate

```json
{
  "constructor_category": "...",
  "enrichment_base": "...",
  "representable_profile": "...",
  "probe_subcategory": "...",
  "variance": "preparation | observation | two_sided",
  "restricted_nerve": "...",
  "packet_injective": "proved | failed | open",
  "fully_faithful": "proved | failed | open",
  "density_theorem": "...",
  "physical_representation_scope": "...",
  "completion_stability": "..."
}
```

## 11. Present conclusion

Constructor equivalence is equality of natural contextual action in the resource-enriched category.

Scalar and resource-profile equivalence are images of this action under forgetful outcome functors.

The correct finite closure question is therefore:

> Does the selected source-authorized probe family form a dense generator for the declared enriched constructor category?
