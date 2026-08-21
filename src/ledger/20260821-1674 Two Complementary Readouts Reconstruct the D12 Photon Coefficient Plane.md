# 1674 — Two Complementary Readouts Reconstruct the D12 Photon Coefficient Plane

Date: 2026-08-21

Sequence claim: `seqclaim-97ffe1f3fa199abbfaa8752b`

## Exact result

The one-loop QED D12 \(\Phi_1\) sector has coefficient coordinates

\[
v=\left(\frac{g_{4,1}}{g_2},\frac{g_{4,2}}{g_2}\right).
\]

Two independently derived readouts see different combinations:

\[
R_{\rm Bell}(v)=g_{4,1}+\frac32g_{4,2}
=\frac{157}{9240}g_2,
\]

\[
R_T(v)=g_{4,1}+g_{4,2}=\frac1{70}g_2.
\]

Their joint matrix has determinant

\[
\det\begin{pmatrix}1&3/2\\1&1\end{pmatrix}=-\frac12,
\]

so the pair, unlike either readout alone, is injective on this coefficient
plane. It reconstructs

\[
\boxed{
\frac{g_{4,1}}{g_2}=\frac{41}{4620},
\qquad
\frac{g_{4,2}}{g_2}=\frac5{924}.
}
\]

The nonforward combination was discovered from the triangular crossed-cut
filtration and independently certified using exact amplitudes at two angles.

## Architectural conjecture

This motivates the cross-sector hypothesis that physical sectors are governed
not by one complete lens but by jointly conservative families of supported
readout functors on filtered coefficient objects.

For cosmology, the corresponding falsifier is to construct the residue,
infinity-Gysin, nearby-cycle, and physical-pairing maps independently from the
source and test their joint kernel. No fitted splitting or rank coincidence
can substitute for those typed maps.

The version-1 falsifier contract has now been frozen before importing any new
cosmology map packet. Its exact rank engine passes positive and negative
synthetic controls. Its current scientific verdict is **inconclusive** because
the frozen domain and required source-derived maps have deliberately not been
supplied by this calculation.

## Scope

Joint conservativity is proved only on the declared two-dimensional QED D12
coefficient plane. The cross-sector statement is a conjecture. This entry does
not claim completeness on the full photon amplitude, at all EFT orders, or in
cosmology.

## Durable verification

- `research/nima/checkers/check_jointly_conservative_d12_readouts.py`
- `research/nima/results/jointly-conservative-d12-readouts.json`
- `research/nima/results/qed-phi1-crossed-cut.json`
- `research/nima/results/qed-d12-phi1-closure.json`
- `research/nima/jointly-conservative-readout-families.md`
- `research/nima/contracts/cosmology-joint-readout-falsifier.v1.json`
- `research/nima/checkers/check_cosmology_joint_readout_protocol.py`
- `research/nima/results/cosmology-joint-readout-protocol-check.json`
- sequence claim: `seqclaim-97ffe1f3fa199abbfaa8752b`
- epistemic-graph event:
  `ev-000000001897-c997b30a-8f09-4fdf-86f6-14394b1449c9`
- falsifier-freeze event:
  `ev-000000001904-90ff9ab6-4ab3-4cec-a7d3-34dc0a073c69`
