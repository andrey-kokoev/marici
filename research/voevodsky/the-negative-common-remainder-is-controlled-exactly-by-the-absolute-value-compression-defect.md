# The negative common remainder is controlled exactly by the absolute-value compression defect

## Full polarized pair

Let

\[
P\succeq0,
\qquad
Q\succeq0,
\]

and define

\[
D=P-Q,
\qquad
T=P+Q.
\]

The forced common remainder is

\[
K
=
\frac{T-|D|}{2}.
\]

Assume the full pair passes the metric gate:

\[
K\succeq0.
\]

The canonical principal-angle \(C_{34}\) dilation has this property blockwise.

## Isometric source compression

Let

\[
V:E\longrightarrow H
\]

be an isometry and write

\[
P_V=V^*PV,
\qquad
Q_V=V^*QV,
\]

\[
D_V=V^*DV,
\qquad
T_V=V^*TV.
\]

The compressed forced remainder is

\[
K_V
=
\frac{T_V-|D_V|}{2}.
\]

Define the absolute-value compression defect

\[
\Delta_V(D)
=
V^*|D|V
-
|V^*DV|.
\]

Then the following identity is exact:

\[
\boxed{
K_V
=
V^*KV
+
\frac12\Delta_V(D).
}
\]

## Negative-part estimate

Since

\[
V^*KV\succeq0,
\]

the negative part of the compressed remainder satisfies

\[
\boxed{
\|(K_V)_-\|
\le
\frac12
\|\Delta_V(D)_-\|
\le
\frac12
\|\Delta_V(D)\|.
}
\]

Thus compression failure is localized completely in the failure of absolute value to commute with compression.

## Reducing subspaces

Let

\[
E=VV^*
\]

be the range projection. If

\[
[D,E]=0,
\]

then functional calculus preserves the range and

\[
|V^*DV|
=
V^*|D|V.
\]

Hence

\[
\Delta_V(D)=0
\]

and

\[
K_V=V^*KV\succeq0.
\]

Exact reduction therefore transports the principal-angle metric theorem to the compressed observer packet.

## Asymptotically reducing packets

For a packet sequence \(V_n\) with range projections \(E_n\), an estimate

\[
\left\|
|V_n^*D_\lambda V_n|
-
V_n^*|D_\lambda|V_n
\right\|
\le
\varepsilon_{n,\lambda}
\]

implies

\[
\|(K_{n,\lambda})_-\|
\le
\frac12\varepsilon_{n,\lambda}.
\]

The desired regulator-tail condition is

\[
\lim_{n\to\infty}
\sup_{\lambda\succeq\lambda_n}
\varepsilon_{n,\lambda}
=0.
\]

This is exactly the metric estimate required for asymptotic minimalization.

## Relation to the phase-energy filtration

For the limiting bounded Tate multiplier

\[
A=\mathcal A_S,
\]

prior work constructs spectrally adapted packet projections \(E_n\) satisfying

\[
\|[A,E_n]\|
\le
2\delta_n
\]

and

\[
\left\|
|E_nAE_n|
-
E_n|A|E_n
\right\|
\le
2\delta_n,
\qquad
\delta_n\longrightarrow0.
\]

Therefore the target-side forced remainder obstruction obeys

\[
\|(K_n)_-\|
\le
\delta_n.
\]

The remaining estimate belongs to the finite physical family \(D_\lambda\):

\[
\sup_{\lambda\succeq\lambda_n}
\left\|
|E_nD_\lambda E_n|
-
E_n|D_\lambda|E_n
\right\|
\longrightarrow0.
\]

## Graph-form version

For unbounded or merely form-defined \(D_\lambda\), replace operator norm by the common phase-energy graph norm. The required estimate is

\[
\left|
\langle u,
\Delta_{E_n}(D_\lambda)u
\rangle
\right|
\le
\varepsilon_n
\|u\|_{\mathscr E_S}^2

after the declared graph normalization, uniformly over the regulator tail.

It gives

\[
q_{(K_{n,\lambda})_-}(u)
\le
\frac12
\varepsilon_n
\|u\|_{\mathscr E_S}^2.
\]

## Consequence

The external semilocal transport problem now has one quantitative invariant:

\[
\boxed{
\Delta_{E_n}(D_\lambda)
=
E_n|D_\lambda|E_n
-
|E_nD_\lambda E_n|.
}
\]

Exact reduction makes this defect zero. Asymptotic reduction makes its negative contribution vanish. This directly controls the obstruction found by the compression checker and supplies the metric input for the later Mosco theorem.
