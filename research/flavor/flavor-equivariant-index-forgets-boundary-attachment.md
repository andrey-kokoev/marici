# Equivariant Index Forgets Boundary Attachment

## Question

Does the marked representation-valued boundary index proposed by WP867 retain
enough information to protect the portal line and its detector attachment?

## Claim boundary

Let both source-domain coordinates carry the odd character of endpoint
exchange, and let the one-dimensional target also carry that character.  For

\[
D_\theta=(\sin\theta,\cos\theta),
\]

the map is equivariant for every (	heta).  It is surjective and satisfies

\[
D_\theta D_\theta^*=1,
\]

so its nonzero singular gap is constant.  Its representation-valued index is

\[
2\chi_- - \chi_- = \chi_-
\]

for the entire family.  The domain character, target character, index,
singular spectrum, and anomaly class therefore remain fixed.

The kernel is nevertheless

\[
k_\theta=(\cos\theta,-\sin\theta)^T.
\]

Declare the first coordinate to be the detector-coupled light boundary copy
and the second to be a heavy odd copy.  The detector support is

\[
\|P_{\rm light}k_\theta\|^2=\cos^2\theta.
\]

Thus the index does not determine how its protected character is embedded in
the source carrier.  At (	heta=0), the kernel is entirely light.  At
(cos	heta=3/4), all index and gap data are unchanged while the retained
light norm is (9/16).

This is stronger than the WP867 anomaly hostile.  It shows that even the full
equivariant chain characters and a uniform spectral gap fail to protect the
marked portal attachment.  The two complexes are connected through gapped
equivariant maps, so no homotopy-invariant index can distinguish them.

## Required stronger source object

Threshold survival requires the actual spectral projector

\[
P_{\ker D}=I-D^*D

\]

together with a named boundary evaluation map

\[
e_{\rm det}:\ker D\longrightarrow H_{\rm detector}.
\]

The relevant invariant is not merely the virtual character but the calibrated
Gram

\[
e_{\rm det}P_{\ker D}e_{\rm det}^*.
\]

For exact threshold transport, the projector and evaluation must intertwine
in one common source/readout frame.  This is a source-marked vector bundle or
subcomplex with connection data, not a bare index class.  Its detector Gram
still needs calibration in physical units.

## Gate classification

- Odd character: fixed by the equivariant index.
- Normalized portal ray: not fixed as an embedded light state.
- Conditional-expectation basin: follows the moving kernel and therefore does
  not repair detector attachment.
- Threshold survival: false for the marked light projection despite constant
  gap and index.
- Readout: changes continuously because the evaluation map is not part of the
  index.
- Physical instrument: still absent until the boundary evaluation is realized
  and calibrated in `physical16` units.

## Smallest exact falsifier

The pair (D_0=(0,1)) and

\[
D_*=(\sqrt7/4,3/4)
\]

has identical equivariant chain data, index, and singular spectrum.  Their
kernel detector Grams are respectively (1) and (9/16).

## Disposition

Negative for index-only protection and progressive for source typing.  The
sought source principle must produce a marked kernel projector and its
detector evaluation naturally through RG and thresholds.  An anomaly class or
equivariant index can protect net representation content but cannot make the
physical portal attachment unavoidable.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp868_equivariant_index_forgets_boundary_attachment.py
```
