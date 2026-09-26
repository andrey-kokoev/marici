# Single-source compilation with retained unary transport

## Implemented extension

`RetainedTransportResolution.agda` adds a separate `ResolveT` datatype with
seed, embedded native-rule and unary transport constructors. The original
Rule and Resolve definitions remain unchanged, and old derivations embed
recursively into the extension.

Given a reachable complete source a, target code R and actual equivalence e,
the unary operation computes

    target = pack R (e(value a))
    output = remember (comparison-package a target e refl) target.

It requires no target seed. The comparison package retains the complete
source, target, equivalence and boundary witness. Checked recovery functions
return that evidence and the exact previous complete packet. The output
remains wrapped; its interpreted value type exposes El R for the next step.

## Source-only sequential compiler

`SingleSourceRouteCompiler.agda` compiles a coordinate-preserving route by
passing each whole retained output packet into the next unary transport. A
typed view supplies its current value type without discarding the packet.
The actual step equivalence is the current view composed with the checked
underlying equivalence of the supplied route map.

The source seed family is exactly `OnlySource source q = (q = source)`.
Compilation begins with `seedT refl`. The inductive `TransportOnly` certificate
proves that the output tree has one seed and unary transport only: no hidden
intermediate seed, native branching node or opaque multi-step route seed.

The final viewed value is proved equal to the original typed route evaluation.
The retained compiler record includes the original route, input value,
source-only extended history, single-seed certificate and effect proof. This
whole record is reified as a subsequent Complete input.

## Fresh checked regressions

`SingleSourceRouteCompilerRegression.agda` checks the arbitrary-dependent
example with an infinite first index and higher witness leaves:

* outer-first and inner-first compile with one source seed and respectively
  three and four unary transports;
* following the retained predecessor packets back three/four times recovers
  exactly the entire original source package;
* the final viewed effects agree;
* zero-step compilation contains only the original seed;
* the output remains wrapped, while the old bare-atomic reachability
  obstruction still holds in the unchanged old signature;
* the retained original route and nontrivial circle-index witness survive.

A further negative check matters for the next branch: transport by Bool
negation and by identity are both valid source-only extended histories, but
their output values are provably unequal. The extension admits actual
equivalences generally; it does not itself impose the shared-coordinate guard.

## Remaining comparison obligation

The earlier two-schema completeness theorem applies to its frozen original
normalization-map algebra. It has not automatically become a theorem about
all extended histories or differently retained endpoints.

The next branch must give explicit view-relative, coordinate-preserving
comparison laws for source-only transport chains, retain both histories and
reconstruct their witnesses. It must reject the identity-versus-negation
counterexample rather than identifying arbitrary transport effects.

## Verification

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SingleSourceRouteCompilerRegression -Fresh
```

* `research/nima/agda/RetainedTransportResolution.agda`
* `research/nima/agda/SingleSourceRouteCompiler.agda`
* `research/nima/agda/SingleSourceRouteCompilerRegression.agda`
* `research/nima/results/agda-SingleSourceRouteCompilerRegression.json`
* `research/nima/results/agda-SingleSourceRouteCompilerRegression.log`
