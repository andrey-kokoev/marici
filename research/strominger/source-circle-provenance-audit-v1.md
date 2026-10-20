# First topology-changing step: source-circle provenance audit

Owner: `marici.Strominger`. Bounded audit of the **first retained circle**, not a reconstruction of the join/action/orbit tower.

- [Parameter ledger and scope contract](contracts/source-circle-provenance-audit.v1.json)
- [Checked audit source](agda/SourceCircleProvenanceAudit.agda)
- [Fresh verification](results/source-circle-provenance-audit/verification.json)
- [Dependency manifest](results/source-circle-provenance-audit/dependency-manifest.json)
- [Current research net](contracts/wg-source-determination-conjecture-net.v1.json)

## Executive finding

**The missing interface is a span/parameter policy, not an unavailable circle constructor.**

The predecessor already constructs a nontrivial retained circle. Its chosen two-attachment span is independent of the native six-arrow graph. The original twelve native schemas can faithfully carry that already-formed circle as an E index, and retain the graph provenance, without deriving the index's topology from the graph.

A source-sensitive contrast is also feasible: under the explicitly chosen program `Unit <- Out(v) -> Unit`, the same graph gives a circle at A/B and a contractible space at C/D. This program remains an additional adapter/realization policy. The tested one-step source covariance condition does not select it over the constant-circle policy.

## 1. What was actually reused

`ClosureGluingTreeRegression.agda` defines two constant maps `Bool -> Unit`, a refined two-label boundary, and their homotopy pushout. Its `preservesLoop` and `gluedLoopNotRefl` retain and distinguish the two attachment paths. Those exact declarations are included in the fresh closure of this audit.

The first topology-changing constructor in that selected program is `glueNode`, interpreted as an actual homotopy pushout. Its inputs are discrete; the output has a nontrivial loop. This is not the native `Body.attach` dependent-sum interpretation.

The distinction between construction and comparison is important. The existing `circleEquiv` identifies the constructed pushout with S1 using standard pushout/suspension equivalences. The audit's `rawTree` instead targets the actual pushout and uses the identity local equivalence. A supplied sphere target or sphere equivalence is therefore not needed to assemble this first pushout.

However, the generic `Tree` interface is not a source-generation certificate by itself: `leaf : Tree A n` permits any ambient A; Sigma/Pi indices, spans and local realization equivalences are also parameters. This does not invalidate the actual discrete-input circle construction. It prevents treating arbitrary Tree membership as proof of generation from the six-arrow source.

## 2. An exact obstruction—and its exact scope

`no-full-circle-equivalence` proves that no interpreted carrier of the classified `Fragment` is equivalent to the actual retained circle `Full`. `no-raw-circle-equivalence` gives the corresponding statement for the raw pushout.

Reason: the fragment theorem supplies sethood; an equivalence would transfer it to the circle and force the retained nontrivial loop to equal reflexivity.

This rules out the candidate **carrier-preserving equivalence** between the finite-reader interpretation and that circle. It does not rule out:

- a topology-changing operation;
- a realization that changes objects or takes a homotopy colimit of a diagram;
- a noninvertible map;
- higher structure in raw histories, Code, universes or classifying spaces;
- constructions in unrestricted native WG.

Thus the right response is to specify a different operation/realization contract, not silently rename the existing dependent extension as a pushout.

## 3. Native encoding is available—and does not establish source dependence

The generic `Envelope` control takes:

- an actual admitted package q and derivation d;
- a proof that its interpreted carrier is a set;
- an **already formed** type X and selected x:X.

The unchanged E/reflexivity rules derive a package interpreted as

```text
Sigma (z : X) (value(q) = value(q)).
```

The particular projection to X is an equivalence because that loop fiber is contractible. This reuses the existing faithful-envelope mechanism; it is not a new general expressibility principle.

Set X to the predecessor's raw circle. For each original endpoint seed, `NativeCircle` gives an actual original-`Seeds` derivation. `parent-retained` proves exact recovery of the preceding graph-pointed native package and derivation. The graph has not been erased.

Now hold X and the ambient operations fixed, and replace the initial source by an explicitly declared **Unit seed policy**. `seed-ablation` proves equivalence of the resulting circle carriers. Unit is not added to the original Seeds, and the native Rule datatype is unchanged.

**Interpretation:** in this particular encoding program, the graph is retained as provenance but is not necessary for the output's circle homotopy type. That topology entered in X. The complete packages and source policies remain different; future observers of their retained provenance can distinguish them. This is not a claim that the graph is irrelevant to all tasks or constructions.

The set-valued-input assumption matters: for a non-set input q, its loop fiber need not be contractible, so the same projection need not preserve only X.

## 4. A source-sensitive contrast, with its extra policy exposed

