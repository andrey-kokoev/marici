# A three-cycle dyon twist supplies the exact cube-root phase but not its controlled bridge coupling

Owner: `marici.Kitaev`

## Bounded question

Can the oriented coefficient `z=-omega` required by the exact sixth-root
qutrit injection come from intrinsic `D(S3)` topological data rather than an
analog phase reference?

Yes, at the coefficient level. The two nontrivial three-cycle dyon species
have scalar topological twists `omega` and its conjugate. A coherent route
that twists one fixed dyon species on one branch and does nothing on the other
returns the dyon unchanged while kicking its twist onto the route coordinate.

The required coefficient then factorizes into two already typed resources:

\[
-\omega=(-1)\omega.
\]

The real sign is available from the pure-electric or `B`-parity layer; the
cube-root orientation is supplied by a chosen three-cycle dyon species. What
remains unproved is the controlled microscopic twist and its coherent
incidence with the charged qutrit bridge.

## Claim boundary

The group, centralizer, topological-spin, and phase-kickback calculations are
exact for the untwisted quantum double `D(S3)`. The physical conclusion is
conditional on a framed twist being an admitted protected operation in the
frozen lattice realization and on coherent route control preserving all
fusion and environment ports.

This packet does not identify a lattice ribbon sequence implementing the
controlled twist, prove fault tolerance, or infer a qutrit action from an
ancillary scalar phase.

## The orientation torsor in the standard electric charge

Present the group as

\[
S_3=\langle r,t\mid r^3=t^2=e,\;trt=r^{-1}\rangle.
\]

In a complex eigenbasis for the standard electric representation `C`, choose

