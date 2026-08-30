# Kitaev topological-sector programme index

Owner: `marici.Kitaev`

Source programme: `research/nima/kitaev-topological-sector-onboarding.md`

## Hard core

The finite toric code must be derived from one labelled periodic cellulation,
but its physical interpretation is not supplied by incidence alone.  The
quantum coefficient lens adds Pauli commutation, a stabilizer Hamiltonian,
state/effect pairing, and physical instruments.

## Current packets

- `toric-code-source-syndrome-logical-algebra.md` — WP1--WP3: frozen source,
  commutation-derived syndromes, logical quotients, and intersection pairing.
- `toric-code-selection-readout-decoding.md` — WP4--WP6: selection layers,
  probe completeness, and decoder noncanonicity.
- `checkers/check_toric_code_wp1_wp6.py` — dependency-free exact GF(2)
  checker.
- `results/toric-code-wp1-wp6.json` — exact generated checker output.
- `toric-code-braiding-boundaries-perturbation.md` — WP7--WP9.
- `toric-code-cross-sector-appraisal.md` — bounded WP10 comparison.
- `checkers/check_toric_code_wp7_wp9.py` and
  `results/toric-code-wp7-wp9.json` — exact continuation checker and output.

## Live frontier

WP1--WP10 are dispositioned at their explicitly finite strengths.  Open
successors are non-Abelian ribbon typing, general planar-code families,
generic perturbative spectral flow, and thermodynamic/colimit statements.

Sprint 2 is indexed separately in
`research/kitaev/topological-sector-sprint-2-index.md`.

The first autonomous successor is
`research/kitaev/wilson-parity-effect-versus-instrument.md`, with checker and
milestone under the same owner directory.

The protected/source-derived completion is
`research/kitaev/toric-source-instrument-and-capability-fiber.md`; its
cross-sector comparison is
`research/kitaev/cross-sector-instrument-group-appraisal.md`.

