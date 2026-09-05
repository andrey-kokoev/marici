# Physical resolution from the prime–spectral–Gram ladder

## Question

What would the prime-level, prime-derived spectral level, and quadratic/Gram level mean as a physical resolution architecture?

## Claim boundary

This packet gives a typed interpretation of the categorical model. The arrows are realization and feedback order, not physical time. A physical process exists only after a sector supplies a map

\[
\tau:C\longrightarrow T_{\rm phys}
\]

from the carrier to a physical-time object, together with orientation and readout authority. No such universal map is asserted here. “Prime” denotes an irreducible localized source identity in the abstract architecture; identifying it with number-theoretic primes in a physical sector requires a separate source map.

## The resolution diagram

Let \(P\) be localized source data, \(P'=\mathcal E(P)\) its completed spectral realization, and \(D(P,P')\) the typed incidence map comparing source and spectral presentations. The quadratic coherence object is

\[
Q(P,P')=D(P,P')^\dagger D(P,P').
\]

The resolution architecture is

\[
P
\xrightarrow{\mathcal E}
P'
\xrightarrow{D^\dagger D}
Q
\xrightarrow{C}
R
\xrightarrow{T}
P_{\rm next}.
\]

Here `next` means the counterclockwise successor in the realization workflow, not a later physical state.

## Physical interpretation of the three levels

### 1. Local source identity

The prime-level object records irreducible localized source contributions: which source components exist, their coupling weights, and the translations or incidence maps they generate. This is the identity-generating face. It contains more presentation information than a physical detector necessarily resolves.

### 2. Spectral realization

The completed transform \(\mathcal E\) combines localized contributions with the required background and boundary terms into a collective spectral object. Different source presentations may map to the same spectral data. The homotopy fiber

\[
\mathsf{Under}(P')=\operatorname{hofib}_{P'}(\mathcal E)
\]

is therefore the unresolved source multiplicity: distinctions still compatible with the same spectral realization.

### 3. Quadratic coherence

The Gram object \(Q=D^\dagger D\) tests simultaneous compatibility of the source and spectral presentations. It retains cross terms, so it is not a list of independent scalar checks. Its coherencer

\[
C:Q\longrightarrow R
\]

extracts failures of compatibility, completion, descent, or readout. The residue \(R\) is over-realization: structure present in the combined presentation that has not descended to a coherent record capability.

## Counterclockwise feedback

The map

\[
T:R\longrightarrow P_{\rm next}
\]

does not select a physical record. It converts a typed coherence residue into constraints on the next admissible source generator. Examples include:

- a normalization residue changing normalization parameters;
- a completion residue changing the permitted completion datum;
- an unresolved spectral multiplicity refining the source incidence family;
- a nonfaithful Gram coordinate requiring an enlarged probe family.

Residue modality must be preserved: a cutoff error cannot become a new source interaction, and a readout ambiguity cannot become arithmetic data without a source-derived map.

## What “resolution” means

Resolution is the simultaneous reduction of two different fibers:

\[
\mathsf{Under}=	ext{source distinctions not detected spectrally},
\]

\[
\mathsf{Over}=	ext{realized structure not coherently descended to records}.
\]

The process is resolved at the categorical level when:

1. the source-to-spectral comparison has the declared faithful quotient;
2. the Gram object retains all required cross pairings;
3. the final residue represents zero in the coherence quotient, not merely in one coordinate;
4. counterclockwise transport preserves the completion cone;
5. the global filler \(\Omega_{ABC}\) identifies the three local coherence routes modulo admitted vertex adjustments.

Our common fixture establishes item 5 at fixture level with \(H^2=0\); it does not establish the source-global version.

## Physical record gate

A coherent quadratic object is not yet a physical record. A sector must additionally provide

\[
\mathcal R:Q_{\rm coh}\longrightarrow\mathsf{Record}_{\rm phys}
\]

and prove that the coordinates used for resolution are faithful on the intended quotient. A state–effect value such as \(\operatorname{Tr}(\rho E_i)\) is a possible record weight, not by itself a unique selected record. No collapse, branching, or observer-independent selection follows from the categorical loop.

## If physical time is supplied

Given \(\tau:C\to T_{\rm phys}\), the same architecture may be indexed over physical time only if the source, spectral, Gram, residue, and feedback maps commute with the sector’s dynamical transport. Without those commuting cells, the diagram remains an inference/realization process rather than physical evolution.

## Disposition

The three-level model describes physical resolution as local identity generation, collective spectral realization, and quadratic compatibility descent, with the unresolved coherence residue constraining the next generator family. It separates underdetermination from over-realization and separates categorical coherence from physical readout. The exact missing physical objects are sector-specific time and record maps; categorical completeness can be studied without inserting either.
