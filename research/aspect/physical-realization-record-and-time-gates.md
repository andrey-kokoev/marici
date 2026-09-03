# Physical realization, record, and time gates

## Question

Which additional arrows are required before a mathematical attachment may be interpreted as a physical apparatus, its readout as a physical record, or its composition order as physical time?

## Claim boundary

This packet states necessary typing gates. It does not construct a sector-specific laboratory realization, detector model, state preparation, or physical clock.

## Mathematical attachment is not physical realization

An object

\[
(S,D)\in\mathcal S_{\rm inst}
\]

contains typed mathematical placement, interfaces, coherence, and readout data. A physical apparatus claim requires a separately defined realization on an admitted domain,

\[
\Phi:\mathcal S_{\rm inst}^{\rm adm}	o\mathcal P_{\rm app},
\]

where \(\mathcal P_{\rm app}\) is a declared category of physical systems and apparatus. It also requires:

1. a physical realization \(\Phi_0(S)\) of the undecorated source;
2. a realized apparatus \(\Phi(S,D)\);
3. a source-derived interface relating \(\Phi_0(S)\) to the realized apparatus;
4. preservation or explicit transport of the attachment incidence and coherence used in the mathematical claim.

Dimension agreement, matching diagrams, or a suggestive instrument name do not define \(\Phi\).

## State and effect gate

To interpret a mathematical attached state \(x\in X_D\), declare a physical state object and a representation or comparison map into the mathematical state semantics. To interpret a detector channel, declare an admitted physical effect \(E_i\) and its source.

Where the sector uses state-effect probabilities, require a positive normalized pairing such as

\[
p_i=\operatorname{Tr}(\rho E_i).
\]

The pairing assigns a weight to an effect-indexed possible record. It does not select one record or establish collapse, branching, or observer-independent actuality.

## Physical record gate

A mathematical readout

\[
r_D:X_D\to Y_D
\]

becomes a physical record only after a detector realization and a physical record map

\[
\operatorname{rec}:Y_D^{\rm phys}\to\mathcal R_{\rm stable}
\]

into a declared stable-record object, together with comparison to \(r_D\). The required chain is therefore:

\[
\text{physical state and apparatus}
\longrightarrow
\text{admitted effect}
\longrightarrow
\text{positive pairing}
\longrightarrow
\text{physical detector response}
\longrightarrow
\text{stable record}.
\]

A probability, a mathematical fiber, or an effect label alone is not a physical record.

## Physical-time gate

Let \(C_D\) denote the actual typed carrier of ordering information: a continuation category, transformer-composition category, filtration, or workflow partial order. Physical-time interpretation requires a source-derived map

\[
\tau:C_D\to T_{\rm phys}
\]

into a declared physical-time object, together with:

- orientation or clock authority;
- compatibility between the order/composition structure on \(C_D\) and that on \(T_{\rm phys}\);
- a readout or calibration identifying the physical clock coordinate;
- the sector boundary on which \(\tau\) is valid.

Without these data, vertical composition means composition order, continuation means typed interface transport, and a path means a parameter-space or categorical path. None is physical time by default.

## Independence of gates

The apparatus, record, and time gates are independent. A realized static apparatus need not supply a physical record. A detector record need not orient the attachment's construction order. A physical clock map need not make a coarse readout faithful.

## Finite diagnostic

A certificate checker treats these gates as required-field predicates. A full synthetic certificate passes all three. Removing the source-apparatus interface rejects physical realization. Supplying a probability without an effect source or stable record map rejects a physical-record claim. Supplying only a composition-order index rejects physical time; adding \(\tau\), orientation authority, order compatibility, and clock calibration admits only the typed time claim.

These are schema-level deliberate failures, not evidence that any physical realization exists.

## Disposition

Physical apparatus, physical record, and physical time require separate source-derived maps and authorities. The instrument-attached-system calculus supplies domains for those maps but does not construct them automatically. Mathematical compatibility and probabilities remain below the physical interpretation gate until the full relevant chain is supplied.
