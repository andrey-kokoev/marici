# Signed observers must descend as relational pairs

## Question

How can an orientation-sensitive port survive a physical quotient that reverses
the candidate reference direction?

## Claim boundary

Let a symmetry group (G) act on a candidate signed port (S) through a
nontrivial one-dimensional character (chi):

\[
gS=\chi(g)S.
\]

The port does not descend as a scalar observable on the quotient by (G). Orbit
averaging can erase it, while an even function such as (S^2) descends but loses
the sign information.

Introduce a source-derived relational tag (t) transforming through the dual
character. Then

\[
g(tS)=tS.
\]

The product descends while retaining sensitivity to transformations that act on
the target phase but not on the reference tag.

This is a representation-theoretic descent condition. It does not construct the
physical tag or calibrate its errors.

## Flavor instantiation

For identical unpolarized proton beams, a candidate phase-sensitive port has
the form

\[
S=D\,b\sqrt{uv}\sin\phi,
\]

where beam exchange reverses (b). The untagged expectation vanishes under the
beam-exchange quotient. Squaring the port retains magnitude information but is
even under (phi\mapsto-\phi).

A beam-odd event tag (t) makes (tS) beam-exchange invariant while preserving
its odd response to phase conjugation. Such a tag must arise from an admitted
associated-production or other source constructor. Assigning a beam label by
coordinate convention does not define the relational observable.

## Optical instantiation

Direct intensity detects

\[
|E|^2
\]

and loses field phase. A phase-sensitive quadrature requires a local oscillator
or equivalent reference that transforms with the signal under global phase
change. The measured quantity is relative phase, not an absolute signal phase.

In the sign-valued finite model, signal amplitude (a) and reference amplitude
(r) both reverse under the unobservable global sign, while (ra) remains
invariant. This is the same relational descent law as the tagged flavor port.

## Gauge-torsor gate

Existence of relational tags does not necessarily select one canonical tag. The
space of valid trivializations may be an affine torsor. A zero-dimensional
torsor gives a unique frame; a positive-dimensional torsor requires a separate
source-authorized selector.

A selector can choose among existing descending observables. It cannot remove a
nontrivial cohomology obstruction or manufacture a tag absent from the source
grammar.

## DPC

A signed observer passes only if:

1. its target odd character is explicitly identified;
2. its failure to descend under the physical quotient is reproduced;
3. a source-derived dual-character reference is constructed;
4. the paired observable is invariant under the quotient and remains odd under
   the target transformation;
5. tag assignment, dilution, and covariance are calibrated;
6. the reference choice is canonical or carries an authorized selector;
7. context saturation and global cocycle closure pass;
8. fault and completion stability are established.

## Finite falsifiers

- Orbit averaging annihilates the unpaired signed port.
- Squaring descends but becomes target-sign even.
- A proposed tag transforms trivially and fails to cancel the quotient action.
- The tag is assigned by presentation convention rather than source process.
- Multiple valid tags form a nontrivial torsor with no authorized selector.

## Disposition

The finite relational descent theorem is closed. It identifies a shared
optics-flavor mechanism: sign information becomes physical only through a
source-derived relative reference. Flavor currently lacks the tagged production
constructor; the optical instantiation remains assigned to Aspect for a native
instrument audit.

Verification is provided by
`research/nima/checkers/check_relational_signed_observer.py` and
`research/nima/results/relational-signed-observer.json`.
