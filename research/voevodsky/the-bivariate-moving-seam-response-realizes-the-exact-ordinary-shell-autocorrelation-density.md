# The bivariate moving-seam response realizes the exact ordinary-shell autocorrelation density

## Question

Is the subleading ordinary Evans shell density absent from the complete response architecture, or can it be obtained source-derivatively from a nonlocal moving-seam response?

## Claim boundary

It is obtained exactly by applying the causal moving-seam response to the bivariate theta product \(\Phi(x)\Phi(x+t)\). Consecutive-shell subtraction gives the full autocorrelation density, adjacent shells concatenate strictly, and Laplace transformation supplies every Evans parameter jet. This constructs the missing response channel, but not the assertion that the reciprocal/linking adjoint enters with the cancelling sign.

## Bivariate source kernel

For the fixed completed theta source \(\Phi\), define

$$
g_t(x)=\Phi(x)\Phi(x+t),
\qquad t\ge0.
$$

Theta decay makes \(g_t\) rapidly integrable in \(x\), uniformly with polynomial \(t\)-weights on the required parameter ranges.

Apply the all-seam causal response in the \(x\) variable:

$$
\mathcal A_\Phi(c,t)
=\int_{-\infty}^c
\Phi(x)\Phi(x+t)\,dx.
$$

This is a function-valued, bivariate response retaining seam \(c\) and lag \(t\).

## Exact shell density

For a shell \([a,b]\), subtract the two seam evaluations:

$$
\mathcal A_\Phi(b,t)-\mathcal A_\Phi(a,t)
=
\int_a^b\Phi(x)\Phi(x+t)\,dx.
$$

Therefore

$$
\boxed{
\rho_{a,b}(t)
=
\mathcal A_\Phi(b,t)-\mathcal A_\Phi(a,t).
}
$$

The ordinary Evans shell is exactly

$$
I_{a,b}^{(0)}(z)
=-\int_0^\infty e^{-zt}
\left(
\mathcal A_\Phi(b,t)-\mathcal A_\Phi(a,t)
\right)dt.
$$

Thus the bulk autocorrelation is not outside the complete response formalism; it requires the response to be retained before collapsing the lag variable.

## Adjacent-shell concatenation

For \(a<b<c\),

$$
\rho_{a,c}(t)
=
\rho_{a,b}(t)+\rho_{b,c}(t)
$$

because the intermediate seam evaluation cancels. Hence the bivariate response obeys exact shell concatenation and is compatible with prime cutoffs.

This is stronger than matching a late-shell asymptotic.

## Parameter jets

Differentiation under the Laplace integral gives

$$
\partial_z^jI_{a,b}^{(0)}(z)
=(-1)^{j+1}
\int_0^\infty t^je^{-zt}\rho_{a,b}(t)\,dt.
$$

Therefore one source response supplies all multiplicity jets simultaneously. No fitting at individual Xi zeros occurs.

## Ordered-pair expansion

If

$$
\Phi=\sum_n\Phi_n
$$

is retained before theta-label codiagonalization, then

$$
\mathcal A_\Phi(c,t)
=
\sum_{n,m}
\int_{-\infty}^c
\Phi_n(x)\Phi_m(x+t)\,dx.
$$

Thus the construction retains ordered pairs \((n,m)\) and distinguishes them before any symmetric scalar sum. This is the carrier required by the prior completed-theta pair-response audit.

## Relation to complete response

The scalar response sheaf used

$$
A_g(c)=\int_{-\infty}^cg(x)\,dx.
$$

The present object is simply

$$
\mathcal A_\Phi(c,t)=A_{g_t}(c).
$$

Hence continuity, moving-seam covariance, endpoint attachment, and closed-image recovery are inherited parameterwise from the established response theorem, with theta decay controlling the lag-family topology.

## Remaining sign comparison

The shell residual requires

$$
I^{({\rm recip})}+I^{({\rm link})}
=-I^{({\rm end})}-I^{(0)}.
$$

The bivariate response now supplies the exact density underlying \(I^{(0)}\). It does not prove that the G4 reciprocal/linking adjoint reads this channel with coefficient \(+1\) after the exterior minus sign, nor that it simultaneously cancels the endpoint density. That is the remaining polarized source-incidence identity.

## Disposition

The allegedly missing nonlocal ordinary-shell response has an explicit source realization: it is the seam difference of the bivariate causal theta autocorrelation response. It is cutoff-additive and jet-complete. The Evans frontier is reduced to the signed comparison placing this existing channel, together with endpoint flux, into the reciprocal/linking adjoint.