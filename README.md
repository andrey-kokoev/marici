# Marici

Research ledger and public map for the scalar master geometry program: intrinsic operations producing NLSM, Yang–Mills, gravity, and the exceptional CHY pairing web.

The ledger currently keeps three frontiers separate:

- **Nima:** the all-arity rooted-spine theorem now proves strict mixed Cut/refinement
  naturality, and its scalar associated grade has a finite nonresonant
  Pochhammer/Cousin lift. Derived index raising identifies the resulting
  factorization-natural worldsheet class with \([({\rm Pf}'A)^2]\) before pairing,
  closing the genus-zero three-generator web. The low-point operator-algebra audit
  identifies the Backus--Figueiredo \(W\) operation as an amplitude-level
  transmutation counit and the Dong--Su--Yang diagram derivatives as a sparse
  Catalan coframe inside it. The all-arity pairwise trace operators now give a
  manifestly cyclic counit and organize the lowering support as the vertex--edge
  incidence algebra of the complete graph on scaffold labels. This graph is the
  one-skeleton of a full semi-simplicial deletion object, whose integral
  degree-zero descent proves coherent reference independence. The exact
  one-bridge calculation now proves a strict tree physical-Cut coaction in the
  tensor product of lower amplitude quotients: the only raw correction is a
  two-pair sector tensored with a separate all-odd annihilator, and the two
  gluing gauges are related by a deletion-simplex filler. Cyclic symmetry also
  exposes a real integral torsion class: a unit invariant representative needs
  denominators or a new barycentric primitive. At the all-topology state layer,
  closed polarization circuits now form a resolved Brauer category with a
  cyclic monoidal scalar augmentation \(D\mapsto1\). This exactly passes the
  one-loop one-point closed-circuit test. Applying the derived modular envelope
  to this state augmentation and the resolved tree counit constructs a unique
  cyclic, all-topology, strictly Cut-monoidal operation on the universal
  ribbon-graph surface complex. The Cut Equation plus the cubic-scalar
  ultraviolet boundary condition then proves the exact descent inclusion
  \(u^{\rm univ}(\ker q_{\rm YM})\subseteq\ker q_\phi\), yielding a unique
  operation on canonical surface functions. Thus \(3S\), \(6AS\), separating
  Cuts, and nonseparating Cuts all close after resolved augmentation, at every
  topology. The first populated handle test now verifies this directly on the
  punctured-torus theta graph and exhibits the pre-augmentation Cut defect
  \(2(D-1)/9\). A single point-set all-loop differential operator on already-summed
  \(X_C\) functions and a metric jet adjoint remain undefined;
- **YM:** verify index raising on the six-point Laurent/nearby-cycle channel quotient and keep
  ordering contraction distinct from physical-state sewing;
- **Frost:** construct, or obstruct, a canonical cyclic/BV lift of the pure-Einstein
  primitive-symmetric retract and the scalar-to-surface lift of \(\mathsf J\).

## Commands

```text
pnpm install
pnpm dev
pnpm check
pnpm build
python research/nima/check_j_reconstruction.py
python research/nima/check_qtds_lift.py
python research/nima/check_qtds_descent.py
python research/nima/check_surface_rees_carrier.py
python research/nima/check_eight_point_transfer.py
python research/nima/check_scalar_edge_transport.py
python research/nima/check_ten_point_falsification.py
python research/nima/check_twelve_point_qtds.py
python research/nima/check_scalar_catalan_map.py
python research/nima/check_scalar_sink_qtds.py
python research/nima/check_qtds_vertex_cancellation.py
python research/nima/check_core_filtered_transfer.py
python research/nima/check_core_incidence_cells.py
python research/nima/check_core_incidence_rank_three.py
python research/nima/check_core_incidence_rank_four.py
python research/nima/check_associahedral_envelope.py
python research/nima/check_qtds_cut_coaction.py
python research/nima/check_mixed_prism_squares.py
python research/nima/check_mixed_prism_curvature.py
python research/nima/check_mixed_prism_spectator_stability.py
rustc --edition=2021 -O research/nima/check_mixed_prism_all_arity.rs -o "$env:TEMP\marici-mixed-prism.exe"
& "$env:TEMP\marici-mixed-prism.exe"
rustc --edition=2021 -O research/nima/check_twelve_point_scalar.rs -o "$env:TEMP\marici-check-twelve.exe"
& "$env:TEMP\marici-check-twelve.exe"
rustc --edition=2021 -O research/nima/check_low_point_transmutation.rs -o "$env:TEMP\marici-low-point-transmutation.exe"
& "$env:TEMP\marici-low-point-transmutation.exe"
rustc --edition=2021 -O research/nima/check_transmutation_counit_all_arity.rs -o "$env:TEMP\marici-transmutation-counit.exe"
& "$env:TEMP\marici-transmutation-counit.exe"
rustc --edition=2021 -O research/nima/check_transmutation_cut_coaction.rs -o "$env:TEMP\marici-transmutation-cut.exe"
& "$env:TEMP\marici-transmutation-cut.exe"
rustc --edition=2021 -O research/nima/check_surface_counit_brauer.rs -o "$env:TEMP\marici-surface-counit-brauer.exe"
& "$env:TEMP\marici-surface-counit-brauer.exe"
rustc --edition=2021 -O research/nima/check_modular_envelope_counit.rs -o "$env:TEMP\marici-modular-envelope-counit.exe"
& "$env:TEMP\marici-modular-envelope-counit.exe"
rustc --edition=2021 -O research/nima/check_cut_equation_descent.rs -o "$env:TEMP\marici-cut-equation-descent.exe"
& "$env:TEMP\marici-cut-equation-descent.exe"
```

Human-readable research records live in `src/ledger`. Ledger entries separate inherited working
structure, independently checked results, strong inferences, open questions, falsifiers, and
prohibited overclaims.

## Ledger map

- `20260812-01` records the gravity cyclic-lift problem.
- `20260812-02` fixes the Nima charter and candidate operation algebra.
- `20260812-03` records the three derived normal sectors and their epistemic boundaries.
- `20260812-04` states the three-generator half-object conjecture and six-theory pairing table.
- `20260812-05` defines the falsification protocol for the rank-jump half-object \(\mathsf J\).
- `20260812-06` fixes the research order and interfaces with YM, Frost, and Cintamani.
- `20260812-07` types candidate surface operations and records the non-conservativity of cuts.
- `20260812-08` refines the Yang–Mills operation to a multi-normal fusion residue.
- `20260812-09` tests the NLSM rank grade against curved cut completion and contact data.
- `20260812-10` separates pure-state cut closure from full primitive-symmetric surface naturality.
- `20260812-11` proves inverse-pairing reconstruction and identifies the resulting CHY class.
- `20260812-12` records exact four-, six-, and eight-point scalar-grade, photon-decoupling, KK,
  BCJ, and basis-change checks with a reproducible standard-library script.
- `20260812-13` corrects boundary index raising to a nearby-cycle channel quotient and assigns the
  scalar-to-surface comparison and cut-kernel primitive tests to YM and Frost.
- `20260812-14` proves direct all-multiplicity scalar descent using residue induction,
  soft-contact lemmas, and primary ordering relations.
- `20260812-15` records the genus-zero three-generator closure verdict, remaining qualifications,
  and the next Nima/YM/Frost ownership split.
- `20260812-16` proves the symmetry and information-loss obstruction to absolute QTDS
  strictification, constructs the correctly typed order-relative lift, and states the enriched
  cyclic-resolution target.
- `20260812-17` records exact quartic-recursion, polarity, scalar-grade, and rectangular-Jordan
  checks with a reproducible standard-library script.
- `20260812-18` identifies the alternating polarity torsor, distinguishes failure of a natural
  section from descent of an all-fibers object, and types the required cyclic-operadic coherence.
- `20260812-19` promotes the complete QTDS period family to a pointed cohomological factorization
  lift, constructs the six-point local flip flow, and identifies the exact eight-point
  projective-plane coherence complex and scalar-specialization target.
- `20260812-20` proves the summed-amplitude underdetermination, then escapes it using the
  cell-resolved scalar grade: the parity-core map derives the exact six-point QTDS contact
  redistribution and canonically labels the eight-point triangles and squares.
- `20260812-21` constructs the two canonical six-point scalar tripods, identifies the eight-point
  scalar carrier as a Möbius band bounded by the missing octagon, and types the filtered
  Pochhammer/Cousin comparison required for a genuine twisted-chain lift.
- 20260812-22 shows that the unique sign local system has a spherical double cover and types the
  first physical obstruction as a deck-odd, residue-free octagonal contact class, naturally
  regulated at finite nonresonant \(\alpha'\).
- `20260812-23` proves the exact eight-point core-stratified QTDS transfer, derives its closed
  contact grammar, finds the unique conditional distance-two marked matching, and shows why a
  genuine edge transport is necessary.
- `20260813-24` removes the conditioning: alternating scalar coorientation uniquely derives the
  marked matching, constructs its local deck-odd edge transport, identifies the integral route
  torsor, and proves zero octagonal contact curvature.
- `20260813-25` verifies the unchanged scalar rule through ten and twelve points, matches all
  QTDS contacts independently at both arities, exposes the Catalan count law, and formulates the
  all-arity discrete-Morse transfer theorem.
- `20260813-26` proves that theorem by a direct marked Catalan bijection with explicit inverse,
  identifies geodesics as linear extensions of disjoint flip chains, and proves the all-arity
  unique-sink QTDS contact theorem from a vertex-local numerator identity.
- `20260813-27` tensors the Catalan map over every partial physical core and proves all-arity,
  occurrence-level equality of the complete core-filtered scalar grade and complete QTDS period.
- `20260813-28` constructs the integral, deck-equivariant rank-two incidence carriers: squares
  for independent flips and pentagons for dependent flips, with exact signed boundaries.
- `20260813-29` falsifies naïve rank-three closure, classifies the missing scalar and physical
  facets, and constructs the canonical integral rank-three associahedral saturation.
- `20260813-30` repeats the falsification at rank four, closes all five product-associahedral
  types, and identifies the full marked associahedral envelope as the correct scalar source.
- `20260813-31` proves the all-rank dual-tree block-face lemma
  \(F_{\mathbf r}\cong\prod_a K_{r_a}\), thereby constructing every higher scalar-source
  coherence.
- `20260813-32` constructs the strict occurrence-level physical cut coaction, proves all cut
  orders agree with its closed product formula, and transports the physical-core cosheaf maps
  through the regional Catalan bijection.
- `20260813-33` splits the prism deficit into a Boolean physical square already closed by that
  coaction and one genuinely mixed scalar-refinement/physical-cut Beck--Chevalley square.
- `20260813-34` proves that mixed curvature vanishes termwise on every decorated occurrence
  through twelve points: the cut of a scalar edge is a two-slot weighted sum of canonical upper
  scalar edges.
- `20260813-35` generates the mixed \(K_2\times I\) cell directly from rooted dependency
  chains and independently extends the complete decorated audit to fourteen points in optimized
  Rust.
- `20260813-36` establishes the publication/claim DAG baseline and isolates scaffold lowering
  operators and reverse surface recovery as high-information external nodes.
- `20260813-37` proves the all-arity rooted-spine base-change theorem, replacing the bounded
  mixed-prism audits by an exact two-slot chain identity.
- `20260813-38` constructs the finite-nonresonant normal-torus Pochhammer/Cousin lift and proves
  that its nearby-cycle unit has associated grade exactly \(1/X_e\).
- `20260813-39` derives the scalar worldsheet half-class, identifies it with
  \([({\rm Pf}'A)^2]\), and proves factorization in the Pochhammer/Cousin complex before
  inverse-pairing reconstruction.
- `20260813-40` falsifies literal adjunction between the fusion jet and individual scaffold
  derivatives, reclassifies those derivatives as a Catalan cellular coframe, and states the
  correctly typed augmented-transmutation matrix test.
- `20260813-41` completes that test at four and five points: the full \(W\) transmuter and
  augmented Catalan coframe agree modulo the annihilator of the canonical YM amplitude for
  every cyclic reference, while the metric adjoint is provably underdetermined by the
  published fusion-map and pairing data.
- `20260813-42` proves an all-arity pairwise trace counit, decomposes every full \(W\)
  transmuter into one vertex sector and its incident complete-graph edge sectors, derives the
  vertex weight \(-(n-2)\), and constructs manifestly cyclic reference-free representatives.
- `20260813-43` promotes the complete graph to the full deletion simplex, proves its alternating
  Koszul differential squares to zero and its scalar counit is integral \(H_0\)-descent, then
  reduces physical-Cut compatibility to an exact one-bridge coevaluation problem.
- `20260813-44` proves weak all-arity Cut descent in the Cut-evaluation quotient, identifies the
  standard trace/insertion transmuter as a decomposable lift of the same counit class, and
  computes the integral cyclic obstruction \(g_n=n\) for odd \(n\) and \(g_n=n/2\) for even
  \(n\) in the reference-generator lattice.
- `20260813-45` proves the strict all-arity tree Cut formula for every retained pair and both
  scaffold gluing gauges: its sole correction factors through an all-odd lower annihilator, so
  the counit is group-like in the ordinary tensor product of lower amplitude quotients.
- `20260813-46` constructs the cyclic monoidal Brauer-state augmentation for closed
  polarization circuits, passes the exact one-loop one-point surface test, rules out a naive
  global \(D^{-L}\) definition, and isolates the local \(3S\) and mixed \(6AS\) Hatcher cells
  before the modular-envelope refinement.
- `20260813-47` applies the derived modular envelope to construct the universal cyclic,
  all-topology, strictly Cut-monoidal surface counit, proves exact Farey \(3S\) holonomy, and
  isolates descent to physical \(X_C\) surface functions as the kernel inclusion
  \(u^{\rm univ}(\ker q_{\rm YM})\subseteq\ker q_\phi\), already verified on the
  arbitrary-topology maximal-Cut quotient.
- `20260813-48` proves that Cuts plus the ultraviolet boundary are conservative for polynomial
  surface functions, uses this to establish the kernel inclusion at full surface-function level,
  and thereby constructs the unique cyclic, all-topology, Cut-monoidal physical surface counit.
- `20260813-49` performs the first populated handle test on the once-punctured torus: nine
  resolved theta sewings give the scalar coefficient \(1/3\), their nonseparating Cut gives the
  annulus coefficient \(1\), and premature circuit evaluation exhibits the exact obstruction
  \(2(D-1)/9\) that the termwise \(D\mapsto1\) augmentation removes.
