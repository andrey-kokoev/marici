# Signed and rational component arithmetic executes the scalar fixture

## Question

Can the component-word semiring be completed to signed and rational coefficients
and used by native Resolve without supplying its coefficient operations?

This implements the operator's instruction to extend the natural-number bridge
in `native-component-arithmetic.md`. SCC obligations are algebraic quotient
descent and native readout compatibility; neither is physical selection descent.

## Claim boundary

The checked chain is

\[
\text{component words}\longrightarrow\text{signed-pair quotient}
\longrightarrow\text{positive-denominator fraction quotient}.
\]

### Signed completion

`agda/SignedComponentArithmetic.agda` forms pairs `(a,b)` of component words,
with `(a,b)` equivalent to `(c,d)` when `a+d=c+b`. Operations on representatives
are constructed from the preceding component operations:

\[
(a,b)+(c,d)=(a+c,b+d),\qquad
(a,b)(c,d)=(ac+bd,ad+bc),\qquad -(a,b)=(b,a).
\]

The code proves quotient descent and identifies this quotient with the library's
checked difference-integer quotient and its signed normal forms. The readout into
integers has a constructed inverse, not just agreement on examples. Additive
inverses and the component-word embedding's addition/multiplication laws are
proved. The generic `Readout` into a commutative ring interprets a pair as the
difference of its two numeral images and proves representative compatibility.

### Fraction completion

`agda/RationalComponentArithmetic.agda` uses a signed numerator and a denominator
of constructor shape `1+n`. Denominator multiplication is implemented using
component multiplication, with a proved comparison to ordinary positive-integer
multiplication. Cross multiplication defines the quotient relation. Addition,
multiplication and negation are defined on representatives and proved to descend.
The signed embedding preserves addition and multiplication. Every positive
component denominator has an explicit inverse fraction, with a checked product
law.

The rational readout and its inverse satisfy both roundtrips. In particular,
equal rational readouts really imply equality in this **coefficient quotient**;
this says nothing about equality of source packages or physical states.

`agda/FaithfulComponentRing.agda` transfers ring laws through these faithful
readouts only after the operations and their preservation proofs exist. It does
not define source operations by pulling back target multiplication. Both completed
coefficient types are actual Cubical commutative rings, with semirings available
for the existing diagram-expansion theorem. The comparison uses library integer
and rational algebra as proof infrastructure; it does not claim an independent
implementation of every library theorem or a new formal localization universal
property for arbitrary targets.

### Native execution and the actual source fixture

`agda/NativeCoefficientTransport.agda` proves the coefficient-homomorphism square
for every finite marked sum/product expression, for direct native executions and
translated original executions. It retains factor labels and reads the actual
operator and child values; it does not identify complete packages with scalar
values.

`agda/NativeRationalComponentArithmetic.agda` instantiates this construction with
both completed coefficient rings. Its scalar fixture imports the actual ten
channel weights from `NativeScalarFiberFixture`, embeds them with denominator one,
and multiplies their sum by the separately marked normalization factor `1/600`.
The denominator is checked against the source's common denominator; the final
numerator and denominator are checked against `ScalarSixFixture`'s exported pair.
The native operation tree evaluates with the constructed quotient operations.
Direct execution, translated execution and diagram expansion all read out

\[
144/600=6/25.
\]

This is an additional checked implementation, not a modification of the existing
integer fixture or Python DAG compiler.

## Tests and disposition

Conjecture: the signed/fraction extensions of component arithmetic can replace
supplied coefficient operations while preserving native amplitude readouts.
Rivals: sign cancellation is not a congruence; denominator zero is silently
admitted; ordinary rational operations are substituted without a compatibility
proof; scalar coincidence hides a broken execution/readout square.
Risky consequences: representative operations must descend, readout roundtrips
must hold, all finite-expression squares must typecheck, and the existing physical
fixture must survive the replacement.

A fresh safe/cubical dependency-closure check passes. Four intended rejections
also pass, with exact error markers:

| Hostile | Required compiler residual |
| --- | --- |
| Zero denominator literal, alongside an accepted positive literal | `InstanceNoCandidate`, `Constraint 0` |
| `2/4 = 1/3` | `6 != 4` |
| `3 + (-3) = 1` | `0 != 1` |
| Native scalar value `7/25` | `3600 != 4200` |

SCC's receipt checker verifies fresh compilation, the current local import
closure, checker and rejection-source hashes, and the four exact rejection logs.
The existing `FiniteFiberAmplitude.agda:19` constructor-shadowing warning remains
nonfatal and unchanged. No postulates or holes were introduced.

Disposition: the signed/rational arithmetic bridge and the six-point native
fixture are checked. The geometric free-component hypothesis remains conditional.
The physical weights remain the supplied source table's weights; neither the
scalar theory nor coupling/propagator selection is derived by this construction.

The first missing physical arrow is a source-authorized coefficient/selection
map from the occurrence-resolved Carrier that respects the proposed component
quotient. Acceptance requires that actual map and its commuting selection square;
an arithmetic equivalence cannot replace them. This branch is deferred rather
than silently passing the physical descent gate. The existing
`readout-arithmetic-naturality-obstruction.md` already distinguishes available
arithmetic from selection-compatible physical operations. Arbitrary-n Python
compiler correctness and loop measures are outside this packet.

## Reproduction and evidence

Through structured-command:

```text
pwsh -NoProfile -File research/nima/checkers/check_completed_component_arithmetic.ps1 -Fresh
python research/nima/checkers/check_completed_component_arithmetic_receipt.py
python research/aspect/scc/scc.py check nima-completed-component-arithmetic
```

Receipts:

- `results/agda-NativeRationalComponentArithmetic.json`;
- `results/completed-component-arithmetic-formal-audit.json`;
- `results/completed-component-arithmetic-receipt.json`;
- `results/agda-ComponentZeroDenominator.log`;
- `results/agda-ComponentBadFractionCancellation.log`;
- `results/agda-ComponentBadSignedCancellation.log`;
- `results/agda-ComponentBadScalarReadout.log`.

All new sources, checkers, manifest, packet and generated evidence remain
uncommitted. No source owned by another researcher was edited; no active
computation, independent review, commit, push or physical prediction is claimed.

Graph reports for this arithmetic thread are admitted but uncommitted: sequence
15601 (`ev-000000015601-4917b734-06d9-43a2-9689-7c778eb6e66d`, natural stage)
and sequence 15604 (`ev-000000015604-0929bc55-f591-482d-a0c0-026cb47ad26b`, this
completion). Admission records communication, not independent mathematical review.
