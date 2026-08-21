# Entry 1241 — The Seven Four-Focus Five-Site Landau Ideals Are Frozen

## Remaining pair class

Entry 1240 leaves seven compatible connected-region pair orbits with disjoint cut supports. Write one representative as

\[
q_A=mt+y_0+y_1,
\qquad
q_B=nt+y_2+y_3.
\]

Retain two signed roots:

\[
y_0=b,
\quad
y_1=-mt-b,
\quad
y_2=c,
\quad
y_3=-nt-c.
\]

## Invariant routing basis

Take \(R_0\) as origin and define

\[
v_i=R_i-R_0,
\qquad i=1,2,3.
\]

Their labelled routing Gram matrix is

\[
H_{ij}
=
\frac{d_{0i}^2+d_{0j}^2-d_{ij}^2}{2}.
\]

Across the seven source representatives, its determinants reduce under \(z^2=5\) to three nonzero values:

\[
\frac{25-5z}{8},
\qquad
\frac{25+10z}{4},
\qquad
\frac{25+5z}{2}.
\]

Thus the invariant basis construction is valid on the frozen conical slice.

## Loop-point realization

Set

\[
p_i
=
\frac{y_0^2+d_{0i}^2-y_i^2}{2},
\qquad
X=\operatorname{adj}(H)p.
\]

The loop point exists in the three-dimensional routing span exactly when

\[
\boxed{
C_{\rm real}
=
(\det H)y_0^2-p^T\operatorname{adj}(H)p
=0.
}
\]

## Gradient vectors

After clearing only common denominators, the two wall-gradient vectors have basis-coordinate representatives

\[
U=(y_0+y_1)X-(\det H)y_0e_1,
\]

\[
V=(y_2+y_3)X-(\det H)(y_3e_2+y_2e_3).
\]

Pair stationarity is the labelled rank-one condition

\[
\boxed{
U_iV_j-U_jV_i=0,
\qquad
1\le i<j\le3.
}
\]

## Frozen elimination ideal

For each of the seven representatives, the admissible projected Landau support is now typed as

\[
\boxed{
\left(
C_{\rm real},
U_1V_2-U_2V_1,
U_1V_3-U_3V_1,
U_2V_3-U_3V_2
\right)
\cap\mathbb Q(z)[t],
\qquad z^2=5.
}
\]

This entry freezes the ideal and its labelled source data. It makes no claim about its elimination polynomial or solution set.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_connected_pair_four_focus_system.rs`
- `research/benincasa/results/five-site-connected-pair-four-focus-system.json`

## Next falsifier

Compute the elimination ideal over several exact finite fields admitting \(z^2=5\), preserving the seven representatives separately. Reconstruct and certify any characteristic-zero factor by exact substitution. A factor appearing only after dropping one collinearity minor is inadmissible.
