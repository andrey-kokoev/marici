# H10: the declared participant exchange is not admitted by the source constructor

## Scope of the negative result

H10 expressly requires complete tagged participant data, **including chirality**, to travel with their owner, while preserving the ambient spin-component trivialization. It also expressly declares non-admission by the existing source constructor to be a failure, rather than permission to introduce a new convention. That admission clause is decisive here.

The source `open_product_solver.py`, embedded in the pinned joint-incoming archive through the strained-phase and axial-deformation archives, reconstructs every unswitched native seam as

    edges += [(i,j,lift(NL[i],NL[j],+1)),
              (i+5,j+5,lift(NR[i],NR[j],-1))].

The chirality signs are tied to the current left/right **slots**. `endpoint(src,sign)` reads left/right geometry, Om, A, T0 and HC; it does not read transported owner-chirality fields. Adding such fields to the input dictionary does not change this rule.

Consequently, swapping complete owner packets would require the old right body's -1 chirality in the new left slot, but the existing constructor supplies +1 there. The required exchanged packet is not represented by this constructor's declared input interpretation. Merely moving the geometry through its available slots is not the tau specified by H10.

## Exact local witness, not just an API observation

At each actual endpoint pose, retain the old right body's normal vectors n_R,0 and n_R,1. The directed seam 0->1 is not incident to small cell 2 (positive endpoint) or small cell 3 (negative endpoint). It is therefore retained, unswitched, in **all eight pairing sectors**.

With the same ambient spin components and vertex labels, the transported old-right comparison is

    V_required = lift(n_R,0,n_R,1,-1).

Independent reconstruction through the source's new-left rule instead gives

    V_actual = lift(n_R,0,n_R,1,+1).

`check_participant_exchange.py` reconstructs both endpoint poses from exact geometry and evaluates these two matrices with the source lift formula. Both are unitary; their difference is nonzero at each endpoint. The receipt records the exact difference, a nonzero entry and its squared Frobenius norm. This is an owner-data mismatch, not a floating tolerance issue or a comparison of output probabilities.

The cell/memory permutations themselves pass X20^2=I and X8^2=I. A round trip of geometry labels alone therefore cannot diagnose this missing transport of participant-specific structure.

## What is and is not concluded

**H10 is refuted within its stated source-constructor admission scope.** We have not constructed a full H_tau, proved a mismatch of every total-Hamiltonian entry, or ruled out abstract relabelling symmetry. Those stronger conclusions do not follow from this test and are not needed for the explicit admission falsifier.

A tag-aware successor builder could carry the original chirality into the new slot and re-examine the inter-chirality sewing and half-turn conventions. That would be a new admitted comparison package with new validation obligations, not a passing result for the unchanged source constructor. We do not reset spin frames, fit a compensating phase, equate different switch orders, or insert a measurement of histories to repair this failed claim.

The failure is independent of H9's native-energy trace obstruction. H1–H4 remain scoped mathematical results for the original supplied model. No general physical distinction between two incoming particles is established by this software/model admission failure.
