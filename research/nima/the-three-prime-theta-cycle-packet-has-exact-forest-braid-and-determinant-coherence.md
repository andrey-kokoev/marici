# The three-prime theta-cycle packet has exact forest braid and determinant coherence

## Question

Does the arithmetic diamond construction extend to a three-prime common refinement without losing route cycles or determinant anomalies?

SCC obligation: finite attachment-presentation transport and route/coherencer compatibility. The candidate retains interval synthesis and a spanning-tree cycle selector. The rival retains only interval history, potentially identifying different source paths.

## Source and analytical construction

Use the Boolean prime cube on products of subsets of {2,3,5}, multiplied by the initial label 2. Its ordered endpoint labels are

\[
2,4,6,10,12,20,30,60.
\]

There are twelve oriented prime-addition edges and seven common-refinement intervals between consecutive logarithmic endpoints. Work in the unweighted interval-edge basis. Let J be interval coverage and partial be endpoint incidence. With D the consecutive-atom incidence,

\[
\partial=DJ,\qquad \operatorname{rank}J=7,\qquad \dim\ker J=5.
\]

Each of the six prime priority orders selects a tree by Kruskal ordering: prime priority, lower endpoint, then fixed edge index. Z_F selects its five chords in fixed edge order. Define

\[
C_F=\begin{pmatrix}J\\Z_F\end{pmatrix}.
\]

No coefficients are fitted to determinant values.

Let H_i be the actual theta interval functions of the predecessor packet, now on these seven intervals. The recorded theta injectivity theorem proves their independence; compact interval support and theta decay give L2 membership. Therefore H has positive definite Gram and a finite coefficient extractor L=(H*H)^-1 H*. The realization and recovery are

\[
\mathcal O_Fc=(HJc,Z_Fc),\qquad
\mathcal R_F(f,z)=C_F^{-1}(Lf,z).
\]

The response is im H direct-sum C^5. No cutoff-uniform inverse estimate is inferred.

## General finite construction lemma

For any finite connected graph with distinct ordered real vertices and signed interval edges, interval coverage J together with the chord selector of a spanning tree gives a unimodular matrix C_F.

Proof: consecutive-vertex incidence D is injective and partial=DJ. Connected graph incidence has rank |V|-1. Once chord coefficients are fixed, the remaining boundary equation on the tree has a unique solution. Deleting one vertex row makes both the tree incidence and consecutive-path incidence square unimodular matrices. Thus the tree-column submatrix of J is unimodular. Ordering tree columns first makes C_F block triangular with that submatrix and an identity chord block. The fixed source column order determines the remaining sign.

If an analytical transform is injective on the elementary interval span, this supplies its finite image reconstruction. The theta application uses that independent injectivity theorem, not matching dimensions alone.

## Forest transport and braid

Set

\[
T_{G\leftarrow F}=C_GC_F^{-1},\qquad
\mathcal T_{G\leftarrow F}=\mathcal O_G\mathcal R_F.
\]

All seven interval coordinates remain unchanged. Cycle coordinates acquire boundary-dependent corrections. Cancellation proves

\[
T_{H\leftarrow G}T_{G\leftarrow F}=T_{H\leftarrow F}.
\]

The two adjacent-priority swap words 121 and 212 both compare (2,3,5) with (5,3,2); their twelve-dimensional transports coincide. All 216 triples of the six forest presentations pass the exact composition check.

This is a forest-presentation braid on one retained source. The priority words choose trees; they do not themselves permute physical prime-labelled states or construct the four-phase successor.

## Noncollapse hostile

Each monotone three-edge path from 2 to 60 has coefficient vector c_word satisfying

\[
Jc_{\rm word}=(1,1,1,1,1,1,1).
\]

Thus all six orders have identical theta history. Nevertheless, their six full vectors C_F c_word are distinct in any fixed forest presentation.

The difference between paths (2,3,5) and (3,2,5) is a nonzero source cycle. Its interval response is zero and its five-coordinate cycle response in the tested forest is (1,0,0,0,0). More samples of the same theta history cannot reconstruct this direction. The cycle port is necessary.

## Determinant and anomaly

Taking top exterior powers gives the finite analytical determinant-line transition. Its coordinate is

\[
\det T_{G\leftarrow F}=\det C_G/\det C_F\in\{1,-1\}.
\]

It is 1 in the common source orientation. This normalizes frames; it does not erase cycle responses.

For K_GF=T_GF-I, use r(K)=-Tr K+Tr(K^2)/2. With column vectors, A=K_GF and B=K_HG compose as B star A. The plus-convention anomaly is

\[
\alpha_3(B,A)=\operatorname{Tr}(B^2A)+\operatorname{Tr}(BA^2)+\tfrac12\operatorname{Tr}((BA)^2).
\]

The checker verifies this formula and the ordered three-factor cocycle. A round trip (2,3,5) -> (2,5,3) -> (2,3,5) has bare det3 anomaly -9 despite identity composite transport. Low regularizers supply the exact compensation. Identity normalized holonomy therefore does not imply strict multiplicativity of the bare factors.

This anomaly belongs to forest transition. It is not the connected Euler determinant of a source state, and the cycle selector has not been identified with that Euler channel.

## Disposition

Constructed: the finite three-prime theta-history-plus-cycle packet, reconstruction, unimodular forest transitions, full-packet braid, determinant-line transport, and exact order-three transition anomaly compatibility. The graph lemma is general; its analytical application explicitly relies on recorded theta injectivity.

Remaining: full Evans comparison, prime-power weights and low Euler trace identification, connected source-state determinant, reciprocal/four-phase successor, archimedean sewing, and cutoff-uniform topology. No Haar-cycle closure or interpretation of the old -4/5 residual follows.

Verification: `uv run --with sympy python research/nima/checkers/check_three_prime_theta_cycle_forest_braid.py`, exit 0. Fifteen grouped checks, including 216 composition triples, pass. Result: `research/nima/results/three-prime-theta-cycle-forest-braid.json`. Theta integrals were not numerically evaluated.
