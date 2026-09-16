# The semilocal Tate logarithmic connection commutes with Fourier sewing and adds under cutoffs

## Question

Does passing from the unitary Tate scattering product to its logarithmic derivative preserve the newly proved Fourier sewing coherence and place-cutoff naturality?

## Claim boundary

Yes for the characterwise Tate logarithmic-connection operator on its natural differentiable domain. It is self-adjoint multiplication, commutes with semilocal Fourier sewing, and adds local terms under enlargement of the place set. This does not prove positivity of its compression to the Sonin/Green relation.

## Scattering and connection

Write

$$
(\mathbb F_Sh)_\chi(t)
=\gamma_S(\chi,t)h_{\chi^{-1}}(-t),
$$

with \(|\gamma_S(\chi,t)|=1\). Define

$$
a_S(\chi,t)
=-i\,\gamma_S(\chi,t)^{-1}
\partial_t\gamma_S(\chi,t)
=-i\partial_t\log\gamma_S(\chi,t),
$$

and let

$$
(\mathbb A_Sh)_\chi(t)
=a_S(\chi,t)h_\chi(t).
$$

The natural maximal multiplication domain is

$$
\mathcal D(\mathbb A_S)
=
\left\{h:
 a_S h\in\mathcal H_S
\right\}.
$$

## Self-adjointness

Since \(\gamma_S\) is unimodular on the critical line,

$$
\gamma_S^{-1}\partial_t\gamma_S
$$

is purely imaginary. Therefore \(a_S\) is real almost everywhere, and multiplication by \(a_S\) is self-adjoint on its maximal domain.

## Reflected derivative identity

Fourier square gives

$$
\gamma_S(\chi,t)
\gamma_S(\chi^{-1},-t)
=\chi(-1).
$$

The right side is constant in \(t\). Logarithmic differentiation yields

$$
\frac{\partial_t\gamma_S(\chi,t)}
{\gamma_S(\chi,t)}
-
\left.
\frac{\partial_u\gamma_S(\chi^{-1},u)}
{\gamma_S(\chi^{-1},u)}
\right|_{u=-t}
=0.
$$

The displayed minus sign is the chain rule from differentiating the reflected argument. Hence

$$
\boxed{
a_S(\chi,t)
=a_S(\chi^{-1},-t).
}
$$

## Fourier commutation

For \(h\) in a common core,

$$
(\mathbb F_S\mathbb A_Sh)_\chi(t)
=
\gamma_S(\chi,t)
a_S(\chi^{-1},-t)
h_{\chi^{-1}}(-t),
$$

while

$$
(\mathbb A_S\mathbb F_Sh)_\chi(t)
=
a_S(\chi,t)\gamma_S(\chi,t)
h_{\chi^{-1}}(-t).
$$

The reflected derivative identity gives

$$
\boxed{
\mathbb F_S\mathbb A_S
=\mathbb A_S\mathbb F_S.
}
$$

The identity also shows that \(\mathbb F_S\) preserves the maximal multiplication domain.

## Additivity under place cutoffs

Because

$$
\gamma_S=\prod_{v\in S}\gamma_v,
$$

one has

$$
a_S(\chi,t)
=\sum_{v\in S}a_v(\chi_v,t).
$$

For \(S'=S\cup\{p\}\),

$$
\boxed{
\mathbb A_{S'}
=\mathbb A_S+\mathbb A_p
}
$$

on the common core. Thus logarithmic differentiation converts the coherent Euler product into the source-required additive local/prime decomposition without losing Fourier covariance.

For an unramified finite place,

$$
\gamma_p(s)
=\frac{1-p^{-s}}{1-p^{s-1}},
$$

and differentiating its logarithm generates the full prime-power frequency tower. For a ramified place, differentiating the conductor monomial contributes the constant conductor term, while the Gauss phase is constant in \(t\).

## Remaining Green gate

Commutation and self-adjointness do not imply

$$
\langle h,\mathbb A_Sh\rangle\ge0
$$

on a compressed Sonin space, nor do they prove that the complete Fourier--Poisson response trace lies in the global maximal-isotropic Green sewing relation. Those require the separate compressed-trace/boundary cancellation theorem.

## Disposition

The full semilocal Tate logarithmic connection is Fourier invariant and place-additive. Therefore normalization, quarter-turn sewing, and prime-cutoff coherence survive differentiation to the Weil operator. The remaining obstruction is precisely positivity/maximal-isotropic Green incidence, not global Fourier--Poisson response intertwining at the uncompressed spectral-operator level.