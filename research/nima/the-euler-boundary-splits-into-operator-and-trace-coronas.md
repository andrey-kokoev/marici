# The Euler Boundary Splits into Operator and Trace Coronas

## Normalized cutoff carriers

For the finite Euler packet, define

\[
H_X=\sum_{p\le X}\frac1p,
\qquad
\mu_{X,p}=\frac{1}{pH_X}.
\]

Let \(b_X=(\sqrt{\mu_{X,p}})_{p\le X}\), and form

\[
K_X=b_Xb_X^*,
\qquad
D_X=\operatorname{diag}(\mu_{X,p}).
\]

The Mellin conditional expectation satisfies

\[
\mathbb E_{\mathrm M}(K_X)=D_X.
\]

Both carriers have trace one at every cutoff.

## Operator norm sees coherence and loses diffuse mass

Since \(K_X\) is a rank-one projection,

\[
\lVert K_X\rVert_\infty=1.
\]

The diagonal carrier instead satisfies

\[
\lVert D_X\rVert_\infty
=
\frac{1}{2H_X}
\longrightarrow0.
\]

Therefore the operator-norm sequence corona retains the coherent seam class
\([K_X]\) but sends its fixed-point image \([D_X]\) to zero. The conditional
expectation descends, but its Euler image is trivial there.

This corona remembers coherent concentration and forgets diffuse trace mass.

## Trace norm retains both carriers

In trace norm,

\[
\lVert K_X\rVert_1
=
\lVert D_X\rVert_1
=1.
\]

Hence both define nonzero classes in the trace-norm sequence quotient. The
coordinatewise Mellin expectation remains contractive and maps the seam class
to the diagonal class.

The trace-norm quotient is naturally a nonunital ideal or module rather than
the unital operator algebra used by Mellin transports. The transports act as
bounded multipliers. This typing difference cannot be erased.

## The relationship residual also survives

Let

\[
R_X=K_X-D_X.
\]

Using \(K_X^2=K_X\) and
\(\operatorname{Tr}(K_XD_X)=\operatorname{Tr}(D_X^2)\),

\[
\lVert R_X\rVert_2^2
=
1-\sum_{p\le X}\mu_{X,p}^2.
\]

Because \(\sum_p p^{-2}<\infty\) while \(H_X\to\infty\),

\[
\sum_{p\le X}\mu_{X,p}^2\longrightarrow0,
\qquad
\lVert R_X\rVert_2\longrightarrow1.
\]

Thus the relationship sector does not disappear at infinity. Every fixed
matrix coefficient tends to zero, but the coherent residual retains unit
Hilbert--Schmidt scale.

## Categorical consequence

There is no single untyped corona object carrying all three desired
structures:

1. unital operator multiplication and Mellin conjugation;
2. diffuse diagonal trace mass;
3. the coherent off-diagonal residual.

The minimal architecture is a multiplier algebra acting on a trace-corona
module, together with the conditional expectation and trace readout. The
operator corona is a different quotient that detects coherent concentration
but annihilates the diffuse diagonal class.

This is the boundary version of the two-observer pattern:

- the operator observer detects relationship coherence;
- the trace observer detects distributed arithmetic mass;
- the conditional expectation is the directed comparison between them.

Any construction using only the scalar prime-harmonic state loses
\(R_X\). Any construction using only the operator corona loses \(D_X\).

## Finite falsifier

At every cutoff,

\[
\lVert K_X\rVert_\infty=1,
\qquad
\operatorname{Tr}D_X=1.
\]

Meanwhile \(\lVert D_X\rVert_\infty\) decreases and
\(\lVert R_X\rVert_2^2\) approaches one. A proposed single completion that
identifies either carrier with zero while claiming to preserve both operator
coherence and trace mass fails these simultaneous measurements.

