# Lightweight pre-cutoff vector census

## Question

Does WP516's own frozen mass matrix contain threshold-open coupling candidates
below its \(10^{-7}\) retention cutoff?

Yes. WP529 reconstructs the same fourteen-state mass matrix directly from
WP507's explicit gauge tangents, avoiding the pathological symbolic replay.
It then transports the exact gauge-basis Yang--Mills tensor through the
numerical mass rotation before applying any coupling cutoff.

## Reconstruction check

The lightweight construction applies:

- the eight \(SU(3)_F\), three \(SO(3)_P\), and three \(SO(3)_E\) tangents;
- the WP508 factor of one-half on flavor generators;
- field metric weights one on the real connector and two on adjoint and
  complex entrance coordinates;
- the exact \(SU(3)\) structure constants and the two three-dimensional
  Levi--Civita tensors.

It reproduces the stored WP516 masses within
\(6.43\times10^{-14}\) GeV. The eigendecomposition residual is below
\(1.43\times10^{-14}\), and the orthogonality residual is below
\(10^{-15}\).

## Pre-cutoff result

Among 173 threshold-open parent and unordered-daughter candidates:

- 34 have couplings above the original \(10^{-7}\) cutoff;
- eight additional entries lie between \(4.63\times10^{-12}\) and
  \(6.24\times10^{-10}\);
- 131 entries lie at or below \(8.38\times10^{-14}\).

Thus the lightweight reconstruction contains 42 entries above
\(10^{-12}\), not 34. The candidate-to-numerical-zero gap exceeds a factor
fifty.

Using WP517's unequal-mass formula, the eight candidate partial widths sum to
approximately

\[
3.13\times10^{-16}.
\]

The width is measured in GeV.

This is tiny relative to the resolved widths. It is nevertheless not admitted
as an exact correction, because several states occur in very small spectral
gaps and individual eigenvector couplings can be basis-sensitive until their
intervals or degenerate-subspace sums are certified.

## Authority boundary

WP529 defeats two opposite shortcuts:

- WP516's cutoff cannot be treated as an exact zero test, because eight
  threshold-open candidates occur below it.
- The eight candidates cannot yet be called physical nonzero channels merely
  because double precision places them above the numerical-zero cluster.

The correct invariant objects near a small gap are complete spectral
projectors and summed squared couplings over the certified cluster. Their
width contribution, rather than an arbitrary eigenvector component, must be
bounded.

## Disposition

- Domain: all threshold-open vector triples at the WP516 witness.
- Source coordinate: the full transported Yang--Mills tensor before cutoff.
- Classification: corrective numerical census, neither selector nor
  rigidifier.
- Width result: eight sub-cutoff candidates with candidate sum
  \(3.13\times10^{-16}\) GeV.
- Smallest falsifier: a high-precision interval for a candidate contains zero
  or its cluster-summed projector coupling vanishes.
- Remaining gate: reconstruct the small-gap clusters at high precision,
  certify basis-invariant summed couplings, and add every certified width to
  the WP527 nonquark-closed packet before WP525 complex-pole transport.

This packet corrects the numerical channel census without promoting a
floating separation into exact algebra.
