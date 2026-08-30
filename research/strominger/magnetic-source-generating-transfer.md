# The magnetic source polynomial is a grade-coupled transfer germ

Define

\[
C_a^{(g)}(x)=\sum_{j=0}^g\binom gj(-1)^{g-j}
 a^{\overline{g-j}}(\beta-a)^{\overline j}x^j.
\]

Its exact generating representation is

\[
\frac{C_a^{(g)}(x)}{g!}
=[t^g](1+t)^{-a}(1-xt)^{a-\beta}.
\]

Therefore increasing pole depth by one acts on the complete grade germ by

\[
F_{a+1}(t,x)=\frac{1-xt}{1+t}F_a(t,x).
\]

Coefficient extraction gives the local cross-grade law

\[
C_{a+1}^{(g)}+gC_{a+1}^{(g-1)}
=C_a^{(g)}-gxC_a^{(g-1)}.
\]

This identifies the hidden state in the fixed-grade transfer calculations:
the apparent finite memory at grade \(g\) is the omitted grade-\(g-1\)
coefficient of a genuinely memory-zero generating-germ evolution.

For the ordinary path polynomial,

\[
P_{a,m}^{(g)}(x)
=(1+x)(m+x\partial_x)C_a^{(g)}(x)-gxC_a^{(g)}(x),
\]

while the current insertion at separation \(Q=q+2\) is

\[
K_a^{(g)}(x)=2(x^Q-1)(1+x)C_a^{(g)}(x).
\]

Thus the current is a finite-difference boundary of the same source germ,
and the ordinary columns are its Euler-derivative observations. Their Fitting
strata must be computed after grade truncation; they are not intrinsic zeros
of the untruncated transfer multiplier.

This explains three earlier observations at once:

- support evolution has finite memory while selected determinants obey scalar
  transport;
- changing \(\beta\) moves the wedge boundaries because it changes the initial
  germ, not the transfer multiplier;
- parity decimation breaks the two-wedge law because it replaces the primitive
  one-step transfer by a coarser, information-losing observation.

The next exact target is to retain the pair
\((C^{(g)},C^{(g-1)})\), derive the induced two-state presentation for
\([M\mid K_0\mid K_1]\), and compute its determinant before eliminating the
lower-grade state.