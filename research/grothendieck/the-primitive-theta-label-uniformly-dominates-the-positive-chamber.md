# The Primitive Theta Label Uniformly Dominates the Positive Chamber

## Label ratio

On \(u\ge0\), the primitive profile is

\[
\phi_1(u)
=
2\pi e^{5u/2}
\left(2\pi e^{2u}-3\right)e^{-\pi e^{2u}}.
\]

The exact translate law is

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

Put \(y=e^{2u}\ge1\). Direct substitution gives

\[
R_n(y)
:=
\frac{\phi_n(u)}{\phi_1(u)}
=
n^2
\frac{2\pi n^2y-3}{2\pi y-3}
e^{-\pi(n^2-1)y}.
\]

For \(n\ge2\),

\[
\frac{d}{dy}\log R_n(y)
=
\frac{2\pi n^2}{2\pi n^2y-3}
-
\frac{2\pi}{2\pi y-3}
-
\pi(n^2-1).
\]

The first fraction is smaller than the second because

\[
\frac{a}{ay-3}=\frac1{y-3/a}
\]

decreases with \(a\). Hence

\[
R_n'(y)<0.
\]

Every higher-label ratio is maximal at the seam \(u=0\) and decreases
strictly into the positive chamber.

## Uniform tail bound

At \(y=1\),

\[
R_n(1)
<
3n^4e^{-3(n^2-1)}.
\]

For \(n=2+j\),

\[
n^2-1\ge3+5j,
\qquad
n^4\le16^{n-1}=16^{j+1}.
\]

Therefore

\[
\sum_{n\ge2}R_n(1)
<
48e^{-9}
\sum_{j\ge0}(16e^{-15})^j
<
0.006001.
\]

Since every \(R_n(y)\le R_n(1)\),

\[
\sum_{n\ge2}\phi_n(u)
<
0.006001\,\phi_1(u)
\qquad
(u\ge0).
\]

Thus the primitive label contributes more than \(99.4\%\) of the completed
positive-chamber source pointwise.

## What this enables

The finite-support collision problem now has a canonical decomposition:

\[
\Phi=\phi_1+\tau,
\qquad
0<\tau<0.006001\,\phi_1.
\]

A proof may first establish a quantitative transversality reserve for the
primitive polynomial--Gaussian transform and then compare the exact theta
tail against that reserve. No arbitrary label cutoff is involved.

The ratio becomes even smaller as \(u\) grows, so moving support endpoints do
not weaken pointwise primitive dominance.

## What this does not prove

Oscillatory integration is not order-preserving. A small positive pointwise
tail can dominate a primitive transform at a frequency where the primitive
value or tangent is already small.

Consequently the estimate does not exclude a double-zero collision by itself.
The required next theorem is relative:

- either a lower bound on the primitive value--tangent determinant in terms
  of a positive norm that also controls the tail;
- or a common high-frequency endpoint asymptotic proving that primitive and
  tail corrections have compatible orientation.

The absence of a uniform transform margin is the exact reason pointwise
dominance cannot be promoted directly to RH.

## Falsifier

The ratio theorem is falsified by one \(n\ge2\) and \(u\ge0\) with
\(R_n'(e^{2u})\ge0\), or by a tail ratio reaching \(0.006001\).

A proposed collision proof is falsified if it uses the pointwise inequality
as though the sine or cosine transform preserved it.
