# Reader-natural E/P comparison with history-covariant coefficient operators

Connection: `face-chart-transition-descent`, specifically the reader-prefixed PN attachment that falsified the proposed fixed-named-matrix U(2) extension.

## Result

**The earlier body-carrying adapter passes the exact failed reader square when the coefficient interpretation retains its history.**

- All24 actual marked cases agree in all five coefficient slots.
- Both routes reach the same full target P packet and the same PN packet.
-120 live native transfer validations pass.
- Exact field/readout squares hold on all36 coordinates of the retained field.
- The unchanged full L/G/N operators act covariantly on the checked preparations. Their compressed five-coordinate matrices change with history.
- A fresh safe-Cubical theorem proves coefficient naturality for any number of reader steps followed by PN.

The old U(2) obstruction is preserved and its false-square fixture still fails. No native reader law or forward E generator was changed.

## 1. The comparison and the actual square

Use the body-carrying coefficient comparison

    T x = (x3,x4,x1,x2,x0).

It preserves the genuinely retained C2/M2 values and carries the other two body coefficients under the declared advancing-occurrence convention. The outside coefficient convention is explicit; it is not an equality of the different outside reference vertices.

With the actual P reader P_P and the whole-reference negative E reader P_E,

    P_P T = T P_E.

The new runtime test reuses the exact geometry and full-reference cases from the obstruction receipt. At P origin2 it constructs a direct PN attachment, returns through the actual inverse-PN step, takes the actual P reader to origin3, and attaches PN there. Re-reading the negative-E target instead gives the very same P packet, including origin, references and all five permutation slots, and then the very same PN packet.

The formerly conflicting final C occurrence is checked literally: its role, vertex and index agree. Agreement is not confined to a scalar, a norm or a projected endpoint.

The E edge remains an explicitly negative-direction comparison obtained by whole-reference reversal. It is not advertised as an emitted forward E operation.

## 2. History-aware field bindings

Let A be the actual P field-reader involution, G the preceding co-moving E/P geometric comparison, S the PN map and Pi its coefficient permutation. The exact check establishes A G = G A.

Starting from the retained negative-E binding B_E0 = B_P Q, define

    B_E1 = A B_E0 P_E*,
    B_P0 = G B_E0 T*,
    B_P1 = A B_P0 P_P*,
    B_Nr = S B_Pr Pi*.

All are isometric five-column bindings. Their metric-adjoint readers satisfy, for r=0,1,

    R_Pr G = T R_Er,
    R_Nr S = Pi R_Pr,
    R_P1 A = P_P R_P0,
    R_E1 A = P_E R_E0.

These reader equations hold on all36 field inputs. The unused prepared E8 complement is not silently identified with a native E return: this test uses the retained negative-E carrier from the earlier reversal construction.

The geometric trace rows are also retained. Their signed edge reindexing under A is computed and checked against H A, not fitted to the five-preparation.

## 3. The operator test did not silently change the native matrices

The N-to-N comparison along inverse-PN, P-reader, PN has field map

    S_N = S A S^-1

and coefficient map

    Delta = Pi P_P Pi*.

For each actual full neutron matrix X in {L,G,N}, put

    x0 = B_N0^sharp X B_N0,
    x1 = B_N1^sharp X B_N1.

Fresh exact checks give

    X B_Nr = B_Nr xr,
    x1 = Delta x0 Delta*,
    x1 != x0.

The checker additionally evaluates the explicitly transported full operator S_N X S_N^-1 on B_N1. Its action there equals the unchanged X action. Thus no change of the full native X matrix is needed **on these checked preparations**.

This does not assert S_N X S_N^-1 = X on every unprepared field direction. Full-input readout squares and prepared-subspace operator covariance are distinct verification claims.

The discrepancy in the previous attempt was therefore not that the body comparison violated these native operator actions. It was the extra demand that their compressed five-coordinate patterns remain numerically identical across changed interpretations.

The moving preparation still differs from the original fixed target preparation. This result does not undo that earlier distinction or independently derive the coupling from geometry.

## 4. Generic kernel theorem

`agda/RamseyCovariantEPReader.agda` proves, for any coefficient type A and any fixed outside-context function c:A->A,

    body_c(x) = (x3,x4,x1,x2,c(x0)),
    P_P^n body_c = body_c P_E^n,
    Pi P_P^n body_c = Pi body_c P_E^n.

The proof is by coordinate computation and induction on n. The field/runtime experiment uses c=identity. An arbitrary c in the coefficient theorem is not asserted to preserve a metric or define an admitted physical operation.

The theorem is about coefficient histories. The live geometry check covers the24 actual one-step reader-prefixed cases; it does not independently prove arbitrary-length geometry admission. Absolute origins are retained, not identified modulo the two-step matrix period.

Fresh safe-Cubical closure checks pass with ignored interfaces. The old adapter's false commuting square is rejected as a hostile control.

## 5. Disposition

The previously found reader-naturality obstruction is repaired by a comparison already suggested by prior research, with its changed coefficient interpretation made explicit. No new primitive operation or discarded coordinate is needed for this local test.

What this does not establish is the complete four-facet semantic descent, independent source selection of the outside/coupling convention, or all other geometric overlap laws. The original conjecture is not promoted merely because its first counterexample has a well-scoped alternative.

## Reproduction

    python research/voevodsky/checkers/check_ramsey_covariant_EP_reader.py

Receipts:

- `results/ramsey-covariant-EP-reader-input-v1.json`: actual packets, operations, complete references and24 matching squares;
- `results/ramsey-covariant-EP-reader-v1.json`: exact history bindings, operator checks and fresh kernel verification.

Verification boundary: the coefficient theorem is kernel-checked; geometry, exact multiradical field/readout identities and operator matrices are separately checked runtime inputs. The kernel does not interpret the JavaScript source or the field matrices.

No owning source, earlier scientific receipt, conjecture-net verdict or graph admission was changed.
