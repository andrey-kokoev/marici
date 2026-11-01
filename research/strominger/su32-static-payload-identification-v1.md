# The full-packet refinement does not descend to static named-fibre content

## Identification tested

The previous cross-cone construction was a locally admissible refinement: a downstream reference can carry a complete upstream comparison packet unchanged. The present test asks whether this is the same as the existing named-fibre content assignment.

Four hypotheses are tested together:

1. Each of the 80 named fibres has one static finite JSON value.
2. Its paired P and E presentation cells expose that same value.
3. A reference record reads the value associated with its reference cell.
4. The full comparison result at a presentation cell is literally the value of that cell's named fibre.

The fourth condition is an attempted identification, not an established source law. The result rejects this conjunction; it does not reject the carrier or a content-bearing fibration in general.

## A finite occurs-check obstruction

The 224 contact records contain 136 distinct producer constraints. In **48** of those constraints, an input reference and the output presentation belong to the **same named fibre**. These occur in **72** of the contact records.

For any such producer, the unchanged `compareAt` constructor places the input fibre value at the proper subtree

```
output.records[label].payload
```

If the full output were also that same static fibre value, it would have to equal an object strictly containing itself.

Let s count nodes in a finite JSON value tree. Literal containment gives

\[
s(v_f)<s(C(v)),
\]

whereas the proposed identification gives `C(v) = v_f`. These conditions contradict one another. No choice of finite JSON payload values fixes the problem.

The receipt retains all 48 witnesses with source occurrence, output cell, self-referenced cell, fibre identity and exact containment path. All four sign bindings are tested, giving **192 concrete rank checks**. The mathematical obstruction is not limited to those sample values: the constructor always places the referenced value inside the enclosing record/object structure.

## Controls locate the failure

Without identifying paired presentation cells, every dependency goes strictly forward by two cell-centre layers. The proposed static identification introduces the self-dependencies; the native geometric traversal did not contain a self-hop.

The earlier local attachment remains valid at its stated scope: it can retain an upstream packet inside a later packet. It did not assert that the later object was the same static value as that nested input.

A positive control constructs all 136 producer comparisons over one complete, unchanged 80-value test bank, for every sign binding: **544 checks**. Every constructor accepts its inputs. The comparison packets remain separate witnesses rather than overwriting the static values. Thus the problem is not the coexistence of static content and retained comparison histories; it is their literal identification.

This control is not a physical global-state construction or a completed operational fibration. It only shows that the four hypotheses above contain the additional source of contradiction.

## Formal and executable evidence

`agda/FinitePayloadOccursCheck.agda` proves that strict natural-number rank increase rules out equality, and even rules out a rank-preserving identification. A fresh safe Cubical Agda check passes with ignored interfaces and stable source/library inventories.

The Agda module does **not** formalize the JavaScript JSON model or the whole edge-five construction. Source extraction, native fibre associations, the containment path and finite JSON node counts are checked separately by the executable audit.

```sh
python research/strominger/checkers/check_finite_payload_occurs_agda.py
node research/strominger/checkers/check_su32_static_payload_identification.mjs
python research/aspect/scc/scc.py check strominger-su32-static-payload-identification-v1
```

The SCC adapter runs both the fresh Agda closure and the Node audit. Its successful outcome means the obstruction is verified; `candidateIdentificationPassed` is false.

Receipt: `results/su32-static-payload-identification-v1/verification.json`.
Contract: `contracts/su32-static-payload-identification-v1.json`.

## Consequence for the fibration problem

The packet-in-payload refinement cannot simply be promoted to the static 80-fibre binding. The next identification must distinguish **content** from the **operation/transport witness over that content**, or explicitly specify a different representation such as time-indexed or graph-backed values. Those alternatives are not implemented here, and none is silently treated as equivalent to finite JSON.

In particular, a return of the active fibre reference does not imply return or equality of its full growing history. This agrees with the earlier retained-history return boundary.
