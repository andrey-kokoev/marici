# One seam differential of the bivariate response cancels the ordinary-plus-endpoint Evans shell identically

## Question

Once the ordinary autocorrelation density is represented by the bivariate moving-seam response, is there a source-defined response combining bulk and endpoint terms with the exact required sign and every parameter jet?

## Claim boundary

Yes as an analytic response identity, before any Xi specialization. Applying \(1+\partial_c\) to the shell difference of the bivariate causal response produces a Laplace section exactly opposite to the ordinary plus derivative-wall endpoint shell. This supplies the unique natural reciprocal-plus-linking candidate. Identification with the already declared G4 adjoint ports remains a typed comparison theorem.

## Bivariate response

Define

$$
\mathcal A_\Phi(c,t)
=\int_{-\infty}^c
\Phi(x)\Phi(x+t)\,dx.
$$

Its seam derivative is

$$
\partial_c\mathcal A_\Phi(c,t)
=\Phi(c)\Phi(c+t).
$$

For a shell \([a,b]\), write

$$
\Delta_{a,b}F=F(b)-F(a).
$$

Then

$$
\rho_{a,b}(t)
=\Delta_{a,b}\mathcal A_\Phi(\cdot,t).
$$

## Ordinary shell

The analytic-transpose ordinary term is

$$
I_{a,b}^{(0)}(z)
=-\int_0^\infty e^{-zt}
\Delta_{a,b}\mathcal A_\Phi(\cdot,t)\,dt.
$$

## Endpoint shell

The Evans history is

$$
u_z(c)
=-\int_0^\infty e^{-zt}\Phi(c+t)\,dt.
$$

Therefore

$$
\Phi(c)u_z(c)
=-\int_0^\infty e^{-zt}
\partial_c\mathcal A_\Phi(c,t)\,dt.
$$

Taking the shell endpoint difference gives

$$
I_{a,b}^{({\rm end})}(z)
=-\int_0^\infty e^{-zt}
\Delta_{a,b}\partial_c\mathcal A_\Phi(\cdot,t)\,dt.
$$

## Exact combined density

Adding the two sourced shell terms yields

$$
I_{a,b}^{(0)}(z)+I_{a,b}^{({\rm end})}(z)
=-\int_0^\infty e^{-zt}
\Delta_{a,b}(1+\partial_c)
\mathcal A_\Phi(\cdot,t)\,dt.
$$

Define the response section

$$
\boxed{
\mathcal R_{a,b}^{\rm RL}(z)
=
\int_0^\infty e^{-zt}
\Delta_{a,b}(1+\partial_c)
\mathcal A_\Phi(\cdot,t)\,dt.
}
$$

Then the identity

$$
\boxed{
I_{a,b}^{(0)}(z)
+I_{a,b}^{({\rm end})}(z)
+\mathcal R_{a,b}^{\rm RL}(z)
=0
}
$$

holds on the common half-plane and extends entire wherever the sourced Evans shell sections do.

## Every multiplicity jet

Differentiating gives

$$
\partial_z^j\mathcal R_{a,b}^{\rm RL}(z)
=(-1)^j
\int_0^\infty t^je^{-zt}
\Delta_{a,b}(1+\partial_c)
\mathcal A_\Phi(\cdot,t)\,dt.
$$

Hence the cancellation identity holds after every \(z\)-derivative. It is not fitted to a zero or to its multiplicity.

## Shell concatenation

For \(a<b<c\),

$$
\Delta_{a,c}
=\Delta_{a,b}+\Delta_{b,c}.
$$

Therefore

$$
\mathcal R_{a,c}^{\rm RL}
=
\mathcal R_{a,b}^{\rm RL}
+
\mathcal R_{b,c}^{\rm RL}.
$$

The candidate is exactly compatible with consecutive-prime cutoff bonding and the limiting common mode.

## Port interpretation

The two summands have distinct source roles:

- \(\Delta\mathcal A_\Phi\) is the nonlocal reciprocal/bulk autocorrelation response;
- \(\Delta\partial_c\mathcal A_\Phi\) is its ordered seam-Stokes boundary response.

Their relative coefficient is forced by the first-order Green totalization, not selected from the desired zero set. The exterior plus sign in \(\mathcal R^{\rm RL}\) is the contragredient return sign needed to oppose the analytic Evans row.

## Remaining typed gate

To identify this section with

$$
I^{({\rm recip})}+I^{({\rm link})}
$$

inside the existing G4 adjoint, one must prove that the declared reciprocal and ordered-linking port maps are exactly the two evaluations above under the common source comparison. Boundedness, equal asymptotics, or scalar trace agreement is insufficient.

## Disposition

A source-defined reciprocal-plus-linking response now satisfies the complete Evans shell cancellation identity, including all multiplicity jets and cutoff concatenation. The remaining question is no longer existence of a cancelling analytic section; it is exact typing of this section as the existing G4 reciprocal/linking adjoint row.