\[
\rho_C(r)
=
\begin{pmatrix}
\omega&0\\
0&\omega^2
\end{pmatrix},
\qquad
\rho_C(t)
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The relation

\[
\rho_C(t)\rho_C(r)\rho_C(t)=\rho_C(r)^{-1}
\]

shows that a transposition exchanges the two oriented eigenlines. Their set
is a `C2` torsor: the representation contains the distinction, but an
unresolved real preparation chooses neither member.

If the eigenline label is twirled, the reference state is

\[
\sigma_{unres}
=
\frac12
\left(
|+\rangle\langle+|
+
|-\rangle\langle-|
\right).
\]

A controlled winding by `r` then has two conjugate phase branches. After the
unresolved reference is discarded, an off-diagonal route coherence is
multiplied by

\[
\frac{\omega+\omega^2}{2}=-\frac12.
\]

This is attenuation, not phase kickback. The central Wilson value is exactly
the scalar shadow of this loss of orientation.

## Three-cycle simple objects

The conjugacy class of `r` is

\[
\mathcal C_3=\{r,r^{-1}\}.
\]

Its centralizer is

\[
Z_r=\langle r\rangle\cong C_3.
\]

Let its three one-dimensional characters be `chi_k`, where

\[
\chi_k(r)=\omega^k,
\qquad
k=0,1,2.
\]

The corresponding quantum-double simple objects have quantum dimension two.
For a simple object labelled by a conjugacy class and a centralizer
representation, the topological twist is

\[
\theta_k
=
\frac{\chi_k(r)}{\chi_k(e)}
=
\omega^k.
\]

Thus the two nontrivial three-cycle dyons have twists

\[
\theta_1=\omega,
\qquad
\theta_2=\omega^2=\overline\omega.
\]

They are conjugate topological charge species, not two unresolved internal
eigenlines of one pure-electric charge.

## Clean topological phase kickback

Let `D_k` be a dyon of the selected species and let `T_k` denote one framed
topological twist. Within its fixed simple sector,

\[
T_k=\theta_k I_{D_k}.
\]

Coherently control this operation by a route bit:

\[
W_k
=
|0\rangle\langle0|\otimes I_{D_k}
+
|1\rangle\langle1|\otimes T_k.
\]

For every dyon state `phi`,

\[
W_k
\left(
(a|0\rangle+b|1\rangle)\otimes|\phi\rangle
\right)
=
\left(
a|0\rangle+b\theta_k|1\rangle
\right)
\otimes|\phi\rangle.
\]

The phase is kicked onto the route coordinate while the dyon returns exactly
to its input state. At the TQFT level this passes the environment-return gate
automatically because the twist is scalar on the fixed simple sector.

This is stronger than using the standard electric `C` charge: no eigenline
resolution inside a two-dimensional representation is required after the
dyon species has been selected.

## Relational rather than absolute orientation

The two nontrivial dyon species are exchanged by conjugation. Creating a dyon
and antidyon from vacuum therefore supplies a relationally oriented pair, not
an absolute external complex frame.

Choosing which endpoint carries the `theta_1` species fixes a source frame.
Reversing the pair exchanges `omega` and its conjugate. All internally
conjugated operations remain mutually consistent, so a compiler that targets
an externally specified complex unitary still needs one trusted classical or
boundary convention recording which species was called positive.

This does not obstruct projective universality: conjugating the complete
sixth-root gate alphabet gives another projectively universal alphabet. It
does obstruct claiming that the sign of the complex orientation has been
absolutely certified by conjugation-invariant probes.

## Factorization of the required measurement coefficient

The phase-halving gadget requires

\[
z=-\omega.
\]

Its two factors have different physical provenance:

- the factor `-1` belongs to the real sign layer and can be supplied by an
  ordinary relative minus in route recombination or by a typed `B`-parity
  operation;
- the factor `omega` belongs to the selected nontrivial three-cycle dyon twist.

The factorization matters because the `B` charge alone has trivial monodromy
on three-cycles and cannot supply `omega`. Conversely, a dyon twist supplies
only a scalar phase on the route unless the route is coherently coupled to the
qutrit bridge.

Possessing the two factors in separate apparatus is insufficient. The same
route coherence must traverse both constructors before the oriented
measurement is made.

## The complex measurement can be replaced by real recombination

There is a useful relocation of the coefficient. Begin after the two charged
routes with

\[
\frac1{\sqrt2}
\left(
R|\psi\rangle\otimes|0\rangle
+
S|\psi\rangle\otimes|1\rangle
\right).
\]

Use the selected dyon twist to kick `omega` onto the second route. The state
becomes

\[
\frac1{\sqrt2}
\left(
R|\psi\rangle\otimes|0\rangle
+
\omega S|\psi\rangle\otimes|1\rangle
\right).
\]

Now measure the route bit in the ordinary real `X` basis. The two branch
operators are

\[
K_{X+}=\frac{R+\omega S}{2},
\qquad
K_{X-}=\frac{R-\omega S}{2}.
\]

The `X-` branch is exactly the earlier phase-halving branch with coefficient
`z=-omega`. For

\[
R=I,
\qquad
S=\exp(2\pi iP_A/3),
\]

it occurs with probability `3/4` and gives, projectively,

\[
K_{X-}\sim\exp(i\pi P_A/3).
\]

The `X+` branch occurs with probability `1/4` and gives the same correctable
inverse cube-root failure found previously.

Therefore an independently implemented complex route-measurement basis is
not necessary. One intrinsic controlled dyon twist followed by real route
recombination has the identical instrument. The resource requirements become
cleaner:

1. the `B`-sector workspace supplies coherent charged-route connectivity;
2. the selected three-cycle dyon supplies topological cube-root kickback;
3. a real `X` measurement supplies the relative sign and branch record;
4. the admitted cube-root correction resets the failure branch.

This does not remove the controlled-incidence problem. It localizes it: the
dyon twist must be controlled by the very route bit that distinguishes `R`
from `S`.

## The remaining controlled-incidence constructor

Let the two charged qutrit routes be `V_R,V_S`, and let the twist-controlled
route operation be `W_1`. The physical target is a single isometry whose
compression has the form

\[
V_R\otimes|0\rangle
+
V_S\otimes|1\rangle,
\]

with the dyon twist and real sign acting only on the second route coefficient
before coherent recombination.

Three independent conditions remain:

1. the dyon twist must be coherently controlled rather than classically
   selected;
2. the controlled worldline must preserve the dyon fusion channel and return
   all ancillary ribbon data;
3. the resulting phase must multiply the same route coordinate whose relative
   qutrit holonomy is `exp(2 pi i P_A/3)`.

The third condition is the incidence law. A perfect dyon phase acting on a
spectator path does not inject `Q_A`.

## Minimal hostiles

### Unresolved electric orientation

Use the twirled standard-charge state `sigma_unres`. Controlled winding
attenuates route coherence by `-1/2`; it does not return a pure phase.

### Dyon spectator

Apply the dyon twist to an ancillary interferometer uncorrelated with the
charged bridge route. The phase is exact and measurable, but the logical
qutrit channel is unchanged.

### Species-erased preparation

Prepare an equal classical mixture of the two conjugate nontrivial dyon
species. The kicked route factor averages `omega` and its conjugate and again
produces attenuation rather than an oriented unitary.

### Uncontrolled twist record

Classically decide whether to twist and retain the decision record. The qutrit
sees a mixture of routes, not the coherent coefficient `z`.

### Framing leakage

Implement a microscopic ribbon motion whose final local framing or ancillary
state differs between the twisted and untwisted routes. The nominal scalar
topological spin is then multiplied by an environment overlap and fails the
whole-instrument closure theorem.

## Physical audit for the lattice model

The next microscopic calculation should freeze one pair-created nontrivial
three-cycle dyon and exhibit:

- its centralizer-character label;
- its vacuum fusion channel with the conjugate partner;
- a lattice ribbon sequence representing one framed twist;
- the induced scalar on the fixed simple sector;
- identical final ribbon, fusion, and environment states on the two route
  alternatives;
- coherent control of whether the twist occurred;
- composition with the `B`-sector bridge on the same route bit;
- the final branch Kraus maps on the encoded qutrit.

If the lattice model has no protected framed-twist primitive, the same audit
must be repeated for a braid or monodromy word having the identical scalar
action. The abstract topological spin does not itself authorize a laboratory
actuator.

## Exact falsifiers

- The two standard-charge eigenlines are called one resolved orientation.
- The unresolved central Wilson value `-1/2` is promoted to `omega`.
- A mixture of conjugate dyon species is treated as a phase eigenresource.
- The `D(S3)` twist formula is applied without fixing the conjugacy-class
  representative and centralizer character consistently.
- The conjugate dyon species are assigned the same twist.
- A scalar dyon phase on an unrelated path is called a qutrit gate.
- The real minus sign and cube-root orientation are attributed to one `B`
  port.
- A controlled twist is inferred from the existence of an uncontrolled twist.
- A framed TQFT identity is promoted to a protected lattice operation without
  a ribbon realization.
- Route-dependent framing or environment residue is ignored.
- Internal conjugation consistency is claimed to fix an absolute external
  complex convention.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies oriented versus unresolved ports, relational
reference pairs, controlled routes, scalar kickback, incidence with the
logical bridge, framing return, and the separation of a resource from its
actuator.

The quantum coefficient lens supplies the `S3` centralizers, quantum-double
simple objects, topological twists, conjugate dyon species, character phases,
fusion sectors, and coherent Kraus closure.

## Disposition

The cube-root coefficient needed by the discrete universal qutrit constructor
is already present intrinsically in `D(S3)`: it is the scalar twist of a
nontrivial three-cycle dyon. Together with an independently supplied real
minus sign it gives the exact coefficient `-omega` without analog waiting.

The frontier has therefore narrowed again. It is not phase existence but
controlled physical incidence: can one protected lattice process condition a
dyon twist on the same coherent route whose qutrit relative holonomy is the
vacuum-projector cube root, while returning every fusion, framing, and
environment port?

No build, checker, or Git operation was run for this research-only packet.
