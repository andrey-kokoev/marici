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
  \(2(D-1)/9\). The marked-theta external-state refinement now gives an
  explicit 150-variable open-path dictionary, its 5,616-monomial free surface
  polynomial, and a symbolic physical-projector identity in thirteen
  independent Gram variables across all 24 audited tree/reference
  presentations. The resolved dictionary is flip natural, strictly
  Cut-compatible before circuit evaluation, and satisfies the mapping-class
  orbit Cut Equation. The two-open-pair Ward audit proves strict partial-trace
  naturality after augmentation but falsifies its diagonal lift to raw cubic
  origins: all 72 partial/full presentations require transport across all five
  vertex-sector coordinates. The resulting graph-multiplihedral carrier has a
  component/innermost marked edge-deletion map that passes every face-poset,
  covariance, and two-edge functoriality test on all connected simple graphs
  through five vertices. Off-shell Ward propagation then gives a general
  flag-incidence exact sequence whose closed sector is graph homology. On the
  marked theta this Ward kernel is integrally and equivariantly \(H_1(K_{2,3})\),
  and individual primitive classes match populated oriented circuit supports.
  There is nevertheless no integral \(D_3\)-equivariant additive section from
  homology to resolved noncrossing curves: the obstruction has index three,
  every primitive tag pair intersects once, and no resolved state contains two
  circuits. Retaining the nonsplit three-tag complex resolves the additive
  problem integrally; the 243-state graph lacks its orientation local system.
  More generally, \(K_{2,m}\) carries the canonical \(A_{m-1}\) circuit
  resolution, and any cyclic-equivariant splitting has exact denominator
  \(m\). This circuit resolution is exactly the cellular complex of the road
  polygon \(C_m\): its rational split is a discrete Green current and its
  denominator is the graph Jacobian \(\operatorname{Jac}(C_m)\cong\mathbb Z/m\).
  More invariantly, the common transport primitive is the integral torsor of
  currents with prescribed divergence; a chosen inverse Laplacian is only a
  gauge fixing, whose Cut-naturality defect is necessarily harmonic. At six
  points the bridge is stronger: the two scalar polarity tripods glue along
  the three channel facets to give \(K_{2,3}=S^0*R_3\), and the
  Mayer--Vietoris suspension sends the QTDS contact difference integrally and
  \(D_6\)-equivariantly to the Ward circuit lattice. Abstractly this
  suspension holds for every \(m\):
  \(H_1(K_{2,m};\mathbb Z)\cong
  \operatorname{sgn}_{S_2}\boxtimes A_{m-1}\). The alternating
  three-gluon fusion residues now derive the full QTDS-to-Ward coefficient
  matrix intrinsically as a normalization/conductor symbol. The guessed
  sequence \(m=n/2\) is false. More sharply, the octagon's connected
  rank-zero/rank-one fibers give two disjoint eight-road stars; \(K_{2,8}\)
  appears only after an inadmissible collapse of disconnected fibers. Every
  marked boundary still recovers \(K_{2,3}\). In general a cut creates
  independent regional polarity choices, so the carrier is a core-incidence
  diagram whose higher strata must supply the transgression. The next carrier
  is therefore an oriented relation complex plus a Brauer--skein
  crossing/smoothing cell for multiplicative coherence inside a cyclic
  Ward--Brauer dictionary. At the first nontransverse octagon stratum, the
  physical four-chart belt now has one normalized, torsion-free degree-zero
  derived Gysin class into a weighted three-interval cube. Its full QTDS
  polarization is eight times the primitive Laurent class, while one
  degree-one belt class exactly locates the missing occurrence-decorated
  source-cap extension. A BRST/kinetic realization of the conductor
  symbol, its higher-core Gysin comparison, an all-topology
  physical-projector comparison, a single point-set all-loop differential
  operator on already-summed \(X_C\) functions, and a metric jet adjoint
  remain undefined;
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
rustc --edition=2021 -O research/nima/check_marked_handle_counit.rs -o "$env:TEMP\marici-marked-handle-counit.exe"
& "$env:TEMP\marici-marked-handle-counit.exe"
rustc --edition=2021 -O research/nima/check_marked_handle_x_dictionary.rs -o "$env:TEMP\marici-marked-handle-dictionary.exe"
& "$env:TEMP\marici-marked-handle-dictionary.exe"
rustc --edition=2021 -O research/nima/check_marked_handle_symbolic_identity.rs -o "$env:TEMP\marici-marked-handle-symbolic.exe"
& "$env:TEMP\marici-marked-handle-symbolic.exe"
rustc --edition=2021 -O research/nima/check_one_edge_closure_ward.rs -o "$env:TEMP\marici-one-edge-ward.exe"
& "$env:TEMP\marici-one-edge-ward.exe"
rustc --edition=2021 -O research/nima/check_two_open_pair_ward_naturality.rs -o "$env:TEMP\marici-two-open-pair.exe"
& "$env:TEMP\marici-two-open-pair.exe"
rustc --edition=2021 -O research/nima/atlas_graph_multiplihedron_k23.rs -o "$env:TEMP\marici-graph-multiplihedron.exe"
& "$env:TEMP\marici-graph-multiplihedron.exe"
rustc --edition=2021 -O research/nima/check_graph_addition_multiplihedron_maps.rs -o "$env:TEMP\marici-graph-addition.exe"
& "$env:TEMP\marici-graph-addition.exe"
rustc --edition=2021 -O research/nima/check_moving_ward_boundary.rs -o "$env:TEMP\marici-moving-ward.exe"
& "$env:TEMP\marici-moving-ward.exe"
rustc --edition=2021 -O research/nima/check_origin_resolution_coherence.rs -o "$env:TEMP\marici-origin-resolution.exe"
& "$env:TEMP\marici-origin-resolution.exe"
rustc --edition=2021 -O research/nima/check_offshell_ward_contact_complex.rs -o "$env:TEMP\marici-offshell-ward.exe"
& "$env:TEMP\marici-offshell-ward.exe"
rustc --edition=2021 -O research/nima/check_longitudinal_edge_gluing.rs -o "$env:TEMP\marici-longitudinal-gluing.exe"
& "$env:TEMP\marici-longitudinal-gluing.exe"
rustc --edition=2021 -O research/nima/check_marked_edge_deletion_general.rs -o "$env:TEMP\marici-marked-deletion.exe"
& "$env:TEMP\marici-marked-deletion.exe"
rustc --edition=2021 -O research/nima/check_ward_cycle_brauer_map.rs -o "$env:TEMP\marici-ward-brauer.exe"
& "$env:TEMP\marici-ward-brauer.exe"
rustc --edition=2021 -O research/nima/check_oriented_brauer_skein_filler.rs -o "$env:TEMP\marici-brauer-skein.exe"
& "$env:TEMP\marici-brauer-skein.exe"
rustc --edition=2021 -O research/nima/check_k2m_circuit_resolution.rs -o "$env:TEMP\marici-k2m-circuit.exe"
& "$env:TEMP\marici-k2m-circuit.exe"
rustc --edition=2021 -O research/nima/check_m3_hodge_comparison.rs -o "$env:TEMP\marici-m3-hodge.exe"
& "$env:TEMP\marici-m3-hodge.exe"
rustc --edition=2021 -O research/nima/check_k2m_suspension.rs -o "$env:TEMP\marici-k2m-suspension.exe"
& "$env:TEMP\marici-k2m-suspension.exe"
rustc --edition=2021 -D warnings -O research/nima/check_three_gluon_qtds_transgression.rs -o "$env:TEMP\marici-three-gluon-transgression.exe"
& "$env:TEMP\marici-three-gluon-transgression.exe"
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_polarity_carrier.rs -o "$env:TEMP\marici-eight-point-polarity.exe"
& "$env:TEMP\marici-eight-point-polarity.exe"
rustc --edition=2021 -D warnings -O research/nima/check_global_polarity_incidence.rs -o "$env:TEMP\marici-global-polarity.exe"
& "$env:TEMP\marici-global-polarity.exe"
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_rank_two_gysin.rs -o "$env:TEMP\marici-rank-two-gysin.exe"
& "$env:TEMP\marici-rank-two-gysin.exe"
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_coefficient_gysin.rs -o "$env:TEMP\marici-coefficient-gysin.exe"
& "$env:TEMP\marici-coefficient-gysin.exe"
rustc --edition=2021 -D warnings -O research/nima/check_eight_point_pentagon_transport.rs -o "$env:TEMP\marici-pentagon-transport.exe"
& "$env:TEMP\marici-pentagon-transport.exe"
rustc --edition=2021 -D warnings -O research/nima/check_pentagon_incidence_span.rs -o "$env:TEMP\marici-pentagon-incidence-span.exe"
& "$env:TEMP\marici-pentagon-incidence-span.exe"
rustc --edition=2021 -D warnings -O research/nima/check_occurrence_support_cosheaf.rs -o "$env:TEMP\marici-occurrence-support.exe"
& "$env:TEMP\marici-occurrence-support.exe"
rustc --edition=2021 -D warnings -O research/nima/check_cubical_gysin_coherence.rs -o "$env:TEMP\marici-cubical-gysin.exe"
& "$env:TEMP\marici-cubical-gysin.exe"
rustc --edition=2021 -D warnings -O research/nima/check_loaded_cech_totalization.rs -o "$env:TEMP\marici-loaded-cech.exe"
& "$env:TEMP\marici-loaded-cech.exe"
rustc --edition=2021 -D warnings -O research/nima/check_filtered_gysin_selector.rs -o "$env:TEMP\marici-filtered-gysin.exe"
& "$env:TEMP\marici-filtered-gysin.exe"
rustc --edition=2021 -D warnings -O research/nima/check_loaded_route_cube_gysin.rs -o "$env:TEMP\marici-loaded-route-cube.exe"
& "$env:TEMP\marici-loaded-route-cube.exe"
rustc --edition=2021 -D warnings -O research/nima/check_route_kernel_hom_complex.rs -o "$env:TEMP\marici-route-hom.exe"
& "$env:TEMP\marici-route-hom.exe"
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
- `20260813-38` constructs the finite-nonresonant normal-torus Pochhammer/Cousin lift on
  undecorated faces and the transverse occurrence complex, and proves that its nearby-cycle unit
  has associated grade exactly \(1/X_e\); entries 70--71 delimit the still-missing dependent-face
  coefficient lift.
