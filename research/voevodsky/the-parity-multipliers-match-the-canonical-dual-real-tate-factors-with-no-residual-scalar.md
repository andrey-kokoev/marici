# The parity multipliers match the canonical-dual real Tate factors with no residual scalar

## Question

Do the verified radial gamma branches agree exactly with the unitary canonical--dual Tate normalization used in the semilocal spectral presentation, or only up to an unspecified constant?

## Claim boundary

They agree exactly once the additive character and Mellin exponent are written explicitly. The apparent inversion comes from the fact that Fourier sends Mellin exponent \(z\) to \(1-z\). The odd factor carries the expected \(-i\) epsilon phase for \(\psi_-(x)=e^{-2\pi ix}\).

## Radial multipliers

For \(0<\operatorname{Re}z<1\), the parity multipliers derived from additive Fourier are

$$
c_0(z)
=2(2\pi)^{-z}\Gamma(z)
\cos\left(\frac{\pi z}{2}\right),
$$

$$
c_1(z)
=-2i(2\pi)^{-z}\Gamma(z)
\sin\left(\frac{\pi z}{2}\right).
$$

They occur in

$$
\mathcal M_j(\mathcal Ff)(z)
=c_j(z)\mathcal M_jf(1-z),
$$

where \(j=0\) is trivial parity and \(j=1\) is sign parity.

## Gamma-ratio form

Duplication and reflection give

$$
c_0(z)
=\pi^{1/2-z}
\frac{\Gamma(z/2)}
{\Gamma((1-z)/2)},
$$

and

$$
c_1(z)
=-i\pi^{1/2-z}
\frac{\Gamma((z+1)/2)}
{\Gamma((2-z)/2)}.
$$

For the real Tate factors normalized with

$$
\psi_-(x)=e^{-2\pi ix},
$$

define

$$
\gamma_{\mathbb R}(w,1,\psi_-)
=\pi^{w-1/2}
\frac{\Gamma((1-w)/2)}{\Gamma(w/2)},
$$

$$
\gamma_{\mathbb R}(w,\operatorname{sgn},\psi_-)
=-i\pi^{w-1/2}
\frac{\Gamma((2-w)/2)}{\Gamma((w+1)/2)}.
$$

The Fourier multiplier is the reflected Tate factor. Explicitly,

$$
c_0(z)=\gamma_{\mathbb R}(1-z,1,\psi_-),
\qquad
c_1(z)=\gamma_{\mathbb R}(1-z,\operatorname{sgn},\psi_-).
$$

If another source assigns `gamma` to the opposite canonical--dual arrow, it writes the reciprocal factor at the reflected argument. The operator formula, rather than the isolated name `gamma`, fixes the polarity unambiguously.

For the convention used in the semilocal packet

$$
(\mathscr F_\chi h)(t)
=\gamma_S(\chi,t)h(-t),
$$

take

$$
z=\frac12-it.
$$

Then its real local scattering factors are exactly

$$
\gamma_{\infty,0}(t)=c_0\left(\frac12-it\right),
$$

$$
\gamma_{\infty,1}(t)=c_1\left(\frac12-it\right).
$$

No additional power of \(2\pi\), modulus factor, or constant phase remains.

## Additive-character check

Changing from \(\psi_-\) to \(\psi_+(x)=e^{2\pi ix}\) conjugates the real epsilon phase. The even branch is unchanged, while the odd phase changes from \(-i\) to \(+i\). Thus the odd sign is not gauge ambiguity; it records the declared additive character.

## Canonical--dual polarity

Because the spectral action includes \(t\mapsto-t\), assigning \(c_j(t)\) to the forward arrow or assigning its reciprocal at \(-t\) to the return arrow gives the same operator. The exact identities

$$
c_0(t)c_0(-t)=1,
\qquad
c_1(t)c_1(-t)=-1
$$

include the parity reflection sign and determine the canonical--dual return without a free block-unitary choice.

## Semilocal product

Finite-place local factors multiply these real branches characterwise. Therefore the archimedean component of

$$
\gamma_S(\chi,t)=\prod_{v\in S}\gamma_v(\chi_v,t)
$$

is now fixed exactly for both real characters. No unsupported scalar normalization remains at infinity.

## Disposition

The oriented radial Mellin multipliers are precisely the real trivial/sign Tate scattering factors used by the canonical--dual spectral operator for the Fourier character \(e^{-2\pi ixy}\). The former phrase “up to fixed normalization constants” can be removed. Only finite-place convention matching remains in the full semilocal product.