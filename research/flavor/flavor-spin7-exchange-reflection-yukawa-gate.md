# Spin(7) Exchange-Reflection Fixes One Yukawa Ratio Conditionally

Work package: WP924

## Question

Can an exchange-reflection symmetry remove WP923's conjugate-channel Yukawa
ratio without fitting it?

## Candidate operation

Combine three actions:

1. exchange the two labelled parent spinors (8_a\leftrightarrow8_b);
2. reverse the Spin(2) charge;
3. reflect the two endpoints of the five-dimensional interval.

On the two complex zero-mode coefficients, the operation is

\[
E:(y_-,y_+)\longmapsto(y_+^*,y_-^*).
\]

The two WP922 target parity assignments are exchanged by this operation, so
the exact A zero-mode orbit is compatible with it.

## Exact fixed locus

Write (y_-=a+ib) and (y_+=c+id). The fixed equations have rank two and
give

\[
c=a,
\qquad
d=-b.
\]

Equivalently,

\[
y_+=y_-^*.
\]

The four-real-dimensional coefficient family collapses to a
two-real-dimensional fixed locus. In particular,

\[
\frac{|y_+|}{|y_-|}=1.
\]

This is a genuine conditional ratio selector and interaction rigidifier. The
common complex coefficient remains free, and no three-family spectral shape
or physical16 point is selected.

## Boundary hostile

The exchange must govern the complete boundary action, not only the displayed
operators. An endpoint-asymmetric localized counterterm changes the magnitude
pair from

\[
(m,m)
\]

to

\[
(m,m+\delta).
\]

For (m=\delta=1), the ratio returns to (2), exactly reproducing WP923's
smallest hostile. Thus a reflection of the bulk equations is insufficient if
the branes, regulator, anomaly inflow, or localized kinetic terms distinguish
the endpoints.

## Claim boundary

WP924 is an acceptance theorem for a new relational five-dimensional source
structure. It does not establish that endpoint exchange is already a symmetry
of the declared model. Deriving it requires a complete bulk-plus-boundary
action and proof that every allowed counterterm respects the operation.

Even if admitted, the result fixes one conjugate-channel ratio only. The next
Yukawa object is the full three-family tensor pair. The exchange-fixed tensor
locus and its RG stability must be computed before returning to the four
spectral-shape directions.

No physical instrument gate opens until the source relation survives RG and
threshold transport.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp924_spin7_exchange_reflection_yukawa_gate.py
~~~
