# Adjoint-mediator matching audit (WP127)

Owner: `marici.Figueiredo`.

## Bounded question

Can one source-side mediator generate the sign and coefficient of WP125's
degree-eight commutator selector, while passing WP126's causal-response gate?

Pre-objective process report: excitement `10/10`, confidence `8/10` in exact
matching and `5/10` that the smallest construction is a genuine renormalizable
UV completion, expected information gain `9/10`. The attraction is that
positivity of a heavy Gaussian field may fix the required sign. Confounds are
operator dimension, radial stability, and the distinction between an
auxiliary EFT field and a microscopic constructor. These reports are
non-evidential.

Frozen optionality snapshot: one Hermitian adjoint mediator; one exact
completion of the square; two source-parameter interventions; one scaling-ray
stability attack; one power-counting gate; ten exact checks.

## Candidate constructor and descent

Define the Hermitian weak-basis adjoint

\[
B=i[H_u,H_d],\qquad H_a=\Phi_a\Phi_a^\dagger,
\qquad K=\operatorname{Tr}(B^2)=\lVert[H_u,H_d]\rVert_F^2.
\]

Introduce a Hermitian `U(3)_Q` adjoint `X`, transforming by conjugation, with

\[
V_X=\frac{M^2}{2}\operatorname{Tr}(X^2)
+g\operatorname{Tr}(XB),\qquad M^2>0.
\]

Both terms descend under the full weak-basis group. The mediator equation is

\[
X_*=-\frac{g}{M^2}B.
\]

Completing the square gives

\[
V_X=\frac{M^2}{2}\operatorname{Tr}
\left(X+\frac{g}{M^2}B\right)^2
-\frac{g^2}{2M^2}K.
\]

Thus positive mediator mass fixes precisely the negative sign required by
WP125, with

\[
q=\frac{g^2}{2M^2}>0.
\]

For `(M^2,g)=(2,10)`, `q=25`; together with `a=28`, the construction
reproduces `sin^2(theta_*)=16/25` exactly.

## Causal fingerprint

After matching,

\[
x_* =\frac12+\frac{aM^2}{4g^2}.
\]

The upstream parameters therefore regenerate nontrivial downstream responses,

\[
\partial_gx_*=-\frac{aM^2}{2g^3},\qquad
\partial_{M^2}x_*=\frac{a}{4g^2}.
\]

At the exact benchmark these are `-7/250` and `7/100`. This is the WP126
intervention signature pulled one arrow upstream. Deleting `X` or setting
`g=0` removes the commutator selector rather than leaving its authority cached.

## Two decisive obstructions

This is not yet a renormalizable UV completion. In four dimensions,
`dim(X)=1` while `dim(B)=4`, so `Tr(XB)` is a dimension-five vertex and `g`
has negative mass dimension. Calling `X` a heavy mediator does not erase that
power-counting fact. The construction is an exact auxiliary-field
representation inside an EFT source class.

It is also radially unstable without further operators. Under
`Phi_a -> s Phi_a`, `C` scales as `s^4` and `K` as `s^8`. On WP125's
noncommuting hostile ray,

\[
V(s)=28\frac{643}{25}s^4
-25\frac{1152}{625}s^8,
\]

whose leading coefficient is `-1152/25`. Hence `V(s)->-infinity`. A positive
degree-eight radial completion can bound the EFT, but its coefficient and
effect on the full vacuum must be source-derived and rechecked.

## Disposition

WP127 establishes an exact, descending, sign-generating mediator match and
two upstream causal response derivatives. It upgrades the coefficient `q`
from an arbitrary sign choice to a positive square ratio. It does not derive
the numerical ratio `aM^2/g^2`, and therefore does not predict the angle.

Classification: **conditional auxiliary-adjoint EFT selector constructor**,
not a renormalizable UV constructor and not a physical instrument. No
reference port is required. The smallest exact physical obstruction is the
negative `s^8` coefficient on the hostile ray; the smallest authority
obstruction is the dimension-five mediator vertex. The next admissible search
is a renormalizable multi-mediator completion whose tree or loop matching
reproduces `-qK` together with a source-fixed stabilizer and coefficient ratio.

Post-objective process report: excitement `9/10`, confidence `10/10` in the
exact matching and `3/10` that this specific auxiliary model is fundamental,
realized information gain `10/10`. Raw delta: the required sign is derived;
two causal derivatives are constructed; one exact angle is reproduced; the
UV-constructor branch is retyped as EFT-only; one unbounded radial direction
is exposed; ten of ten checks pass; no physical instrument is added. These
reports are non-evidential.
