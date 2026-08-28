# Frozen higher projective-transport signature v13

## Status

Version 13 is a new frozen local candidate. Version 12 remains unchanged and falsified.

v13 admits coherent projective transport without demanding an honest global unitary lift. It also prevents the repair from becoming an unrestricted higher-cell escape hatch.

## Projective repair

The Pauli torus packet carries a (PU(2)) representation with local (U(2)) lifts and multiplier

\[
\omega((a,b),(c,d))=(-1)^{bc}.
\]

v13 retains the multiplier as a normalized 2-cocycle. Rephasing local lifts changes it by a coboundary. An honest (U(2)) representation exists only after the obstruction class is trivialized.

## Higher coherence without vacuity

Each packet must declare a finite Postnikov profile before hostile replay: maximum obstruction degree, coefficient objects, and k-invariants. At every declared degree, the cocycle equation is checked exactly.

Replay cannot create a new cell or filler. If a hostile exposes an obstruction above the preregistered profile, the packet is rejected; the checker cannot repair it after seeing the answer.

## First unused hostile

The normalized degree-three cocycle on (\mathbb Z_2)

\[
\omega_3(a,b,c)=(-1)^{abc}
\]

satisfies its full cocycle equation and has nontrivial value at ((1,1,1)). v13 retains it as a source-declared next Postnikov obstruction rather than forcing it into a matrix multiplier.

## Cross-sector consequence

Benincasa's conductor collision retains the rank-two value/derivative module of the dual-number fiber. v13 says its full matrix transport may itself have only a projective lift; the central obstruction must be tested before selecting a strict frame.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v13.py
```
