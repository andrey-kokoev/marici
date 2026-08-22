# 1905 — The Proposed P02 Graph-Principal Filler Fails Source Typing

The proposed first-jet filler \(P_{02}\) does not extend to an untruncated
flat superconnection. The obstruction is stronger than a nonzero second-jet
curvature: the candidate fails source typing already at first jet.

## Two different rank-two spaces

The earlier certificate conflated

\[
P_{\rm raw}=\langle e_6,e_8\rangle
\]

with the supported graph pair

\[
P_{\rm graph}=\langle i(j_0),i(j_2)\rangle,
\qquad i(j)=(-Rj,j).
\]

Exact reduction gives

\[
\dim P_{\rm raw}=\dim P_{\rm graph}=2,
\qquad
\dim(P_{\rm raw}+P_{\rm graph})=4.
\]

Hence

\[
\boxed{P_{\rm raw}\cap P_{\rm graph}=0}.
\]

The raw block carries the observed parity label but is not supported in the
localization kernel. The actual graph generators lie in that kernel but mix
several raw parity characters.

## The factorization fails

The moving checker exported a row-reduced kernel basis. Rowwise agreement of
its curvature images with selected raw free rows was incorrectly interpreted
as equality with the literal equation-(58) graph basis.

Direct substitution into that graph basis gives, for both parameter axes,

\[
\operatorname{rank}\Theta|_{S_6}=1,
\qquad
\operatorname{rank}\Theta|_{i(J_3)}=1,
\]

and

\[
\boxed{
\operatorname{rank}\bigl(\Theta-(\Theta i)\pi_J\bigr)=1.
}
\]

Therefore the former identity

\[
\Theta=(\Theta i)\pi_J
\]

and the resulting claim \(D_{\rm tot}^2=0\) are withdrawn.

## Horizontal gate

Independently, neither the raw \(P_{02}\) projection nor the full raw
\(J_3\) projection has connection-invariant kernel. The raw modular covector

\[
(3,0,121)
\]

is nonhorizontal on both axes. Its dual connection closure has rank six, and
the invariant closure of the raw projection kernel is all of \(A_9\).

Thus no nonzero quotient connection descends through the proposed
contraction.

## Disposition

The mixed derivatives of \(h_{02}\) and \(\pi_{02}\), and consequently the
\(dx\wedge dy\) component of a superconnection square, are not canonical
objects for this candidate. No higher cell is fitted to repair a construction
whose prerequisite source maps fail.

The raw observations survive only at their demonstrated strength:

\[
\operatorname{rank}\Theta=1,
\qquad
\dim(\operatorname{im}\Theta_x+operatorname{im}\Theta_y)=2,
\]

with raw-basis covector \((3,0,121)\). They no longer carry a graph-cell or
horizontal-line interpretation.

## Stability and scope

The complete signature reproduces at

\[
(p,A,D)=(32003,12,6),\ (32003,12,7),\ (32009,12,6).
\]

This is a finite-field, finite-cutoff no-go for the proposed \(P_{02}\)
construction. It does not rule out a different independently derived
relative-support complex or physical-chain object.

## Durable verification

- Sequence authority: `seqclaim-0f2e288841a12e04fc1901ea`
- Epistemic event: `ev-000000002278-607ac4c2-1f10-4af7-81cb-80babce39b3b`
- `research/nima/physical-theta-graph-principal-cell.md`
- `research/nima/checkers/audit_physical_theta_graph_typing.py`
- `research/nima/checkers/check_physical_graph_cell_horizontality.py`
- `research/nima/checkers/certify_physical_theta_graph_cell.py`
- `research/nima/results/physical_theta_graph_typing_audit_p32003_a12_c6.json`
- `research/nima/results/physical_theta_graph_typing_audit_p32003_a12_c7.json`
- `research/nima/results/physical_theta_graph_typing_audit_p32009_a12_c6.json`
- `research/nima/results/physical_graph_cell_horizontality_p32003_a12_c6.json`
- `research/nima/results/physical_graph_cell_horizontality_p32003_a12_c7.json`
- `research/nima/results/physical_graph_cell_horizontality_p32009_a12_c6.json`
- `research/nima/results/physical_theta_graph_cell_certificate.json`