The non-Abelian successor begins at
`research/kitaev/s3-quantum-double-ribbon-typing.md`; it freezes the exact
group/anyon census and records the full ribbon-category typing blocker.
The next bounded refinement,
`research/kitaev/s3-oriented-ribbon-operator-algebra.md`, freezes one
primary-source orientation convention and derives the 36-dimensional
fixed-ribbon algebra without promoting it to a fusion category.
The adjacent `research/kitaev/s3-quantum-double-fusion-ring.md` derives the
complete multiplicity-free fusion ring from exact commuting-pair characters;
associator and braid coherence remain open.
The modular successor `research/kitaev/s3-exact-modular-data.md` freezes the
exact `S,T` data and independently recovers fusion through Verlinde, while
leaving microscopic `F/R` gauges unresolved.
The first microscopic coherence successor,
`research/kitaev/s3-electric-FR-coherence-fragment.md`, derives
`F_CCC^C` and electric channel braids from explicit intertwiners; mixed
flux/dyon sectors remain open.
The first mixed-sector successor,
`research/kitaev/s3-charge-flux-monodromy-versus-modular-readout.md`, proves
that a zero modular entry can hide an invertible non-scalar monodromy and
identifies the centralizer-irrep kernel of pure-charge probes.
The scalar-readout successor,
`research/kitaev/s3-minimal-jointly-faithful-scalar-probes.md`, proves that
three probes are necessary and sufficient over the frozen twist/Hopf-link
surface and lists all four minimum families.
Its robustness successor,
`research/kitaev/s3-scalar-probe-adversarial-margin.md`, proves uniform
minimum separation `1/3` and the sharp deterministic error radius `1/6`.
The formal-effect refinement,
`research/kitaev/s3-binary-hadamard-probe-instrument.md`, resolves scalar
quadratures into formal binary effects, preserves the three-setting minimum,
and derives a conditional i.i.d. sampling bound.  Its raw `S` effects do not
yet have a source-derived apparatus dilation.
The corrected apparatus successor,
`research/kitaev/s3-normalized-monodromy-controlled-trace-probes.md`, replaces
raw `S` by the controlled-trace expectation `6S_ab/(d_a d_b)` and recovers a
three-setting minimum with an abstract typed dilation.
On the electric subdomain,
`research/kitaev/s3-electric-one-setting-reference-twirl.md` shows that
uniform conjugation of one `D` reference removes target-state dependence and
gives a one-setting classifier for `A,B,C`.
The universal-R successor,
`research/kitaev/s3-universal-R-target-state-independence.md`, extends
target-state independence to all 64 ordered simple-sector pairs by exact
reference partial trace.
The domain successor,
`research/kitaev/s3-pure-sector-readout-versus-mixture-tomography.md`,
separates pure-label identification from classical-mixture tomography and
proves the respective three- versus seven-setting minima.
The operator-algebra successor,
`research/kitaev/s3-central-readout-algebra-and-superselection.md`, proves
that those seven probes span exactly the sector center, exhibits the
248-dimensional ambient Hermitian kernel, and keeps superselection
admissibility separate from algebraic invisibility.
Its channel-theoretic successor,
`research/kitaev/s3-center-conditional-expectation-and-operational-quotient.md`,
constructs the center quotient as a 36-Kraus measure--prepare conditional
expectation and proves that it is strictly coarser than sector dephasing.
The control-compilation successor,
`research/kitaev/s3-center-random-unitary-control-compilation.md`, realizes
that quotient as seven finite randomized-unitary stages while keeping the
availability of the required sector-sign and internal Weyl controls open.
The endpoint-span successor,
`research/kitaev/s3-endpoint-algebra-span-versus-control.md`, proves that the
full block-selective matrix algebra is present in the `D(S_3)` endpoint
representation, falsifies gauge-only sufficiency by rank 6 versus 36, and
isolates executable source control as the remaining gap.
The minimal-generator successor,
`research/kitaev/s3-minimal-flux-resolved-control-generators.md`, proves that
gauge access needs exactly two additional flux ports—one transposition and
one three-cycle projector—to generate the full endpoint algebra.
The dynamical successor,
`research/kitaev/s3-two-flux-projective-lie-controllability.md`, corrects the
promotion from associative to Lie control: the two-port surface has dimension
33 rather than 36, misses three central phase combinations, but contains the
full 28-dimensional projective block algebra needed for conjugation twirls.
The central-phase successor,
`research/kitaev/s3-central-phase-deficit-and-dephasing-completion.md`, further
corrects the channel claim: the available center fuses `G,H`, and one extra
imaginary three-cycle endpoint quadrature is necessary and sufficient for an
exact 19-branch sector-dephasing twirl.
The cyclic-cost successor,
`research/kitaev/s3-optimal-cyclic-dephasing-and-weight-errors.md`, supersedes
19 as a minimum by attaining the sharp eight-branch lower bound and computes
an exact Fourier residual for nonuniform branch weights.
The source-to-instrument audit begins at
`research/kitaev/s3-local-hamiltonian-source-model.md`.  It freezes one
oriented square directly on `C[S3]^{otimes 4}`, proves that the two required
element-flux ports are four-edge Hermitian projectors, and falsifies their
membership in the native gauge-invariant commuting Hamiltonian.  Their
availability is therefore a typed apparatus enlargement, not a consequence
of endpoint-algebra span.
`research/kitaev/s3-ancilla-compiled-element-flux-ports.md` gives one exact
finite realization of that enlargement: a clean six-level plaquette ancilla
compiles either element-flux phase in nine serial gates.  It retains the
basepoint/gauge-frame dependence and is trivial on the flat vacuum sector.
`research/kitaev/s3-gh-separator-local-orbit-compilation.md` derives the
additional `G/H` separator as the local current
`(B^c U_c-U_c^{-1}B^c)/(2i)` and compiles it through the `C3` orbit Fourier
basis in thirteen serial gates, conditional on the stated coherent gate set.
`research/kitaev/s3-source-generated-lie-closure.md` composes the microscopic
compiler maps with the endpoint certificate: the actual conditional source
surface has Lie dimension 34, comprising the full 28-dimensional projective
algebra and a six-dimensional separating center, while two central phase
directions remain inaccessible.
`research/kitaev/s3-within-block-twirl-protocol-and-pulse-gap.md` freezes the
six-stage `(4,9,9,4,4,4)` randomized Weyl protocol and proves exact
projective reachability, while refusing to infer timed primitive pulse words
from Lie rank alone.
`research/kitaev/s3-eight-branch-dephasing-source-protocol.md` freezes the
sharp dephasing channel as a typed fresh-three-bit protocol and checks all 56
ordered cross-sector coherences, while retaining the unresolved timed-word
typing of its reachable central target.
`research/kitaev/s3-control-leakage-and-fixed-point-energy.md` proves zero
vacuum-code action, exact phase-dependent leakage on Haar flux excitations,
the ancilla-compute transients, and fixed-point energy preservation of the
`G/H` orbit current.
`research/kitaev/s3-timing-amplitude-phase-and-weight-errors.md` gives exact
central-pulse scale residuals, branch-dependent phase and weight bounds, and
local-port angle-to-leakage propagation without assuming a noise law.
`research/kitaev/s3-ancilla-measurement-reset-and-instrument.md` separates the
six-level coherent compiler ancilla, discarded random-control records, and
the three-qubit sector record; it constructs the exact 36-Kraus readout target
and isolates controlled central powers as a new source obligation.
`research/kitaev/s3-single-fault-propagation-and-recovery.md` proves the
holonomy compiler data-nonspreading, finds weight-two spread in the separator
coordinate gate, and separates quantum syndrome recovery from classical
branch/readout faults without selecting a decoder.
The twelve-move audit closes at
`research/kitaev/s3-source-to-instrument-final-verdict.md`: the exact center
instrument is a conditional extended-apparatus target, not a physical
implementation derived from the frozen native source.  The remaining gaps
are timed words, controlization, apparatus operations, and fault-tolerant
recovery rather than finite algebra.
The first post-audit successor,
`research/kitaev/s3-controlled-power-controlization-boundary.md`, sharpens
the controlization gap into an exact black-box impossibility theorem: global
phase becomes a control-branch-relative phase.  It also freezes the minimal
constructive repairs as either the conditional Hamiltonian `P1 tensor Z` or
controlled access to every primitive of a named timed word, while retaining
the missing timed word and hardware coupling as explicit source obligations.
Its record-protection companion,
`research/kitaev/s3-sector-record-minimal-redundancy.md`, proves that six bits
are necessary and sufficient to encode eight sector labels with correction of
one final-record bit flip.  The optimal `[6,3,3]` punctured-simplex code does
not protect phase acquisition or supply the missing controlled powers.
`research/kitaev/s3-controlled-power-fault-propagation.md` then proves the
exact acquisition-fault split: control dephasing does not spread, but a
control bit flip acquires the full support of `U`, while noncommuting data
faults become record--data correlated.  A numeric light-cone bound therefore
requires the still-missing microscopic timed word or conditional-Hamiltonian
support declaration.
`research/kitaev/s3-direct-center-versus-switched-synthesis.md` computes the
direct primitive-span obstruction: its block-central sector-signature rank is
only one, although the Lie-accessible center has rank six.  The optimal `Z`
is therefore not one simultaneous primitive pulse; its use requires either an
effective switched-word compiler or the explicit apparatus enlargement
`P1 tensor Z`.
`research/kitaev/s3-minimal-controlled-power-apparatus.md` freezes that
enlargement exactly.  The original record--data-factorized surface cannot
produce a Schmidt-rank-two controlled unitary; one new tunable interaction
family `P1 tensor Z` is necessary and sufficient in that sense, giving the
three powers in three five-body pulses with no workspace residue.  Its
primitive fault bound reaches four data edges and hence is not yet a
fault-tolerant low-arity gadget.
The controlled-power line closes at
`research/kitaev/s3-controlled-power-successor-verdict.md`, which composes the
native tensor-cut obstruction, direct-center rank-one theorem, exact
three-pulse `P1 tensor Z` enlargement, four-edge fault bound, and sharp
six-bit final-record code without promoting the conditional coupling to a
native Hamiltonian term.
The lower-arity successor begins at
`research/kitaev/s3-holonomy-bus-versus-sector-label.md`.  It proves that the
existing six-level holonomy bus cannot be repurposed into the full sector
oracle: gauge-invariant phase tables are class functions with only three
signatures, while a one-shot clean bus for eight distinct sector phases needs
dimension at least eight and charge-sensitive information.
`research/kitaev/s3-sequential-charge-predicate-lower-bound.md` shows that a
reusable-qubit alternative needs three rounds and all three predicates must
be charge-sensitive.  No relabeling can make even one bit flux-class-only,
because class sizes `3,2,3` admit no balanced four-versus-four union; all
`40320` three-bit labelings pass the obstruction.
`research/kitaev/s3-sector-bus-four-edge-support-bound.md` proves that reduced
primitive arity cannot reduce ideal data support below four: omitting any edge
loses a flux-class distinction.  A standard clean bus therefore starts at
four forward plus four reverse edge interactions and one phase gate before
the unavoidable charge-sensitive overhead.
`research/kitaev/s3-centralizer-fourier-sector-bus.md` supplies the first
constructive answer: centralizer Fourier labels `(S3,Z2,Z3)` derive all eight
sectors before residue assignment.  An eight-state label bus then compiles
each controlled power in 45 one-/two-body gates with exact cleanup.  Primitive
arity falls to two, but an unverified shared-bus fault can still reach all
four edges, so worst-case distance nine remains.
`research/kitaev/s3-verified-cat-versus-shared-bus-faults.md` shows that a
four-rail verified cat reduces accepted control-fanout faults to data weight
one, but does not protect either shared coherent bus.  The combined arbitrary
single-fault weight therefore remains four and the distance-nine requirement
survives until a coherent bus-verification or segmentation theorem exists.
`research/kitaev/s3-encoded-bus-interleaving-bound.md` gives the conditional
improvement: arbitrary bus faults require distance-three quantum buses, with
five rails each by Singleton.  Interleaving correction after all twenty
bus--data interactions can reduce bus spread to one if the logical gates are
fault-transversal, but the existing relative-coordinate gate keeps total
spread at two and therefore leaves a distance-five data-code requirement.
The lower-arity line consolidates at
`research/kitaev/s3-lower-arity-sector-bus-verdict.md`: all controlled powers
have exact 45-gate clean one-/two-body compilers derived from centralizer
Fourier labels.  Unverified spread remains weight four; fully encoded,
twenty-cycle interleaving conditionally lowers it to one, but the two-edge
relative-coordinate gate fixes the combined bound at weight two/distance five.

