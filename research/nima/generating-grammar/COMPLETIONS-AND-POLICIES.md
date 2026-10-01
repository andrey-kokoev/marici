# Arithmetic completion and policy interpretation

Generated from `completions-and-policies.json`. Source definitions and compiled witnesses govern claims.

## Coefficient grammar

```text
Pair = Word x Word
Signed = Pair / Balance
Denominator = 1+Word
Representative = Signed x Denominator
Rational = Representative / Cross
Balance((a,b),(c,d)) iff append(a,d)=append(c,b)
Cross((a,d),(b,e)) iff multiply(a,den-signed(e))=multiply(b,den-signed(d))
add-pair((a,b),(c,d))=(a+c,b+d)
multiply-pair((a,b),(c,d))=(ac+bd,ad+bc)
negate-pair(a,b)=(b,a)
den-product(1+a,1+b)=1+(a+(1+a)*b)
add-representative((a,d),(b,e))=(a*e+b*d,d*e)
multiply-representative((a,d),(b,e))=(a*b,d*e)
negate-representative(a,d)=(-a,d)
```

Operations are first constructed on representatives and proved compatible with the quotient. FaithfulComponentRing transfers laws only after source operations and preservation proofs exist.

SignedBridge and FractionBridge instantiate NativeCoefficientTransport; every finite marked sum/product Expr has direct and translated native executions with commuting readouts.

Inductive Word, set-quotient/type-theoretic infrastructure and library algebra used in proofs. Factor weights and the geometric component-normal-form hypothesis remain supplied.

The recorded source proves inversion of each admitted positive component denominator. Do not promote this to an independently formalized universal localization theorem for arbitrary targets.

## Exhaustive public-definition coverage

Proof-local where helpers are not public definitions. Module schemas and aliases are also checked against source.

### signed

| Group | Kind | Definitions | Rule |
|---|---|---|---|
| signed.carriers | type_and_relation | Pair, Balance, Signed | Word pairs and the balance set quotient. |
| signed.representatives | operation | zero-pair, one-pair, add-pair, multiply-pair, negate-pair | Construct representative arithmetic from component append and multiply; negation swaps the pair. |
| signed.generic_readout | readout | Readout.pair, Readout.read | Difference of numeral images, descending through Balance into a supplied commutative ring. |
| signed.readout_laws | proof | Readout.add-polynomial, Readout.multiply-polynomial, Readout.pair-add, Readout.pair-multiply, Readout.negate-polynomial, Readout.pair-negate, Readout.cancel, Readout.respects | Ring polynomial identities and compatibility with representative arithmetic and Balance. |
| signed.integer_bridge | equivalence_and_proof | append-native, balance-native, balance-component, to-difference, from-difference, roundtrip, asInt, fromInt, recover, faithful, asInt-fromInt | Compare to the library difference quotient and signed normal forms; prove roundtrips and faithful readout. |
| signed.preservation | proof | numeral-pos, pair-asInt, raw-add, raw-multiply, raw-negate | Show constructed representative operations commute with integer readout. |
| signed.quotient_operations | descent | QuotientOperation.operation, QuotientOperation.preserves, add, multiply, zero, one, negate, negate-preserves, add-inverse, signedRing | Descend operations, prove their readouts and additive inverse, and assemble the source commutative ring. |
| signed.embedding | embedding_and_proof | embed-word, embed-word-add, embed-word-multiply | Embed Word as (n,0), preserving constructed addition and multiplication. |

### rational

| Group | Kind | Definitions | Rule |
|---|---|---|---|
| rational.denominators | carrier_operation_and_proof | Denominator, word, den-product, den-product-word, multiply-native, den-product-native, den-signed, den-readout | Strictly positive word denominators, constructed product, and compatibility with signed/library readouts. |
| rational.carriers | type_and_relation | Representative, Cross, Rational, include | Signed numerator/positive denominator pairs modulo component cross multiplication. |
| rational.readout | equivalence_and_proof | representative, cross-law, cross-native, asRational, from-representative, fromRational, recover, readout-recover, faithful | Construct coefficient-quotient/readout roundtrips and cross-relation compatibility; not package equivalence from scalar equality. |
| rational.representatives | operation_and_proof | add-representative, multiply-representative, raw-add, raw-multiply, negate-representative, raw-negate | Construct representative operations first and prove their rational readouts. |
| rational.quotient_operations | descent | QuotientOperation.operation, QuotientOperation.preserves, add, multiply, zero, one, fraction, negate, negate-preserves, readoutRing, rationalRing | Descend the constructed operations, then transfer ring laws through the faithful readout. |
| rational.embedding_and_inverse | embedding_and_proof | embed-signed, embed-signed-add, embed-signed-multiply, positive-inverse-readout, positive-inverse | Embed signed coefficients at denominator one and invert every admitted positive component denominator. |

### faithful

