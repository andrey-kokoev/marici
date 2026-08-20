# Phase-I five-point string disk readout factors through dihedral abelianization

## Source object

Use Entry 891's source-normalized five-point Parke--Taylor period, transporting
the ordered chamber, Parke--Taylor cocycle, Koba--Nielsen loading, and labelled
kinematics simultaneously.  This is a physical period readout, not merely a
local coefficient module.

The Parke--Taylor denominator is cyclic.  Reversing the cyclic word reverses
all five oriented edge factors and gives the standard color-order character

\[
\chi(r)=+1,
\qquad
\chi(s)=(-1)^5=-1,
\]

where \(r\) is a rotation and \(s\) a reflection.  The Koba--Nielsen loading
is transported by label substitution and contributes no independent
character.

## Exact group audit

For

\[
D_5=\langle r,s\mid r^5=s^2=1,\ srs=r^{-1}\rangle,
\]

the commutator subgroup is

\[
[D_5,D_5]=\langle r\rangle\simeq C_5.
\]

The durable checker constructs all ten permutations, verifies the character
on all 100 products, derives the five-element commutator subgroup, and checks
that every commutator acts by \(+1\).  Hence

\[
\boxed{
\chi:D_5\longrightarrow\{\pm1\}
\text{ factors through }D_5^{\rm ab}\simeq C_2.
}
\]

Entries 894--896 independently establish that the finite-\(\alpha'\) sine
circuit is assembled from the transported physical periods and source-derived
Pochhammer cells.  The conclusion therefore holds at the physical disk-period
readout, not only in the field-theory associated grade.

## Cross-sector consequence

Strings now supply a third positive physical-readout example alongside the
scattering orientation line and cosmology's coefficient--Betti pairing.
Flavor remains the essential warning: its coefficient/chart lens is
commutator-sensitive even though its physical weak-basis readout kills a
larger gauge orbit.

The surviving architecture is

\[
\text{nonabelian Carrier}
\to
\text{sector lens}
\to
\text{physical readout}
\to
\text{abelian arithmetic shadow}.
\]

This does not establish a universal quotient or a Carrier-level product.  It
also does not settle the six-point exceptional shift module, whose global
physical pairing remains unconstructed.

Evidence: Ledger Entries 891, 894--896; checker
`research/nima/check_phase_i_string_disk_readout_d5.py`.
