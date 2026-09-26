# Raw unary-history recognition, and a genuine native-branch boundary

## New positive result

`GuardedUnaryHistoryRecognition.agda` accepts existing raw `ResolveT`
histories with one designated source. They need not have been emitted by the
route compiler. A `Guarded` annotation records the actual equivalences, a
faithful normal chart at each endpoint, and each step's pointwise
coordinate-preservation proof.

The recognizer decodes those actual steps into a typed route. Checked
induction proves that decoding preserves their composed function, and that
the raw composed function at the original source value equals the actual
stored endpoint value. Finishing through the declared endpoint chart gives a
route to the shared normal presentation.

The previous finite guarded-route basis then supplies derivations for every
requested comparison of the raw guarded observers. Its soundness is
transported back to the original observers, with witness reconstruction.
The retained record stores both original raw histories—not regenerated
substitutes—their endpoints, charts, guards, source packet, requested witness,
derivation, reconstruction and the comparison of actual charted endpoint
values.

This is effect recognition. It does not claim that decoding and recompiling
reproduce identical native syntax or identical numbers of retained wrappers.

## Fresh positive and negative tests

`GuardedUnaryHistoryRecognitionRegression.agda` builds one-step and two-step
raw histories directly with `transportT`, recognizes them, reconstructs a
requested witness, and checks exact retention of both original histories.
Bool negation remains incompatible with the fixed identity target chart.

It also makes two different coverage failures explicit:

1. An existing native identity-rule history has a faithful endpoint chart,
   but is not a constructor of this unary recognizer. This is a syntactic
   coverage gap, not a claim that its semantics is incompatible.
2. A native E-rule over Bool with Unit inputs is reachable from a designated
   Unit source. Its output value type is Bool × Unit, while that source's
   normal type is contractible. A checked two-point discriminator proves
   that **no faithful chart** from this output to that fixed source normal
   type exists.

The second failure cannot be repaired merely by adding a native constructor
to `Guarded`. It refutes a universal fixed-source-chart coverage claim. It
does not refute dependent normalization: the E output has its own normal
form, which retains the newly introduced Boolean index.

## Consequence for the broader completeness branch

Guarded unary recognition is now checked beyond the compiler image. However,
coverage of all native resolution constructors cannot use one fixed source
normal type while ignoring newly introduced index choices.

The constructive successor is to build faithful boundary coordinates for
native E/Pi applications that retain the introduced indices and the complete
input family. Their output normal form may vary with that boundary. Only
then should the finite comparison basis be lifted to those branches. The
arbitrary-source identity obligations remain separate.

## Verification

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module GuardedUnaryHistoryRecognitionRegression -Fresh
```

* `research/nima/agda/GuardedUnaryHistoryRecognition.agda`
* `research/nima/agda/GuardedUnaryHistoryRecognitionRegression.agda`
* `research/nima/results/agda-GuardedUnaryHistoryRecognitionRegression.json`
* `research/nima/results/agda-GuardedUnaryHistoryRecognitionRegression.log`
