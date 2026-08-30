# Control identifiability splits determinant output from characteristic transfer

## Correction

The statement that a scalar section cannot determine an ordered realization is
correct for determinant, trace, overlap, and other aggregate scalarizations.
It is too broad for a full scalar transfer function. Under minimality, a SISO
transfer can determine a finite realization up to similarity. Under stronger
conservative hypotheses, a scalar Sz.-Nagy--Foias characteristic function can
determine a completely nonunitary contraction up to unitary defect-port gauge.

The theta programme must therefore type the completed section before applying
either conclusion.

## Determinant observation sees only control abelianization

Consider the right-invariant switched system

\[
\dot U(t)=A_{u(t)}U(t),
\qquad
U(0)=I,
\]

with scalar output

\[
y(t)=\det U(t).
\]

Jacobi's formula gives

\[
\frac{d}{dt}\log y(t)
=
\operatorname{Tr}A_{u(t)}.
\]

Hence

\[
y(T)
=
\exp\left(
\int_0^T\operatorname{Tr}A_{u(t)}\,dt
\right).
\]

The determinant output depends only on the integrated traces of the applied
generators. It does not see their ordering. Every Lie bracket is invisible:

\[
\operatorname{Tr}[A,B]=0.
\]

Thus the determinant observation factors through the abelianization of the
control Lie algebra. Commutator motion, mode shear, and determinant-one
holonomy lie in its unobservable fiber.

This remains true even if the determinant is observed for every time and every
switching word. More experiments do not recover information annihilated by
the output homomorphism.

## Full transfer carries more information

For a finite state-space system

\[
\dot x=Ax+Bu,
\qquad
y=Cx+Du,
\]

the transfer function is

\[
G(s)=D+C(sI-A)^{-1}B.
\]

This is not merely \(\det(sI-A)\). It contains the ordered attachment of the
input port \(B\), internal dynamics \(A\), and output port \(C\).

If two finite realizations of the same rational \(G\) are both controllable
and observable, then they are similar. Therefore a full scalar transfer can
identify the minimal realization up to state-coordinate gauge.

Without controllability, unreachable state directions may be added. Without
observability, dark state directions may be added. Both additions preserve the
same transfer function.

## Characteristic-function closure

For a completely nonunitary contraction \(A\), its operator-valued
characteristic function

\[
\Theta_A(z):
\mathcal D_A\longrightarrow\mathcal D_{A^*}
\]

is a complete unitary invariant up to constant unitary identifications of the
incoming and outgoing defect spaces. When both defect spaces have dimension
one, this is a scalar analytic function up to two scalar port phases.

This is the legitimate control-theoretic route by which a scalar analytic
object can determine an ordered state model:

1. prove that the scalar is the full characteristic transfer, not a
   determinant or overlap;
2. prove complete nonunitarity or the corresponding simplicity condition;
3. retain both defect ports;
4. fix their source-authorized gauges;
5. construct the canonical model realization.

The result is uniqueness up to the admitted realization gauge. It is not
automatic physical authority for a particular actuator.

## Three distinct scalar types

The programme must not use the word “section” without selecting one of these
types.

| Scalar object | What it retains | Reconstruction strength |
|---|---|---|
| determinant or trace section | aggregate spectrum, volume, phase, divisor | does not recover ordered realization |
| distinguished matrix coefficient or overlap | one input-output channel | recovers only its cyclic subspace under additional hypotheses |
| full rank-one characteristic transfer | complete minimal input-state-output response | recovers a simple realization up to port gauge |

An analytic function may occupy more than one row only after an independently
derived theorem identifies the corresponding constructions.

## Theta/Tate decision gate

Let \(\Xi(s)\) be the completed theta/Tate scalar section. The next question is
not merely whether some operator has determinant \(\Xi\). It is which of the
following typed claims is source-derived:

\[
\Xi(s)=\det_{\mathrm{rel}}\mathcal L_s,
\]

\[
\Xi(s)=\langle c,(\mathcal A-s)^{-1}b\rangle,
\]

or

\[
\Xi(s)=\Theta_{\mathcal A}(s)
\]

after the declared half-plane normalization.

The first identity makes \(\Xi\) a diagnostic invariant. The second can
identify only the source-and-endpoint cyclic subspace. The third may close the
local realization orbit if minimality and both boundary gauges are proved.

At present the pinned full-Weyl characteristic function is not yet the framed
theta cross transfer. Therefore characteristic-function completeness cannot
be imported as authority for the missing tail–seam incidence.

## Minimal hostile tests

1. **Determinant blindness:** use two noncommuting trace-zero generators.
   Every switching word has determinant one although the propagators differ.
2. **Unreachable augmentation:** append an arbitrary internal block with zero
   input incidence.
3. **Unobservable augmentation:** append an arbitrary internal block with zero
   output incidence.
4. **Port-gauge ambiguity:** multiply incoming and outgoing rank-one defect
   coordinates by independent phases.
5. **False characteristic identification:** match the divisor of \(\Xi\) while
   the proposed transfer has different residues or boundary-port incidence.
6. **Minimal but nonselective hostile:** realize an arbitrary off-seam finite
   Blaschke factor as a passive, controllable, observable model.

## Programme consequence

Control theory supplies a possible reconstruction theorem, but only after the
scalar section is upgraded from aggregate readout to a fully typed transfer
with minimal source and endpoint ports. Even then, generic minimality does not
select RH-compatible zeros: every hostile finite Blaschke product has such a
realization.

The remaining source theorem must therefore do two jobs:

1. identify the completed theta section with the framed source-to-endpoint
   characteristic transfer;
2. impose an arithmetic incidence law that excludes hostile minimal
   realizations without inspecting their zero locations.
