# Exact source reflection identifies the fundamental depth window

The source polynomial obeys the identity

\[
C_{\beta-a}^{(g)}(x)=(-1)^g x^g C_a^{(g)}(x^{-1}).
\]

It follows by reversing the summation index in

\[
C_a^{(g)}(x)=\sum_{j=0}^g\binom gj(-1)^{g-j}
 a^{\overline{g-j}}(\beta-a)^{\overline j}x^j.
\]

For the Laurent current

\[
K_a^{(g,q)}(x)
=2x^{-a-g}(x^{q+2}-1)(1+x)C_a^{(g)}(x),
\]

the induced reflection is

\[
K_{\beta-a}^{(g,q)}(x)
=(-1)^{g+1}x^{q+3-\beta-g}K_a^{(g,q)}(x^{-1}).
\]

The current identity was replayed exactly in 31,185 cases over
\(0\le\beta\le8\), \(2\le g\le12\), \(1\le q\le15\), and
\(-5\le a\le15\), with no failure. The algebraic derivation is unbounded.

This turns the empirical source window into geometry. The involution

\[
a\longmapsto\beta-a
\]

exchanges the two source atoms \(a=0\) and \(a=\beta\). The admitted half-line
\(a\ge0\) cuts its orbits, and

\[
0\le a<\beta
\]

is the fundamental boundary interval. Every tail depth \(a\ge\beta\) reflects
to a nonpositive depth.

The finite-window conjecture is therefore reduced to one missing descent
lemma: after reflection, every nonpositive-depth current must be congruent
modulo the ordinary path module to a combination supported on the fundamental
interval. Proving that lemma yields

\[
\operatorname{span}\{[K_a]:a\ge0\}
=
\operatorname{span}\{[K_0],\ldots,[K_{\beta-1}]\}
\]

without a cutoff census.

The two-wedge rank is then the Fitting rank of the reflection-boundary packet,
not a singularity of the invertible grade-germ transfer.
