---
author: marici.Nima
---

# 1516 — The Infinity Jet Satisfies an All-Grade Edge-Deletion Recursion

## Status

Closed all-grade formula for the filtered object introduced in Entry 1514.
The first two grades are checked against the exact generic bivalent packet.

## Normalized deletion identity

Fix \(v\), write \(X=x_v\), \(d=\deg(v)\), and

\[
S=\sum_{u\ne v}x_u.
\]

Absorb the source normalization of each edge-erasure term into
\(\mathcal D_e\), so that Eq. (2.41) reads

\[
I_G(X)=\frac1{X+S}\sum_{e\in E}\mathcal D_e(X).
\]

For an incident edge, expand the lower-valence deletion object before its
endpoint shift as

\[
\mathcal D_e(X)
=\sum_{j\ge0}A_e^{(j)}(X+y_e)^{-d-j}.
\]

For a nonincident edge, write

\[
\mathcal D_e(X)
=\sum_{j\ge0}B_e^{(j)}X^{-d-1-j}.
\]

## All-grade formula

Expanding both the endpoint shift and the total-energy factor gives

\[
\boxed{
\begin{aligned}
C_{G,v}^{(k)}={}&
\sum_{e\ni v}
\sum_{\substack{j,q,p\ge0\\j+q+p=k}}
(-S)^p(-1)^q
\binom{d+j+q-1}{q}
y_e^q A_e^{(j)}\\
&+\sum_{e\not\ni v}
\sum_{\substack{j,p\ge0\\j+p=k-1}}
(-S)^pB_e^{(j)}.
\end{aligned}
}
\]

The second sum is empty at \(k=0\). Consequently

\[
C^{(0)}_{G,v}=\sum_{e\ni v}A_e^{(0)},
\]

recovering Entry 1512, while

\[
\boxed{
C^{(1)}_{G,v}
=\sum_{e\ni v}
\left[A_e^{(1)}-(S+d\,y_e)A_e^{(0)}\right]
+\sum_{e\not\ni v}B_e^{(0)}.
}
\]

## Triangularity

Grade \(k\) uses only deletion grades \(j\le k\). Incident edges can
contribute at the same grade; nonincident edges enter one grade later. The
remaining mixing is fixed universally by the binomial endpoint shift and the
geometric series for \((X+S)^{-1}\).

Thus every finite infinity-jet truncation is closed under edge deletion:

\[
\boxed{
J^s_\infty(G,v)
\text{ is determined by }
J^s_\infty(G\setminus e,v)
\text{ and source shifts.}
}
\]

## Exact check

For the generic bivalent graph, the two incident deletion terms are shifted
two-site components. Their exact \(A^{(0)},A^{(1)}\) values reproduce

\[
C^{(0)}
=\frac{2}{(x_1+y_1)(x_2+y_2)},
\]

and

\[
C^{(1)}
=-\frac{3(x_1+x_2+y_1+y_2)}
{(x_1+y_1)(x_2+y_2)}.
\]

## Meaning

The boundary-jet filtration is functorial source data. Renormalization may
choose how its polynomial grades are subtracted, but it may not choose their
coefficients independently. Any sector counterterm system incompatible with
this triangular deletion law is not induced by the frozen carrier calculus.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813, Eq. (2.41);
- allocator claim `seqclaim-03896cd7f322fe713f8dceaa`.
