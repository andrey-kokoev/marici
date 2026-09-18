# Translation Hopf module and endpoint cocycle

Let `H_tr` be the labelled translation Hopf algebra with group-like basis `Q_a`. A source carrier `V` with the declared translations is a left `H_tr`-module via

$$
\rho(Q_a)v=e^{-a/2}S_av.
$$

The identity `Q_aQ_b=Q_(a+b)` gives

$$
\rho\mu=m_{\operatorname{End}(V)}(\rho\otimes\rho),
\qquad
\rho\eta=I_V.
$$

For the paired response dual `V^vee`, define the contragredient action

$$
\langle\rho^\vee(h)\lambda,v\rangle
=\langle\lambda,\rho(\mathsf S h)v\rangle.
$$

The antipode identity makes this a representation, and the evaluation pairing is `H_tr`-invariant:

$$
\langle\rho^\vee(Q_a)\lambda,\rho(Q_a)v\rangle
=\langle\lambda,v\rangle.
$$

Consequently the hyperbolic form on `V direct-sum V^vee` and the graph of the reciprocal/contragredient response action are Hopf-module covariant. This is the algebraic core underlying the already constructed maximal-isotropic Fourier–Poisson response graph.

## Endpoint crossed cocycle

Define

$$
b_a(G)=G(a)-G(0).
$$

Then

$$
b_{a+b}(G)=b_a(G)+b_b(S_aG).
$$

Thus `b` is a one-cocycle for the translation action groupoid. In cochain notation,

$$
\delta b=0.
$$

The Euler endpoint current is its logarithmic weighted synthesis

$$
J_X(G)=\sum_{p\le X}\sum_{k\ge1}\frac1k p^{-k/2}b_{k\log p}(G).
$$

It therefore belongs to a crossed-cocycle port over the Hopf module, not to the scalar counit port.

## Six-port status

| Port | Construction |
|---|---|
| unit | `eta(1)=Q_0` |
| counit | `epsilon(Q_a)=1` |
| multiplication | label concatenation `Q_a Q_b=Q_(a+b)` |
| comultiplication | group-like diagonal `Delta(Q_a)=Q_a tensor Q_a` |
| realization | source module `rho` |
| dual realization | antipode-twisted contragredient `rho^vee` |

Status: six-port Hopf module core closed algebraically. Linking, determinant, and Xi compatibility remain separate module/comodule morphism tests.
