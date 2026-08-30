# Raw support peeling does not produce the local collision core

The local parity minors in `magnetic-low-grade-core.md` suggested that every
low-grade initialization block might reduce to width two or three by deleting
forced support leaves.  This is false.

The smallest counterexample is

\[
(g,d)=(2,6),
\qquad q=8.
\]

After every available noncore degree-one observation is removed, the columns

\[
(0,-),(4,+),(6,+)
\]

remain.  The desired even collision minor uses only `(0,-),(6,+)`, so the
extra `(4,+)` column cannot be removed by a forced support pivot.

For larger excess, the stalled plus-chain grows.  Hence

\[
\boxed{
\text{full initialization}
\not\xrightarrow{\text{raw leaf peeling}}
\text{fixed parity core}.
}
\]

This does not invalidate the symbolic local determinants or their arithmetic
classification.  It changes the missing theorem: one must construct an
oriented weighted elimination of the plus-chain and prove that its Schur
response is exactly the classified `2x2` or `3x3` collision coordinate.

The situation mirrors the stable transport result.  Support supplies a
finite-width chain, while source-derived coefficient identities collapse its
determinant response.  Hall support alone cannot perform that collapse.
