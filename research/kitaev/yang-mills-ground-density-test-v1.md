# Iteration 5 — the actual ground density acquires a connected plaquette term

## Question and disposition

Can one obtain a volume-independent detection estimate simply by treating the actual magnetic ground density as a local Wilson plaquette Gibbs density?

**No for that shortcut.** On the existing seven-link source, the exact second-order ground-state expansion distinguishes two physical configurations with identical individual plaquette traces. Its normalized log density therefore cannot be a function solely of those traces near zero coupling. This is an actual SU(2) source calculation, not a surrogate ground vector or another finite spin cutoff.

**Still open:** `faithful-excitation-detection`. A sufficient conditional variance theorem below identifies two missing volume-uniform estimates. Neither is inferred from the Taylor calculation. No net gate is closed merely by supplying a conditional implication.

[Contract](contracts/yang-mills-ground-density-test.v1.json). All earlier sources, vacua and their scope boundaries are retained.

## Fixed-source spectral perturbation

Use the two plaquettes sharing a link from iteration 2. Write p=Tr x, q=Tr y, S=p+q, F=pq, F0=Tr(x y inverse)/2, F1=F-F0 and C_p=p squared-1, C_q=q squared-1. Normalize L=H0/kappa and r=lambda/kappa. Then

\[
H/\kappa=L+2r-rS/2.
\]

The unperturbed physical vacuum is 1, simple, and its electric gap is 3. Bounded analytic spectral perturbation gives a real-analytic ground branch near r=0 at each fixed finite graph. Elliptic regularity upgrades the expansion to smooth functions, so the pointwise comparison below is legitimate. These are imported compact elliptic/analytic perturbation results; no uniform-in-volume convergence or formal-kernel proof is asserted.

For the algebra choose intermediate normalization <Omega>=1:

\[
\Omega(r)=1+ra+r^2b+O(r^3),\quad
\langle a\rangle=\langle b\rangle=0.
\]

Subtract 2r from the eigenvalue. Since <S>=0 and <S squared>=2, the first two perturbation equations are

\[
La=S/2,\qquad Lb=S a/2-1/6.
\]

Characters give Lp=3p, Lq=3q, L C_p=8 C_p, L C_q=8 C_q. The shared-link channels have L F0=(9/2)F0, L F1=(13/2)F1. Therefore the actual coefficient functions are

\[
a=S/6,\qquad
b=(C_p+C_q)/96+F_0/27+F_1/39,
\]

and the source energy is

\[
E_0/\kappa=2r-r^2/6+O(r^3).
\]

The negative second-order correction is consistent with min–max; it is not a negative ground-subtracted spectrum. All coefficients use the full electric operator on actual polynomial functions. There is no spin truncation in solving these two exact coefficient equations.

## Normalize the probability density before comparing it

The intermediate vector is not L2 normalized: <a squared>=1/18, so <Omega squared>=1+r squared/18+O(r cubed). For the actual probability density rho=Omega squared/<Omega squared>,

\[
\log\rho=\frac r3S+r^2\ell_2+O(r^3),
\]

\[
\ell_2=-\frac{C_p+C_q}{144}-\frac19
+\frac{F_0}{54}-\frac{F_1}{234}.
\]

The constant minus 1/9 is necessary for normalization at this order: <ell2>=-1/9 and <(S/3) squared>/2=1/9. Omitting the L2 normalization would produce the wrong constant, although the configuration difference below would remain unchanged.

Evaluate two configurations admitted by the same source:

    x=i, y=i: p=q=0, F0=1, F1=-1;
    x=i, y=j: p=q=0, F0=0, F1=0.

Their log-density difference is

\[
\log\rho(i,i)-\log\rho(i,j)
=\frac8{351}r^2+O(r^3).
\]

Analyticity and the nonzero leading coefficient imply an actual difference for all sufficiently small nonzero real r. It is not just a discrepancy of unverified finite approximants. Every density depending only on p and q assigns equal values to these configurations. In particular exp(c(r)(p+q)) and arbitrary products of separate plaquette weights fail to describe the actual ground density.