| Group | Kind | Definitions | Rule |
|---|---|---|---|
| faithful.transfer | law_transfer | Transfer.associative, Transfer.commutative, Transfer.add-unit, Transfer.mul-unit, Transfer.add-inverse, Transfer.distribute, Transfer.ring | Transfer laws through an injective readout only after source operations and preservation proofs are supplied. |

### transport

| Group | Kind | Definitions | Rule |
|---|---|---|---|
| coefficients.transport | expression_interpretation | Transport.mode, Transport.expression, Transport.evaluate-commutes, Transport.native-readout-commutes, Transport.translated-readout-commutes | Retain all factor labels while recursively transporting expressions along a coefficient homomorphism, with evaluation and both native readout squares. |

### bridge

| Group | Kind | Definitions | Rule |
|---|---|---|---|
| rational.fixture | source_fixture | ScalarFixture.weight, ScalarFixture.sum-channels, ScalarFixture.expression, ScalarFixture.execution, ScalarFixture.denominator-from-source, ScalarFixture.numerator-from-export, ScalarFixture.denominator-from-export, ScalarFixture.computed, ScalarFixture.translated, ScalarFixture.expanded | Reuse the existing channel weights and marked 1/600 factor; construct actual native execution, obtaining the existing 6/25 scalar with both readout comparisons. |
| rational.cancellation_controls | proof | signed-cancellation, fraction-cancellation | Check signed cancellation and equality of common-factor fraction representatives in the coefficient quotient. |

### macros

| Group | Kind | Definitions | Rule |
|---|---|---|---|
| native.retained_macros | native_derivation_and_recovery | Retained.family, Retained.family-run, Retained.family-premise, Retained.family-value, Retained.pair-family, Retained.pair, Retained.pair-run, Retained.pair-left-premise, Retained.pair-right-premise | Construct actual P-kind applications and recover their original premise packages and derivations. No output is admitted as a fresh literal. |

## Policy audit: all nine source rows

A native encoding or a retention macro does not establish a derivation of the entire policy operation.

| Operation | Status | Available native correspondence | Remaining input / adapter |
|---|---|---|---|
| Re-present retained records | partial_realization | The path ledger's source/target family and deconstruct_family give exact ordered-record recovery; TableFibrationCycle supplies the record-presentation recovery theorem. | A typed macro connecting the particular record presentation and its admission certificates to native Package/Resolve. The existence of an equivalence does not itself admit its endpoint packages. |
| Passive frame change | conditional_encoding | Native rules retain supplied pointed equivalences, inverses/composites and path lifting. | The actual representation acting jointly on maps, witnesses and any metric; relabelling covariance alone does not construct it. |
| Fixed-frame comparison | computation_not_identified | The DG source supplies C2*r*C1 and reference/higher-witness corrections. Native compose-kind instead composes pointed equivalences and retains both parents. | A typed interpretation of DG maps, weak return and corrections; arbitrary actual/reference maps need not be equivalences. |
| Witnessed reference substitution | conditional_encoding | The source operation retains actual maps and versions reference/witness data with a supplied change witness. | A type-correct map from that DG reference-change witness to native pointed package equivalence or higher-path data; these witness types are not silently interchangeable. |
| Protected active frame request g | external_admission_policy | The candidate protocol checks [g,delta(v)]=0 and [g,v]=delta(K_g), then updates W to g*W+K_g*d. | A representation and filler-space policy plus an actual certificate; native generic Admit does not generate K_g or select the request. |
| Permitted history edit | external_admission_policy | History is retained; native higher-kind records an actual equality between supplied paths. | A permission/readout/cost policy and a bridge between its allowed edits and the native path type. Equal readouts do not imply path equality. |
| Family promotion | partial_realization | GeneratingGrammarMacros.Retained.family-run constructs the actual P-kind derivation; family-premise recovers each original package AND its derivation by refl. | The grouping, fresh-label identity policy and next-level endpoints; the retention macro does not supply them or independent copies. |
| Uniform family admission | external_admission_policy | Membership in the intersection of member permission sets means every member supplies permission for the same request. P-kind can retain the resulting family of certificate packages. | A mapping from these member permissions to the declared Admit family; native P-kind itself neither chooses nor proves an admission policy. |
| Independent carrier copying/pairing | core_macro_with_external_policy | GeneratingGrammarMacros.Retained.pair-run constructs the actual ordered-pair derivation; pair-left-premise and pair-right-premise recover both original packages and derivations by refl. | This pairs supplied operands. It does not construct an independent new operand or establish independence by duplicating an existing derivation. |

## Boundary

Public declarations/module schemas/aliases in the six named arithmetic/macro files; every row in the policy ledger has an explicit assessment.

A generation-preserving interpreter for every policy and retained-path computation, and an authoritative boundary for all sector operations in the repository.

Neither admitting the desired answer as a fresh seed, storing an arbitrary external computation as an atom, nor labelling an unproved correspondence an equivalence counts as deriving the operation.

Next executable: Construct a typed native interpreter for the DG comparison operation with its weak-return correction, under a frozen admission policy. Pairing and family-retention macros are now implemented and checked; they do not close that computational adapter.
