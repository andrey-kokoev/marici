# Forgetful projections and the no-canonical-section theorem

## Problem

A legacy evidence projection may forget operative constructor fields while
remaining surjective:

\[
U:C\to E.
\]

Set-theoretic preimages exist, so “there is no lift” is too strong. The
correct statement is that the forgotten data cannot be reconstructed
canonically from \(E\).

## Symmetry obstruction

Let a group \(G\) act on the core space \(C\) while preserving the legacy
projection:

\[
U(gc)=U(c).
\]

A source-canonical lift must be invariant under every symmetry invisible to
the legacy data. Thus a section \(s:E\to C\) must satisfy

\[
g\,s(e)=s(e)
\qquad
\text{for every }g\in G_e,
\]

where \(G_e\) is the symmetry group of the fiber \(U^{-1}(e)\).

Therefore:

> If one legacy fiber has no point fixed by all of its invisible
> automorphisms, no canonical equivariant section exists.

Any chosen lift then breaks an invisible symmetry and requires an additional
source-authorized constructor carrying the choice.

## Smallest finite witness

Take

\[
C=\{c_{\mathrm{linear},e},c_{\mathrm{bounded2},f}\},
\qquad E=\{p\},
\]

with

\[
U(c_{\mathrm{linear},e})
=U(c_{\mathrm{bounded2},f})=p.
\]

Let the nontrivial symmetry exchange the two core capabilities. It preserves
all legacy evidence because the projection forgets modality, quantity,
physical roots, and epoch. Neither core point is fixed. A section must select
one of them, but the swap sends it to the other. Hence no symmetry-invariant
section exists.

The finite rejection witness is:

\[
\texttt{noncanonical\_reverse\_lift},
\quad
\texttt{fiber\_size}=2,
\quad
\texttt{fixed\_points}=0.
\]

## Relation to constructor trees

A reverse lift is itself a constructor:

\[
\mu_{\rm lift}:
(\text{legacy packet},\text{modality},\text{quantity},
\text{roots},\text{epoch})
\rightharpoonup
\text{core capability}.
\]

The missing fields are inputs, not defaults. Declaring only the legacy
packet leaves the constructor under-applied. An arbitrary software default
is a hidden nullary authority source.

## Cross-sector consequences

- **Strominger.** The native linear capability at epoch \(e\) and the
  bounded-two-use capability at epoch \(f\) project to the same legacy
  packet. Their fiber symmetry proves there is no canonical import. The
  core normalizer is correct to require native construction.
- **Arithmetic/RH.** Scalar trace forgets labelled winding directions and
  their transport relations. A Gram or operator lift chosen from the scalar
  Xi kernel is noncanonical whenever invisible carrier unitaries move all
  candidate lifts. Source-labelled construction must precede projection.
- **Kitaev.** Equal logical action may have inequivalent physical
  realizations, resource modalities, and fault surfaces. A compiler cannot
  reverse-lift a logical gate to a physical gadget without an encoding and
  fault-model constructor.
- **Benincasa.** An integrated period value does not canonically reconstruct
  latent insertion coordinates, contact terms, or a de-Rham-Cech
  representative. Those data live in the projection fiber and require the
  source-labelled adapter.

## Essential-image refinement

The obstruction is stronger than noninjectivity alone. A noninjective map
can have a canonical section if each fiber contains a distinguished
source-fixed point. The correct finite test is:

1. compute the fiber of the projected packet;
2. compute its automorphisms invisible to the target;
3. find the common fixed-point set;
4. reject canonical reconstruction if that set is empty;
5. if it is nonempty but has several points, require an additional
   distinguishing source law.

This is the reverse-direction analogue of the essential-image gate.

## Durable statement

> Projection erases authority whenever its invisible fiber symmetries have
> no source-distinguished fixed point. A reverse lift is then a new typed
> constructor, not recovery of data already present in the projection.

