# Raw endpoint Gram equivalence is impossible; the Pauli dilation is the correct quadratic target

## Asymptotic obstruction

The raw Stieltjes endpoint Gram is

\[
G_p^{\mathrm{win}}
=
\begin{pmatrix}
a_p&z_p\\
\bar z_p&b_p
\end{pmatrix},
\]

where

\[
W_{\log p}\to-\mathbf1,
\qquad
W_{2\log p}\to-\mathbf1
\]

in \(L^2(\nu)\). Hence

\[
G_p^{\mathrm{win}}
\longrightarrow
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\]

and

\[
\det G_p^{\mathrm{win}}\to0.
\]

Every finite prime cell is positive, but the disagreement singular value
collapses.

## No uniformly bi-bounded raw equivalence

Let \(G_p^\theta\) be a completed theta endpoint Gram with a uniform positive
lower bound. Suppose there were maps \(T_p\) satisfying

\[
T_p^*G_p^\theta T_p=G_p^{\mathrm{win}}
\]

and

\[
\sup_p\|T_p\|<\infty,
\qquad
\sup_p\|T_p^{-1}\|<\infty.
\]

Uniform coercivity of \(G_p^\theta\) and uniform invertibility of \(T_p\)
would imply a uniform lower bound for \(G_p^{\mathrm{win}}\), contradicting
its collapsing determinant.

Therefore the quadratic comparison cannot be a uniformly bi-bounded
equivalence of the raw two-vector endpoint planes.

## Pauli dilation

Retain the two typed Euler ports

\[
X=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
Y=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
\]

For the Stieltjes lift \(J_p\), define

\[
\mathcal O_pv
=
\begin{pmatrix}
J_pXv\\
J_pYv
\end{pmatrix}.
\]

Then

\[
\mathcal O_p^*\mathcal O_p
=
XG_p^{\mathrm{win}}X
+
YG_p^{\mathrm{win}}Y
=
2
\begin{pmatrix}
b_p&0\\
0&a_p
\end{pmatrix}.
\]

The collapsing cross-correlation \(z_p\) cancels exactly.

Since

\[
a_p,b_p\ge m_\nu^2,
\]

the dilated observer has the uniform lower bound

\[
\mathcal O_p^*\mathcal O_p
\ge
2m_\nu^2I.
\]

Thus the correct completed comparison target is the two-output Pauli dilation,
not the raw endpoint Gram.

## Correct quadratic square

Let \(Q_p^{\mathrm{lin}}\) be the fixed wall/odd/tail linear constructor.
The required theorem is a typed isometry or uniformly equivalent embedding

\[
\widetilde Q_p:
\operatorname{ran}\mathcal O_p
\longrightarrow
\mathcal H_{\theta,+}\oplus\mathcal H_{\theta,-}
\]

such that

\[
\langle\mathcal O_px,\mathcal O_py\rangle
=
\left\langle
\widetilde Q_p\mathcal O_px,\,
\widetilde Q_p\mathcal O_py
\right\rangle_{\theta}
\]

or a source-derived uniformly equivalent form comparison.

This square retains the two Pauli outputs separately. Merging them before the
comparison can restore destructive cross-cancellation.

## Four matrix units, retyped

The four endpoint matrix units remain the correct finite polarization test,
but they must be evaluated after Pauli dilation:

\[
X|e_j\rangle\langle e_k|X
+
Y|e_j\rangle\langle e_k|Y.
\]

Their sum removes the raw off-diagonal correlation from the observer norm,
while their separate typed images still retain reciprocal orientation.

Therefore:

- the summed frame proves uniform observability;
- the separate polarized outputs prove constructor identity;
- neither may replace the other.

## Soft disagreement is not deleted

The Pauli dilation does not claim that the raw disagreement vector has
uniform norm. It routes the two arithmetic coordinates through two typed
outputs whose total energy depends only on the endpoint norms.

The physical soft disagreement remains trace class after Euler weighting and
can enter the Schur return. It is not inverted in the raw endpoint metric.

This is the legitimate third repair from the raw-area audit: suppress and
transport the soft direction globally before any inverse is formed.

## Completion theorem

A sufficient package is:

1. primewise Pauli-dilated polarization identity;
2. preservation of both output types through the completed theta carrier;
3. uniform endpoint bounds \(a_p,b_p\ge m_\nu^2\);
4. prime diagonality of the comparison;
5. Euler-weighted trace-class completion of the disagreement return;
6. no terminal mixed cancellation.

No uniform lower bound on

\[
\det G_p^{\mathrm{win}}
\]

is required or possible.

## Hostiles

1. Demand uniform equivalence of raw endpoint Grams.
2. Renormalize by
   \(\|W_{2L}-W_L\|^{-1}\) without source authority.
3. Sum the \(X\) and \(Y\) outputs before the terminal evaluator.
4. Use the Pauli frame bound to claim the raw disagreement is nonsoft.
5. Form \(G_p^{-1}\) before Euler-weighted completion.
6. Preserve total Pauli energy while swapping the reciprocal odd output.

## Verdict

The raw endpoint-area collapse is a genuine obstruction to the previously
suggested uniform Gram equivalence. It does not obstruct the typed Adams
constructor.

The source already supplies the correct repair: a two-output Pauli dilation
whose frame operator cancels endpoint cross-correlation exactly. The remaining
quadratic theorem must compare this dilated polarized observer, not the raw
two-vector endpoint plane, with the completed theta-history Green carrier.
