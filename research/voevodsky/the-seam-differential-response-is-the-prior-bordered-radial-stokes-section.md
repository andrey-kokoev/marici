# The seam-differential response is the prior bordered radial Stokes section

## Question

Is the newly constructed section \(\mathcal R_{a,b}^{\rm RL}\) genuinely new, and does prior research identify its decomposition into endpoint and Wronskian response coordinates?

## Claim boundary

It is the same source section previously obtained from the diagonal radial Stokes identity. The bivariate seam formulation supplies a compact derivation and embeds it naturally into the v3 function-valued response type. This identifies all analytic coordinates and coefficients, but owner declaration is still required to assert that the G4 arithmetic adjoint uses this bordered section as its reciprocal-plus-linking row.

## Translation between notations

Let

$$
\rho(t)=\int_a^b\Phi(x)\Phi(x+t)\,dx
=\Delta_{a,b}\mathcal A_\Phi(\cdot,t).
$$

Define

$$
R(z)=\int_0^\infty e^{-zt}\rho(t)\,dt,
$$

and

$$
E(z)=\frac12\int_0^\infty e^{-zt}
\Delta_{a,b}\partial_c\mathcal A_\Phi(\cdot,t)\,dt.
$$

Then the seam-differential response is exactly

$$
\mathcal R_{a,b}^{\rm RL}(z)=R(z)+2E(z).
$$

This is the combined section frozen in prior research.

## Wronskian decomposition

Define the ordered shell Wronskian current

$$
\mathcal W^{[a,b]}(t)
=
\int_a^b
\left[
\Phi'(x)\Phi(x+t)
-
\Phi(x)\Phi'(x+t)
\right]dx.
$$

Integration by parts gives

$$
\rho'(t)
=
\frac12\Delta_{a,b}
\bigl(\Phi(c)\Phi(c+t)\bigr)
-
\frac12\mathcal W^{[a,b]}(t).
$$

After Laplace transformation,

$$
zR(z)-\rho(0)
=E(z)-\frac12W(z),
$$

where

$$
W(z)=\int_0^\infty e^{-zt}\mathcal W^{[a,b]}(t)\,dt.
$$

Therefore

$$
\boxed{
\mathcal R_{a,b}^{\rm RL}(z)
=
\frac{\rho(0)+E(z)-\frac12W(z)}{z}
+2E(z).
}
$$

The apparent singularity is removable by the Stokes identity.

## Fixed bordered coefficients

The complete function-valued section uses:

- initial autocorrelation coefficient \(+1\);
- endpoint coefficient \(+1\) inside the divided difference;
- Wronskian coefficient \(-1/2\) inside the divided difference;
- additional endpoint coefficient \(+2\).

These numbers are derived before Xi specialization. They reproduce the necessary leading and subleading late-shell asymptotics automatically.

## V3 response typing

The v3 interface retains a function-valued response and a compatible all-jet family rather than only one scalar wall/incidence trace. The objects

$$
(\rho(0),E(z),W(z),R(z))
$$

form a bordered response packet with:

- shell and theta-pair labels retained;
- slot-reversal orientation in \(W\);
- exact adjacent-shell concatenation;
- entire Laplace jets;
- endpoint atom separated from bulk response.

Thus this packet has the analytic type required by the v3 response carrier.

## Why typing is still not admission

The equality

$$
I^{({\rm recip})}+I^{({\rm link})}
=\mathcal R_{a,b}^{\rm RL}
$$

is the arithmetic return placement that would annihilate the complete shell residual. Declaring it is therefore already the RH-bearing chain-promotion input. It cannot be inferred solely from the fact that the packet fits the response type.

The remaining source comparison must show that the existing reciprocal and linking adjoint maps, with their frozen arithmetic coefficients and contragredient signs, evaluate to this bordered section.

## Disposition

Prior research and the new bivariate construction agree exactly: the required combined response is the bordered radial Stokes section \(R+2E=(\rho(0)+E-W/2)/z+2E\). All analytic coordinates, coefficients, jets, and cutoff laws are fixed. The sole unresolved statement is its arithmetic G4 adjoint placement, which is precisely the RH-bearing source identity rather than a missing analysis formula.