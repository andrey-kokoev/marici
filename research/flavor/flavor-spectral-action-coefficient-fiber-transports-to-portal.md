# Spectral-Action Coefficient Fiber Transports to the Portal

## Question

Can the primitive current and WP837 reflection determine the interacting
action, or can spectral-action coefficient freedom propagate all the way to
the portal magnitude?

## Frozen finite geometry

Retain the same primitive current and normalized reflection throughout:

\[
q=(1,2,3)^T,\qquad
H_q=I-2\frac{qq^T}{q^Tq},\qquad
D_m=mH_q.
\]

For every positive (m), the WP836 shape functional gives (R_3(D_m)=3).
Thus the current, completion, mixing orientation, and scale-free spectral
shape are identical data for the present comparison.

## Polynomial spectral-action fiber

The two-moment polynomial action is

\[
S_{\alpha,\beta}(m)
=\alpha\operatorname{Tr}(D_m^TD_m)
+\beta\operatorname{Tr}((D_m^TD_m)^2)
=3\alpha m^2+3\beta m^4.
\]

For \(\alpha<0\) and \(\beta>0\), its positive stationary minimum obeys

\[
m_*^2=-\frac{\alpha}{2\beta}.
\]

The coefficient packets ((\alpha,\beta)=(-2,1)) and ((-4,1)) therefore
select (m_*^2=1) and (2), respectively, while leaving (q) and (H_q)
unchanged. The second derivative at either nonzero stationary point is
(-12\alpha>0).

## Transport into the fixed-point magnitude

To test the missing WP838 arrow rather than merely exhibit a mass ambiguity,
let the same source interface feed the selected spectral invariant into the
gauge coefficient

\[
c=2+m_*^2,
\]

while (a=b=d=f=1). The coupled fixed point is then

\[
x_*=y_*=\frac1{c-1}=\frac1{1+m_*^2}.
\]

The two spectral actions produce (x_*^{(A)}=1/2) and
(x_*^{(B)}=1/3), hence positive portals (1/\sqrt2) and (1/\sqrt3).
This is an exact transport of action-coefficient freedom into the predicted
portal magnitude. It is not a claim that (c=2+m^2) is the physical flavor
matching law; it is the smallest hostile showing that a matching law cannot
repair unselected action coefficients.

## Source-principle consequence

A finite spectral packet does not determine which function of its spectrum is
the action. Declaring “the spectral action” without deriving its cutoff
profile or moment ratios leaves a family of distinct dynamics over the same
geometry. Stationarity then selects only relative to that freely supplied
functional.

Therefore the first missing WP838 arrow refines to

\[
(I,Q,H_q)
\longrightarrow
(f,\text{ normalization},\mathcal A_f)
\longrightarrow
\beta(\mathcal A_f).
\]

The source must derive the spectral-action profile and normalization before
its beta coefficients have selection authority. Even that would fix only a
dimensionless stationary ratio; an absolute threshold still requires a
source-derived clock or transmutation boundary, and threshold survival and
instrument realization remain separate gates.

## Verdict

Negative source-map result. WP836 and WP837 constrain the finite carrier but
do not determine its interacting action. The smallest exact falsifier is the
pair of coefficient packets above: identical primitive current, normalized
reflection, completion, and scale-free shape; distinct stable spectral minima
and distinct portal magnitudes.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp839_spectral_action_coefficient_fiber.py
```
