# Deeper prior search: rung diagrams, coherence fibers and realization

This is a local source-reading audit, not a new construction or fresh execution
of the cited checkers. Searches covered research, docs, ledger references and
selected formal source files. Names and numbers alone were not used to identify
different towers.

## 1. Earlier nine-rung specification recovered

`research/nima/label-from-to-fibration-tower.md` records an operator-proposed
nine-row correspondence:

| Rungs | Proposed gauge names |
|---|---|
| 12,11,10 | U(1), SU(2), SU(3) |
| 9,8,7 | U(1)^2, SU(2)^2, SU(3)^2 |
| 6,5,4 | U(1)^4, SU(2)^4, SU(3)^4 |

Its actual construction is a retained-total fibration recurrence selecting
label, from, and to. Each total is equivalent to the original row type and
retains its construction history. Neither gauge groups nor the multiplicities
1,2,4 are derived by that equivalence. The source explicitly distinguishes
this presentation tower from the dimension-reducing Gram tower.

The later operator-confirmed `rung-transport-diagram-and-fixed-reference.md`
uses 9,8,7 as horizontal transport roles, not intermediate states. These are
not interchangeable descriptions without a stated adapter or revision.

## 2. Genuine coherence-extension fibers already specified

`research/nima/coherence-realization-depth-is-a-dependent-filler-tower-not-a-source-cutoff.md`
gives

    R_(k+1) = Sigma(r:R_k) Fill_k(r),
    fib(projection,r) equivalent to Fill_k(r).

It explicitly separates analytical presentation i, source parameter iota and
coherence-cell degree k. None is automatically time, spatial dimension or an
arithmetic cutoff. Objects, comparison maps, triangle comparisons and a
comparison between their tetrahedral routes are typed separately.

A higher extension requires a specified boundary and a filler, not merely a
higher numeral. An existing signed tetrahedron in the referenced source is
already coherent at its recorded strength; its remaining positive/metric
realization problem is not automatically a missing homotopy degree.

## 3. Formal implementations, not just prose analogies

Inspected `research/nima/agda/RetainedTetrahedralPackage.agda` directly:

- `Package = Sigma Surface Filler`;
- actual surface/filler projections and reassembly;
- six shared-edge recovery equalities;
- marked path-horn completion and `horn-iso`.

This reuses a theorem about path-horn completion. It does not assert that every
fully prescribed surface fills, or that every arbitrary relation is invertible.

Inspected `research/voevodsky/agda/DGPyramidFiller.agda` directly:

    AdmissibleFiller = Sigma K (delta K = discrepancy) x frame conditions.

The frame separately requires support, endpoints, generic-Q and Rees/Cartier
preservation. Forgetting these conditions yields a weaker boundary filler;
there is deliberately no automatic converse constructor.

These are more concrete starting points than inventing a new generic forgetful
map. Their existing reports describe formal checks; this search did not rerun
Agda or instantiate them on the current P/N field.

## 4. Current software T9 is already selected

`research/nima/pinned-T9-software-contract.md` supersedes historical statements
that the software policy remains unselected. It fixes incoming promotions at
depths 1 and 2 with inherited target keys: 137 -> 32 -> 32, with exactly 977
admitted original leaf pairs. T8/T7 are its indexed presentations; complete
leaves, endpoints, weights and histories remain recoverable.

`research/strominger/generating-horizontal-schedule-v1.md` separately constructs
a candidate with twelve primitive input arrows and generation of 137 slots
inside the horizontal operation. The adapter between initial domains must not
be erased when composing these results.

`research/kitaev/transport-t9-coherence-and-scattering-prior-work-recovery.md`
also corrects the claim that no Hamiltonian descent exists: conditional
Hamiltonian and energy transport through retained T9 are already constructed
in `interface-preserving-carrier-hamiltonian.md` and
`retained-hamiltonian-observer.md` under research/strominger. Physical source
selection, calibration and comparisons with particular scattering systems
remain distinct questions.

## 5. The new PN rotation obstruction has an existing conceptual home

`research/kitaev/realization-fiber-coherence-rung.md` defines a fiber of
realizations over one abstract capability profile. Comparisons must intertwine
named constructors, observations and viewing forms. Equal profile or equal
metric is insufficient: its explicit two-dimensional example has incompatible
characters (-2 versus 0).

Our P/N rotation traces (3 versus 0 on corresponding projector images) are
another instance of the same necessary character test. This suggests comparing
realization components inside a fiber before treating the discrepancy as a new
Postnikov degree. No formal adapter or identification of the two examples is
claimed.

That note's eighth rung belongs to a different canonical tower. Its 36 interval
cells are not identified with the 36 field components; equal counts do not
supply such a map.

## 6. Mixed coherence is a separate question

`research/nima/rh-two-tower-four-structures-need-a-mixed-interchange-cell.md`
distinguishes forward composition from source realization and requires a cell
comparing Realize(g composed f) with Realize(g) composed Realize(f). Individually
valid generator realizations need not preserve composition: its Pauli example
has commuting abstract generators but anticommuting realizations.

This is relevant to simultaneous field rotation and PN conversion. Separate
valid maps do not establish a commuting rotation/conversion square. Our trace
obstruction addresses one strict square; no higher filler or permitted boundary
modification follows automatically.

## 7. Historical Postnikov terminology requires correction

Inspected `research/nima/checkers/check_postnikov_tower.py`. It computes scalar
powers and proposed correction factors, with comments assigning S4 factors to
homotopy degrees. It does not construct homotopy groups, a space, projections,
or cohomological k-invariants. A nonabelian S4 cannot itself be pi_n for n>=2.
The later `research/strominger/hamiltonian-descent-wg-and-postnikov-clues.md`
explicitly records this boundary and notes that BS4 is already a 1-type.

The stronger general reference is
`research/kitaev/ascending-rungs-stabilizes-the-law-and-moves-the-problem-to-truncation.md`:
uniform simplicial/hypercrossed structure, residual kernel modulo authorized
boundaries, and task-relative factorization through a truncation. These general
results do not assign the native numerical labels to Postnikov stages.

## Synthesis

The corpus already supports a richer interpretation than a stack of geometric
coordinate dimensions: retained presentations, generating transports, coherent
realizations and comparisons among realizations. The user's proposed grouping
has real ancestry, including an older gauge-multiplicity conjecture.

The next question should bind the current decorated P/N configuration to those
existing typed interfaces, keeping separate:

1. presentation rung;
2. coherence degree;
3. source-changing realization operation;
4. internal automorphism or realization-fiber component;
5. physical spacetime readout.

No source inspected here establishes the new 36-component configuration as
rung12 or the designated rung4 readout as the whole Lorentzian 4D spacetime.
This is a bounded search result, not a global absence theorem. No source rules,
production code, earlier ledger checkpoint, or proof status were changed.