## Ledger promotions

- `src/ledger/20260824-2169 Toric Syndromes and Logical Readout Arise from
  Pauli Commutation.md` freezes the WP1--WP6 finite theorem boundary.
- `src/ledger/20260824-2170 Topological Readout Can Disappear by Access
  Projection or Boundary Migration.md` freezes the WP7--WP15 operational and
  relative-homology boundary.
- `src/ledger/20260824-2171 Wilson Effects Do Not Determine Instruments and
  Non-Abelian Braiding Is Matrix-Valued.md` freezes the instrument, fault,
  perturbative-order, and `D(S_3)` frontier results.
- `src/ledger/20260824-2173 Local Ribbon Orientation Determines
  Multiplication and Exact Characters Determine D(S3) Fusion.md` freezes the
  oriented fixed-ribbon algebra and complete fusion ring.
- `src/ledger/20260824-2175 The D(S3) Modular Pair Is Exact and Verlinde
  Recovers Fusion.md` freezes exact modular data and its independent fusion
  consistency check.
- `src/ledger/20260824-2179 Explicit Electric Intertwiners Produce a
  Microscopic D(S3) F-R Fragment.md` freezes the first source-derived
  recoupling and channel-braid fragment.
- `src/ledger/20260824-2182 A Zero Modular Entry Can Hide an Invertible
  Non-Scalar Braid.md` freezes the mixed charge--flux monodromy witness and
  its exact probe kernel.
