# Green boundary totalization must remain three-stratum

## Finite direct sums

For every finite labelled cutoff, the centered-dilation Green identities add
exactly.  If the local bulk defect and oriented boundary flux at label \(j\) are
\(G_j\) and \(B_j\), then

\[
G_j=B_j
\]

implies

\[
\sum_{j\le N}G_j=sum_{j\le N}B_j.
\]

This finite equality does not determine the type of the infinite totalization.

## Three completion classes

There are three qualitatively distinct source families.

First, an absolutely summable family has

\[
\sum_j|B_j|<\infty.
\]

Its scalar boundary flux is canonical and independent of enumeration.  This is
the appropriate model for the connected trace-class tail.

Second, a square-summable but non-absolutely-summable family has

\[
\sum_j|B_j|^2<\infty,
\qquad
\sum_j|B_j|=\infty.
\]

It defines a Hilbert boundary vector but not a canonical scalar sum.  This is
the appropriate model for the prime-square current.

Third, a family that is not square-summable does not define a Hilbert boundary
vector.  It requires distributional pairing with a declared test object.  This
is the appropriate model for the primitive-prime current.

## Categorical consequence

The global operative coherencer cannot land directly in one scalar boundary
object.  It must first land in a stratified carrier

\[
B^{(1)}\oplus B^{(2)}\oplus B^{(3)},
\]

where the three summands carry distributional, Hilbert, and trace-class
modalities.  The superscripts indicate regularity strata, not ordinary vector
degrees.

Only a later source-derived totalization functor may combine them with the
endpoint and archimedean channels.  That functor must declare its ordering,
test space, subtraction terms, and completion topology.

This clarifies the internal three of each \((3+2+1)\) packet: it is not merely
three named contributions.  It is three incompatible completion modalities
that must remain typed through both sector legs and the dynamic Green cell.

## Finite-cutoff exactness does not authorize scalar completion

Three elementary families provide exact hostiles:

- \(B_j=1/j^2\) is absolutely summable;
- \(B_j=1/j\) is square-summable but not absolutely summable;
- \(B_j=1\) is not square-summable.

Every finite partial sum satisfies the same local Green identity.  Their global
boundary meanings are nevertheless different.  Treating all three as one
scalar series smears completion authority.

Conditional cancellation is also insufficient.  The alternating harmonic
family can be rearranged to change its scalar limit while preserving every
local term.  Enumeration or renormalization must therefore be source-derived.

## RH-bearing gate

The live theorem is a stratified restricted-product Green identity:

1. construct the primitive current as a continuous distributional boundary
   functional;
2. construct the square current as a Hilbert boundary vector with its declared
   quadratic pairing;
3. construct the connected tail as an absolutely summable scalar flux;
4. add the endpoint and archimedean boundary objects;
5. derive one totalization functor whose result is the mixed theta/Tate residue;
6. prove that zero-state boundary conditions annihilate the total oriented flux
   without annihilating the positive bulk norm off the seam.

Any scalar cancellation written before these constructions is unauthorised.

## DPC verdict

The finite Green triangle is exact, but global scalar totalization is falsified
as a universal operation.  The three regularity strata are irreducible source
types.  The dynamic \(+1\) must preserve them until a source-derived
renormalized boundary functor is available.

The smallest falsifier for a proposed scalar totalization is a square-summable
non-absolutely-summable boundary family admitted by its domain.  If the functor
returns an enumeration-independent scalar without additional source data, it
has exceeded its authority.

## Verification

`check_rh_green_three_stratum_totalization.py` verifies exact bounded partial
sums for the three model strata, distinguishes their norm growth, and checks a
finite rearrangement witness for conditional scalar sensitivity.
