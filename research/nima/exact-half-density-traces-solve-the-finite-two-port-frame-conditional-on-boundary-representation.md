# Exact half-density traces solve the finite two-port frame, conditional on boundary representation

## Existing normalized columns

The closed reciprocal half-density histories already carry the exact endpoint columns

\[
v_0=
\begin{pmatrix}
1/2\\
1/2
\end{pmatrix},
\qquad
v_1=
\begin{pmatrix}
1/4\\
-1/4
\end{pmatrix}.
\]

The first is reciprocal-even and the second reciprocal-odd. Their trace matrix is

\[
T=
\begin{pmatrix}
1/2&1/4\\
1/2&-1/4
\end{pmatrix}.
\]

Hence

\[
\det T=-\frac14,
\]

and, in the standard endpoint norm,

\[
T^{*}T
=
\begin{pmatrix}
1/2&0\\
0&1/8
\end{pmatrix}.
\]

The finite lower frame bound is therefore

\[
\sigma_{\min}(T)=\frac{1}{2\sqrt2}.
\]

It is independent of prime label because translated histories are isometric before Euler weighting.

## Consequence for the wall port

If \(v_0,v_1\) represent the symmetric and antisymmetric wall characters in the five-cell boundary quotient, then the wall part of the two-port observer is already uniformly faithful. Reciprocal symmetrization has not killed the odd wall character because the second column is retained as a separate typed trace.

The earlier search for a new one-sided wall functional was therefore too pessimistic. The existing two-history trace packet is already the stronger object.

## Tail port

The same closed history construction preserves the Wronskian normalization and exchanges causal with anti-causal orientation under reflection. A nonzero Wronskian row and its reciprocal transport separate the real tail plane \(\operatorname{span}\{K,V\}\), provided the representation identifies them with the \(K,V\) coefficient directions rather than only with their scalar compression.

Thus the finite numerical frame problem is solved on both blocks:

- wall block: exact lower bound \(1/(2\sqrt2)\);
- tail block: nonzero oriented Wronskian orbit, with its magnitude fixed by the source normalization.

## Remaining arrow

What is not yet proved is the representation theorem connecting these analytic history traces to the coefficient five-cell:

\[
\begin{array}{ccc}
\text{coefficient five-cell}
&\xrightarrow{\quad F\quad}&
\text{coefficient five-cell}\\
\downarrow\Pi&&\downarrow\Pi\\
\text{closed two-history boundary packet}
&\xrightarrow{\quad\mathcal F_{\mathrm{Tate}}\quad}&
\text{closed two-history boundary packet}.
\end{array}
\]

The map \(\Pi\) must satisfy:

1. \(1,\delta_0\) map to the exact even and odd endpoint columns with the frozen normalization;
2. \(K,V\) map to the causal and anti-causal Wronskian ports;
3. \(\Pi\) intertwines Fourier transport and reciprocal reflection;
4. \(\Pi\) is injective on the boundary quotient;
5. the quadratic lift of \(\Pi\) intertwines polarized Green currents;
6. all identities survive the valuation-labelled completion.

Without this theorem, matching dimensions and characters do not authorize identification.

## Hostiles

A representation may send the correct wall basis to \(v_0,v_1\) while mapping both \(K\) and \(V\) to one scalar Wronskian row. The endpoint determinant passes, but the tail plane loses rank.

Another representation may be linearly faithful while reversing the \(V\mapsto-K\) Fourier sign. Every norm bound survives, but reciprocal orientation is wrong.

A cutoff-dependent representation may be injective at every stage while its inverse norm diverges.

## Frontier

The finite observer margins need not be invented. They are already present in the exact half-density trace and Wronskian data. The earliest missing constructor is now:

> Prove that the coefficient five-cell is represented faithfully and Fourier-equivariantly by the closed reciprocal two-history boundary packet, including its polarized quadratic lift.

This is a representation/intertwining theorem, not a new positivity estimate.
