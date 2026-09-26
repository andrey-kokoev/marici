# An unwrapped, orientation-transported angular clock

Active SCC obligations: attachment transport and readout descent. Inputs are
freshly read from `retained-rotor-phase-transport.md`: the declared Clifford
module, its continuous rotor enlargement, the phase connection with scale kappa,
and full retained histories. None of the native algebra/metric selection gaps
is assumed closed.

## Extract a reading from the constructed phase lift

The previous leaf defined F=(qp+sz)/2 and phi=psi+F/kappa, where psi is the
module's circle-valued angle. On a chosen real lift of that angle, define

\[
T=F/\kappa-\varphi=-\psi.
\]

For a rotor trajectory, the previously derived equations give

\[
\frac{dF}{d\theta}=p^2-q^2,
\qquad
\frac{d\varphi}{d\theta}=\frac{p^2-q^2-C}{\kappa},
\qquad
\frac{dT}{d\theta}=C/\kappa.
\]

The defining-module-compatible normalization C=kappa therefore gives unit
angular rate. The earlier C=0 phase prescription would make this reading
constant. This is a dimensionless phase-frame clock relative to the constructed
angular flow, not a calibration of physical seconds.

Consistent changes of the primitive and phase chart, F -> F+kappa*chi and
phi -> phi+chi, leave T unchanged. A choice of initial lifted phase still fixes
an arbitrary clock origin. The full history must remain present: T is not a
faithful history encoding and is not a function of the coarse observable Q.

## Reversals transport the clock affinely

Write a lifted transformation as g=(theta,e), representing U(theta)*e1^e, and
let o(g)=(-1)^e. Direct substitution into the checked phase-lift formula yields

\[
T\longmapsto o(g)T+\theta.
\]

On real angular lifts, composition is

\[
(\theta,e)(\eta,d)
=(\theta+(-1)^e\eta,\ e\mathbin\oplus d).
\]

Consequently its translation reading tau obeys

\[
\tau(gh)=\tau(g)+o(g)\tau(h).
\]

Ordinary addition is recovered on orientation-preserving rotor histories.
With reversers present, the comparison must carry orientation. There is an
algebraic obstruction to an ordinary additive real clock on the entire group:
a reflection r conjugates every rotation u to its inverse. An additive
homomorphism would have c(rur)=c(u) but also c(u inverse)=-c(u), hence c(u)=0.
Since r squared is identity, c(r)=0 as well. This argument applies even to the
unwrapped rotor/reverser group and does not require continuity.

The continuous orientation-twisted cocycles on that unwrapped group have form
A*theta+B*e: restriction to real rotations is additive and continuous, and the
reflection determines B. A is an angular scale; changing the clock origin
changes B. The constructed module chart gives A=1 and B=0 for the reference
reflection. It does not provide a physical time unit or a preferred future.

## Why retained path data are needed

The signed matrix group returns after 2*pi; its adjoint returns after pi.
Neither return erases the nonzero unwrapped angle. Therefore T cannot descend
to a real-valued clock on either endpoint group. A real lift requires a
continuous phase path and a starting lift, or explicitly chosen angular lifts
for the primitive operations. A discrete word alone supplies neither choice.

This is visible without numerical approximation. In units of pi/2 choose

\[
L=(0,1),\qquad R=(-1,1).
\]

They project exactly to the existing e1,e2. The word (LR)^2 has reading 2 and
matrix -1, while (LR)^4 has reading 4 and matrix +1. The empty word has reading
zero. Conversely LL and the empty word both have reading zero but remain
distinct histories.

A second choice R=(3,1) gives the SAME matrix e2 but changes the reading of LR
from 1 to -3. The difference is a full winding. Declaring a shortest-path or
principal-angle convention would add a selection rule; it is not information
already contained in the primitive word tag. Raw words and interpolation
choices must both remain visible.

The integer winding record is itself orientation-transported. Using residues
r in {0,1,2,3} for the signed endpoint angle, composition has a carry

\[
\nu(g,h)=\frac{r_g+o(g)r_h-r_{gh}}{4}.
\]

It satisfies

\[
\nu(g,h)+\nu(gh,k)
=o(g)\nu(h,k)+\nu(g,hk).
\]

All 512 signed-endpoint triples are checked exactly. A reflection sends winding
n to -n. Treating the winding as an untransported central scalar would therefore
be wrong. This is separate from the central sign extension of the finite action
group considered in earlier leaves.

## A signed reading is not nonnegative elapsed duration

On a supplied piecewise-smooth rotor path one can also define its angular
variation

\[
\ell(\gamma)=\int_\gamma |dT|.
\]

It is additive on concatenated paths, unchanged under reversal of orientation,
and invariant under subdivision and monotone reparameterization. It differs
from net T change: going out by one angular unit and returning has net zero
but variation two. It does not survive arbitrary backtrack deletion or general
endpoint-preserving homotopies. Thus any physical readout using it must declare
which history comparisons preserve duration rather than infer that from endpoint
agreement. This quantity measures angular distance, not calibrated time.

An odd operation is a frame-reversing transformation, not a continuous rotor
path from identity. No execution duration for such an operation is supplied by
this variation formula. It would require its own physical path/protocol data.

## HJ and continuation boundary

Along a chosen lifted rotor history T-T0=theta. The previously checked HJ
functions can therefore use that reading in place of the angular parameter:

\[
\partial_T S+(\partial_qS)^2+q^2+\kappa=0.
\]

This is a reparameterization by the retained module phase, not a new local
quantum equation. The construction establishes an affine angular clock only
within the specified realization. The unwrapped path, module, metric, observer
access to a phase reference and physical calibration are not native-source
consequences demonstrated here.

The next existing frontier is `nima-retained-analytic-source-audit-v1`:
identify which actual source constructors authorize those choices, especially
the response-to-implementer identification isolated by Voevodsky's source
algebra audit. Further endpoint algebra alone cannot manufacture a missing
clock-observation or continuous-path policy.

Verification:

```text
uv run --with sympy python research/aspect/scc/scc.py check nima-retained-rotor-history-clock
```

The checker verifies universal angle/parity identities symbolically, every
positive source word through length eight against the existing matrix reader,
the winding cocycle, chart-gauge cancellation, rate extraction and duration
controls. The continuous-cocycle classification and path-lifting requirements
are the mathematical arguments above, not a new Agda formalization. Receipt:
`results/retained-rotor-history-clock.json`.
