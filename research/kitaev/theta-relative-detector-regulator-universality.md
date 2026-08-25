# The theta relative detector is universal across normalized Mellin regulators

Owner: `marici.Kitaev`

## Bounded question

Is Grothendieck's heat finite-part detector specific to the Gaussian cutoff, or
is its constant term invariant under a source-compatible normalized class of
regulators?

## Mellin regulator class

Let \(\rho:(0,\infty)\to\mathbb C\) decay rapidly at infinity, have a smooth
expansion at zero, and satisfy

\[
\rho(0)=1.
\]

Let its Mellin transform be

\[
M_\rho(z)=\int_0^\infty\rho(x)x^{z-1}dx.
\]

The normalization implies

\[
\operatorname{Res}_{z=0}M_\rho(z)=1.
\]

Define the regulated Euler detector

\[
Z_{\rho,\varepsilon}(s)
=\sum_{n\ge1}n^{-s}\rho(\varepsilon n^2).
\]

Mellin inversion gives

\[
Z_{\rho,\varepsilon}(s)
=\frac1{2\pi i}\int
M_\rho(z)\varepsilon^{-z}\zeta(s+2z)\,dz.
\]

## Two decisive residues

Moving the contour crosses two structurally different poles.

The pole of \(\zeta(s+2z)\) at

\[
z=\frac{1-s}{2}
\]

produces the regulator-dependent boundary current

\[
B_{\rho,\varepsilon}(s)
=\frac12M_\rho\left(\frac{1-s}{2}\right)
\varepsilon^{(s-1)/2}.
\]

The pole of (M_\rho\) at (z=0\) has residue one and produces the universal
constant term

\[
\zeta(s).
\]

Poles at negative integers produce positive powers of \(\varepsilon\). Hence

\[
\operatorname{FP}_{\varepsilon\downarrow0}
\left[Z_{\rho,\varepsilon}(s)-B_{\rho,\varepsilon}(s)\right]
=\zeta(s)
\]

for every regulator in the normalized Mellin class, wherever the contour
argument and asymptotic expansion are valid.

## Gaussian and exponential controls

For \(\rho_\pi(x)=e^{-\pi x}\),

\[
M_{\rho_\pi}(z)=\pi^{-z}\Gamma(z).
\]

For \(\rho_1(x)=e^{-x}\),

\[
M_{\rho_1}(z)=\Gamma(z).
\]

Their divergent boundary coefficients differ by
\(\pi^{-(1-s)/2}\), but both Mellin transforms have residue one at zero, so
their relative finite parts agree exactly.

Thus changing the regulator together with its correctly derived boundary
current is allowed within this class. Changing the boundary current alone, or
adding a finite counterterm, remains unauthorized and changes the detector.

## Failure modes

1. **Wrong normalization:** if \(\rho(0)=c\ne1\), the constant term is
   (c\zeta(s)\).
2. **Unmatched subtraction:** using the Gaussian boundary term with a
   non-Gaussian regulator leaves a divergent residual.
3. **Finite counterterm:** subtracting (B_{\rho,\varepsilon}+h(s)\) changes
   the finite part to \(\zeta(s)-h(s)\) and can manufacture a divisor.
4. **Non-Mellin regulator:** insufficient decay or uncontrolled singularities
   require a separate theorem.
5. **Scalar cancellation:** regulator universality does not constrain where
   the universal finite part vanishes.

## Consequence

The relative Euler detector is not a Gaussian artifact. Its constant term is
fixed by two source facts: the Euler pole and the unit boundary value of the
regulator. This closes a bounded regulator-independence question.

It does not advance the remaining scalar theorem beyond a canonical
formulation. Off-seam divisor avoidance/nonvanishing of the completed finite
part is still equivalent to the unresolved RH content in the half-strip.
“Transversality” is not the correct term because a transverse zero remains a
zero.

## Claim strength

Conditional Mellin-asymptotic theorem for a normalized regulator class. No
nonvanishing, RH, or arbitrary regularization-independence claim is made.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_regulator_universality.py`.
The result is written to
`research/kitaev/results/theta-regulator-universality.json`.
