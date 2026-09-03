# Optical port attachments and the domain of reindexing

## Question

Can an attachment indexed category be derived from a concrete optical source model, and which optical network maps actually admit pullback of instruments?

## Claim boundary

This packet constructs a finite typed-port optical model. It derives an attachment functor only on a restricted class of port-cartesian maps. It does not model continuous fields, loss, detector dynamics, or a laboratory realization.

## Typed optical networks

An optical network \(N\) consists of:

1. a finite directed graph of components and ports;
2. for each port \(p\), a mode object \(H_p\), including propagation direction, frequency band, and polarization space;
3. component maps between tensor products of incident mode objects;
4. boundary incidence identifying externally accessible ports.

For the finite diagnostic, a mode object is represented by a tuple

\[
(\text{direction},\text{band},\text{polarization dimension}).
\]

This tuple is a source type, not merely a display label.

## Optical attachments

An attachment over \(N\) is occurrence-indexed data

\[
D=(I_D,\ell,K,c,\kappa),
\]

where:

- \(I_D\) is a finite set of detector occurrences;
- \(\ell:I_D\to\operatorname{Port}_{\partial}(N)\) places each occurrence at an accessible boundary port;
- \(K_i\) is the detector acceptance type;
- \(c_i:H_{\ell(i)}\to K_i\) is a typed coupler or analyzer map;
- \(\kappa\) records shared-resource, coherence, and readout compatibility.

A placement is admissible only when the port mode lies in the detector acceptance domain and the coupler is typed. Thus \(\operatorname{Att}_{\rm opt}(N)\) is derived from the boundary-port and mode data of \(N\), not chosen independently.

## Reindexing domain

Let \(f:M\to N\) be a typed optical-network map. Pulling back a detector occurrence at \(p\in N\) requires a source boundary port over \(p\) with compatible mode type.

A canonical occurrence-preserving pullback exists when the square of accessible typed ports is cartesian over every attached locus. In the finite model this means:

1. every attached target port has exactly one accessible source preimage;
2. its mode type is preserved;
3. incidence and orientation are preserved;
4. the coupler composes with the supplied mode transport;
5. shared attachment constraints pull back naturally.

Under these conditions, each occurrence has a unique transported locus and

\[
f^*:\operatorname{Att}_{\rm opt}(N)\to\operatorname{Att}_{\rm opt}(M)
\]

is defined.

## Obstructions

Three source-level obstructions occur before coherence or readout:

- **deletion:** an attached target port has no source preimage;
- **branch ambiguity:** it has several preimages and no replication or selection policy;
- **mode mismatch:** a preimage exists but its direction, band, or polarization type does not support the coupler.

Deletion makes pullback undefined. Branch ambiguity produces a family of possible pullbacks rather than a canonical functor. Mode mismatch rejects the transported attachment.

Therefore the natural base is not the category of all optical-network maps. One may instead use:

- a subcategory \(\mathcal S_{\rm opt}^{\rm cart}\) of attachment-cartesian maps;
- a partial indexed category on all maps;
- or a correspondence-valued semantics retaining ambiguous preimages.

Silently choosing one branch would manufacture attachment data.

## Composition

Unique typed preimages compose: if \(L\to M\to N\) are port-cartesian at every attached locus, then the unique preimage in \(L\) is the composite preimage. Mode transports and couplers compose, giving

\[
(gf)^*=f^*g^*
\]

up to the declared coherence of mode transport. This derives the indexed-category law on the restricted base.

## Finite diagnostic

A target network has horizontal and vertical polarization ports with matching detectors. A typed bijective boundary map admits unique pullback of both occurrences. Separate hostile maps delete the vertical port, duplicate the horizontal preimage, and replace the horizontal mode by an incompatible vertical mode. Each fails at its predicted gate. Two admissible renamings compose and produce the same pulled-back placement as direct reindexing.

## Disposition

A concrete optical attachment category can be derived from typed boundary ports, detector acceptance types, couplers, and coherence constraints. Contravariant reindexing is not available for arbitrary optical maps: it is canonical on port-cartesian typed maps, partial on deletions and mismatches, and correspondence-valued under unresolved branching. This identifies the first source-derived obstruction theory for \(\operatorname{Att}_{\rm opt}\).
