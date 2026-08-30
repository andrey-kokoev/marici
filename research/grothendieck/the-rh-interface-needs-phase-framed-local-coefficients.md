# The RH interface needs phase-framed local coefficients

## New transfer

The normalized-interface proposal still hid an assumption: it treated every
boundary route as carrying a scalar coefficient in one fixed frame.

Aspect's Fibonacci falsifier shows that a legitimate source can mix
factorization routes by a non-diagonal matrix. Such a comparison is neither a
scalar phase nor a permutation. A scalar normalized complex rejects it or
mis-types it as a Gram form.

Nima's controlled-channel theorem identifies a prior loss. Passing from a
phase-framed amplitude `U` to its projective channel identifies `U` and
`omega U`, but coherent control distinguishes them. No operation performed
after that quotient can reconstruct the relative phase.

Together these results imply that the RH interface must be tested as a chain
complex with a source-derived, phase-framed local coefficient system.

## Twisted interface complex

Let `I_s` be the frozen simplicial or Čech interface object. Assign to every
interface chart `i` a source amplitude module `V_i(s)`. An admitted route
`r:i -> j` carries a linear transport

\[
\rho_s(r):V_i(s)\longrightarrow V_j(s).
\]

The transport may be scalar, diagonal, or genuinely matrix-valued; its type
must be derived from the theta/Tate constructor before the homology test.
Composition requires

\[
\rho_s(r_2r_1)=\rho_s(r_2)\rho_s(r_1)
\]

or an explicitly preregistered higher coherence cell.

The correct candidate is therefore the normalized chain complex with local
coefficients

\[
N_\bullet(I_s;\rho_s),
\]

not the scalar complex `N(B_s)` by default. The earlier derived-pullback
statement becomes

\[
C_+\times_{B_s}^{h}C_-
\simeq
N_\bullet(I_s;\rho_s)[-1]
\]

when this complex is the actual interface object.

## Why phase framing precedes scalar completion

The Evans inner factor is relative-phase data. If theta/Tate amplitudes are
first collapsed to scalar magnitudes, projective channels, or determinant
values modulo a unit, the controlled comparison needed to expose that inner
factor may no longer descend.

The construction order must be:

1. source-labelled amplitude modules;
2. phase-framed Fourier–Tate route transports;
3. normalized chains with those local coefficients;
4. cycles modulo authorized fillings;
5. coherent target/control comparison;
6. scalar determinant or Evans readout.

Scalarization before the third or fourth step can erase the candidate class.

## Direct theta/Tate consequence

Poisson sewing may exchange a primal lattice basis with a dual basis rather
than act diagonally on integer labels. The required audit is therefore not
whether the scalar functional equation closes. It is whether the complete
labelled sewing defines `rho_s` on a common amplitude module, possibly after
primal–dual doubling.

This also supplies a better interpretation of an off-line inner factor. Its
phase delay could be holonomy of the source local system. But that statement
is meaningful only after `rho_s` is independently derived; assigning a
connection from the observed phase delay would be circular.

## Frozen falsifiers

The proposal fails if:

1. two source routes with the same scalar endpoint require non-diagonal
   mixing absent from the frozen coefficient type;
2. `rho_s` is defined only after taking the scalar determinant;
3. transport is specified only projectively and no source phase-framed lift
   exists;
4. a phase-framed lift exists but depends on an arbitrary representative;
5. the face differential does not square to zero after inserting route
   transport;
6. a hostile symmetric multiplier is admitted merely by changing the local
   system after its divisor is observed.

## Smallest next calculation

Use the two-chart reciprocal interface and one prime label. Keep primal and
dual amplitude coordinates separate. Derive the smallest transport matrix
directly from the Fourier–Tate trace correspondence. Then test:

\[
\rho_s(r^{-1})\rho_s(r)=I,
\]

the transported face identities, and whether the resulting one-cycle is a
boundary under the already frozen filling operations.

The key output is not yet a determinant. It is the rank, kernel, and holonomy
class of this smallest phase-framed twisted interface complex.

## Scope

This result corrects the coefficient type of the proposed interface complex.
It does not derive the theta/Tate transport matrix, prove that its twisted
homology vanishes off the seam, connect its holonomy to the Evans inner
factor, or prove RH.
