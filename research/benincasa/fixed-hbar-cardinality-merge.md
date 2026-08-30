# Fixed-hbar collective merge is associative when cardinality is retained

For a block of (N) labelled canonical occurrences define

\[
Q_N=\frac1{\sqrt N}\sum_{i=1}^Nq_i,
\qquad
P_N=\frac1{\sqrt N}\sum_{i=1}^Np_i.
\]

Then

\[
[Q_N,P_N]=i\hbar.
\]

Blocks of sizes (m,n) merge by

\[
Q_{m+n}
=
\sqrt{\frac m{m+n}}Q_m
+
\sqrt{\frac n{m+n}}Q_n,
\]

and identically for (P). Along any binary merge tree, the squared
coefficient of every leaf is

\[
\frac1N.
\]

Hence the normalized fixed-(\hbar) merge is associative once occurrence
cardinality is retained. The unweighted binary rule fails because it erases
that label.

The exact checker enumerates all 82,500 ordered binary bracketings through
twelve occurrences. Every occurrence count has one output coefficient vector,
and its squared weights sum to one.

This is a coefficient normalization over the occurrence-resolved carrier. It
does not require a new Cut cell or a second Planck primitive.

