# Entry 496 — The Conormal Bockstein Vanishes at Both Endpoints

Entry 495 identifies the generic soft Bockstein with

\[
-{1\over2}[a^3e_u].
\]

Its endpoint behavior is controlled by the
\(e_a\wedge e_u\) Koszul boundary.  Writing \(c=1-b^2\), one has

\[
d(e_a\wedge e_u)=-ca^2e_a+4a^3e_u.
\]

Therefore the family relation in homology is

\[
\boxed{4[a^3e_u]=c[a^2e_a].}
\]

The Bockstein is consequently

\[
\beta(a^3)=-{c\over8}[a^2e_a].
\]

This expression is regular along the entire \(b\)-line; there is no pole or
residue.  But at either endpoint \(b=\pm1\), where \(c=0\),

\[
[a^3e_u]=0.
\]

Equivalently, at the endpoint

\[
d\left({1\over4}e_a\wedge e_u\right)=a^3e_u.
\]

Thus the generic conormal Bockstein becomes an ordinary Koszul boundary on
both endpoint fibers.

## Consequence

The global invariant defect of Entry 473 cannot be the ordinary endpoint
restriction of the generic conormal Bockstein.  The class extends regularly
but vanishes at the boundary.  Any globally retained endpoint datum must
therefore live in a nearby-cycle, relative-support, or derived-base-change
term that remembers the first normal derivative in \(c\).

The relevant normalized class is

\[
{\beta(a^3)\over c}=-{1\over8}[a^2e_a],
\]

which is regular before setting \(c=0\).  This is not an ordinary fiber
class; it is conormal to the endpoint divisor.

## Next gate

Base-change derivedly along \(c=1-b^2=0\), retaining the two-term endpoint
resolution \([\mathcal O\xrightarrow c\mathcal O]\).  Compute its connecting
class and test whether it is the single invariant defect of Entry 473.  A
rank other than one, or opposite signs at the two endpoint branches after
orientation is included, falsifies the identification.

The family relation and both endpoint specializations are checked by
`research/voevodsky/check_soft_axis_bockstein_endpoint.py`.
