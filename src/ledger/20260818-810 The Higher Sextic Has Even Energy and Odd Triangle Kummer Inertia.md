# The Higher Sextic Has Even Energy and Odd Triangle Kummer Inertia

## Critical-value refinement

Entry 807 gives the exact universal critical value

\[
s=E^2\Lambda(P_1,P_2,P_3).
\]

The generic anti-invariant Kato line is represented by

\[
\frac1{\sqrt{s}}.
\]

Consequently its inertia depends on the valuation of \(s\), not merely on
the reduced support \(E\Lambda=0\).

## Energy divisor

Along a generic point of \(E=0\) with \(\Lambda\ne0\),

\[
\nu_E(s)=2.
\]

Locally, after choosing the \(\Lambda\)-sheet,

\[
\sqrt{E^2\Lambda}=E\sqrt\Lambda.
\]

A loop around \(E=0\) therefore acts trivially on the Kummer line:

\[
\boxed{M_E=+1.}
\]

This does not decide whether the geometric vanishing-cycle specialization is
zero or rank one; it only fixes its Kummer inertia.

## Momentum-triangle divisor

Along a generic point of \(\Lambda=0\) with \(E\ne0\),

\[
\nu_\Lambda(s)=1.
\]

Hence

\[
\boxed{M_\Lambda=-1.}
\]

The triangle degeneration retains the anti-invariant sign character.  Its
local critical locus is nonisolated in the squared-edge fiber, so this
character again does not by itself determine the full specialization rank.

## Intersection

At \(E=\Lambda=0\), the two local inertia generators commute and act by

\[
\boxed{(M_E,M_\Lambda)=(+1,-1).}
\]

Thus the \(\mu_2\) character factors through the triangle loop; the energy
loop is invisible to the Kummer cover because of its even multiplicity.

Both divisors are cyclically invariant.  Therefore these local inertia
characters tensor with Entry 808's regular occurrence representation.  For a
local rank \(r\), the occurrence character remains \((3r,0,0)\), while its
commuting divisorial inertia is respectively \(+1\) or \(-1\).

## Meaning for H2

The same frozen carrier supports two different coefficient behaviors:

\[
\boxed{
E=0:\text{ Kummer-trivial},
\qquad
\Lambda=0:\text{ Kummer-odd}.
}
\]

This is another precise instance of shared carrier calculus with
sector-specific—or here stratum-specific—coefficient data.

## Scope and handoff

No Milnor/Kato rank or surjectivity of the existing nearby-cycle/Gysin maps is
inferred.  Benincasa's local calculation must determine those ranks and maps;
this entry supplies the inertia and cyclic-character constraints they must
obey.

## Verification

- checker: `research/nima/audit_higher_sextic_kummer_ramification.py`;
- packet: `research/nima/higher-sextic-kummer-ramification.json`;
- allocator claim: `seqclaim-7a7480d43fdca8793c13b171`.
