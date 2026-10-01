# Does the conditional exchange test actually require the two triangles?

## Controlled intervention

`check_seed_exchange_structural_controls.py` retains the SAME four vertex labels, existing S4 probe dictionary, six record-coordinate conventions and initial preparation. It removes each non-seam primitive edge in turn, then all four, leaving only AB and BA. Removed record ports are unavailable for execution and remain idle zero coordinates; deleting those unused coordinates leaves the compared output unchanged.

This tests the current hypothesis's actual dependence on its edge domain. It does not silently rebuild the carrier metric, change the preparation, or reinterpret the observation after deleting an edge. The inspected hypothesis contains no rule for such graph-dependent rebuilding.

## Result: two-pulse discriminator survives without either triangle

The complete AB-then-BA output is identical in the full seed, all four single-edge deletions, and the seam-only graph. In particular,

    endpoint-fixing: w_BA=1,
    directed-transition: w_BA=1/3.

Therefore this discriminator tests probe choice and the exchange instrument. It does NOT test the two-triangle construction, its indirect paths, or a jointly generated physical reference.

The checker also verifies all ten composable two-edge protocols with unused edges removed. Their outputs depend only on the executed labels and their assigned features. More generally, for a fixed prepared state and fixed event maps, any admitted word has the same product action regardless of unexecuted edges. A structural environment effect would require an additional law changing those maps or preparation.

## What is genuinely seed-dependent

The full graph has two vertex-simple A->B paths and two B->A paths, supporting all four mixed-rectangle protocols. Deleting BC or CA removes the indirect return path; deleting AD or DB removes the indirect forward path. The seam-only graph has one path in each direction.

Thus the four-corner comparison domain genuinely requires all six original edges under the declared simple-path extraction. However, when an edge is removed, the corresponding experiment is UNAVAILABLE. Its response is not zero. Treating absence as a zero numerical output would insert a new intervention/readout convention.

This is structural dependence of available comparisons, not yet a force or response of the remaining system to its changed environment.

## Consequence for operational hypothesis v1

The proposed local exchange task remains a mathematically implementable, discriminable conditional model. But its short transfer signature cannot serve as evidence that the shared two-triangle object explains that response. The model's seed-specific contribution currently lies in available path words and their retained comparisons.

To claim stronger explanatory dependence, the source must determine how the retained surrounding relationships affect preparation, feature geometry, accessible operations or measured response. Existing global-body laws and reference-attachment candidates are possible research branches, but their additional assumptions cannot be silently imported here.

Do not repair this result by choosing a graph-dependent normalization after seeing it. Either accept that this candidate is a local instrument on a supplied path domain, or state and independently motivate a new environment-sensitive source operation.

## Verification

    python research/nima/checkers/check_seed_exchange_structural_controls.py

Fresh exact checks pass, including imported carrier-probe controls, five deletion variants, unchanged full AB-BA outputs for both kernels, all ten primitive-pair controls, and rejection of unavailable rectangle corners. No new physical response law or hardware experiment is claimed.
