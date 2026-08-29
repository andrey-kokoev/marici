# Nearest-neighbor sewing is controlled by a rank stratum

On the hostile consecutive-depth complex, let \(M_N\) contain the ordinary
columns of depths \(0,1,\ldots,N\). The first nearest-neighbor sewing
question is

\[
K_1\in\operatorname{im}(M_N,K_0).
\]

When it holds and the full current quotient has width one, there is a unique
cokernel scalar \(R_{g,q,0}\) satisfying

\[
[K_1]=R_{g,q,0}[K_0].
\]

The relation is intrinsic once it appears: exact coefficients remain unchanged
under further cutoff enlargement in the tested cases.

## Failed support conjecture

A natural first guess was that sewing begins at

\[
N=\max(g,q+4),
\]

after both the grade path and the upper collision window fit inside the
presentation.

This is false. In the exact census over \(2\le g\le10\) and
\(1\le q\le10\), 49 of 90 cases disagree. Some sew earlier and some later.
For example,

\[
(g,q)=(2,1)
\]

sews at \(N=4\), one step earlier than predicted, while

\[
(g,q)=(5,3)
\]

sews at \(N=9\), two steps later.

Therefore support closure is necessary background but not the controlling
invariant.

## Correct invariant

The sewing threshold is the first \(N\) at which the augmented rank stops
increasing:

\[
\operatorname{rank}[M_N\mid K_0\mid K_1]
=
\operatorname{rank}[M_N\mid K_0].
\]

This is a Fitting-stratum event. Width-one and width-two regions are separated
by vanishing maximal minors of the augmented current packet, not solely by
endpoint overlap.

The next proof target should isolate the finite local minor whose
nonvanishing produces this rank equality. Factoring that minor should yield
the recurrence coefficient and classify delayed or failed sewing in one step.

Replay with: python research/strominger/checkers/magnetic_nearest_neighbor_sewing_checks.py
