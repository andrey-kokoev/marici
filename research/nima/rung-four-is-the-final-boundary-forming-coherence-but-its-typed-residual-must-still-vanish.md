# Rung four is the final boundary-forming coherence, but its typed residual must still vanish

## Question

What exactly is meant by calling

\[
d_2\Delta^4=[S,A,C,G]
\]

the final boundary-forming coherence rung?

## Straightened hierarchy

For the declared four-system packet, use:

1. **Rung one — state signals.** The individual source, analytic,
   characteristic, and Green responses.
2. **Rung two — pair interfaces.** Pairwise correlations, transports, and
   boundary maps.
3. **Rung three — interface coherence.** Triangle cells comparing composites
   of pair interfaces.
4. **Rung four — boundary-forming coherence.** The oriented tetrahedral packet
   whose triangle faces must sew into one closed boundary.

In this convention, a correlation defect is an interface signal, and a
higher-order correlation defect is an interface-coherence signal. Rung four is
final relative to the chosen four objects; no additional internal rung is
needed merely to state their closure.

## Based coherence requirement

The hierarchy is not absolute. It is formed over the retained base signal

\[
b_z=\Delta_\Xi(z)=\Phi\otimes u_z.
\]

Every rung must retain or explicitly transport this same source coordinate:

\[
X_i(b_z),
\qquad
C_{ij}(b_z),
\qquad
C_{ijk}(b_z),
\qquad
C_{SACG}(b_z).
\]

A higher correlation with no retained base is only an unbased scalar
observation. Its vanishing cannot certify interface closure because the source
may already have been quotiented away.

The required base conditions are

\[
b_z\ne0,
\qquad
E_p(b_z)>0.
\]

Both hold for the corrected pair state. They do not hold for the Xi-exact
residue coordinate, which vanishes on the divisor. The residue is therefore a
coherence coordinate, not the base signal.

## Formation versus closure

Two assertions must remain distinct.

**Boundary formation** means that every face has a declared type, orientation,
transport, and common boundary coordinate. It constructs a single residual in
a common target.

**Boundary closure** means that this oriented residual vanishes.

Thus boundary formation does not automatically imply matching. It makes
matching a well-typed equation. If “boundary” is reserved definitionally for a
closed object, then a formed packet with nonzero residual is a horn or
boundary candidate, not yet a filled boundary.

## Current rung-four residual

After the lower source, trace, residue, wall, jump, endpoint, prime, and
polarization cells are sewn over the retained base, the final placewise
residual is the based evaluation

\[
\mathcal R_p(b_z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z),
\qquad
b_z\ne0,
\qquad
E_p(b_z)>0.
\]

Therefore

\[
\mathcal R_p(b_z)=0
\quad\Longleftrightarrow\quad
\operatorname{Re}z=0.
\]

The architecture has reached rung four: the final obstruction is formed,
typed, oriented, and noncollapsed. It has not proved rung-four closure.

## Claim boundary

This straightening asserts:

- rung four is the final coherence level for the four-system packet;
- all lower mismatches have been localized or sewn;
- the surviving residual is an interface-level signal;
- closure of that signal is equivalent to critical-line confinement on the
  corrected Xi lane.

It does not assert that boundary formation itself proves closure or RH.

## Disposition

Use the following terminology consistently:

- **formed rung-four horn** when the residual is defined;
- **closed rung-four boundary** only when the residual is proved zero;
- **rung-four filler** for a witness of that vanishing compatible with all
  lower faces.

The current status is a formed rung-four horn with one RH-strength Hermitian
residual, not a closed boundary.