- `20260813-39` derives the scalar period half-class and identifies it with
  \([({\rm Pf}'A)^2]\); its pre-pairing Pochhammer/Cousin factorization is exact on the
  transverse subcomplex, while entries 70--71 reopen the complete dependent-face chain lift.
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
- `20260813-50` adds three external scaffold states to the marked theta handle, verifies the
  resolved state carrier and cyclic support balance, and records the first finite
  physical-projector comparison together with its corrected longitudinal-sector scope.
- `20260813-51` constructs the literal open-path endpoint-extension dictionary, retains 150
  homotopy-sensitive curve variables and 5,616 surviving surface monomials, and matches the
  complete marked-handle physical projector at four exact points and all twelve spanning trees.
- `20260813-52` upgrades that comparison to an exact Gram-ring identity across 24
  tree/reference presentations and proves that the resolved curve-cover construction is natural
  under flips and Cuts and descends through mapping-class summation with the exact Cut Equation.
- `20260813-53` falsifies unrestricted projector closure, proves the corrected Ward-quotient
  formula and strict two-trace interchange, and isolates closure-stable Ward alignment plus
  environmentwise curve realization as the hypotheses needed for cycle-rank induction.
- `20260813-54` keeps both marked-theta forward pairs open and proves all 48 partial
  physical/curve realization squares over a 48-variable Gram-free ring; the gauge-reduced
  surface representative absorbs 96 nonzero ordinary Ward coefficients and makes each first
  trace strict before the second closure.
- `20260813-55` falsifies the diagonal lift of that equality to the 243 raw cubic-sector
  origins: neither closure endpoints nor their two-edge union support the cancellation, and
  every presentation requires all five sector coordinates, forcing a derived Ward--Brauer
  dictionary with explicit Ward/V homotopies.
- `20260813-56` constructs the marked-theta graph-multiplihedral carrier, proves strict
  component/innermost deletion on all sewing stages, and separates connected propagation
  regions from arbitrary gauge-tail subsets and formal origin fillers.
- `20260813-57` derives the off-shell Ward contact-minus-longitudinal sequence, selects
  even endpoint gluing from projector parity, and identifies the residual closed sector with
  ordinary graph homology.
- `20260813-58` extends the marked-deletion audit to every connected simple graph
  through five labeled vertices with zero validity, order, dimension, surjectivity,
  covariance, or two-edge functoriality failures.
- `20260813-59` proves the integral equivariant Ward--\(H_1\) bridge, matches individual
  cycles to populated circuit tags, and finds the index-three/intersection obstruction that
  forces an oriented Brauer--skein crossing cell.
- `20260813-60` keeps the nonsplit circuit extension as an integral two-term resolution,
  proves that the unoriented 243-state graph cannot bound its unpointed relation, identifies
  the extra core-orientation character, and reserves smoothing cells for multiplicative
  intersection coherence rather than additive homology.
- `20260813-61` proves the all-\(m\) \(K_{2,m}\) circuit theorem: graph homology is
  \(A_{m-1}\), cyclic adjacent-road tags give its saturated integral resolution, and an
  equivariant split has exact denominator \(m\).
- `20260813-62` identifies that resolution with the cellular complex of the road polygon,
  derives its Green-current section, and identifies the denominator with
  \(\operatorname{Jac}(C_m)\cong\mathbb Z/m\).
- `20260813-63` replaces inverse-Laplacian transfer by the canonical flow torsor, proves strict
  functoriality before choosing a section, and identifies failure of Green-section Cut naturality
  as a homology-valued categorical cocycle.
- `20260813-64` proves that the two six-point scalar polarity tripods glue to
  \(K_{2,3}=S^0*R_3\), whose Mayer--Vietoris suspension carries the QTDS contact difference
  integrally and \(D_6\)-equivariantly to the marked-theta Ward circuit lattice.
- `20260813-65` proves the abstract all-\(m\) suspension
  \(H_1(K_{2,m})\cong\operatorname{sgn}_{S_2}\boxtimes A_{m-1}\), separates canonical
  transgression from the flow-torsor lift, and formulates the scalar \(m=4\) falsifier.
- `20260813-66` derives the QTDS contact matrix and its Ward-kernel lift from the intrinsic
  normalization/conductor symbol of the two alternating scalar-scaffolded three-gluon residues.
- `20260813-67` rejects \(K_{2,4}\) and proves that every marked octagon boundary
  recovers \(K_{2,3}\); its provisional global \(K_{2,8}\) quotient is corrected next.
- `20260813-68` proves the regional polarity-fiber theorem: connected rank-one contractions
  cease to be suspension graphs beyond six points, mixed regional sheets and parallel incidences
  appear, and higher core strata or the full homotopy colimit must carry global transgression.
- `20260813-69` executes the octagon rank-two falsifier: the honest carrier has homotopy type
  \(K_{2,12}=S^0*\operatorname{Quad}_8\), not the Möbius carrier; marked Cut is a
  degree-shifting Gysin map to local \(K_{2,3}\), and polarity descent separates from
  quadrangulation coherence for the first time.
- `20260813-70` proves exact marked-Cut factorization on all rank-eight full-core coefficient
  fibers and closes the sixteen transverse route squares, while isolating the eight dependent
  pentagons' undefined same-core scalar transport as the first genuinely nontransverse Cousin
  gap; existing sign lines leave the Möbius index-two class intact.
- `20260813-71` falsifies an intrinsic edgewise repair of that gap: strict Laurent support
  already obstructs endpoint transport, while the common full-core fiber admits both
  \(\tau_s=+\mathrm{Id}\) and \(-\mathrm{Id}\), with defects zero and
  \(-2\mathrm{Id}\); the canonical target is therefore the loaded five-facet Cousin identity.
- `20260813-72` replaces endpoint transport by constructible incidence descent: physical Gysin
  kills the exchanged scalar-flip quotients, polarity supports glue by a saturated
  \(2\to4+4\to6\) sequence, and each pentagon/companion-square pair glues by
  \(4\to6+6\to8\) to recover the entire rank-eight coefficient fiber integrally.
- `20260813-73` proves the route-face coefficient is an extension-by-zero constructible cosheaf
  and every rank-two core has an honest fixed-core cube.  On the eight four-chart cores the
  charts form only the side belt; two caps and the cube give exact target coherence, while forty
  support-compatible pentagon lifts leave the physical loaded Gysin naturality conditional.
- `20260813-74` resolves the forty-lift ambiguity in the derived category: existing data select
  one oriented relative/Borel--Moore class but no preferred strict map.  It replaces the
  overlarge constant-coefficient cube by a 27-generator weighted interval cube, derives the
  scalar-edge Cousin counit and uniquely forces both caps and the cube coherence, while leaving
  the global occurrence-decorated Pochhammer/Cousin comparison theorem open.
- `20260813-75` computes the complete local route-kernel derived Hom: the normalized degree-zero
  class is unique and torsion-free, a single belt degree-one class locates the missing decorated
  cap extension, the polynomial target is a nonfree occurrence ideal, and the full QTDS
  polarization is eight times the primitive Laurent class rather than a torsion effect.
