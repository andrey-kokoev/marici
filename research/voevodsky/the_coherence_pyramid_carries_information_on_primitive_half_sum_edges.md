# The coherence pyramid carries information on primitive half-sum edges

## Question

What are the four vertices of the existing coherence pyramid, and along which objects should information move to retain the primitive complement erased by endpoint parity?

## Claim boundary

This packet identifies the integral carrier and its edge directions from the established four split fibers. It does not yet identify a chosen primitive edge with the de Rham coordinate \(v_{\rm alg}\).

## Four vertices

The four critical lines of the reflection-adapted pencil have split inverse images

\[
C_i^+\cup C_i^-,
\qquad i=1,2,3,4.
\]

Their oriented component differences

\[
d_i=[C_i^+]-[C_i^-]
\]

satisfy

\[
d_i^2=-6,
\qquad
d_i\cdot d_j=2\quad(i\ne j),
\qquad
d_1+d_2+d_3+d_4=0.
\]

These \(d_i\), not the abstract conductor root swaps, are the four vertices relevant to the integral coherence pyramid.

## Edge carriers

Information does not move integrally by choosing one isolated vertex difference. The primitive closure is carried by correlated half-sums

\[
\alpha_{ij}=\frac{d_i+d_j}{2}.
\]

Opposite edges differ by sign:

\[
\alpha_{12}=-\alpha_{34},
\qquad
\alpha_{13}=-\alpha_{24},
\qquad
\alpha_{14}=-\alpha_{23}.
\]

Three adjacent edge classes form the orthogonal lattice

\[
\langle\alpha_{12},\alpha_{13},\alpha_{14}\rangle
\cong A_1^3,
\qquad
(\alpha_{1i}\cdot\alpha_{1j})=-2\delta_{ij}.
\]

Thus the half-factor required by the response is already an integral geometric operation: pair two split-fiber vertices and pass to their primitive half-sum.

## Path selected by the four energy arrangement

The repeated collision types pair the four energy values as

\[
\{0,2(x+y)\},
\qquad
\{2x,2y\}.
\]

After a labelled braid-to-Picard lift identifies these with \((d_1,d_4)\) and \((d_2,d_3)\), the two paired edge carriers are

\[
\frac{d_1+d_4}{2}=\alpha_{14},
\qquad
\frac{d_2+d_3}{2}=\alpha_{23}=-\alpha_{14}.
\]

Hence the information reaching the total-energy vertex through the two middle critical fibers should be accumulated as a half-sum, not as an endpoint difference and not as the half-difference of two abstract monodromy actions.

## Role of the missing comparison

The missing comparison has two jobs:

1. label the four energy punctures by the four integral component differences \(d_i\), including orientations;
2. identify which primitive \(A_1\) edge maps to the source coordinates \(e_6\) and \(v_{\rm alg}\).

The carrier itself is not missing. It is the primitive closure of the four vertex differences. Endpoint mod-two parity sees all \(d_i\) as the same class and therefore forgets the edge coordinate. The primitive half-sum retains exactly that relational information.

## Disposition

The flow should run from vertex data into a correlated two-vertex half-sum edge, then into the primitive \(A_1^3\) lattice, and only afterward into the two-coordinate physical readout. The immediate executable comparison is to match two labelled soft centers with two independent \(\alpha_{1i}\) directions; one center alone can determine only the already known \(e_6\) line.

Verification:

- `research/voevodsky/checkers/check_coherence_pyramid_half_sum_edges.py`
- `research/voevodsky/results/coherence_pyramid_half_sum_edges.json`
