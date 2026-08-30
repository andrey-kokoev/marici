# Local weighted confluence forces the magnetic offset four

The deformation audit found a family

\[
(1+t)^{-a}(1-xt)^{a-h}
\]

with identical pole-depth transport for every `h`.  That apparent modulus
arose because the generating function had forgotten the local fold engine.

Restore a connection strength `c` and a unit-increment weight sequence starting
at `w0`.  Before the step of weight `s`, the denominator power is `s-w0`.
For a numerator monomial with horizontal exponent `r`, direct clearing of the
denominator gives the two moves

\[
H:(r,t)\mapsto(r-1,t)\quad[r],
\]

\[
V:(r,t)\mapsto(r,t+1)
\quad[r+(c-1)s+w_0].
\]

Compare the two paths around one elementary diamond.  Horizontal then vertical
has weight

\[
r\,[r-1+(c-1)(s+1)+w_0],
\]

while vertical then horizontal has weight

\[
[r+(c-1)s+w_0],r.
\]

Their difference is

\[
\boxed{r(c-2)}.
\]

Thus endpoint weights depend only on the numbers of horizontal and vertical
moves, rather than their ordering, exactly when

\[
c=2.
\]

At this confluent value, if `j` vertical moves have already occurred, the next
vertical factor is

\[
2w_0-a+j.
\]

Consequently the offset in the rising factorial is not free:

\[
h=2w_0.
\]

The independently rigid fold weights begin at `w0=2`.  Therefore

\[
\boxed{h=4}.
\]

The full coefficient follows immediately:

\[
\binom gj(-1)^{g-j}
a^{\overline{g-j}}(4-a)^{\overline j}.
\]

This supplies the hard-to-vary explanation missing from the generating-function
audit.  Changing the connection strength destroys weighted confluence; changing
the weight start preserves confluence but changes the offset and is excluded by
the separate weight-rigidity theorem.  The value four is therefore the joint
invariant of connection confluence and the admitted weight origin, not a fitted
constant.

The checker proves the weighted-diamond and coefficient identities symbolically.
