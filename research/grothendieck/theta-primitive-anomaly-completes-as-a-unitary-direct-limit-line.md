# Theta primitive anomaly completes as a unitary direct-limit line

## Finite-cutoff boundary lines

Let the directed set consist of finite prime cutoffs.  For each cutoff `X`,
take a one-dimensional boundary Hilbert line

\[
 L_X\simeq\mathbb C.
\]

For `X<Y`, define the source transition

\[
 \boxed{
 U_{X,Y}(s)=\prod_{X<p\le Y}\gamma_p(s):L_X\to L_Y.}
\]

Finite Euler reconstruction gives the exact cocycle law

\[
 U_{Y,Z}U_{X,Y}=U_{X,Z},
 \qquad U_{X,X}=1.
\]

No infinite Euler product is used.

## Seam completion

On the critical seam,

\[
 |\gamma_p(1/2+it)|=1.
\]

Therefore every `U_(X,Y)` is unitary.  The Hilbert direct limit

\[
 \boxed{
 L_{\rm seam}=\varinjlim_X(L_X,U_{X,Y})}
\]

exists, even though the scalar coordinates

\[
 \prod_{p\le X}\gamma_p(1/2+it)
\]

need not converge relative to one fixed copy of `C`.

The distinction is exact:

\[
 \boxed{
 \text{nonconvergent scalar trivialization}
 \ne
 \text{nonexistent line-valued limit}.}
\]

## Primitive and square anomaly coordinates

Using the connected decomposition,

\[
 U_{X,Y}
 =\exp\left(
 \Delta C_{1;X,Y}+\Delta C_{2;X,Y}
 \right)U_{\ge3;X,Y}.
\]

The primitive and square currents are therefore transition cocycles of the
line system.  They are not required to converge as absolute scalar
coordinates.  The trace-class tail supplies an ordinary convergent local
trivialization, while `C_1,C_2` record how those trivializations change.

Equivalently, compatible affine coordinates obey

\[
 c_Y=c_X+\Delta C_{1;X,Y}+\Delta C_{2;X,Y}.
\]

This is the explicit anomaly torsor over the restricted-product trace space
of packet 173.

## Distinguished transported state

Choose the unit vector `1` in one initial cutoff line and transport it through
the `U_(X,Y)`.  Its equivalence class in `L_seam` is well-defined and has norm
one.  No choice of a limiting scalar phase is necessary.

Changing the initial vector multiplies the entire line by one constant unit;
it does not change the transition cocycle or introduce a divisor.

## Fourier--Tate action

Reciprocal sheet exchange sends the local transition to its inverse/conjugate
on the seam.  Hence it acts by an antiunitary or dual-line correspondence on
the direct system, depending on the fixed real-structure convention.  The
cocycle law guarantees compatibility with cutoff inclusions.

The exact choice between dual and conjugate line must be frozen with the
global Haar and Fourier normalization; no scalar phase is inserted here.

## Compiler consequence

The completion-sensitive primitive operation is now well typed:

- `domain_after`: the restricted-product trace object together with the line
  system `{L_X,U_(X,Y)}`;
- `boundary_delta`: `Delta C_1` and `Delta C_2` as transition cocycles;
- `completion_scope`: unitary direct limit on the critical seam;
- `residual_capability`: retains nonconvergent prime phases without assigning
  them a false scalar sum.

Thus the primitive divergence does not obstruct seam completion.  It
obstructs only a global scalar trivialization.

## Scope boundary and next gate

Every transition is invertible, so this line system cannot itself produce a
zero.  Zeros still belong to a distinguished scalar pairing or section after
the line is coupled to the archimedean/Tate trace object.

Off the seam, the local transitions are not unitary in the seam metric.  The
next theorem must derive the two sector metrics and determine whether the
same directed system is bounded/closable there.  That metric comparison is
the natural input for the seam return operator, not convergence of the raw
Euler phase.
