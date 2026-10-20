# Continuation sides: requests, synchronization, and an obstruction

## Constructed on the existing comparison carrier

For any actual `Body.compare m a b e p h` and any value z of its retained carrier, write s for the source reader and t for the existing target reader. The retained comparison witness gives `act m (s z) = t z`.

`agda/ContinuationSidePolicies.agda` constructs:

- `Out (s z) ≃ Out (t z)`, composing the existing mode edge equivalence with transport along that actual port path;
- synchronized pairs `Σ u : Out (s z), Σ v : Out (t z), route u = v` equivalent to either one-sided request type;
- a counterexample to identifying the raw source port with the target port, on the original A/B exchange;
- an independent pair with no synchronized preimage under the actual forgetful map.

The last pair is source **AB** and target **BC**. The original exchange sends AB to **BA**, not BC. The endpoint discriminator proves the mismatch, including transport along the actual port path. Local Vertex sethood is used only to compare that port path with reflexivity; no native history sethood is assumed.

The synchronized equivalence retains the witness: the inverse adds the canonical matching request and reflexivity, and its inverse law contracts the retained equality path. This argument does not discard proof data by fiat.

## Exact interpretation

The existing target-side convention remains unchanged. Mode-adjusted source requests and target requests carry equivalent pointwise request information. A synchronized both-side policy presents the same request information. An **independent** both-side policy permits the exhibited incompatible pair, so forgetting synchronization is not surjective.

This is not a proof that no abstract equivalence whatsoever exists between the independent and synchronized types. Nor does request equivalence identify native operations or choose a policy. Both the existing operand equivalence and its port-compatibility witness remain supplied parameters; this packet does not certify their origins.

No new task, graph relation, topology, seed or native rule was supplied. The examples use the existing graph and comparison. No existing Body reader or native adapter was modified.

## Verification

    python research/strominger/checkers/check_continuation_side_policies.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,323-file manifest. Three controls reject raw-source/target reflexivity, synchronizing arbitrary independent requests by reflexivity, and routing AB to BC using the BA computation. All report `UnequalTerms`. Dependency warnings are recorded; no repository-source warnings were reported.

- Contract: `contracts/continuation-side-policies.v1.json`
- Receipt and manifest: `results/continuation-side-policies/`

## Net disposition and executable continuation

A constructed support node records this bounded request classification. `policy-classification` remains open: pointwise request equivalences are not native policy-program comparisons or independently justified task selection.

Next, construct an explicitly named source-indexed continuation adapter using the derived request equivalence, retain its actual native premises, and compare it to the original target adapter with return-port and attachment laws. It must be labelled a separate adapter, not a redefinition of Body. Independent-pair admissibility needs an explicit synchronization requirement or a different task contract. No unique policy should be inferred from the completed source-composition coherence.
