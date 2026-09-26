# Faithful coordinates for complete native application boundaries

## Checked construction

`NativeBranchBoundaryCoordinates.agda` replaces the insufficient fixed
original-source chart with coordinates for the **whole native application
boundary**. For E this contains:

* the index type I;
* the entire family F : I -> Complete, not just its chosen member;
* every actual child resolution history;
* the selected index.

The Pi boundary contains the same data without a selected index. Dependent,
infinite and empty index types are permitted without enumeration. A general
Rule boundary additionally covers every native rule head and its complete
child-history family. The structured E/Pi evaluators agree with this general
native evaluator.

Evaluation constructs the actual original native `apply` history, not a
stand-in semantic value. Its result is a Closure containing both the output
Complete packet and the raw parent derivation.

For a boundary type B and its actual evaluator eval, the application type is

    Application = Σ b : B. Σ out : Closure S. eval(b) = out.

The checked graph equivalence identifies this application type with B.
Composing its inverse with faithful dependent normalization of B supplies
application coordinates. This retains the whole boundary, output and
compatibility witness; inverse homotopies reconstruct the whole application.
The equivalence also lifts to paths and higher paths. Neither raw histories
nor arbitrary source types are made contractible.

## Actual computation and finite-basis coherence

The construction compares two routes with the SAME evaluator and application
target:

1. evaluate the complete boundary directly;
2. normalize the boundary, reconstruct it, then evaluate.

Both compile as guarded source-only transport routes at the raised universe.
Checked effect theorems project their actual compiled packets back to the
exact native output closure. The previous two-local-schema guarded basis
reconstructs every requested witness between these two compiled observers.

The strengthened `guarded-application` theorem proves that ANY guarded map
into this fixed application presentation reconstructs the entire canonical
application, including its evaluation witness. Consequently,
`every-compiled-native-output` proves preservation of the specified native
output closure for every compiled guarded route with that target—not just
the two displayed routes. This remains relative to the fixed evaluator.

The complete boundary, application, route certificate, compiled history and
requested generated-comparison record are retained as subsequent input.
The application boundary lives one universe above the original packets;
the reified route-and-comparison record lives another universe above it.
No resizing or proof truncation is used.

Here 'one source' means the whole supplied application boundary, including
its already-valid child histories. It does NOT manufacture those histories
from one original low-level seed or bypass native atomic reachability.

## Adversarial and general regressions

`NativeBranchBoundaryCoordinatesRegression.agda` checks:

* changing a Boolean index choice changes its normalized fixed-index boundary;
* changing an UNSELECTED child's raw seed label changes that boundary's
  normal coordinates, even though the native output Complete packets agree;
* exact retention of arbitrary boundaries, actual native output closures
  and requested witnesses;
* reconstruction of whole applications and arbitrary higher witnesses;
* genuine empty and Nat-indexed native Pi histories;
* a dependent Bool-indexed family with Unit and Bool fibres;
* impossibility of an E boundary with an empty selected-index type;
* impossibility of substituting a differently tagged seed history for the
  actual native parent output, including through an arbitrary guarded map;
* failure of boundary projection to be an equivalence if the application
  merely stores an arbitrary output WITHOUT its evaluation equation.

The last test exhibits two different raw output closures over the same
boundary. The evaluation witness is therefore essential to the claimed
projection equivalence; retaining an uncertified pair alone is insufficient.

This resolves the earlier Bool x Unit obstruction by keeping the introduced
index in the input boundary, not by pretending the result has the old Unit
source's normal type.

## Precise remaining frontier

This proves faithful application-boundary coordinates and coherence of
normalization around a fixed native evaluator. It does not identify distinct
child histories or establish completeness for arbitrary pairs of native
resolution schedules. Charts belonging to different evaluation graphs do
not, by themselves, prove equality of those evaluators' outputs.

The next obligation is relational: lift existing Structural.Generated child
comparisons through native application boundaries, retaining both distinct
boundary records and their actual semantic witness. Full boundary identity
cannot replace that relation—the unselected-history discriminator proves
why. The arbitrary-source identity theory remains a separate open branch.

## Verification

Fresh safe Cubical Agda closure passed (Agda 2.8.0, Cubical 0.9):

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeBranchBoundaryCoordinatesRegression -Fresh
```

* `research/nima/agda/NativeBranchBoundaryCoordinates.agda`
* `research/nima/agda/NativeBranchBoundaryCoordinatesRegression.agda`
* `research/nima/results/agda-NativeBranchBoundaryCoordinatesRegression.json`
* `research/nima/results/agda-NativeBranchBoundaryCoordinatesRegression.log`
