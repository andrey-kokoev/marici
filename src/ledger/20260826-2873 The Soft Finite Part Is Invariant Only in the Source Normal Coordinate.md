# 2873 — The Soft Finite Part Is Invariant Only in the Source Normal Coordinate

## Frozen finite part

After the moving-fiber pushforward of Entry 2871, write

\[
I(t)=\frac{L}{t}+O(1),
\qquad
P(t)=\int_2^t I(s)\,ds.
\]

The pointed soft finite part is

\[
\operatorname{FP}_t(P)
=
\lim_{t\to0}
\left[P(t)-L\log\!\left(\frac{t}{2}\right)\right].
\]

Here \(t=q_{g1}/X_1\) is the source-normalized polar coordinate.

## Hostile coordinate change

Let an endpoint-preserving reparametrization satisfy

\[
\phi(t)=ct+O(t^2),
\qquad
\phi(0)=0,
\qquad
\phi(2)=2.
\]

Then

\[
\log\!\left(\frac{\phi(t)}2\right)
=
\log\!\left(\frac t2\right)+\log c+o(1),
\]

and therefore

\[
\operatorname{FP}_{\phi}(P)
=
\operatorname{FP}_t(P)-L\log c.
\]

Endpoint preservation alone does not make the finite part invariant.

## Source-admissible regulator class

The frozen boundary-value prescription transports the same
\(q_{g1}\)-germ inside the convex negative-imaginary tube. The denominator
normalization fixes \(dq_{g1}\), hence fixes the first normal coordinate:

\[
c=1.
\]

For this source-admissible class the shift vanishes. Regulator invariance is
therefore established precisely for first-normal-preserving deformations, not
for arbitrary changes that merely fix the two endpoints.

## Narrow result

The pushed-forward finite part is source-canonical once the labelled polar
coordinate is retained. Forgetting that first-normal normalization turns it
into an affine logarithmic torsor with translation \(-L\log c\).

No new carrier datum is required. The normalization belongs to the existing
source-labelled normal geometry.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_regulator_invariance.py`
- `research/benincasa/soft-endpoint-regulator-invariance.json`

