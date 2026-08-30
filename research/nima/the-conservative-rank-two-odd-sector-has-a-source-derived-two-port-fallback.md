# The conservative rank-two odd sector has a source-derived two-port fallback

## Why the rank-one route may fail

Rank-one support requires the mixed block to factor through the oriented boundary of the two-chart cell. The source corpus states this as the desired first-order boundary architecture, but does not yet construct the relative boundary map.

Therefore the conservative local type remains

\[
\mathcal V_{\mathrm{odd}}
\subseteq
\operatorname{span}\{k_{\mathrm{wall}},k_{\mathrm{bulk}}\},
\]

where

\[
k_{\mathrm{wall}}=r_-\otimes s,
\qquad
k_{\mathrm{bulk}}=r_-\otimes a.
\]

The next question is whether the source already contains a faithful fallback observer for these two directions.

## Two independent source ports

It does, at the level of carrier types.

### Wall port

The symmetric face combination satisfies

\[
I+O=-1.
\]

It is carried by the constant–delta exchange plane. The wall coefficient therefore detects \(s\) and is invariant under face exchange.

### Oriented port

The antisymmetric face combination satisfies

\[
O-I=C,
\qquad
C'(u)=2e^{-\pi u^2}>0.
\]

Its orientation readout is carried by the tail–principal-value plane. For a half-line state \(h\), the Wronskian current is

\[
J(h)
=
-2\pi\operatorname{pv}
\int_{\mathbb R}\xi|\widehat h(\xi)|^2\,d\xi.
\]

It changes sign under orientation reversal while the wall amplitude does not.

Thus the wall coefficient and oriented Wronskian port transform in the two different face characters.

## Character-diagonal observer

Let \(\omega_s\) be the source wall readout and let \(\omega_a\) be the polarized Wronskian readout. Character covariance requires

\[
\omega_sP_a=0,
\qquad
\omega_aP_s=0.
\]

On the face basis \((s,a)\), the ideal observer matrix is therefore diagonal:

\[
J_{\mathrm{face}}
=
\begin{pmatrix}
\omega_s(s)&0\\
0&\omega_a(a)
\end{pmatrix}.
\]

The source formulas give a nonzero wall value because \(I+O=-1\), and a nonzero oriented density because \(C'(u)>0\). Hence the local carrier-level observer has rank two, provided the Wronskian quadratic form is polarized on the declared mixed operator domain.

This is a fallback theorem, not yet the Adams linking theorem.

## Sheet parity is a separate rank-two result

The Mellin position row supplies a different separation. For the reciprocal atoms

\[
s_L=\delta_L+\delta_{-L},
\qquad
j_L=\delta_L-\delta_{-L},
\]

the even theta test \(f\) and odd position test \(Qf\) give

\[
\begin{pmatrix}
\langle s_L,f\rangle&\langle j_L,f\rangle\\
\langle s_L,Qf\rangle&\langle j_L,Qf\rangle
\end{pmatrix}
=
\begin{pmatrix}
2f(L)&0\\
0&2Lf(L)
\end{pmatrix}.
\]

This matrix separates reciprocal sheet parity. It does not by itself separate the two face types inside the reciprocal-odd sector.

The complete local observer is therefore tensorial:

\[
J_{\mathrm{sheet}}\otimes J_{\mathrm{face}}.
\]

Restricting to sheet-odd incidence leaves the face observer \(J_{\mathrm{face}}\).

## What must be polarized

The wall coefficient is linear. The Wronskian readout is quadratic. To act on a mixed block, it must be polarized:

\[
\mathcal W(h_1,h_2)
=
\frac14
\sum_{\nu\in\{1,-1,i,-i\}}
\nu\,J(h_1+\nu h_2),
\]

with the convention adjusted to the chosen linear argument.

The source must prove that this polarized form is continuous on the same relative Green domain as \(B_{\alpha,p}\). Otherwise the oriented port exists only on diagonal states and cannot test mixed incidence.

## Finite faithfulness alternative

There are now two admissible finite routes.

### Selection route

Prove

\[
B_{\alpha,p}
=
L_Q\partial_{\mathscr C_p}L_P^*.
\]

Then only \(k_{\mathrm{bulk}}\) survives and one nonzero odd port suffices.

### Joint-observer route

Retain both face types and prove

\[
\det J_{\mathrm{face}}\ne0.
\]

This requires:

- nonzero wall normalization;
- nonzero polarized Wronskian normalization;
- exact character orthogonality;
- chart and reciprocal covariance.

## Completion margin

In the joint-observer route, the relevant margin is

\[
\sigma_{\min}(J_{\mathrm{face},X}(s)).
\]

A diagonal character decomposition reduces this to separate absolute lower bounds on the two calibrated diagonal entries, but only after proving cross-character terms vanish exactly.

## New frontier

Failure to construct rank-one boundary factorization does not force scalar blindness. The source already contains a natural rank-two fallback: constant–delta wall amplitude plus polarized Wronskian orientation.

The next exact calculation is to polarize the Wronskian current on the two-chart relative Green domain and verify the character-diagonal \(2\times2\) matrix. That either establishes conservative finite faithfulness or exposes a genuine invisible odd wall direction.
