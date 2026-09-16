# The complete semilocal Tate sewing is a cutoff-natural unitary order-four operator

## Question

Do the locally normalized real, unramified, and ramified factors assemble into one semilocal Fourier operator that is unitary, has the correct fourth power, and commutes with enlargement of the finite place set?

## Claim boundary

Yes on the characterwise test/Hilbert spectral carrier with canonical--dual finite seed charts. The operator is exact and cutoff-natural. This does not by itself prove invariance of the differentiated Weil quadratic form or the downstream Evans--Green chain.

## Characterwise carrier

Decompose the semilocal multiplicative carrier along unitary angular characters:

$$
\mathcal H_S
=\int_{\widehat{C_S^1}}^\oplus
L^2(\mathbb R_t)\,d\chi,
$$

with a direct sum in the discrete case. Additive Fourier sends the \(\chi^{-1}\) angular fiber to the \(\chi\) fiber and reverses the Mellin coordinate.

Define

$$
(\mathbb F_Sh)_\chi(t)
=\gamma_S(\chi,t)
h_{\chi^{-1}}(-t),
$$

where

$$
\gamma_S(\chi,t)
=\prod_{v\in S}
\gamma_v\left(\frac12+it,\chi_v,\psi_v\right).
$$

Each factor is the source-derived local multiplier already computed from its canonical--dual seed.

## Unitarity

For unitary \(\chi\) and real \(t\), every local factor has modulus one:

$$
|\gamma_v(\chi_v,t)|=1.
$$

Character inversion and spectral reflection preserve the Plancherel measure. Consequently

$$
\|\mathbb F_Sh\|_{\mathcal H_S}
=\|h\|_{\mathcal H_S}.
$$

No mixing unitary between equal-multiplicity blocks is selected; the local functional equations determine the multiplier character by character.

## Square and fourth power

The local reflected product law is

$$
\gamma_v(\chi_v,t)
\gamma_v(\chi_v^{-1},-t)
=\chi_v(-1).
$$

Therefore

$$
(\mathbb F_S^2h)_\chi(t)
=\chi(-1)h_\chi(t),
$$

where

$$
\chi(-1)=\prod_{v\in S}\chi_v(-1).
$$

This is exactly additive reflection \(f(x)\mapsto f(-x)\) in the angular decomposition. Since \(\chi(-1)^2=1\),

$$
\mathbb F_S^4=I.
$$

## Canonical--dual finite charts

At an unramified finite place, Fourier exchanges

$$
\sigma_p
\longleftrightarrow
\tau_p.
$$

At a ramified place, it exchanges the normalized unit-shell character seed with its conductor-shell Gauss transform. Thus the global source and target are paired tensor charts; no finite seed is incorrectly required to be fixed.

## Place-cutoff naturality

Let \(S\subset S'=S\cup\{p\}\). The canonical enlargement tensors the source chart by the local canonical seed and the dual chart by its Fourier image. Denote these paired embeddings by

$$
iota_{S,S'}^{\rm can},
\qquad
iota_{S,S'}^{\rm dual}.
$$

Local Fourier equivariance gives the exact square

$$
\mathbb F_{S'}\iota_{S,S'}^{\rm can}
=
iota_{S,S'}^{\rm dual}\mathbb F_S.
$$

On Mellin fibers, this is precisely multiplication by the newly added local gamma factor. Iterating proves naturality for arbitrary finite-place cutoffs.

## Relation to radial sewing

At the real place, the factor is the parity diagonalization of the oriented Hankel lift. Hence the real component satisfies

$$
\widetilde W_u^2=W_u.
$$

The finite factors supply canonical--dual scattering phases without altering the real radial square-root relation. The total semilocal operator is therefore the characterwise spectral presentation of actual additive Fourier sewing.

## Remaining quadratic-form gate

The Weil operator involves logarithmic derivatives

$$
-i\partial_t\log\gamma_S(\chi,t),
$$

not merely multiplication by \(\gamma_S\). Unitarity and cutoff naturality of \(\mathbb F_S\) do not imply positivity or global maximal-isotropic incidence for that differentiated form. Those remain separate.

## Disposition

The full characterwise semilocal Tate sewing is now an explicit cutoff-natural unitary with square equal to additive reflection and fourth power identity. The radial, spectral, and canonical--dual Fourier operators agree on the common test/Hilbert carrier. The remaining global-response obstruction lies in the Weil/Green form, not in sewing normalization or coherence.