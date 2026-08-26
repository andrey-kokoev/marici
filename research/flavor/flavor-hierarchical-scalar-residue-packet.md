# Hierarchical scalar pole, residue, and width packet

## Conditional endpoint domain

WP475 recomputes the radial spectrum at the exact WP474 kaon-conditioned
endpoint. It inherits all WP461 assumptions and sets `y=kappa=1`,
`f=f_min`, and

\[
a=3(v/f_{\min})^2.
\]

The Higgs mass is then used only to calibrate `eta`, as in WP471. It is not a
source-selection input for `g_F f/v`.

## Exact reduced Hessian

For canonical radial coordinates `(r_F,r_H,sigma)`, with `lambda=rho=1`, the
source potential gives

\[
R(a,\eta)=\begin{pmatrix}
106&2\sqrt{6a}&-98\sqrt3\\
2\sqrt{6a}&4a(\eta+1)&2\sqrt{2a}(1-2a\eta)\\
-98\sqrt3&2\sqrt{2a}(1-2a\eta)&302+8a^2\eta
\end{pmatrix}.
\]

Let

\[
\ell={2m_H^2\over v^2}.
\]

Demanding the eigenvalue `a ell`, which equals `m_H^2/w^2`, fixes

\[
\eta_H={\ell(a\ell-400)\over
4(2a^2\ell+a\ell-200a-400)}.
\]

This is positive at the admitted endpoint.

## Exact poles and residues

The radial spectrum factorizes into

\[
L_H=a\ell,qquad L_D=8+4a,qquad
L_+= {200(a+2)(a\ell-400)\over
2a^2\ell+a\ell-200a-400}.
\]

The exact Higgs-channel residues are

\[
Z_H={ (a\ell-400)^2\over
2a^3\ell^2+a^2\ell^2-400a^2\ell-800a\ell+80000a+160000},
\]

\[
Z_D={a\over a+2},
\]

and the remaining positive residue is fixed by completeness. At the WP474
endpoint, `Z_H` differs from one only near the `10^-16` level and exceeds the
frozen Higgs-rate lower edge.

The lifted and heavy radial poles lie at multi-PeV scales in detector units,
while the calibrated Higgs pole is exactly `125.20 GeV`. Thus no new radial
decay channel is open for the Higgs.

## Independently frozen leading Higgs width

On the mixing-only Standard Model decay domain,

\[
\Gamma_H=Z_H\Gamma_H^{\rm SM}.
\]

Using the independently quoted `4.10 MeV` Standard Model central width gives a
width essentially equal to `4.10 MeV`, compatible with the current direct
summary. This width is derived after the residue and is not used in the mass
calibration.

## Authority boundary

This is the first common-clock scalar packet simultaneously compatible with
the provisional kaon-current endpoint, Higgs mass, and Higgs rate/width
instruments. It is not a numerical selector: `f=f_min` and the 5-TeV vector
pole are conditional benchmark choices, while `eta` is detector calibrated.

The next gate is to recompute the flavor-vector current response and widths in
this same hierarchical scalar threshold domain, including whether any scalar
channel is open at the vector poles. A likelihood must retain the provisional
and benchmark labels explicitly.

