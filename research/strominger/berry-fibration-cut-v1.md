# A concrete Berry-domain cut in the marked-fibration tower

## Question and construction

The prior tetrahedral Berry calculation found the right physical data but did not specify a serialization stage or cut. This construction supplies a **candidate cut with an explicit operation**, using the existing `TableFibrationCycle` interface. It does not assert that this is the unique intended meaning of the operator's cut.

Read the actual stored four-face Pauli projectors from `research/voevodsky/results/electron_tetrahedral_spinor_store.json`. Check them against the ordered negative-polarization tetrahedral source. Do not insert their precomputed Berry phases as labels.

Represent their sixteen coefficients by the existing three-column schema:

| label | from | to |
| --- | --- | --- |
| complex coefficient (P_i)_ab | projector index i | matrix-entry port (a,b) |

All endpoint pairs are unique. Matrix-entry orientation, complex coefficients and source indices are retained.

Instantiate `group-from`: its four fibers are exactly the four projectors. At this stage define the cut for the ordered face (i,j,k) to retain those three fibers. Its twelve rows expose the three quantum lines and their comparison operations; keep the fourth fiber as the complement, not as secretly accessible data in the face reader. Selected rows plus complement reconstruct all sixteen source rows.

This is an explicit source-index restriction at a named serialization stage. It is not a claim that an isolated face reconstructs the entire tetrahedron.

## Independent operation on the cut

The native row reader computes

    B_ijk = sum over a,b,c of row(i,a,b) row(j,b,c) row(k,c,a).

It does not decode a matrix and call the previous matrix reader. It yields exactly `Tr(P_i P_j P_k)` for all four faces. Normalizing its nonzero value gives the Berry phase under the prior geodesic/overlap convention.

The comparisons are the normalized nonzero overlaps between these actual rank-one lines. Their cyclic product is the formed triangular loop; its phase is not set to one. The tetrahedral boundary law relates the four such loop phases. The full coefficient and port data remain available when the phase is read, so scalarization does not replace the domain.

Recovering `-Tr(P_i sigma_a)` gives the original regular tetrahedral normals. Thus the tetrahedral representation is tied to the actual projectors and incidence, not inferred from four names. No infinite FCC lattice or lattice dynamics is asserted by this finite tetrahedral representation.

## Serialization/deserialization square

Implemented the actual marked-column grouping and restoration formulas from `TableFibrationCycle.agda`, including selector and empty fibers. Checked:

- all three column choices reconstruct the sixteen-row table;
- all three choices reconstruct each twelve-row face cut;
- grouping by source, reversed unpacking, then repeating with the exchanged endpoint types returns the original table in the existing four-step convention;
- reading each face directly, after marked reconstruction, and after the complete four-step cycle gives the same complex Bargmann invariant;
- cutting the restored source gives exactly the same selected data as the original cut.

The endpoint exchange in the middle of the cycle is representation wiring, not physical transport or a physical time step. The previously formalized generic recovery theorem supplies the general table interface; this work is a fresh exact finite implementation test, not a fresh Agda compilation or a new arbitrary-Resolve certification.

## Strongest discriminating tests

Complex conjugation of all coefficient rows leaves their entry magnitudes unchanged and reverses every Berry face phase. A magnitude-only serialization therefore fails this domain. Transposing matrix-entry ports without accounting for orientation also reverses the loop phase. Removing one required coefficient is rejected as an incomplete domain rather than filled with zero.

All four cut phases remain `i,-i,i,-i` in ascending face order. Their oriented tetrahedral boundary product is one.

## Disposition

**Constructed at a bounded candidate scope:** a concrete marked-fibration-stage cut, a phase-bearing triangular domain, a source-tied tetrahedral realization, and an independently computed operation-preservation square. The previous missing stage/cut map is supplied for this fixture.

The source projectors, Pauli operations, geodesic convention and face query are supplied inputs. This does not show that WG selects those inputs, that every physical-law domain has this form, or that four sampled lines determine arbitrary continuum Berry transport. The governing conjecture remains open. The candidate cut definition is frozen here so later failures cannot be hidden by changing it.

Fresh verification: `uv run --with sympy python research/strominger/checkers/check_berry_fibration_cut.py`, exit zero through structured-command (`structured_command_execution:e_42200_1792519578769484000_21`). Receipt: `research/strominger/results/berry-fibration-cut/verification.json`, with hashes of the actual source store, table kernel, equivalence report and checker. No other-owner artifacts were rewritten.
