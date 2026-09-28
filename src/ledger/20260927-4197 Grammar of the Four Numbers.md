# Grammar of the Four Numbers: Carrier Degree, Pair Arity, and Witness Escalation

## Purpose

This entry records a proposed reduction of the four Gram numbers (r = 11, l = 12, s = 4, c = 10) to a single input — the carrier cardinality N = 4 and uniform cross-coupling — with the claim that the observed constants are one self-coupling read at three depths of witnessing (identity, witness, record). The structural component is computed; the physical routing is proposed and flagged as such. The reduced ladder is:

| Quantity | Value | Origin | Status |
|---|---|---|---|
| N | 4 | carrier cardinality | input |
| N − 1 | 3 | multiplicity of the lower eigenvalue | structural |
| C(N,2) | 6 | unordered pairs | structural |
| N + C(N,2) | 10 | symmetric-Gram degrees of freedom (self + pairs) → C_U1 | structural |
| 2·C(N,2) | 12 | pairs × orientations (1:1 witnesses) → l_U1 | structural |
| 12 − 1 | 11 | the screened 12 → r | structural if (a) or (b) holds |

## Established within this project (computed)

For a symmetric N-point Gram G = self·I + cross·J with uniform cross-overlap:

- eigenvalues: self + (N−1)·cross (multiplicity 1) and self − cross (multiplicity N−1); gap = N·cross.
- N = 4 forces: eigenvalue gap 4 (= l_SU2), multiplicity 3 (= three generations), lower eigenvalue self − cross.
- Pair structure of the 4-point carrier: C(4,2) = 6 unordered pairs; 12 = 2·6 directed pairs (the 1:1 witnesses, = l_U1); 10 = 4 + 6 independent symmetric-Gram entries (= C_U1); 16 = 10 + 6 = 4² (symmetric + antisymmetric decomposition of the 4×4 relation space).
- S12 carrier under S4×S4×S4 (three generations of 4), uniform cross: spectrum {23 (×1), 11 (×11)} for self = 12; {22 (×1), 10 (×11)} for self = 11. The eigenvalue 11 = 12 − 1 coincides with N − 1 = 11.

## Proposal: the escalation ladder

The four numbers are not four inputs. With N = 4:

| Quantity | Value | Reading |
|---|---|---|
| N | 4 | carrier cardinality |
| N − 1 | 3 | generations (multiplicity) |
| C(N,2) | 6 | pairs |
| 2·C(N,2) | 12 | l_U1 — identity stage, full bidirectional structure (hidden diagonal) |
| 12 − 1 | 11 | r — witness stage, screened once |
| 12 − 2 | 10 | C_U1 — record stage, symmetric remainder 4 + 6 |

Proposed mechanism: each act of witnessing or recording consumes one unit of cross-coherence; the visible eigenvalue drops by one per stage (12 → 11 → 10 over identity → witness → record). The "lazy 12" is 12 renormalized by the unit cross-coupling, or equivalently 12 minus the reflexive (unwitnessed) direction. Both readings are checkable: (a) spectral — the S12 carrier Gram under S4×S4×S4 must show the self-overlap eigenvalue one unit below the U(1) eigenvalue; (b) arity — the witness count must exclude the reflexive relation. In words: at identity nothing is spent (the node carries 12, hidden on the diagonal); to witness, the relation pays one unit of coherence (you see 11); to record, it pays again (you see 10 = 4 + 6, only the symmetric, time-flat content survives; the antisymmetric part is spent for good).

## Program (a) — executed: the S12 Gram under S4×S4×S4

**Setup.** S12 partitioned into three generations of 4 points (S4×S4×S4 acts within each block). Gram entries by orbit: self s, within-generation cross a, between-generation b. Eigenvalues by block structure:

```
s + 3a + 8b   (×1)     fully-symmetric mode
s − a         (×9)     within-block antisymmetric
s + 3a − 4b   (×2)     cross-block odd
```

**Uniform cross (s = 12, a = b = 1):**

```
λ = 23   ×1
λ = 11   ×11
```

The eigenvalue 11 = 12 − 1 appears with multiplicity 11. Two structural reasons coincide in the S12 carrier: 11 = N − 1 (the other points) and 11 = 12 − 1 (the screened self-coupling). The r-model (s = 11) gives λ = 10 ×11, placing C_U1 = 10 on the same ladder.

**Caveat.** 12 itself does not appear as an eigenvalue in the uniform model; it is the diagonal self-coupling s. "l_U1 = 12" must therefore be read as the self-coupling whose spectrum shows 11, not as a spectral line. The lazy-12 thesis survives precisely in this form: the full 12 is hidden on the diagonal; physics sees the screened 11.

**Strict four-point form.** Within one generation (4×4 Gram, entries {s, a}), the one-below condition s − a = (s + 3a) − 1 forces 4a = 1, i.e., the within-generation cross-overlap a = 1/4 — an independently derivable constraint to check.

