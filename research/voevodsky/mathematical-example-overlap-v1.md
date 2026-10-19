# Finite/RH example overlap: policy-indexed realization semantics

Target: `math:mathematical-realization-example-assembly`.
Checker: `research/voevodsky/checkers/check_mathematical_example_overlap.py`.
Receipt: `research/voevodsky/results/mathematical-example-overlap-v1.json`.
Run: `uv run research/voevodsky/checkers/check_mathematical_example_overlap.py`.

## Reviewed bounded disposition

The two registered bindings share a **policy-indexed typed-operation and retained-history semantics**. This is a registered bounded semantic assembly, with formal outcome left null, not a translation of classical analysis into Cubical Agda, a common native source, or an implementation of every general dependent-payload obligation.

The frozen general interface explicitly permits distinct evidence policies. Accordingly, validity means a named judgement with its source, premises, domain, evidence policy and verification status retained. It does not mean that an analytic argument can be consumed as an Agda proof. If the assembly were required to supply one unindexed proof kernel or a source-identifying functor between the examples, these witnesses would not meet that stronger gate.

## Common semantics, not just shared field names

Fix a source tag d, typed states S_d, licensed operations with guards, and retained witnessed histories. A presentation map F comes with its actual target operation and a square

    F(op(s)) = op_view(F(s))

on the declared admitted domain. Availability guards must also agree. Source recovery is an additional witness, not a consequence of the square. A history view maps each retained state and witness; it does not replace the history by its terminal state.

History composition is concatenation only when the source tag and intermediate state match. A step square induces a finite-history square by induction: the empty history is immediate; extend by applying the given one-step square to the current endpoint. Since mapping a concatenated list equals concatenating the mapped lists, the history view preserves composition and units. This elementary argument does not assume every source relation already has a single-edge composition law.

For an observational quotient q, the separate obligation q op = op_q q supplies future-safe equality under that licensed operation, by induction. It does not supply source recovery. Neither example may substitute current output equality for full retained identity.

These are common mathematical conditions with policy-indexed evidence, not an asserted isomorphism between the source models.

## Two actual instantiations

| Obligation | Finite WG | RH endpoint/analytic view |
|---|---|---|
| Typed source | Tagged requests and dependent responses of the supplied compiler | Declared real endpoint space with M and the generic finite analytic attachment J |
| Actual operation | Evaluate a request; leave a response idle | Native M, transported as J M J^-1; not Fourier |
| Reversible presentation used in overlap test | Six-state Boolean encoding retaining phase, index AND actual output | Invertible J on the declared finite generic image |
| Step/continuation square | Independently written six-entry transition table agrees with actual compute/idle semantics | (J M J^-1) J = J M; exact one- and two-step squares recomputed |
| Histories | Source Agda theorem retains length despite stationary response endpoint; exact finite regression checks concatenation and decoding | A typed route/retained archive is not discarded when analytic observations agree; the common finite-history lemma applies to the displayed square |
| Task quotient | No index-only or endpoint-only complete-identity assertion | Z=[ell;ell M] satisfies Z M=T Z, with nontrivial kernel; scalar ell alone fails |
| Law provenance | Boolean law by cases; category composition/laws supplied; compiler certificates recover supplied proof | Source matrices supplied, finite squares constructed; analytic theorems imported with domains |
| Validity | Safe Cubical Agda plus bounded executable regression | Exact finite algebra plus owner-qualified classical analysis; no invented formal kernel certificate |
| Completion/resources | Finite history length; no analytic completion or general complexity theorem | Fixed finite models, declared mesh/core/rigging and imported completion proofs; no global Hilbert/raw-comb substitution |

The category pilot need not have finitely many objects or arrows. The six-state executable test is specifically Boolean; the generic compiler's request/response and proof-retention facts come from the existing parameterized Agda theorem. The assembly does not turn finite enumeration into a category theorem.

## Newly exposed hostile: request retention alone is insufficient

The actual compiler permits response(i,y) for ANY y : Output(i), not only outputs reached from a request. In the Boolean instance, response(false,false) and response(false,true) are both legal states and both remain idle. Erasing y and keeping only phase/index collapses states with different observable output. Recomputing not false cannot recover the first one.

Thus a view omitting the output needs either an explicit reachable-state restriction with evidence, or a retained output/recovery witness. The accepted overlap encoding keeps all three fields and covers all six typed Boolean states. This strengthens the source-retention audit without changing the existing compiler or its claims.

A second hostile retains the familiar one-step versus two-step history: same endpoint, different retained trace. On the RH side, Z has a two-dimensional kernel, so even its correct continuation action is not complete identity. These are the same distinction between source recovery and task observation, instantiated differently.

The checker also rejects attempted joins across source tags even when numerical endpoint labels agree, and joins within a tag with mismatched intermediate states. No physical-source or WG/RH carrier identification is inferred.

## Verification and scope

The checker revalidates the finite proof receipt and its source hashes, reruns the RH binding validation and its exact continuation checks, and performs 150 finite history-composition/view-recovery cases (six states, two lengths each ranging from zero through four). It recomputes the RH one/two-step squares, quotient square and kernel preservation symbolically. Arbitrary finite lengths follow from the stated induction and existing finite compiler theorem, not the regression cutoff alone.

No new Agda closure is run for this overlap checker; the existing compiled receipt is reused with explicit freshness checks. No new analytic interval computation is claimed. The unchanged-Evans rejection, non-unit normalization restrictions, native/Fourier distinction and completion restrictions remain in the RH binding; category laws remain supplied in the finite binding.

## Unresolved stronger claims

Neither binding instantiates arbitrary dependent payload families in one common foundation. The shared interface describes that optional/general layer, but the bounded witnesses supply only their stated indexed records and operations. Full native dependent syntax, cross-foundation interpretation, common physical source, positive Weil pullback, RH truth and universal coverage remain outside this assembly.

Review conclusion: the acceptance is met at the declared policy-indexed scope. The examples preserve the same distinction between actual operations and observations, and between complete identity and continuation-safe task quotients. Their different proof policies are explicit parameters of the frozen interface, not silently interchangeable meanings of validity. The falsifier remains effective against erasure of response outputs, histories, guards or source tags.

Five registration controls reject universal, cross-foundation, arbitrary-payload, parent-discharge and formal-outcome promotion. The bounded assembly is a contribution to the parent mathematical branch, not automatic closure of the universal parent. Continue at the freshly ranked parent/work-net frontier.
