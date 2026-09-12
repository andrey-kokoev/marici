# The four-prime two-cochain completes boundedly on the actual logarithmic half-line

## Actual source lengths

Let

\[
a_p=\log p
\]

and work on

\[
\mathcal H=L^2(\mathbb R_+).
\]

Define

\[
(R_pf)(x)=f(x+a_p)
\]

and

\[
(S_pf)(x)=
\begin{cases}
0,&x<a_p,\\
f(x-a_p),&x\ge a_p.
\end{cases}
\]

Then \(S_p=R_p^*\), both operators have norm one, and

\[
R_pS_p=I,
\qquad
S_pR_p=I-P_p,
\qquad
P_p=1_{[0,a_p)}.
\]

No discretization of \(\log p\) is needed for these identities.

## Exact mixed residual

For ordered primes \((q,p)\), set

\[
K_{q,p}=R_qS_p-S_pR_q.
\]

Writing \(a=a_p\), \(b=a_q\), one has exactly

\[
K_{q,p}=
\begin{cases}
P_aR_{b-a},&b>a,\\
1_{[a-b,a)}S_{a-b},&a>b.
\end{cases}
\]

Thus \(K_{q,p}\) is a norm-one partial isometry supported at the physical left boundary. In particular,

\[
\lVert K_{q,p}\rVert=1.
\]

The oriented two-cochain

\[
\mathcal F_{pq}=K_{q,p}-K_{p,q}
\]

therefore extends boundedly to \(\mathcal H\), with

\[
\lVert\mathcal F_{pq}\rVert\le2.
\]

## Bianchi identity

Translations commute:

\[
R_pR_q=R_qR_p.
\]

Expanding the Jacobi identity for commutators consequently gives, for distinct \(p,q,r\),

\[
[R_p,\mathcal F_{qr}]
+[R_q,\mathcal F_{rp}]
+[R_r,\mathcal F_{pq}]
=0.
\]

Hence the finite-prime two-cochain is covariantly closed on the actual logarithmic half-line.

## Four-cup bound

For four ordered primes define

\[
\mathcal Q_{pqrs}
=
\{\mathcal F_{pq},\mathcal F_{rs}\}
-
\{\mathcal F_{pr},\mathcal F_{qs}\}
+
\{\mathcal F_{ps},\mathcal F_{qr}\}.
\]

Since \(\|\{A,B\}\|\le2\|A\|\|B\|\),

\[
\boxed{
\lVert\mathcal Q_{pqrs}\rVert\le24.
}
\]

Thus every finite four-prime cell has an actual, bounded, non-discretized \(P^4\) operator on \(L^2(\mathbb R_+)\).

## Projective coefficient continuity

Let a finitely supported two-cochain carry typed coefficients \(u_{pq}\), and define

\[
q_\delta(u)=\sum_{p<q}e^{\delta(a_p+a_q)}|u_{pq}|.
\]

The operator-valued cup convolution obeys

\[
q_\delta(u\smile v)
\le
2q_\delta(u)q_\delta(v),
\]

because logarithmic lengths add and the operator anticommutator contributes at most the factor two. Therefore the cup product extends continuously to the projective exponential completion

\[
\bigcap_{\delta>0}\ell^1
\left(\binom{\mathbb P}{2},e^{\delta(a_p+a_q)}\right).
\]

The all-prime four-cup is consequently continuous whenever its two-cochain coefficients belong to this source test algebra. This is a topology theorem, not a claim that the unweighted family \(u_{pq}=1\) belongs to it.

## The remaining graph-domain obstruction

The \(L^2\) completion does not automatically extend to the derivative graph used by boundary jets.

The right shift \(S_p\) creates a jump at \(x=a_p\) unless the source trace satisfies \(f(0)=0\). Conversely, the left shift has

\[
(R_pf)(0)=f(a_p),
\]

so it does not preserve the zero-trace condition. Therefore the ordinary Sobolev domains \(H^1\) and \(H^1_0\) do not provide a common invariant domain for all \(R_p,S_p\).

This is not a failure of the four-cup. It identifies its correct analytic type:

\[
\boxed{
\mathcal Q_4\text{ is bounded at the }L^2\text{ rung but requires a broken-Sobolev or distributional graph domain for jet readout.}
}
\]

A suitable graph must retain the jump traces at every logarithmic seam rather than demand that the shifts erase them.

## Result

The finite construction survives replacement of integer proxies by the actual logarithmic prime lengths, and its cup product is continuous on the projective exponential coefficient algebra. The next constructor is a common broken graph domain containing the seam-jump channels and carrying a dual-valued Green identity.
