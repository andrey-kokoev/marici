# Moving-carrier PN covariance under a declared transported-grid policy

## Result

The complementary contexts now have an exact typed PN square on all36 field coordinates, conditional on the explicit transport of the tensor-grid ordering and phase conventions. The neutron target is the rotated carrier constructed in the preceding audit, not a relabeling of the fixed belt.

The prospective contract was frozen at `scc-freezes/ramsey-moving-carrier-PN-v1.4df947719615e9db.json`; the SCC challenge passes. No source-owned file was modified.

## Neutron frames reconstructed, not assumed

For each of the actual18 ordered triangles, the source mode is `r + i sqrt(3) s`. Reapply the source intrinsic-frame constructor to the rotated r and s:

    a = <s,s>, b = <r,s>, v = r - (b/a)s, beta = <v,v>.

The orthonormal axes are `s/sqrt(a)` and `v/sqrt(beta)`. Exact arithmetic verifies that the target columns are the rotated source columns, while a, b and beta remain unchanged. All36 target metric radicands and selected coefficient numerators agree with the existing source registry, occurrence by occurrence.

Thus the geometric map Q_N between the source and rotated target has identity coefficients **in these different moving intrinsic bases**. It is not identity on ambient spatial vectors and not an automorphism of the old fixed belt. This step strengthens the earlier spatial-Gram audit by binding the source's actual intrinsic coordinates.

Triangle order, sector matching and ordered occurrences are retained rather than reselected. These are part of the declared policy.

## PN constructor rerun in the target normalization

The proton uses its fixed directed-edge/vector world labels, so Q_P is the previously constructed signed permutation. Transport its return vector, metric and ordered tensor-grid occurrences by Q_P. The normalized factor probabilities at corresponding grid occurrences are unchanged; the existing ordered factor-rotation convention therefore has the same factor inputs.

Using those target phases, metric and grid, the checker regenerates every entry of T_B from the original tensor-factor PN formula. It does not seed T_B as `T_A Q_P^-1`. The regenerated matrix satisfies

    Q_N T_A = T_B Q_P,

where Q_N has identity coefficients between the independently reconstructed moving neutron frames. All1,296 entries are checked exactly.

As a control, the unchanged numerical target matrix T_A gives `T_A Q_P != T_A` at864 entries. A local co-moving sewing receipt therefore cannot be read as a fixed-world PN covariance theorem without transporting its input convention.

Because Q_P is unitary and T_A is metric-unitary, the verified square also entails metric unitarity of T_B for the reconstructed target metric. This is a consequence of the checked relation and imported candidate theorem, not independent source selection of a unique PN completion.

## Scope of the positive result

This proves covariance of the existing PN candidate **under the declared transported-grid policy**. The ordered rotations in that candidate already choose an extension on complementary modes. We have preserved and transported that choice; we have not proved it canonical or physically selected. Re-running a fresh grid selector with unrelated tie-breaking is a different question.

The field-level result does not transport a source-ineligible geometric PN facet into an eligible one. The two contexts continue to have separate role-indexed triangle permits and separately admitted assemblies. The earlier total-domain no-go remains intact.

Still open:

- a source-bound E moving frame and joint NE covariance;
- edge/vertex restriction objects retaining both parent contexts and permits;
- actual native higher-WG comparison/restriction derivations;
- full four-facet incidence descent, whole-space admission and the Ramsey root.

The next discriminating check is whether the existing joint NE contrast exchange has a compatible target E frame under the same marking, without dropping the three retained baryon coefficients or six raw E complement directions.

## Artifacts

- Contract: `contracts/ramsey-moving-carrier-PN-attempt.v1.json`.
- Checker: `checkers/check_ramsey_moving_carrier_PN.py`.
- Exact target frames and PN matrix: `results/ramsey-moving-carrier-PN-v1.json`.

The checker validates live direct PN/world-action input hashes and the geometry/triangle-store binding. It uses exact rational and multiradical arithmetic, not proof-assistant certification. No net revision, graph verdict or Git checkpoint was made.
