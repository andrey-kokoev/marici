# The standard p-adic Sonin seed is a canonical--dual pair, not a Fourier-fixed vector

## Question

Is the local seed

$$
\sigma_p=\mathbf1_{\mathbb Z_p}-p^{-1}\mathbf1_{p^{-1}\mathbb Z_p}
$$

actually fixed by the standard self-dual p-adic Fourier transform?

## Claim boundary

No. With the basic additive character of conductor \(\mathbb Z_p\) and self-dual Haar measure \(\operatorname{vol}(\mathbb Z_p)=1\), its Fourier transform is the unit-shell indicator. The two vectors have equal norm and form the local canonical--dual Sonin pair. Any semilocal Fourier claim must transport this pair rather than hold the finite seed fixed.

## Indicator transform

For the self-dual normalization,

$$
\mathcal F_p\mathbf1_{p^k\mathbb Z_p}
=p^{-k}\mathbf1_{p^{-k}\mathbb Z_p}.
$$

In particular,

$$
\mathcal F_p\mathbf1_{\mathbb Z_p}
=\mathbf1_{\mathbb Z_p},
$$

and

$$
\mathcal F_p\mathbf1_{p^{-1}\mathbb Z_p}
=p\,\mathbf1_{p\mathbb Z_p}.
$$

Therefore

$$
\boxed{
\mathcal F_p\sigma_p
=
\mathbf1_{\mathbb Z_p}-\mathbf1_{p\mathbb Z_p}
=:\tau_p.
}
$$

This is not \(\sigma_p\).

## Return transform

Similarly,

$$
\mathcal F_p\mathbf1_{p\mathbb Z_p}
=p^{-1}\mathbf1_{p^{-1}\mathbb Z_p},
$$

so

$$
\mathcal F_p\tau_p=\sigma_p.
$$

Both vectors are even under \(x\mapsto-x\), hence this two-cycle agrees with \(\mathcal F_p^2=\mathcal R_p\).

## Norm check

The dual seed is the unit-shell indicator, so

$$
\|\tau_p\|_2^2
=\operatorname{vol}(\mathbb Z_p^\times)
=1-p^{-1}.
$$

Direct shell decomposition also gives

$$
\|\sigma_p\|_2^2=1-p^{-1}.
$$

Thus local Fourier exchanges two equal-norm vectors, as required by Plancherel, but does not fix either one.

## Mellin interpretation

The Mellin transform of \(\sigma_p\) supplies the canonical inverse Euler multiplier

$$
1-p^{-1/2-is},
$$

while \(\tau_p\) supplies its Fourier-dual local section. Their relation is governed by the local unramified Tate gamma factor. This is the finite-place canonical--dual normalization required by the semilocal spectral presentation.

## Correction to the odd extension

The archimedean odd Sonin construction remains valid, but its semilocal tensor extension must use paired finite seeds:

$$
O_\lambda\otimes\bigotimes_p\sigma_p
\quad\xleftrightarrow{\ \mathcal F_S\ }\quad
O_\lambda\otimes\bigotimes_p\tau_p,
$$

with the archimedean factor transformed simultaneously. Statements that the finite seeds are individually Fourier fixed must be replaced by this paired canonical--dual transport.

## Disposition

Finite-place convention matching exposes and resolves a normalization error: \(\sigma_p\) is not Fourier invariant. The exact local sewing is the norm-preserving exchange \(\sigma_p\leftrightarrow\tau_p\). Consequently the parity-complete semilocal carrier must retain canonical and dual finite tensor charts; with that correction, the local Fourier and Euler-factor normalizations agree.