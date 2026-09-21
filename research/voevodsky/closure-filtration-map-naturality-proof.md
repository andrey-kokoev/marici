# Cut/rejoin naturality for homotopy-commuting filtration ladders

## Result

The canonical cofiber cut/rejoin comparison now respects arbitrary maps between three-object filtration segments:

```
A  --f-->  B  --g-->  C
| u        | v        | w
v          v          v
A' --f'--> B' --g'--> C'
```

The inputs are arbitrary vertical functions and specified square homotopies

- Hf(a): v(f(a)) = f'(u(a));
- Hg(b): w(g(b)) = g'(v(b)).

The vertical maps need not be equivalences. The squares need not commute judgmentally. No cut/rejoin compatibility is an input.

`Ladder.mapQuotient` constructs a function from (C/A)/(B/A) to (C'/A')/(B'/A'). `Ladder.mapCofiber` constructs a function from C/B to C'/B'. The module proves the rejoin square and the inverse-cut square for these particular constructed functions.

Code: `agda/ClosureFiltrationMapNaturality.agda`.
Regression: `agda/ClosureFiltrationMapRegression.agda`.

## Construction

There are three concrete object-changing operations:

1. Target postcomposition reuses the checked canonical naturality square.
2. Middle change is defined on the nested attachment constructors: a B-indexed attachment is sent to its v(B)-indexed attachment.
3. Source change sends A-indexed attachments to their u(A)-indexed attachments and preserves target points.

Each operation supplies both a rejoin square and a cut square, with proofs on all higher-inductive constructors.

For squares which commute only up to homotopy, `ArrowPaths.comparison` follows a path of the source arrows. The canonical rejoin and cut maps form dependent families along that path. Cubical `transport-filler` and `fromPathP` turn those families into the required transport-compatible squares. This retains the specified homotopies rather than replacing them with reflexivity.

The complete ladder is factored as:

1. target change by w;
2. adjustment from wg to g'v using Hg;
3. middle change by v;
4. adjustment from vf to f'u using Hf;
5. source change by u.

A small `Comparison` record packages the proved maps and squares for composition. Its fields are constructed at every step, and the final theorem takes no inhabitant of that record as a hypothesis. `compose` pastes the existing witnesses with explicit whiskering and path concatenation. It does not assume the desired result.

The exported maps use this factorization and its transport choices. Agreement with another standard cofiber-map implementation is not silently assumed. In particular, even transport along a constant type path is not treated as judgmental identity.

## Regressions

The first fixture changes every object from Bool to Unit and uses the constant vertical map at every stage. A proof that this vertical map is not an equivalence accompanies the checked rejoin square. Thus the construction genuinely accepts noninvertible maps, not merely relabelings of a filtration.

The second fixture uses circle-valued middle and final objects. Both Hf and Hg are instantiated with the circle loop. It checks the rejoin comparison on the nested attachment square and the cut-comparison family along a whole loop in the cofiber. The output has an explicitly checked circle retract, rather than being replaced by a terminal fixture.

## Verification

Fresh dependency-closure command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureFiltrationMapRegression.agda`

Result: exit 0. Both new modules use `--safe --cubical --guardedness`, with no holes or postulates. Existing modules were not modified.

Initial incremental checks identified missing stage type annotations around reflexivity paths and an ambiguous `cong inr loop` in the regression. Explicit stage signatures and the direct formula `inr (loop i)` resolved those elaboration issues before the passing fresh check.

## Scope after this increment

Established: naturality of canonical rejoin and cut for arbitrary homotopy-commuting three-object ladders, in addition to the earlier canonical five-route cofiber pentagon.

Still separate:

- compatibility of the factorized ladder maps with composition of arbitrary ladders, including their chosen square homotopies;
- naturality of the complete five-object pentagon under such maps;
- coherence for arbitrary finite towers;
- comparison with the earlier opaque 3-by-3 implementation and analytical realization.

The checked three-object theorem is not being labelled as any of those higher results.
