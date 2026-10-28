# Falsification: the proposed U(2) semantic extension fails a native reader square

## Verdict

**The specified moving U(2) comparison does not extend coherently to the actual reader-prefixed PN construction while preserving the claimed retained values.**

This refutes the semantic extension asserted in the bold conjecture. It does not refute the bare retained four-facet construction or the weaker existential claim that some other semantic interpretation might work under the declared input policy.

The failure is not scalar-locality, absent single-source generation, an empty overlap, or lack of a forward E generator. It is a noncommuting square involving the already declared negative-direction reader and an actual forward P reader.

## 1. The two fixed reader laws

Use the convention output[i] = input[permutation[i]]. The live source P reader is

    P_P = [2,3,0,1,4].

The proved full-reference reversal uses Q = [4,3,2,1,0]. Its reversed P-reader edge is therefore a negative-direction E reader with

    P_E = Q P_P^-1 Q = [0,3,4,1,2].

No operation is added to the terminal forward E source. This is precisely the existing whole-reference negative-direction policy being tested for semantic descent.

The local moving family previously derived from the retained pair and the fixed named L/G/N coefficient actions is

    T_U x = (x3,x4,x2,U(x0,x1)).

## 2. The impossible naturality square

Allow independent context choices U and V at the source and target. Compatibility with the reader histories would require

    P_P T_U = T_V P_E.

But their first rows are

    row0(P_P T_U) = e2*,
    row0(T_V P_E) = e1*.

Choose x = e1. The first route produces0; the second produces1. Neither U nor V appears in these entries.

The kernel proof permits arbitrary context functions, not only unitary ones. It also proves the stronger statement: even an otherwise unrestricted target adapter cannot repair the square if it continues to read the genuinely retained C occurrence in its first slot.

The necessary third source value is x1. The locally operator-compatible family instead assigns x2 there. This is the exact incompatibility, not an unspecified missing coherence argument.

## 3. These are actual matching occurrences and actual native ports

For each of24 original P markings, the runtime checker constructs:

1. its native P reader from origin0 to1;
2. complete PN/NE reference extensions at both ends;
3. the whole-reference dual E frames, using reflection center K=3, with old 'after' as dual source at origin0 and old 'before' as dual target at origin1;
4. their complementary P re-readings at origins2 and3.

The P re-reading at origin2 has an actual emitted reader transition to the other re-reading at origin3. Its full target chart agrees, including the outside reference.

The conflicting final slot is literally the same occurrence on both routes: same geometric vertex, C role and index3. It is also the occurrence retained by the actual P reader from its source third slot.

Appending the actual PN operation to each route gives identical geometry, origin, operation permutation and shared face, but different packet coefficient permutations. The discrepancy appears at neutron slot3, inside its active window. Thus it is not an unobservable choice confined to the two contexts.

All24 cases pass these binding checks.192 actual native transfers validate. The two resulting packets and full references are retained in the receipt.

## 4. Why the earlier positive tests did not exclude this

The preceding tests established:

- native construction under independently admitted inputs;
- pointwise moving readout equations;
- invariance under unchanged field operators;
- selected named coefficient actions at a local preparation;
- covariance of geometric trace rows;
- a U(2) family at that local scope.

None established naturality of that family under the actual coefficient reader step. Geometric covariance of H does not imply the square above. Treating each context's seed-level interpretation as though it were automatically compatible with retained reader history was the invalid extension.

Changing U changes only context coordinates. The failure is in a retained active occurrence. A context-gauge equivalence therefore cannot hide it, even though different context readouts themselves were allowed to vary.

## 5. A control separates the conflicting requirements

The earlier body-carrying comparison

    T_body x = (x3,x4,x1,x2,x0)

**does** satisfy

    P_P T_body = T_body P_E.

It was already shown to preserve the moving preparation's norm and operator invariance, but not the saved named L/G/N coefficient actions. Exhausting the six positive permutations fixing the retained pair finds no member satisfying both the named-operator condition and reader naturality. The generic kernel obstruction rules out arbitrary context choices within the proposed U(2) family as well.

So the situation is not 'all passive comparisons are impossible'. Rather, two locally plausible semantic requirements, with the chosen interpretation, cannot be combined. One must revise the preparation/reader interpretation or weaken the fixed named-action requirement explicitly. A phase/history-dependent treatment must be re-derived; it cannot be advertised as the unchanged U(2) extension.

## 6. Consequence for the conjecture

I withdraw the claim that the existing structural result and this particular moving U(2) semantic family already fit together at the required source-history scope.

The broader parent remains open. Its wording did not mandate the particular static named-projector interpretation, so this result is not a parent refutation. It is a genuine falsification of the proposed route to that parent, using admitted data and a concrete native reader-prefixed attachment rather than an invented stronger locality demand.

## Verification

    python research/voevodsky/checkers/check_ramsey_EP_reader_obstruction.py

Fresh safe Cubical checks with `--ignore-interfaces` prove:

- no commuting square for any context choices;
- the discrepancy survives the PN active readout;
- no arbitrary target retaining the required C value can repair it;
- reader naturality forces the third source coefficient to be x1.

The positive instance checks pass. A false commuting-square fixture is rejected. Compiler and source inventories remain stable.

Artifacts:

- `agda/RamseyEPReaderObstruction.agda`
- `results/ramsey-EP-reader-obstruction-input-v1.json`
- `results/ramsey-EP-reader-obstruction-v1.json`

Verification boundary: the generic coefficient obstruction is kernel-proved; live JavaScript permutations, complete reference geometry and occurrence bindings are independently runtime checked. The kernel does not interpret the JavaScript implementation.

No owning operation, prior scientific receipt, conjecture-net verdict or graph publication was changed.
