# Zero Confinement Is Not Stable under Positive Even Convolution

The positive even packet

\[
\nu=\frac25\delta_{-1}+\delta_0+\frac25\delta_1
\]

has bilateral Laplace transform

\[
L_\nu(z)=1+\frac45\cosh z.
\]

It vanishes at `z=plus-or-minus log(2)+(2k+1)pi i`. For every positive even
source `mu`, convolution preserves positivity and reciprocal symmetry but
multiplies transforms:

\[
L_{\mu*\nu}=L_\mu L_\nu.
\]

Thus it inserts this off-seam divisor into any source transform. Smoothness
and Schwartz decay are also preserved when the original source has them.

Consequently zero confinement is not a monoidal property of positive even
sources. Any RH-bearing constructor category must reject arbitrary positive
convolution factors through source provenance, or expose them through a
connected/logarithmic primitive before scalar aggregation.

Research packet:
`research/grothendieck/zero-confinement-is-not-stable-under-positive-even-convolution.md`

Exact checker:
`research/grothendieck/checkers/check_positive_even_convolution_divisor_hostile.py`

The checker passes 6/6 exact gates.