- `src/ledger/20260824-2184 Three Scalar Probes Are Necessary and Sufficient
  for D(S3) Sector Readout.md` freezes the surface-relative scalar probe
  minimum and all minimum families.
- `src/ledger/20260824-2188 Minimum D(S3) Scalar Readout Has Sharp Error
  Radius One Sixth.md` freezes the deterministic robustness margin and its
  exact boundary collision.
- `src/ledger/20260824-2191 Three Binary Hadamard Settings Retain Faithful
  D(S3) Readout.md` freezes the atomic quadrature minimum and formal binary
  effects, with a correction that raw `S` Hadamard realization is unresolved.
- `src/ledger/20260824-2196 Raw Modular Scalars Do Not Yet Have a
  Source-Derived Hadamard Instrument.md` records the apparatus-typing defect,
  repaired v2 claim, and exact missing dilation.
- `src/ledger/20260824-2197 Normalized Monodromy Restores a Typed
  Three-Setting D(S3) Instrument.md` freezes the corrected controlled-trace
  surface, minimum, margins, and conditional sampling bound.
- `src/ledger/20260824-2198 One Twirled Flux Reference Separates All Pure
  Electric D(S3) Charges.md` freezes the source-typed reference twirl and
  one-setting electric classifier.
- `src/ledger/20260824-2202 Reference Partial Trace Makes D(S3) Monodromy
  Independent of the Target State.md` freezes the universal-R construction
  and all-64-pair target-state-independence theorem.
- `src/ledger/20260824-2206 Three Settings Identify Pure D(S3) Sectors but
  Seven Are Needed for Mixtures.md` freezes the admitted-domain split,
  convex collisions, and exact mixture-tomography minimum.
- `src/ledger/20260824-2210 Central D(S3) Probes Recover Sector Weights but
  Leave a 248-Dimensional Operator Kernel.md` freezes the central readout
  algebra, its ambient kernel, and the superselection boundary.
