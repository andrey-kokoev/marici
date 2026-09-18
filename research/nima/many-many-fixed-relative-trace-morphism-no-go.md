# Many-many fixed relative-trace morphism no-go

Suppose a state-independent linear map

$$
\Theta_{\rm tr}:\mathcal A_{\rm trans}\to\mathcal S_1
$$

satisfied

$$
\operatorname{Tr}(\Theta_{\rm tr}(T))
=\operatorname{Tr}^{\rm rel}_G(T)
$$

for every admissible source state `G`. The left side is independent of `G`, whereas for `T=S_ell`,

$$
\operatorname{Tr}^{\rm rel}_G(S_\ell)=G(\ell)-G(0).
$$

Choose two admissible states with different endpoint increments. Their right sides differ while the left side is fixed, a contradiction.

Therefore the determinant comparison cannot be a bare map from the translation algebra. It must be typed over the source-state graph, for example

$$
\Theta_{\rm tr}:(G,T)\longmapsto K_{G,T},
$$

or factor through a source-selected state/functional before entering the determinant ideal. Its compatibility law is groupoid-natural rather than an unbased algebra homomorphism.

This correction preserves the common logarithmic operator `H_X`; it changes only the type of the remaining comparison morphism.

Status: fixed state-independent comparison excluded; source-graph-indexed determinant comparison remains open.
