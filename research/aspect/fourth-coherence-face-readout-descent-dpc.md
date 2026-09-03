# Fourth coherence face: readout descent DPC

## Question

Does the proposed coherence pyramid have a fourth independent face, and is that face readout/descent coherence?

## Claim boundary

This packet tests the structural role of readout. It does not claim that the metaphor of a geometric tetrahedron is canonical.

## Precise structure beneath the metaphor

Let \(\mathcal R\) be the realization category and let

\[
\operatorname{Att}:\mathcal R^{op}\to\mathbf{Cat}
\]

be attachment transport, understood as a pseudofunctor when identity and composition hold up to coherent cells. This supplies:

- forward realization arrows in \(\mathcal R\);
- contravariant attachment transport;
- unit, compositor, naturality, and associativity coherence.

Readout adds another indexed family \(\operatorname{Rec}(R)\) of stable record objects and maps

\[
Q_R:\operatorname{Att}(R)\to\operatorname{Rec}(R).
\]

For a realization arrow \(f:R\to S\), readout descent requires a comparison between

\[
Q_R(f^*A)
\quad\text{and}\quad
f_{\rm rec}^*(Q_S(A)).
\]

Equality or a specified comparison cell is an additional naturality condition. Attachment coherence alone does not supply it.

## DPC cycle

### Governing conjecture

The fourth face is readout/descent coherence: transported attachments must yield records compatible with transporting the records themselves. This is the missing interface between internal categorical coherence and observable output. The conjecture is hard to vary because neither realization transport nor attachment coherencers determine a map into record space.

### Rivals

1. **Unit face:** identity coherence is the fourth face.
2. **No fourth face:** realization, transport, and coherencers already determine every lawful readout.
3. **Literal tetrahedron:** the four faces follow solely from counting the existing ingredients, without another typed datum.
4. **Readout face:** a separately declared readout family and descent comparison provide an independent coherence gate.

### Risky consequences

The readout-face conjecture predicts two models with identical realization, attachment transport, units, and compositors but different readout-descent behavior. One readout family must commute with transport; another must fail while all internal attachment equations remain unchanged.

The unit-face rival predicts that identity laws distinguish these models. The no-fourth-face rival predicts that the failing readout cannot exist once attachment coherence holds. The literal-tetrahedron rival predicts a canonical fourth face without specifying record objects or readout maps.

### Falsification attempt

The checker uses two realization objects linked by one arrow. Each attachment fiber contains two objects, and transport is the identity, so every unit and composition law is strict. Record transport is also identity. A constant readout assignment at both realizations satisfies descent. A second assignment swaps the two record labels only at the source realization; it leaves all attachment data unchanged but fails both descent equations.

### Residual

The finite model establishes independence of the readout gate. It does not prove that the full structure is geometrically a tetrahedron. The exact object is more accurately an indexed attachment pseudofunctor equipped with a readout transformation and coherence cell.

### Disposition

Rivals 1 and 2 are rejected: unit coherence is internal to the attachment pseudofunctor, and internally coherent attachment transport does not determine readout descent. Rival 3 is rejected because face counting supplies no typed readout map. Rival 4 is provisionally retained as the explanatory interpretation of “fourth face,” provided the pyramid language is explicitly declared as a metaphor.

## Explanation

The first three obligations govern the internal construction: realization arrows, transported attachments, and agreement among composite routes. None specifies what becomes a stable record. Readout introduces a new codomain and a new comparison problem. That independent interface explains why a fourth obligation appears.

The concise four-obligation picture is:

1. forward realization coherence;
2. contravariant attachment coherence;
3. compatibility of transport with coherencers;
4. compatibility of transported attachments with readout descent.

## Disposition

The fourth face is not forced by geometric counting. It is justified by an independently typed readout transformation. Without that datum, there are only three internal coherence obligations and no lawful claim about records.
