# The source window history and resolved window vector have uniformly equivalent labelwise scale

## Operator-valued source history

For \(L=\log p\), consider

\[
\mathcal H_L:t\longmapsto M_{W_t},
\qquad t\in[L,2L],
\]

with the operator-valued graph norm

\[
\|\mathcal H_L\|_{G,\mathrm{op}}^2
:=\int_L^{2L}
\left(
\|M_{W_t}\|_{\mathrm{op}}^2+
\|M_{\partial_tW_t}\|_{\mathrm{op}}^2
\right)dt.
\]

The established upper bounds

\[
\|M_{W_t}\|_{\mathrm{op}}\le1,
\qquad
\|M_{\partial_tW_t}\|_{\mathrm{op}}\le2
\]

give

\[
\|\mathcal H_L\|_{G,\mathrm{op}}^2\le5L.
\]

## Uniform source lower bound

At \(q=0\),

\[
|W_t(0)|
=|H(t)-H(-t)|
=1-2H(t).
\]

This is increasing for \(t>0\).  Since \(t\ge L\ge\log2\),

\[
\|M_{W_t}\|_{\mathrm{op}}
=\|W_t\|_\infty
\ge |W_t(0)|
\ge m_0,
\]

where

\[
m_0:=1-2H(\log2)>0.
\]

Therefore

\[
{
m_0^2L
\le
\|\mathcal H_L\|_{G,\mathrm{op}}^2
\le5L.
}
\]

The source history graph has exactly linear squared scale in \(L\), uniformly
for every prime.

## Resolved endpoint-vector scale

The ordinary endpoint window satisfies

\[
\|W_L\|_2^2
=2\bigl(R(2L)-R(0)\bigr).
\]

Because this function is continuous and positive on
\([\log2,\infty)\), and is asymptotic to \(2L\), there exist constants
\(c_W,C_W>0\) such that

\[
c_WL\le\|W_L\|_2^2\le C_WL
\qquad(L\ge\log2).
\]

The selected resolved form obeys

\[
(1+M_\Phi^2)\|W_L\|_2^2
\le
\|W_L\|_{\mathrm{res}}^2
\le
(1+5M_\Phi^2)\|W_L\|_2^2.
\]

Hence there are constants \(c_R,C_R>0\) with

\[
{
c_RL
\le
\|W_L\|_{\mathrm{res}}^2
\le
C_RL.
}
\]

## Uniform labelwise metric comparison

Combining the source and resolved estimates gives constants \(A,B>0\),
independent of \(p\), such that

\[
{
A\,\|\mathcal H_L\|_{G,\mathrm{op}}
\le
\|W_L\|_{\mathrm{res}}
\le
B\,\|\mathcal H_L\|_{G,\mathrm{op}}.
}
\]

The same argument applies to a grade-\(k\) cell after replacing
\(L\) by \(kL\).  Thus the source operator-history metric and resolved
window-vector metric have the same source-authorized \(\sqrt{kL}\) scale on
every labelled one-dimensional endpoint fiber.

## What this closes

This proves the missing two-sided **labelwise scale comparison**.  In
particular, no additional prime-dependent scalar normalization is required to
pass from the source window-history graph to one resolved endpoint-window
line.

## What remains

A two-column first-Adams cell contains \(W_L\) and \(W_{2L}\) simultaneously.
To identify its full polarized metric, one must strengthen the scalar estimate
to a matrix inequality comparing:

- the source history/trace Gram on the endpoint pair;
- the resolved two-window Gram, including the explicit mixed tail \(g_p\).

Matching the norms of the two individual columns does not determine their
mixed pairing.  The ordered linking form and cut-atom wall ports must then be
added on the same two-column graph.

Thus the earliest local gate is now a uniform two-by-two metric comparison,
not discovery of the logarithmic scale.  Radical descent and global rigged
closed range remain open.  No RH conclusion is authorized.