## Program (b) — FCC 12:4 = 3: dimension or coincidence

Computed in the lattice experiments: FCC tight-binding gives band shifts +12 (Γ, L) and −4 (X, W flat band), so 12 : 4 = 3 = spatial dimension falls out of the dispersion. Assessment: real lattice physics, but the identification with l_U1 : l_SU2 remains an analogy unless the routing of the band data through the carrier Gram is exhibited. The two lattices (FCC 12-neighbor shell; S12 carrier) have not yet been shown to be the same object.

## Falsified hypotheses (recorded so they are not re-run)

- SU(2)-valued edge transport on the cube with flat face holonomy: satisfiable but under-determined; edge traces do not quantize to {11, 12, 4, 10}.
- S4-doublet (D3) edge transport with flat faces: 6⁷ = 279,936 solutions (6 faces, 5 independent closure conditions); no edge is favored.
- "10 = 12 − 2 unwitnessed directions": falsified by count; cube-graph pairs with no common neighbor are 16, not 10.

## Positive structural facts from the lattice program

- FCC tight-binding: band eigenvalues s + 12t (Γ) and s − 4t (X, W flat band); 12 : 4 = 3 = spatial dimension.
- Cube closure counting: 6 faces impose only 5 independent flatness conditions (one global holonomy relation); 12 − 5 = 7 free edge values.

## Full tower: descend and ascend (9 rungs, closed cycle)

The escalation is not three rungs — it is nine, from 12 down to 4, with the floor regenerating the top.

**The descend (witnessing/recording, −1 per act):**

| rung | value | free | fixed (history) | C(v,2) | v+C(v,2) | status |
|---:|---:|---:|---:|---:|---:|---|
| 1 | **12** | 12 | 0 | 66 | 78 | l_U1 — full S12 carrier |
| 2 | **11** | 11 | 1 | 55 | 66 | r — one point fixed |
| 3 | **10** | 10 | 2 | 45 | 55 | C_U1 — two points fixed |
| 4 | 9 | 9 | 3 | 36 | 45 | first value below spectral bottom 11 |
| 5 | 8 | 8 | 4 | 28 | 36 |  2³ — cube, full outward engagement |
| 6 | 7 | 7 | 5 | 21 | 28 | prime, Fano/octonion separation |
| 7 | **6** | 6 | 6 | 15 | 21 | 6 = C(4,2) — internal carrier pairs |
| 8 | **5** | 5 | 7 | **10** | 15 | 5 = N+1 (witness). C(5,2)=10 unifies both readings: 6 internal + 4 witness spokes = C_U1 |
| 9 | **4** | 4 | 8 | 6 | **10** | floor = N = l_SU2 — minimal S4 carrier. C(4,2)=6 pairs, symmetric dof 10 |

**Three triplets:**

| Triplet | Rungs | Values | Phase |
|---|---|---|---|
| 1 | 1–3 | **12, 11, 10** | Coherence. Named constants. The square 4+6+2=12 closes here. "I am fully coherent and forward-compatible." |
| 2 | 4–6 | 9, 8, 7 | Transition. Interaction grid (3²), outward engagement (2³), irreducible oddness (7). Dof drops below the persistent spectral bottom 11. |
| 3 | 7–9 | **6, 5, 4** | Floor. 6 = C(4,2) pairs, 5 = N+1 (the witness, C(5,2)=10 unifies the two 10s), 4 = N. Seed of regeneration: 4×3 generations = 12. |

**The cycle closure:**

```
floor 4  ──  N(N−1) = 4×3 = 12  ── rung 1
       ──  N² = 16 = 12 + 4   ── rung 1 + rung 9 (the square of the carrier
                                      decomposes into directed pairs + diagonal)
```

The two factorizations of 12 — 2×6 (orientations × pairs) and 3×4 (generations × carrier) — are the same count: N(N−1) = 4×3 = 12. The ladder is a closed cycle: the floor's own square re-emits the top.

**The spectral bottom never moves:** the n-point Gram at every rung has bottom eigenvalue 11 ×(n−1). The descend line 13−r starts above it (12), crosses it at r=2 (11), then passes below. The name r = 11 marks the crossover between the descending dof and the persistent screening line.

## Open programs

1. Route the FCC band data through the carrier Gram (not just the S12 block model), or exhibit that the FCC 12-shell and the S12 carrier are the same object.
2. Derive the within-generation cross-overlap a = 1/4 (forced by the one-below condition on the 4-point restriction) independently of the arity reading.
3. Show how QM, GR, and the SM fall out of G under the reduced parameterization. Nothing in this entry touches the physical routing; the reduction reorganizes the constants, not the derivations.

## Boundaries

Recording this structure here does not upgrade it to a theorem. The spectral facts are arithmetic; the escalation ladder and the lazy-12 reading are proposals with stated falsifiable programs.