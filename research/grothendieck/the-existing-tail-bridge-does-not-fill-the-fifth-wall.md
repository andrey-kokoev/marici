# The existing tail bridge does not fill the fifth wall

## Scope correction

The previous reduction identified a sufficient categorical lift:

\[
\{X(z)=0\}\longrightarrow
\{(z,\psi):D\psi=z\psi,\ D^*=-D,\ \psi\ne0\}.
\]

The completed theta tails provide an exact zero-to-state bridge, but they do
not provide this lift.

## What the source actually constructs

After adjoining the constant forcing channel, the tail equation is

\[
\mathcal D_z\Psi=(D_0+zP)\Psi=0,
\qquad
P=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The scalar zero supplies the antidiagonal seam condition on the two reciprocal
tails. Thus it lands canonically in the solution incidence of a singular
pencil.

The desired fifth wall instead requires the spectral incidence of one fixed
skew-adjoint realization, whose parameter multiplies the identity on the
admissible state module. These are different categorical targets.

## Exact obstruction

The rank of (P) is invariant under invertible changes of source coordinates.
It cannot become the identity. Removing its null channel deletes the constant
source coordinate that produces the tail forcing. Completing the triangular
source coupling symmetrically adds a reverse incidence from the tail into the
source channel, changing the equations.

Therefore there is no source-authorized equivalence

\[
\mathcal E_{D_0+zP}\simeq\mathcal E_D
\]

available from the present tail construction.

This is the concrete obstruction behind the missing pullback: the scalar zero
does lift to a state, but the state has the wrong spectral type.

## Three legitimate continuations

Only three routes remain.

1. Prove a confinement theorem directly for a self-adjoint or skew-adjoint
   linear relation with singular weight (P), retaining its null channel.
2. Derive a new reciprocal source incidence that makes the constant channel
   dynamical and gives the completed system nonsingular spectral weight.
3. Eliminate the constant channel into a nonlocal boundary relation, then
   prove independently that this relation is the Weyl family of a fixed
   skew-adjoint carrier.

The second route is the most explanatory: the missing wall would be a genuine
reverse constructor, not an analytic repackaging. It also matches the recent
controllability lesson that an off-axis source incidence can enlarge closure,
whereas an aligned channel cannot.

## Falsifier

Any proposed repair fails if it merely changes basis, discards the null
channel, or inserts the reverse coupling after inspecting (X). The first
acceptable construction must derive the reverse incidence from labelled
theta/Tate operations and reproduce every original finite-cutoff tail equation
after projection.

## Status

The skew-adjoint incidence theorem remains an exact sufficient endpoint. The
existing tail augmentation does not meet its hypotheses. RH is not proved.

