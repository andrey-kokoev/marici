# Strict and weak readings of `2(2+1)+1`

## First move: presentation versus diagnostics

A length-two additive presentation consists of three typed objects, two maps,
and one chain condition:

\[
X_0\xrightarrow{d_0}X_1\xrightarrow{d_1}X_2,
\qquad
d_1d_0=0.
\]

This is the minimal constructor inventory summarized by `3+2+1`.

Applying kernel and cokernel diagnostics to each map yields

\[
(\ker d_0,d_0,\operatorname{coker}d_0),
\qquad
(\ker d_1,d_1,\operatorname{coker}d_1).
\]

Adding the composite residual

\[
\kappa=d_1d_0
\]

gives the seven-slot diagnostic packet summarized by `2(2+1)+1`.

The seven-slot packet is not a second ontology.  Kernels and cokernels are
functorial readouts of the two maps.  It is an enriched audit of the
constructor packet.

## Second move: obstruction is not filler

The last slot has two incompatible readings.

In the strict reading, it records the equation

\[
\kappa=0.
\]

No additional filler is needed because the source requires literal chain
closure.

In the obstructed reading, the same slot records a nonzero value

\[
\kappa\neq0.
\]

Merely storing this value does not repair the complex.  A separately typed
null-homotopy or correction cell is required, and it must satisfy an explicit
boundary equation.  Therefore a weak packet that retains both obstruction and
repair has the schematic count

\[
2(2+1)+2,
\]

not `2(2+1)+1`.

The extra two slots are the computed obstruction and the authorized filler.
If the obstruction is treated as implicit, one may count only the filler, but
the types must remain distinct.

## Third move: ordinary associativity stops one regress

For three composable residuals, define

\[
\kappa_{10}=d_1d_0,
\qquad
\kappa_{21}=d_2d_1.
\]

Their compatibility residual is

\[
d_2\kappa_{10}-\kappa_{21}d_0.
\]

In an ordinary additive category this vanishes identically by associativity:

\[
d_2(d_1d_0)-(d_2d_1)d_0=0.
\]

Thus a new associator tower is not required for strict linear maps.  The
ambient category already supplies it.

This is a genuine termination theorem for that coherence direction.  Higher
data reappear only when composition is weak, projective, domain-dependent, or
defined up to homotopy.

## Fourth move: the magnetic instantiation is incomplete

The magnetic work currently supplies individual boundary matrices, their
kernels, cokernels, Smith data, and chart comparisons.  It does not yet supply
a source-derived pair

\[
d_0,d_1
\]

whose composite is the proposed coherence curvature.

Therefore `2(2+1)+1` is presently a compiler architecture for magnetic
comparisons, not an instantiated theorem about the magnetic operator tower.
The next substantive task is to identify two actual source maps and verify
their domains before computing \(d_1d_0\).

## Deutschian conjecture

> In a strictly additive source sector, the seven-slot diagnostic packet is
> complete for two consecutive comparisons: kernels and cokernels diagnose
> each map, and the vanishing composite supplies strict coherence.  A nonzero
> composite is a falsifier, not a filler.  Additional higher cells are required
> only after the source weakens strict composition.

This conjecture is proved for ordinary module maps and remains conditional for
the magnetic source until its consecutive comparison maps are constructed.
