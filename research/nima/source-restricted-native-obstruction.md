# Source-only native compilation: a checked signature obstruction

## Result

The canonical intermediate-boundary seeds cannot simply be removed from the
current native compiler. This is a theorem about the existing rule signature,
not an unsuccessful search for a derivation.

`NativeAtomicReachability.agda` checks every current Rule constructor and proves
that its output expression is never a bare `atom A`. Consequently, for any
seed family S,

    Resolve S (pack (atom A) x) -> S (pack (atom A) x).

Every reachable bare atomic endpoint therefore already has seed evidence. This
holds for arbitrary dependent indices and higher types.

With `OnlySource source q = (q = source)` and a non-atomic source expression,
no bare atomic endpoint is reachable. A Boolean constructor discriminator
proves this even when equality paths, rather than syntactic identity, are
allowed in the seed family. It does not rely on discreteness of the types
stored inside atom.

## Applied to the actual compiler

`SourceRestrictedNativeRegression.agda` is parameterized by arbitrary
I, J(i), K(i,j), L(i,j,k), B(i,j,k,l). The original dependent route source is a
Pi expression; its first outer-first intermediate, first inner-first
intermediate and terminal presentation are currently coded as atoms.

The original source is reachable from its one source seed. All three named
bare intermediate/terminal endpoints are unreachable from that seed family.
The proof then applies to the exact `edge-rule` instances emitted by
`NativeNormalizationRouteCompiler`: their target-boundary premises cannot be
discharged. Supplying the corresponding intermediate seed makes that atomic
endpoint reachable, pinpointing the hypothesis used by the previous compiler.

This does not refute the earlier compiler under its stated all-boundary Seed
family, or the two-schema comparison completeness theorem under its frozen
semantics. Nor does it prove that every alternative structured encoding of an
intermediate endpoint is unreachable. It refutes removal of boundary seeds
from these exact native nodes under the existing signature.

## Constructive successor: retain provenance while transporting a value

The next branch should test a separate unary extension, leaving the old
signature and its obstruction theorem intact. Given a reachable complete
package a, a target code R and an actual equivalence

    e : El(expression a) ≃ El R,

compute, rather than assume a seed for,

    target = pack R (e(value a)).

The proposed output is

    remember (comparison-package a target e refl) target.

This retains the full source package, target, equivalence and boundary
witness. Its interpreted value type is El R, so a following step can use that
view while passing the entire retained packet onward. It does not manufacture
a bare atomic endpoint or silently erase a remembered prefix.

Proof obligations for the successor are single-source sequential compilation,
recovery of the retained step/source evidence, and preservation of the
original typed route's effect. This constructor and those proofs are proposed
here, not yet implemented or certified.

## Verification

Fresh safe Cubical Agda verification passed:

```
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SourceRestrictedNativeRegression -Fresh
```

* `research/nima/agda/NativeAtomicReachability.agda`
* `research/nima/agda/SourceRestrictedNativeRegression.agda`
* `research/nima/results/agda-SourceRestrictedNativeRegression.json`
* `research/nima/results/agda-SourceRestrictedNativeRegression.log`
