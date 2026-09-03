# Framed-metric Markov GL equipment fragment

## Question

Can the nonorthogonal obstruction be repaired by enlarging the object signature rather than weakening normalization silently?

## Claim boundary

This packet constructs a finite fixed-fiber fragment whose objects include an explicit invertible frame at every vertex. It admits arbitrary invertible frame changes. The frame is part of the object; the construction does not claim canonical dependence on the metric alone, and no infinite completion is proved.

## Framed objects

Fix normalized contraction transfers \(A_i\) and invertible frames \(R_i\in GL(H_i)\). Define

\[
M_i=R_iR_i^T
\]

and the framed block kernel

\[
K_{ii}=M_i,
\qquad
K_{ij}=R_i(A_i\cdots A_{j-1})R_j^T
\]

for \(i<j\), with transposed lower blocks. If \(K^0\) is the normalized Markov kernel and \(R=\bigoplus_iR_i\), then

\[
K=RK^0R^T.
\]

Therefore positivity follows from the normalized kernel.

## General linear gauges

For arbitrary invertible \(S_i\), set \(R_i'=S_iR_i\). Then

\[
M_i'=S_iM_iS_i^T,
\qquad
K'=(\bigoplus_iS_i)K(\bigoplus_iS_i)^T.
\]

The transformed object remains in the framed class. Shears and nonunit scalings are now admitted because the target diagonal metric is transported rather than forced back to identity.

## Equipment data

Vertical arrows are frame changes \(S=(S_i)\). Freely adjoin horizontal companions with witnesses \(S_i\) and conjoints with witnesses \(S_i^{-1}\). Unit, counit, and triangle equations reduce to inverse identities. Composition comparisons use matrix multiplication and satisfy pentagon strictly.

Chain concatenation acts on normalized transfers while retaining seam frames. Shared seam frame changes must agree, giving interchange. Contiguous block compression preserves frames and gives identity Beck–Chevalley cells with strict pasting.

## Scope gate

Metrics \(M_i\) alone do not choose frames uniquely: \(R_iO_i\) yields the same metric for orthogonal \(O_i\) but changes normalized transfer coordinates. The current object is therefore \((H_i,R_i,A_i)\), not merely \((H_i,M_i,A_i)\). Descent to unframed metric objects requires an orthogonal quotient and coherence proof.

## Disposition

The nonorthogonal no-go is repaired by a typed framed-metric enlargement. A finite GL gauge equipment fragment exists, but unframed descent and bounded completion require separate certificates.

## Verification

- `research/voevodsky/checkers/check_framed_metric_markov_gl_equipment.py`
- `research/voevodsky/results/framed_metric_markov_gl_equipment.json`
