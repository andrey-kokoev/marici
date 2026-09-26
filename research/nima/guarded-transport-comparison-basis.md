# Witness-complete comparisons of guarded, source-only compiled routes

## Result and semantic boundary

`GuardedTransportComparisonBasis.agda` supplies a finite comparison calculus
for coordinate-preserving routes compiled by `SingleSourceRouteCompiler`.
Their native retained endpoints need not be equal.

For every source value, `observe` reads the value of the **actual compiled
packet**, through its retained view. It pairs that value with the proof that
its target coordinates equal the original source coordinates. Thus the
semantic witness compares guarded compiled maps, including their coordinate
witnesses, rather than comparing unrelated bare endpoint values.

Every primitive route step must already have its typed coordinate-preservation
guard. The concrete dependent reordering steps were previously checked against
that interface. This theorem does not infer a guard for an arbitrary
unrestricted equivalence or an arbitrary raw ResolveT history.

## Two local schemas

The primitive comparison laws are:

1. Normalize a stopped route to the canonical one-step route.
2. Normalize one guarded step followed by a canonical continuation.

Closure adds identity, reversal, concatenation and prefix congruence. Neither
primitive law accepts an arbitrary semantic comparison witness. Unlike the
older whole-seed normalization schema, these laws operate on the actual route
spine, one step at a time.

Induction reduces every route to the canonical route between its two
coordinate-equipped presentations. This yields a Generated comparison for
any pair. The guarded-map space is contractible; hence its path spaces are
contractible. The theorem therefore constructs

    (p : observe(a) = observe(b))
      -> Σ(c : Generated a b). sound(c) = p.

Higher witness comparisons are supplied by path-space contractibility. This
is a new typed calculus for compiled routes, not an assertion that the old
same-endpoint `Structural.Generated` datatype magically gained heterogeneous
endpoints.

## Full retention

The requested-comparison record retains both route records, the source value,
the requested guarded witness, its generated derivation and reconstruction,
both actual source-only extended histories, both single-seed certificates and
the induced equality of viewed effects. The whole record becomes a subsequent
Complete input.

Native endpoint packets are not identified or stripped of provenance. In the
regression, a stopped route and a one-step identity route have provably
different packet expressions—bare atom versus retained packet—while their
guarded effects have a generated comparison.

## Checked regressions

`GuardedTransportComparisonBasisRegression.agda` proves retention symbolically
for arbitrary universe, source code, presentations, routes, source value and
requested witness. This avoids eagerly expanding the large concrete dependent
normalization certificates; an earlier fully expanded specimen exceeded the
checking timeout and is not the retained regression.

Closed Bool checks establish witness reconstruction across differently
retained endpoints and prove that a negating map cannot acquire the shared
identity-coordinate guard. The prior identity-versus-negation transport
counterexample is therefore not collapsed by the new calculus.

## Remaining coverage

The theorem covers the image of the guarded route compiler. It is not yet an
adequacy theorem recognizing every intended raw extended history as such a
route, nor completeness for arbitrary native branching histories or atomic
source identities. The programme's broader completeness/coverage and source
boundary branches remain open.

## Verification

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module GuardedTransportComparisonBasisRegression -Fresh
```

* `research/nima/agda/GuardedTransportComparisonBasis.agda`
* `research/nima/agda/GuardedTransportComparisonBasisRegression.agda`
* `research/nima/results/agda-GuardedTransportComparisonBasisRegression.json`
* `research/nima/results/agda-GuardedTransportComparisonBasisRegression.log`
