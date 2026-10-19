# The segmented construction needs fourteen selectors and a retained preparation residual

**Strength:** exact finite controller, preparation and graph-symmetry audit. An explicit conditional implementation with retained rejection records, not a source-derived physical interaction or emission probability.

[Previous construction](SEGMENTED-COPY-TRANSPORT.md) · [Checker](check_controller_preparation_audit.py) · [Receipt](results/controller-preparation-audit.v1.json)

## 1. Question and tested operation class

The segmented unchanged-copy construction supports a synchronized reference-mode plane. It still supplies its controller and correlated preparation. This audit asks which parts follow from unrestricted endpoint extension, which require additional supplied records, and whether the static glued graph's symmetries select the preparation.

The tested operations are the existing retained-path ledger's endpoint composition with neutral or explicitly supplied right payloads, exact coordinate-record splits, and directed graph automorphisms. This is not a classification of all source interactions. In particular, the physical seed metric, dynamics and measurement theory are not replaced by a counting model.

## 2. Four forced contexts, fourteen genuine selectors

The finite controller has twelve macro-boundary states and six internal states. Given a state, its current macro-word fixes the next primitive arrow. Compare that arrow with the unrestricted outgoing primitive registry at the same vertex:

- at fourteen states, there are two available primitive arrows and the controller chooses one;
- at four states, only the required primitive arrow is available.

The fourteen branching contexts lie at A, B or C. The four forced contexts lie at D, E, Ep or Dp. The receipt lists the expected and rejected primitive IDs for every context.

Thus the controller is not just endpoint matching. For example, inside AC=(AB,BC), after AB reaches B the primitive extension rule also permits BA. The macro dictionary forbids that exit until the composite is complete.

This audit concerns the primitive choice **given an existing context**. It does not derive the next macro-context choice, its pair label, or the preparation of the context memory.

## 3. Implement the selector without erasing rejected histories

Use the actual `RetainedSuccessorLedger` and its existing coefficient multiplication:

1. retain a compatible incoming prefix;
2. compose it with the full primitive right family carrying coefficients one;
3. separately compose with a supplied indicator right family, coefficient one on the context's expected primitive and zero elsewhere;
4. compose with the complementary indicator to retain the rejected branch.

The accepted and rejected payloads have exactly the same full word carrier as the unrestricted extension. Forbidden words remain present with zero accepted coefficient. Both indicator records and parent bindings remain registered.

If E is the unrestricted extension, then coefficient-by-coefficient

    E = E_accept + E_reject.

The two branch records have disjoint coefficient support. Under the declared counting metric their squared norms add to the unrestricted squared norm. Recovery therefore requires retaining the rejected record, not inventing an inverse of a projection.

**Crucial provenance:** the ledger records every indicator as a **supplied** leaf. The API can express this control operation; it does not derive its physical availability from the seed. Reindexing or neutral copying alone does not remove the unwanted nonzero extension.

For a unit prefix and equal-copy extension, the accepted counting-norm fraction is 1/2 in the fourteen branching contexts and 1 in the four forced contexts. These are bookkeeping ratios on a specified basis extension, not physical success rates, scattering probabilities, or independent repeated-trial factors. No detector, state normalization or Born-rule identification is supplied here.

## 4. The preparation has a six-dimensional rejected part

Retain the primitive coordinate order

    x=(a,b,c,d,e,f,g,h,i,j).

The synchronized mode inputs, with the previously unused d,g kept, have the form

    (alpha,beta,-alpha,d,-beta,alpha,g,beta,-alpha,-beta).

This is a four-dimensional subspace of the ten-dimensional free-coordinate model: two observable mode parameters plus two residual coordinates. For the **declared counting metric**, its orthogonal projector is explicit:

    alpha=(a+f-c-i)/4,
    beta =(b+h-e-j)/4.

Call that projector S. The exact checker verifies

    S^2=S, S^T=S, rank S=4,
    rank(I-S)=6, S(I-S)=0.

The preparation split

    x -> (Sx,(I-S)x)

is lossless: sum the two records to recover x, and their counting squared norms add. Retaining only Sx discards six independent directions. The primitive residuals d,g are already kept by S; they are not the six rejected directions.

A small falsifier is the a-only unit input. Its selected and rejected squared counting norms are respectively 1/4 and 3/4. The selected part is not the original state. This is not a 25% physical photon-emission prediction.

The projector is an explicit **candidate preparation selector**, derived from the desired synchronized input subspace for audit. It is not independently justified as a native state preparation or physical metric operation. Moreover it does not commute with unrestricted endpoint continuation on the supplied glued primitive registry. That operator itself remains combinatorial, not an identified physical law.

## 5. Static reflection symmetry is insufficient

The checker enumerates all 7! vertex permutations of the supplied directed glued graph, preserving its full directed edge set. There are exactly two graph automorphisms: identity and the reflection exchanging A with C, fixing B, and exchanging D with Ep and E with Dp.

The reflection's primitive permutation is

    a <-> i, b <-> j, c <-> f, d <-> g, e <-> h.

Let R be its permutation matrix. Then R^2=I, and the odd projector (I-R)/2 has rank **five**. The synchronized two-dimensional observable input plane is odd under this reflection. That is a compatibility result, not a selection theorem.

For example, e_a-e_i is also odd but fails the required synchronized preparation: its f and c coordinates do not match the preparation relations. The checker verifies that S changes this vector. Thus reflection parity alone cannot select the desired plane.

The full preparation S commutes with R, but symmetry-compatible projectors need not be uniquely chosen by symmetry. The extra restrictions remain additional structure. This automorphism audit concerns the supplied directed graph only; it neither classifies all geometric source operations nor promotes arbitrary signed coordinate averaging to a native operation.

## 6. Current conclusion

There is now an explicit conditional implementation that retains all the records previously at risk of being hidden:

- full primitive extensions and their forbidden branches;
- supplied context-selector payloads and their source parent bindings;
- the synchronized preparation and its six-dimensional rejected record.

What is **not derived** is the source interaction that produces those selector payloads, chooses/updates the macro-context memory and prepares the correlated input. Static endpoint matching and reflection parity do not suffice for these particular tasks.

The next gate is therefore concrete: identify an existing source interaction providing this control/preparation, or give a scoped obstruction within a stated source-operation class. It must account for the context memory and rejected records. A larger environment can store them conditionally, but merely postulating that environment or discarding its record would not derive an emission process.

No physical metric, triangle faces, independent photon sectors, annihilation or ratio 372 is established. Existing work-net contracts, pinned records and formal outcomes remain unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_controller_preparation_audit.py
python research/scattering/seed-composition/check_controller_preparation_audit.py --check
python research/scattering/seed-composition/check_segmented_copy_transport.py --check
python research/scattering/seed-composition/check_retained_word_transport.py --check
python research/scattering/seed-composition/check_incidence_audit.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker recomputes the preceding finite construction, exercises the actual path ledger, enumerates the graph symmetries, verifies rational matrix identities and hashes its dependencies. It writes only its own receipt; `--check` is read-only. No full source-owner scientific replay or central proof admission is claimed.
