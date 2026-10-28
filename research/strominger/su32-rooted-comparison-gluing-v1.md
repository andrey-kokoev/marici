# Rooted comparison gluing: first bounded operadic test

## Result

The existing candidate comparisons admit exact **rooted, typed gluing** into reconciliation. The result is a finite Segal-style construction on specific two- and three-operation trees, not a cyclic operad or a new native physical law.

The main falsification is useful: **matching geometric sites and record-support labels is insufficient for gluing.** Shared record identities must carry the same payloads, including between branches that were separately valid.

## Shape and port interpretation

Use the fixed entry reading `reading:0:-1`. One vertex is the existing `compareAt` operation, with two channel-operand inputs and a ternary comparison output. Another is the existing `reconcileAt`, with two comparison inputs and a four-record output.

Two tested shapes are:

```
Two vertices:                    Three vertices:

channel --\                      channel --\
           compare --\                      compare --\
channel --/           \          channel --/           \
                       reconcile                        reconcile
prepared comparison --/          channel --\           /
                                            compare --/
                                 channel --/
```

The two-vertex test can expand either child of reconciliation. The other child stays a complete supplied boundary operand, with its own retained provenance. The three-vertex tree expands both children.

A port carries a typed operand header: node kind, occurrence anchor, original cell attachment, reference identities and payloads. The producer/consumer distinction belongs to the tree ports; it is not identified with P/E or with the input direction signs. The operation's own cell records the consumer location. Every tested edge uses actual shared-face adjacency.

Input-slot indexing follows the existing constructor and preserves its ordered histories. It is not claimed to be a native planar cyclic order.

## Construction is checked against existing results

`su32-rooted-comparison-gluing.mjs` decomposes an existing validated reconciliation tree into:

- local operation headers and declared output headers;
- internal edge connections with expected operand headers;
- complete external boundary operands.

Internal headers do **not** contain nested `children`. Thus the entire retained root is not hidden in each local vertex decoration.

The gluing function reconstructs the result by calling the original `compareAt` and `reconcileAt`. It verifies each connected port, each computed local output, and all tree/boundary coverage. It does not return a cached result or declare any list of decorations a realization by definition.

For these fixed shapes, fixed slots and boundary operands, deterministic evaluation fixes the result recursively. Restricting the original tree and gluing again recovers its exact nested child histories. Contracting either lower comparison first and then performing the remaining two-vertex graft produces the same final retained tree as the complete reconstruction.

This is an exact syntax/data statement about the candidate operations already implemented, not proof that their physical native maps have been supplied.

## Exhaustive independent-appearance test

The four channel operands contain eight record appearances. Rather than generating them from an already consistent registry, assign each appearance an independent Boolean value: `2^8 = 256` possibilities per binding, across four bindings.

Of **1,024 boundary assignments**:

- **64 succeed**, exactly the four independent record choices per binding;
- **960 are refused**.

Both E-referenced and P-referenced routes accept precisely the same 64 cases and recover equal four-record dictionaries while retaining distinct trees.

For either route:

- 768 cases fail an initial comparison's shared-reference check;
- 192 cases have individually valid comparison outputs but fail reconciliation because a shared record differs between branches.

Every refusal is checked to be a shared-record disagreement, not an arbitrary exception.

The 192 latter cases do **not** refute a Segal condition with correctly specified local operations: the root operation is not valid for those inputs. They refute the weaker proposal that two separately valid lower comparisons with the right support shapes automatically glue.

Repeated record appearances remain references to the same independent record when the constraints pass. The test does not authorize independent copying of payloads merely because a tree has distinct leaves.

## Verified controls

Fresh execution passed:

- **390 exact tree reconstructions**, covering both routes, two choices of two-vertex expansion, and full three-vertex expansion;
- **260 staged gluing checks**;
- **11 negative controls**, including altered port values, missing links, cycles, reused operation vertices, wrong attachment, invented outputs, dropped operands and unreachable vertices.

An attempt to use a reconciliation output where the current `compareAt` requires a channel operand is rejected. This is a refusal by the present typed grammar, not proof that every cyclic extension is impossible.

The raw E-first and P-first trees still differ. No higher path between them is produced by this adapter. No claim is made that contracting arbitrary operation histories preserves syntax.

## Boundary of the result

The Doherty–Hackney paper provides an appropriate language for asking about operation trees. This finite test does not yet provide its required full presheaf, all-tree Segal condition, units, dual color involution or coherent root-changing actions.

In particular:

- selecting E+ versus E- in a central retained core is not yet re-rooting an operation;
- extracting retained input children from an output is not automatically an admitted physical inverse;
- the comparison/reconciliation grammar does not currently close under arbitrary output-to-input grafting;
- native outgoing transport and selection of the forty middle assignments remain separate.

The positive conclusion is narrower and concrete: **the candidate information model supports compositional rooted reconstruction, provided gluing matches full typed record data rather than just support labels.** Root independence is the next additional hypothesis, not a consequence already established here.

## Artifacts

- Adapter: `su32-rooted-comparison-gluing.mjs`.
- Checker: `checkers/check_su32_rooted_comparison_gluing.mjs`.
- Receipt: `results/su32-rooted-comparison-gluing-v1/verification.json`, retaining a full decomposition, a conflicting pair of locally valid comparisons, counters and source hashes.

```sh
node research/strominger/checkers/check_su32_rooted_comparison_gluing.mjs
```

No native source implementation was modified, no formal cyclic completion was installed, and no proof assistant was run.
