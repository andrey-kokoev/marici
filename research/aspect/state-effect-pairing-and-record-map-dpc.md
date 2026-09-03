# State–effect pairing and physical record map DPC

## Question

Does invariant state–effect pairing fully supply readout descent, or is a stable physical record map an independent gate?

## Claim boundary

This packet proves independence in an exact two-label finite model. It does not assert that every Marici readout is quantum, projective, or binary.

## Typed readout module

For each realization context \(R\), use:

- states \(\rho\) in a positive normalized state object;
- effects \(E_i\) in an admitted effect family;
- pairings \(p_R(i)=\operatorname{Tr}(\rho E_i)\);
- a physical record map \(r_R:i\mapsto \operatorname{Rec}(R)\).

A realization transport carries states, effects, and labels. Pairing descent requires

\[
p_S(\sigma(i))=p_R(i).
\]

Record descent is the separate square

\[
r_S(\sigma(i))=\tau(r_R(i)),
\]

where \(\tau\) is the declared record transport.

## DPC cycle

### Governing conjecture

Invariant state–effect pairing already determines coherent physical records, so the record map adds no independent obligation.

### Rivals

1. Probability invariance determines records.
2. A record is merely the effect label.
3. Pairing invariance and record descent are independent interfaces.
4. Record descent follows only from an additional faithful identification of effects with records.

### Risky consequences

If the conjecture is correct, two models with identical transported states, effects, labels, and probabilities cannot differ on record descent. A countermodel preserving all pairing data while breaking only the record square rejects it.

### Falsification attempt

Use a two-dimensional rational model with state \(\rho=\operatorname{diag}(1,0)\), effects \(E_0=\operatorname{diag}(1,0)\) and \(E_1=\operatorname{diag}(0,1)\), and swap transport \(U\). Conjugation swaps state, effects, and labels while preserving each paired probability.

With identity record transport, the descending target record map reverses its two label values. A rival target record map leaves them unreversed. Both models have identical states, effects, and probabilities, but only the first record square commutes.

### Residual

The finite countermodel establishes logical independence. A physical application still requires source authority for its state object, effect family, transport, and stable record map.

### Disposition

The governing conjecture and Rival 1 are rejected. Rival 3 is retained. Rival 4 states a sufficient extra premise, not a consequence of pairing alone.

## Explanation

Probabilities are state–effect values attached to possible records. They do not construct the record map. The equipment transports internal attachment and effect structure; the readout module needs both invariant pairing and a separate map to stable physical records.

## Disposition

Readout coherence has two faces: probability descent and record descent. Neither may be silently substituted for the other.