- `src/ledger/20260824-2217 Sector Dephasing Is Not the D(S3) Central
  Readout Quotient.md` freezes the measure--prepare center expectation and
  its exact separation from block dephasing.
- `src/ledger/20260824-2221 The D(S3) Center Quotient Has a Finite
  Random-Unitary Compilation.md` freezes the seven-stage control compilation
  and its unresolved source-availability boundary.
- `src/ledger/20260824-2228 The D(S3) Endpoint Algebra Spans Every Block
  Control but Gauge Actions Do Not.md` freezes the full endpoint-image theorem,
  gauge-only rank deficit, and span-versus-control boundary.
- `src/ledger/20260824-2238 Two Flux Ports Are Necessary and Sufficient for
  Full D(S3) Endpoint Access.md` freezes the exact two-port associative
  generator minimum and its conjugacy-type restriction.
- `src/ledger/20260824-2249 Two D(S3) Flux Ports Give Projective but Not Full
  Block-Unitary Control.md` freezes the 33-dimensional Lie correction, three
  missing central phases, and full 28-dimensional projective survivor.
- `src/ledger/20260824-2258 One Extra D(S3) Endpoint Port Is Required for
  Complete Sector Dephasing.md` corrects the twirl inventory, freezes the
  unique `G,H` collision, and constructs the exact 19-branch completion.
- `src/ledger/20260824-2265 Eight Cyclic Branches Are Optimal for D(S3)
  Sector Dephasing.md` supersedes 19 as the branch minimum and freezes the
  exact branch-weight Fourier residual.

## Successor: recovered relative coordinate

- `s3-recovered-relative-coordinate-shuttle.md` replaces the last direct
  weight-two relative-coordinate primitive by an exact three-contact clean
  `S3` shuttle.  With recovery of both incident encoded blocks after every
  contact, its 18 abstract single-fault paths have data weight at most one;
  the conditional compiler accounting becomes 49 gates and 26 recovery
  layers per controlled power, fifteen bus rails, and data distance three.

## Executable fault-tolerance frontier

- `s3-five-rail-code-and-transversal-obstruction.md` freezes explicit
  `[[5,1,3]]_2` and `[[5,1,3]]_3` component codes, complete one-rail recovery
  tables, and the resulting six- and eight-level bus encodings.  Exact
  normalizer tests falsify railwise qubit/qutrit SUM and `H/F3`; coordinate
  inversion is the sole tested transversal survivor.  Executable
  multiplication and Fourier therefore require teleportation, switching, or
  another explicitly recovered nontransversal gadget.
- `s3-clifford-teleportation-and-magic-boundary.md` constructs noncircular
  encoded Choi teleportation for `H`, `F3`, and qubit/qutrit SUM across all
  110 Bell branches.  It also isolates the true source obstruction:
  qubit-controlled qutrit inversion is non-Clifford with 32/36 non-Clifford
  teleportation corrections, while record phases for powers one and two need
  controlled-`T`/controlled-`S`-type resources.  No such verified magic
  source belongs to the frozen interfaces.  The Clifford Choi resources
  themselves are explicitly prepared by three-round verified-cat measurement
  of weight `(6,6)` or `(9,6,6,9)` logical stabilizers.
- `s3-five-rail-shor-recovery.md` supplies the previously missing explicit
  generalized Shor-cat recovery schedule.  Adjacent verification accepts only
  harmless global cat shifts, three complete syndrome rounds correct one bad
  sample, and the exact six-/eight-level recovery contact counts are 105/144.
- `s3-26-contact-exrec-fault-pairs.md` freezes the full recovered contact
  order and exhausts 78 macro single faults plus 3,081 macro pairs.  Every
  single fault is contained; 220 pairs are malignant in the conservative
  support model.  Microscopic factory pairs remain uncountable until the
  missing nonstabilizer factories are supplied.
- `s3-executable-fault-tolerance-final-verdict.md` consolidates the executable
  frontier.  The stabilizer subcompiler, Choi resources, recovery, and macro
  exRec are explicit, but the full compiler is obstructed in the frozen
  resource theory by controlled inversion, two controlled phases, and three
  coherent lookup multiplexors.  Full physical gate/depth/magic costs are
  therefore undefined rather than silently fitted; a new verified magic
  source would be a theorem-changing extension.
- `s3-transporter-and-label-lookup.md` derives the six-entry transporter,
  verifies its 36-state alignment/inverse and non-Clifford normalizer failure,
  freezes all eight residue bit words, and separates unavailable coherent
  predicate extraction from executable three-XOR label copy.
