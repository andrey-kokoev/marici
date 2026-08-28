# 3629 — Theta-Label Slices Are Prime-Polydisk Stable, but the Completed Readout Need Not Preserve Stability

The actual positive-chamber theta summands satisfy a uniform vacuum-dominance
theorem. For `u>=0`, their ratios obey

\[
\frac{\phi_n(u)}{\phi_1(u)}
<\frac{2n^4}{2^{3(n^2-1)}},
\]

and the sum of this majorant for `n>=2` is below `1/15`. Consequently the full
prime-labelled slice

\[
\Theta_u(w)=\sum_{n\ge1}\phi_n(u)w^{v(n)}
\]

has modulus greater than `14 phi_1(u)/15` whenever every `|w_p|<=1`. Every
fixed-`u` theta slice is therefore uniformly prime-polydisk stable.

For each two-prime cell, the scalar interaction determinant is strictly
negative because it is the exponential of a mixed finite difference of
`log(phi_1)`, whose exact second derivative is negative. This does not signal
failure of source interchange: the shift operators commute exactly. It
measures failure of scalar evaluation to preserve their tensor product.

This still does not prove RH. The Riemann spectral variable emerges only after
the completed Mellin/Fourier readout transports the label shifts and moving
seam. Oscillatory linear aggregation does not generally preserve stable
polynomials: `1+w` and `1-w` are disk-stable, while their difference `2w`
vanishes at the origin.

Thus the missing theorem is now an operator theorem: the completed theta
readout, with its seam channel retained, must have a stability-preserving
symbol on the source-authorized labelled class. Pointwise slice stability is
proved; preservation under completed aggregation is the real obstacle.

The exact checker passes 8/8 gates.

Artifacts:

- `research/grothendieck/theta-label-slices-are-prime-polydisk-stable-but-the-completed-readout-need-not-preserve-stability.md`
- `research/grothendieck/checkers/check_theta_slice_prime_polydisk_dominance.py`
