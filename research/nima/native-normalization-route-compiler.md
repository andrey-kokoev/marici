# Native comparison-node compilation of retained routes

## Checked construction

`NativeNormalizationRouteCompiler.agda` compiles every step of a retained
coordinate-preserving route into the existing native `compare-rule`. A native
`Pi-rule` collects the resulting comparison packages in their route order.
There is no new resolution constructor and no opaque multi-step route seed
inside the emitted tree.

For a map f between presentations with faithful normal coordinates, the
compiler proves that the underlying function of f is an equivalence. It does
not replace that function by the canonical map: only its isEquiv proof is
transported from the canonical equivalence along the checked map comparison.
The target value is exactly f applied to the current source value, so the
native edge's boundary witness is reflexivity.

The route-indexed Slots type has one position per step. Recursion supplies
each successive step with the preceding map's output. Each comparison package
retains both endpoint codes and values, the actual equivalence and boundary
witness. The complete original route and its coordinate witnesses are retained
separately in the compiled record.

## No hidden route seeds

`CanonicalLeaves` is an inductive certificate for the emitted native tree.
Every seed is the single canonical normalization seed of its boundary package;
all other nodes are native rule applications. `compile-leaves` proves this
for every compiled route. A regression proves that the earlier opaque
four-step seed cannot satisfy this certificate.

The original outer-first route yields three native comparison steps; the
inner-first route yields four. Both work with the previously checked infinite
and dependent indices. The zero-step route is supported as an empty native
Pi batch.

## Comparison without erasing provenance

The two batches need not have the same complete endpoint: their index types
and retained intermediate packages differ. The compiler does not coerce them
into the same endpoint merely to apply a same-endpoint comparison theorem.

Instead `Compared` retains both route records, both native histories, their
canonical-leaf certificates and a checked equality of sequential output
values. The sequential effect agrees with the original typed route evaluation.
The full comparison record becomes a next-level Complete input. A regression
checks that its source still contains the original nontrivial circle loop.

This is a native comparison-node compiler, not an emitter specializing each
step to `distribution-rule`, and not a claim that the normalization-algebra
carrier of a comparison batch equals the carrier of the original source.

## Remaining source restriction

The compiler uses the already frozen Seed family, which admits a canonical
normalization route at every boundary package. It does **not** prove that
intermediate boundary packages are reachable from only the initial source
seed. The native compare-rule requires both boundary histories.

The next discriminator is to restrict seeds and test native atomic-endpoint
reachability. If the existing signature cannot produce the required bare
intermediate endpoint, a provenance-preserving view/transport constructor is
needed; silently unwrapping remembered packages is not acceptable.

## Verification

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeNormalizationRouteCompilerRegression -Fresh
```

* `research/nima/agda/NativeNormalizationRouteCompiler.agda`
* `research/nima/agda/NativeNormalizationRouteCompilerRegression.agda`
* `research/nima/results/agda-NativeNormalizationRouteCompilerRegression.json`
* `research/nima/results/agda-NativeNormalizationRouteCompilerRegression.log`
