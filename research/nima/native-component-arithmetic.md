# Component arithmetic now instantiates native Resolve

## Question

Can the earlier conditional endomorphism-semiring construction supply the
arithmetic operations in the native amplitude-expression implementation?

The operator directed reuse of prior arithmetic rather than a new NAND-adder
construction. Sources are `phase-i-endomorphism-semiring.md` and
`../grothendieck/phase-i-three-level-reconciliation-audit.md`.

SCC obligations: forward realization and readout compatibility. The stratum is
finite expressions over component normal forms, not physical selection descent.

## Claim boundary

`agda/ComponentArithmetic.agda` represents a word of connected components by an
inductive empty/copy type (Agda naturals, with no imported arithmetic). It defines
addition by concatenation and the additive endomorphism classified by a word a:

- `endo a empty = empty`;
- `endo a (copy b) = append a (endo a b)`.

It proves additivity and uniqueness from the image of the generator. Multiplication
is `endo a b`. Endomorphism composition proves associativity; pointwise addition
proves the other distributive law; uniqueness proves commutativity. These laws
construct an actual Cubical `Semiring`, rather than assume its multiplication.
For any target semiring, `Readout` constructs the unique zero/unit/addition-preserving
numeral map and proves that it also preserves this multiplication. This establishes
initiality; it is not merely a finite arithmetic test.

`agda/NativeComponentArithmetic.agda` supplies that semiring to the existing
`AmplitudeDiagramExpansion` and `NativeAmplitudeResolution` implementations.
For every finite expression it obtains an actual native `Resolve` derivation,
its diagram expansion, and commuting readout squares into a supplied target
semiring for both direct and translated executions. Factor labels, operator tokens,
and full native execution packages remain in the source; the scalar map does not
identify packages with equal readouts. The target semiring is needed to interpret
numbers, not to define component multiplication.

The `ComponentPort` explicitly takes an equivalence from a proposed component
object M to word normal forms. It transports the word operations and proves their
compatibility with normalization. It does **not** prove that a geometric M exists,
that a pre-existing geometric operation is the transported one, or that arbitrary
native packages have this normal form. The prior free-disjoint-union hypothesis
remains the geometric input. No categorical coproduct or faithful quotient of the
full occurrence-resolved Carrier is asserted.

## Test and disposition

Conjecture: the recorded component semiring can replace supplied natural-number
arithmetic in the native expression layer without changing its readout.
Rivals: multiplication is secretly imported from the target; component union is
idempotent; scalar equality is being substituted for package identity.
Risky consequences: multiplication must be constructed without a target algebra;
all expression readout squares must typecheck; repeated components must remain
distinct.

A fresh safe/cubical Agda closure check passes. The fixture constructs
`2 * (3 + 4)` as native applications and gives 14 through direct execution,
translated execution and diagram expansion. Two deliberate failures reject
`multiply 2 3 = append 2 3` and `append unit unit = unit` with `UnequalTerms`.
There are no postulates, holes, or arithmetic-law input assumptions in the component
semiring module. The local import closure and rejection-source hashes are audited
by a dependency-free receipt checker.

Disposition: the natural-number component bridge is implemented and checked.
Signed group completion and fraction localization are **not** implemented by this
packet. Consequently the six-point scalar fixture still uses its existing supplied
integer operations and physical weights; no rational-amplitude replacement is
claimed. The next algebraic extension is the signed-pair completion, followed by
localization with explicit nonzero denominators and the corresponding native
readout square. Physical weight/selection descent is independent of those algebraic
extensions.

## Reproduction

Through the structured-command surface, run:

```text
pwsh -NoProfile -File research/nima/checkers/check_native_component_arithmetic.ps1 -Fresh
python research/nima/checkers/check_native_component_arithmetic_receipt.py
python research/aspect/scc/scc.py check nima-native-component-arithmetic
```

The PowerShell checker normalizes PATHEXT only in its child process: the execution
surface's inherited environment initially caused PowerShell to classify the Agda
executable as a document. This runner repair changes no formal source assumptions.

Evidence: `results/agda-NativeComponentArithmetic.json`,
`results/native-component-arithmetic-formal-audit.json`,
`results/native-component-arithmetic-receipt.json`, and the two rejection logs.
No physical prediction, independent review, commit or publication is claimed.
