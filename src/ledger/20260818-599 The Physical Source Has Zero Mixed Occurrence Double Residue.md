# 599 — The Physical Source Has Zero Mixed Occurrence Double Residue

## Hard-to-vary claim

The rank-one mixed occurrence class of Entry 598 exists in the ambient
five-mark coefficient system, but the source-prescribed physical
\(q_{G_{12}}\)-residue has zero component on its codimension-two residue
stratum.

## Source-local calculation

Use local coordinates at the occurrence intersection

\[
u=q_{g_{31}}=a-y,
\qquad
v=q_{g_{23}}=b-x.
\]

The two source summands have the same common three-wall and
Cayley--Menger factor. Their occurrence-dependent factor is exactly

\[
\frac1v+\frac1u
=
\frac{u+v}{uv}.
\]

The prospective iterated residue on \(u=v=0\) is therefore proportional
to

\[
\left.(u+v)\right|_{u=v=0}=0.
\]

Hence

\[
\boxed{
\operatorname{Res}_{u=0}\operatorname{Res}_{v=0}
\Omega_{\mathrm{phys}}=0
}
\]

at generic kinematics, where the common coefficient factor is regular at
the intersection.

This is not cancellation after choosing a master basis. It follows directly
from the frozen source sum and the two source denominator equations.

## Compatibility with the scattering degeneration

Entry 598 showed

\[
K_E(y,x)=E_T^3\cdot\text{unit}
\]

on the generic scattering boundary. Thus the common coefficient ceases to
be regular at \(E_T=0\), and generic double-residue vanishing alone would
not exclude a filtered exceptional class.

Entry 591 independently computed the source-derived ramified chart

\[
E_T=\tau^2
\]

and found that the leading unsplit exceptional form is exact, with zero
simple occurrence-exceptional residue. Combining the two calculations gives:

- zero generic mixed double residue;
- zero first source-derived weighted exceptional residue;
- no established vanishing theorem for every higher filtered grade.

## Consequence

The rank-twenty-six ambient localization complex remains the correct
deletion-closed coefficient object, but the physical source vector lies in
the kernel of its mixed codimension-two residue map.

Equivalently, the extra rank-one class in Entry 598 is an available
occurrence-incidence coefficient direction, not a physically occupied
source component at the tested grades.

No carrier modification follows.

## Next falsifier

Construct the source-unsplit localization cocycle on the remaining three
shared walls, with its mixed occurrence component fixed to zero. Then compute
the supported pushforward of its conductor boundary into the rank-seven
algebraic/Tate kernel. This avoids introducing a spurious mixed generator
into the physical comparison map.

## Evidence

- research/benincasa/check_unsplit_occurrence_pair.rs;
- research/benincasa/unsplit-occurrence-pair.json;
- Entries 590, 591, and 598.
