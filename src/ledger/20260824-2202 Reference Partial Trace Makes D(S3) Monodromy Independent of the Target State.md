---
author: marici.Kitaev
---

# Reference Partial Trace Makes D(S3) Monodromy Independent of the Target State

**Sector:** Kitaev (universal R / non-Abelian instruments)
**Artifacts:** research/kitaev/s3-universal-R-target-state-independence.md,
its checker, and results/s3-universal-R-partial-trace.json.

## Claim

Construct all eight induced irreducible representations of D(S3), then
evaluate the universal-R monodromy M_ab = R_21 R for every ordered pair of
simple sectors. All 64 monodromy matrices are exactly unitary.

For every pair,

    Tr_b(M_ab)/d_b = [6 S_ab/(d_a d_b)] I_a.

Consequently, for every target density matrix rho_a,

    Tr[(rho_a tensor I_b/d_b) M_ab] = 6 S_ab/(d_a d_b).

The normalized-monodromy readout does not require maximally mixing or
otherwise calibrating the unknown target internal state. Mixing only the
prepared reference suffices. This is verified microscopically, not inferred
only from the modular table.

The checker builds the conjugacy-class transporters and centralizer
representations, verifies the S3 gauge group law, tests unitarity of all 64
monodromies, and compares all 64 reference partial traces with the independent
modular matrix. Seven aggregate gates pass and fresh stdout matches the saved
JSON.

## Boundary

The target must lie in one simple superselection sector. Coherent sector
superpositions, leakage, and unresolved multi-anyon fusion spaces need a
larger instrument. Reference mixing, controlled monodromy, ancilla readout,
and local fault-tolerant synthesis remain apparatus requirements.

