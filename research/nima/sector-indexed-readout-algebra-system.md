# Readout algebras form a sector-indexed system, not a cross-sector algebra

## Typing correction

The first census found no source-derived algebra map between radiative memory,
flavor, strings, and cosmology.  This absence should not be treated as a
failure until a physical constructor relating two sectors is independently
declared.

The minimal typed organization is a projection

\[
\pi:\mathsf{ReadoutAlg}\longrightarrow\mathsf{Sector},
\]

whose fiber over a sector \(s\) contains its substrates, symmetries,
selection resources, and invariant-record algebras.  Physical constructors
give morphisms primarily **inside one fiber**.  A cross-sector morphism exists
only when the source supplies a bridge between the sectors.

Thus the current object should not be

\[
R_{\rm memory}\to R_{\rm flavor}\to R_{\rm string}\to R_{\rm cosmology}.
\]

It should be a family

\[
\{R_s\}_{s\in\mathsf{Sector}}
\]

equipped with sectorwise constructor maps and a common vocabulary for the
shapes of their diagrams.

## Two distinct notions of shared calculus

1. **Cross-sector morphism:** an actual physical bridge
   \(F:s\to t\) inducing
   \(F^*:R_t\to R_s\).  This requires declared equivariance and physical
   selection compatibility.
2. **Shared diagram shape:** two sectors independently realize localization,
   nearby-cycle, Gysin, or pairing squares of the same formal type.  This is
   evidence for common calculus but is not an algebra homomorphism between
   their coefficient rings.

Confusing these would mix sector-specific coefficients with the generic
machinery—the same error the program has repeatedly rejected.

## Composition law

Within a sector, sourced constructors

\[
(V,G)\xrightarrow{F}(W,H)\xrightarrow{E}(X,K)
\]

induce contravariant algebra maps only when all equivariance and selection
data are retained:

\[
A[X]^K\xrightarrow{E^*}A[W]^H\xrightarrow{F^*}A[V]^G.
\]

The required coherence is

\[
(E\circ F)^*=F^*\circ E^*.
\]

If the sector supplies only an isolated scalar value, a finite observable
list, or an unpaired coefficient class, this composition is untyped.

## Arithmetic consequence

The conditional \(\pi_0\) semiring cannot act as one natural operation on the
sector family merely because every \(R_s\) is commutative.  One must first
construct sectorwise operations

\[
\psi_{n,s}:R_s\to R_s
\]

and verify naturality against every admitted constructor:

\[
F^*\psi_{n,t}=\psi_{n,s}F^*.
\]

No current packet supplies these \(\psi_{n,s}\).  Therefore arithmetic
naturality is an open construction problem, not a consequence of the initial
semiring on disconnected Carrier components.

## Sharp next test

Do not search first for a map between unrelated sectors.  Choose one sector
with two independently established physical constructors, derive both
invariant-algebra pullbacks, and test one composition square.  Only after one
fiber closes should the same diagram shape be sought independently in a
second sector.

A failure localizes cleanly:

- no substrate map: constructor absent;
- substrate map but no equivariance: symmetry resource missing;
- equivariant map but no physical selection compatibility: chain/support
  resource missing;
- individual pullbacks exist but composition fails: coherence resource
  missing.

## Scope

This is an organizational typing claim.  It constructs no new physical
bridge, arithmetic operation, Carrier multiplication, or Phase-II object.

Evidence: `research/nima/cross-sector-readout-algebra-type-census.md` and the
cross-sector synthesis of Ledger Entry 1213.
