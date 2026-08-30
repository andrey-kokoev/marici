# Bidirectional constructor pullback pilot

## Question

Can one small constructor contract express the backward proof obligations in
the RH, flavor, and optical frontiers without reconstructing a source from a
lossy record?

## Contract

A bidirectional constructor carries a forward map and a contravariant
requirement transformer:

\[
F:X\to Y,
\qquad
F^*:\operatorname{Req}(Y)\to\operatorname{Req}(X).
\]

For composable constructors, requirements move in reverse order:

\[
(G\circ F)^*=F^*\circ G^*.
\]

This is not an inverse to `F`. When `F` identifies two source states, the
contract returns the collision as a typed residual. It does not choose one
preimage.

The finite compiler record is:

```text
BidirectionalConstructor
  constructor_id
  source_type
  target_type
  forward_map
  requirement_rules
  authority_root
  completion_scope
```

A target requirement is a finite set of atomic obligations. Each constructor
replaces every known target atom by its declared source obligations. Unknown
atoms are rejected rather than silently transported. A source capability set
discharges the resulting obligations; the set difference is the residual.

## Exact composition gate

The checker uses two constructors

```text
source --prepare--> carrier --observe--> record
```

and verifies that direct pullback through their composite equals pullback
through `observe` followed by pullback through `prepare`. Reversing that order
is ill-typed and deliberately rejected.

## RH pilot

The desired record claim is Fourier-stable faithful observation. Pullback
through determinant and moment-germ compression requires the full
function-valued trace and completion continuity.

The hostile source has three symbolic states: zero, a visible theta state,
and a nonzero flat-bump state whose complete moment germ vanishes. Moment
observation identifies zero with the flat bump. Full-trace observation does
not.

The backward contract therefore stops at the exact missing obligation
`full_function_trace`. It does not infer a source from the determinant line.

## Flavor pilot

The desired record claim is a proper `physical16` selector. Pullback through
the rank-nine response window requires:

- a non-aligned tensor;
- independently derived linear coefficients;
- rank-nine persistence over all fitted sheets.

The present source supplies only the response-capacity calculation. The
compiler returns the first two missing obligations. Rank nine is therefore
typed as capacity, not selection.

## Optical pilot

The desired record claim is a unique physical inverse of the calibrated
quadratic monitor. Pullback requires both three-level calibration and a
source-authorized monotone domain.

For

\[
y={1\over100}+{5\over4}x-{1\over2}x^2,
\]

the exact inputs

\[
x={1\over4},
\qquad
x={9\over4}
\]

produce the same record. Three-level calibration identifies the polynomial
but cannot choose between these roots. The compiler returns
`monotone_source_domain` and preserves the collision pair as the falsifier.

## Claim boundary

The pilot proves a finite contract and three exact instances. It does not yet
provide a general predicate language, quantifiers, higher-order constructor
rules, continuous-state verification, or an integration into Strominger's
compiler.

## Disposition

The common contract survives all three pilots. Its central invariant is:

> Effects compose forward; requirements compose backward; noninjective
> projections return collisions rather than fabricated inverses.

The next integration gate is to add `requirement_rules` and a backward
discharge pass to the DPC constructor tree while preserving the existing
domain, residual, support, authority, completion, and fault-model checks.

## Verification

Run:

```text
python research/nima/checkers/check_bidirectional_constructor_pullback.py
```

The checker writes
`research/nima/results/bidirectional-constructor-pullback.json`.
