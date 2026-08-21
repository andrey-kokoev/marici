# Radiative memory detects a nonabelian commutator

## Source-derived physical readout

Entry 1056 constructs the displacement-memory field

\[
\Delta C_{zz}=D_z^2N
\]

as one of three physical readouts of the common sphere operator.  Retain three
labelled celestial directions forming an equilateral orbit.  Their measured
memory values form a three-component readout on which the direction symmetry
is

\[
D_3=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle.
\]

The constant combination is a trivial scalar line.  The two independent
directional differences form the standard rank-two representation.

## Exact obstruction to universal abelianization

The durable checker constructs the exact permutation action, restricts it to
the difference plane, and derives

\[
[D_3,D_3]=\langle r\rangle\simeq C_3.
\]

On that physical directional plane,

\[
\rho(r)\ne I.
\]

Therefore

\[
\boxed{
\text{the vector-valued physical memory readout does not factor through }
D_3^{\rm ab}.
}
\]

This is not a failure of Grothendieck's physical-readout congruence.  It is its
first hostile positive detector: the detected commutator is retained in
\(G_{\rm phys}\).

## Required refinement

The proposed arithmetic shadow cannot apply to **all** physical readouts.
It applies, if at all, after an invariant scalarization or pairing:

\[
\text{covariant physical multiplet}
\longrightarrow
\text{invariant scalar record}
\longrightarrow
\text{possible abelian arithmetic shadow}.
\]

The constant sample line is commutator-blind; the directional memory plane is
not.  Hence the distinction between covariant records and invariant scalar
records is structural, not semantic.

## Scope

The test uses a finite \(D_3\) subgroup of celestial-direction symmetry.  It
does not assert a new BMS algebra result, change Entry 1056's carrier, or say
that every scalarized gravitational observable abelianizes.

Evidence: Ledger Entry 1056; checker
`research/nima/check_radiative_memory_d3_commutator.py`.
