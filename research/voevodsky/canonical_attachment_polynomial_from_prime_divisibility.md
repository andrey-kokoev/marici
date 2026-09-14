# The canonical attachment polynomial follows from prime divisibility

## Question

Why do canonical cube grades produce the attachment polynomials

\[
A_n(x)=(1+x)^{n-2}(1+x+x^2),
\]

and do the relative boundary ranks continue to equal the preceding attachment vector?

## Claim boundary

For every \(n\geq3\), unique factorization gives the exact number of distinct-shell cells born at the canonical grade \(L_n\). Relative boundary ranks and acyclicity are computed through dimension ten over two prime fields. A general chain contraction remains to be written before promoting the rank recurrence to an all-dimensional theorem.

## Divisibility classification

At

\[
L_n=p_2p_3\cdots p_{n-1}p_n^2p_{n+1},
\]

an \(r\)-cell with shell set \(I\) is born exactly when

\[
L(I)=p_{\max I}\prod_{i\in I}p_{i+1}
\]

divides \(L_n\). Unique factorization forces \(I\subseteq\{1,\ldots,n\}\) and \(\max I\geq2\).

Write \(m=\max I\). If \(m<n\), then \(m-1\notin I\), because its inclusion would make \(p_m^2\mid L(I)\), while \(p_m\) occurs only once in \(L_n\). If \(m=n\), every subset of the first \(n-1\) directions is allowed because \(p_n^2\mid L_n\).

Therefore

\[
\Delta c_r(L_n)
=
\sum_{m=2}^{n-1}
\binom{m-2}{r-1}
+
\binom{n-1}{r-1}.
\]

The hockey-stick and Pascal identities give

\[
\Delta c_r(L_n)
=
\binom{n-2}{r}
+
\binom{n-2}{r-1}
+
\binom{n-2}{r-2}.
\]

Hence the positive-degree counts, together with the unique new vertex, are the coefficients of

\[
A_n(x)=(1+x)^{n-2}(1+x+x^2).
\]

In particular,

\[
A_{n+1}(x)=(1+x)A_n(x).
\]

## Relative rank recurrence

The computations at dimensions three through six give

\[
\operatorname{rank}\bar d_r^{(n)}
=[x^{r-1}]A_{n-1}(x).
\]

If this continues, then

\[
\dim C_r^{(n)}
=
\operatorname{rank}\bar d_r^{(n)}
+
\operatorname{rank}\bar d_{r+1}^{(n)},
\]

so every relative homology group vanishes. This is the chain-level form of recursive interval thickening.

## Path increment

The number of maximal directed paths born at \(L_n\) is

\[
\Delta R(L_n)
=
\sum_{r=1}^{n}r!\,[x^r]A_n(x).
\]

This is computable directly from \(n\), without primes or graph construction once the canonical grade is known.

## Strongest falsification attempt

For dimensions three through ten, construct every exact-grade cell from \(L(I)\mid L_n\), derive relative faces from actual cell bases, and independently compute boundary ranks over two large prime fields. Compare cell vectors with \(A_n\), rank vectors with \(A_{n-1}\), verify boundary compositions, and require all relative Betti numbers to vanish. Record path increments for future pyramid allocation.

## Computed recurrence

Exact relative complexes through dimension ten match the attachment polynomial, the preceding-vector boundary ranks, and vanishing relative homology over both tested prime fields. At dimension seven the cell vector is

\[
(1,6,16,25,25,16,6,1),
\]

its boundary-rank vector is the six-dimensional attachment vector, and it contributes 12068 maximal paths. At dimension ten the corresponding path increment is 8987291.

## Disposition

The attachment-count formula is proved by prime divisibility. The relative-rank recurrence and acyclicity now survive exact tests through dimension ten. An all-dimensional chain contraction remains the proof obligation.