To test more than a source-independent encoding, the audit fixes one uniform alternate program:

```text
SourceSuspension(v) = Pushout(Unit <- Out(v) -> Unit).
```

The shared boundary is computed from the actual six-arrow source. The two Unit endpoints, their constant maps and the use of homotopy pushout are **declared additional policy**, not consequences of bare native retention.

The checked classifications are:

| Pointed source | Actual outgoing boundary | Output homotopy type |
|---|---|---|
| A | AB, AD | S1 |
| B | BA, BC | S1 |
| C | CA | Unit |
| D | DB | Unit |

`A-not-C` proves that the A and C outputs are not equivalent. This is a homotopy-type theorem, not an inference from Betti-number enumeration.

This experiment varies the **pointed source input** while holding the graph and the new program fixed. It is not an edge-deletion or whole-graph ablation. `source-covariance` supplies equivalences along the actual sigma source symmetry, consistent with the two source orbits.

`NativeSuspension` faithfully encodes these computed pushouts using the original native Seeds and twelve rules. Thus this is a feasible new parameter-program adapter without a new native rule. It is outside the old finite-reader adapter because its E index is now the constructed pushout rather than Out(v).

No preferred initial vertex/orbit, suspension policy, circle group action, physical state count or physical dynamics is derived by this test.

**The observation contract must also change.** `no-old-discrete-ports` proves that a Vertex-valued reader on `SourceSuspension A` cannot assign A to its left endpoint and B to its right endpoint: the new AB pushout path would force A=B. Edge labels and source provenance remain in the construction, but they cannot silently become these distinct discrete value observations on the realized space. A different or dependent observation interface, or separate retained construction-level labels, must be specified. Faithful native encoding of the new pushout does not supply the old Body port contract.

## 5. A concrete nonselection result

Both policies have the tested one-step sigma-covariance equivalences:

1. constant raw-circle output;
2. the Out(v)-pushout family.

`policies-differ-at-C` proves that their outputs at C are inequivalent. Therefore **that covariance requirement alone does not select a span policy**.

This does not refute every possible stronger source-selection condition. It also does not claim that this audit has supplied all-dimensional coherent group actions for both policies. The counterexample is precisely to selection by the explicitly tested covariance condition.

## 6. The join-tower evidence boundary

The imported source-join note explicitly chooses the later complete projection span `A <- A x C -> C`. It reports its adapter as uncompiled and leaves all-dimensional action/orbit/colimit interfaces outside the candidate.

A bounded current search under `research/` finds no `WGCircleJoinIntegration.agda`. This audit does not reconstruct or compile that absent candidate. Its absence is not an impossibility proof. Nor does the new first-circle closure retroactively verify the note's entire join, action, orbit or colimit programme.

The first-circle result is sufficient to locate the policy boundary; compiling a whole tower would not by itself resolve it.

## 7. Verification and limitations

```sh
python research/strominger/checkers/check_source_circle_provenance_audit.py
```

Fresh safe Cubical headless closure passes, including the actual predecessor circle/nontrivial-loop sources. The driver records exact commands, compiler hash/version, input hashes and a conservative **2,286-file** include-root/primitive inventory across the required owner source directories. Inputs remain unchanged during verification; no other-owner source implementation is edited.

Three intended negative controls fail with `UnequalTerms`: treating a fragment normalizer as a circle equivalence, applying the A-circle classification uniformly at C, and treating the replacement Unit seed as a member of the original Seeds.

Cubical dependency indexed-match warnings are recorded; repository sources have none. Small cellular controls check the two-versus-one attachment counts and source permutation. They do not replace the formal homotopy equivalences and inequivalence proofs.

## 8. Feasibility verdict and next decision

| Proposed next move | Verdict |
|---|---|
| Identify the finite-reader value carrier with this circle by equivalence | **Obstructed** at that exact interface. |
| Encode an already formed circle with the existing native rules | **Constructed**, but it does not establish source determination. |
| Use the explicit Out(v)-span parameter program | **Constructed conditional adapter**, with genuinely source-sensitive outputs. |
| Claim the source/covariance uniquely selects that program | **Not justified**; two tested policies disagree. |
| Build the full join/action/orbit tower next | Not required to resolve the present policy question; the cited adapter is absent/unverified here. |

**Recommended next task: policy classification at the span-program and reader boundary.** State an independently motivated realization task, the admitted parameter-program constructors, and which boundary observations must descend. Then either certify the Out(v)-span relative to that contract or retain both programs as members of a derived family of alternatives. Specify any additional selection condition explicitly; do not choose it merely to obtain a desired circle or gauge target.

Canonical finite comparison synthesis remains useful supporting infrastructure. The audited bottleneck for richer interpreted content is now explicit: which span/type-building programs are authorized and why—not the absence of an existing circle or another local coherence witness.
