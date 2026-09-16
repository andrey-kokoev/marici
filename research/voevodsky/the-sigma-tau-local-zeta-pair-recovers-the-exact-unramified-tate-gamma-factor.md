# The sigma--tau local zeta pair recovers the exact unramified Tate gamma factor

## Question

Does the corrected finite canonical--dual seed exchange reproduce the exact local Tate scattering multiplier used in the semilocal spectral presentation?

## Claim boundary

Yes for the trivial unramified character, with the basic additive character of conductor \(\mathbb Z_p\). Direct local zeta integration gives the standard gamma ratio and proves unit modulus on the critical line. Ramified angular characters require their separate Gauss-sum epsilon factors.

## Local conventions

Let \(d^\times x\) satisfy

$$
\operatorname{vol}(\mathbb Z_p^\times)=1,
$$

and use

$$
Z_p(f,s)=\int_{\mathbb Q_p^\times}f(x)|x|_p^s\,d^\times x.
$$

For \(\operatorname{Re}s>0\),

$$
Z_p(\mathbf1_{p^k\mathbb Z_p},s)
=\sum_{n\ge k}p^{-ns}
=\frac{p^{-ks}}{1-p^{-s}}.
$$

The canonical and dual seeds are

$$
\sigma_p
=\mathbf1_{\mathbb Z_p}
-p^{-1}\mathbf1_{p^{-1}\mathbb Z_p},
$$

$$
\tau_p
=\mathbf1_{\mathbb Z_p}-\mathbf1_{p\mathbb Z_p},
$$

with \(\widehat\sigma_p=\tau_p\).

## Canonical zeta section

Direct substitution gives

$$
Z_p(\sigma_p,s)
=
\frac{1-p^{s-1}}{1-p^{-s}}.
$$

For the dual seed,

$$
Z_p(\tau_p,s)
=
\frac{1-p^{-s}}{1-p^{-s}}
=1.
$$

Thus the shell-supported dual seed is the normalized local zeta section.

## Functional equation

The local Tate equation in these conventions is

$$
Z_p(\widehat f,1-s)
=
\gamma_p(s,1,\psi_p)Z_p(f,s).
$$

Setting \(f=\sigma_p\) yields

$$
\boxed{
\gamma_p(s,1,\psi_p)
=
\frac{1-p^{-s}}{1-p^{s-1}}.
}
$$

Equivalently,

$$
\gamma_p(s,1,\psi_p)
=
\frac{L_p(1-s)}{L_p(s)}
$$

for \(L_p(s)=(1-p^{-s})^{-1}\), with numerator/denominator interpreted according to the displayed functional-equation arrow.

## Critical-line check

For

$$
s=\frac12+it,
$$

one has

$$
1-p^{s-1}
=\overline{1-p^{-s}}.
$$

Therefore

$$
|\gamma_p(1/2+it)|=1,
$$

and

$$
\gamma_p(s)\gamma_p(1-s)=1.
$$

This is the finite-place analogue of the even real parity product.

## Semilocal sewing

For a finite set \(S\), tensoring the local pairs gives canonical and dual finite vectors

$$
\Sigma_S^{\rm can}
=\bigotimes_{p\in S_f}\sigma_p,
\qquad
\Sigma_S^{\rm dual}
=\bigotimes_{p\in S_f}\tau_p.
$$

Fourier exchanges them, and Mellin comparison contributes

$$
\prod_{p\in S_f}
\frac{1-p^{-s}}{1-p^{s-1}}.
$$

Multiplying by the already matched real trivial/sign factors yields the exact semilocal Tate scattering symbol. No finite scalar or norm correction remains, since \(\|\sigma_p\|_2=\|\tau_p\|_2\).

## Boundary

For ramified multiplicative characters, ball indicators may pair trivially and the local factor contains conductor powers and a Gauss-sum epsilon phase. Those sectors are not derived from the unramified \(K_p\)-invariant seed pair and remain a separate characterwise extension.

## Disposition

The corrected local seed exchange exactly reproduces the unramified finite Tate gamma factor. Combined with the verified real parity factors, the full unramified semilocal canonical--dual Fourier normalization is now fixed with no residual block-unitary choice.