The constant part of log rho is immaterial to this witness, but the mixed-loop term is not. In terms of iteration 4's hidden invariant h=Tr(xy)-pq/2, the mixed contribution in ell2 is F/702-4h/351. Thus the very state missed by the individual-loop reader reappears in the actual ground density.

This rejects a single-plaquette Gibbs replacement. It does **not** prove arbitrarily long-range interactions in log rho, exclude useful connected local/cluster descriptions, or disprove a uniform spectral gap. The connected term here couples adjacent plaquettes only.

## A precise volume-independent sufficient criterion

Let nu be the actual normalized Omega squared Haar measure on the full finite link product. For each link e, condition on all other links. Suppose two source estimates hold with constants independent of volume:

1. Approximate tensorization: Var_nu f <= A times the sum over e of the expected conditional variance of f on link e.
2. Each conditional link density has log oscillation at most b0, uniformly over the conditioned links.

For the full SU(2) link, the Haar Poincare constant is 3/4 in our generator convention. It is **not** the physical loop constant 3: conditioning on the other links does not leave an independent physical four-link loop. Density comparison on each link gives a conditional constant at least (3/4) exp(-b0). Therefore

\[
\operatorname{Var}_\nu f
\le\frac{4A}{3}e^{b_0}
\sum_e\int|X_e f|^2d\nu.
\]

Set psi=Omega f and restrict to invariant functions. The already proved exact ground-form identity yields

\[
\|D_\Omega\psi\|^2\ge
\frac{3e^{-b_0}}{4A}\|(I-P_\Omega)\psi\|^2,
\quad
\Delta\ge\kappa\frac{3e^{-b_0}}{4A}.
\]

First prove this on the smooth core and then close the form. This is a genuine sufficient transfer theorem, not a source solution: neither approximate tensorization nor a uniform b0 has been established for the actual interacting family. The actual density's connected correction explains why importing Wilson-density estimates without a comparison theorem would be invalid.

At r=0 product Haar satisfies A=1 and b0=0. This criterion then yields the valid but nonsharp kinematic lower bound 3 kappa/4; the physical electric bound is independently 3 kappa. The distinction in constants is intentional.

## Why fixed-graph analyticity is not a uniform cluster result

On a box with P plaquettes, after subtracting the scalar rP, the perturbation is -r times the sum of fundamental traces divided by two, whose norm is at most |r|P. The unperturbed physical eigenprojection has a Neumann-resolvent sufficient condition |r|P<3/2 on the circle of radius 3/2 around zero. The associated eigenvector normalization is chosen analytically in a neighborhood of zero.

This sufficient isolation condition shrinks with volume. It says nothing decisive about the true maximal analytic domain; it also cannot justify exchanging this expansion with a thermodynamic limit. Connected coefficient computations must be supplemented by a uniform cluster/influence estimate. Repeating them at a larger finite spin cutoff or replacing P by its sampled value does not supply that estimate.

## Exact controls and boundary

The checker applies the actual seven-link second-jet Casimir to a and b independently and verifies both perturbation equations on rational quaternion fixtures. It separately verifies the normalized log-density algebra, the coefficient 8/351 at equal-trace configurations and the conditional-link versus physical-loop constant distinction. Haar normalization controls use exact quadratic moments. These finite regressions accompany the written analytic coefficient proof; the O(r cubed) claim rests on analytic perturbation, not fitted numerical samples.

The conditional criterion is also regressed on rational finite probability products by exact conditional variances and a weighted two-state analogue. Those controls are not estimates of the unknown interacting SU(2) density.

**Next executable operation:** seek a volume-local connected expansion or influence bound for the actual log ground density and test the two conditional premises. `faithful-excitation-detection`, `continuum-correlation-construction`, and the independent atomic-source branch remain open. No continuum or volume-uniform gap is claimed.

Reproduce: `python research/kitaev/checkers/check_yang_mills_ground_density_test.py`.
Receipt: `research/kitaev/results/yang-mills-ground-density-test-v1.json`.
