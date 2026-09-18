# Canonical bilateral dilation of history translation

Use the standard right-shift semigroup on `H_+=L^2(R_+)`

$$
(V_af)(q)=\begin{cases}0,&0\le q<a,\\f(q-a),&q\ge a.\end{cases}
$$

Let `H_bi=L^2(R)` and let bilateral translation be

$$
(U_af)(q)=f(q-a).
$$

If `i:H_+ -> H_bi` extends a function by zero to the negative half-line and `P_+=i^*`, then

$$
V_a=P_+U_ai,
\qquad a\ge0.
$$

The family `U_a` is a strongly continuous unitary group and is the canonical minimal unitary dilation of the unilateral history shift. Its self-adjoint Stone generator is

$$
D=-i\partial_q
$$

on `H^1(R)`.

Thus the dissipative half-line history generator admits a conservative realization before any fitted Green metric. For the two-history Xi carrier, use

$$
H_{\rm dil}=H_{\rm bi}\oplus H_{\rm bi},
\qquad
D_{\rm dil}=D\oplus D.
$$

The complete tail-plus-seam coordinates provide finite-interval factorizations of this bilateral history: discarded past information is stored in the seam rather than erased.

## Port gate

The dilation of the generator does not by itself lift the forcing and observation ports. One still needs vectors or boundary distributions `b_dil,c_dil` such that

$$
P_+b_{\rm dil}=b_0,
\qquad
c_{\rm dil}i=c_0,
$$

and a decomposable metric commuting with `D_dil` that satisfies

$$
K_{\rm dil}b_{\rm dil}=\alpha c_{\rm dil}^*.
$$

Point evaluation is not bounded on bare `L^2(R)`; the port lift must therefore live on the declared Sobolev/graph rigging or use an explicit boundary space.

Status: canonical conservative dilation of the history generator constructed; source-compatible forcing/observation lift and positive colocation remain open.
