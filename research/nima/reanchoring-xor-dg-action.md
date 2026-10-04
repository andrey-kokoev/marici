# All four XOR torsors preserve the reanchored DG coherence fragment

## Question and disposition

Does origin-dependent translation on the actual state-block references preserve the existing d,r,u,v,W coherence datum, including typed products and composition?

**Result:** all four torsors pass. Current payloads compose strictly, so this test neither selects q=1 nor requires a homotopy correction to composition. Immutable parent histories remain distinct. This verifies realizations of the specified free DG fragment inside the existing ambient algebra; it does not construct an automorphism of every source generator, a simplicial stable-source comparison, or a lattice realization of the higher products.

SCC obligation: attachment transport and composition compatibility on the existing free DG model. The baseline is [witnessed reference reanchoring](witnessed-reference-reanchoring.md). The source model explicitly adjoins leg, base-path, weak-return and triangle witnesses; this test does not derive those adjunctions from a universal stable source.

## Actual source and operation

For q,o,g in F2^2, read the actual state-block records

\[
D_o^{(q)}=\operatorname{anchors}[s:o:o\mathbin\oplus q],\qquad
H_o^{(q)}=\operatorname{hs}[s:o:o\mathbin\oplus q].
\]

The source differential is homological: u,v have degree 1 and W has degree 2. Define

\[
\kappa_g^{(q)}(o)=H_{o\oplus g}^{(q)}-H_o^{(q)}.
\]

Select the frame at origin o by the repository's existing `reanchor` operation. Its witness for the next selected reference is precisely this difference, not an origin-independent constant.

For the current reference d, the update keeps r fixed and uses

\[
d'=d+\delta\kappa,\qquad
u'=u+r\kappa,\qquad v'=v+\kappa r,
\]

\[
W'=W+\kappa u+v\kappa+\kappa r\kappa.
\]

The implemented equations are

\[
\delta u'=rd'-1_A,\qquad
\delta v'=d'r-1_B,\qquad
\delta W'=d'u'-v'd'.
\]

The generator assignment extends multiplicatively on the typed free fragment. Testing its differentials on generators and composable generator products verifies the corresponding DG realization. It does not identify the image of every ambient leg or witness generator and hence is not a full-source automorphism theorem.

## Exact checks

Checker: `checkers/check_reanchoring_xor_dg_action.py`.
Result: `results/reanchoring-xor-dg-action.json`.

The checker reruns the actual baseline audit before testing:

| Check | Count |
|---|---:|
| Origin translations, including identities | 64 |
| Two-translation composition laws | 256 |
| Generator differential identities | 448 |
| Typed product and product-differential identities | 1536 |
| Round trips | 64 |
| Rejection after omitting the quadratic W correction | 48 |

For every q,o,g,h, the existing operations satisfy

\[
R_{\kappa_h^{(q)}(o\oplus g)}
R_{\kappa_g^{(q)}(o)}
=
R_{\kappa_{g\oplus h}^{(q)}(o)}
\]

on current frame payloads: reference, unit witnesses, triangle witness, and all retained comparison witnesses. The staged and direct operations have different retained parents; those histories are not equated.

For every nonidentity translation, deleting the quadratic term kappa r kappa makes the triangle differential fail. Thus passing the full update is not an artifact of checking only the first-degree boundary equations. Reusing the same kappa for the reverse translation also fails: the correct reverse witness is -kappa.

Fresh execution passed with exit code 0: `structured_command_execution:e_25120_1790953088071910900_149`.

```text
python research/nima/checkers/check_reanchoring_xor_dg_action.py
```

## Interpretation and next boundary

The result extends the earlier rank-three witness comparison to the actual reanchored coherence payload and its typed free-fragment products. It is consistent with the existing general update law: the new computation exhausts all four proposed XOR torsors rather than testing selected references only.

All q pass. Selection of the marked torsor therefore remains independent of this test. The [direct-reference/local-mark adapter](reference-semantics-carrier-versus-counted-domain.md) is still unspecified.

A separate comparison must send the higher DG fragment to the proposed integral/affine target while preserving differential, products, and the intended endpoint rebasing. This checker does not extend the rank-three lattice readout through u,v,W. The distinction between current-payload equality and history retention must also survive any claimed simplicial realization.

Problem: determine whether the proposed translation law survives the higher DG update. Conjecture: the existing formulas work for every state torsor. Rival: some q require higher corrections or are excluded. Falsifier: exact differential/product tests and deletion of the quadratic correction. Disposition: all q survive strictly on current payloads; the deletion controls fail as predicted. No physical interpretation or formal-backend theorem is promoted from this finite symbolic audit.

Artifacts remain local and uncommitted. No commit, push, or deployment was performed.
