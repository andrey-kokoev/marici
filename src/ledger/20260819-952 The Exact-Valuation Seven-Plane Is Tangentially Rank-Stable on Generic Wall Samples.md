# The Exact-Valuation Seven-Plane Is Tangentially Rank-Stable on Generic Wall Samples

## Question

Entry 947 identifies the quadratic triangle-wall sector as the fifth
cross-effect of the exact-valuation functor,

\[
E_2(C)=
\frac{\ker(\Lambda:C\to C)\cap \Lambda C}
     {\ker(\Lambda:C\to C)\cap \Lambda^2C},
\qquad
\dim E_2(C)=7.
\]

That calculation was made at the wall point \((X_1,X_2,X_3)=(2,3,5)\).
Before asking for a Gauss--Manin connection on this object, its rank must at
least remain stable under tangential motion along

\[
X_3=X_1+X_2.
\]

## Exact finite test

The source exporter now accepts arbitrary integral tangential coordinates
\((X_1,X_2)\) and takes its seven exact normal samples at

\[
(X_1,X_2,X_1+X_2+\Lambda),
\qquad -3\leq \Lambda\leq3.
\]

At ambient relation degree ten, the complete sparse relation packet has
11520 columns and 15256 raw rows at each normal sample.  Complete finite-field
reduction gives

\[
\begin{array}{c|c|c|c}
(X_1,X_2,X_3)&\operatorname{rank}R_0&n_1&n_2\\
\hline
(2,3,5)&6305&5&7\\
(3,3,6)&6305&5&7\\
(2,4,6)&6305&5&7
\end{array}
\]

The two new points move in independent tangential directions from the
original one.  Their complete cumulative family filtrations also agree:

\[
\operatorname{rank}R_0=(264,2021,3989,5117,5757,6117,6305),
\]

\[
n_1=(0,6,6,6,6,6,5),
\qquad
n_2=(0,0,0,0,0,0,7).
\]

The elimination representatives vary with the point, while these ranks do
not.  This is the behavior expected of a rank-seven object rather than of a
special numerical accident at \((2,3,5)\).

## Conclusion and boundary

The intrinsic exact-valuation object is tangentially rank-stable on the
tested generic triangle-wall samples:

\[
\boxed{\dim E_2(C_X)=7.}
\]

This is a sampled rank theorem, not yet a local-system theorem.  No canonical
comparison

\[
E_2(C_X)\longrightarrow E_2(C_{X+dX})
\]

or tangential Gauss--Manin operator has been constructed.  Consequently the
result does not yet identify this seven-plane with the known generic
rank-seven algebraic kernel.  The next typed calculation is to differentiate
the full relation presentation tangentially, derive the induced connection
on \(E_2\), and test its compatibility with occurrence transport and the
infinity-Gysin sequence.

## Durable artifacts

- `research/nima/export_triangle_wall_dual_rows.py`
- `research/nima/triangle-wall-dual-relation-rank.json`
- `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`
