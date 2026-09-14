# A site-symmetric scalar readout cannot detect both parity defects

## Question

What readout structure is required to detect the residual cokernel

\[
Q\cong(\mathbb Z/2)^2
\]

while respecting wall exchange?

## Claim boundary

This classifies linear mod-two readouts of the exact parity defect. It does not construct a laboratory detector or assert that the defect has physical binary values.

## Symmetry on the defect

The two elementary conductor characters define wall-labelled parity coordinates

\[
(b_1,b_2)\in\mathbb F_2^2.
\]

Root swaps act trivially modulo two because sign changes disappear in \(\mathbb F_2\). Wall exchange acts by

\[
\sigma(b_1,b_2)=(b_2,b_1).
\]

Thus the two-primary defect is a two-bit permutation representation.

## Invariant scalar functionals

A linear scalar readout has the form

\[
f(b_1,b_2)=\alpha b_1+\beta b_2.
\]

Wall-exchange invariance requires \(\alpha=\beta\). Therefore the only nonzero invariant scalar functional is

\[
f_{\rm sym}(b_1,b_2)=b_1+b_2.
\]

It has kernel

\[
\{(0,0),(1,1)\}.
\]

Consequently a symmetric scalar parity readout cannot distinguish no defect from simultaneous defects on both walls.

## Characteristic-two nonsemisimplicity

The swap matrix is

\[
\Sigma=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Over \(\mathbb F_2\),

\[
(\Sigma-I)^2=0
\]

but \(\Sigma\ne I\). The representation is not a direct sum of symmetric and antisymmetric lines because those lines coincide in characteristic two. Its invariant subspace and the image of \(\Sigma-I\) are both

\[
\mathbb F_2(1,1).
\]

This prevents reconstruction of both parity coordinates from one symmetric/antisymmetric decomposition.

## Minimal faithful readout

A faithful linear readout of \(Q\) needs rank two. It must retain the ordered pair

\[
(b_1,b_2)
\]

or an invertible transform of it, with wall exchange acting nontrivially on the two output channels. Equivalently, the readout must be wall-labelled before any symmetric scalar aggregation.

A complex period followed by one symmetric detector channel cannot meet this requirement. Even if augmented by total parity \(b_1+b_2\), it leaves the diagonal class \((1,1)\) invisible.

## Speculative physical consequence

If the integral defect admits a physical record, it requires two distinguishable parity-sensitive channels or one record retaining a two-component wall label. A single dark-port-like scalar may test relative parity but cannot certify both wall normalizations.

## Disposition

The minimal faithful parity readout dimension is two. Site symmetry may exchange its channels, but collapsing them to one invariant scalar loses one nonzero defect class. Physical realization remains absent.
