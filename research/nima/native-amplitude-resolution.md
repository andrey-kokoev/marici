# Amplitude expressions now execute in native Resolve

## Established result

The amplitude construction is now connected to the actual native `Resolve` datatype, rather than only to a separate numeric table evaluator.

For **every finite marked sum/product expression**:

1. an original `WholePackageResolution.Resolve` execution is constructed;
2. a native `NativeTableResolution.Full.Resolve` execution is independently constructed;
3. independent readouts agree with the expression's arithmetic;
4. the full old-to-native closure equivalence has a commuting amplitude readout at the marked endpoint;
5. the old retained execution is recovered by the inverse law.

With a supplied semiring, a further theorem identifies that arithmetic with the expanded sum of products over diagram choices, preserving multiplicity. The actual six-point scalar fixture instantiates the construction and reads out `144/600 = 6/25`.

These statements freshly compile in safe/cubical Agda. They do **not** establish arbitrary-n correctness of the Python partition enumerator or DAG compiler.

## Native execution and independently defined readout

`agda/NativeAmplitudeResolution.agda` takes a type of marked factors A, a coefficient type W, supplied weights and coefficient operations.

Expressions have zero, one, marked-factor and binary-operation constructors. Binary nodes carry a sum/product mode. A native binary package is constructed using the actual native Pi rule, with three declared ports:

| port | retained input |
| --- | --- |
| operator | actual sum/product token |
| left | left child's complete package |
| right | right child's complete package |

Only marked input factors, algebra constants and operation tokens have literal seed constructors. `native-run` recursively constructs actual Pi applications. It does not introduce the computed final amplitude as a new literal input. Factor identifiers are retained even when two factors have equal numerical weight.

The native `readout` reads the selected operator token and both selected child values, then applies the supplied algebra operation recursively. It does not call the old decoder, old readout or `evaluate` to obtain its answer. `native-correct` proves agreement with expression arithmetic by induction.

The original execution is independently constructed with the actual imported old Pi rule. `package-commutes` compares complete packages, including metadata. Applying the existing full closure equivalence gives a translated native execution. Its selected value is aligned along the proved endpoint equality; `translated-amplitude` proves that the native readout still gives the original expression value. This alignment is a typed compatibility witness, not an old evaluator hidden in the readout.

`direct-and-translated` compares the two readouts. It does not assert that independently built and transported derivation terms are definitionally identical.

## General finite diagram expansion

`agda/AmplitudeDiagramExpansion.agda` works over a supplied semiring:

- zero expands to no diagrams;
- one expands to the empty factor word;
- a factor expands to one singleton word;
- a sum concatenates diagram families;
- a product takes the Cartesian product and concatenates factor words.

Associativity, unit, annihilation and distributivity prove

\[
\sum_{d\in\operatorname{diagrams}(e)}\prod_{a\in d}w(a)
=\operatorname{evaluate}(e).
\]

`native-diagram-sum` and `translated-diagram-sum` connect this equality to the direct native and translated native executions. No diagram deduplication is performed: multiplicity and factor order survive. The theorem does not require multiplication to be commutative.

This closes the finite algebraic recurrence-to-expanded-sum step once a valid finite expression and its local weights are supplied. It does not prove that any arbitrary external program has enumerated precisely the physical diagrams.

## Actual scalar fixture

`agda/ScalarAmplitudeResolveFixture.agda` imports the existing native six-point channel table and treats its ten individually marked channel weights as source factors. Their sum is built as an actual nested native Resolve execution, with operation-token and factor premises.

Checked results include:

- direct native readout equals 144;
- agreement with `NativeScalarFiberFixture.native-numerator`;
- translated original execution has the same readout;
- agreement with the original exported `6/25` at the common denominator 600;
- explicit semiring expansion using the integer semiring;
- a control showing that the readout uses the actual supplied operator value.

Two intended compiler rejections forbid replacing the complete expression execution with an unrelated constant seed and changing its readout to 145.

## General native DAG compiler

`amplitudes/native_scalar_program.py` compiles the arbitrary-even-n current tables into a shared program with exactly the zero/one/factor/sum/product grammar above.

Each nonleaf current contributes a marked **local** coefficient: `-lambda` at the amputated root, or `lambda/q^2` at an internal current. Every partition contributes the product of its three child expressions; every current sums all its partitions. The compiler reads declarations and attachments, never a cached amplitude.

The program validates declared rational factors, operation arity, strictly earlier operand references, reachability and factor use. A separate fold evaluates its arithmetic. A natural-number fold counts diagram choices, and optional expansion recovers factor words under an explicit budget.

Checks compare compiled programs against both the native current evaluator and original recurrence at 4, 6, 8, 10 and 12 points. At eight points the expanded factor words reproduce all 280 individual topology weights from the independent direct enumeration. Cyclic operands, undeclared factors and dead instructions are rejected. Changing a sum to a product demonstrates that valid expression syntax alone does not certify the intended amplitude.

This compiler targets the **grammar modeled by Agda**. There is not yet a verified Python-to-Agda compiler or an imported Agda proof term for every Python-generated DAG. The distinction is retained in the receipts.

## Verification

```powershell
pwsh -NoProfile -File research/nima/checkers/check_native_amplitude_resolution.ps1
python research/nima/amplitudes/native_scalar_program_check.py
python research/aspect/scc/scc.py check nima-native-amplitude-resolution
```

Artifacts:

- `results/agda-ScalarAmplitudeResolveFixture.json` — fresh aggregate proof check;
- `results/native-amplitude-resolution-formal-audit.json` — source-bound rejection controls;
- `results/native-scalar-program.json` — source-bound compiler/readout comparisons.

## Remaining gates

The native-Resolve amplitude connection is established for all finite expressions and the concrete six-point fixture. Remaining general-n gates are:

1. machine-checked completeness and uniqueness of the physical partition/tree enumeration;
2. machine-checked correctness of the actual DAG compiler and its connection to the formal expression model;
3. any further physical scope beyond the supplied scalar tree rules, including loop measures.

Weights and algebra remain supplied inputs, not consequences of bare fibration. No new physical prediction or independent review is claimed.
