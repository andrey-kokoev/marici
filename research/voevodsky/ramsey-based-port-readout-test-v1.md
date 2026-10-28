# Fresh test: the port-based field lift passes; the typed reader binding remains open

**Correction:** the named-reader failure below tested an unchanged N selector, not the intended outgoing E window. The [corrected E-reader test](ramsey-outgoing-E-readout-v1.md) passes the ordered E readout and complementary recovery. The earlier field calculation remains valid; its selector mismatch must not be treated as an obstruction to outgoing E observation.

Node: `T-seam-based-port-readout-binding` (local net revision31).
Prospective scope: `contracts/ramsey-based-port-readout-attempt.v1.json`.
Checker: `checkers/check_ramsey_based_port_readout.py`.
Receipt: `results/ramsey-based-port-readout-v1.json`.

## Constructed from the existing marked data

The occurrence reflection induces (b c)(u v) on the N reader. Applying this to its ordered face/patch lists gives the exact patch permutation

    [3,4,5,0,1,2].

Of all six permutations of the three belt sectors, three make the chartwise transformed belt vertices consistent across shared occurrences. The already declared active-window/sector seed and Q select

    [2,1,0].

That choice is consistent on shared vertices. This is compatibility with the prior seed ansatz, not independent source selection of that ansatz or a spatial-isometry theorem.

The checker binds every chart patch back to its actual triangle in the native store. It checks that the native numerator metric matches the full-five source metric coordinate by coordinate. Equal dimensions alone are not used to identify carriers.

## Exact whole-field construction

For each of18 required plane pairs, evaluate the prior pointed Gram port formula, without fitting phases:

    B_ba w_a = w_b,
    B_ba conjugate(w_a) = (c_a/c_b) conjugate(w_b),
    c_a = <w_a,conjugate(w_a)>.

All required mode norms and normalized conjugate-eigenline Gram shapes agree. Every full-plane map is metric-unitary, and its independently constructed reverse is its inverse. Six of the required directed pairs are outside the previously checked12-port route. Their success is a NEW finite extension test of the formula, not inherited route admission.

Assemble these blocks with the patch and sector permutations to obtain a full36-coordinate map U. With B the unchanged saved neutron five-column embedding and R its metric adjoint, exact arithmetic gives

    U^sharp U = I36,
    U_backward U = I36,
    U B = B Q,
    R U = Q R,
    R B = I5.

All five columns pass with zero residual entries. The readout equation is a full5-by36 matrix equality, not a test only on prepared inputs. All complementary directions remain present.

For THIS port-exchange map, U squared is identity. This was computed rather than imported from occurrence reversal. It does not contradict the prior opposite-branch converter's nontrivial forward-square phases: the present map uses ordinary Gram port transport, not that branch converter. No16-coordinate bank was identified with the8-coordinate E field.

## First unresolved interface: native versus outgoing named reader

The numerical field/readout square does not fix the already distinct label types:

| N reader slots1,2,3 | Labels |
|---|---|
| Native incoming reference | M0,C1,M1 |
| Literal outgoing reference at the same indices | C1,M1,C2 |

The literal basis cast therefore fails the named-reader gate. This test supplies no additional decoder that turns one list into the other while preserving both C0/M2 provenances. The five-column square is an actual constructive improvement over slot conjugacy alone, but not the completed typed T-seam adapter.

Disposition: **numeric field lift passes; typed binding remains open**. This is not a universal nonexistence result. No PN/NE extension or native reverse admission was attempted after this gate.

## Controls and verification

Five negative controls reject:

1. Identity field transport in place of the Q lift.
2. An unchanged readout in place of the transported one.
3. Coordinate erasure masquerading as an invertible full-field map.
4. A source/target plane pair with unequal Gram shape.
5. The literal outgoing-basis cast as a native labelled reader.

The fresh bounded exact checker passed twice (the second run includes the full-field readout and added negative controls). Recorded direct input hashes of the imported reader, seed and local-field receipts were checked against live files. Imported research modules and inputs are pinned in the new receipt; this is not a replay of their entire scientific suites or a transitive proof certificate.

Reproduce from repository root:

    python research/voevodsky/checkers/check_ramsey_based_port_readout.py

Owner source implementations and prior receipts are read-only. The conjecture net, graph admission and formal outcomes were not changed by this test.
