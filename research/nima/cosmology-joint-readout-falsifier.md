# Frozen cosmology joint-readout falsifier

## Purpose

This protocol tests the cross-sector jointly-conservative-readout conjecture
without influencing the construction of the cosmological maps. It is frozen
before importing any new map packet from another researcher.

## Frozen domain

The domain must be one explicitly versioned, finite, frozen marked-relative
cosmological coefficient object. Its basis, dimension, coefficient field, and
digest must be declared before ranks are computed. A dimension match does not
identify the domain.

## Required readouts

Exactly four source-derived maps are admitted in version 1:

\[
R_{\rm res},\qquad R_\infty,\qquad R_{\rm near},\qquad R_{\rm phys}.
\]

They represent the residue, infinity-Gysin, nearby-cycle, and physical-pairing
readouts. Each must arrive with source provenance, a matrix in the frozen
domain basis, a typing certificate, and the appropriate differential,
connection, or Beck--Chevalley coherence certificate.

## Decision

Let

\[
R_{\rm joint}=
\begin{pmatrix}
R_{\rm res}\\R_\infty\\R_{\rm near}\\R_{\rm phys}
\end{pmatrix}.
\]

The conjecture passes this bounded test precisely when

\[
\ker R_{\rm joint}=0.
\]

It fails when every required map is admissible but this kernel is nonzero. It
is inconclusive—not failed—while the domain or any required map or certificate
is missing.

## Forbidden repairs

The test may not be rescued by a fitted splitting, a quotient chosen after
seeing the residual, a rank-only identification, promotion of an untyped
associated grade, or addition of a fifth readout after inspecting the joint
kernel. Any expanded readout family is a new protocol version and does not
alter the version-1 outcome.

## Present status

The protocol checker and both positive and negative synthetic controls pass.
The scientific result is currently **inconclusive**, because no map has been
borrowed or manufactured for this protocol. This preserves the independence
of the ongoing cosmology work.
