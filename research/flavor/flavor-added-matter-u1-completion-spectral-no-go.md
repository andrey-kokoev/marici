# The smallest bounded matter completion permits the flux but destroys its spectral basin: WP780

## Question

Can ordinary additional matter repair WP779 while making the common-sign
family flux compulsory and preserving the positive spectral mechanism?

## Smallest non-Abelian repair

Give every member of \(15+2\overline6\) charge \(+1\). Its mixed
\(SU(6)^2U(1)_F\) coefficient is

\[
2+\frac12+\frac12=3.
\]

The smallest nontrivial \(SU(6)\)-vectorlike representation pair is
\(6+\overline6\). Assigning both members charge \(-3\) cancels the mixed
coefficient:

\[
3+\frac12(-3-3)=0.
\]

Before adding singlets, the remaining linear and cubic coefficients require
singlet charges satisfying

\[
\sum_i s_i=9,
\qquad
\sum_i s_i^3=297.
\]

In the declared integer box \(|s_i|\le12\), no solution exists with one, two,
or three singlets. The first four-singlet solution is

\[
(s_1,s_2,s_3,s_4)=(-7,4,4,8).
\]

This packet cancels the ordinary mixed, gravitational, and cubic anomalies
exactly. The bounded minimality claim does not extend beyond the declared
charge box.

## Full flux cost

At flux \(m=3\), absolute Landau multiplicities weight every charged field.
The complete contributions are

\[
N_{\mathrm{family}}=27(3)=81,
\]

\[
N_{6+\overline6}=6(9+9)=108,
\]

\[
N_{\mathrm{singlets}}=21+12+12+24=69.
\]

Thus

\[
N_{\mathrm{matter}}=258.
\]

Including the \(SU(6)\times U(1)_F\) vector degrees gives the inherited
equal-weight diagnostic

\[
\kappa=2+36-258=-220.
\]

This is not a transported effective potential, but it is an exact spectral
cost falsifier: the ordinary-matter repair cannot preserve the positive
half-twist basin that motivated the source construction.

## No orientation or tadpole selection

All ordinary anomaly equations are invariant under reversal of every charge.
Primitive normalization removes common magnitude rescaling but not this
orientation pair. Moreover, gravitational anomaly cancellation makes the
total linear charge zero, so the completion does not provide
\(Q_{\mathrm{loc}}=-3c\).

## Classification

The added-matter branch permits common-sign family flux but does not make it
unavoidable. It leaves the global orientation choice, fails the tadpole gate,
and destroys the favorable spectral basin. The remaining sharply different
branch is a geometrically quantized Green--Schwarz constructor. It must fix
orientation and tadpole while avoiding a new flux-weighted chiral tower and
while retaining an executable low-energy \(U(1)_F\) probe.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp780_added_matter_u1_completion_spectral_no_go.py

Generated result:
research/flavor/results/wp780_added_matter_u1_completion_spectral_no_go.json
