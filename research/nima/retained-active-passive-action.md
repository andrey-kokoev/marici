# Moving-frame action: local freezing does not erase the retained phase

This tests the declared Clifford realization, connection and defining module
from `retained-rotor-phase-transport.md`. It does not turn the preceding Q^8
presentation transport into a selected Clifford product or native evolution.

## Pull back the whole action, not only the base coordinates

Write the moving coordinates as X=(s,u,v,z), and Q=T_theta X. Explicitly,

\[
q=u\cos(2\theta)+v\sin(2\theta),\qquad
p=v\cos(2\theta)-u\sin(2\theta).
\]

Use the previously defined F=(qp+sz)/2, beta=p*dq+s*dz and
Hplus=q^2+p^2+kappa. In moving coordinates set beta0=v*du+s*dz and
B(X,theta)=F(T_theta X)-F(X). The full space-time pullback is

\[
\Phi^*(\beta-H^+d\theta)=\beta_0+d(B-\kappa\theta).
\]

The time component of the pulled-back beta is NOT zero. More precisely it is
beta0+dB+(u^2+v^2)*dtheta, whose last term cancels the quadratic Hamiltonian.
The remaining constant is absorbed only by the full phase counterterm.

With phase coordinates related by

\[
\varphi=\chi+B/\kappa-\theta,
\]

the extended phase connection becomes

\[
\Phi^*(d\varphi-\beta/\kappa+H^+d\theta/\kappa)
=d\chi-\beta_0/\kappa.
\]

Thus the transformed Hamiltonian is zero and X,chi are stationary along the
specified lifted trajectory. The action has not simply vanished: its change
is the endpoint difference of B-kappa*theta. This exact boundary function is
also the required correction when transporting the earlier HJ charts. Any
initial-endpoint Legendre term remains a separate chart comparison, not a
license to discard this temporal boundary term.

## The observing apparatus must also be transported

For the SAME experiment, a fixed laboratory observable f(Q) becomes the
explicitly time-dependent observable f(T_theta X). For example a constant
moving state (u,v)=(1,0) gives laboratory q=cos(2theta), not constant q=1.
Using the latter would replace the laboratory observable by a comoving one.

Every sufficiently regular Hamiltonian flow can locally be frozen by adapting
coordinates to that flow. This neither proves that its original dynamics was
unphysical nor distinguishes active evolution from a presentation change.
That distinction requires specifying what measuring structure is physically
held fixed. The source admission problem therefore survives this calculation.

## The base-period frame is not a closed full phase frame

At theta=pi the base transformation is the identity and B=0, but

\[
\varphi=\chi-\pi,\qquad
B-\kappa\theta=-\kappa\pi.
\]

The retained module comparison is -1. At theta=2pi it is +1. The local phase
change exp(iB/kappa-i*theta) is antiperiodic over the base period pi; it is not
a single-valued phase gauge on that base-time circle. It can be used on the
unwrapped interval only if its endpoint transition is retained. Declaring the
moving phase constant AND identifying its endpoint frame with its starting
frame at pi would incorrectly erase that transition.

At 2pi the module reading returns, but the full unwrapped history still need
not equal the empty history. Thus coordinate freezing removes neither the
half-return sign nor the separately retained winding record.

This is the precise obstruction to treating the earlier constant action shift
as globally irrelevant in the retained phase model. It is not a derivation of
quantum interference, a Born rule or a calibrated physical energy.

## Checked result and continuation

The symbolic checker verifies all six coefficients of both space-time one-form
identities, the generator signs, laboratory/comoving observer distinction,
nine signed endpoint returns, and rejection of a base-only phase counterterm.

```text
uv run --with sympy python research/nima/checkers/check_active_passive_action.py
```

Receipt: `results/active-passive-action.json`.

Next local leaf: construct a relative-path phase comparator with common
endpoint frames and test its gauge covariance. State explicitly which extra
readout/recombination assumptions would be needed to make the retained sign
operational, rather than announcing an interference prediction. The independent
native product/readout owner gate remains open.
