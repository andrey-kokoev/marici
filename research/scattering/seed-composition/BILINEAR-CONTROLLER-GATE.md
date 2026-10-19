# A single product cannot supply the controller; two retained terms suffice algebraically

**Strength:** exact source-operation cut-rank obstruction, a two-product algebraic recipe and a retained-information falsifier. No physical controlled interaction, coherent preparation, independent photon outputs or formal outcome admission.

[Previous controller/preparation audit](CONTROLLER-PREPARATION-AUDIT.md) · [Checker](check_bilinear_controller_gate.py) · [Receipt](results/bilinear-controller-gate.v1.json)

## 1. Bounded source search

Four existing candidate interfaces were inspected rather than replacing the missing interaction with a fitted matrix:

| Existing source | Relevant operation | Attachment still missing |
|---|---|---|
| [Bilinear branch preparation](../../nima/bilinear-branch-preparation-synthesis.md) | Endpoint-compatible coefficient products, retained branch detail and rank-one cut constraints | Physical authority to prepare the operands, normalization and schedule |
| [Retained interaction pipeline](../../nima/retained-interaction-end-to-end-audit.md) | Conditional kick/drift action with reversible records and work bookkeeping | Source-derived control law and native clock attachment |
| [Retained proton operation](../../nima/retained-proton-operation.md) | Bound six-port proton execution with geometry/spin/exchange readings | Electron exchange and a contact/mediator adapter; these are explicitly unbound |
| [Shape-interaction finite audit](../../voevodsky/shape-interaction-finite-operator-audit.md) | Conditional finite isometries, propagators and retained hidden-channel checks | Native phase/port and intermediate-state adapter |

None of these inspected interfaces already supplies the current pair/segmentation controller and preparation. This is a bounded attachment audit, not a claim that no relevant operation exists anywhere in the repository or in physics.

The bilinear interface does supply a useful exact restriction and constructive test, which we now apply to the actual glued primitive registry.

## 2. One bilinear product has rank one at each interface vertex

The source operation is

    B(x,y)_[a b] = x_a y_b,

for endpoint-compatible primitive words. At a fixed intermediate vertex v, its incoming/outgoing coefficient block is an outer product and has rank at most one.

The smallest controller conflict is already at B. The candidate requires the two composites

    AC = AB then BC,
    CA = CB then BA.

To retain both with unit coefficient while rejecting premature reversal or switching, the required block is

                next BC    next BA
    incoming AB    1          0
    incoming CB    0          1

Its determinant is one. A single bilinear product would instead require

    x_AB*y_BC = x_CB*y_BA = 1,
    x_AB*y_BA = x_CB*y_BC = 0,

which contradicts its determinant-zero identity. This remains an obstruction when both desired diagonal amplitudes are arbitrary nonzero numbers. If one branch is unpopulated, a single product can handle that restricted case; it is not the full controller table.

This exact cut-rank test reuses the source's operation rather than assuming that a context-dependent right operand is already available.

## 3. Two retained product terms are enough at this cut

The two desired diagonal entries have an explicit decomposition:

    B(e_AB,e_BC) + B(e_CB,e_BA).

The checker constructs both products with the actual retained-path ledger, keeps their operand records, and verifies the summed coefficient readout on the complete sixteen-word primitive successor carrier. All other words remain represented with zero coefficient.

Extending this to the eighteen supplied controller contexts gives block ranks:

    A:2, B:2, C:2, D:1, E:1, Ep:1, Dp:1.

At each vertex, order the available outgoing primitives. Define two right profiles: the first chooses the first outgoing primitive at each vertex, the second chooses the second where it exists. Split left context coefficients according to which profile the context requires. On the endpoint-compatible domain their two products reconstruct the entire desired table, including arbitrary nonzero amplitudes on the contexts.

Thus the minimum is **two product terms** for this full table. This is a per-interface cut statement: the disconnected vertex blocks are not being treated as one dense rank-two matrix. The receipt retains the exact profiles and context masks.

### What this does not supply

The context-to-profile assignment is still supplied by the macro dictionary and memory. The two output records are not automatically a physically coherent sum: the ledger constructs the individual products, while this audit checks their sum as an explicit external coefficient readout. It does not register a sum as if it were a native single-product preparation.

An actual implementation must supply the control of the two terms, their relative phase or other declared combination rule, and the retained controller state. Two algebraic product terms are **not two emitted particles**, two scattering channels or a prediction of a branching ratio.

## 4. Final-occurrence aggregation destroys a direction needed by preparation

Let N be the endpoint-incidence matrix of the supplied ten-primitive glued registry, and A_final aggregate a retained two-step payload by its last primitive occurrence. The exact source identity is

    A_final B(x,y) = diag(y) N x.

The new checker verifies every one of the 100 primitive basis pairs with the actual ledger. Since both sides are bilinear, this certifies the rational identity; the same coefficient identity extends to real or complex inputs. The successor has sixteen retained words and rank N=7.

Consider

    w = e_AB - e_CB.

Both primitives end at B, so their contributions cancel in Nw:

    Nw=0,
    A_final B(w,y)=0 for every right operand y.

The retained path payload itself is nonzero. With neutral right input its AB BC and AB BA entries have coefficient +1, while CB BC and CB BA have coefficient -1. The cancellation occurs only when different incoming histories are merged by the final-occurrence reader.

The synchronized preparation projector S from the previous audit does not annihilate this same direction:

    Sw = (1/2,0,-1/2,0,0,1/2,0,0,-1/2,0) != 0.

Therefore no construction of the form `diag(y) N x` can equal Sx on the full free input carrier. Changing the right operand cannot repair the missing input distinction; the zero identity still holds even if a right operand is selected depending on that particular input. A sum of right-weighted terms with the same unconditioned left input also remains blind.

This is deliberately narrower than a no-go for the retained source. Left/context conditioning can expose the witness: keep its AB component before composing with BC, and the resulting final BC coefficient is nonzero. That is precisely the additional operation requiring source justification. It cannot be performed after the necessary distinction has already been erased.

## 5. Refined construction gate

The broad phrase “find a source interaction” is now reduced, within this operation class, to a concrete specification:

1. keep the incoming histories and pair/segment context distinct;
2. derive two context-conditioned product channels rather than one shared right profile;
3. supply and retain the control/combination rule, including relative phase if a coherent sum is claimed;
4. realize the correlated preparation while retaining its six-dimensional rejected record;
5. only then apply any coarse final-occurrence or photon-mode readout.

The available bilinear source law gives the two-term algebraic recipe, but not the missing physical control/preparation. The inspected other interaction interfaces cannot be imported merely because they also have a small state space or a hidden channel.

Physical metric, triangle faces, independent asymptotic photon sectors and normalized scattering remain separate obligations. No existing contract, pinned source-owner receipt or formal outcome is changed. No physical annihilation or ratio 372 is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_bilinear_controller_gate.py
python research/scattering/seed-composition/check_bilinear_controller_gate.py --check
python research/scattering/seed-composition/check_controller_preparation_audit.py --check
python research/scattering/seed-composition/check_segmented_copy_transport.py --check
python research/scattering/seed-composition/check_retained_word_transport.py --check
python research/scattering/seed-composition/check_incidence_audit.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker recomputes the preceding exact construction, exercises the source ledger and records dependency hashes, cut ranks, profile masks and the hidden-history witness. It writes only its own receipt. `--check` is read-only; the inspected historical interaction suites are not claimed as freshly replayed.
