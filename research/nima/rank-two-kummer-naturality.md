# The Rank-Two Kummer Line and Fifth Selector Transport Together

The invariant equations

\[
w^2+R=0,
\qquad
Nw=C_p
\]

pass the exact presentation-change audit.

## Ordered-basis reversal

Swapping the two plane generators \(a\leftrightarrow b\) reverses the normal
\(n=a\times b\). Describing the same loop point therefore sends

\[
n\mapsto-n,
\qquad
w\mapsto-w,
\qquad
N=p\cdot n\mapsto-N.
\]

Meanwhile \(R\) and \(C_p\) are invariant. Consequently both

\[
w^2=-R
\]

and the paired selector

\[
Nw=C_p
\]

are unchanged. The Kummer coordinate and normal coefficient each carry the
odd character; their algebraic incidence pairing is even.

## Ambient transport and scaling

Orientation-preserving orthogonal coordinate transport leaves every
invariant unchanged. Orientation reversal changes the signs of the
pseudovector normal and the corresponding Kummer coordinate, while preserving
their product. Under common scaling of all external and loop coordinates by
\(\lambda\),

\[
\Delta\mapsto\lambda^4\Delta,
\quad
R\mapsto\lambda^6R,
\quad
w\mapsto\lambda^3w,
\quad
N\mapsto\lambda^3N,
\quad
C_p\mapsto\lambda^6C_p.
\]

Thus the cover equation and selector are homogeneous of weight six.

This establishes a genuine naturality square on the rank-two stratum:

\[
\text{odd Kummer coefficient}\otimes
\text{odd normal incidence}
\longrightarrow
\text{even scalar selector}.
\]

It is structurally analogous to the paired-character cancellation already
seen in the five-point string reflection and radiative detector-memory
pairing, but no physical-current identification follows from this algebraic
naturality square alone. Benincasa's marked degree-32 cover remains the
authoritative physical coefficient object.

Artifacts:

- `research/nima/check_rank_two_kummer_naturality.py`
- `research/nima/results/rank-two-kummer-naturality.json`
