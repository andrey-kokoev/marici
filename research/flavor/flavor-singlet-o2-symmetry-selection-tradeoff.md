# Singlet O(2) symmetry versus CP selection

Work package: WP594  
Owner: marici.Figueiredo

## Ward-identity candidate

WP593 shows that adding the CP modulus enlarges the closed radial quartic basis
to fifteen coordinates. The strongest symmetry compatible with the shared
gauge-singlet typing of \(\sigma\) and \(s\) is an \(O(2)\) rotation of
that pair, with CP embedded as a reflection.

Under this symmetry the pair appears only through

\[
S=\sigma^2+s^2.
\]

The radial quartic basis then contains ten coordinates: \(S^2\), three leaf
self-quartics, three leaf-pair portals, and three \(S\)-leaf portals. Thus
the Ward identity removes five of WP593's fifteen radial coordinates.

## Selection failure

The symmetric singlet potential is

\[
V_0={\lambda\over4}(\sigma^2+s^2-a^2)^2.
\]

Its vacuum is the circle

\[
\sigma^2+s^2=a^2.
\]

That circle includes the CP-conserving point \((\sigma,s)=(a,0)\) as well
as CP-broken points. Its Hessian has one positive radial eigenvalue and one
zero angular eigenvalue. The symmetry therefore relates coefficients but does
not select a CP orientation.

This is a direct hard-to-vary conflict: the continuous symmetry strong enough
to remove the normalization coordinates also makes the desired orientation
continuously variable.

## Minimal anisotropic repair

Add the positive term

\[
V_1={\kappa\over4}(s^2-\chi\sigma^2)^2.
\]

The two zero-energy conditions select

\[
{s^2\over\sigma^2+s^2}={\chi\over1+\chi}.
\]

But the result responds continuously to \(\chi\). The equally typed values
\(\chi=1\) and \(3\) select fractions \(1/2\) and \(3/4\). Breaking
the symmetry restores directional selection by restoring an unexplained
coefficient.

## Deutschian disposition

The continuous Ward-identity route cannot simultaneously provide:

1. coefficient reduction by singlet rotation symmetry;
2. exclusion of the CP-conserving vacuum;
3. a numerical CP/flavor-clock ratio.

The symmetric branch predicts a massless angular singlet mode and permits
\(J=0\). Those are independently criticizable physical consequences, but
they refute rather than confirm it as the desired flavor explanation.

A progressive architecture needs directional anisotropy derived from discrete
representation data, an explicit anomaly, or another source theorem that
fixes \(\chi\). Only after that derivation can joint CP-invariant and
scalar-pole measurements test the numerical relation.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp594_singlet_o2_symmetry_selection_tradeoff.py

The generated result is
research/flavor/results/wp594_singlet_o2_symmetry_selection_tradeoff.json.
