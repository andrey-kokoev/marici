# Route completeness is required before torsor-kernel descent

## Question

Does a Gram factorization through the currently visible physical routes suffice to prove that a q_G12 lift-torsor direction is null?

## Truncated-route obstruction

Let the complete physical route map be a direct sum

\[
B=\bigoplus_{s\in S}B_s,
\qquad
Q=B^*B=
\sum_{s\in S}B_s^*B_s.
\]

For a source-complete family,

\[
\ker B=igcap_{s\in S}\ker B_s.
\]

But if only a subset \(S_N\subset S\) is represented, the truncated map

\[
B_N=igoplus_{s\in S_N}B_s
\]

has a larger kernel. A direction killed by every retained route may still be detected by an omitted wall, history, tail, or PV-reciprocal route.

The exact two-route hostile is

\[
B_{\rm seen}=\begin{pmatrix}1&0\end{pmatrix},
\qquad
B_{\rm omitted}=\begin{pmatrix}0&1\end{pmatrix},
\qquad
v=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Then \(B_{\rm seen}v=0\), while \(B_{\rm omitted}v=1\). The truncated Gram form falsely classifies \(v\) as radical; the complete form does not.

## Completeness certificate

A valid torsor-kernel conclusion requires one of:

1. a source theorem that the listed route family exhausts every contribution to the physical joint form;
2. an exact decomposition \(Q=\sum_{s\in S}B_s^*B_s\) with all summands represented;
3. a remainder map \(R_N\) with \(R_Nv_i=0\) proved for every torsor basis direction;
4. a quantitative remainder bound that is zero on the torsor subspace, not merely small on tested samples.

A small omitted-route norm cannot prove exact radical membership unless it is exactly zero on the torsor directions. It may support an approximate return bound but not quotient descent.

## Joint faithfulness versus physical completeness

Joint faithfulness of the retained probes on their declared quotient is distinct from completeness of the physical route family. The former says the retained probes separate points in a chosen domain. The latter says no physical contribution has been omitted from \(Q\). Neither implies the other.

Target-unitary changes \(B\mapsto UB\) with \(U^*U=I\) preserve both \(Q\) and \(\ker B\). Thus the issue is not factorization gauge; it is missing source routes.

## Verification

`research/aspect/checkers/check_route_completeness_torsor.py` verifies that an omitted exact route detects a torsor direction lying in the truncated route kernel.

## Disposition

The owner request must include a route-completeness theorem, not only a matrix factorization for visible sectors. Until every omitted route is proved zero on the rank-seven torsor, kernel descent remains unverified even if the retained Gram form is positive.
