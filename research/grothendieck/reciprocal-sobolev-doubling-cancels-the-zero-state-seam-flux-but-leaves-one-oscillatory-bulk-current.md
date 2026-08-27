# Reciprocal Sobolev Doubling Cancels the Zero-State Seam Flux but Leaves One Oscillatory Bulk Current

## Reciprocal tails

Let `f` be the real positive theta forcing on the logarithmic half-line and
write `z=a+it`. Define the two source tails

\[
G_+(q)=\int_q^\infty f(v)e^{z(v-q)}\,dv,
\qquad
G_-(q)=\int_q^\infty f(v)e^{-z(v-q)}\,dv.
\]

They satisfy the source-derived reciprocal equations

\[
(\partial_q+z)G_+=-f,
\qquad
(-\partial_q+z)G_-=f.
\]

Both belong to the completed Sobolev boundary system because the theta source
decays superexponentially.

## Oriented Green identities

The two half-line orientations give

\[
-|G_+(0)|^2+2a\|G_+\|^2
=-2\Re\langle f,G_+\rangle,
\]

and

\[
|G_-(0)|^2+2a\|G_-\|^2
=2\Re\langle f,G_-\rangle.
\]

The completed scalar readout is

\[
X(z)=G_+(0)+G_-(0).
\]

Therefore a scalar zero imposes anti-diagonal seam data:

\[
G_-(0)=-G_+(0).
\]

In particular, the two oriented boundary norms cancel exactly. This is the
source-native reciprocal seam cancellation sought after the completion audit.

## The surviving bulk current

Adding the Green identities at a zero gives

\[
2a\left(\|G_+\|^2+\|G_-\|^2\right)
=
2\Re\langle f,G_--G_+\rangle.
\]

The right-hand side is not a boundary trace. Expanding before source
aggregation gives

\[
2\Re\langle f,G_--G_+\rangle
=
-4\int_{0<q<v}
f(q)f(v)\sinh(a(v-q))\cos(t(v-q))\,dq\,dv.
\]

Thus reciprocal Sobolev doubling removes the seam defect but leaves exactly
one oscillatory separation current. Positivity of `f` does not orient it,
because the cosine changes sign.

For `a=0` the current vanishes identically, as required by reciprocal
unitarity. Off the seam it factors by `a`, but the remaining quotient still
has an oscillatory kernel:

\[
\frac{\sinh(a d)}{a}\cos(td).
\]

This is the same obstruction previously seen in the Wronskian and curvature
coordinates, now derived from the fully completed reciprocal boundary system.

## Meaning

Three possible sources of failure have now been separated:

1. finite control closure fails but is repaired by Sobolev completion;
2. seam flux cancels automatically on a scalar zero-state;
3. one bulk reciprocal-difference current remains and contains all
   zero-confinement content.

No further boundary port can remove this current without changing the bulk
comparison. The next theorem must use theta's labelled arithmetic or modular
structure to orient the cosine-weighted separation integral. Treating it as a
missing endpoint term would be a type error.

## Smallest falsifier

For a generic positive forcing, select `a`, `t`, and two narrow separated
source packets so that their separation lies in a negative cosine band. This
changes the sign of the surviving current while preserving positivity and the
completed Sobolev typing. Hence any proposed sign law must distinguish the
actual theta label transport from arbitrary positive sources.

## Result

The reciprocal completed boundary systems are jointly faithful and their seam
fluxes cancel exactly at a scalar zero. The sole remaining analytic obstruction
is the source-labelled oscillatory bulk current
`2 Re <f,G_- - G_+>`. RH requires a theta-specific orientation law for this
current.

