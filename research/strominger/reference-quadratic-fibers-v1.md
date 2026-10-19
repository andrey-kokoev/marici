# Sharper missing-reference fibers and smaller sufficient retention

## Structural question

The previous P/Q linear probe gate was sufficient, not necessary. Its failure did not by itself prove lost information. This experiment uses **all already retained scalar observations** before deciding what additional data to keep.

It extends [conditional reconstruction](field-reconstruction-v1.md), [reconstruction-aware transport](reconstruction-aware-tower-v1.md) and [reference transitions](field-reference-transitions-v1.md). The old verifier is not weakened: a new compact packet expands into its original validated contract.

## First recover the selected arrows

The existing P/Q/C arrow measurements recover the eleven selected triples up to a common phase and known positive normalization, provided they span C3. The selected-frame routine is now shared by both decoders. It validates all selected-arrow measurements, not only its three chosen anchors.

Selected-span failures remain outside the sharper theorem. The existing 144-block fallback is preserved on that stratum, including the zero-field case. This is deliberately conservative, not an optimal zero-field representation.

## All linear reference constraints

For reference r=(a,t), let x be its missing triple. For each b outside {a,t}, the two orientations of the state comparisons give, after subtracting known contributions,

```
w_b* K E x = forward residual,
w_b* E* K x = conjugate(reverse residual),
```

where w_b=c_(b,t) and E ranges over P, Q and C. The second equation uses conjugation of the reverse measurement; C is not assumed Hermitian or metric-unitary. P/Q repeat their self-adjoint constraints, but C and its metric adjoint can add information that the old gate ignored.

Exact elimination writes the solution set as

```
x = x0 + U z,
```

with U a kernel basis. Shift x0 within the affine solution space to its K-orthogonal minimum-norm point. The three remaining diagonal state measurements give the exact quadratic constraints

```
(x0 + U z)* K E (x0 + U z) = d_E,    E=P,Q,C.
```

The checker constructs their constant, linear, conjugate-linear and quadratic coefficients explicitly. Since all other state contributions are already known, these constraints exhaust the missing-triple dependence of the retained measurements. Every selected completion is also checked by regenerating all 411 values.

## Classified strata

### Full linear rank

The missing triple is unique if it satisfies all diagonal quadrics. Thus some old P/Q failures need no additional records once the cycle measurements are used.

### Minimum-norm tangency, any nullity

P+Q supplies the positive K norm. Let

```
R = d_P + d_Q - ||x0||_K^2.
```

If R<0, the packet is inconsistent. If R=0, positivity forces z=0: x=x0 is unique, subject to the other quadrics. This includes a zero missing triple with no surviving linear reference probes.

### Complex nullity one: complete classification

Write x=x0+u z. The norm fixes |z|^2=R/||u||_K^2. Substituting that value into each other quadratic leaves real linear constraints on Re z and Im z.

The resulting circle and real affine subspace give:

- two independent real constraints: one point if consistent;
- one real constraint: no point, one tangent point or exactly two points;
- no real constraints: an entire circle.

The two-point certificate stores `base +/- sqrt(radicand) direction`. It verifies the quadratic-extension identities exactly without choosing a root or assuming that root belongs to the source coefficient field. An inconsistent intersection is rejected.

Algebra-only tests exercise two points, a tangent point and an entire circle. Their synthetic operators test this solver and are explicitly **not replacements for the actual named source cycle**.

### Higher nullity

If x0=0 and a nonzero measurement-consistent witness is available, its full phase orbit is a certified continuum of solutions. The selected nonzero spanning arrows fix the common phase, so changing only this missing triple is a genuine relative ambiguity.

The witness is supplied by the already validated operator data or the retained completion column, not inferred from the desired answer. The exact quadratic system remains available, but no complete parameterization or dimension of this higher-nullity fiber is asserted.

Other higher-nullity intersections are labelled **unresolved**, never silently unique. General finite algebraic intersections in that stratum remain open.

## Revisiting the twelve-reference census

For the field used in the prior reference-transition experiment:

- eleven reference choices now have a unique missing triple and need no extra reference record;
- reference (0,1) retains a genuine continuous ambiguity.

The two other old failures, (2,1) and (3,1), are no longer treated as intrinsically ambiguous. The report records the actual all-channel rank and uniqueness reason rather than assuming which additional equation resolves them.

A separate source-derived control zeros all three arrows into vertex 1. With reference (0,1), there are no linear probes at all (rank zero), yet its diagonal norm forces the missing triple to zero. Full measurement regeneration verifies uniqueness. This directly distinguishes a decoder limitation from lost information.

## A smaller sufficient record for a nonunique missing triple

Once the selected arrows span and are recovered projectively, retaining the full 144-block core is unnecessary merely to recover the one missing triple.

Choose a canonical nonzero selected coordinate `(e,j)`. Retain the column

```
b_i = c_reference[i] conjugate(c_e[j]),    i=0,1,2.
```

This is **three complex values**, plus its anchor labels, from an existing reference-touching outer-product block. It is common-phase invariant and is not an amplitude/phase anchor.

If the selected decoder returns y=lambda c with rho=|lambda|^2, recover

```
y_reference[i] = rho b_i / conjugate(y_e[j]).
```

Then regenerate all comparisons. The column resolves the missing triple regardless of the unclassified higher-nullity quadrics. It is a sufficient record, not a proved minimum; some fibers could require less.

The two blind-reference fields have identical scalar carriers but different completion columns. Removing or corrupting that column is rejected. On unique fibers the compact packet forbids an unnecessary completion column; outside the selected-span domain it keeps the full verified fallback.

## Integration without changing the old contract

`SharpPacket` contains a transport carrier, a new fiber certificate, the previous probe/conditioning certificate, and either no extra record, one completion column or the full fallback. It uses an explicitly named **exact-uniqueness-plus-completion** retention policy.

Its carrier is not falsely typed as a complete old packet. Expansion reconstructs the complete operator core from the actual compact data, recomputes the old certificate, materializes any sidecar the old policy requires, and invokes the unchanged old verifier. All tested old packets round-trip through compact and expanded form exactly.

The old weak-probe warning is retained even when exact uniqueness permits compact storage without the old sidecar. This changes storage policy, not the conditioning of the inverse. No improvement in noise stability is claimed.

Reference changes use this expansion adapter, the existing verified transition and recompaction. Identity, round-trip and cocycle tests pass; both retained-promotion policies commute with the adapted transitions. The genuinely ambiguous intermediate reference now retains three complex values rather than 144 matrix blocks. The original full core is only materialized when the old interface needs it, not hidden inside the compact packet.

## Scope and remaining work

This is a sharper reconstruction-domain certificate and a smaller sufficient retention scheme, not universal quadratic-fiber classification, a minimum-storage theorem or a stable numerical solver. Higher-nullity nonhomogeneous fibers remain unresolved. Selected-span failure remains on the earlier fallback. Physical instrument availability, reference d and the fixed 2x2 DG binding are unchanged.

## Reproduction

```
python research/strominger/checkers/check_reference_quadratic_fibers.py
```

Receipt: `research/strominger/results/reference-quadratic-fibers/verification.json`. The checker freshly replays prior reconstruction, retained transport and reference-transition tests, including the shared selected-frame refactor. No production or viewer code is changed.
