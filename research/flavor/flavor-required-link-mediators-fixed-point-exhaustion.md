# Required link mediators fixed-point exhaustion: WP738

## Question

Can the vectorlike mediators already required to generate Standard Model
Yukawas across the two product-group sites repair WP737's missing magnitude
selector without adding optional spectator matter?

## Required renormalizable completion

Keep the WP736 parent assignments and add three vectorlike (B)-site quark
doublets (X_Q) and lepton doublets (X_L). With the bifundamental link
(Omega), the required interactions are

\[
\bar Q_A\Omega X_{Q,R},\qquad
\bar L_A\Omega X_{L,R},\qquad
\bar X_{Q,L}\widetilde H_Bu_R,\qquad
\bar X_{Q,L}H_Bd_R,\qquad
\bar X_{L,L}H_Be_R.
\]

Integrating out the vectorlike doublets generates the ordinary Standard Model
Yukawa operators after diagonal breaking. These fields are therefore demanded
by the source grammar exposed in WP736; they are not added solely to alter beta
functions.

An official PyR@TE 3 calculation at revision
`04b219c2016f3fc4f2371d72607edc26a7e06364` verifies gauge invariance and gives
the one-loop gauge coefficients

\[
B_1=\frac{51}{2},\qquad
B_A=1,\qquad
B_B=\frac{31}{6},\qquad
B_3=-3
\]

in its beta-function sign convention. Hypercharge and both product-group
factors now require interacting ultraviolet zeros; color may remain Gaussian.

## Exact branch system

Take all six Yukawa matrices proportional to the three-flavor identity and
write their squared rescaled couplings as

\[
(k,q,l,u,d,e)
=(\alpha_{\kappa_U},\alpha_{\lambda_Q},\alpha_{\lambda_L},
\alpha_{\lambda_U},\alpha_{\lambda_D},\alpha_{\lambda_E}).
\]

Their one-loop nullcline brackets are the exact linear equations

\[
\begin{aligned}
0={}&15k+2l+18u+18d+6e
-\frac{15}{2}a_1-9a_A-\frac92a_B,\\
0={}&22q+6l-\frac13a_1-16a_3-\frac92a_A-\frac92a_B,\\
0={}&10l+18q+2k-3a_1-\frac92a_A-\frac92a_B,\\
0={}&12k+21u+15d+6e-\frac{17}{6}a_1-16a_3-\frac92a_B,\\
0={}&12k+15u+21d+6e-\frac56a_1-16a_3-\frac92a_B,\\
0={}&12k+18u+18d+9e-\frac{15}{2}a_1-\frac92a_B.
\end{aligned}
\]

The checker enumerates every active or inactive Yukawa subset. It also allows
the asymptotically free color factor to be interacting or Gaussian and, as a
hostile generosity check, allows (SU(2)_B) to be Gaussian. Hypercharge and
(SU(2)_A) remain active because their positive one-loop coefficients cannot
produce the observed nonzero low-energy interactions from an exact Gaussian
ultraviolet coordinate.

This yields

\[
4\times2^6=256
\]

exact linear fixed-point branches. Every branch is solved over the rationals
and checked for strict positivity of each declared active squared coupling.
The number of physical branches is zero.

On the fully interacting branch, the unique gauge solution already has

\[
a_3=-\frac{1747041281}{6918678948},
\qquad
a_B=-\frac{116978905}{2306226316},
\]

providing a small explicit hostile witness in addition to the exhaustive
count.

## Disposition

The source-required link mediators do increase Yukawa screening, but not enough
to create a physical 210 fixed point on any admitted branch. Consequently the
WP736 Clebsch mechanism still fixes only the matching sign and ratio. It does
not fix the magnitude or RG basin, so threshold and detector authority remain
unreached.

This result closes the minimal and compulsory-mediator product-group packets.
A successor needs a further source principle that independently requires new
Yukawa-active matter. Candidate matter cannot be selected by scanning until a
fixed point appears; its representation, multiplicity, masses, and couplings
must follow from anomaly cancellation, a parent simple group, compositeness,
or another declared physical necessity.

Reproduce with:
`uv run --with sympy python research/flavor/checkers/wp738_required_link_mediators_fixed_point_exhaustion.py`.

Generated result:
`results/wp738_required_link_mediators_fixed_point_exhaustion.json`.
