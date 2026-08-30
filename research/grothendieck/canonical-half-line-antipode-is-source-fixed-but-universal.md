# Canonical half-line antipode is source-fixed but universal

## Bounded question

Is the forbidden projective value \(-1\) merely a gauge artifact, or does the
completed theta source select a canonical equal-coefficient route frame?

## Source-derived route resolution

Let \(\Phi\) be the even completed source and define

\[
H(z)=\int_0^\infty\Phi(u)e^{zu}\,du.
\]

Super-exponential source decay makes \(H\) entire. Splitting the fixed real
contour at the modular seam \(u=0\) gives the two canonical route amplitudes

\[
r_+(z)=H(z),
\qquad
r_-(z)=H(-z).
\]

The full transform is reconstructed by ordinary contour addition:

\[
X(z)=r_+(z)+r_-(z).
\]

Thus the source-derived readout covector in this frame is

\[
c=(1,1).
\]

No coefficient is fitted from the zeros. The equal-coefficient frame is fixed
by the two half-contours and their common orientation.

## Invariant incidence and canonical chart

Under a route-basis change \(r\mapsto Dr\), the covector changes as
\(c\mapsto cD^{-1}\). The invariant zero condition is

\[
c,r=0.
\]

In the source-selected half-line frame, this becomes

\[
\frac{r_+(z)}{r_-(z)}=-1
\]

whenever \(r_-(z)\ne0\). Therefore the antipode is a legitimate canonical
coordinate for this particular decomposition, although it is not invariant
without the covector.

## Reciprocity supplied by evenness

The route state obeys

\[
r_-(z)=r_+(-z).
\]

On the imaginary axis,

\[
r_-(ib)=\overline{r_+(ib)}.
\]

Hence real-axis transform zeros are exactly antipodal route incidences on the
seam. Off the seam, reciprocal exchange persists but conjugacy does not.

## Universal no-go

The same construction applies to every even super-exponentially decaying
source, including the exact hostile carrier

\[
g_{\varepsilon,k}(u)
=
e^{-u^2}[1+\varepsilon\cos(ku)].
\]

Its two half-line routes have the same canonical covector \((1,1)\), the same
reciprocal exchange, and the same conjugacy on the seam. Nevertheless, its
full transform has explicit off-axis zeros. At those zeros, its canonical
route ratio reaches \(-1\) off the seam.

Therefore canonical half-line resolution and source-fixed antipodal typing do
not exclude the forbidden incidence.

## Result

Two apparent alternatives are now separated:

1. The antipode is not merely a coordinate artifact for the theta half-line
   decomposition; the source fixes the equal-weight frame.
2. That fixed frame and its reciprocal symmetry are universal and carry no
   RH force by themselves.

The missing theorem cannot live solely on the aggregated half-line packet. It
must retain structure that the modulated Gaussian lacks before its shifted
frequency components are summed.

## Labelled refinement target

For theta, write

\[
H(z)=\sum_{n\ge1}H_n(z)
\]

with the arithmetic scale labels retained. The next admissible object is the
labelled route packet

\[
r^{\mathrm{lab}}(z)
=
\left(
(H_n(z))_{n\ge1},
(H_n(-z))_{n\ge1}
\right),
\]

together with the source aggregation covector. The required theorem must
exclude incidence with the covector kernel by a labelled modular relation
that fails for the two shifted Gaussian frequency labels.

## Circularity boundary

A connection defined from \(H'/H\), from the ratio of the final scalar to one
route, or from division by \(X\) is not accepted. The transport must be
derived labelwise before applying either the label-sum or the half-line
readout.
