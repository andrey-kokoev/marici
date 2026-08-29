# Four-atom pentagon holonomy is the first associator obstruction

## Correction

A nontrivial three-atom phase is not automatically a defect. In a non-strict constructor theory, it may be the source-authorized associator
\[
\alpha_{p,q,r}:
(\mathcal M_p\otimes\mathcal M_q)\otimes\mathcal M_r
\overset{\sim}{\longrightarrow}
\mathcal M_p\otimes(\mathcal M_q\otimes\mathcal M_r).
\]

The three-atom gate is therefore constructive and typed:

- construct \(\alpha_{p,q,r}\);
- establish its source authority;
- prove that it preserves or coherently transports every interface annotation;
- identify its gauge class;
- verify naturality with the nine authorized operations.

Literal equality is required only if the source theory declares strict associativity.

## When a three-atom phase is defective

A phase or other intertwiner at three atoms fails only when at least one condition holds:

1. the source assembly is explicitly strict and the phase is nontrivial;
2. no source-authorized associator realizes it;
3. it changes a non-gauge boundary annotation;
4. an authorized observer detects a forbidden change;
5. it is not natural under cutoff, Adams, seam, Real, reciprocal, or completion transport.

Valid determinant-line and quantum coefficient systems may have nontrivial associators and must not be rejected merely for being non-strict.

## Typed associator packet

The associator carries more than a scalar. Define its digest by
\[
\mathsf A_{p,q,r}
=
(\alpha^{\mathrm{seam}},
 \alpha^{\det},
 \alpha^{\mathrm{Adams}},
 \alpha^{G},
 \alpha^{\mathrm{grade}},
 \alpha^{\mathrm{sheet}},
 \alpha^{\mathrm{end}},
 \alpha^{\infty}).
\]

Each component may be a strict identity, a gauge equivalence, or a nontrivial authorized intertwiner. The classification is fixed by the constructor theory, not inferred from terminal scalar behavior.

## Four-atom pentagon

For four packets \(M_p,M_q,M_r,M_t\), there are five parenthesizations. The two composite routes from
\[
(((M_p\otimes M_q)\otimes M_r)\otimes M_t)
\]
to
\[
M_p\otimes(M_q\otimes(M_r\otimes M_t))
\]
must agree.

Writing associators schematically, the pentagon is
\[
\alpha_{p,q,r\otimes t}\,
\alpha_{p\otimes q,r,t}
=
(1_p\otimes\alpha_{q,r,t})\,
\alpha_{p,q\otimes r,t}\,
(\alpha_{p,q,r}\otimes1_t).
\]

This equality is interpreted in the authorized higher morphism class and includes every typed annotation.

## Phase form and the 3-cocycle law

If the associator is scalar phase multiplication
\[
\alpha_{p,q,r}=\omega(p,q,r),
\]
then the pentagon becomes
\[
\omega(q,r,t)\,
\omega(p,qr,t)\,
\omega(p,q,r)
=
\omega(pq,r,t)\,
\omega(p,q,rt).
\]
Equivalently,
\[
\delta\omega=1.
\]

The first gauge-invariant associator obstruction is the pentagon holonomy
\[
\delta\omega\neq1.
\]

A change of trivalent gauge modifies \(\omega\) by a coboundary but leaves its cohomology class and pentagon validity appropriately invariant.

## Minimal hostile I: unauthorized associator

Every atomic and binary constructor passes. At three atoms, the two parenthesizations differ by a phase \(\omega\neq1\), but the source theory supplies neither a non-strict associator nor gauge authority for that phase.

This fails at the three-atom authority gate, before the pentagon is considered.

## Minimal hostile II: four-atom holonomy

Every triple has an individually authorized phase associator. Choose four atoms so that the product of phases along one pentagon route differs from the product along the other:
\[
\delta\omega(p,q,r,t)\neq1.
\]
All one-, two-, and three-atom local tests pass. The four-atom assembly is path-dependent in a gauge-invariant way.

This is the first irreducible associator-coherence falsifier.

## Observer caution

A determinant or scalar Mellin observer may annihilate pentagon holonomy. Therefore the checker compares the typed associator composites before observer projection.

Conversely, a nontrivial determinant-line phase may be fully legitimate if the determinant observer is itself a representation of the authorized associator. Nontriviality is not failure; unauthorized or incoherent nontriviality is failure.

## Refined finite attack path

### Two atoms

Verify binary assembly, mixed analytic interaction, primitive arithmetic flux, seam cross-terms, and scalar shadows.

### Three atoms

Construct and type the associator; determine strict, gauge, or nontrivial authorized status.

### Four atoms

Verify the pentagon and detect any 3-cocycle obstruction.

### Finite families

Use the pentagon and unit coherence to generate path-independent reassociation throughout the finite assembly category, together with the additional critical joins from the nine operations.

### Completion

Prove the coherent assembly maps and associators are uniformly continuous in the projective exponential topology and compatible with bounded-energy realization.

## Interaction with the five margins

The pentagon certificate remains constructor-level. It is not a numerical coercivity margin. However, failure of uniform continuity of an otherwise valid associator at completion can invalidate the common Green system before the five margins are applied.

Thus the completed order is:

1. binary assembly;
2. authorized associators;
3. pentagon and finite coherence;
4. uniform completion of coherent assembly;
5. five-margin coercivity;
6. spectral identification.

## Next executable checker

For four distinct prime atoms:

1. construct all five parenthesized packets;
2. compute all associator arrows;
3. compose the two pentagon routes;
4. compare their complete typed digests;
5. quotient only source-authorized gauge;
6. report the first non-gauge discrepancy;
7. separately verify that scalar projections do not hide it.

This checker accepts nontrivial coherent phases and rejects only unauthorized associators or nontrivial pentagon holonomy.
