# Correction: finite-interval images include translation aliases as well as reflections

The odd `2ell`-periodic extension underlying the spectral Dirichlet
logarithm has image kernel schematically

\[
\sum_{k\in\mathbb Z}
\bigl[h(x-y+2k\ell)-h(x+y+2k\ell)\bigr],
\]

where `h` is the whole-line logarithmic kernel, modulo its local and
regularization constants. Restriction of the zero-extension operator supplies
only the `k=0` direct term `h(x-y)`.

Hence the finite-interval remainder contains both

\[
\sum_{k\ne0}h(x-y+2k\ell)
\]

and

\[
-\sum_{k\in\mathbb Z}h(x+y+2k\ell).
\]

The previous nearest-image packet discussed only the reflected series. A
complete direct comparison must also include the nonzero translation aliases.
After symmetric pairing in `k`, the first-order harmonic divergences cancel
or reduce to explicitly regularized constant kernels, while the residual
terms decay quadratically in `k`.

The corrected decomposition therefore has four pieces:

1. nearest left and right reflected Carleman images;
2. paired nonzero translation aliases;
3. farther reflected aliases;
4. local/rank-one constants fixed by the Fourier convention.

No direct finite-interval norm is certified until all four are assembled with
their exact prefactors.
