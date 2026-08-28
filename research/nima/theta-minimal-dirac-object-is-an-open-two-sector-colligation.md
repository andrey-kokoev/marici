# The Minimal Theta Dirac Object Is an Open Two-Sector Colligation

## Construction order

Begin with the reciprocal source-tail equations in the centered coordinate

\[
z=r+it,
\qquad
r=\operatorname{Re}(s)-\frac12.
\]

Keep the common source amplitude as an input port.  Do not homogenize it into
the transported state.  With

\[
\psi=\begin{pmatrix}u\\v\end{pmatrix},
\qquad
\Gamma=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
Bc=-\begin{pmatrix}f_+c\\f_-c\end{pmatrix},
\]

the doubled flow is

\[
\psi'=-it\psi-r\Gamma\psi+Bc.
\]

The normal coordinate is therefore already a pure first-order mass on the
transported state:

\[
\Gamma^* = \Gamma,
\qquad
\Gamma^2=I.
\]

No spectral jet tower is required to obtain linear dependence on $r$.

## Why the earlier homogeneous state was misleading

Adjoining $c$ to the state gives the normal coefficient

\[
\operatorname{diag}(1,-1,0),
\]

which is a projection on the tail coordinates rather than an involution on
the full carrier.  That failure is caused by collapsing an input port into a
state coordinate.  A positive-metric adjoint completion would then make the
supposedly constant input dynamical and cease to realize the native forced
equation.

The correct object is an input-state-output system:

```text
common source input -> two-sector tail spinor -> two local response outputs
```

## Common and relative responses

The two source-local adjoint outputs are

\[
y_+=-\overline{f_+}u,
\qquad
y_-=-\overline{f_-}v.
\]

In the reciprocal common frame, retain both output characters:

\[
y_\Sigma=y_++y_-,
\qquad
y_\Delta=y_+-y_-.
\]

The completed scalar endpoint readout uses the common character.  The Green
forcing defect uses the relative character.  Applying the codiagonal before
forming $y_\Delta$ erases the relationship state.

## Exact port balance

Define the positive state energy and signed flux

\[
N=\psi^*\psi,
\qquad
J=\psi^*\Gamma\psi.
\]

The seam term $-itI$ is skew-adjoint and contributes no real power.  Direct
differentiation gives

\[
J'=-2rN+2\operatorname{Re}(c^*B^*\Gamma\psi).
\]

Hence

\[
2rN=-J'+2\operatorname{Re}(c^*y_\Delta),
\]

up to the fixed sign convention identifying $y_\Delta=B^*\Gamma\psi$.

The previously unresolved doubled Green term is therefore not a failure of
the mass grading.  It is power through an open relative port.

## Dirac conclusion and remaining constructor

The two-sector tail already supplies:

- the minimal spinor $\psi=(u,v)$;
- the mass involution $\Gamma$;
- the two mass signs $r>0$ and $r<0$;
- the massless seam $r=0$;
- a positive state energy $N$;
- a relative response carrying the exact forcing defect.

What it does not yet supply is a lossless termination of the relative port.
To force $r=0$ for a nonzero two-ended zero state, the source must construct
a boundary reservoir with storage $S$ satisfying

\[
S'=-2\operatorname{Re}(c^*y_\Delta)
\]

and with vanishing total endpoint flux on the completed zero domain.  Then

\[
2rN=-\partial_q(J+S),
\]

and integration forces $r=0$ whenever the completed state energy is finite
and nonzero.

The moving-seam and source-primitive constructions are candidates for this
termination.  They must be treated as a boundary reservoir or outer mate,
not as extra additive bulk energy and not as duplicated Euler-current state
channels.

## Finite falsifier

At cutoff $X$, derive the input column $B_X$, local response pair
$C_{+,X},C_{-,X}$, mass involution $\Gamma_X$, and proposed reservoir
incidence.  The route fails at the first cutoff where any of the following is
nonzero:

\[
\Gamma_X^2-I,
\qquad
C_{\pm,X}-B_{\pm,X}^*,
\]

or

\[
\partial_qS_X+2\operatorname{Re}(c^*B_X^*\Gamma_X\psi_X).
\]

The last expression is the decisive closure residual.  Scalar cancellation
after summing sectors cannot repair a nonzero typed residual.

## Status

The smallest source-derived first-order carrier has been identified.  It is
an open two-sector Dirac colligation, not a closed homogeneous spinor.  The RH
content has moved to one source question: whether the relative response port
has an exact, completion-stable, lossless boundary termination.

## Attempted lossless termination

The completed theta source supplies a direct ternary candidate.  For seam
position $L$, ordered separation $d$, and centered spectral parameter
$z$, define

\[
W_L(d)=2\int_0^L\Phi(q)\Phi(q+d)\,dq
\]

and

\[
\mathcal K_L(z)=\int_0^\infty W_L(d)\sinh(zd)\,dd.
\]

Differentiation at the moving boundary gives

\[
\partial_L\mathcal K_L(z)
=\Phi(L)\bigl(H_+(L,z)-H_-(L,z)\bigr).
\]

After the fixed response-sign normalization, this is precisely the local
relative-port power in the doubled Green identity.  The ternary window
therefore provides the missing local storage derivative without introducing
the nonterminating binary primitive tower.

Arithmetic translations also act coherently.  For an admitted seam increment
$a$, put

\[
\delta_a\mathcal K_L=\mathcal K_{L+a}-\mathcal K_L.
\]

Then

\[
\delta_b\mathcal K_{L+a}+\delta_a\mathcal K_L
=\delta_{a+b}\mathcal K_L,
\]

so prime and prime-power seam moves telescope independently of their binary
factorization order.  This closes the local current and its finite path
coherence.

## Endpoint no-go

Local storage does not imply lossless global termination.  We have

\[
\mathcal K_0(z)=0,
\]

while the completed endpoint

\[
\mathcal K_\infty(z)
=2\int_0^\infty\int_0^\infty
\Phi(q)\Phi(q+d)\sinh(zd)\,dd\,dq
\]

is the oriented autocorrelation current.  At a zero of the scalar completed
transform, its normal component has the strict sign opposite to
$\operatorname{Re}z$.  Consequently

\[
X(z)=0,
\qquad
\operatorname{Re}\mathcal K_\infty(z)=0
\]

forces

\[
\operatorname{Re}z=0.
\]

The converse interpretation is decisive: a law asserting vanishing of this
endpoint current at every scalar zero is already equivalent to zero
confinement.  It is not supplied by the local port balance, positivity of the
source, ternary arity, arithmetic path coherence, or autocorrelation
completion.

A two-atom positive source gives the finite falsifier.  With weights $1,2$,
the scalar transform has the off-seam zero

\[
z=-\log 2+i\pi,
\]

while its oriented autocorrelation current equals $3$.  It satisfies the
local moving-seam construction but not lossless endpoint termination.

## Revised disposition

The direct ternary window closes the relative port locally and coherently.
The attempted global Dirac closure stops at a source-specific endpoint law.
The next admissible advance cannot be another autocorrelation identity,
because the completed autocorrelation is reconstructed from scalar boundary
modulus and cannot select a spectral factor from its reciprocal mate.

The remaining candidate must retain phase before scalar aggregation.  In the
current source architecture that means testing the unaggregated bilateral
valuation/Weyl boundary module for a boundary selector compatible with both
complementary transports.  Such a selector would have to imply the endpoint
law rather than assume it.
