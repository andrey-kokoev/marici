# A common-source integer mass norm isolates seventeen: WP1028

## Question

Can one construct the missing source-to-threshold interface without a free
continuous normalization?

## Candidate source constructor

Let the same source vacuum of norm \(f\) generate \(N\) equal orthogonal
messenger-mass contributions. Their positive mass Gram norm is

\[
M^2=Nf^2,
\qquad
r=\frac fM=\frac1{\sqrt N},
\qquad N\in\mathbb Z_{>0}.
\]

This is a common-source interface: no relative continuous scale remains after
granting equal unit-normalized contributions. The integer \(N\) remains
source data and must not be inferred from CKM.

## Exact window theorem

Comparing the discrete family with the WP1025 reconstructed interval gives
exactly one compatible integer:

\[
N=17.
\]

The neighbouring predictions are hostile witnesses:
\(1/\sqrt{16}\) lies above the full interval and \(1/\sqrt{18}\) lies
below it. Hence the singleton is not a consequence of finite scan resolution.

Composing \(r=1/\sqrt{17}\) with the exact WP1025 response predicts

\[
J^2=
\frac{6800}{3(258539696800\sqrt{17}+1203211349783)},
\]

or \(|J|\simeq3.1605134974\times10^{-5}\). Among the 1,210 fitted sheets,
18 lie below this value, 1,192 above it, and none equals it literally. The
prediction lies strictly inside the ensemble range; exact sheet equality is
not claimed.

## Selector classification and instrument

The family replaces a continuous normalization fiber with an integer fiber and
has one data-compatible member. It becomes a genuine source selector only if a
source theory independently derives:

- exactly seventeen contributions;
- equality and orthogonality of their physical mass norms;
- the absence of a bare messenger mass or unequal threshold corrections.

The remaining instrument is not CKM. It is a source-count or spectroscopy
experiment capable of establishing the seventeen-component mass constructor
and its equal-norm Gram law.

## Smallest exact falsifier

The pair \(N=16,18\) brackets and excludes the reconstructed interval from
opposite sides. For source authority, any independently admitted value
\(N\ne17\), unequal contribution norm, or nonzero bare mass falsifies the
candidate.

## Claim boundary

This packet proves a discrete compatibility and a common-source interface
normal form. It does not derive seventeen, establish a messenger spectrum,
control loops, or promote CKM inversion into source authority.

## Disposition

Progressive candidate, not yet an admitted selector. The next move is to search
the declared source spectrum for an independently compulsory rank or index
equal to seventeen and a physical mass-Gram realization.

Verification: uv run --with sympy python
research/flavor/checkers/wp1028_integer_mass_norm_window.py
