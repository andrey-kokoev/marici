# A three-cycle dyon twist is a complex reference only inside a controlled path comparison

Owner: `marici.Kitaev`

## Bounded question

Can the frozen `D(S3)` source supply the independent complex reference needed
to distinguish coherent fusion-corridor closure from the hostile rank-two Gram
matrix invisible to real electric braid tests?

Algebraically, yes: the three-cycle dyons `G` and `H` have nonreal twists.
Operationally, the twist becomes a reference only when an admitted coherent
instrument compares a twisted path with an untwisted path. An unconditional
twist of one isolated simple anyon is a global phase and has no observable
effect.

## Frozen source datum

In label order `A,B,C,D,E,F,G,H`, the exact modular packet gives

\[
(\theta_A,\ldots,\theta_H)
=(1,1,1,1,-1,1,\omega,\omega^2),
\qquad
\omega=e^{2\pi i/3}.
\]

Geometric ribbon reversal exchanges `G` and `H`. Thus it complex conjugates
the two candidate references:

\[
\omega\longleftrightarrow\omega^2.
\]

This is distinct from the `B`-simple-current sheet, which exchanges `A,B` and
`D,E` but not `G,H`.

## Any nonreal trusted phase completes the real quadrature

Let an unknown corridor coherence be

\[
z=x+iy.
\]

The frozen electric tester supplies the real statistic

\[
m_0=\operatorname{Re}z=x.
\]

Suppose an independent reference supplies a known phase

\[
u=e^{i\phi},
\qquad
\sin\phi\ne0,
\]

inside the same coherent route comparison. A second real readout gives

\[
m_u=\operatorname{Re}(uz)
=x\cos\phi-y\sin\phi.
\]

The two observations reconstruct the missing quadrature:

\[
y={x\cos\phi-m_u\over\sin\phi}.
\]

For the `G` twist,

\[
m_\omega=-{x\over2}-{\sqrt3\over2}y,
\qquad
y=-{2\over\sqrt3}\left(m_\omega+{m_0\over2}\right).
\]

Therefore a quarter turn is not special. One nonreal cube-root phase is
already sufficient. The exact minimality condition is simply that the second
real functional not be collinear with the first.

## Rank certification needs less orientation than phase identification

Replacing `G` by `H` sends the reconstructed value of (y) to its negative.
It does not change

\[
|z|^2=x^2+y^2.
\]

This separates two tasks.

- To certify rank-one closure of a normalized environment Gram matrix, a
  fixed but unoriented `G/H` reference is enough. The conjugation torsor does
  not change the pairwise unit-visibility test.
- To identify the implemented logical phase or the sign of a `Y` quadrature,
  the apparatus must also anchor geometric ribbon orientation and distinguish
  `G` from `H`.

The reference may remain unanchored only if it is fixed throughout a coherent
data set. Randomly switching between `G` and `H` averages the two rotated
statistics:

\[
{1\over2}\operatorname{Re}(\omega z)
+{1\over2}\operatorname{Re}(\omega^2z)
=-{x\over2}.
\]

That mixture erases the imaginary quadrature and recreates the real-tester
kernel.

## Why modular `T` is not yet an instrument

On an isolated simple `G` anyon, a full ribbon twist acts as

\[
|G\rangle\longmapsto\omega|G\rangle.
\]

The output ray is unchanged. No measurement on that ray alone can observe
the phase. A usable reference needs a coherent path degree of freedom, for
example

\[
{1\over\sqrt2}
\left(
|0\rangle|G\rangle+|1\rangle|G\rangle
\right)
\longmapsto
{1\over\sqrt2}
\left(
|0\rangle|G\rangle+\omega|1\rangle|G\rangle
\right),
\]

where only the second branch executes the framed twist and both branches
return the anyon and every unobserved degree of freedom to the same state.

The equality of the returned environment states is essential. If the two
paths leave distinguishable ribbon, motion, or controller records, their
overlap multiplies the intended phase and the reference itself has acquired a
Gram defect.

## Minimal source-authorized tester

A sufficient sacrificial tester has four typed components.

1. A prepared and charge-resolved `G` or `H` dyon reference.
2. A coherent binary path controller.
3. One branch implementing an oriented framed twist while both branches close
   on the same final anyon and apparatus state.
4. A real pointer readout performed once without and once with the resulting
   cube-root phase in the corridor route comparison.

Applied pairwise to the normalized corridor Gram entries, the two real
statistics recover each modulus. Exact coherent closure follows when

\[
|G_{AB}|=|G_{AC}|=|G_{BC}|=1.
\]

This tester may consume prepared copies. It does not synthesize the protected
single-copy logical bridge whose corridor it audits.

## Fault and authority boundary

The exact modular source proves the twist scalars and their conjugation under
ribbon reversal. It does not yet prove any of the following physical
constructors:

- preparation of an isolated `G` or `H` excitation with a declared error
  model;
- coherent controlled twisting;
- clean path recombination;
- coupling of the reference phase to the selected electric fusion-corridor
  matrix element;
- fault-local certification of the path controller.

Consequently the source contains an algebraic complex reference but the
current executable surface does not yet contain a certified complex-reference
instrument.

This is the same constructor distinction seen elsewhere in the programme:
an invariant can specify the value an operation must have without supplying a
local Hamiltonian path that realizes the operation.

## Exact hostile cases

- Treating the diagonal modular `T` matrix as an already executable gate.
- Applying an unconditional `G` twist and claiming its global phase was read.
- Replacing coherent path control by a classical random choice of twist.
- Mixing `G` and `H` between shots and still claiming imaginary-quadrature
  reconstruction.
- Using the unverified electric bridge as the only controller for its own
  phase reference.
- Ignoring residual which-path information after recombination.
- Inferring the sign of the logical `Y` quadrature from an unanchored `G/H`
  torsor.
- Claiming that the unanchored torsor prevents rank certification, even though
  pairwise moduli are conjugation invariant.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies two routes, a closed comparison, and the
condition that both routes return to one common endpoint state. It also
supplies the general two-real-probe reconstruction criterion.

The quantum coefficient lens supplies the ribbon twist, the cyclotomic phases
`omega` and `omega^2`, the `G/H` conjugation action, complex fusion coherences,
and the rank-one Gram condition.

## Result

The `D(S3)` source already contains a minimal nonreal phase. A `G` or `H`
twist is sufficient to complete the real electric tester at the level of
algebraic information. It becomes operational information only through a
clean controlled-path interferometer. Ribbon orientation is unnecessary for
rank-one certification but necessary for signed phase identification.

No build or checker was run for this research-only packet.
