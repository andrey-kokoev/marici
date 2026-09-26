# Nine-point full sum: cyclic re-anchoring validation

Freshly extended the sourced50-term evaluator with all nine cyclic choices of recursion anchor while keeping external physical chi labels fixed. Pair order is preserved when converting physical indices to local labels; sorting would introduce incorrect signs for mixed-flavor monomials.

`check_nine_point_cyclic_tree.py` passes120 nonbaseline exact coefficient comparisons: five components, eight alternate anchors, three rational inputs. All1350 history products evaluate with nonzero denominators. Inputs include the two previous moment-curve configurations and a seeded general integer9x4 twistor matrix; the latter avoids relying solely on the rational-normal-curve sublocus. Exact matrix and component values are recorded in results/nine-point-cyclic-tree.json.

Components include the three repeated-pair coefficients from the previous turn and two mixed-flavor monomials. At the uniform curve, one mixed coefficient vanishes and the other is1/144. These are outcomes, not assumed support rules. Cyclic agreement is at the summed level; individual histories are not expected to be cyclic invariant.

This is a nontrivial normalization/boundary/Grassmann-sign check, but still uses the same source formula under re-anchoring. It does not independently derive super-BCFW recursion, prove a symbolic identity on all kinematics, or establish equality of the50-term full tree sum with the four-channel geometric construction.

Next geometric comparison must use common data. Read the fork's bosonized6D target projection z=Z[:,2:]-Z[:,:2]*B and its h frame, and explicitly derive which reduced4D fermions/components the sampled source forms represent. Then evaluate the source tree at that very quotient configuration, accounting for bosonization/gauge factors rather than inserting unrelated moment-curve numbers into the two-family coefficient matrix. If the quotient is singular for a selected source chart, change chart or choose another regular common target; do not regularize by arbitrary numeric perturbation.
