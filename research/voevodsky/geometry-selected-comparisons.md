# Can the actual assembly pieces select the comparison rule?

## Question and claim boundary

The operator requests deriving the comparison rule missing from the conditional meta-tetrahedron, rather than choosing a scalar view merely to make its faces commute.

Active obligations: **local attachment transport** and **sewing across the retained sectors**, before promoting a state diagram to a comparison of construction procedures.

- **Problem:** Does restricting the spinor encoders to the actual proton triangles and neutron two-face sectors supply a compatible scalar view?
- **Conjecture under test:** Local geometric restriction, possibly followed by a canonical eigenline selection, determines a common one-component comparison without altering the old pairings or returns.
- **Rivals:** A sector retains two independent input directions; spectral selection differs between sectors; an apparently successful rule silently changes adjacency or discards a positive channel.
- **Risky consequences:** The original neutron local selectors and the corresponding restricted spinor blocks must admit the proposed scalar factorization. Selected local rays must sew through one common input functional. A face-local isometric comparison must preserve normalized ray overlaps.
- **Falsification attempt:** Recover the actual sector membership from stored coordinate provenance; compute its full input Gram matrix; test both spectral lines and every three-sector assignment; compare opposite pairs as a forbidden repair.
- **Disposition:** The geometric-restriction rule fails. Selecting local eigenlines does not repair its sewing, and swapping to opposite faces changes the source assembly. Twelve exact checks reproduce these residuals. This rejects the named local rules, not every possible coherent mixing rule.

## Follow the actual local pieces

The proton constructor has twelve centroid-edge triangles belonging to its four tetrahedral faces. Restricting the electron encoder to one face gives a rank-one input Gram matrix. Thus a local scalar view exists, up to its amplitude/phase convention, but the four face views are different: their normalized projectors have pairwise overlap 1/3.

The neutron candidate instead groups its triangles into three **adjacent two-face sectors**. Their membership is recovered from the stored triangle owners and coordinate order, not chosen for this test:

\[
(0,4),\qquad (1,3),\qquad (2,5).
\]

Each original twelve-coordinate sector has a rank-one local selector in its retained intrinsic metric. The checker reconstructs every coefficient of these three local selectors from the stored mode numerators.

## Restrict the fourth encoder to those sectors

Let J_i be the two-row block of the normalized fourth encoder belonging to belt face i. Retain its whole input Gram matrix

\[
F_i=J_i^\dagger J_i.
\]

For the current signed belt, each F_i has trace 1/3 and rank one. For an actual adjacent pair, define

\[
H_{ij}=F_i+F_j.
\]

All three retained sectors have

\[
\operatorname{tr}H_{ij}=\frac23,
\qquad \det H_{ij}=\frac1{12},
\qquad \operatorname{spec}H_{ij}=\{1/2,1/6\}.
\]

Consequently the corresponding four-row restriction of J_X carries **two independent input directions**, not one. It cannot factor losslessly through the original sector's single complex mode. This is an operator-rank obstruction, not a discrepancy in one sampled scalar intensity.

## Selecting a spectral line does not solve the common-view problem

The principal eigenprojector is

\[
Q^{\mathrm{major}}_{ij}=3H_{ij}-\frac12 I.
\]

Discarding its secondary eigenline removes a channel whose eigenvalue is 1/6, not zero. More importantly, the principal projectors for the three sectors are different, with pairwise overlap 1/4. The same issue remains if one chooses secondary lines: the checker tests all eight major/minor assignments and none gives a common input ray.

For a comparison factoring through the fixed global neutron return, its restriction to sector s would have the form v_s ell, where v_s is the retained local mode and ell is one common scalar functional. All three input Gram matrices would then be proportional to the same ell-dagger ell. The geometrically selected lines do not satisfy that condition.

The proton has the corresponding global-sewing issue: its four distinct face rays cannot all equal one common scalar view while preserving those local face restrictions. A subsequent coherent mixing operation could change the views, but that would require the missing inter-carrier adapter rather than follow from restriction alone.

## Two tempting repairs fail their source checks

**Re-pair opposite panels.** Pairs (0,3), (1,5), (2,4) do share input rays, and their paired Gram determinants vanish. But they share no edges and are not the retained adjacent-face sectors. This changes the assembly instead of deriving its comparison.

**Rotate the spinor basis to identify corresponding face channels.** Let

\[
Q_i=F_i/\operatorname{tr}(F_i).
\]

Distinct tetrahedral input rays have overlap 1/3, while distinct belt input rays have overlap 1/4. A common unitary basis change and local scalar rescalings cannot alter those normalized overlaps. Hence no isometric face-local identification matches even the three retained distinct tetrahedral directions with the three belt directions.

These are **normalized input effects**, not the raw output-face projectors from the earlier tetrahedral-parent test. The latter had overlap 149/296 on the projected belt. The non-scalar frame normalization changes the input effects; the two calculations concern different operators.

## What remains and where to stop

The existing aggregate E–X isometry remains valid: it preserves the two-component state while mixing face records. The previous conditional six-map diagram also remains valid with its explicitly chosen scalar functional.

The stronger local geometric rule tested here does not derive that functional. The first missing constructor is a **spinor-to-cyclic-mode adapter**, carrying its relative phases and an explicit account of any discarded information, supplied by the assembly operations and compatible across the original sectors. Its acceptance test is agreement with the stored local and collective selectors without changing the pairing or identifying unequal input rays. This branch stops at that missing operation; it is not repaired by choosing a convenient projection.

No general impossibility of source-derived coherent mixing, no physical particle identification, and no completion of the construction-level meta-tetrahedron is asserted.

## Reproduction

```text
python research/aspect/scc/scc.py check voevodsky-geometry-selected-comparisons
python research/aspect/scc/scc.py challenge voevodsky-geometry-selected-comparisons research/voevodsky/checkers/check_geometry_selected_comparisons.py falsifies
```

The checker was frozen before execution at `0e6eedcf6eea3394`. Exit zero verifies the stated residuals; the scientific classification is `local_geometric_restriction_and_spectral_selection_rules_falsified`, not a successful comparison construction.

Artifacts:

- `research/voevodsky/checkers/check_geometry_selected_comparisons.py`
- `research/voevodsky/results/geometry_selected_comparisons.json`
- `research/voevodsky/results/geometry_selected_comparison_store.json`

All source stores and viewers remain unchanged.
