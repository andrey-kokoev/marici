# c-kernel versus p-normal mismatch

## Question

Can the retained \(c\) pivot itself be identified with the p-normal \(\Xi_{\log}\) leg required by the \(\tau_p\) contract?

## Claim boundary

This packet tests only the covector comparison between the base-dependent \(c\) pivot and the source p-normal. It does not construct a base--fiber comparison, kernel section, Bockstein class, global contour, or physical period.

## Disposition

The source p-normal is

\[
dp=dx+dy+3dz,
\]

with coefficient vector

\[
(1,1,3).
\]

The retained pivot has source role

\[
c=-(x+y+z),
\]

so

\[
dc=-(dx+dy+dz),
\]

with coefficient vector

\[
(-1,-1,-1).
\]

These covectors are not unit multiples. Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), their span has rank \(2\).

Thus retaining \(c\) restores a relative three-chart cover, but it does not identify the \(c\)-kernel with the p-normal \(\Xi_{\log}\) leg. The missing datum is a source-derived base comparison from the \(c\)-kernel direction to the p-normal residue class, not a scalar normalization of \(c\).

The forbidden shortcut is to treat \(c=-(x+y+z)\) as the normal \(p=x+y+3z\).

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_c_kernel_p_normal_mismatch.py`

Result:

- `research/voevodsky/results/cosmology_c_kernel_p_normal_mismatch.json`

Command:

- `python research/voevodsky/check_cosmology_c_kernel_p_normal_mismatch.py`
