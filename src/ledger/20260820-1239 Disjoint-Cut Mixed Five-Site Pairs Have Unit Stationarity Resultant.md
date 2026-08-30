# Entry 1239 — Disjoint-Cut Mixed Five-Site Pairs Have Unit Stationarity Resultant

## Frozen representatives

Entry 1238 leaves six source-present free \(C_5\)-orbits in which the one-cut root \(y_e\) is distinct from both roots \(y_i,y_j\) of the connected-region wall:

\[
\begin{aligned}
&G_{-e_{12}}\mid g_3,
&&G_{-e_{12}}\mid g_{34},
&&G_{-e_{12}}\mid g_{345},\\
&G_{-e_{12}}\mid g_4,
&&G_{-e_{12}}\mid g_{45},
&&G_{-e_{12}}\mid g_5.
\end{aligned}
\]

All routing distances are taken directly from Entry 1234's conical five-cycle.

## Root reduction

For a region of size \(m\), impose the two wall equations by

\[
y_e=-\frac52t,
\qquad
y_i=b,
\qquad
y_j=-mt-b.
\]

Let \(R_e,R_i,R_j\) be the three labelled routing foci and let

\[
d_{ab}^2=(R_a-R_b)^2.
\]

## Two exact stationarity equations

Pair stationarity requires

\[
n_i+n_j\parallel n_e.
\]

Two polynomial conditions retain its full three-focus geometry.

First, the loop point and the three foci must be coplanar. With

\[
p=\frac{y_e^2+d_{ei}^2-y_i^2}{2},
\quad
q=\frac{y_e^2+d_{ej}^2-y_j^2}{2},
\quad
r=\frac{d_{ei}^2+d_{ej}^2-d_{ij}^2}{2},
\]

the coplanarity determinant is

\[
C_{m pl}
=
y_e^2d_{ei}^2d_{ej}^2
+2pqr
-y_e^2r^2
-d_{ei}^2q^2
-d_{ej}^2p^2.
\]

Second, clearing denominators from the collinearity Gram determinant gives

\[
\begin{aligned}
C_{\parallel}
={}&
\left[
y_j(y_e^2+y_i^2-d_{ei}^2)
+y_i(y_e^2+y_j^2-d_{ej}^2)
\right]^2\\
&-4y_e^2y_iy_j
\left[(y_i+y_j)^2-d_{ij}^2\right].
\end{aligned}
\]

## Exact elimination

For every one of the six labelled representatives, Symbolica computes

\[
\boxed{
\operatorname{Res}_b(C_{\rm pl},C_{\parallel})=1
}
\]

over \(\mathbb Q(z,t)\), before imposing \(z^2=5\). The unit remains a unit after specialization to \(\mathbb Q(\sqrt5,t)\).

Therefore the full coplanarity-plus-collinearity system has no common algebraic solution for any of the six source-present routing configurations.

## Result

\[
\boxed{
\text{the six disjoint-cut }M1+A_m\text{ pair orbits have no stationary Landau solution.}
}
\]

Combined with Entries 1237–1238, 21 of the 49 compatible pair orbits are now classified:

- seven are confined to \(t=0\);
- eight project only to existing one-wall thresholds;
- six have unit stationarity ideal.

No new carrier or coefficient divisor has appeared in these classes.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_mixed_pair_landau_disjoint.rs`
- `research/benincasa/results/five-site-mixed-pair-landau-disjoint.json`

## Next falsifier

Proceed to the 28 remaining connected-region pair orbits. Begin with pairs whose two cut supports intersect in two occurrences, then one, then zero. Preserve exact labelled routing distances; do not infer elimination from the coarse arc-size profile.
