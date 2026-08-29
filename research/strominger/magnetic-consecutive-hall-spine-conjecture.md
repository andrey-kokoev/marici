# Consecutive-depth Hall basis is a minus spine with a finite plus cap

Order ordinary columns semantically by increasing pole depth and, at each
depth, by minus branch before plus branch. Exact column elimination on the
native \(\beta=4\) matrices gives a stable normal form:

\[
\{(a,-):a\ge0\}
\quad\cup\quad
\{(a,+):a\in P_{g,q}\},
\]

where \(P_{g,q}\) is finite.

Across all 135 cases

\[
2\le g\le10,
\qquad
1\le q\le15,
\]

through cutoff \(N=20\):

- every minus column is a pivot;
- no minus column is omitted;
- the retained plus set below depth 16 is identical at cutoffs 15 and 20;
- all sufficiently deep plus columns are relations over the spine and cap.

For the separated regime visible in the audit, the largest retained plus
depth is

\[
\max P_{g,q}=q+3.
\]

The cap can contain internal holes at exceptional collision depths, so it is
not always the full interval \(0\le a\le q+3\). Those holes are primitive
column relations and must be retained as certificates rather than silently
discarded.

This supplies the candidate prequotient required by the adjoint cocircuit
lift:

\[
\text{all minus columns}
+
\text{finite plus cap}
\longrightarrow
\text{square tail block after boundary rows are reserved}.
\]

The conjecture is stronger than cutoff rank stabilization: it predicts a
source-labelled infinite spine and finite relation packet. An unbounded proof
should use the nonzero left endpoint of each new minus column to extend the
matching, then show that plus support lies in the already generated row span
after the cap boundary.

The next checker must replace elimination order by an explicit Hall row map
and verify its determinant. Until that map is derived, this remains a bounded
semantic-basis conjecture rather than a source-authorized functor.
