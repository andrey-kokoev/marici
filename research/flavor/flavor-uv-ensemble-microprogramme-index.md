# UV flavor-ensemble microprogramme index

Owner: `marici.Figueiredo`.

## Frozen predecessor

WP116 is authoritative. Texture charts are presentation rigidifiers;
`physical16` probes are faithful separator/readouts; the mixed Gram word
`I_11` separates the measured-ten hostile pair; the FDM-2 thermal arrow is a
conditional algebraic selector; no source-authorized physical selector is
currently established. This programme cannot reopen downstream selector
fitting.

## Objective

The only admitted direction is

`UV source and normalization -> physical flavor ensemble -> frozen readouts`.

Numerical flavor constants may test a frozen ensemble, but may not define the
UV source, its coefficients, its normalization, or its equivalence weights.

## Work packages

1. **UV source class.** Declare fields, representations, local action,
   coefficient domain, UV scale, scheme, and boundary data without flavor
   targets.
2. **Parameter typing.** Partition source inputs, gauge/presentation choices,
   renormalization data, and derived observables.
3. **Normalization.** Supply a normalized positive state or probability
   measure on UV quotient configurations.
4. **UV-to-`physical16`.** Derive the measurable covariant map before reading
   phenomenological outputs.
5. **Descent.** Prove invariance under UV gauge, weak-basis, and chart arrows.
6. **Ensemble fiber.** Classify the pushforward as unique, finite, continuous,
   or undefined from missing source data.
7. **RG transport.** Fix input/output scales and scheme, then push the ensemble
   through an equivariant RG map.
8. **Phenomenology.** Test only the already frozen pushforward ensemble.
9. **Readout reuse.** Apply canonicalization, thermal, detector, repeatability,
   and route weights without selector authority.
10. **Hostile controls.** Reject output-fitted parameters, post-readout
    normalization, chart-weight dependence, measured-ten injectivity, and
    selector authority silently assigned to RG/detectors.
11. **Missing datum.** If the ensemble is undefined, state the minimal missing
    source datum rather than fitting it.
12. **Data-descent v2.** Compile conditional capability, reliability contract,
    and bounded evidence replay.

## Common-domain vector thresholds and widths: WP476

- `flavor-common-domain-vector-widths.md`
- `checkers/wp476_common_domain_vector_widths.py`
- `results/wp476_common_domain_vector_widths.json`

WP476 composes the corrected kaon-conditioned scalar endpoint with the vector
current and pole packets. With the explicitly frozen common-clock messenger
benchmark `M_U=M_D=mu`, both messenger-pair and physical charged-flavon-pair
channels lie far above the quintet pole, so WP449's leading quark widths survive
on one declared domain. The source-generated readouts
`(m_1=g_F mu, C_0=1/(6 mu^2))` have exact logarithmic determinant `-2` and
separate positive `(g_F,mu)` points. Current instrumentation does not realize
that rank: the CP-even kaon likelihood is provisional and the Run-2 pole
channel is operationally empty. The five-TeV ratio readout remains a benchmark,
not a source-selected value.

## Scale-free ratio-selector normal form: WP477

- `flavor-ratio-selector-normal-form.md`
- `checkers/wp477_ratio_selector_normal_form.py`
- `results/wp477_ratio_selector_normal_form.json`

WP477 isolates the coefficient combination needed by the remaining numerical
selector gate: `c=a/(g_F^2 y^2)`. A source-fixed `c` would give
`g_F f/v=sqrt(3/c)` independently of the common scale. The conditional
five-TeV readout corresponds to the exact coefficient
`151560721/125000000000`, but that value is derived from the readout and cannot
be inserted as source data. The currently admitted positive action contains a
hostile `c` versus `4c` pair with targets differing by two. RG descent further
requires `beta_a/a=2 beta_g/g_F+2 beta_y/y`; WP465's gauge-only root supplies
neither this relation nor threshold stability. The selector normal form is now
exact, while its source constructor remains absent.

## Messenger-generated portal threshold: WP478

- `flavor-messenger-portal-threshold.md`
- `checkers/wp478_messenger_portal_threshold.py`
- `results/wp478_messenger_portal_threshold.json`

WP478 derives the one-loop mixed Higgs–flavon threshold of one singular channel
of the actual WP435 messenger chain. The local mixed coefficient is finite and
negative, with magnitude `3 y_Q^2 y_Phi^2/(8 pi^2)` for three colors, so the
messenger dynamics generates the sign and functional form required by the
common-clock portal. Its induced WP477 coordinate still depends continuously
on the messenger Yukawas, `eta`, `g_F`, `y`, and the matrix/background
normalization. The hostile source replacement `y_Q -> 2 y_Q` multiplies `c` by
four and halves the predicted ratio. The threshold is therefore an interaction
rigidifier, not a numerical selector; the successor must derive the complete
coupled trajectory and full matrix-valued matching.

## Adjoint-triplet messenger-port rank: WP479

- `flavor-triplet-portal-port-rank.md`
- `checkers/wp479_triplet_portal_port_rank.py`
- `results/wp479_triplet_portal_port_rank.json`

WP479 performs the full adjoint-label typing omitted by the one-channel WP478
calculation. Each messenger port contributes a rank-one positive Gram form on
the three `X_i` labels. WP435's two up/down ports therefore have rank at most
two and an exact cross-product kernel; they cannot generate the positive
isotropic `kappa I_3` pairing assumed by WP467 and WP475. Three ports are
necessary, and the canonical equal-norm orthogonal triple is sufficient, but
that Gram law still needs source authority. Existing scalar residues and vector
widths remain conditional on an independently declared isotropic portal rather
than derived from the minimal messenger completion.

## Triplicated-messenger gauge-beta gate: WP480

- `flavor-triplicated-messenger-beta-gate.md`
- `checkers/wp480_triplicated_messenger_beta_gate.py`
- `results/wp480_triplicated_messenger_beta_gate.json`

WP480 grants three equal orthogonal ports in each Standard Model quark sector
and computes their unavoidable gauge-matter cost. Three up and three down ports
with color give eighteen messenger Dirac fundamentals, hence twenty-four total
active fundamentals. The exact gauge-only coefficients become `b0=-13/2` and
`b1=-265`, with the formal nonzero root
`g_F^2=-104 pi^2/265`. Thus the minimum isotropic repair eliminates the
positive gauge-only fixed point. Decoupling restores the old running but not a
selected finite-scale coupling; keeping messengers near the vector poles opens
channels excluded from the frozen quark-only widths. A complete coupled
gauge–Yukawa fixed point is now the only remaining fixed-point repair.

## Coupled fixed-ray acceptance gate: WP481

- `flavor-coupled-fixed-ray-acceptance.md`
- `checkers/wp481_coupled_fixed_ray_acceptance.py`
- `results/wp481_coupled_fixed_ray_acceptance.json`

WP481 preregisters the exact reduced conditions under which a complete
gauge–Yukawa trajectory could repair WP480. For beta functions
`beta_g proportional to A+C alpha_g-D alpha_y` and
`beta_y proportional to E alpha_y-F alpha_g`, a positive interacting root
exists exactly when `D F/E-C>0`. Propagating fixed Yukawa/quartic rays through
WP478 gives a scale-independent source prediction
`g_F f/v=4 pi y_geom sqrt(r_eta/(k_Phi r_Q r_Phi))`. This would be a genuine
selector only if every coefficient and ray ratio is derived before comparison
with the withheld pole/current records. WP481 supplies the acceptance theorem,
not the missing concrete beta functions.

## Port-symmetry messenger-entrance obstruction: WP482

- `flavor-port-symmetry-entrance-obstruction.md`
- `checkers/wp482_port_symmetry_entrance_obstruction.py`
- `results/wp482_port_symmetry_entrance_obstruction.json`

WP482 tests whether symmetry can supply WP479's equal-port Gram in the minimal
one-stage messenger chain. The irreducible oriented triplet has no invariant
vector but a one-dimensional symmetric commutant: it forces `W=kappa I_3` and
simultaneously forbids the singlet quark–Higgs entrance. The reducible
permutation triplet has an invariant entrance vector, but its commutant is
two-dimensional, `a I_3+b 11^T`, so isotropy is no longer selected. A repair
requires a new dynamical connector/reference field and an explicitly changed
stabilizer groupoid before the fixed-ray or spectral packets can descend.

## Dynamical connector-frame architecture: WP483

- `flavor-connector-frame-architecture.md`
- `checkers/wp483_connector_frame_architecture.py`
- `results/wp483_connector_frame_architecture.json`

WP483 supplies a concrete renormalizable relational repair for WP482. A real
`3x3` connector frame links three equal cyclic entrances to the oriented
adjoint triplet through two vectorlike messenger stages. The positive frame
potential `||S^T S-s^2 I||^2` has exact unit-vacuum spectrum `0^3,8^6` and
gives the required route Gram `W=I_3`. This changes the physical groupoid by
adding a reference frame; the three orientation zeros are new physical modes,
not recovery of absolute orientation. The repair also raises the active matter
count to forty-two Dirac fundamentals, with gauge-only coefficients
`b0=-37/2`, `b1=-493`, and a negative formal root. It repairs descent but does
not yet select the ratio or support the frozen spectral packet.

## Gauged connector-frame lift: WP484

- `flavor-gauged-connector-frame-lift.md`
- `checkers/wp484_gauged_connector_frame_lift.py`
- `results/wp484_gauged_connector_frame_lift.json`

WP484 gauges the connector's right `SO(3)_P` port symmetry. At the joint vacuum
`X_i=J_i,S=I_3`, the exact 33-by-11 gauge-tangent matrix has rank eleven and a
positive Gram determinant, so the eight flavor and three frame zeros are all
gauge directions. After eating them, the block-separated scalar spectrum is
strictly positive: `8^6,16^8,36^7,100`. The isotropic Gram survives. This is a
genuine source-derived lift in a new relational groupoid, not recovery of an
absolute orientation and not a numerical selector. The mixed gauge spectrum,
new thresholds, beta functions, residues, and widths must now be recomputed.

## Mixed connector-gauge pole residues: WP485

- `flavor-mixed-gauge-pole-residues.md`
- `checkers/wp485_mixed_gauge_pole_residues.py`
- `results/wp485_mixed_gauge_pole_residues.json`

WP485 recomputes the vector poles in the changed WP484 groupoid. Here `mu` is
the adjoint amplitude and the physical flavor norm is `f_phys^2=6 mu^2`. The
principal quintet remains an unmixed fivefold pole at `3 g_F^2 mu^2`. Each principal
triplet flavor vector mixes with a port vector through one common two-by-two
mass block, producing two threefold poles. The connector makes its determinant
`2 g_F^2 g_P^2 mu^2 s^2`, lifting the diagonal zero. Representation theory
freezes the five-three-three grammar, the mixed-residue sum, and the exact
zero-momentum triplet current kernel `(2 mu^2+s^2)/(mu^2 s^2)`. It does not
freeze either individual mixed-pole residue: an exact hostile pair differing
only by `g_P=1` versus `g_P=2` changes the lower-pole current weight. Numerical
widths and residues therefore still require source selection or independent
calibration of `g_P/g_F` and `s/mu`, followed by a complete threshold audit.

## Pole-plus-current inverse instrument: WP486

- `flavor-pole-current-inverse-instrument.md`
- `checkers/wp486_pole_current_inverse_instrument.py`
- `results/wp486_pole_current_inverse_instrument.json`

WP486 proves that the three resolved vector pole locations together with the
zero-momentum triplet current coefficient form a jointly faithful probe family
on the positive four-parameter WP485 domain. An exact inverse reconstructs
`g_F^2,g_P^2,mu^2,s^2`; the positive image additionally requires
`T-Q/3-3D/Q>0`. The two mixed-pole weights are functions of pole locations
alone, and the inverse then fixes their absolute current residues. The exact
six-massless-quark partial fractional widths inherit the same calibration and
obey a sum rule with the quintet width. This is identification, not dynamical
selection. It is not yet a physical instrument: no common-domain experiment
currently supplies three populated resolved poles plus the calibrated current
coefficient, and nonquark thresholds remain unaudited.
The physical clock readout is `g_F f_phys/v=sqrt(2Q)/v`.

## Tree-level total-width closure cone: WP487

- `flavor-total-width-closure-cone.md`
- `checkers/wp487_total_width_closure_cone.py`
- `results/wp487_total_width_closure_cone.json`

WP487 gives a source-independent sufficient cone on which WP486's calibrated
six-quark partial widths become the complete tree-level widths. Every vector
pole and every physical scalar or messenger daughter is required to be heavier
than half every possible vector parent. This closes vector-vector,
vector-scalar, scalar-pair, and messenger-pair channels without fitting away a
coupling. The cone is exactly nonempty: the witness
`g_F^2=mu^2=tau^2=1`, `g_P^2=1/68`, `s^2=32` has squared vector masses
`1-1/sqrt(17),3,1+1/sqrt(17)` and satisfies every strict inequality. The
witness is not a selected source point. Actual total-width authority still
requires deriving all connector and messenger masses on the selected source
trajectory and proving that it lies inside the cone.

## Flavor-clock normalization correction: WP488

- `flavor-clock-normalization-correction.md`
- `checkers/wp488_flavor_clock_normalization_correction.py`
- `results/wp488_flavor_clock_normalization_correction.json`

WP488 repairs a coordinate-label defect in WP485-WP487. The coefficient in
`X_i=mu J_i` is the adjoint amplitude, whereas the established invariant flavor
clock obeys `f_phys^2=6 mu^2`. The quintet pole is
`Q=3 g_F^2 mu^2`, hence the physical readout is
`g_F f_phys/v=sqrt(2Q)/v`. The mass Gram, pole multiplicities, inverse map,
response rank, residues, and closure inequalities are unchanged. Treating
`mu=f_phys` would misnormalize the requested clock ratio by `sqrt(6)`.

## Common-source threshold constructor: WP489

- `flavor-common-source-threshold-constructor.md`
- `checkers/wp489_common_source_threshold_constructor.py`
- `results/wp489_common_source_threshold_constructor.json`

WP489 replaces the connector scale and both explicit messenger masses by one
renormalizable singlet-clock source. Its zero-energy relations fix
`mu^2=y^2w^2`, `f_phys^2=6y^2w^2`, `v^2=2aw^2`, `s^2=bw^2`, and
`M_A,B^2=z_A,B^2w^2`. For fixed source coefficients it therefore selects all
relational thresholds and `g_F f_phys/v=g_F y sqrt(3/a)`. An exact positive
witness has a conservative radial lower-bound Hessian above the unit threshold
and lies strictly inside
WP487's total-width cone, proving that one common source can support the whole
conditional spectral packet. The witness is not a numerical prediction:
continuous positive coefficient changes preserve the declared symmetries.
Concrete coefficient dynamics and the WP486 physical instrument remain open.

## Dual gauge-running selector gate: WP490

- `flavor-dual-gauge-running-gate.md`
- `checkers/wp490_dual_gauge_running_gate.py`
- `results/wp490_dual_gauge_running_gate.json`

WP490 computes the one-loop coefficients of the complete high-scale
`SU(3)_F x SO(3)_P` theory. The flavor factor retains `b0_F=-37/2`. The port
factor sees eighteen Dirac vectors and eleven real scalar vectors, giving
`b0_P=-133/3`. Neither factor has a positive finite gauge-only one-loop fixed
point. The simultaneous flow has the exact ratio ray
`g_P^2/g_F^2=111/266`, but it approaches the Gaussian infrared point and does
not select finite `g_F`; messenger decoupling also interrupts the full-matter
ray. WP489's `1/68` existence witness is not RG selected. A complete
gauge-Yukawa system with threshold matching is required for a finite selector.

## Gauge-Yukawa tensor-completeness gate: WP491

- `flavor-yukawa-tensor-completeness-gate.md`
- `checkers/wp491_yukawa_tensor_completeness_gate.py`
- `results/wp491_yukawa_tensor_completeness_gate.json`

WP491 shows that the requested coupled beta vector field is not yet defined.
WP489 freezes singlet-generated messenger masses but omits the up/down
interaction tensors `Y_H,Y_S,Y_X`. The symmetry-preserving hostile pair
`Y_X=I_18` versus `Y_X=2I_18` leaves every WP489 vacuum and threshold datum
unchanged while multiplying the quadratic Yukawa contraction by four and the
quartic contraction by sixteen. A calculable successor must freeze ten up/down
messenger maps, their contractions, retained scalar and Standard Model
couplings, scheme, loop order, and both finite threshold maps independently of
the desired fixed point. Until then no numerical selector follows from RG.

## Canonical messenger-tensor grammar: WP492

- `flavor-canonical-messenger-tensor-grammar.md`
- `checkers/wp492_canonical_messenger_tensor_grammar.py`
- `results/wp492_canonical_messenger_tensor_grammar.json`

WP492 freezes the ten up/down tensor shapes before any fixed-point search. The
cyclic fixed entrance, oriented-port dot, and symmetric port mass are
symmetry-forced. Componentwise connector incidence and the identity entrance
mass require an explicit diagonal-incidence locality axiom: cyclic symmetry
alone leaves respectively three- and two-dimensional commutants. The exact
shape norms are `1,9,3,3,3` for `Y_H,Y_S,Y_X,Z_A,Z_B`. This removes WP491's
tensor-shape ambiguity without selecting the ten scalar normalizations. The
remaining RG packet must freeze those scalars, retained quartics/SM couplings,
scheme, loop order, and finite threshold maps before deriving beta functions.

## Radial-quartic RG closure: WP493

- `flavor-radial-quartic-rg-closure.md`
- `checkers/wp493_radial_quartic_rg_closure.py`
- `results/wp493_radial_quartic_rg_closure.json`

WP493 proves that WP489's positive sum-of-squares coefficient surface is not
an RG-closed truncation. Its `F^2 sigma^2`, `H^2 sigma^2`, and
`R^2 sigma^2` vertices generate the missing `F^2 H^2`, `F^2 R^2`, and
`H^2 R^2` counterterm support at one loop. The exact vertex products are
nonzero throughout the positive source domain. The minimal radial basis has
four self quartics plus all six pairwise portals, ten independent running
couplings. Sum-square relations can be boundary data but carry no RG-invariant
authority. Nonradial invariant closure remains to be audited before deriving a
complete beta vector field.

## Port-alignment RG closure: WP494

- `flavor-port-alignment-rg-closure.md`
- `checkers/wp494_port_alignment_rg_closure.py`
- `results/wp494_port_alignment_rg_closure.json`

WP494 proves that WP493's radial completion is still nonradially incomplete.
The exact `SO(3)_P` generator identity reduces the connector-flavon gauge
contraction to `Tr(G_S)Tr(G_X)-Tr(G_S G_X)`. The first term is radial; the
second is an independent alignment quartic absent from WP493. Parallel and
orthogonal unit port vectors have identical radial data but gauge contractions
zero and one. At the isotropic vacuum the radial and alignment invariants are
`18 s^2 mu^2` and `6 s^2 mu^2`, so the generated combination is nonzero. Its
coefficient must run independently before the scalar vacuum, thresholds, or
fixed point can be recomputed with RG authority.

## Adjoint port-Gram RG closure: WP495

- `flavor-adjoint-gram-rg-closure.md`
- `checkers/wp495_adjoint_gram_rg_closure.py`
- `results/wp495_adjoint_gram_rg_closure.json`

WP495 shows that the WP447 radial-plus-commutator adjoint basis is not closed
after port gauging. `SO(3)_P` support contains
`(Tr G_X)^2-Tr(G_X^2)`, and the Gram-square term is independent. The exact
commuting hostile pair `(T_3,T_3,0)` versus `(T_3,T_8,0)` has equal radial
invariant one and commutator invariant zero but Gram-square values one and
one-half. At the spin-one vacuum the radial and Gram-square values are
`36 mu^4` and `12 mu^4`, so the gauge-supported combination is nonzero. The
Gram-square coefficient must run independently; the remaining single-trace
adjoint and cyclic-row connector invariant census is still open.

## Adjoint quartic Cayley-Hamilton closure: WP496

- `flavor-adjoint-quartic-cayley-hamilton.md`
- `checkers/wp496_adjoint_quartic_cayley_hamilton.py`
- `results/wp496_adjoint_quartic_cayley_hamilton.json`

WP496 closes the scoped parity-even pure-adjoint quartic census. The polarized
traceless-`3x3` Cayley-Hamilton identity reduces both delta-contracted
single-trace words uniquely to the radial, Gram-square, and commutator
invariants. At the spin-one vacuum these basis values are
`36 mu^4,12 mu^4,6 mu^4`, and the direct reductions agree exactly. Thus WP495's
Gram-square coordinate is the only additional coupling needed in this scoped
pure-adjoint sector. Cyclic-row connector invariants and mixed tensor portals
remain before rebuilding the complete scalar Hessian.

## Cyclic-row connector quartic census: WP497

- `flavor-cyclic-row-quartic-census.md`
- `checkers/wp497_cyclic_row_quartic_census.py`
- `results/wp497_cyclic_row_quartic_census.json`

WP497 solves the exact `C3` invariance equations for quartics quadratic in the
six entries of `R=SS^T`. The invariant space has dimension seven, with an
explicit orbit-sum basis. WP483's frame Frobenius form plus WP493's radial
square span only rank two, leaving codimension five. The omitted directions
vanish at the isotropic vacuum but affect fluctuations and are permitted by the
declared row symmetry. A complete source must either enhance the row symmetry
or promote all seven invariants to independent running couplings before the
full Hessian and threshold cone are recomputed.

## Equal-entrance stabilizer quartic obstruction: WP498

- `flavor-entrance-stabilizer-quartic-obstruction.md`
- `checkers/wp498_entrance_stabilizer_quartic_obstruction.py`
- `results/wp498_entrance_stabilizer_quartic_obstruction.json`

WP498 tests whether a stronger symmetry already compatible with the canonical
messenger grammar repairs WP497. With canonical row kinetic normalization, the
largest orthogonal symmetry preserving the frozen nonzero equal-entrance
vector is \(O(2)\). Its exact connector-quartic invariant space has dimension
five, while the retained radial and Frobenius forms span rank two. Full row
\(SO(3)\) would reduce the space to two invariants, but it moves the entrance
vector and forbids the existing nonzero entrance vertex. Symmetry-only closure
therefore fails: either run the full five-coupling stabilizer basis or add a
new dynamical entrance field and recompute the complete spectrum and readout.

## Complete stabilizer-compatible connector Hessian: WP499

- `flavor-o2-connector-hessian.md`
- `checkers/wp499_o2_connector_hessian.py`
- `results/wp499_o2_connector_hessian.json`

WP499 follows the minimally enlarged existing-source branch. The complete
\(O(2)\)-invariant connector potential has two quadratic and five quartic
coordinates. Exact isotropic stationarity fixes the two quadratic coefficients.
After the three right-gauge tangents are removed, the six physical modes form a
mixed singlet pair, a vector doublet with mass squared \(4s^2\lambda _4\), and
a tensor doublet with mass squared \(16s^2\lambda _5\). The exact local
positivity cone is stated. The old sixfold mass \(8s^2\lambda\) occurs only on
the full-row-symmetric coefficient slice that WP498 found incompatible with the
nonzero entrance source. Consequently old connector widths cannot be reused;
the five couplings and mixed-sector running must be independently frozen first.

## Coherent-tree and traced-loop connector split: WP500

- `flavor-tree-loop-port-split.md`
- `checkers/wp500_tree_loop_port_split.py`
- `results/wp500_tree_loop_port_split.json`

WP500 distinguishes two contractions generated by the same connector grammar.
Tree elimination yields the coherent port (p=S^Th), whose vacuum outer
product has rank one. A closed messenger loop traces the row label and yields
(W_{\mathrm{loop}}=S^TS/3) for WP492's normalized equal entrance; it has rank
three and determinant (s^6/27). On WP499's physical connector modes, the tree
Jacobian has rank three with a three-dimensional kernel, while the formal loop
Gram Jacobian has rank six. Shared up/down tree ports remain collinear, so the
loop isotropy repair cannot be transported into a generic `physical16` Yukawa
map. The loop is a formal full-rank rigidifier, but no six-coordinate physical
threshold instrument is yet admitted.

## Externally distinguishable entrance rank theorem: WP501

- `flavor-external-entrance-rank-theorem.md`
- `checkers/wp501_external_entrance_rank_theorem.py`
- `results/wp501_external_entrance_rank_theorem.json`

WP501 gives the exact repair theorem for WP500. For external preparation matrix
(H) and invertible connector (S), the tree map (P=HS) is faithful on all
three adjoint directions exactly when (\operatorname{rank}H=3). Hence three
externally distinguishable channels are necessary, and three orthonormal
channels are sufficient for the isotropic Gram (s^2I_3). Cauchy-Binet gives
the general finite-family criterion. Generic rank three guarantees separation
but not isotropy, and neither property selects the normalization. The current
shared up/down entrances have rank one. No admitted physical preparation and
calibrated readout yet realizes the required three persistent external labels.

## Gauged entrance-triplet stabilizer: WP502

- `flavor-gauged-entrance-triplet-stabilizer.md`
- `checkers/wp502_gauged_entrance_triplet_stabilizer.py`
- `results/wp502_gauged_entrance_triplet_stabilizer.json`

WP502 tests a renormalizable realization of WP501 using electroweak-doublet
row triplets and a gauged entrance (SO(3)_E). At the connector-plus-adjoint
vacuum, the enlarged fourteen-generator gauge orbit has rank eleven because a
three-dimensional diagonal row/port/spin-one-flavor stabilizer survives. One
entrance-triplet vev raises the rank to thirteen and leaves one massless gauge
direction. Two noncollinear entrance vevs raise it to fourteen and remove the
continuous stabilizer exactly. This is a conditional carrier completion, not
an instrument: the two-triplet potential, full masses and widths, and survival
of three independently calibrated detector channels remain to be derived.

## Positive noncollinear entrance vacuum: WP503

- `flavor-noncollinear-entrance-vacuum.md`
- `checkers/wp503_noncollinear_entrance_vacuum.py`
- `results/wp503_noncollinear_entrance_vacuum.json`

WP503 constructs a positive renormalizable two-vector potential on the neutral
CP-even row-order-parameter subspace. Its global zero fixes two nonzero entrance
vectors to be orthogonal. The exact six-dimensional Hessian has three zeros,
all and only the gauged row-rotation tangents, plus positive radial masses
(8\lambda_u a^2), (8\lambda_d b^2), and relative-angle mass
(2\kappa(a^2+b^2)). This proves the noncollinear vacuum on the scoped row
sector, but not on the complete complex electroweak-doublet space. The source
rigidifies the angle while leaving both norms and their ratio unselected.

## Minimal complex entrance flat-direction obstruction: WP504

- `flavor-complex-entrance-flat-obstruction.md`
- `checkers/wp504_complex_entrance_flat_obstruction.py`
- `results/wp504_complex_entrance_flat_obstruction.json`

WP504 tests the direct Hermitian complex lift of WP503. On the twelve-real
dimensional neutral space, its exact Hessian has rank four and nullity eight.
The admitted row-plus-hypercharge gauge orbit accounts for only four null
directions; four independent physical neutral flats remain, including the
relative entrance phase. Thus the real noncollinear vacuum cannot yet be used
as a physical multi-doublet pole packet. The complete renormalizable invariant
basis needs independently justified phase-sensitive terms, followed by a full
charged, CP-even, and CP-odd Hessian audit.

## Positive complex neutral entrance-kernel closure: WP505

- `flavor-complex-entrance-kernel-closure.md`
- `checkers/wp505_complex_entrance_kernel_closure.py`
- `results/wp505_complex_entrance_kernel_closure.json`

WP505 adds four positive renormalizable invariants available for complex vectors
in the real row representation: two reality penalties, a holomorphic cross
norm, and a relative-phase locking square. The orthogonal real vacuum remains a
global zero. Its twelve-real-dimensional neutral Hessian now has rank eight and
nullity four, with kernel exactly equal to the three row rotations plus common
hypercharge. Every WP504 physical flat is lifted. The phase-locking coefficient
uses the predeclared norm ratio (a^2/b^2), so this closes the neutral spectrum
without selecting that ratio. Charged components and full pole, residue, width,
and detector calculations remain open.

## Full electroweak entrance-sector kernel closure: WP506

- `flavor-full-doublet-entrance-kernel-closure.md`
- `checkers/wp506_full_doublet_hessian_attempt.py`
- `results/wp506_full_doublet_hessian_attempt.json`

WP506 replaces the neutral abstraction by two complete complex electroweak
doublet triplets and a manifestly positive
(SO(3)_E\times SU(2)_L\times U(1)_Y)-invariant source. The Cauchy phase gap
has an exact sum-of-squares decomposition. At the orthogonal neutral vacuum,
the full twenty-four-real-dimensional Hessian has rank eighteen and nullity
six. Its kernel is exactly the six-dimensional broken row-plus-electroweak
gauge orbit, so no physical charged, CP-even, or CP-odd flat remains in the
entrance sector. The source remains a rigidifier: \(a,b\), their ratio, and all
dimensionless couplings are unselected. Complete mixed poles, residues, widths,
and detector response remain the successor gate.

## Complete gauge-tangent Gram and photon kernel: WP507

- `flavor-complete-gauge-gram-rank.md`
- `checkers/wp507_complete_gauge_gram_rank.py`
- `results/wp507_complete_gauge_gram_rank.json`

WP507 combines the flavor adjoints, connector, full entrance doublets, and all
five gauge factors. The eighteen-generator tangent Gram has rank seventeen.
Its flavor–port–row block has rank fourteen, its electroweak block has the
standard rank-three form, and their cross block vanishes at the real neutral
vacuum. The unique kernel is the electromagnetic generator
\(T_3/g_2+Y/g_Y\). This proves complete gauge support but not selected pole
values: canonical kinetic normalization, diagonalization, current residues,
all open widths, and detector response remain to be derived.

## Canonical heavy gauge poles and current resolvents: WP508

- `flavor-canonical-heavy-gauge-poles.md`
- `checkers/wp508_canonical_heavy_gauge_poles.py`
- `results/wp508_canonical_heavy_gauge_poles.json`

WP508 applies the canonical connector, adjoint, and complex-doublet kinetic
metrics and restores the physical (SU(3)_F) generator normalization. It
recovers the five quintet factors at (3g_F^2\mu^2). The remaining nine heavy
poles form three exact cubic flavor–port–row sectors, distinguished by entrance
coordinates (a^2,a^2+b^2,b^2). In the Gell-Mann basis each cubic shares a
four-generator block with one quintet direction, so the exact flavor-current
readout is a (2\times2) matrix resolvent; its adjugate numerators and factored
denominators are generated exactly. Numerical roots, individual residues,
channel-complete widths, and detector calibration remain unselected.

## Heavy-pole spectral residues and conditional widths: WP509

- `flavor-spectral-residue-width-sum-rules.md`
- `checkers/wp509_spectral_residue_width_sum_rules.py`
- `results/wp509_spectral_residue_width_sum_rules.json`

WP509 extracts exact pole projectors from each WP508 matrix resolvent on the
positive simple-spectrum domain. The embedded quintet and every cubic root
carry rank-one flavor-current residues, with matrix completeness sum
\(R_Q+\sum_\rho R_\rho=g_F^2I_2\). Under the independently declared
six-massless-quark approximation this freezes conditional partial widths and
the sector sum \(\sum\Gamma_q/M=g_F^2/(2\pi)\). It does not establish total
widths: the enlarged scalar, messenger, and vector thresholds remain to be
closed in the same source vacuum. Numerical coefficient selection and a
calibrated pole-current instrument also remain open.

## Common-source complete tree-level width closure: WP510

- `flavor-common-source-total-width-closure.md`
- `checkers/wp510_common_source_total_width_closure.py`
- `results/wp510_common_source_total_width_closure.json`

WP510 constructs one exact singlet-clock source witness for the complete WP508
vacuum. Exact root counting places all fourteen heavy poles in
\((19/10,31/5)\), whose spread closes every heavy-vector-pair channel. The
same source puts all physical scalar, messenger, and massive electroweak
thresholds above \(31/20\), so WP509's six-quark partial widths are the
complete declared tree-level widths. The action conditionally fixes
\((g_Ff_{\mathrm{phys}}/v_{\mathrm{phys}})^2=6/5941\), but the dimensionless witness
coefficients remain unpredicted. Loop/off-shell completion and a calibrated
matrix-current pole instrument remain open.

## Executable neutral-B flavor-current instrument: WP511

- `flavor-neutral-b-current-instrument.md`
- `checkers/wp511_neutral_b_current_instrument.py`
- `results/wp511_neutral_b_current_instrument.json`

WP511 attaches the pinned `flavio` 2.7.0 \(\Delta M_d\) and \(\Delta M_s\)
likelihoods to the two real correlated vector-current rays in the `bdbd` and
`bsbs` sectors. With an independently frozen correlated theory covariance,
the response Jacobian and detector-weighted Gram both have rank two. This is
an actual CP-even calibrated current instrument on the declared two-coordinate
WET packet. The ratio \(\Delta M_d/\Delta M_s\) obeys the quotient chain rule
and adds no third local direction. The upstream messenger-vacuum orientation
map remains unselected, and the contact experiment cannot resolve WP509's
individual pole residues or widths.

## Electroweak-calibrated aligned-source falsifier: WP512

- `flavor-aligned-source-bmixing-falsifier.md`
- `checkers/wp512_aligned_source_bmixing_falsifier.py`
- `results/wp512_aligned_source_bmixing_falsifier.json`

WP512 composes the simplest WP450 down-sector alignment with the WP510 source
and WP511 instrument in one physical frame. The exact current map has
\(C_{bd}=0\) and \(C_{bs}=C_{sd}=729/17971525\), so the rank-two detector sees
only a rank-one aligned source image. Calibrating the same entrance doublets to
\(v_{\mathrm{phys}}=246\) GeV fixes the common clock and predicts
\(x_s=-81/20340100\) GeV\(^{-2}\). The full pinned likelihood then predicts
\(\Delta M_s\approx2.69\mathbin{\cdot}10^{-6}\), over five million frozen
standard deviations from the measurement. This excludes the aligned WP510
completion, not every orientation in WP450's still-unselected fiber. A source
orientation law must be derived before any alternative is tested.

## Aligned width-closure/current incompatibility: WP513

- `flavor-aligned-closure-current-no-go.md`
- `checkers/wp513_aligned_closure_current_no_go.py`
- `results/wp513_aligned_closure_current_no_go.json`

WP513 closes the entire principal-frame-aligned messenger family, not merely
the WP510 witness. The exact matched coefficient is
\(x_s=-(b/a)^2/(4v_{\mathrm{phys}}^2)\). Global vector-pair closure forces
\(1/8<b/a<8\) because the relevant three-root determinant ratio is
\(a^2/b^2\). Thus the observed electroweak norm implies
\(|x_s|>1/15492096\) GeV\(^{-2}\). The least-magnitude boundary already
predicts \(\Delta M_s\approx4.37\mathbin{\cdot}10^{-8}\), about 86,968 frozen
standard deviations from the calibrated instrument. An aligned source cannot
retain both quark-only total-width closure and B-mixing viability. A successor
must derive a nonaligned orientation or calculate the newly open widths.

## Entrance-defined orientation B-current no-go: WP514

- `flavor-entrance-orientation-bd-no-go.md`
- `checkers/wp514_entrance_orientation_bd_no_go.py`
- `results/wp514_entrance_orientation_bd_no_go.json`

WP514 tests the minimal connector-mediated nonaligned law: the entrance ray
\((a,b)\) fixes a real 1–3 mass-basis rotation before the instrument is read.
Its exact \(bd\) current is strictly positive. Electroweak matching and the
WP513 closure bound imply \(|x_d|>2/(65v_{\mathrm{phys}}^2)\), or
\(1/1966770\) GeV\(^{-2}\) at 246 GeV. The least-magnitude boundary predicts
\(\Delta M_d\approx2.40\mathbin{\cdot}10^{-7}\), over 10.8 million frozen
standard deviations from WP511. Thus both the aligned law and the simplest
source-derived nonaligned law are incompatible with quark-only total-width
closure. Further rotation requires new independently declared geometry.

## B-mixing-forced pole hierarchy: WP515

- `flavor-bmixing-forced-pole-hierarchy.md`
- `checkers/wp515_bmixing_forced_pole_hierarchy.py`
- `results/wp515_bmixing_forced_pole_hierarchy.json`

WP515 inverts the full executable \(\Delta M_s\) response on the aligned
negative current ray. The frozen 1.96-standard-deviation endpoint requires
\(b/a<0.002934563\). Since the exact ratio of the \(a^2\)- and \(b^2\)-sector
three-root products is \(a^2/b^2\), every compatible spectrum has global
squared-mass spread above 48.787. This is incompatible with WP510's sufficient
spread-below-four quark-only width certificate. The result proves loss of that
certificate, not an open decay vertex. The successor must transport the
nonabelian and scalar vertices into a hierarchical mass basis and compute the
allowed widths explicitly.

## Hierarchical mass-basis vector vertices: WP516

- `flavor-hierarchical-mass-basis-vertices.md`
- `checkers/wp516_hierarchical_mass_basis_vertices.py`
- `results/wp516_hierarchical_mass_basis_vertices.json`

WP516 transports the exact \(SU(3)_F\times SU(2)_P\times SU(2)_E\) cubic
gauge tensor through the canonical fourteen-pole mass rotation at one
electroweak-normalized witness with \(a/b=400\). The ratio lies inside WP515's
formal contact-coordinate interval, but WP519 retracts the \(B_s\)-compatibility
label because no source-to-WET threshold map is admitted. The executable
census finds 34 resolved open channels,
with maximum threshold margin 3.52903 GeV and maximum transported coupling
\(5.35897\mathbin{\cdot}10^{-3}\). This disproves a universal zero-vertex
rescue of the hierarchical branch. It is an existence witness, not a selected
source point or a total-width calculation. The successor must derive the
unequal-mass vector width functional, add scalar channels, and attach a
pole-resolved decay instrument.

## Unequal-vector partial widths: WP517

- `flavor-unequal-vector-partial-widths.md`
- `checkers/wp517_unequal_vector_partial_widths.py`
- `results/wp517_unequal_vector_partial_widths.json`

WP517 derives the unequal-mass Yang--Mills decay functional by an explicit
physical-polarization contraction and applies it to all 34 resolved WP516
channels. Every partial width is positive. The largest is 0.00493152 GeV; the
four contributing parents have resolved vector fractional-width sums between
\(3.77\mathbin{\cdot}10^{-6}\) and \(2.18\mathbin{\cdot}10^{-3}\). Orthogonal
rotation within a complete exactly degenerate daughter subspace preserves the
summed squared coupling. These are independently normalized vector partial
widths, not total widths: quark-residue ordering, scalar and sub-resolution
channels, and pole-resolved detector response remain to be composed.

## Common-order residue and width composition: WP518

- `flavor-common-order-residue-width-composition.md`
- `checkers/wp518_common_order_residue_width_composition.py`
- `results/wp518_common_order_residue_width_composition.json`

WP518 evaluates the WP508/WP509 current-residue functionals at the WP516
witness and matches all nine cubic roots plus five quintet poles into the same
fourteen-state mass ordering used by WP517. Every cubic residue is positive,
each sector saturates its \(g_F^2\) trace sum, and the global residue trace is
\(8g_F^2=16\). Resolved vector widths add to states 4, 5, 12, and 13. The
resulting quark-plus-resolved-vector quantities are channel-explicit lower
bounds, not total widths. Scalar, off-shell, and sub-resolution channels plus
a pole-resolved detector response remain open.

## WET matching-domain correction: WP519

- flavor-wet-matching-domain-correction.md
- checkers/wp519_wet_matching_domain_audit.py
- results/wp519_wet_matching_domain_audit.json

WP519 locates the first nonfaithful arrow in WP516--WP518. WP511 admits local
WET coefficients at 160 GeV, whereas all fourteen WP516 poles lie below
4.947 GeV and the lightest lies at 0.0121 GeV. No finite-propagator threshold
matching and running constructor was declared. Consequently the WP516 ratio
passes only a formal contact-coordinate inequality; it is not authorized as a
\(B_s\)-compatible source point. The mass spectrum, vertices, residues, and
partial widths remain valid source-model calculations. Restoring flavor
compatibility requires matching every pole threshold, running to the hadronic
domain, and re-evaluating the calibrated \(\Delta M_s\) likelihood.

## Finite-propagator aligned bs kernel: WP520

- flavor-finite-propagator-bs-kernel.md
- checkers/wp520_finite_propagator_bs_kernel.py
- results/wp520_finite_propagator_bs_kernel.json

WP520 constructs the exact aligned \(bs\) matrix-current resolvent at the
WP516 source witness. It recovers WP513 at zero momentum but has normalized
slope \(-2395516267/1613760000\ \mathrm{GeV}^{-2}\), so a single
momentum-independent WET coefficient cannot represent it away from contact.
The normalized spacelike kernel is 0.702 at 0.5 GeV and 0.285 at 1 GeV.
These are hostile nonlocality diagnostics, not a hadronic momentum model.
The remaining interface is a calibrated bilocal neutral-\(B\) matrix element
with legal threshold running and uncertainties.

## Bilocal neutral-B moment obstruction: WP521

- flavor-bilocal-moment-obstruction.md
- checkers/wp521_bilocal_moment_obstruction.py
- results/wp521_bilocal_moment_obstruction.json

WP521 proves that neither WP511's contact normalization nor any finite tower
of ordinary \(q^2\) moments determines the exact WP520 convolution on a
hostile positive normalized measure class. The reduced form factor has
denominator degree six and is not in any finite polynomial-moment span.
Explicit positive measure pairs matching moments through orders zero to six
all have distinct responses. The remaining legal instrument is the calibrated
bilocal matrix element itself, or a complete source-authorized representation
with a controlled truncation-error theorem.

## Resolvent bilocal authority split: WP522

- flavor-resolvent-bilocal-authority-split.md
- checkers/wp522_six_resolvent_bilocal_basis.py
- results/wp522_six_resolvent_bilocal_basis.json

WP522 replaces the failed polynomial-moment strategy with a source-shaped
rational representation. The frozen WP520 numerator is constant, so one
direct functional \(H_0=\int D(q^2)^{-1}d\mu\) determines its exact bilocal
response. Six functions \((q^2)^k/D(q^2)\) are complete and generically
minimal only for the algebraically enlarged degree-below-six numerator family.
No source operation independently prepares those numerator directions, so the
six-dimensional span is not executable control. The remaining physical gate
is a calibrated computation of the single direct \(H_0\) matrix element with
threshold running and uncertainties.

## WP522 H0 instrument census: WP523

- `flavor-h0-instrument-census.md`
- `checkers/wp523_h0_instrument_census.py`
- `results/wp523_h0_instrument_census.json`

WP523 freezes a bounded primary-source census. The neutral-B lattice sources
found provide local five-operator matrix elements or bag parameters, so they
instantiate WP511's local WET readout but not WP522's direct resolvent
functional. Bilocal integrated-correlator methods exist in kaon mixing and
provide a transferable technical precedent, not calibrated B_s data. The
remaining gate is one common-frame B_s calculation weighted by the exact
WP522 denominator, with renormalization, threshold matching, continuum and
finite-volume control, heavy-quark systematics, normalization, and covariance.

## Euclidean H0 tensor-completion gate: WP524

- `flavor-euclidean-h0-tensor-completion-gate.md`
- `checkers/wp524_euclidean_h0_estimator.py`
- `results/wp524_euclidean_h0_estimator.json`

WP524 constructs an exact lattice discretization of WP522's scalar resolvent
kernel, proves that its six poles are timelike and that its continuum error
starts at order \(a^2\), then blocks the physical-instrument inference. The
left-handed \(b\)-to-\(s\) current is not conserved:
\(q_\mu J_L^\mu=m_bS_R-m_sS_L\). Hence longitudinal massive-vector exchange,
Goldstone cancellation, and induced scalar operators are not determined by
the scalar WP520 form factor. The next source packet must derive the complete
gauge-independent tensor-plus-Goldstone bilocal kernel before any calibrated
\(B_s\) ensemble evaluation can identify the physical exchange.

## Complex-mass Ward completion: WP525

- `flavor-complex-mass-ward-completion.md`
- `checkers/wp525_complex_mass_ward_completion.py`
- `results/wp525_complex_mass_ward_completion.json`

WP525 derives the polewise \(R_\xi\) vector-plus-Goldstone completion and
proves exact gauge-parameter cancellation when one common real or complex pole
parameter is used everywhere. A hostile partial width insertion leaves an
exact nonzero \(\xi\)-derivative, so widths cannot be added only to visible
vector denominators. WP509/WP520 already provide signed residue algebra, but
WP518's hierarchical width entries are lower bounds. The next legal interface
must close all pole widths, transport residues and self-energies into one
complex-pole scheme, and measure the induced vector-plus-scalar bilocal basis.

## Messenger-width hostile pair: WP526

- `flavor-messenger-width-hostile-pair.md`
- `checkers/wp526_messenger_width_hostile_pair.py`
- `results/wp526_messenger_width_hostile_pair.json`

WP526 proves that the hierarchical pole and residue packet does not determine
channel-complete tree widths. One exact aligned pole obeys
\(24<M^2<25\) GeV squared. With the same gauge and vacuum data, the
source-authorized choices \(z_A=1\) and \(z_A=3\) respectively open and close
a messenger pair while leaving the tree vector polynomial unchanged. WP518's
widths therefore remain lower bounds. A legal WP525 complex pole requires the
messenger Yukawas, scalar spectrum, complete channel census, signed residues,
and self-energies to be frozen in one common source witness and perturbative
scheme.

## Hierarchical nonquark threshold closure: WP527

- `flavor-hierarchical-nonquark-closure.md`
- `checkers/wp527_hierarchical_nonquark_closure.py`
- `results/wp527_hierarchical_nonquark_closure.json`

WP527 constructs a common-source completion of the WP516 hierarchical witness
in which every declared nonquark pair threshold is closed. Exact Sturm counts
place all vector mass squares below 25, while the frozen entrance, radial,
adjoint, connector, messenger, and electroweak spectra all exceed the required
daughter bound 25/4. This repairs WP526's source-support ambiguity on one
conditional witness. Total-width authority still fails because WP516 retained
mass-basis vector vertices only above a numerical \(10^{-7}\) cutoff. The next
finite task is exact algebraic enumeration of every vector threshold and
transported vertex before composing the complete self-energies with WP525.

## Vector-cutoff width envelope: WP528

- flavor-vector-cutoff-width-envelope.md
- checkers/wp528_vector_cutoff_width_envelope.py
- results/wp528_vector_cutoff_width_envelope.json

WP528 audits whether WP516's \(10^{-7}\) coupling cutoff can be treated as
negligible without exact channel enumeration. Exact pole bounds and WP517's
longitudinal unequal-mass functional give the available uniform unresolved
width bound \(7007/(10240\pi)\) GeV, about 0.218 GeV. This deliberately loose
upper bound does not show that a large width is missing; it shows that the
cutoff alone cannot certify a small missing width. Exact projectors or
channel-specific interval bounds remain necessary, especially for channels
containing the lightest vector pole.

## Lightweight pre-cutoff vector census: WP529

- flavor-lightweight-vector-census.md
- checkers/wp529_lightweight_vector_census.py
- results/wp529_lightweight_vector_census.json

WP529 reconstructs WP516's fourteen-state mass matrix directly from the WP507
gauge tangents and canonical WP508 metrics, reproducing stored masses within
\(6.43\times10^{-14}\) GeV. Before applying the \(10^{-7}\) cutoff it finds
eight additional threshold-open coupling candidates above the numerical-zero
cluster. Their candidate width sum is only \(3.13\times10^{-16}\) GeV, but
near-degenerate eigenvector sensitivity prevents exact admission. The next
step is high-precision interval certification of cluster-summed spectral
projector couplings.

## Multiprecision vector-candidate collapse: WP530

- flavor-multiprecision-vector-collapse.md
- checkers/wp530_multiprecision_vector_candidates.py
- results/wp530_multiprecision_vector_candidates.json

WP530 independently reconstructs the eight WP529 candidates at 50, 80, and
120 digits. Their largest coupling collapses from \(4.68\times10^{-46}\) to
\(1.45\times10^{-115}\), tracking the eigenpair residual, while their summed
width collapses below \(10^{-225}\) GeV. They are numerical basis artifacts
consistent with exact structural zeros, so WP529's provisional
candidate-channel interpretation is superseded. Exact total-width authority
now needs only the block-support proof that the relevant restricted
Yang--Mills tensors vanish.

## Exact candidate block zeros: WP531

- flavor-exact-candidate-block-zeros.md
- checkers/wp531_exact_candidate_block_zeros.py
- results/wp531_exact_candidate_block_zeros.json

WP531 supplies the exact proof requested by WP530. The eight apparent
sub-cutoff channels occupy four ordered tensor restrictions built from the
three exact WP508 four-generator blocks. Every entry of all four restrictions
vanishes symbolically, and arbitrary within-block mass rotations preserve
that zero. The eight entries are therefore eigensolver leakage, not physical
decay support. Complete vector-width authority still requires an exact
five-dimensional quintet projector and a basis-invariant audit of all
remaining threshold-open numerical-zero classes.

## Quintet projector width sum: WP532

- flavor-quintet-projector-width-sum.md
- checkers/wp532_quintet_projector_width_sum.py
- results/wp532_quintet_projector_width_sum.json

WP532 constructs the exact rank-five mass-six spectral projector and contracts
the cubic tensor over a complete unordered quintet pair. The resulting parent
operator is exactly \(S=(5/2)P_3\), with \(P_3\) the complementary
principal-triplet projector. A hostile quintet-frame rotation changes an
individual displayed coupling while preserving the complete norm. Hence
WP517's twenty quintet-pair rows are coordinate expansions of two invariant
parent-level sums, not twenty separately physical channels. The remaining
width gate is an exact projector/block classification of the 131
threshold-open numerical-zero triples.

## Exact open-channel partition: WP533

- flavor-exact-open-channel-partition.md
- checkers/wp533_exact_open_zero_classification.py
- results/wp533_exact_open_zero_classification.json

WP533 removes numerical-cutoff authority from the complete WP516 threshold
census. The exact decomposition \(Q\oplus C_0\oplus C_1\oplus C_2\) yields
49 zero and 15 nonzero ordered tensor restrictions. Of 173 threshold-open
coordinate triples, exactly 139 are forbidden: all 131 numerical-zero entries
and the eight WP529 candidates. The 34-coordinate complement is exactly the
WP516/WP517 channel list. No unresolved zero class remains. The successor can
therefore aggregate the 34 rows into invariant parent-level widths and compose
them with the WP527 source closure and WP525 Ward-complete propagator.

## Invariant complex-pole packet: WP534

- flavor-invariant-complex-pole-packet.md
- checkers/wp534_invariant_complex_pole_packet.py
- results/wp534_invariant_complex_pole_packet.json

WP534 reduces the 34 exact channel rows to sixteen invariant decay groups,
adds the independently normalized quark widths, and promotes WP518's lower
bounds to channel-complete declared tree widths on the bounded WP527 source
domain. The fivefold quintet becomes one projector-valued complex pole; nine
cubic poles remain simple. Six signed \(b\!-\!s\) residues are extracted from
WP520 at high precision and reconstruct its zero-momentum kernel exactly.
The same complex mass in every vector, longitudinal and Goldstone occurrence
preserves the WP525 Ward identity. The remaining gate is the renormalized
vector-plus-scalar bilocal matrix-element instrument with covariance, followed
by production, lineshape and detector response.

## Six-port bilocal instrument: WP535

- flavor-six-port-bilocal-instrument.md
- checkers/wp535_six_port_bilocal_instrument.py
- results/wp535_six_port_bilocal_instrument.json

WP535 derives the minimal Ward-complete lattice interface for WP534's six
signed complex poles. Six pole kernels times four operator channels require
24 complex estimators, reported as 48 real components with full covariance.
The source-generated pole-resolved map has rank six. The experimental
\(\Delta M_s\) scalar has rank one and an exact five-dimensional kernel; a
nonzero two-pole hostile displacement is invisible after this compression but
visible to the six-port vector. The packet specifies an executable lattice
instrument, while WP523's census still withholds realization authority until
the correlators and \(48\times48\) calibrated covariance are actually
computed.

## Selector-width common-source gate: WP536

- flavor-selector-width-common-source-gate.md
- checkers/wp536_selector_width_common_source_gate.py
- results/wp536_selector_width_common_source_gate.json

WP536 proves that WP477's withheld five-TeV ratio and WP534's complete
declared tree widths do not inhabit one admitted source point. The width
witness has \(c=15129\) and \(g_Ff/v=\sqrt3/123\); the target requires
\(c=151560721/125000000000\), a clock-ratio change by about 3532. A common
scale change cannot repair a dimensionless mismatch. At fixed electroweak
norm and other witness coefficients, imposing the target opens the lightest
entrance-scalar pair below the quintet, invalidating WP527's nonquark closure.
The selected point therefore requires a new vacuum, threshold, pole, residue
and width computation before the WP535 instrument can be applied.

## First bounded release: WP117

- `flavor-uv-source-equivalence-conventions.md`
- `flavor-uv-to-physical16-contract.md`
- `flavor-uv-ensemble-hostile-controls.md`
- `contracts/flavor-uv-ensemble-data-descent.v2.json`
- `checkers/wp117_uv_ensemble_contract.py`
- `results/wp117_uv_ensemble_contract.json`

WP117 types all twelve packages and proves the decisive finite descent
falsifier. It does not invent the missing UV action or measure. Its current
classification is **undefined without additional source data**.

## DPC hostile reduction: WP118

- `flavor-dpc-bounded-audit-framework.md`
- `checkers/wp118_flavor_dpc_bounded_audit.py`
- `results/wp118_flavor_dpc_bounded_audit.json`

WP118 retracts the universal flavor DPC and retains a bounded source-relative
audit. It permits point predictions, quotient-only measures, universality,
memory augmentation, calibrated detector conditioning, and approximate
recovered-ensemble bounds. The physical source produces an ensemble/channel;
a separate verification model produces its certificate. No flavor candidate
is admitted until one independently validated bounded UV class and its
accuracy, scale, scheme, time, and resource budgets are frozen.

## First candidate-class audit: WP119

- `flavor-first-bounded-uv-candidate-audit.md`
- `checkers/wp119_first_bounded_uv_candidate_audit.py`
- `results/wp119_first_bounded_uv_candidate_audit.json`

WP119 freezes the retrospective four-member class `C_FUV_0`: SM one-loop RG,
the fixed FDM-2 benchmark, the two-parameter repair, and the WP117 abstract UV
template. Zero candidates pass the eight-field WP118 admission gate. Because
all four routes have already inspected historical flavor readouts, no
agreement with the 1,210-sheet ensemble counts as a protected prediction.

## First concrete normalized ensemble: WP120

- `flavor-gaussian-yukawa-ensemble-audit.md`
- `checkers/wp120_gaussian_yukawa_ensemble_audit.py`
- `results/wp120_gaussian_yukawa_ensemble_audit.json`

WP120 constructs the isotropic complex-Gaussian law on two `3 x 3` Yukawa
matrices. The measure is exactly normalized, invariant under the full weak-
basis group, and pushes to Wishart spectra with a Haar relative CKM frame. It
is therefore a genuine mathematical probability law on `physical16`, not a
texture chart. It still fails the bounded DPC at independent physical source
validation: Gaussianity, its scale, and its RG/matching contract are posited,
not derived from an admitted production mechanism.

## Conditional stochastic production: WP121

- `flavor-ou-yukawa-production-audit.md`
- `checkers/wp121_ou_yukawa_production_audit.py`
- `results/wp121_ou_yukawa_production_audit.json`

WP121 derives WP120's Gaussian measure as the unique stationary law of a
weak-basis-equivariant matrix Ornstein–Uhlenbeck process, with
`beta=kappa/(2D)`, exact semigroup composition, finite-time convergence, and
stacky quotient descent. This is a conditional production model, not an
admitted physical source: the dynamical Yukawa substrate, microscopic bath,
fluctuation–dissipation inputs, UV scale, and RG/matching transport remain
postulated.

## Thermal source and freeze-out obstruction: WP122

- `flavor-thermal-flavon-freezeout-audit.md`
- `checkers/wp122_thermal_flavon_freezeout_audit.py`
- `results/wp122_thermal_flavon_freezeout_audit.json`

WP122 derives the WP121 OU coefficients from an isotropic overdamped thermal
matrix-flavon zero mode: `kappa=m^2/eta`, `D=T/(eta V_c)`, and
`beta_eff=V_c m^2/(2T)`. It also proves the decisive obstruction: equilibrium
variance scales as `T/(V_c m^2)`, so the homogeneous draw collapses to zero in
the thermodynamic limit, while an active finite-volume bath leaves Yukawas
time-dependent. A quench and post-quench stabilization define a new physical
history whose correlation volume, trigger, freeze time, and matching remain
source-unauthorized.

## First proper quotient selector: WP123

- `flavor-invariant-flavon-quench-selector-audit.md`
- `checkers/wp123_invariant_flavon_quench_selector_audit.py`
- `results/wp123_invariant_flavon_quench_selector_audit.json`

WP123 adds the minimal weak-basis-invariant symmetry-breaking potential
`V_0=lambda(R^2-v^2)^2/4`. Conditional on a source-timed quench, it is the
first proper selector in this chain: it selects and stabilizes the nonzero
norm shell on the physical quotient. It does not select a flavor point. Exact
hostile minima with squared singular values `(1,0,0)` and
`(1/3,1/3,1/3)` have the same radial potential but different
`Tr(H_u^2)`. Quartic trace invariants can refine hierarchy and alignment
without chart data or a reference port, but their source coefficients and
physical realization remain unvalidated.

## Renormalizable generic-mixing no-go: WP124

- `flavor-renormalizable-flavon-mixing-no-go.md`
- `checkers/wp124_renormalizable_flavon_mixing_no_go.py`
- `results/wp124_renormalizable_flavon_mixing_no_go.json`

WP124 classifies the complete field-degree-at-most-four invariant potential
for two bifundamentals under the full weak-basis group. At fixed spectra its
only orientation-dependent generator is `Tr(H_u H_d)`. A nonzero coefficient
selects commuting permutation-aligned extrema; a zero coefficient leaves
relative orientation flat. The class can therefore select coarse norms,
spectra, and alignment extrema, but cannot select generic CKM mixing. A
rational noncommuting hostile point has exact orientation residual `-48/25`.
The result does not cover higher-dimensional operators, extra fields, reduced
symmetry, or charged spurions, and it establishes no physical instrument.

## First interior-mixing capability: WP125

- `flavor-degree-eight-mixing-selector-audit.md`
- `checkers/wp125_degree_eight_mixing_selector.py`
- `results/wp125_degree_eight_mixing_selector.json`

WP125 locates the first operator-degree escape from WP124. Through field
degree six, fixed-spectrum orientation functionals are linear in the
unistochastic matrix `|U_ij|^2`, so a global minimum always exists at a
permutation. Degree eight first admits a multi-alternating trace word and the
commutator invariant `K=||[H_u,H_d]||_F^2`. The exact conditional potential
`V=28 Tr(H_uH_d)-25 K` selects `sin^2(theta)=16/25` with positive second
variation and nonzero commutator in a two-family slice. This proves interior
mixing capability, not a numerical prediction: the angle is fixed by the
coefficient ratio, full radial stability and the remaining CKM coordinates
are unresolved, and no source or physical instrument fixes that ratio.

## Causal selector-authority window: WP126

- `flavor-selector-authority-intervention-audit.md`
- `checkers/wp126_selector_authority_intervention.py`
- `results/wp126_selector_authority_intervention.json`

WP126 transfers Strominger's partial authority-composition and intervention
law to WP125. The typed chain is `UV constructor -> EFT coefficients ->
invariant potential -> vacuum selector -> physical16 readout`; downstream
static fits cannot supply upstream authority. The selector predicts
`dx/da=1/(8q)` and `dx/dq=-a/(8q^2)`. Common coefficient scaling is an exact
null control, whereas at `(a,q)=(28,25)`, `a->a+1` moves the selected angle
coordinate by `1/200`. This is a source-response fingerprint, not yet a
physical probe: the UV constructor, matching, stable completion, controllable
intervention, and Yukawa instrument remain missing.

## Auxiliary-adjoint mediator match: WP127

- `flavor-adjoint-mediator-matching-audit.md`
- `checkers/wp127_adjoint_mediator_matching.py`
- `results/wp127_adjoint_mediator_matching.json`

WP127 introduces a Hermitian weak-basis adjoint `X` coupled to
`B=i[H_u,H_d]`. Exact elimination gives
`-g^2 ||[H_u,H_d]||_F^2/(2M^2)`, deriving the sign required by WP125 and
pulling the causal fingerprint upstream to `g` and `M^2`. The benchmark
`(M^2,g)=(2,10)` generates `q=25` exactly. The construction is nevertheless
an auxiliary EFT representation, not a renormalizable UV completion:
`Tr(XB)` has field dimension five. Without an independently sourced positive
degree-eight completion, the matched potential is also unbounded along a
noncommuting radial ray. The numerical ratio and physical instrument remain
unfixed.

## Renormalizable two-adjoint completion: WP128

- `flavor-two-adjoint-renormalizable-completion.md`
- `checkers/wp128_two_adjoint_renormalizable_completion.py`
- `results/wp128_two_adjoint_renormalizable_completion.json`

WP128 replaces WP127's dimension-five auxiliary vertex by two Hermitian
weak-basis adjoints coupled linearly to `H_u,H_d`. Their renormalizable
commutator quartic matches exactly through field degree eight to
`-lambda alpha^2 beta^2 ||[H_u,H_d]||_F^2`; a simultaneous positive radial
adjoint quartic is coercive for `rho>lambda/2`. The exact benchmark
`lambda=25,rho=13,alpha=beta=1` reproduces WP125 and removes its hostile
radial runaway at this order. This establishes a renormalizable conditional
selector architecture, not a numerical prediction: coefficients, the full
coupled vacuum, higher matching orders, RG transport, and the physical
instrument remain unauthorized.

## Rival-source kernel: WP129

- `flavor-rival-source-identification-audit.md`
- `checkers/wp129_rival_source_identification.py`
- `results/wp129_rival_source_identification.json`

WP129 performs the Deutschian hard-to-vary attack on WP128. Three inequivalent
constructors—the two-adjoint sector, the auxiliary-adjoint EFT, and a direct
contact EFT—are matched to the same `(a,q,r)` packet. Six common low-energy
coefficient, vacuum, Hessian, and intervention probes give identical response
columns: exact rank one and source-kernel dimension two. Formal threshold
spectroscopy separates the frozen rivals with full rank, but it is a new
relational experiment and has no admitted physical instrument or independently
closed port family. WP128 therefore establishes selector architecture, not UV
source identification.

## Detector-smeared threshold rank: WP130

- `flavor-detector-smeared-threshold-audit.md`
- `checkers/wp130_detector_smeared_threshold_rank.py`
- `results/wp130_detector_smeared_threshold_rank.json`

WP130 replaces WP129's formal pole labels by a predeclared conditional
spectral instrument: two absorptive energy bins plus a subtracted contact
channel. The ideal and finite-overlap (`eta=1/4`) response matrices have rank
three. Full pole-bin merging makes the two-adjoint and auxiliary-adjoint
constructors exactly equivalent, reducing rank to two; below all thresholds,
decoupling restores rank one and the full two-dimensional source kernel. Thus
threshold identification is detector-resolution-relative. The experiment
changes the relational groupoid and remains conditional: no gauge/Lorentz-
complete SM portal, accessible scale, derived widths, or calibrated detector
is established.

## Gauge-complete portal and scale obstruction: WP131

- `flavor-sm-portal-accessibility-audit.md`
- `checkers/wp131_sm_portal_accessibility.py`
- `results/wp131_sm_portal_accessibility.json`

WP131 freezes the gauge-, Lorentz-, and weak-basis-complete dimension-five
portal `bar(Q_L) H Phi_a f_R/Lambda`. Adjoint--flavon mixing then gives
source-dependent quark--Higgs pole residues and exact reduced widths. A common
flavor-sector scale dilation preserves `V_a/Lambda`, the dimensionless
low-energy flavor packet, and normalized selector coordinates while moving
all mediator thresholds and suppressing their residues. With fixed detector
reach, an exact hostile pair has two accessible poles before dilation and zero
afterward. Thus the portal exists conditionally, but threshold accessibility
requires an additional source-selected absolute scale and an implemented
calibrated instrument.

## Higgs--flavon scale-selector obstruction: WP132

- `flavor-higgs-flavon-scale-selector-audit.md`
- `checkers/wp132_higgs_flavon_scale_selector.py`
- `results/wp132_higgs_flavon_scale_selector.json`

WP132 tests the minimal classically scale-invariant Higgs--flavon portal. A
nonzero stationary branch requires `kappa^2=lambda_h lambda_f` and fixes only
the ratio `R^2/h^2=-lambda_h/kappa`; its Hessian retains one exactly flat
dilation direction. Exact stationary points `(1,1/2)` and `(100,50)` have the
same dimensionless flavor packet but thresholds differing by a factor ten.
Explicit masses or Coleman--Weinberg running can lift the direction only by
transporting dimensionful boundary data whose source remains undeclared.
Thus the portal is a conditional relative-scale selector, not an absolute-
scale selector, and detector accessibility remains undefined.

## Physical-instrument open-world closeout: WP133

- `flavor-physical-instrument-open-world-audit.md`
- `checkers/wp133_physical_instrument_open_world_audit.py`
- `results/wp133_physical_instrument_open_world_audit.json`

WP133 propagates WP131's derived reduced widths through a frozen rational
detector-uncertainty envelope. The original three-constructor response remains
rank three with determinant margin `31/40`. Enlarging the family by one
non-gauge isospectral two-adjoint constructor leaves every two-point threshold
record unchanged, producing a one-dimensional source kernel. A formal
four-point port restores rank four only on that finite enlargement and has no
implemented physical instrument. Together with WP132's scale obstruction,
this closes the requested physical-realization audit negatively: conditional
spectral identifiability is robust, but neither accessibility nor open-world
source identification is authorized.

## Dimensional-transmutation boundary gate: WP134

- `flavor-dimensional-transmutation-authority-audit.md`
- `checkers/wp134_dimensional_transmutation_authority.py`
- `results/wp134_dimensional_transmutation_authority.json`

WP134 tests whether asymptotically free dimensional transmutation supplies
WP132's missing scale. The generated `Lambda=mu exp[-1/(2bg^2(mu))]` is exactly
invariant under coherent changes of renormalization presentation, so it is a
genuine conditional scale selector. It is not source-free: a distinct
boundary packet with the same local coupling value shifts `log Lambda` by
exactly three in the hostile example. The remaining gate is therefore a
source-authorized RG trajectory and dimensionful boundary, not further RG
algebra or detector fitting.

## UV-fixed-point relevant-amplitude gate: WP135

- `flavor-uv-fixed-point-scale-authority-audit.md`
- `checkers/wp135_uv_fixed_point_scale_authority.py`
- `results/wp135_uv_fixed_point_scale_authority.json`

WP135 tests whether a UV fixed point closes WP134's boundary gate. For a
relevant eigenoperator, `Lambda=mu |delta(mu)|^(1/theta)` is exactly invariant
along one RG trajectory, but the fixed point and critical exponent do not fix
the relevant amplitude. Two trajectories approaching the same fixed point
shift `log Lambda` by one in the hostile packet; the exact fixed trajectory
has no finite crossover. A UV fixed point therefore rigidifies critical data
and may fix irrelevant couplings, but it does not select the physical flavor
scale without an independently sourced relevant-amplitude boundary and clock.

## Stochastic cosmological boundary ensemble: WP136

- `flavor-stochastic-cosmological-boundary-audit.md`
- `checkers/wp136_stochastic_cosmological_boundary.py`
- `results/wp136_stochastic_cosmological_boundary.json`

WP136 freezes a light weak-basis-singlet de Sitter spectator as an independent
source of WP135's relevant amplitude. Its quadratic equilibrium law is a
Gaussian with variance `3H^4/(8pi^2m^2)`. This replaces an unweighted
relevant-coordinate fiber by a source-generated probability measure, but does
not select a trajectory: exact normalized draws `z=1,4` have nonzero density
and crossover scales differing by two, landing in different accessibility
classes. The scale readout also collapses the sign pair unless the source
authorizes that quotient. Hubble/mass inputs, equilibration,
reheating-to-flavor matching, and a physical instrument remain unestablished.

## Reheating transfer and detector reliability: WP137

- `flavor-reheating-detector-reliability-audit.md`
- `checkers/wp137_reheating_detector_reliability.py`
- `results/wp137_reheating_detector_reliability.json`

WP137 freezes a quadratic singlet mixing channel from WP136's spectator to the
flavor relevant coordinate. An exact `3/5--4/5` rotation transports the
Gaussian injectively and gives flavor variance `16/25` of the spectator
variance. For `|w|<2`, accessibility has exact probability `erf(sqrt(2))` and
a distribution-free lower bound `3/4`. Formal four-source multi-point rank is
four only on accessible draws; the nonzero inaccessible tail has rank one and
kernel dimension three. Identification is therefore conditional and
non-uniform over the full cosmological support.

## Compact-source uniform-faithfulness condition: WP138

- `flavor-compact-source-uniform-faithfulness-audit.md`
- `checkers/wp138_compact_source_uniform_faithfulness.py`
- `results/wp138_compact_source_uniform_faithfulness.json`

WP138 replaces WP137's unbounded Gaussian coordinate by a compact uniform
source `u in [-1,1]`. With `Lambda(u)=Lambda_max sqrt(|u|)`, finite detector
reach covers the entire source domain iff `Lambda_max<=E_max`. Thus compact
support can make identification uniform in principle. It does not select the
support scale: at `E_max=1`, exact packets `Lambda_max=4/5` and `4/3` have
accessibility probabilities `1` and `9/16`. Compactness removes the necessary
tail obstruction while leaving the scale-authority and physical-instrument
gates intact.

## Boundary-to-instrument candidate closeout: WP139

- `flavor-boundary-instrument-candidate-closeout.md`
- `checkers/wp139_boundary_instrument_candidate_closeout.py`
- `results/wp139_boundary_instrument_candidate_closeout.json`

WP139 freezes four boundary candidates and replays WP134--WP138 against the
seven gates of the boundary-to-instrument objective. Zero candidates pass all
gates. RG transmutation lacks boundary authority; a UV fixed point leaves the
relevant amplitude free; Gaussian cosmological preparation has an unavoidable
finite-reach tail; compact preparation leaves its support scale unsourced; and
none has an executable open-rival multi-point instrument. The bounded
programme closes negatively with a fixed reopening condition: a predeclared
source-selected trajectory/support scale plus a physically implemented
detector convolution faithful on an enlarged non-gauge rival class.

## Flux-sector scale selector: WP140

- `flavor-flux-modulus-scale-selector-audit.md`
- `checkers/wp140_flux_modulus_scale_selector.py`
- `results/wp140_flux_modulus_scale_selector.json`

WP140 reopens WP139 with a gravitationally clocked modulus and quantized flux.
The exact source `V_n(r)=a r^2+n^2/r^2` selects a stable radius
`r_n^4=n^2/a` within each fixed sector. It does not select the sector: at
`a=1`, `n=1,4` give thresholds `1,1/2` and opposite accessibility classes for
reach `3/4`. Flux reversal also leaves a sign kernel. Quantization converts
the continuous scale ambiguity into a discrete non-singleton fiber; a sector
preparation law and executable orientation-sensitive instrument remain absent.

## Flux-sector preparation ensemble: WP141

- `flavor-flux-sector-preparation-audit.md`
- `checkers/wp141_flux_sector_preparation.py`
- `results/wp141_flux_sector_preparation.json`

WP141 supplies WP140's missing normalized sector law on the frozen set
`{+-1,+-4}` with weights `q^|n|`, `q=1/2`. Exact probabilities are
`P(+-1)=4/9` and `P(+-4)=1/18`; only `1/9` of the ensemble is threshold-
accessible at WP140's reach. Scale records retain the two flux-sign classes,
and even the zero-temperature limit leaves the lowest `+-1` orientation pair.
The route is a genuine sector-ensemble producer, not a sector-orientation
selector, and no executable topological probe is established.

## Oriented flux selector and stability gate: WP142

- `flavor-oriented-flux-selector-audit.md`
- `checkers/wp142_oriented_flux_selector.py`
- `results/wp142_oriented_flux_selector.json`

WP142 adds a CP-odd boundary `E_h(n)=2|n|-hn`. Normalizability on the full
flux lattice requires `|h|<2`; at `h=1` the zero-temperature source uniquely
selects `n=1`, removing WP141's sign degeneracy. That sector's threshold `1`
remains above reach `3/4`. A linear bias large enough to favor growing
positive flux crosses `h=2` and makes the energy unbounded below; `h=3` is the
exact hostile case. Orientation selection therefore does not imply accessible
scale selection, and no physical instrument is established.

## Convex accessible-flux selector: WP143

- `flavor-convex-flux-accessibility-selector-audit.md`
- `checkers/wp143_convex_flux_accessibility_selector.py`
- `results/wp143_convex_flux_accessibility_selector.json`

WP143 replaces WP142's unstable large-flux bias by the convex full-lattice
energy `E(n)=alpha n^2-hn`. At `(alpha,h)=(1,8)`, sector `n=4` is the unique
ground state throughout the open interval `7alpha<h<9alpha` and its threshold
`1/2` is below reach `3/4`. Stability and accessibility are therefore jointly
possible. The numerical sector remains encoded in `h/(2alpha)`: the equally
stable packet `h=2` selects inaccessible `n=1`. A microscopic source relation
for the coefficient ratio and an executable open-rival instrument remain
missing.

## Topological coefficient matching: WP144

- `flavor-topological-flux-matching-audit.md`
- `checkers/wp144_topological_flux_matching.py`
- `results/wp144_topological_flux_matching.json`

WP144 derives WP143's coefficient ratio from the frozen contract
`N=chi(X)/24`, `h=2alpha N`. For fixed `chi=96`, the unique sector is `n=4`
and its threshold is accessible; the relation is invariant under geometric
presentation changes. The equally admissible topology `chi=24` selects
inaccessible `n=1`. The continuous coefficient ambiguity is therefore
replaced by a discrete topology-class fiber. A topology-preparation law and
executable multi-point instrument remain missing.

## Topology-preparation stability: WP145

- `flavor-topology-preparation-stability-audit.md`
- `checkers/wp145_topology_preparation_stability.py`
- `results/wp145_topology_preparation_stability.json`

WP145 extends WP144 from two hand-picked geometries to the full positive
topology lattice `k=chi/24>=1`. The normalized linear topology action gives a
geometric law; at `q=1/2`, `P(k=1)=1/2`, `P(k=4)=1/16`, and the accessible
tail `k>=2` has probability `1/2`. Its zero-temperature limit selects the
minimal inaccessible topology. Reversing the ordering to favor large topology
requires `q>1` and makes the sum divergent. The construction is therefore a
normalized topology ensemble, not a point selector; a nonlinear source action
and an executable physical instrument remain missing.

## Topology entropy-normalization boundary: WP146

- `flavor-topology-entropy-normalization-audit.md`
- `checkers/wp146_topology_entropy_normalization.py`
- `results/wp146_topology_entropy_normalization.json`

WP146 adds exact Catalan topology multiplicities to WP145's linear source
action. Throughout the full normalization range `q<=1/4`, successive sector
weights decrease, so the modal topology remains the minimal inaccessible
`k=1`. At the critical boundary, `P(1)=1/2`, `P(4)=5/128`, the accessible tail
has probability `1/2`, and the mean topology diverges. For `q>1/4` the
partition sum diverges. Combinatorial entropy therefore produces no accessible
point selector before control of the source law is lost.

## Topology congruence selector: WP147

- `flavor-topology-congruence-selector-audit.md`
- `checkers/wp147_topology_congruence_selector.py`
- `results/wp147_topology_congruence_selector.json`

WP147 tests a structural admissibility route. Conditional on the congruence
`k=0 mod 4`, the allowed topology domain is `{4,8,12,...}`, every member is
threshold-accessible, and the inherited `q=1/2` law gives `P(k=4)=15/16`; its
zero-temperature limit selects `k=4`. This is a genuine proper-subspace
selector if the modulus is independently source-derived. The congruence form
alone supplies no such authority: the equally formed `m=1` projector selects
inaccessible `k=1`. The frontier is therefore an actual anomaly/index/tadpole
derivation of the modulus, followed by the still-missing physical instrument.

## Free-action topology selector: WP148

- `flavor-free-action-topology-selector-audit.md`
- `checkers/wp148_free_action_topology_selector.py`
- `results/wp148_free_action_topology_selector.json`

WP148 derives WP147's modulus condition from a genuine topological mechanism.
A free order-96 action gives `chi(X)=96 chi(X/G)` and hence
`k=chi(X)/24=4 chi(X/G)`, selecting the proper domain `k in 4N`; the minimal
positive quotient class gives accessible `k=4`. The theorem is conditional in
two independently hostile ways: a free order-24 action gives inaccessible
`k=1`, while an order-96 action with a stabilizer-four orbit can give `k=5` and
break divisibility. The remaining source gates are therefore the physical
derivation of the group order, anomaly freedom, and freeness over the complete
admitted deformation family; the instrument gate is still separate.

## Natural flavor-group freeness obstruction: WP149

- `flavor-group-freeness-obstruction-audit.md`
- `checkers/wp149_flavor_group_freeness_obstruction.py`
- `results/wp149_flavor_group_freeness_obstruction.json`

WP149 derives the number 96 from the natural three-generation presentation
grammar `((Z2)^3 semidirect S3) x CP`, but its canonical linear action is not
free. Transpositions fix generation-collision loci, sign flips fix coordinate
hyperplanes, and CP fixes the real locus. A generic complex point has trivial
stabilizer, yet generic freeness does not authorize WP148's global covering
formula. The order-96 count therefore supplies presentation symmetry, not the
required topology selector. Reopening requires a source-derived free
realization or a complete fixed-point correction that independently preserves
the modulus-four conclusion.

## Fixed-point Euler correction: WP150

- `flavor-fixed-point-euler-correction-audit.md`
- `checkers/wp150_fixed_point_euler_correction.py`
- `results/wp150_fixed_point_euler_correction.json`

WP150 replaces WP148's inapplicable covering formula by Burnside's corrected
identity `k=4 chi(X/G)-F/24`, where `F` is the sum of nonidentity fixed-set
Euler characteristics. Integral packets split into four classes indexed by
`F/24 mod 4`, spanning every residue of `k mod 4`. At quotient Euler one,
`F=24` gives `k=3` and `F=72` restores inaccessible `k=1`. Modulus-four
selection survives exactly when `F=0 mod 96`; freeness is sufficient but not
necessary. The natural order-96 grammar is therefore only a rigidifier unless
an equivariant source identity forces this total correction residue.

## Conjugacy-divisibility obstruction: WP151

- `flavor-conjugacy-divisibility-obstruction-audit.md`
- `checkers/wp151_conjugacy_divisibility_obstruction.py`
- `results/wp151_conjugacy_divisibility_obstruction.json`

WP151 exactly enumerates the natural order-96 group's 20 conjugacy classes.
Its center has order four, producing three nonidentity singleton classes, so
the gcd of nonidentity class sizes is one. Conjugacy invariance therefore
forces no useful divisibility of WP150's fixed-point sum `F`. A class-invariant
value 24 on the singleton CP class already gives `F=24` and `k=3` at quotient
Euler one. The remaining route must constrain fixed-set Euler *values* through
an independently derived equivariant index, anomaly identity, or pairing
theorem; group organization alone is only a rigidifier.

## Central fixed-sector pairing obstruction: WP152

- `flavor-central-pairing-obstruction-audit.md`
- `checkers/wp152_central_pairing_obstruction.py`
- `results/wp152_central_pairing_obstruction.json`

WP152 tests pairwise supersymmetric/index cancellation on WP151's three
central nonidentity sectors. Every involution of this odd three-element set
has a fixed sector. Values `+24,-24` cancel on the exchanged pair while the
fixed sector can retain `+24`, leaving `F=24` and `k=3`. Pairing organization
therefore cannot force the modulus-four selector. A successor must derive a
vanishing theorem for the residual sector or a simultaneous three-sector
index identity whose coefficient lattice forces `F=0 mod 96`.

## Trivial-representation amplitude obstruction: WP153

- `flavor-trivial-representation-amplitude-audit.md`
- `checkers/wp153_trivial_representation_amplitude.py`
- `results/wp153_trivial_representation_amplitude.json`

WP153 decomposes the three central fixed-set values into a two-dimensional
difference sector and a one-dimensional trivial amplitude. Permutation
coherence has rank two and aligns the values, but cyclic averaging preserves
their sum. The symmetric packet `f=(1,1,1)` gives `F=72` and inaccessible
`k=1`. Thus three-sector symmetry is a rigidifier, not a selector. A successor
must independently derive the amplitude constraint `sum(f)=0 mod 4`; adding
that symmetric equation without a source derivation would simply restate the
desired fixed-point law.

## Faithful Z4 anomaly selector: WP154

- `flavor-faithful-z4-anomaly-selector-audit.md`
- `checkers/wp154_faithful_z4_anomaly_selector.py`
- `results/wp154_faithful_z4_anomaly_selector.json`

WP154 finds the first progressive selector kernel in the topology branch.
Every permutation-invariant linear `Z4` character is `A_c=c sum(f)`. Requiring
faithfulness restricts `c` to the units `1,3`, whose kernels coincide exactly
with `sum(f)=0 mod 4`. This selects 16 of 64 residue packets and, combined with
WP153 alignment, forces the diagonal amplitude to vanish modulo four,
restoring `F=0 mod 96`. Dropping faithfulness admits `c=2`, doubles the kernel,
and accepts a hostile aligned packet. Promotion now requires an independently
derived gauge-complete `Z4` charge assignment and anomaly polynomial, RG
preservation, and a decision whether the consistency gate has any physical
instrument.

## Anomaly spectator kernel: WP155

- `flavor-anomaly-spectator-kernel-audit.md`
- `checkers/wp155_anomaly_spectator_kernel.py`
- `results/wp155_anomaly_spectator_kernel.json`

WP155 opens WP154's UV completion domain by adding one unresolved spectator or
counterterm residue `s in Z4`. The faithful total constraint
`sum(f)+s=0 mod 4` has exactly one completion for every flavor packet, so its
anomaly-free 64-element graph projects onto all 64 flavor residues. WP154's
16-packet flavor selector therefore exists only on the frozen `s=0` slice; an
even-spectator grammar leaves an intermediate 32-packet image. The smallest
hostile repair is `f=(1,1,1),s=1`, which restores the inaccessible branch.
Promotion requires a gauge-complete spectrum that independently forbids net
spectator residue or a typed threshold instrument that retains spectator
source attribution.

## Massive spectator residue: WP156

- `flavor-massive-spectator-residue-audit.md`
- `checkers/wp156_massive_spectator_residue.py`
- `results/wp156_massive_spectator_residue.json`

WP156 asks whether symmetry-preserving spectator masses close WP155's open
completion domain. Dirac pairs always have residue zero and recover WP154's
16-packet kernel. A charge-two Majorana block also has an invariant mass but
contributes residue two, so general massive completions generate `{0,2}` and
leave a 32-packet flavor image. The exact hostile packet is a charge-two
Majorana spectator paired with `f=(2,2,2)`. Massiveness therefore does not
imply selector closure; an independently conserved fermion number or complete
anomaly theorem forbidding/quotienting the Majorana residue is still required.

## U(1)-parent Majorana obstruction: WP157

- `flavor-u1-parent-majorana-obstruction-audit.md`
- `checkers/wp157_u1_parent_majorana_obstruction.py`
- `results/wp157_u1_parent_majorana_obstruction.json`

WP157 embeds the candidate `Z4` in a gauged `U(1)` broken by a charge-four
scalar. A charge-two Weyl spectator admits the renormalizable invariant
`Phi^dagger N N` because `-4+2+2=0`; after Higgsing it becomes precisely
WP156's residue-two Majorana block. The continuous parent therefore
UV-completes rather than forbids the obstruction. Keeping `U(1)` unbroken
changes the source experiment, while setting the Yukawa to zero without a
protecting rule is not selection. A successor needs an additional anomaly-
consistent gauge or representation constraint that forbids this operator.

## Minimal Z3 Dirac protector: WP158

- `flavor-minimal-z3-dirac-protector-audit.md`
- `checkers/wp158_minimal_z3_dirac_protector.py`
- `results/wp158_minimal_z3_dirac_protector.json`

WP158 constructs the smallest cyclic representation protector for WP157's
Majorana obstruction. `Z2` cannot forbid a same-field bilinear; auxiliary
`Z3` charges `N:(2,1), Nbar:(2,2)` under `Z4 x Z3` forbid both Majorana blocks
while allowing a zero-residue Dirac mass. Combined with WP154, this restores
the 16-packet selector on the declared spectrum. The construction changes the
source groupoid and remains conditional: the `Z3` origin, complete anomaly
packet, exactness under RG/gravity, and physical instrument are unproved.

## Rival protector identification: WP159

- `flavor-rival-protector-identification-audit.md`
- `checkers/wp159_rival_protector_identification.py`
- `results/wp159_rival_protector_identification.json`

WP159 performs the Deutschian rival-constructor attack on WP158. Protectors
`Z3`, `Z5`, `Z7`, and continuous `U(1)_F` give identical six-record low-energy
columns: exact rank one and source-kernel dimension three. All implement the
same conditional 16-packet selector, so minimality does not identify the `Z3`
source. A formal order/holonomy moment tower has rank four on the frozen rivals,
but it is a new relational experiment with no defect preparation or physical
instrument. The next gate is a finite-energy, resolution-typed protector probe
faithful on an enlarged rival grammar.

## Finite-winding defect probe: WP160

- `flavor-finite-winding-defect-probe-audit.md`
- `checkers/wp160_finite_winding_defect_probe.py`
- `results/wp160_finite_winding_defect_probe.json`

WP160 replaces WP159's arbitrary formal moments by normalized defect-holonomy
return records. Through winding six, `Z7` and generic `U(1)_F` remain
equivalent and the rank is three. At winding seven the ideal tower has rank
four and is jointly faithful on the frozen rivals; seven is exactly minimal.
The normalization port is load-bearing. This is a new relational experiment,
not an improved flavor readout, and remains uninstrumented: defect existence,
finite tension, controlled winding, reach, decoherence, resolution, and
nonprimitive/rational-holonomy hostile rivals remain open.

## Rational-holonomy aliasing: WP161

- `flavor-rational-holonomy-aliasing-audit.md`
- `checkers/wp161_rational_holonomy_aliasing.py`
- `results/wp161_rational_holonomy_aliasing.json`

WP161 enlarges WP160's continuous rivals to rational `U(1)` holonomies of
orders 3, 5, and 7. Each has exactly the same complete return tower as the
corresponding discrete protector. The seven-source response has rank four and
kernel dimension three even through winding 105; the equality is rule-level,
not a truncation artifact. Return probes identify holonomy order, not ambient
protector type. A complementary source-derived probe must access defect-sector
inventory, continuous holonomy deformations, or continuous-constructor
thresholds, with an actual physical instrument.

## Holonomy tangent complement: WP162

- `flavor-holonomy-tangent-complement-audit.md`
- `checkers/wp162_holonomy_tangent_complement.py`
- `results/wp162_holonomy_tangent_complement.json`

WP162 adds local holonomy deformability to WP161's return tower. One binary
tangent record separates all seven point alternatives, but raises response
rank only from four to five, leaving a two-dimensional source-mixture kernel.
The mixed tower `(D,nD,n^2D)` raises ranks successively `5,6,7` and is jointly
faithful on the frozen coefficient packet. This distinguishes point separation
from mixture faithfulness. The complement remains formal: finite-energy gauge
actuation, defect stability, susceptibility resolution, and detector
convolution are still required before algebraic span becomes executable
control.

## Tangent-actuator accessibility: WP163

- `flavor-tangent-actuator-accessibility-audit.md`
- `checkers/wp163_tangent_actuator_accessibility.py`
- `results/wp163_tangent_actuator_accessibility.json`

WP163 types WP162's tangent complement through an on-shell actuator with
`M<E_max=1`. Uniform masses `1/2` retain rank seven; a partial packet has rank
six; a common dilation to mass `2` leaves all flavor and return records
unchanged while collapsing operational rank to four and restoring the
three-dimensional alias kernel. Joint faithfulness is therefore restricted to
an accessible source domain. A source-selected gauge scale, defect tension,
width, actuator efficiency, and detector resolution remain missing.

## Virtual-susceptibility resolution: WP164

- `flavor-virtual-susceptibility-resolution-audit.md`
- `checkers/wp164_virtual_susceptibility_resolution.py`
- `results/wp164_virtual_susceptibility_resolution.json`

WP164 replaces WP163's on-shell gate by virtual response
`chi=g^2/M^2`. Formal rank remains seven at every finite benchmark mass. With
detector sensitivity `delta=1/4`, however, a common dilation from mass `1` to
`3` suppresses `chi` from `1` to `1/9`; detector rank falls from seven to four
while formal rank stays seven. A partial packet has rank six. Nonzero algebraic
response therefore does not establish operational faithfulness. A physical
apparatus must derive a uniform sensitivity bound or the protector scale.

## Finite decoupling-probe uniform no-go: WP165

- `flavor-finite-decoupling-probe-no-go.md`
- `checkers/wp165_finite_decoupling_probe_no_go.py`
- `results/wp165_finite_decoupling_probe_no_go.json`

WP165 promotes WP163--WP164's scale examples to a theorem: any finite probe
family bounded by `C_j/M^p_j` with positive powers and fixed positive detector
thresholds becomes jointly unresolved at sufficiently large mass. The exact
three-probe witness first becomes blind at integer mass 11 despite all formal
responses remaining nonzero. Return-order probes avoid decoupling but remain
source-nonfaithful by WP161; tangent probes separate sources but are not
uniformly detectable. Reopening requires a compact source scale, a
nondecoupling complementary observable, a uniform-margin instrument, or an
authorized adaptive resource law.

## Two-holonomy closure probe: WP166

- `flavor-two-holonomy-closure-probe-audit.md`
- `checkers/wp166_two_holonomy_closure_probe.py`
- `results/wp166_two_holonomy_closure_probe.json`

WP166 tests a nondecoupling complement to WP161. Rational second ports remain
inside the same order-`n` cyclic subgroup and do not separate `Zn` from `U(1)`.
If the continuous source independently supplies an irrational holonomy, the
generated closure becomes infinite; the mixed closure tower `(C,nC,n^2C)`
raises rank from four to seven. This evades WP165 algebraically but is wholly
relative to source-authorized ports. Importing an arbitrary ambient `U(1)`
element is not executable control. A finite closure-testing instrument,
stopping rule, and error/resource bound remain absent.

## Bounded closure-certification no-go: WP167

- `flavor-bounded-closure-certification-no-go.md`
- `checkers/wp167_bounded_closure_certification_no_go.py`
- `results/wp167_bounded_closure_certification_no_go.json`

WP167 proves that WP166's infinite-closure rescue cannot be certified by any
bounded relation/fusion protocol uniformly over unbounded finite rivals. For
word-depth `L`, the relation language of `Z^2` agrees with `(Z/(L+1)Z)^2`
through all tested words. At `L=7`, the exact hostile finite rival has order
`64`; `+e1^8` is the first distinguishing relation, while `(Z/7Z)^2` is
already distinguished at depth seven. Thus finite closure testing can at most
rigidify the two-port presentation unless the source supplies an a priori
bound on finite rivals or a separately typed nonlocal instrument.

## Exponent-bound closure certificate: WP168

- `flavor-exponent-bound-closure-certificate.md`
- `checkers/wp168_exponent_bound_closure_certificate.py`
- `results/wp168_exponent_bound_closure_certificate.json`

WP168 proves the exact positive boundary of WP167. If the source independently
supplies a finite exponent cap `E`, then exhaustive relation/fusion testing
through depth `E` separates `Z^2` from every two-port finite abelian rival with
generator periods at most `E`. The bound is sharp: `(Z/EZ)^2` matches `Z^2`
through depth `E-1` and first separates at `+e1^E`. For the audited value
`E=8`, all `49` rivals with `2 <= n1,n2 <= 8` are separated at depth eight.
This is a conditional selector only if the exponent cap is source-derived;
otherwise WP167 still governs and the finite relation test is only a
rigidifier.

## Adaptive relation-depth lower bound: WP169

- `flavor-adaptive-relation-depth-lower-bound.md`
- `checkers/wp169_adaptive_relation_depth_lower_bound.py`
- `results/wp169_adaptive_relation_depth_lower_bound.json`

WP169 proves that WP168's depth requirement is a resource lower bound, not an
artifact of exhaustive testing. Any adaptive relation/fusion protocol whose
maximum queried word length is below the source exponent cap `E` receives
identical transcripts from `Z^2` and `(Z/EZ)^2`. For `E=8`, even the complete
under-depth language of `21845` words cannot separate the hostile pair; the
first separator is the single depth-eight query `+e1^8`. Adaptive scheduling
therefore cannot replace a source-derived cap and an executable depth-`E`
instrument.

## Closure-order oracle gate: WP170

- `flavor-closure-order-oracle-gate.md`
- `checkers/wp170_closure_order_oracle_gate.py`
- `results/wp170_closure_order_oracle_gate.json`

WP170 types the nonlocal escape left open by WP167-WP169. An exact closure
order or exponent readout separates `Z^2` from every finite two-port closure
in one shot, but this is a new oracle-like probe family, not a bounded
relation/fusion instrument. It also does not fully identify finite source
stories: `(2,6)` and `(3,4)` share order `12`, while `(2,6)` and `(3,6)` share
exponent `6`. The oracle is therefore a formal finite-versus-infinite
selector only after a physical closure-order, return-volume, or recurrence
growth instrument is independently derived; otherwise WP167-WP169 still govern.

## Finite growth-window no-go: WP171

- `flavor-finite-growth-window-no-go.md`
- `checkers/wp171_finite_growth_window_no_go.py`
- `results/wp171_finite_growth_window_no_go.json`

WP171 audits recurrence growth as a candidate physicalization of WP170's
closure-order oracle. A finite radius-`R` Cayley-ball growth probe is still
fooled by the finite torus `(Z/(2R+1)Z)^2`: its local growth agrees with `Z^2`
through radius `R`. At the audited radius `R=3`, both have growth
`1,5,13,25`; the first difference appears only at radius four. Therefore a
finite recurrence-growth window is only a presentation rigidifier unless the
source supplies a finite-size bound that the instrument radius exceeds, or an
actually unbounded recurrence observable is physically admitted.

## Growth-bound certificate: WP172

- `flavor-growth-bound-certificate.md`
- `checkers/wp172_growth_bound_certificate.py`
- `results/wp172_growth_bound_certificate.json`

WP172 proves the positive recurrence-growth boundary for square finite tori.
If the source supplies a period bound `B` on rivals `(Z/NZ)^2`, then growth
through radius `ceil(B/2)` separates every finite rival with `N <= B` from
`Z^2`, and the radius is sharp. For `B=8`, `(Z/8Z)^2` still matches `Z^2`
through radius three, then differs at radius four with growth `39` instead of
`41`. This is a conditional finite-versus-infinite selector only when the
period bound and the recurrence instrument are source-derived.

## Order-bound growth certificate: WP173

- `flavor-order-bound-growth-certificate.md`
- `checkers/wp173_order_bound_growth_certificate.py`
- `results/wp173_order_bound_growth_certificate.json`

WP173 weakens WP172's source datum from a period cap to a total finite-order
cap `K` on rectangular rivals `(Z/n1Z) x (Z/n2Z)`. The least recurrence-growth
certificate radius is the least `R` with `(2R+1)^2 > K`. For `K=64`, radius
four separates all finite rivals with `n1 n2 <= 64`, while radius three is
fooled by `(Z/7Z)^2` of order `49`. This gives a more plausible conditional
finite-versus-infinite selector if flavor source dynamics supplies a finite
closure-volume bound; otherwise WP171 remains the governing no-go.

## Growth-resolution margin: WP174

- `flavor-growth-resolution-margin.md`
- `checkers/wp174_growth_resolution_margin.py`
- `results/wp174_growth_resolution_margin.json`

WP174 adds detector resolution to WP173. With source order cap `K=64`, the
noiseless recurrence certificate at radius four has minimum finite deficit
only `2`, attained by `(Z/7Z)x(Z/9Z)`, `(Z/8Z)^2`, and `(Z/9Z)x(Z/7Z)`.
If the absolute count error is `tau=1`, strict interval separation fails at
radius four because robust selection requires `d_min(R) > 2 tau`. Radius five
is the first robust radius, with minimum deficit `10`. Thus a physical
recurrence-growth selector must declare not only a source order cap and
executable radius, but also a calibrated count-resolution margin.

## Skew quotient growth correction: WP175

- `flavor-skew-quotient-growth-correction.md`
- `checkers/wp175_skew_quotient_growth_correction.py`
- `results/wp175_skew_quotient_growth_correction.json`

WP175 removes WP173's rectangular-product restriction. For arbitrary finite
index-lattice quotients `Z^2/L` with index at most `64`, skew HNF quotients
`(a,b,d)=(10,4,6)` and `(10,5,6)` have shortest `l1` relation length `10`,
match `Z^2` through growth radius four, and first separate at radius five.
Thus the order-bound recurrence selector is domain-relative: radius four is
valid for rectangular product rivals, but the full finite-quotient domain at
the same order cap requires radius five, and the WP174 detector margin must be
recomputed on that enlarged domain.

## HNF growth-resolution margin: WP176

- `flavor-hnf-growth-resolution-margin.md`
- `checkers/wp176_hnf_growth_resolution_margin.py`
- `results/wp176_hnf_growth_resolution_margin.json`

WP176 recomputes detector resolution on WP175's arbitrary finite-quotient
domain. At order cap `K=64`, the corrected noiseless radius five has minimum
growth deficit only `1`, uniquely at HNF `(10,5,6)` of index `60`, so an
absolute count error `tau=1` breaks robust interval separation. Radius six is
the first robust radius, with minimum deficit `21`. The current domain-relative
table is: rectangular exact `R=4`, rectangular `tau=1` `R=5`, arbitrary HNF
exact `R=5`, arbitrary HNF `tau=1` `R=6`.

## Growth certificate compiler: WP177

- `flavor-growth-certificate-compiler.md`
- `checkers/wp177_growth_certificate_compiler.py`
- `results/wp177_growth_certificate_compiler.json`

WP177 turns WP173-WP176 into a reusable exact admission gate. Given a source
order cap `K`, legal quotient domain, and absolute count error `tau`, the
checker compiles the first recurrence radius `R` with
`min_finite(growth_Z2(R)-growth_finite(R)) > 2 tau`. Across `4 <= K <= 64`, the
compiled radii are monotone and reproduce the corrected `K=64` table:
rectangular exact `4`, rectangular `tau=1` `5`, arbitrary HNF exact `5`, and
arbitrary HNF `tau=1` `6`. This is not a new selector; it is the gate preventing
radius and detector-margin portability errors.

## Growth selector authority gate: WP178

- `flavor-growth-selector-authority-gate.md`
- `checkers/wp178_growth_selector_authority_gate.py`
- `results/wp178_growth_selector_authority_gate.json`

WP178 separates WP177's formal compilability from selector authority. A
recurrence-growth readout becomes a conditional physical selector only when
four independent fields are authorized before readout: source order cap `K`,
legal quotient-domain law, calibrated count error `tau`, and an instrument
that executes at least the compiled radius. The checker enumerates all `16`
authorization patterns and admits exactly one. Missing `K` restores WP171;
missing domain restores WP175; missing `tau` restores WP174/WP176; missing
execution leaves a formal gate with no physical instrument.

## Constructor rigidity gate: WP179

- `flavor-constructor-rigidity-gate.md`
- `checkers/wp179_constructor_rigidity_gate.py`
- `results/wp179_constructor_rigidity_gate.json`

WP179 states Deutsch's audit exactly. WP177-WP178 make recurrence growth a
formal admission gate, but an explanation requires one source constructor to
entail `K`, quotient-domain law, detector error `tau`, and executable radius as
a hard-to-vary package. At `K=64`, multiple consistent packages exist:
rectangular exact radius `4`, HNF exact radius `5`, and HNF `tau=1` radius `6`.
Therefore the next falsifier is constructor-level: find two sources with the
same low-energy flavor packet but different authorized gate tuples, or prove a
source law tying the tuple together.

## Rival constructor gate kernel: WP180

- `flavor-rival-constructor-gate-kernel.md`
- `checkers/wp180_rival_constructor_gate_kernel.py`
- `results/wp180_rival_constructor_gate_kernel.json`

WP180 supplies WP179's hostile constructor pair. `C_rect_exact` and
`C_hnf_noisy` are frozen to the same `physical16` and measured-ten low-energy
flavor packet, but authorize different recurrence-growth gate tuples:
rectangular exact `K=64,R=4` versus arbitrary-HNF noisy `K=64,tau=1,R=6`.
Both tuples are formally consistent by WP177. Thus the low-energy flavor packet
does not uniquely explain the recurrence-growth gate; the gate is a
constructor-sensitive discriminator, not a low-energy-derived source
explanation.

## Constructor discrimination protocol: WP181

- `flavor-constructor-discrimination-protocol.md`
- `checkers/wp181_constructor_discrimination_protocol.py`
- `results/wp181_constructor_discrimination_protocol.json`

WP181 turns WP180's rival gate tuples into an instrument comparison. A
radius-four exact rectangular probe tests `C_rect_exact` but not
`C_hnf_noisy`; an exact HNF radius-five probe still fails the noisy HNF
constructor because WP176 requires radius six at `tau=1`; and a noisy HNF
radius-six channel tests the noisy constructor but not the exact-count
rectangular commitment. The smallest common comparison is a vector instrument
with both exact and `tau=1` HNF radius-six channels. Thus recurrence growth
breaks the constructor kernel only as a typed constructor-discrimination
experiment, not by a single weaker readout.

## Channel degradation authority: WP182

- `flavor-channel-degradation-authority.md`
- `checkers/wp182_channel_degradation_authority.py`
- `results/wp182_channel_degradation_authority.json`

WP182 tests whether WP181's exact-plus-noisy vector instrument can compress to
a single exact HNF radius-six channel. It can only if an exact-to-`tau=1`
degradation map is independently authorized. Without that map, exact HNF
radius six tests the exact rectangular constructor but not the noisy HNF
constructor, while the WP181 vector channel tests both. The direction is not
symmetric: a noisy channel cannot test an exact-count commitment. Thus
degradation is an additional physical instrument operation, not automatic
authority inherited from finer formal data.

## Compressed instrument authority: WP183

- `flavor-compressed-instrument-authority.md`
- `checkers/wp183_compressed_instrument_authority.py`
- `results/wp183_compressed_instrument_authority.json`

WP183 folds WP182's degradation map into the authority table. With the four
base fields from WP178 authorized but no degradation map, the recurrence probe
is a vector-channel selector: both exact and noisy channels must be present.
Only when the degradation map is also authorized does a single exact channel
compress the noisy contract. The checker enumerates all `32` five-field
authorization patterns and admits exactly one compressed single-channel
selector pattern. The degradation map does not replace `K`, domain, `tau`, or
executable radius.

## Recurrence-growth decision table: WP184

- `flavor-recurrence-growth-decision-table.md`
- `checkers/wp184_recurrence_growth_decision_table.py`
- `results/wp184_recurrence_growth_decision_table.json`

WP184 closes the recurrence-growth branch with a compact admission table. It
lists nine selector overclaims, their missing authority gates, smallest exact
falsifiers, and admissible weaker claims. The branch has not produced an
unconditional flavor selector. It has produced a typed constructor-
discrimination gate:
`source K + source quotient-domain law + calibrated tau + executable compiled
radius + optional degradation -> vector or compressed recurrence selector`.
The next frontier is a source constructor law tying that tuple together before
low-energy flavor readout.

## Constructor-law template audit: WP185

- `flavor-constructor-law-template-audit.md`
- `checkers/wp185_constructor_law_template_audit.py`
- `results/wp185_constructor_law_template_audit.json`

WP185 begins the constructor-law frontier. A finite source state-space
dimension can explain an order cap `K`, and an abelian two-port law can explain
part of the quotient-domain typing, but the source-only template does not
derive detector error `tau`, executable recurrence radius, degradation, or a
complete quotient-shape restriction. Thus finite state space plus two-port
closure is insufficient for a Deutsch-Popperian recurrence selector; a stronger
source action or an independently admitted instrument law is still needed.

## Rectangular domain source law: WP186

- `flavor-rectangular-domain-source-law.md`
- `checkers/wp186_rectangular_domain_source_law.py`
- `results/wp186_rectangular_domain_source_law.json`

WP186 attacks WP185's quotient-shape gap. In HNF coordinates `(a,0),(b,d)`,
independent port reset symmetries are exactly the condition `b=0`, hence force
the rectangular quotient domain. The WP175 skew hostiles `(10,4,6)` and
`(10,5,6)` are excluded only under that source law; if coupled port relations
are legal, the arbitrary HNF domain returns. This supplies a conditional source
law for rectangular radii, not a result derivable from recurrence growth.

## Coupled-port rival source: WP187

- `flavor-coupled-port-rival-source.md`
- `checkers/wp187_coupled_port_rival_source.py`
- `results/wp187_coupled_port_rival_source.json`

WP187 supplies the rival to WP186. `S_independent_ports` and `S_coupled_ports`
share the same `physical16`, measured-ten packet, and order cap `K=64`, but
authorize different port laws and hence different recurrence gates:
rectangular exact/tau-one radii `4/5` versus arbitrary-HNF radii `5/6`. The
WP175 skew hostile `(10,4,6)` is illegal under independent resets but legal
under coupled port relations. Thus quotient-domain law is source-
discriminating and cannot be imposed as notation after low-energy fitting.

## Port-law discrimination: WP188

- `flavor-port-law-discrimination.md`
- `checkers/wp188_port_law_discrimination.py`
- `results/wp188_port_law_discrimination.json`

WP188 asks which recurrence observations distinguish the WP187 port laws.
Rectangular radius-four success tests only the independent-port commitment and
does not choose the port law. HNF radius four is still under-depth for the
coupled source because skew quotients match through that radius. The smallest
exact port-law discriminator is HNF recurrence growth through radius five with
skew quotients included; with `tau=1`, the corresponding discriminator is HNF
radius six.

## Coupled source kernel: WP189

- `flavor-coupled-source-kernel.md`
- `checkers/wp189_coupled_source_kernel.py`
- `results/wp189_coupled_source_kernel.json`

WP189 prevents overreading WP188. HNF recurrence growth discriminates
independent versus coupled port law, but it does not identify the coupled
source origin. A local-constraint coupled source and a mediator-elimination
coupled source can share the same low-energy flavor packet, HNF quotient
domain, order cap `K=64`, and recurrence radii `5/6`. Thus the port-law
discriminator still leaves a coupled-source kernel; finite fiber is not
singleton fiber.

## Coupled origin intervention probe: WP190

- `flavor-coupled-origin-intervention-probe.md`
- `checkers/wp190_coupled_origin_intervention_probe.py`
- `results/wp190_coupled_origin_intervention_probe.json`

WP190 supplies the first origin-sensitive probe inside WP189's coupled-source
kernel. A local hard-constraint origin has no legal continuous weakening
parameter, while a mediator-elimination origin has an `epsilon` coupling:
nonzero `epsilon` preserves the coupled HNF gate, and `epsilon=0` restores
independent rectangular ports. Static recurrence growth still collapses the
origins; only a source-authorized controlled `epsilon` intervention separates
them.

## Frozen mediator intervention kernel: WP191

- `flavor-frozen-mediator-intervention-kernel.md`
- `checkers/wp191_frozen_mediator_intervention_kernel.py`
- `results/wp191_frozen_mediator_intervention_kernel.json`

WP191 adds the hostile intervention-family case. WP190 separates local
constraint from mediator elimination only if the authorized `epsilon` controls
reach zero. A frozen nonzero mediator with accessible `epsilon` values away
from zero has the same observable recurrence-gate trace as a local hard
constraint: only HNF `5/6`. A zero-accessible mediator additionally reaches the
rectangular `4/5` gate. Thus origin discrimination is relative to the admitted
control range, not merely to the existence of a formal mediator parameter.

## Mediator threshold origin probe: WP192

- `flavor-mediator-threshold-origin-probe.md`
- `checkers/wp192_mediator_threshold_origin_probe.py`
- `results/wp192_mediator_threshold_origin_probe.json`

WP192 tests an alternative to WP191's zero-coupling intervention. A resolved
mediator-threshold channel separates local hard constraints from mediator
origins: local constraints have no threshold, while frozen and zero-accessible
mediators share a threshold at energy `5`. A below-threshold unresolved window
does not separate them, and the threshold vector still collapses mediator
subtypes. Thus threshold spectroscopy is a conditional mediator-origin probe
only if the threshold channel, coverage, and resolution are independently typed.

## Combined origin-probe rank: WP193

- `flavor-combined-origin-probe-rank.md`
- `checkers/wp193_combined_origin_probe_rank.py`
- `results/wp193_combined_origin_probe_rank.json`

WP193 combines WP190's `epsilon` response with WP192's threshold vector on the
frozen three-origin domain: local hard constraint, frozen nonzero mediator, and
zero-accessible mediator. Threshold alone collapses the mediator subtypes;
epsilon response alone collapses local constraint with frozen mediator. The
joint pair `(threshold_vector, epsilon_trace)` is discrete on this small
domain. This is a progressive but bounded joint-faithfulness result, conditional
on both physical channels being independently admitted.

## Open-world origin rival: WP194

- `flavor-open-world-origin-rival.md`
- `checkers/wp194_open_world_origin_rival.py`
- `results/wp194_open_world_origin_rival.json`

WP194 stress-tests WP193 under domain expansion. Adding a fourth origin,
`composite_hidden_mediator`, with the same threshold vector and `epsilon` trace
as the frozen nonzero mediator restores a source kernel. The WP193 joint probe
remains faithful on its frozen three-origin class, but not on the expanded
open-world class. Thus joint faithfulness is domain-relative; source
identification requires a closed origin domain or an additional probe for the
new rival.

## Threshold multiplicity probe: WP195

- `flavor-threshold-multiplicity-probe.md`
- `checkers/wp195_threshold_multiplicity_probe.py`
- `results/wp195_threshold_multiplicity_probe.json`

WP195 adds the missing probe for WP194's composite hidden mediator. Binary
threshold detection plus `epsilon` response still collides frozen and composite
mediators, but resolved threshold multiplicity separates them: multiplicity
`1` versus `2` at the same threshold energy. On the four-origin domain, the
pair `(threshold_multiplicity, epsilon_trace)` is discrete. This is conditional
on a physical multiplicity-resolving threshold instrument; binary threshold
detection does not authorize that stronger readout.

## Multiplicity resolution margin: WP196

- `flavor-multiplicity-resolution-margin.md`
- `checkers/wp196_multiplicity_resolution_margin.py`
- `results/wp196_multiplicity_resolution_margin.json`

WP196 adds detector resolution to WP195. The frozen/composite multiplicity gap
is `1`, so robust interval separation with absolute multiplicity error `mu`
requires `mu < 1/2`. At `mu=1/2`, touching intervals transitively merge local,
frozen, and composite origins; at `mu=1/3`, the four-origin partition remains
discrete. Thus
threshold multiplicity is a conditional probe only with a calibrated
multiplicity-resolution margin.

## Multiplicity smearing gate: WP197

- `flavor-multiplicity-smearing-gate.md`
- `checkers/wp197_multiplicity_smearing_gate.py`
- `results/wp197_multiplicity_smearing_gate.json`

WP197 decomposes WP196's multiplicity error into finite-width and background
components. The `1` versus `2` multiplicity distinction survives only when
`width + background < 1/2`. Exact audited cases show a sharp detector
(`1/10+1/10=1/5`) remains faithful, the borderline case
(`1/4+1/4=1/2`) fails by touching intervals, and a smeared case
(`1/3+1/4=7/12`) fails. Thus multiplicity-based source identification requires
a source-derived or independently admitted detector model bounding both terms.

## Minimal constructor-law candidate: WP198

- `flavor-minimal-constructor-law-candidate.md`
- `checkers/wp198_minimal_constructor_law_candidate.py`
- `results/wp198_minimal_constructor_law_candidate.json`

WP198 proposes and audits the first compact constructor-law candidate:
`finite two-port mediator lattice`. Finite internal state space supplies
`K=64`; coupled mediator port relations supply the coupled/HNF domain and a
formal `epsilon` channel; two mediator species supply threshold and
multiplicity probes. This ties the source-side tuple together, but it still
fails the physical selector gate because no width bound, background bound, or
executable recurrence-radius/actuator law is derived. The next attack is
detector and actuator derivation.

## Detector margin from lattice: WP199

- `flavor-detector-margin-from-lattice.md`
- `checkers/wp199_detector_margin_from_lattice.py`
- `results/wp199_detector_margin_from_lattice.json`

WP199 attacks WP198's detector gap. The finite mediator lattice supplies
multiplicity spacing, but spacing alone does not bound detector width or
background. The exact margin rule is `width + background < spacing/2`; for
unit spacing this is WP197's `width + background < 1/2`. A sharp detector
contract passes, while borderline and smeared contracts fail. The source-only
lattice has no margin proof, so detector law remains an independent physical
gate.

## Actuator radius from lattice: WP200

- `flavor-actuator-radius-from-lattice.md`
- `checkers/wp200_actuator_radius_from_lattice.py`
- `results/wp200_actuator_radius_from_lattice.json`

WP200 attacks WP198's actuator gap. The finite mediator lattice with `K=64` and
HNF domain determines required radii, but not executable control: HNF exact
recurrence needs radius `5`, and HNF `tau=1` needs radius `6`. Source-only has
no actuator radius; radius `4` supports neither HNF gate; radius `5` supports
exact only; radius `6` supports the noisy HNF gate. Thus algebraic span/domain
typing does not produce an actuator law.

## Source-instrument closure: WP201

- `flavor-source-instrument-closure.md`
- `checkers/wp201_source_instrument_closure.py`
- `results/wp201_source_instrument_closure.json`

WP201 combines WP198's finite two-port mediator-lattice source law with
explicit instrument-law candidates. Only the sharp radius-six instrument closes
the conditional selector gate: `width=1/10`, `background=1/10`, so
`width+background=1/5<1/2`, and actuator radius `6` supports the HNF `tau=1`
gate. A borderline detector with `width+background=1/2` fails, and a sharp
radius-five actuator fails the noisy HNF gate. This is the strongest current
positive result, but it is source+instrument conditional, not source-only.

## Instrument-law rival kernel: WP202

- `flavor-instrument-law-rival-kernel.md`
- `checkers/wp202_instrument_law_rival_kernel.py`
- `results/wp202_instrument_law_rival_kernel.json`

WP202 stress-tests WP201's Deutsch caveat. The same finite two-port
mediator-lattice source can be paired with rival instrument laws:
`I_sharp_radius6` passes detector and actuator gates, `I_borderline_radius6`
fails detector only, and `I_sharp_radius5` fails actuator only. Only the sharp
radius-six law authorizes the selector. Therefore WP201's closure is real but
not hard-to-vary source explanation unless that instrument law is derived from
the constructor or independently admitted as part of the physical experiment.

## Constructor-coupled instrument law: WP203

- `flavor-constructor-coupled-instrument-law.md`
- `checkers/wp203_constructor_coupled_instrument_law.py`
- `results/wp203_constructor_coupled_instrument_law.json`

WP203 tests the stronger candidate demanded by WP202: a
`self_reading_finite_two_port_mediator_lattice` that entails both the
source-side tuple and the sharp radius-six instrument law. Within the frozen toy
domain it blocks the WP202 rival-instrument variations: the borderline detector
and weak actuator are incompatible with the constructor law, while
`width+background=1/5<1/2` and radius `6` close the selector gate. This is the
first hard-to-vary candidate in the branch, but it is still a candidate, not a
physical derivation of the self-reading law.

## Self-reading law variation: WP204

- `flavor-self-reading-law-variation.md`
- `checkers/wp204_self_reading_law_variation.py`
- `results/wp204_self_reading_law_variation.json`

WP204 attacks WP203's self-reading declaration. The same source-side tuple
`K=64`, HNF domain, and epsilon/threshold/multiplicity probes admits multiple
instrument-law variants: sharp radius `6`, sharp radius `7`, sharper radius
`6`, and borderline radius `6`. Three pass and the borderline detector fails,
but all share the same source-side tuple. Thus WP203's constants are hard to
vary only after being frozen; a real explanation must derive the detector and
actuator constants, not merely declare them.

## Minimal instrument optimality: WP205

- `flavor-minimal-instrument-optimality.md`
- `checkers/wp205_minimal_instrument_optimality.py`
- `results/wp205_minimal_instrument_optimality.json`

WP205 tests whether a minimal-instrument optimality principle derives WP203's
self-reading constants. Minimal actuator radius does motivate radius `6`, since
radius `5` is insufficient and radius `7` is not minimal. But a simple
sharpness-cost principle selects a near-margin detector rather than the
`width=background=1/10` constants; the borderline detector still fails by
touching the strict margin. Thus WP204 is only partially closed: actuator
radius can be motivated, detector constants require a separate dynamics or cost
law.

## Detector safety-margin selector: WP206

- `flavor-detector-safety-margin-selector.md`
- `checkers/wp206_detector_safety_margin_selector.py`
- `results/wp206_detector_safety_margin_selector.json`

WP206 conditionally derives WP203's detector constants by adding a safety cap
`width+background <= 1/5` and then minimizing sharpness cost among safe
radius-six detectors. The near-margin detector fails the cap, the WP203
`1/10,1/10` detector passes exactly, and a sharper `1/20,1/20` detector passes
but costs more. Thus the one-tenth constants are selected only if the `1/5`
safety cap is itself source- or detector-authorized.

## Five-readout safety cap: WP207

- `flavor-five-readout-safety-cap.md`
- `checkers/wp207_five_readout_safety_cap.py`
- `results/wp207_five_readout_safety_cap.json`

WP207 conditionally derives WP206's `1/5` safety cap from a detector redundancy
law: five equal readout subchannels with at most one bad subchannel. Hostile
controls show four copies with one bad gives `1/4`, and five copies with two
bad gives `2/5`, both too large. Thus the safety cap is explained only if the
five-copy/one-bad readout architecture is itself source- or detector-authorized.

## Minimal five-copy readout: WP208

- `flavor-minimal-five-copy-readout.md`
- `checkers/wp208_minimal_five_copy_readout.py`
- `results/wp208_minimal_five_copy_readout.json`

WP208 conditionally explains the five-copy count. If the detector must tolerate
one bad subchannel with strict margin below `1/4`, then four copies fail by
touching exactly `1/4`, while five copies pass with `1/5`; five is also the
least copy count satisfying the WP207 declared cap `bad/copies <= 1/5`. Six
copies pass but are not minimal. The remaining gate is to derive the one-bad
tolerance and strict below-`1/4` target.

## One-bad strict target audit: WP209

- `flavor-one-bad-strict-target-audit.md`
- `checkers/wp209_one_bad_strict_target_audit.py`
- `results/wp209_one_bad_strict_target_audit.json`

WP209 reduces WP208's assumptions. Minimal nonzero fault tolerance motivates
one bad subchannel, and strict interval separation rejects touching at `1/4`.
The exact copy counts are: one-bad non-strict `1/4` target needs four copies,
one-bad strict `1/4` target needs five, and two-bad strict needs nine. Thus the
five-copy law is explained by a one-bad strict contract, but the physical
one-bad fault model and the `1/4` target remain to be derived.

## Quarter target factorization: WP210

- `flavor-quarter-target-factorization.md`
- `checkers/wp210_quarter_target_factorization.py`
- `results/wp210_quarter_target_factorization.json`

WP210 reduces WP209's `1/4` target. Adjacent multiplicity gap `1` plus
half-gap interval separation gives `1/2`; reserving half of that budget for
fault/readout uncertainty yields `1/4`. Hostile alternatives show no reserve
would give `1/2`, while a three-way reserve gives `1/6`. Thus the quarter
target is reduced to a half-reserve law, which remains the next detector
authority gate.

## Half-reserve symmetry: WP211

- `flavor-half-reserve-symmetry.md`
- `checkers/wp211_half_reserve_symmetry.py`
- `results/wp211_half_reserve_symmetry.json`

WP211 conditionally derives the half-reserve law. In a two-bucket model splitting
the interval half-gap `1/2` between intrinsic detector smearing and
fault/readout reserve, exchange symmetry forces the equal split `1/4+1/4`.
Asymmetric splits such as `1/3+1/6` also sum to the half-gap but are not
exchange-invariant. Thus the `1/4` target is explained only if the detector
architecture supplies a two-bucket exchange symmetry.

## Asymmetric bucket falsifier: WP212

- `flavor-asymmetric-bucket-falsifier.md`
- `checkers/wp212_asymmetric_bucket_falsifier.py`
- `results/wp212_asymmetric_bucket_falsifier.json`

WP212 corrects a possible overread of WP211. The half-gap budget `1/2` permits
asymmetric detector/fault splits such as `1/3+1/6` and `1/6+1/3`; they preserve
the total budget but break exchange symmetry. Also, splitting the detector
bucket evenly does not derive WP203's `1/10,1/10` constants: the symmetric
bucket gives `1/8,1/8`, while asymmetric buckets give `1/6,1/6` or
`1/12,1/12`. Thus two-bucket symmetry can explain the quarter target, but the
actual detector constants still require another law.

## Five-copy width-background split: WP213

- `flavor-five-copy-width-background-split.md`
- `checkers/wp213_five_copy_width_background_split.py`
- `results/wp213_five_copy_width_background_split.json`

WP213 resolves WP212's detector-constant gap by using the direct five-copy cap.
The WP207 safety cap is `width+background <= 1/5`; exchange symmetry between
width and background selects `width=background=1/10`. Asymmetric splits such as
`3/20+1/20` obey the cap but violate exchange symmetry, while `1/5+1/5` is
exchange-invariant but exceeds the cap. Thus WP203's one-tenth constants are
conditionally derived from the five-copy cap plus width/background exchange
symmetry.

## Detector derivation chain: WP214

- `flavor-detector-derivation-chain.md`
- `checkers/wp214_detector_derivation_chain.py`
- `results/wp214_detector_derivation_chain.json`

WP214 closes the detector-constant arithmetic by recording the dependency
chain. The one-tenth constants follow conditionally from: minimal nonzero fault
tolerance -> one-bad contract; strict below-quarter target; five-copy
minimality -> one-fifth safety cap; and width/background exchange symmetry.
The remaining external gates are exactly three: minimal nonzero fault
tolerance, strict below-quarter target, and width/background exchange symmetry.
Thus the detector constants are no longer arbitrary, but they remain
architecture-conditional.

## Symmetric detector architecture: WP215

- `flavor-symmetric-detector-architecture.md`
- `checkers/wp215_symmetric_detector_architecture.py`
- `results/wp215_symmetric_detector_architecture.json`

WP215 supplies a compact detector-architecture candidate for WP214's three
remaining gates: a strict interval comparator, a single-fault sentinel, and
exchangeable width/background channels. Together these entail the strict
below-quarter target, minimal nonzero fault tolerance, and width/background
exchange symmetry. Each hostile one-feature omission leaves exactly one gate
open. This conditionally closes the detector-architecture chain, but physical
realization of the three features remains unproved.

## Detector physical-realization gate: WP216

- `flavor-detector-physical-realization-gate.md`
- `checkers/wp216_detector_physical_realization_gate.py`
- `results/wp216_detector_physical_realization_gate.json`

WP216 prevents overclaiming from WP215. The detector architecture becomes a
physical instrument only after three additional realization fields are supplied:
executable operation, calibrated error contract, and source coupling/descent.
Hostile variants with any one missing field fail admission. Thus the WP215
architecture remains a conditional scaffold until a real flavor experiment or
source-derived construction realizes the full detector tuple.

## Existing-observation detector audit: WP217

- `flavor-existing-observation-detector-audit.md`
- `checkers/wp217_existing_observation_detector_audit.py`
- `results/wp217_existing_observation_detector_audit.json`

WP217 tests whether currently admitted flavor observations already realize the
WP216 detector tuple. They do not. The measured-ten family is a calibrated,
executable low-energy readout, but it lacks the strict interval comparator,
single-fault sentinel, exchangeable width/background channels, and
source-coupling/descent field. The `physical16` coordinate remains the faithful
coordinate for source claims, but coordinates are not instruments. Existing
observations therefore do not supply selector authority.

## Successor experiment route matrix: WP218

- `flavor-successor-experiment-route-matrix.md`
- `checkers/wp218_successor_experiment_route_matrix.py`
- `results/wp218_successor_experiment_route_matrix.json`

WP218 classifies the possible successor routes after WP217. Threshold
spectroscopy is executable/calibrated but still needs a declared source
coupling/descent law. Controlled epsilon intervention has source typing and
calibration but still needs executable control. A reference port can be typed
only as a new relational stabilizer-groupoid experiment, not as a selector on
the original `physical16` quotient. The route with the right original-selector
shape is source-derived detector dynamics, but it remains a type target rather
than a constructed law.

## Source detector dynamics audit: WP219

- `flavor-source-detector-dynamics-audit.md`
- `checkers/wp219_source_detector_dynamics_audit.py`
- `results/wp219_source_detector_dynamics_audit.json`

WP219 audits the strongest WP218 route. A genuine source detector law must
independently entail both the WP215 detector features and the WP216 realization
fields. Renaming the detector architecture as a source law fails. A source
action without detector outputs fails. A source action with detector outputs
but no calibrated error contract fails. Only a full source-detector dynamics
law would admit selector authority, and no such concrete law is constructed in
this packet.

## Two-port source detector entailment: WP220

- `flavor-two-port-source-detector-entailment.md`
- `checkers/wp220_two_port_source_detector_entailment.py`
- `results/wp220_two_port_source_detector_entailment.json`

WP220 tests whether the finite two-port mediator-lattice source already supplies
the WP219 detector dynamics. It does not. The source entails order cap, HNF
domain, coupled port law, formal epsilon, threshold, multiplicity, and source
coupling/descent. It does not entail the strict interval comparator,
single-fault sentinel, exchangeable width/background channels, executable
operation, or calibrated error contract. The self-reading law covers those
fields only by declaration, and WP204 remains the hostile same-source variant
falsifier.

## Missing detector-field ladder: WP221

- `flavor-missing-detector-field-ladder.md`
- `checkers/wp221_missing_detector_field_ladder.py`
- `results/wp221_missing_detector_field_ladder.json`

WP221 ranks the five WP220 missing detector fields. The smallest constructive
targets are structural: strict interval comparator is one strict-boundary rule
short, and exchangeable width/background channels are one channel-exchange
action short. The single-fault sentinel requires a fault model; executable
operation requires apparatus; calibrated error contract requires width,
background, and drift bounds. Thus the next exact move should derive a
structural detector rule rather than claim the full instrument.

## Strict boundary from robustness: WP222

- `flavor-strict-boundary-robustness.md`
- `checkers/wp222_strict_boundary_robustness.py`
- `results/wp222_strict_boundary_robustness.json`

WP222 conditionally derives the strict-boundary rule from robust discrimination.
If detector acceptance must survive a positive perturbation margin, touching at
the target has zero margin and must be rejected. Thus robust acceptance is
exactly strict acceptance `error < target`; for target `1/4`, `1/5` passes,
`1/4` fails by touching, and `1/3` fails by overshoot. This closes one
structural detector rule only conditional on admitting robustness as a
source/detector requirement.

## Channel-exchange action gate: WP223

- `flavor-channel-exchange-action-gate.md`
- `checkers/wp223_channel_exchange_action_gate.py`
- `results/wp223_channel_exchange_action_gate.json`

WP223 tests whether two detector error channels entail width/background
exchange symmetry. They do not. The split `3/20+1/20` satisfies the one-fifth
safety cap but is not exchange-invariant. Equal split follows only if an actual
exchange action is admitted. Thus the remaining structural authority gate is a
source automorphism or detector dynamics that swaps width and background
channels.

## Source automorphism exchange test: WP224

- `flavor-source-automorphism-exchange-test.md`
- `checkers/wp224_source_automorphism_exchange_test.py`
- `results/wp224_source_automorphism_exchange_test.json`

WP224 types the missing exchange authority. A width/background swap derives
exchange symmetry only if it swaps the channels, commutes with the source law,
preserves error semantics, and descends to the detector quotient. Label swapping
alone fails; a source symmetry with wrong error semantics fails; and a semantic
detector swap that is not a source symmetry fails. The next gate is to construct
this automorphism from the finite two-port source or leave exchange as external.

## Two-port automorphism semantics: WP225

- `flavor-two-port-automorphism-semantics.md`
- `checkers/wp225_two_port_automorphism_semantics.py`
- `results/wp225_two_port_automorphism_semantics.json`

WP225 tests the finite two-port source against the WP224 automorphism
requirements. Mediator-species and port-label swaps may commute with the source
law, but they act on source labels, not detector-error semantics. They neither
swap width/background nor descend to the detector quotient. Therefore the
finite two-port source does not derive width/background exchange; a coupled
source-detector action is required.

## Coupled source-detector action gate: WP226

- `flavor-coupled-source-detector-action-gate.md`
- `checkers/wp226_coupled_source_detector_action_gate.py`
- `results/wp226_coupled_source_detector_action_gate.json`

WP226 tests the coupled-action repair to WP225. A formal coupled action needs a
source action, detector error bundle, coupling term, exchange automorphism, and
descent to the detector quotient. Even that is only formal unless the source
action uniquely entails the coupling. If the same source admits rival detector
couplings, one exchange-symmetric and one asymmetric, exchange remains an
appended detector law rather than a source-derived structural rule.

## Coupling uniqueness principles: WP227

- `flavor-coupling-uniqueness-principles.md`
- `checkers/wp227_coupling_uniqueness_principles.py`
- `results/wp227_coupling_uniqueness_principles.json`

WP227 reduces coupling uniqueness to a typed source-law target. The one-fifth
cap alone admits width-heavy, equal, and background-heavy couplings. External
exchange symmetry selects the equal split but has no source authority. A
source-derived symmetric strictly convex cost is the minimal principle that
would make the equal coupling unique: symmetry makes it stationary, strict
convexity makes it unique, and source derivation supplies authority.

## Convex cost source authority: WP228

- `flavor-convex-cost-source-authority.md`
- `checkers/wp228_convex_cost_source_authority.py`
- `results/wp228_convex_cost_source_authority.json`

WP228 audits candidate detector-coupling costs. Convexity alone is insufficient:
an arbitrary asymmetric quadratic can select a wrong rival. External symmetric
quadratic selects `1/10+1/10` but has no source authority. A source-derived
symmetric flat cost has authority and symmetry but no uniqueness. The admitted
type is exactly a source-derived symmetric strictly convex cost minimized at
the equal split.

## Source metric to detector cost: WP229

- `flavor-source-metric-to-detector-cost.md`
- `checkers/wp229_source_metric_to_detector_cost.py`
- `results/wp229_source_metric_to_detector_cost.json`

WP229 tests whether an equal quadratic metric on the two-port source supplies
the WP228 detector cost. It does not automatically do so. A source metric must
descend through a detector-coordinate map, with a proved pullback identity,
positive definiteness on detector errors, and width/background symmetry. Without
that descent, the metric lives on mediator variables while width/background
remain detector-error semantics.

## Detector-coordinate map kernel: WP230

- `flavor-detector-coordinate-map-kernel.md`
- `checkers/wp230_detector_coordinate_map_kernel.py`
- `results/wp230_detector_coordinate_map_kernel.json`

WP230 shows the kernel inside the source-metric route. The same equal two-port
source metric admits rival detector-coordinate maps: symmetric `1/10+1/10`,
width-heavy `3/20+1/20`, and background-heavy `1/20+3/20`. A formal pullback
identity does not repair authority unless the coordinate map itself is
source-derived. Thus the detector cost remains coordinate-gauge data until the
map from source variables to detector-error coordinates is derived.

## Coordinate-map observability gate: WP231

- `flavor-coordinate-map-observability-gate.md`
- `checkers/wp231_coordinate_map_observability_gate.py`
- `results/wp231_coordinate_map_observability_gate.json`

WP231 states the observability gate for deriving the detector-coordinate map.
The source must generate calibrated probes with full rank on the
two-dimensional width/background error space. A total-error-only probe has rank
one and leaves a one-dimensional kernel. Untyped rank-two responses lack
calibration, and external rank-two calibration lacks source authority. Only a
source-derived calibrated two-error probe identifies the map.

## Current sources two-error probe audit: WP232

- `flavor-current-sources-two-error-probe-audit.md`
- `checkers/wp232_current_sources_two_error_probe_audit.py`
- `results/wp232_current_sources_two_error_probe_audit.json`

WP232 audits current flavor source/probe families against WP231. No currently
admitted family supplies a source-derived calibrated rank-two width/background
response. SM one-loop RG is source-derived transport but not a detector-error
probe. The `physical16` experimental algebra is calibrated readout but not
source-derived detector response. Nine-link textures and perturbations are
presentation data/tests. Thus the coordinate-map branch needs a new experiment
or should be closed negative.

## `P_det` interface-constructor gate: WP233

- `flavor-pdet-interface-constructor-gate.md`
- `checkers/wp233_pdet_interface_constructor_gate.py`
- `results/wp233_pdet_interface_constructor_gate.json`

WP233 names the missing common-frame constructor. A source-derived RG object
and calibrated `physical16` readout do not define a probe merely because their
coordinates appear compatible. Admission requires a physical `P_det` from the
source-error module to the detector-response module, with experimental units,
a common frame, source-born variations, uncertainty/support contract, and a
robust rank-two Jacobian. Mapping two independent source directions to the
same response gives the smallest falsifier: rank one and zero Gram determinant.
Without `P_det`, WP232 is a source-support closure rather than a missing
algebraic step.

## Executable `P_det` calibration protocol: WP234

- `flavor-executable-pdet-calibration-protocol.md`
- `contracts/flavor-pdet-calibration-record.v1.json`
- `checkers/wp234_executable_pdet_calibration.py`
- `results/wp234_executable_pdet_calibration.json`

WP234 constructs an executable calibration intake for a frozen two-direction
experiment: zero-accessible mediator coupling plus resolved threshold scan,
with joint finite-width/background response in one frame. Exact interval-corner
tests enforce uncertainty-stable rank two. The bundled record is deliberately
synthetic and is rejected as experimental evidence because run provenance,
signed frame/metric calibration, and physical support models are absent. The
protocol is executable; empirical instrument admission remains open.

## CMS `P_det` response calibration: WP235

- `flavor-cms-pdet-response-calibration.md`
- `data/cms-open-data-700/MuRun2010B.csv`
- `data/cms-open-data-700/provenance.json`
- `checkers/wp235_cms_pdet_response_model.py`
- `results/wp235_cms_pdet_response_model.json`

WP235 imports checksum-verified CMS Run2010B dimuon data and binds it to the
CMS-MUO-10-004 momentum calibration. A preregistered even/odd event split
calibrates and evaluates a finite-width Voigt signal, positive exponential
background, Gaussian detector resolution, and two-state mixing/decoupling
model. The calibration-fold likelihood Hessian supplies a positive-definite
detector metric. This closes the empirical detector-model fields left by WP234
but not its source-intervention field: the observed CMS run does not vary two
counterfactual mediator directions and therefore supplies no source selector.

## Spectral-component `P_det` audit: WP236

- `flavor-source-identifying-pdet.md`
- `checkers/wp236_source_identifying_pdet.py`
- `results/wp236_source_identifying_pdet.json`

WP236 constructs a component-identifying detector map on the frozen spectral
domain `{Z pole, smooth continuum}`. The two columns
of the calibrated 40-bin response Jacobian are linearly independent and have a
positive Gram determinant; held-out CMS data identify nonnegative component
yields. Coincident templates give the exact hostile rank-one kernel. The map
descends under weak-basis transformations because it uses invariant-mass
records, but its empirical continuum column lacks microscopic source authority
and it is not a `physical16` selector. Transfer to the WP192 mediator
requires a source-derived nonzero spectral residue or executable epsilon
control.

## Trace-adjoint muon portal: WP237

- `flavor-trace-adjoint-muon-portal.md`
- `checkers/wp237_trace_adjoint_muon_portal.py`
- `results/wp237_trace_adjoint_muon_portal.json`

WP237 repairs the final-state mismatch between WP131's quark--Higgs portal and
WP235's dimuon detector by adding renormalizable, gauge- and weak-basis-
invariant trace-adjoint Higgs portals. Higgs mixing then generates physical
dimuon residues, providing a named source-to-detector interface. Uniform
source identification still fails at the exact zero-coupling locus and when
the unselected absolute masses are coincident or outside detector support.
The next gate is source selection of nonzero residues and accessible distinct
poles followed by the calibrated multi-pole rank test.

## Production–acceptance kernel: WP238

- `flavor-production-acceptance-kernel.md`
- `checkers/wp238_production_acceptance_kernel.py`
- `results/wp238_production_acceptance_kernel.json`

WP238 factors the WP237-to-WP235 composition and locates its first nonfaithful
arrow. Accepted yield is the product of portal residue, production, branching,
acceptance, efficiency, and luminosity. Distinct residue/acceptance pairs can
therefore generate identical spectra; effective-yield rank is not microscopic
source rank. CMS Open Data record 718 supplies a validated Standard Model
Drell–Yan AODSIM route, but a trace-adjoint portal signal sample and its common
selection response remain required.

## Scalar-dimuon acceptance calibration: WP239

- `flavor-scalar-dimuon-acceptance-calibration.md`
- `data/cms-open-data-43611/provenance.json`
- `checkers/wp239_scalar_dimuon_acceptance.py`
- `results/wp239_scalar_dimuon_acceptance.json`

WP239 imports all 4,600 checksum-verified events of CMS Open Data record 43611
and freezes a generator-matched reconstructed dimuon selection. The physical
MSSM `bbH` scalar topology has combined acceptance×efficiency `1371/4600`, with
stable per-file values and an empirically measured reconstructed-parent mass
response. This closes the acceptance factor for that source-labelled topology,
not for WP237 automatically. A validated production-topology reweighting or
new trace-adjoint signal sample and its production/branching normalization are
still required before microscopic source rank can be claimed.

## Physical source-presence `P_det`: WP240

- `flavor-physical-source-presence-pdet.md`
- `data/cms-open-data-31305/provenance.json`
- `checkers/wp240_physical_source_presence_pdet.py`
- `results/wp240_physical_source_presence_pdet.json`

WP240 combines WP239's generator-labelled scalar response with a checksum-
verified and muon-certified 2016 DoubleMuon collision shard. After a smooth
background nuisance is frozen from sidebands, the scalar/background response
has rank two and positive Gram determinant; coincident templates give the
rank-one hostile kernel. The observed shard fits zero scalar yield, so it
contains no evidence for the source. This is nevertheless a physical source-
presence identifier on the declared MSSM domain. It is not yet a WP128 or
`physical16` selector; trace-adjoint production/branching transfer remains.

## Topology-transfer gate: WP241

- `flavor-topology-transfer-gate.md`
- `checkers/wp241_topology_transfer_gate.py`
- `results/wp241_topology_transfer_gate.json`

WP241 tests whether WP240's executable CMS MSSM scalar response can be reused
as a trace-adjoint source identifier. The official construction fixes MSSM
`bbH` production and forces dimuon decay; WP237 fixes neither a matched
production law nor physical cross section, branching ratio, mass, and width.
Shape and yield transport are rejected. The exact hostile pair
`(sigma,A)=(2,1/4)` and `(1,1/2)` has identical accepted yield and exposes the
rank-one normalization arrow. WP240 remains a physical MSSM source-presence
instrument; trace-adjoint identification awaits a source-authorized sample or
validated reweighting in the common frame.

## Two-source physical `P_det`: WP242

- `flavor-two-source-physical-pdet.md`
- `data/cms-open-data-43651/provenance.json`
- `checkers/wp242_two_source_physical_pdet.py`
- `results/wp242_two_source_physical_pdet.json`

WP242 adds an independently generated CMS `MA=150, tan beta=20` signal column
to WP239's `MA=130` response and executes both against the certified WP240
DoubleMuon instrument. The two signal templates plus independently frozen
smooth background have rank three and positive Gram determinant. Replacing the
second signal by the first lowers rank to two. This is a source-identifying
physical detector map on the finite labelled MSSM mass-source domain. It is
not a `physical16` selector or trace-adjoint identifier; WP241's production and
branching transfer gate remains active.

## Trace-adjoint source-rate `P_det`: WP243

- `flavor-trace-adjoint-rate-pdet.md`
- `data/lhchxswg-yr4/provenance.json`
- `checkers/wp243_trace_adjoint_rate_pdet.py`
- `results/wp243_trace_adjoint_rate_pdet.json`

WP243 composes WP237's Higgs-mixing law, WP242's two independently simulated
detector columns, and checksum-pinned LHC Higgs Cross Section Working Group YR4
production and partial-width tables. On the frozen two-pole, CP-even,
universal-mixing, no-exotic-decay domain, the selected spectrum per inverse
femtobarn has a rank-two Jacobian in `(kappa_A_squared,kappa_D_squared)` and a
positive Gram determinant that survives the declared cross-section lower
normalization. This is an asymptotically source-parameter-injective calibrated
rate map. WP245 rejects finite-2016 identification. Portal signs, rival scalar
grammars, source selection of absolute poles/couplings, and `physical16`
selection remain outside its authority.

## Physical rival-source `P_det`: WP244

- `flavor-physical-rival-source-pdet.md`
- `checkers/wp244_physical_rival_source_pdet.py`
- `results/wp244_physical_rival_source_pdet.json`

WP244 composes the formerly formal WP129 threshold-support test with the
calibrated WP242/WP243 detector ports. On the frozen rival domain with compulsory
nonzero accessible distinct residues, two adjoints, one auxiliary, and direct
contact have distinct support signatures `(1,1)`, `(1,0)`, and `(0,0)`. This
is an asymptotic source-grammar partition, not a finite-exposure identifier.
At `kappa_D=0`, the two-adjoint and one-auxiliary sources collide exactly.

## Finite-exposure source-identification audit: WP245

- `flavor-finite-exposure-source-id-audit.md`
- `data/cms-luminosity-2016/provenance.json`
- `checkers/wp245_finite_exposure_source_id_audit.py`
- `results/wp245_finite_exposure_source_id_audit.json`

WP245 applies the official certified 2016 recorded luminosity to WP243's rate
columns. Even at maximal scalar mixing and zero background, the two sources
produce at most `0.717` and `0.127` selected events, giving only a `6.09%`
chance to observe both poles. Thus WP243/WP244 are asymptotically injective but
not operational source identifiers at 2016 exposure. The weaker source needs
at least `858.6 fb^-1` for a 95% chance of one selected event, before any
background-aware discrimination requirement.

## Tau-channel feasibility gate: WP246

- `flavor-tau-channel-feasibility-gate.md`
- `data/cms-tau-channel-catalog/provenance.json`
- `checkers/wp246_tau_channel_feasibility_gate.py`
- `results/wp246_tau_channel_feasibility_gate.json`

WP246 screens the source-derived tau-pair channel before importing large CMS
MiniAOD samples. Its branching enhancement makes the weaker pole count-feasible
if calibrated acceptance exceeds roughly `2.5%` for one-event probability or
`8.3%` for ten expected events at full 2016 exposure. Available 2015 catalogue
points at 130, 140, and 160 GeV bracket both actual poles, but do not share the
common 2016 frame or establish reconstructed-response interpolation. The tau
branch remains promising but unadmitted pending interpolation closure, tau
reconstruction, backgrounds, and a finite-power rank test.

## Tau MiniAOD execution boundary: WP247

- `flavor-tau-miniaod-execution-boundary.md`
- `data/cms-open-data-19459-pilot/provenance.json`
- `checkers/wp247_tau_miniaod_execution_boundary.py`
- `results/wp247_tau_miniaod_execution_boundary.json`

WP247 imports a checksum-verified 316.9-MB, 14,688-event pilot from the
140-GeV tau sample. Split reconstructed-tau kinematics and charge are readable,
but the required `pat::Tau` ID payload uses unsupported memberwise
`vector<pair<string,float>>` serialization; generic ROOT also lacks the CMSSW
dictionaries. Generating only the nested STL dictionary does not repair it:
the first nonempty event returns an impossible `14757395258967575620` ID
elements for one tau, larger than the entire file in bytes. A kinematics-only
acceptance and a detached-leaf proxy are rejected. The tau repair now has
a precise execution gate. File-local `MakeProject` metadata generate 299
dependent classes but fail compilation at a `reco::CaloJet` class/namespace
collision, producing no dictionary. The admitted successors are compatible
CMSSW 7.6 processing, an official flat derivation retaining tau IDs, triggers,
MET, and generator matching, or a generated dictionary validated against
official CMSSW readback.

## Tau streamer offline-ID gate: WP248

- `flavor-tau-streamer-offline-id-gate.md`
- `checkers/wp248_tau_streamer_offline_id_gate.py`
- `results/wp248_tau_streamer_offline_id_gate.json`

WP248 repairs the generated dictionary's layout-neutral `reco::CaloJet`
declaration collision and reads the full `pat::Tau` wrapper. All 17,352 taus
in the complete pilot share one 98-ID schema. A frozen four-ID conjunction
leaves at least two selected taus in exactly `811/14688` events (`5.52%`),
above WP246's weaker-pole one-event screen but below its ten-event screen.
This supersedes WP247's offline-ID execution closure. Official CMSSW layout
validation, triggers, mass-grid closure, backgrounds, and finite-power rank
remain open, so no complete detector acceptance or source identifier is
claimed.

## Tau trigger-calibrated pilot: WP249

- `flavor-tau-trigger-calibrated-pilot.md`
- `checkers/wp249_tau_trigger_calibrated_pilot.py`
- `results/wp249_tau_trigger_calibrated_pilot.json`

WP249 decodes the source-local CMSSW `@trigger_paths` menu, joins it exactly to
the event `psetid_`, and intersects two named double-medium-tau paths with
WP248's frozen offline selection. Only `142/14688` events pass (`0.967%`),
below WP246's `2.49%` weaker-pole one-event screen. Trigger-object matching can
only reduce this count. The frozen double-hadronic-tau route therefore closes
negative before backgrounds; a different channel or selection must be frozen
independently rather than tuned after this failure.

## Muon–tau trigger pilot: WP250

- `flavor-mu-tau-trigger-pilot.md`
- `checkers/wp250_mu_tau_trigger_pilot.py`
- `results/wp250_mu_tau_trigger_pilot.json`

WP250 preregisters the semileptonic `mu + tau_h` branch before counting. The
three source-local isolated-muon-plus-loose-tau20 paths, intersected with one
frozen offline-ID tau, retain `414/14688` events (`2.819%`). This clears
WP246's weaker-pole one-event screen, but only by 48 events: retaining 365 or
fewer after trigger-object matching and offline-muon typing falsifies the
branch. Backgrounds, mass-grid closure, common-era calibration, and rank remain
open; no source identification is claimed.

## Muon–tau object-match gate: WP251

- `flavor-mu-tau-object-match.md`
- `checkers/wp251_mu_tau_object_match.py`
- `results/wp251_mu_tau_object_match.json`

WP251 spends WP250's object-typing budget using same-path last-filter trigger
objects, PF offline muons, frozen-ID offline taus, and geometric matching. It
retains `389/14688` events (`2.648%`), losing 25 of WP250's 414 and leaving a
23-event margin above the exact minimum. Retaining 365 or fewer under later
typing falsifies the branch. Backgrounds, mass-grid closure, common-era
calibration, and rank remain open.

## Muon–tau background pilots: WP252

- `flavor-mu-tau-background-pilots.md`
- `data/cms-mu-tau-background-pilots/provenance.json`
- `checkers/wp252_mu_tau_background_pilots.py`
- `results/wp252_mu_tau_background_pilots.json`

WP252 freezes DY, top, and W+jets before yield inspection and streams their
smallest official 2015 MiniAODv2 files through XRootD. WP251 selects 1/899 DY,
38/9600 top, and 0/809 W events. Signed normalization gives nonzero DY and top
support that overwhelms the unit-mixing weaker signal rate by about five orders
of magnitude. The W zero is censored and QCD remains a data-driven gate.
Rate-only source identification is therefore falsified; weighted shapes,
uncertainties, and rank/power remain open.

## Muon–tau visible-mass shape: WP253

- `flavor-mu-tau-visible-mass-shape.md`
- `checkers/wp253_mu_tau_visible_mass_shape.py`
- `results/wp253_mu_tau_visible_mass_shape.json`

WP253 freezes a six-bin visible `mu + tau_h` mass probe. The 140-GeV signal
template `[11,199,159,20,0,0]` and combined simulated-background template
`[11,19,2,1,3,3]` have exact rank two, while summing the bins has rank one.
The shape therefore restores signal/background information erased by rate.
This remains a finite pilot: QCD, weighted full shapes, uncertainties, 130/160
signal columns, and two-source rank/power remain open.

## Muon–tau signal-grid shape: WP254

- `flavor-mu-tau-signal-grid-shape.md`
- `data/cms-mu-tau-signal-grid/provenance.json`
- `checkers/wp254_mu_tau_signal_grid_shape.py`
- `results/wp254_mu_tau_signal_grid_shape.json`

WP254 applies the frozen instrument at 130, 140, and 160 GeV. The three signal
columns have exact rank three; adjoining simulated background raises rank to
four, with nonzero minors `626824` and `1880472`. Rate projection remains rank
one. This is finite-grid contextual faithfulness, not yet transport authority
to the actual two pole masses. Weighted completion, QCD, uncertainties, and
finite-power rank remain open.

## Signal-shape transport closure: WP255

- `flavor-signal-shape-transport-closure.md`
- `checkers/wp255_signal_shape_transport_closure.py`
- `results/wp255_signal_shape_transport_closure.json`

WP255 tests normalized linear interpolation leave-one-out at 140 GeV. Exact
closure fails with total-variation residual
`23108773/354073635` (`6.53%`); the largest bin residual is about `-4.25`
percentage points. Thus WP254's finite-grid rank does not mechanically descend
to the physical poles. A source-authorized uncertain morphing law or direct
actual-pole simulation is required; rank-preserving post-hoc interpolation is
forbidden.

## Scale-covariant shape transport: WP256

- `flavor-scale-covariant-shape-transport.md`
- `checkers/wp256_scale_covariant_shape_transport.py`
- `results/wp256_scale_covariant_shape_transport.json`

WP256 repeats the frozen leave-one-out test in the source-relative coordinate
`x = m_visible / M_source`. Its total-variation residual falls from WP255's
`23108773/354073635` to `12641608/354073635` (`3.57%`), so source-mass scaling
captures part of the finite-grid variation. Exact closure nevertheless fails.
The improvement is diagnostic rather than transport authority: actual-pole
simulation or a source-derived uncertain response kernel remains required.

## Source-mass reference descent: WP257

- `flavor-source-mass-reference-descent.md`
- `checkers/wp257_source_mass_reference_descent.py`
- `results/wp257_source_mass_reference_descent.json`

WP257 locates WP256's first nonfaithful arrow. `M_source` is not a `physical16`
coordinate, so `m_visible / M_source` does not descend to the faithful flavor
quotient. The exact hostile pair fixes `physical16` and `m_visible = 65 GeV`
but obtains `1/2` or `13/32` from 130- and 160-GeV reference labels. Adjoining
the label creates a new relational experiment over its stabilizer groupoid;
it does not produce a flavor selector or recover an absolute property.

## Actual-pole reference interface: WP258

- `flavor-actual-pole-reference-interface.md`
- `checkers/wp258_actual_pole_reference_interface.py`
- `results/wp258_actual_pole_reference_interface.json`

WP258 tests the nearest physical repair for WP257: the 2016 CMS forced-dimuon
records at the two actual pole masses. They supply the mass-reference field but
not common decay topology, detector era/reconstruction, event selection, or
physical branching normalization for WP256's 2015 muon–tau response. The
numerical pole match therefore rigidifies the declared MSSM dimuon domain but
does not create a common-frame reference port or a `physical16` selector.

## Muon–tau selector disposition: WP259

- `flavor-tau-branch-selector-disposition.md`
- `checkers/wp259_tau_branch_selector_disposition.py`
- `results/wp259_tau_branch_selector_disposition.json`

WP259 closes the WP252–WP258 branch at selector level. The frozen muon–tau
visible-mass family is an executable finite-domain separator, but rate
projection, actual-pole transport, reference-port forgetting, and dimuon-to-tau
transfer each introduce a named kernel. The operation is consequently a
source-labelled discriminator/readout, neither a proper `physical16` selector
nor a texture-presentation rigidifier or complete physical instrument.

## Commutator-gradient selector audit: WP260

- `flavor-commutator-gradient-selector.md`
- `checkers/wp260_commutator_gradient_selector.py`
- `results/wp260_commutator_gradient_selector.json`

WP260 dynamically realizes spectral pinching as the positive double-commutator
flow generated by the weak-basis-invariant commutator energy. Every finite-time
map is exactly invertible and therefore transports rather than selects. A
proper commuting image occurs only in the infinite-time limit, where it lacks
a finite stopping/stabilization instrument and predicts empirically excluded
trivial mixing. Dissipation alone therefore does not supply a flavor selector.

## Interior-mixing coefficient authority: WP261

- `flavor-interior-mixing-coefficient-authority.md`
- `checkers/wp261_interior_mixing_coefficient_authority.py`
- `results/wp261_interior_mixing_coefficient_authority.json`

WP261 adds the smallest invariant nonlinear term capable of stabilizing an
interior two-generation mixing point. The action `V(x)=-a*x+b*x^2` descends and
conditionally selects `x*=a/(2b)`, but the equally admissible packets `(1,1)`
and `(1,2)` select `1/2` and `1/4`. Geometry therefore supplies a conditional
selector family while numerical authority remains entirely in the unfixed
coefficient ratio.

## Single-invariant operator-count theorem: WP262

- `flavor-single-invariant-operator-count.md`
- `checkers/wp262_single_invariant_operator_count.py`
- `results/wp262_single_invariant_operator_count.json`

WP262 promotes WP261's example to a bounded theorem. One nonconstant monomial
in a normalized invariant mixing coordinate has no interior stationary point.
The minimal polynomial interior selector needs two operator degrees, and its
selected point fixes a relative coefficient. For example `x*=3/10` requires
`a=3b/5`, while the equally invariant packet `a=b` selects `1/2`. The remaining
authority must therefore come from an independent symmetry or microscopic
matching calculation.

## Cross-degree symmetry obstruction: WP263

- `flavor-cross-degree-symmetry-obstruction.md`
- `checkers/wp263_cross_degree_symmetry_obstruction.py`
- `results/wp263_cross_degree_symmetry_obstruction.json`

WP263 closes the ordinary-linear-symmetry repair of WP262. The commutator
invariant and its square occupy homogeneous field degrees four and eight.
Linear source symmetries preserve degree and cannot exchange those operators
or fix their relative coefficient. Closing the gate requires an added
dimensionful spurion, nonlinear symmetry, or microscopic matching relation.

## Gaussian-mediator matching obstruction: WP264

- `flavor-gaussian-mediator-matching.md`
- `checkers/wp264_gaussian_mediator_matching.py`
- `results/wp264_gaussian_mediator_matching.json`

WP264 tests the smallest microscopic matching repair. Integrating out one
stable Gaussian mediator linearly coupled to the commutator invariant produces
the desired negative linear term but an unavoidable negative quadratic term.
A positive stabilizer requires a new direct coefficient or more elaborate
source sector. Minimal tree matching therefore does not derive WP262's missing
relative-coefficient authority.

## Gaussian-sector Schur-complement theorem: WP265

- `flavor-gaussian-sector-schur-complement.md`
- `checkers/wp265_gaussian_sector_schur_complement.py`
- `results/wp265_gaussian_sector_schur_complement.json`

WP265 promotes WP264 to the full finite Gaussian class. For any
positive-definite mediator Hessian `K`, linear coupling produces the effective
term `-x^2 g^T K^-1 g/2`, which is negative semidefinite by Cholesky
factorization. Arbitrary finite mediator mixing therefore cannot generate the
positive interior-mixing stabilizer.

## Linear-source envelope concavity: WP266

- `flavor-linear-source-envelope-concavity.md`
- `checkers/wp266_linear_source_envelope_concavity.py`
- `results/wp266_linear_source_envelope_concavity.json`

WP266 extends the Gaussian sign obstruction to arbitrary stable mediator
self-interactions and finite competing branches. Eliminating a sector from
`U(S)-x*G(S)` takes the infimum of affine functions of `x`, hence produces a
concave effective envelope. Positive curvature for an interior mixing minimum
requires new direct nonlinear invariant dependence or nonequilibrium/quantum
source structure.

## One-loop curvature authority: WP267

- `flavor-one-loop-curvature-authority.md`
- `checkers/wp267_one_loop_curvature_authority.py`
- `results/wp267_one_loop_curvature_authority.json`

WP267 tests the radiative reopening of WP266. A one-loop determinant can give
positive invariant curvature, but its isolated curvature changes sign with the
renormalization-relative logarithm. The physical selector coefficient belongs
to the complete loop-plus-counterterm matching packet; choosing a scale or
counterterm from the observed angle has no source authority.

## RG-completed curvature boundary: WP268

- `flavor-rg-completed-curvature-boundary.md`
- `checkers/wp268_rg_completed_curvature_boundary.py`
- `results/wp268_rg_completed_curvature_boundary.json`

WP268 completes WP267's counterterm running. The matching-scale dependence
cancels exactly, but one renormalized boundary integration constant remains in
the invariant curvature. Two equally RG-consistent boundary values select
`x=1/2` and `x=1/4`. RG consistency therefore transports rather than selects
the numerical coefficient.

## UV fixed-point boundary selector: WP269

- `flavor-uv-fixed-point-boundary-selector.md`
- `checkers/wp269_uv_fixed_point_boundary_selector.py`
- `results/wp269_uv_fixed_point_boundary_selector.json`

WP269 shows that a UV-attractive fixed point can genuinely remove WP268's
initial boundary freedom. However, its selected value is `-beta/alpha`. Two
flows with the same attractive exponent, `-c+1` and `-c+2`, select different
mixing points while forgetting initial data at the same rate. Numerical
authority therefore moves to the UV field content that derives the beta
coefficients.

## UV-limit trajectory kernel: WP270

- `flavor-uv-limit-trajectory-kernel.md`
- `checkers/wp270_uv_limit_trajectory_kernel.py`
- `results/wp270_uv_limit_trajectory_kernel.json`

WP270 corrects the finite-scale interpretation of WP269. Even a completely
fixed attractive beta function admits trajectories `1+A*exp(-t)` with the same
UV limit and different finite matching values. The fixed point selects an
asymptotic boundary class, not the trajectory amplitude required by the flavor
potential. A finite boundary match or zero-dimensional UV critical surface is
still necessary.

## UV stability–predictivity tradeoff: WP271

- `flavor-uv-stability-predictivity-tradeoff.md`
- `checkers/wp271_uv_stability_predictivity_tradeoff.py`
- `results/wp271_uv_stability_predictivity_tradeoff.json`

WP271 generalizes WP270 to a hyperbolic finite-dimensional RG flow. Every
UV-attractive eigendirection contributes one free finite-scale trajectory
amplitude erased by the fixed-point limit. A zero-dimensional critical surface
removes those amplitudes only by eliminating open-basin attraction, leaving a
measure-zero preparation gate.

## Symmetry-fixed trajectory preparation: WP272

- `flavor-symmetry-fixed-trajectory-preparation.md`
- `checkers/wp272_symmetry_fixed_trajectory_preparation.py`
- `results/wp272_symmetry_fixed_trajectory_preparation.json`

WP272 tests whether symmetry closes WP271's preparation gate. A `Z2`-equivariant
flow identifies trajectory amplitudes `A` and `-A` but retains `|A|`; the
finite quotient records for `A=1` and `2` are `1` and `4`. Orbit averaging has
zero mean but nonzero second moment, so a symmetric ensemble is not a prepared
fixed state. The quotient removes sign redundancy but is neither a trajectory
selector nor a flavor texture rigidifier.

## Dissipative preparation resource bound: WP273

- `flavor-dissipative-preparation-resource-bound.md`
- `checkers/wp273_dissipative_preparation_resource_bound.py`
- `results/wp273_dissipative_preparation_resource_bound.json`

WP273 tests the unique-dissipative-vacuum repair. Finite-time relaxation remains
injective; preparation within tolerance requires a declared bound on the
initial amplitude and runtime `log(Amax/epsilon)/gamma`. No finite runtime is
uniform on an unbounded domain. The operation is therefore a conditional
approximate selector only with a source-calibrated resource contract.

## Noisy dissipative selector floor: WP274

- `flavor-noisy-dissipative-selector-floor.md`
- `checkers/wp274_noisy_dissipative_selector_floor.py`
- `results/wp274_noisy_dissipative_selector_floor.json`

WP274 adds source noise to WP273. The Ornstein-Uhlenbeck channel converges to
variance `D/gamma`, not a point. Finite mean-square preparation within
`epsilon^2` requires the strict calibrated inequality `D/gamma < epsilon^2`;
equality is reached only asymptotically. Noisy dissipation is therefore a
conditional approximate distribution selector.

## Feedback selector noise tradeoff: WP275

- `flavor-feedback-selector-noise-tradeoff.md`
- `checkers/wp275_feedback_selector_noise_tradeoff.py`
- `results/wp275_feedback_selector_noise_tradeoff.json`

WP275 adds a calibrated linear sensor-controller port. The exact optimum
balances added damping against injected sensor noise; unbounded gain diverges.
In the frozen packet feedback improves variance from `1/100` to `1/150` but
misses `1/200`. Feedback can refine an approximate selector only in a new
relational experiment with a typed physical sensor and actuator.

## Feedback observability kernel: WP276

- `flavor-feedback-observability-kernel.md`
- `checkers/wp276_feedback_observability_kernel.py`
- `results/wp276_feedback_observability_kernel.json`

WP276 exposes the sensor kernel hidden by WP275's scalar model. A rank-one
sensor on a two-dimensional deviation module leaves a gain-independent blind
direction and zero closed-loop mode. A complementary row restores formal rank
two and a positive observation Gram determinant, but only if it is a
source-derived physical port rather than invented algebraic span.

## Feedback actuator reachability: WP277

- `flavor-feedback-actuator-reachability.md`
- `checkers/wp277_feedback_actuator_reachability.py`
- `results/wp277_feedback_actuator_reachability.json`

WP277 applies the dual control gate. Even with a faithful rank-two sensor, one
actuator leaves an invariant state coordinate and a zero closed-loop mode.
Adding a complementary actuator restores formal reachability, but algebraic
matrix completion is not executable control without a source-derived physical
coupling.

## Dynamic single-port closure: WP278

- `flavor-dynamic-single-port-closure.md`
- `checkers/wp278_dynamic_single_port_closure.py`
- `results/wp278_dynamic_single_port_closure.json`

WP278 gives a conditional positive repair. A source rotation drift makes the
two-score tower `(C,CA)` observable and the control tower `(B,AB)` reachable,
although both instantaneous ports have rank one. Exact one-port feedback and
observer gains stabilize both modes. The remaining gate is a real dynamical
flavon substrate and time-resolved physical instrument, not more algebra.

## Dynamic drift orientation descent: WP279

- `flavor-dynamic-drift-orientation-descent.md`
- `checkers/wp279_dynamic_drift_orientation_descent.py`
- `results/wp279_dynamic_drift_orientation_descent.json`

WP279 applies the full descent gate to WP278. Its rotation generator is
preserved by oriented rotations but flips under reflection. Both chart-local
score towers remain rank two, proving that faithfulness does not imply descent.
A source-derived pseudoscalar can repair covariance; an external orientation
would instead define a new stabilizer-groupoid experiment.

## Jarlskog-oriented drift: WP280

- `flavor-jarlskog-oriented-drift.md`
- `checkers/wp280_jarlskog_oriented_drift.py`
- `results/wp280_jarlskog_oriented_drift.json`

WP280 uses signed Jarlskog `J` as the intrinsic pseudoscalar. The product of
`J` with the rotation generator descends, and both dynamic tower Gram
determinants equal `J^2`. Generic formal closure is restored for nonzero `J`,
but the CP-conserving locus is singular. More importantly, a quotient readout
does not itself generate dynamics: the candidate remains an unauthorized
self-reading law until a CP-odd source field and coupling are derived.

## CP-odd orientation vacuum: WP281

- `flavor-cp-odd-orientation-vacuum.md`
- `checkers/wp281_cp_odd_orientation_vacuum.py`
- `results/wp281_cp_odd_orientation_vacuum.json`

WP281 supplies the missing dynamical pseudoscalar with a CP-even double-well
source. Its two stable vacua generate opposite full-rank drift orientations,
repairing self-reading at the architectural level. The source selects only the
unordered CP-conjugate pair; a signed branch still requires an independently
typed bias, history, boundary condition, or superselection rule.

## Thermal CP-branch selector: WP282

- `flavor-thermal-cp-branch-selector.md`
- `checkers/wp282_thermal_cp_branch_selector.py`
- `results/wp282_thermal_cp_branch_selector.json`

WP282 gives the bias a finite thermal preparation law. Branch odds are
`exp(2*h*v*Vcorr/T)`; a one-percent error requires log odds at least `log(99)`.
Finite bias produces a probabilistic branch selector rather than a certain
sign. The bias, correlation volume, thermal history, walls, and quench remain
source and instrument gates.

## Multi-domain majority amplification: WP283

- `flavor-multidomain-majority-amplification.md`
- `checkers/wp283_multidomain_majority_amplification.py`
- `results/wp283_multidomain_majority_amplification.json`

WP283 shows that nineteen independent `p=3/4` domains are the first odd count
whose formal majority error falls below one percent. But equal-majority spatial
configurations can have different wall counts. Majority amplification is not a
physical coarsening law; global flavor selection still requires source-derived
domain dynamics.

## Biased domain-coarsening threshold: WP284

- `flavor-biased-domain-coarsening-threshold.md`
- `checkers/wp284_biased_domain_coarsening_threshold.py`
- `results/wp284_biased_domain_coarsening_threshold.json`

WP284 replaces majority voting by local zero-temperature domain dynamics. A
positive bias can still trap the wrong uniform vacuum; deterministic finite-ring
coarsening requires the exact threshold `h>2J`. Above it every minus flip lowers
energy and all-plus is the unique absorbing state. The ratio `h/J` and physical
wall dynamics remain source and instrument gates.

## Graph-domain coarsening threshold: WP285

- `flavor-graph-domain-coarsening-threshold.md`
- `checkers/wp285_graph_domain_coarsening_threshold.py`
- `results/wp285_graph_domain_coarsening_threshold.json`

WP285 proves the topology-uniform finite-graph threshold `h>J*Delta`, with
`Delta` the maximum degree. The ring result is only its degree-two case.
Regular graphs retain the wrong uniform vacuum below threshold, so topology is
part of the selector's source contract rather than an incidental presentation.

## Heterogeneous domain selector: WP286

- `flavor-heterogeneous-domain-selector.md`
- `checkers/wp286_heterogeneous_domain_selector.py`
- `results/wp286_heterogeneous_domain_selector.json`

WP286 replaces the global threshold by the exact local conditions
`h_i>sum_j J_ij`. A positive total or averaged bias is not faithful: a weighted
triangle remains locally trapped when one vertex fails its incident wall
budget. Spatially resolved source calibration is therefore mandatory.

## Robust calibrated domain selector: WP287

- `flavor-robust-calibrated-domain-selector.md`
- `checkers/wp287_robust_calibrated_domain_selector.py`
- `results/wp287_robust_calibrated_domain_selector.json`

WP287 upgrades nominal local inequalities to the robust interval conditions
`lower(h_i)>sum_j upper(J_ij)`. A central packet can pass while an admitted
uncertainty corner traps the wrong vacuum. The exact audit checks all 64
parameter corners and all spin configurations.

## Correlated calibration selector: WP288

- `flavor-correlated-calibration-selector.md`
- `checkers/wp288_correlated_calibration_selector.py`
- `results/wp288_correlated_calibration_selector.json`

WP288 shows that a source-declared joint calibration polytope can preserve a
strict selector margin while its independent marginal box falsely fails. The
repair is admissible only when the correlation is derived before evaluating
selection; answer-fitted support remains prohibited.

## Covariance-support selector obstruction: WP289

- `flavor-covariance-support-selector.md`
- `checkers/wp289_covariance_support_selector.py`
- `results/wp289_covariance_support_selector.json`

WP289 proves that joint moments do not determine selector support. Two exact
margin laws share mean 2 and variance 1, while their selector-failure
probabilities are respectively zero and `1/12`. Support or independently
authorized tail bounds remain necessary.

## Moment-tail selector bound: WP290

- `flavor-moment-tail-selector-bound.md`
- `checkers/wp290_moment_tail_selector_bound.py`
- `results/wp290_moment_tail_selector_bound.json`

WP290 gives the sharp distribution-free replacement for support authority:
Cantelli bounds failure by `sigma^2/(sigma^2+mu^2)`. The mean-two,
variance-one bound `1/5` is exactly attained. One-percent certification needs
`mu/sigma>=sqrt(99)` but still does not prove positive support.

## Joint-tail selector bound: WP291

- `flavor-joint-tail-selector-bound.md`
- `checkers/wp291_joint_tail_selector_bound.py`
- `results/wp291_joint_tail_selector_bound.json`

WP291 proves that identical local laws do not determine global selector risk.
Aligned and disjoint three-margin failures give global probabilities `1/12`
and `1/4`. Without dependence probes, a one-percent three-vertex union
certificate requires each `mu_i/sigma_i>=sqrt(299)`.

## Boolean coincidence selector hierarchy: WP292

- `flavor-boolean-coincidence-selector.md`
- `checkers/wp292_boolean_coincidence_selector.py`
- `results/wp292_boolean_coincidence_selector.json`

WP292 shows that even all pairwise coincidence probes remain nonfaithful for
three-domain global risk. Even- and odd-parity laws agree through pair order
but give global failure `3/4` and `1`. The complete labelled Boolean tower
reconstructs the union exactly; physical higher-order coincidence access is
the remaining instrument gate.

## Unlabelled coincidence quotient: WP293

- `flavor-unlabelled-coincidence-quotient.md`
- `checkers/wp293_unlabelled_coincidence_quotient.py`
- `results/wp293_unlabelled_coincidence_quotient.json`

WP293 removes unauthorized domain labels. The complete order tower is exactly
invertible on the four count classes modulo `S3`, but has a four-dimensional
kernel on the eight labelled atoms. Addressable labels require new relational
ports and reduce the physical groupoid to their stabilizer.

## Branch-to-physical16 fiber: WP294

- `flavor-branch-to-physical16-fiber.md`
- `checkers/wp294_branch_to_physical16_fiber.py`
- `results/wp294_branch_to_physical16_fiber.json`

WP294 returns the domain programme to the faithful flavor quotient. Even if a
source maps the prepared branch to `sign(J)`, two exact unitary physical16
points with positive `J` retain different CKM moduli and magnitudes. The first
nonfaithful arrow is `physical16 -> sign(J)`: orientation selection is not
point selection.

## Signed-J physical16 kernel: WP295

- `flavor-signed-j-physical16-kernel.md`
- `checkers/wp295_signed_j_physical16_kernel.py`
- `results/wp295_signed_j_physical16_kernel.json`

WP295 adds the strongest immediate complementary CP-odd probe: exact `|J|`.
Even full signed `J` collapses an exact unitary hostile pair with different
CKM moduli. The remaining kernel is CP-even, so it requires independent
source-derived operations rather than more reliable branch preparation.

## First-row plus signed-J kernel: WP296

- `flavor-first-row-signed-j-kernel.md`
- `checkers/wp296_first_row_signed_j_kernel.py`
- `results/wp296_first_row_signed_j_kernel.json`

WP296 adds all six masses and the complete first CKM row to signed `J`.
Interchanging `s23` and `c23` leaves that readout unchanged while changing the
lower CKM rows. The family is a physical partial separator, not a selector;
lower-sector probes remain necessary for faithfulness.

## Finite CKM phase fiber: WP297

- `flavor-finite-ckm-phase-fiber.md`
- `checkers/wp297_finite_ckm_phase_fiber.py`
- `results/wp297_finite_ckm_phase_fiber.json`

WP297 adds `|V_cb|`, fixing the remaining mixing angle but leaving the exact
`delta` versus `pi-delta` pair because signed `J` fixes only `sin(delta)`.
Four lower-sector moduli distinguish the pair. This is the direct exact rule:
finite fiber is not singleton fiber.

## Compact faithful CKM readout: WP298

- `flavor-minimal-faithful-ckm-readout.md`
- `checkers/wp298_minimal_faithful_ckm_readout.py`
- `results/wp298_minimal_faithful_ckm_readout.json`

WP298 adds the cosine-sensitive `|V_cd|^2` probe and gives exact inverse
formulas on the nondegenerate standard CKM chart. Six masses, four moduli, and
signed `J` reconstruct physical16 there. This closes readout faithfulness but
does not create a source selector.

## Faithful readout is not selection: WP299

- `flavor-faithful-readout-not-selector.md`
- `checkers/wp299_faithful_readout_not_selector.py`
- `results/wp299_faithful_readout_not_selector.json`

WP299 separates the arrow types exactly. A faithful readout has singleton
fibers but preserves the full admissible image. Only an independently defined
source selector has a proper image. Conditioning on an observed singleton
fiber is retrospective inference, not source selection.

## Domain-to-physical16 disposition: WP300

- `flavor-domain-physical16-disposition.md`
- `checkers/wp300_domain_physical16_disposition.py`
- `results/wp300_domain_physical16_disposition.json`

WP300 closes WP284–WP299 as one typed route. Domain dynamics can conditionally
select a branch, but the source-derived branch-to-physical16 interface is
missing. If mapped to `sign(J)`, exact invariant kernels remain. WP298 restores
readout faithfulness; WP299 prevents promoting that readout to selector
authority. No genuine source-generated physical16 selector is established.

## Target-coded invariant potential: WP301

- `flavor-target-coded-invariant-potential.md`
- `checkers/wp301_target_coded_invariant_potential.py`
- `results/wp301_target_coded_invariant_potential.json`

WP301 tests the direct quotient-potential repair. A positive quadratic action
selects `x_star=A^{-1}b`, but the inverse identity `b=A*x_star` shows that an
arbitrary target can be encoded in the linear source. The operation becomes
predictive only if its coefficients are independently source-derived.

## Symmetry direction-amplitude kernel: WP302

- `flavor-symmetry-direction-amplitude-kernel.md`
- `checkers/wp302_symmetry_direction_amplitude_kernel.py`
- `results/wp302_symmetry_direction_amplitude_kernel.json`

WP302 imposes swap symmetry on the invariant potential. Symmetry fixes the
direction `x1=x2`, but the selected amplitude remains `beta/(a+c)`. The same
symmetric architecture selects distinct points at different invariant source
amplitudes. Symmetry rigidifies without numerically selecting.

## Projective direction selector: WP303

- `flavor-projective-direction-selector.md`
- `checkers/wp303_projective_direction_selector.py`
- `results/wp303_projective_direction_selector.json`

WP303 changes the admitted groupoid to positive rays. Swap symmetry then
genuinely selects the singleton projective point `[1:1]`. Distinct
normalization radii lift that ray to distinct physical points, so a
source-derived normalization remains necessary for full physical16 selection.

## Dimensional-transmutation normalization: WP304

- `flavor-dimensional-transmutation-normalization.md`
- `checkers/wp304_dimensional_transmutation_normalization.py`
- `results/wp304_dimensional_transmutation_normalization.json`

WP304 tests RG dimensional transmutation as the normalization lift. The scale
`Lambda=mu0*exp(-1/(b*g0))` is exactly RG invariant, but its numerical value
remains controlled by the boundary coupling `g0`. RG transport relocates
normalization authority; it does not create it.

## Selector predictivity Jacobian: WP305

- `flavor-selector-predictivity-jacobian.md`
- `checkers/wp305_selector_predictivity_jacobian.py`
- `results/wp305_selector_predictivity_jacobian.json`

WP305 measures the local ambiguity of a selector by the response rank of its
physical image to surviving source moduli. WP301 has rank two, swap symmetry
reduces it to one, the projective ratio has rank zero, and both physical
normalization and dimensional transmutation restore rank one. Zero rank is a
necessary, not sufficient, predictivity gate.

## Dual-Jacobian selector and instrument gate: WP306

- `flavor-dual-jacobian-selector-instrument.md`
- `checkers/wp306_dual_jacobian_selector_instrument.py`
- `results/wp306_dual_jacobian_selector_instrument.json`

WP306 separates opposite arrows. Prediction requires zero response of the
selected physical image to surviving source moduli; identification requires
full detector response rank. The exact audit realizes all four combinations,
showing that faithful readout and source selection are independent gates.

## Robust dual-Jacobian margins: WP307

- `flavor-robust-dual-jacobian-margins.md`
- `checkers/wp307_robust_dual_jacobian_margins.py`
- `results/wp307_robust_dual_jacobian_margins.json`

WP307 adds uncertainty. Any admitted nonzero source response, however small,
breaks exact rank-zero prediction. Detector rank instead survives when its
smallest singular value exceeds the calibrated perturbation radius. Structural
source zeros and quantitative detector margins are distinct robust gates.

## Affine symmetry-center authority: WP308

- `flavor-affine-symmetry-center-authority.md`
- `checkers/wp308_affine_symmetry_center_authority.py`
- `results/wp308_affine_symmetry_center_authority.json`

WP308 tests symmetry as a structural-zero mechanism. An affine `Z2` centered
at `a` exactly selects `x=a`, but `dx_star/da=1`. Different embeddings of the
same abstract symmetry select different points. Nonzero numerical authority
therefore resides in the source-derived affine center or reference port.

## Reciprocal ratio selector: WP309

- `flavor-reciprocal-ratio-selector.md`
- `checkers/wp309_reciprocal_ratio_selector.py`
- `results/wp309_reciprocal_ratio_selector.json`

WP309 gives a parameter-free progressive model: reciprocal duality on a
positive dimensionless ratio selects `r=1` with zero source-response rank. A
scaled duality `r->kappa^2/r` restores rank-one ambiguity. Physical admission
requires source-derived duality and normalization, not a fitted ratio chart.

## Up/down reciprocal-duality typing: WP310

- `flavor-up-down-reciprocal-duality-typing.md`
- `checkers/wp310_up_down_reciprocal_duality_typing.py`
- `results/wp310_up_down_reciprocal_duality_typing.json`

WP310 instantiates reciprocity on an ordered-mass hierarchy ratio. Sector
exchange would select equal up/down hierarchies, but it is not an admitted
Standard Model source operation: `u_R` and `d_R` have inequivalent
hypercharges. An enlarged anomaly-consistent source is required.

## Left-right exchange completion: WP311

- `flavor-left-right-exchange-completion.md`
- `checkers/wp311_left_right_exchange_completion.py`
- `results/wp311_left_right_exchange_completion.json`

WP311 repairs the representation mismatch in an enlarged right-handed
doublet. The Weyl exchange is legal upstream and the bidoublet matching is
equivariant. A generic breaking vacuum still gives hierarchy ratio `17/22`;
only the symmetric vacuum gives the reciprocal fixed locus. Vacuum selection
is the next missing arrow.

## Symmetric-vacuum ratio selector: WP312

- `flavor-symmetric-vacuum-ratio-selector.md`
- `checkers/wp312_symmetric_vacuum_ratio_selector.py`
- `results/wp312_symmetric_vacuum_ratio_selector.json`

WP312 supplies a positive sum-of-squares vacuum potential selecting `v1=v2`
throughout its declared coefficient family. The ratio response rank is zero,
while the radial scale remains free. Under WP311 matching the same vacuum
forces the stronger prediction `M_u=M_d`, creating an immediate ensemble
falsifier.

## Symmetric-selector ensemble falsifier: WP313

- `flavor-symmetric-selector-ensemble-falsifier.md`
- `checkers/wp313_symmetric_selector_ensemble_falsifier.py`
- `results/wp313_symmetric_selector_ensemble_falsifier.json`

WP313 rebuilds weak-basis-invariant ordered spectra for all 1,210 canonical
WP20 sheets. Zero sheets satisfy `M_u=M_d`, and zero even satisfy the coarser
equal-hierarchy ratio. WP312 is a genuine selector whose numerical prediction
is decisively falsified, not a presentation rigidifier.

## Soft exchange-breaking ratio selector: WP314

- `flavor-soft-exchange-breaking-ratio.md`
- `checkers/wp314_soft_exchange_breaking_ratio.py`
- `results/wp314_soft_exchange_breaking_ratio.json`

WP314 adds the minimal exchange-odd soft coefficient. It selects
`t=(sqrt(epsilon^2+kappa^2)-epsilon)/kappa`, but the inverse formula installs
any desired ratio through `epsilon/kappa`. Soft breaking repairs equality only
by restoring a rank-one source ambiguity.

## Quantized breaking-sector fiber: WP315

- `flavor-quantized-breaking-sector-fiber.md`
- `checkers/wp315_quantized_breaking_sector_fiber.py`
- `results/wp315_quantized_breaking_sector_fiber.json`

WP315 quantizes `epsilon/kappa=n`. This removes continuous tuning but leaves a
finite discrete prediction family; opposite fluxes give reciprocal ratios.
The simplest positive flux energy selects `n=0` and returns the already
falsified symmetric prediction. Finite fiber is not singleton fiber.

## Nontrivial-flux orbit selector: WP316

- `flavor-nontrivial-flux-orbit-selector.md`
- `checkers/wp316_nontrivial_flux_orbit_selector.py`
- `results/wp316_nontrivial_flux_orbit_selector.json`

WP316 excludes the trivial sector by source topology. `E=n^2` then selects the
singleton exchange orbit `|n|=1` without fitted coefficients. Literal signs
predict reciprocal ordered ratios, so an orientation port is required before
matching to labelled Standard Model sectors.

## Unit-flux ensemble falsifier: WP317

- `flavor-unit-flux-ensemble-falsifier.md`
- `checkers/wp317_unit_flux_ensemble_falsifier.py`
- `results/wp317_unit_flux_ensemble_falsifier.json`

WP317 tests both orientations of WP316's reciprocal unit-flux prediction on
all 1,210 canonical fitted sheets. No orientation port can rescue a failure,
because both ordered branches are admitted before comparison. The topology is
a genuine conditional selector, but its numerical hierarchy prediction is
falsified on the complete fitted ensemble.

## High-flux discrete lookup audit: WP318

- `flavor-high-flux-discrete-lookup.md`
- `checkers/wp318_high_flux_discrete_lookup.py`
- `results/wp318_high_flux_discrete_lookup.json`

WP318 allows the full quantized ratio lattice and finds that the fitted
hierarchy range intersects only magnitude 64. This does not rescue selection:
the admitted quadratic source energy selects magnitude 1, while choosing 64
from the downstream fit is a discrete lookup. Quantization removes continuous
tuning but does not provide upstream numerical authority.

## Fixed-charge center authority: WP319

- `flavor-fixed-charge-center-authority.md`
- `checkers/wp319_fixed_charge_center_authority.py`
- `results/wp319_fixed_charge_center_authority.json`

WP319 tests the apparent repair `E_N(m)=(m-N)^2`. It uniquely selects charge
magnitude `N`, but the same grammar permits every center and the selected ratio
responds strictly to `N`. The construction relocates numerical authority into
a discrete boundary label; it does not explain why the fitted lookup happens
near magnitude 64.

## Binary-cardinality groupoid audit: WP320

- `flavor-binary-cardinality-groupoid.md`
- `checkers/wp320_binary_cardinality_groupoid.py`
- `results/wp320_binary_cardinality_groupoid.json`

WP320 attacks the tempting identity `64=2^6`. Six labelled binary slots have
64 literal words, but only seven `S6` permutation orbits, or four after global
complement exchange. Obtaining 64 therefore requires physically distinguishable
label ports plus a source-derived map from literal cardinality to flux; it is
not a prediction of the unlabelled quotient.

## Quark-slot port descent: WP321

- `flavor-quark-slot-port-descent.md`
- `checkers/wp321_quark_slot_port_descent.py`
- `results/wp321_quark_slot_port_descent.json`

WP321 tests whether the six binary labels can be supplied by the six quark
names. Under independent up/down generation permutations, 64 literal words
collapse to 16 sector-weight classes, or 10 after sector exchange. Individual
binary addresses fail descent already on this subgroup. Mass-ordered Yukawa
eigenvectors are downstream readouts and cannot retroactively define source
ports.

## Relational generation spurion: WP322

- `flavor-relational-generation-spurion.md`
- `checkers/wp322_relational_generation_spurion.py`
- `results/wp322_relational_generation_spurion.json`

WP322 adds a nondegenerate Hermitian reference spurion. Three mixed moments
form an invertible Vandermonde system and separate all binary generation
occupancies. This is a new relational experiment over the stabilizer of the
spurion: it supplies faithful labelled readout and rigidification, but selects
neither a charge magnitude nor a `physical16` point.

## Spectral-projector selector: WP323

- `flavor-spectral-projector-selector.md`
- `checkers/wp323_spectral_projector_selector.py`
- `results/wp323_spectral_projector_selector.json`

WP323 upgrades the reference construction to a genuine relational selector.
A positive squared-distance potential uniquely selects the negative spectral
projector of a nondegenerate Hermitian reference and descends under simultaneous
conjugation. The operation is both selector and rigidifier conditional on the
reference, but supplies neither an absolute generation label nor a map to
charge 64 or `physical16`.

## Projector flavor-lift no-go: WP324

- `flavor-projector-flavor-lift-no-go.md`
- `checkers/wp324_projector_flavor_lift_no_go.py`
- `results/wp324_projector_flavor_lift_no_go.json`

WP324 applies the minimal affine Yukawa lift to the WP323 projector. Both
sector characteristic polynomials retain an exact double root for every
coefficient choice, and their Hermitian covariants commute. The relational
selector is genuine, but its economical flavor image lies on the degenerate
boundary outside nondegenerate `physical16` and has no generic CKM mixing.

## Two-projector flavor lift: WP325

- `flavor-two-projector-flavor-lift.md`
- `checkers/wp325_two_projector_flavor_lift.py`
- `results/wp325_two_projector_flavor_lift.json`

WP325 adds a second nonorthogonal relational projector. Exact affine lifts can
now have nondegenerate spectra and a nonzero sector commutator, repairing
WP324's first obstruction. The two projectors retain a common invariant line,
however, so mixing is only two-family and the cubic CP-odd commutator trace
vanishes exactly.

## Three-projector CP capability: WP326

- `flavor-three-projector-cp-capability.md`
- `checkers/wp326_three_projector_cp_capability.py`
- `results/wp326_three_projector_cp_capability.json`

WP326 adds a third projector with complex overlap geometry. The three rays span
the full space; an exact affine witness has nondegenerate spectra, nonsingular
sector commutator, and nonzero cubic CP-odd invariant. This establishes generic
`physical16` capability, not selection: the rays and coefficients are
stipulated, and complex conjugation supplies an exact opposite-CP branch with
the same sector spectra.

## CP-orientation selector: WP327

- `flavor-cp-orientation-selector.md`
- `checkers/wp327_cp_orientation_selector.py`
- `results/wp327_cp_orientation_selector.json`

WP327 separates spontaneous CP breaking from CP-orientation selection. A
CP-even double-well selects the finite conjugate fiber `c=+-c0` with identical
energies and curvatures. A linear CP-odd bias selects one sign but introduces a
new source-authority parameter. Observing a domain with a CP-sensitive
instrument does not turn branch readout into unique source selection.

## CP-domain preparation channel: WP328

- `flavor-cp-domain-preparation-channel.md`
- `checkers/wp328_cp_domain_preparation_channel.py`
- `results/wp328_cp_domain_preparation_channel.json`

WP328 promotes the WP327 branch pair to a thermal preparation channel. Its
CP-resolved log-odds is `2 beta epsilon c0`, so the response to the three source
parameters has rank one and a two-dimensional kernel. Repeated calibrated
branch counts can identify the preparation bias product, but neither one
observed domain nor the full branch frequency identifies its separate source
story.

## CP-detector calibration: WP329

- `flavor-cp-detector-calibration.md`
- `checkers/wp329_cp_detector_calibration.py`
- `results/wp329_cp_detector_calibration.json`

WP329 adds known-negative and known-positive calibration ports to the CP-domain
detector. The resulting three-readout Jacobian has determinant equal to minus
the detector contrast, so it is faithful to the true branch probability away
from zero contrast. This repairs detector identification, not source selection
or WP328's source-parameter kernel.

## CP complementary-probe tower: WP330

- `flavor-cp-complementary-probe-tower.md`
- `checkers/wp330_cp_complementary_probe_tower.py`
- `results/wp330_cp_complementary_probe_tower.json`

WP330 adds formal inverse-temperature and CP-scale probes to the calibrated
branch log-odds. Either complement alone leaves a one-dimensional kernel; both
give a full-rank response with determinant `-2 beta c0`. This proves minimal
formal identifiability, not joint physical executability or selection: the two
common-freeze-out instrument constructors remain missing.

## Common-frame CP instrument: WP331

- `flavor-common-frame-cp-instrument.md`
- `checkers/wp331_common_frame_cp_instrument.py`
- `results/wp331_common_frame_cp_instrument.json`

WP331 supplies an explicit common-frame contract: a co-located two-level
thermometer, CP-amplitude transducer, and branch log-odds channel. With frozen
gap and gain its response determinant is nonzero and the source triple is
exactly invertible. Floating either calibration restores a rescaling kernel;
physical co-location, calibration, uncertainty, and freeze-out simultaneity
remain unbuilt instrument gates.

## Log-instrument robust margin: WP332

- `flavor-log-instrument-robust-margin.md`
- `checkers/wp332_log_instrument_robust_margin.py`
- `results/wp332_log_instrument_robust_margin.json`

WP332 rewrites the calibrated WP331 response in positive logarithmic
coordinates. The constant Jacobian has smallest singular value
`sqrt(2-sqrt(3))`, yielding an exact uniform perturbation margin for full-rank
identification. The certificate excludes zero bias and remains conditional on
turning physical errors into a valid common-frame spectral-norm bound.

## Zero-bias chart completion: WP333

- `flavor-zero-bias-chart-completion.md`
- `checkers/wp333_zero_bias_chart_completion.py`
- `results/wp333_zero_bias_chart_completion.json`

WP333 returns to nonlogarithmic common-frame coordinates and proves that the
instrument remains full rank at zero CP bias. The exact boundary singular
values expose a unit-aware robustness margin. The zero stratum is a chart
boundary for WP332, not a physical identification kernel; finite-sample
resolution and a calibrated detector metric remain necessary.

## CP-bias finite-sample resolution: WP334

- `flavor-cp-bias-finite-sample-resolution.md`
- `checkers/wp334_cp_bias_finite_sample_resolution.py`
- `results/wp334_cp_bias_finite_sample_resolution.json`

WP334 derives the exact Bernoulli Fisher information for detecting bias through
the calibrated CP detector. At zero bias, symmetric detector confusion reduces
the information by the squared contrast, while zero contrast kills it for all
sample counts. Local identifiability therefore remains distinct from finite
statistical resolution and from repeatable physical domain preparation.

## Correlated-domain resolution: WP335

- `flavor-correlated-domain-resolution.md`
- `checkers/wp335_correlated_domain_resolution.py`
- `results/wp335_correlated_domain_resolution.json`

WP335 removes the independent-domain assumption. Exchangeable correlation
inflates the sample-mean variance and replaces `N` by the exact effective count
`N/[1+(N-1)rho]`; perfect correlation leaves one effective sample. Covariance
alone does not determine a joint likelihood or Fisher information, so the
packet grants only a second-moment correction pending a source-derived domain
correlation model.

## Exchangeable count tower: WP336

- `flavor-exchangeable-count-tower.md`
- `checkers/wp336_exchangeable_count_tower.py`
- `results/wp336_exchangeable_count_tower.json`

WP336 transfers Benincasa's finite inversion theorem to six exchangeable CP
domains. The complete factorial-count tower is a unimodular binomial zeta
transform and reconstructs the entire count law exactly. It remains blind to
labelled spatial routes; physical use requires executable coincidence probes
through order six and a source-derived exchangeability contract or label ports.

## Thinned count-tower calibration: WP337

- `flavor-thinned-count-tower-calibration.md`
- `checkers/wp337_thinned_count_tower_calibration.py`
- `results/wp337_thinned_count_tower_calibration.json`

WP337 types the complete count tower through independent detector thinning.
The `j`-th factorial moment scales by `eta^j`, and the calibrated composite
determinant is `eta^21`. Without an independent efficiency-normal channel,
distinct source occupancies and efficiencies yield identical complete detected
laws. Raw coincidence moments therefore cannot self-calibrate their deletion
sectors.

## Confused coincidence tower: WP338

- `flavor-confused-coincidence-tower.md`
- `checkers/wp338_confused_coincidence_tower.py`
- `results/wp338_confused_coincidence_tower.json`

WP338 adds false-positive backgrounds to the order-six coincidence tower. Raw
order `j` contains every lower detector sector, but calibrated background
subtraction gives a triangular inverse with determinant `gamma^21`. As in
Benincasa's contact-normal correction, the calibration channel must be derived
independently rather than fitted from the desired source reconstruction.

## Coincidence-tower robustness: WP339

- `flavor-coincidence-tower-robustness.md`
- `checkers/wp339_coincidence_tower_robustness.py`
- `results/wp339_coincidence_tower_robustness.json`

WP339 shows that WP338's formal inverse is poorly conditioned at low contrast.
Even without background, sixth-order error is amplified by `gamma^-6`: factors
64 and one million at contrasts one-half and one-tenth. Robust faithfulness
therefore needs a certified contrast floor and a full propagated error budget,
not merely a nonzero determinant.

## First-order domain sufficiency: WP340

- `flavor-first-order-domain-sufficiency.md`
- `checkers/wp340_first_order_domain_sufficiency.py`
- `results/wp340_first_order_domain_sufficiency.json`

WP340 freezes the one-parameter independent Bernoulli source grammar and proves
that the calibrated first moment already reconstructs its probability. Higher
coincidences are redundant and less robust inside that family. An exact
correlated hostile pair shares the first moment but differs at second order, so
the reduction is valid only after independence is independently authorized.

## Independence-probe hierarchy: WP341

- `flavor-independence-probe-hierarchy.md`
- `checkers/wp341_independence_probe_hierarchy.py`
- `results/wp341_independence_probe_hierarchy.json`

WP341 asks how to test WP340's iid grammar. Second order detects pair covariance
but cannot certify mutual independence: iid fair coins and a uniform
even-parity law share all first and second moments while differing at third
order. Probe order must therefore track the admitted dependence family and its
contrast-conditioned instrument cost.

## Six-domain parity obstruction: WP342

- `flavor-six-domain-parity-obstruction.md`
- `checkers/wp342_six_domain_parity_obstruction.py`
- `results/wp342_six_domain_parity_obstruction.json`

WP342 constructs the uniform odd-parity law on six domains. It agrees with iid
fair domains on every labelled coincidence through order five and differs only
at order six. Therefore no truncated tower certifies independence on the
unrestricted six-bit family; one needs the poorly conditioned sixth-order
probe or an independently derived source theorem excluding global parity.

## Additive-source factorization: WP343

- `flavor-additive-source-factorization.md`
- `checkers/wp343_additive_source_factorization.py`
- `results/wp343_additive_source_factorization.json`

WP343 supplies the conditional source theorem requested by WP342. A strictly
additive identical one-site action with positive weights and no shared latent
field or global constraint factorizes exactly, forcing every moment to `p^j`
and excluding parity laws. It authorizes first-order sufficiency inside that
grammar but does not select `p`; connected coincidences remain falsification
controls.

## Shared latent mediator: WP344

- `flavor-shared-latent-mediator.md`
- `checkers/wp344_shared_latent_mediator.py`
- `results/wp344_shared_latent_mediator.json`

WP344 supplies the exact hidden-common-cause attack on WP343. Domains can be
iid conditional on one shared mediator yet correlated after its record is
discarded. The mixture has the same first moment as a product law but connected
pair coincidence `d^2`. First-order sufficiency therefore requires the
no-latent clause or a calibrated second-order control.

## Symmetric-mediator quotient: WP345

- `flavor-symmetric-mediator-quotient.md`
- `checkers/wp345_symmetric_mediator_quotient.py`
- `results/wp345_symmetric_mediator_quotient.json`

WP345 quotients the equal-weight mediator by branch exchange. First and second
moments reconstruct `(pbar,d^2)` with unit Jacobian determinant; the apparent
signed-coordinate singularity at `d=0` is a chart effect. Third order is then a
grammar falsifier, not an additional parameter probe. Resolving the sign of
`d` requires a new branch-labelled reference experiment.

## Unequal-mediator moment inversion: WP346

- `flavor-unequal-mediator-moment-inversion.md`
- `checkers/wp346_unequal_mediator_moment_inversion.py`
- `results/wp346_unequal_mediator_moment_inversion.json`

WP346 widens the shared mediator to unequal branch weights. Three calibrated
moments generically reconstruct the unordered weighted two-point measure; the
Jacobian determinant is `w(1-w)(a-b)^4`. Fourth order is a grammar-consistency
test. Identification fails exactly at unused-branch and branch-collision
strata, and still supplies no selector of the recovered parameters.

## CP-selector physical16 rank: WP347

- `flavor-cp-selector-physical16-rank.md`
- `checkers/wp347_cp_selector_physical16_rank.py`
- `results/wp347_cp_selector_physical16_rank.json`

WP347 returns the CP-domain branch to the faithful flavor quotient. Shell and
orientation selection constrain one CP-odd coordinate but leave fifteen
CP-even directions free. The operation is a genuine conditional partial
selector, not a full `physical16` selector or readout; the first projection to
the CP coordinate is the irreparable nonfaithful arrow for the remaining
directions.

## Three-projector coefficient authority: WP348

- `flavor-three-projector-coefficient-authority.md`
- `checkers/wp348_three_projector_coefficient_authority.py`
- `results/wp348_three_projector_coefficient_authority.json`

WP348 intervenes on one affine coefficient of the generic WP326 lift. Up norm,
up determinant, and the CP-odd invariant all have nonzero exact response at the
benchmark. The coefficient survives to faithful physical invariants, proving
that WP326 is a tunable capability family rather than a numerical selector.

## Democratic projector-symmetry no-go: WP349

- `flavor-democratic-projector-symmetry-no-go.md`
- `checkers/wp349_democratic_projector_symmetry_no_go.py`
- `results/wp349_democratic_projector_symmetry_no_go.json`

WP349 tests the natural parameter-free repair: a common permutation symmetry
forcing democratic projector coefficients. Both sectors then become
polynomials in `P+Q+R`, so their Hermitian covariants commute and CP vanishes
identically. The symmetry genuinely rigidifies coefficients but removes the
relative geometry required for a viable `physical16` selector.

## Sector-character coefficient rays: WP350

- `flavor-sector-character-rays.md`
- `checkers/wp350_sector_character_rays.py`
- `results/wp350_sector_character_rays.json`

WP350 assigns distinct symmetry characters to the two sectors, selecting the
nonparallel rays `(1,1,1)` and `(1,-1,0)`. An exact benchmark has nondegenerate
spectra and nonzero CP, so structural direction selection can evade WP349.
Both radial amplitudes retain nonzero physical response, leaving a two-parameter
capability family rather than a numerical `physical16` selector.

## Radial-independent CP selector: WP351

- `flavor-radial-independent-cp-selector.md`
- `checkers/wp351_radial_independent_cp_selector.py`
- `results/wp351_radial_independent_cp_selector.json`

WP351 divides the WP350 CP commutator by the exact sector discriminants. All
radial dependence cancels, yielding the numerical prediction `J^2=1/543` on
every nondegenerate radial stratum. This is a genuine conditional partial
mixing selector, not a full `physical16` selector; its projector geometry and
sector-character source remain to be derived and its ensemble prediction must
now be tested.

## CP-selector ensemble falsifier: WP352

- `flavor-cp-selector-ensemble-falsifier.md`
- `checkers/wp352_cp_selector_ensemble_falsifier.py`
- `results/wp352_cp_selector_ensemble_falsifier.json`

WP352 tests `J^2=1/543` on all 1,210 canonical fitted sheets, admitting both CP
signs. Zero sheets match; the predicted magnitude exceeds every fitted value
by more than three orders. The selected-ray geometry is therefore a genuine
conditional selector that is numerically falsified, not a rigidifier awaiting
radial or detector repair.

## Complex-geometry deformation: WP353

- `flavor-complex-geometry-deformation.md`
- `checkers/wp353_complex_geometry_deformation.py`
- `results/wp353_complex_geometry_deformation.json`

WP353 continuously deforms the complex projector ray and derives an exact
rational `J^2(t)`. The family interpolates from CP conservation at `t=0` to the
falsified WP351 value at `t=1`; the fitted scale lies on a small-deformation
capability branch. Selecting that branch from data would merely transfer
numerical authority into the geometry parameter.

## CP-geometry technical naturalness: WP354

- `flavor-cp-geometry-technical-naturalness.md`
- `checkers/wp354_cp_geometry_technical_naturalness.py`
- `results/wp354_cp_geometry_technical_naturalness.json`

WP354 shows that CP symmetry and multiplicative transport can protect a small
geometry deformation, but the matched value has unit logarithmic response to
its boundary seed. Technical naturalness explains stability, not magnitude;
RG remains a carrier until a nonzero seed or threshold kick is independently
derived.

## Instanton-seed authority: WP355

- `flavor-instanton-seed-authority.md`
- `checkers/wp355_instanton_seed_authority.py`
- `results/wp355_instanton_seed_authority.json`

WP355 tests a quantized instanton seed. Charge discretization protects
smallness but leaves nonzero logarithmic response to the coupling. The WP353
fitted-scale estimate requires unit-charge coupling above the declared
weak-coupling control domain; the semiclassical formula is therefore neither a
controlled numerical selector nor permission to fit the coupling from `J`.

## Critical-bifurcation authority: WP356

- `flavor-critical-bifurcation-authority.md`
- `checkers/wp356_critical_bifurcation_authority.py`
- `results/wp356_critical_bifurcation_authority.json`

WP356 tests whether a source pitchfork can select the small nonzero WP353
geometry deformation. It selects the symmetric versus broken phase and
rigidifies the broken vacuum to a sign pair, but the magnitude remains
`q=-r/u`. Quantizing `r=-m*Delta` leaves the smallest nonzero value `Delta/u`;
criticality is therefore a carrier and phase selector, not a numerical
physical16 selector.

## First-order jump authority: WP357

- `flavor-first-order-jump-authority.md`
- `checkers/wp357_first_order_jump_authority.py`
- `results/wp357_first_order_jump_authority.json`

WP357 tests the finite-jump escape from WP356. Sextic coexistence fixes
`r=3*u^2/(16*w)` and produces a discontinuous broken magnitude
`q=-3*u/(4*w)`. This removes near-critical susceptibility but leaves the
quartic-to-sextic ratio authoritative, so coexistence selects a phase and
rigidifies a sign pair without numerically selecting the physical readout.

## Coexistence fluctuation completion: WP358

- `flavor-coexistence-fluctuation-completion.md`
- `checkers/wp358_coexistence_fluctuation_completion.py`
- `results/wp358_coexistence_fluctuation_completion.json`

WP358 adds the source-derived broken-vacuum curvature to WP357's jump. The
joint response has nonzero determinant and exactly reconstructs every
coexistence coefficient packet once kinetic normalization is fixed. This
repairs source identification, not selection: arbitrary positive jump and
curvature values remain admissible, and a calibrated pole-mass instrument is
still required.

## Canonical fluctuation descent: WP359

- `flavor-canonical-fluctuation-descent.md`
- `checkers/wp359_canonical_fluctuation_descent.py`
- `results/wp359_canonical_fluctuation_descent.json`

WP359 removes WP358's coordinate-normalization ambiguity. The invariant
readouts `Q=Z*q` and `M2=kappa/Z` exactly reconstruct the canonically
normalized coexistence coefficients and identify field-rescaling orbits. This
is a faithful effective-source quotient and a properly typed candidate
instrument, but it neither selects numerical values nor proves full
weak-basis descent into `physical16`.

## Canonical source-to-physical16 portal: WP360

- `flavor-canonical-source-to-physical16-portal.md`
- `checkers/wp360_canonical_source_physical16_portal.py`
- `results/wp360_canonical_source_physical16_portal.json`

WP360 supplies the minimal full weak-basis-descending interface from WP359's
canonical source displacement to flavor: a conditional positive portal
`lambda*(J^2-c*Q)^2`. It selects a proper codimension-one CP shell but leaves
fifteen CP-even coordinates, CP orientation, and the numerical matching
coefficient free. This is genuine conditional selection, not a full
`physical16` prediction.

## Dimensionless portal normalization: WP361

- `flavor-dimensionless-portal-normalization.md`
- `checkers/wp361_dimensionless_portal_normalization.py`
- `results/wp361_dimensionless_portal_normalization.json`

WP361 uses WP359's pole scale to replace WP360's dimensionful matching by the
ratio `rho=Q/M2`. Dimensional closure still permits an arbitrary positive
dimensionless coefficient `alpha`, and the portal discards the independent
sextic source direction. It therefore remains a conditional shell selector,
not a numerical selector or faithful source identifier.

## Cross-sector exchange Ward gate: WP362

- `flavor-cross-sector-exchange-ward-gate.md`
- `checkers/wp362_cross_sector_exchange_ward_gate.py`
- `results/wp362_cross_sector_exchange_ward_gate.json`

WP362 proves that a Ward exchange of the dimensionless ports `J^2` and
`Q/M2` would force WP361's positive matching coefficient to `alpha=1`.
However, the exchange is not contained in the existing product groupoid. It
requires a new source-derived relational two-port experiment and stabilizer
groupoid; without that interface it is unauthorized algebraic
parallelization, not a flavor theorem. WP363 further qualifies the unit result:
it assumes a unit relative port calibration.

## Scaled exchange normalization obstruction: WP363

- `flavor-scaled-exchange-normalization-obstruction.md`
- `checkers/wp363_scaled_exchange_normalization_obstruction.py`
- `results/wp363_scaled_exchange_normalization_obstruction.json`

WP363 attacks the hidden normalization in WP362. Every positive scaled swap
is involutive, and its Ward identity fixes `alpha=s`, not `alpha=1`. A common
source-defined Euclidean Gram pairing additionally forces `s=1`; detector
calibration can identify `s` but cannot turn it into a source prediction.
WP364 further separates Euclidean equal norm from mere positivity.

## Positive-pairing scale kernel: WP364

- `flavor-positive-pairing-scale-kernel.md`
- `checkers/wp364_positive_pairing_scale_kernel.py`
- `results/wp364_positive_pairing_scale_kernel.json`

WP364 proves that every positive exchange scale admits invariant positive Gram
metrics, including determinant-one metrics. Positivity therefore converts the
scale into a port norm ratio but does not select it. Unit normalization follows
only from the additional source condition that the two port norms are equal in
a fixed common-unit chart. WP365 gives the quotient correction.

## Port-unit quotient correction: WP365

- `flavor-port-unit-quotient-correction.md`
- `checkers/wp365_port_unit_quotient_correction.py`
- `results/wp365_port_unit_quotient_correction.json`

WP365 quotients independent positive changes of units on the two relational
ports. Both `s` and `alpha` transform by the same factor, so only `alpha/s` is
invariant. The Ward result is the relational selection `alpha/s=1`; its unit
form and equal-coordinate-norm statement require a physically fixed common
unit and otherwise are presentation rigidification.

## Common-perturbation port calibration: WP366

- `flavor-common-perturbation-port-calibration.md`
- `checkers/wp366_common_perturbation_port_calibration.py`
- `results/wp366_common_perturbation_port_calibration.json`

WP366 gives an operational candidate for WP365's relational scale. One common
source perturbation and independently calibrated detector gains recover the
unit-invariant response ratio `p/q` and make the Ward relation falsifiable.
The response has rank one and measures rather than predicts the scale; a
concrete source operation causally reaching both ports remains missing.

## Quartic-intervention common response: WP367

- `flavor-quartic-intervention-common-response.md`
- `checkers/wp367_quartic_intervention_common_response.py`
- `results/wp367_quartic_intervention_common_response.json`

WP367 supplies that common perturbation conditionally inside the canonical
portal grammar. Intervening on `U` moves both `Q/M2=-1/U` and the equilibrium
shell `J^2=alpha*Q/M2`, with exact response ratio `p/q=alpha`. Portal deletion
kills only the flavor response. This is a causal source-side constructor, but
a physical threshold knob and joint calibrated measurement remain unproved.

## Mediator-mass threshold knob: WP368

- `flavor-mediator-mass-threshold-knob.md`
- `checkers/wp368_mediator_mass_threshold_knob.py`
- `results/wp368_mediator_mass_threshold_knob.json`

WP368 realizes WP367's quartic intervention by tree-level elimination of a
heavy singlet mediator with a controlled pole mass. Exact matching, deletion,
and decoupling tests pass, and the common response still gives `p/q=alpha`.
The remaining gate is laboratory control of that pole mass with finite widths,
mixing, loops, stability, and detector resolution included.

## Finite-width complementary threshold: WP369

- `flavor-finite-width-complementary-threshold.md`
- `checkers/wp369_finite_width_complementary_threshold.py`
- `results/wp369_finite_width_complementary_threshold.json`

WP369 adds the mediator's absorptive channel. The ordinary dispersive response
is blind at `L=Omega`, while the source-derived width response is exactly
nonzero there. Joint dispersive and absorptive threshold coordinates locally
identify the pole packet when the coupling is known, but the single mass
control remains rank one and no new numerical flavor selector appears.

## Threshold detector confusion: WP370

- `flavor-threshold-detector-confusion.md`
- `checkers/wp370_threshold_detector_confusion.py`
- `results/wp370_threshold_detector_confusion.json`

WP370 composes WP369 with a calibrated two-channel detector. Faithfulness
survives exactly for positive contrast `gamma=1-2*beta`; complete confusion
collapses the complementary channels, and unknown differential background
creates a separate exact kernel. Detector inversion identifies threshold data
but supplies no new control or selector authority.

## Threshold finite-sample Fisher gate: WP371

- `flavor-threshold-finite-sample-fisher.md`
- `checkers/wp371_threshold_finite_sample_fisher.py`
- `results/wp371_threshold_finite_sample_fisher.json`

WP371 adds finite sample size and calibrated differential-background
covariance. The exact Fisher determinant stays positive for positive detector
contrast, while complete confusion kills it. A fixed unknown background is a
different model: at one scan point it creates a one-dimensional nuisance
kernel that repeated samples alone cannot remove.

## Two-point threshold scan: WP372

- `flavor-two-point-threshold-scan.md`
- `checkers/wp372_two_point_threshold_scan.py`
- `results/wp372_two_point_threshold_scan.json`

WP372 uses two predeclared distinct mediator-mass settings and one shared fixed
differential background. An exact positive three-by-three minor proves global
local rank three on the admitted positive domain. Repeating one setting leaves
rank two; calibrated positive detector contrast preserves the repaired rank.

## Two-point background-drift robustness: WP373

- `flavor-two-point-background-drift-robustness.md`
- `checkers/wp373_two_point_background_drift_robustness.py`
- `results/wp373_two_point_background_drift_robustness.json`

WP373 strengthens WP372 to independent differential background at each scan
setting. The exact four-by-four determinant stays positive and even survives
complete channel confusion because two common-channel contexts identify the
pole. Independent common plus differential offsets at both settings instead
create a two-dimensional kernel.

## Three-point common-drift scan: WP374

- `flavor-three-point-common-drift-scan.md`
- `checkers/wp374_three_point_common_drift_scan.py`
- `results/wp374_three_point_common_drift_scan.json`

WP374 sizes the minimal scan for one common offset shared across the scan plus
independent differential drift at every point. Three equally spaced settings
give a globally nonzero reduced determinant with cubic spacing margin and a
full six-parameter benchmark. Independent common drift at every setting still
exceeds the record dimension.

## Three-point spacing optimum: WP375

- `flavor-three-point-spacing-optimum.md`
- `checkers/wp375_three_point_spacing_optimum.py`
- `results/wp375_three_point_spacing_optimum.json`

WP375 upgrades rank to a frozen D-optimal design at `L=Omega=1` with constant
covariance and cost. The determinant vanishes for collapsed and infinitely
separated scans and has one exact positive stationary root, bracketed by 1 and
`3/2`. The numerical locator is about `1.270374202`; it is not a universal or
flavor-fitted setting.

## Width-ratio scan optimum: WP376

- `flavor-width-ratio-scan-optimum.md`
- `checkers/wp376_width_ratio_scan_optimum.py`
- `results/wp376_width_ratio_scan_optimum.json`

WP376 proves that WP375's unique finite optimum persists for every positive
width ratio `r=Omega/L`. The exact stationarity polynomial has one coefficient
sign change and hence one positive root. The calibrated scaling law is
`d_star=L*h_star(Omega/L)`; the optimum moves with source pole data and is not
a universal constant.

## Critical-to-threshold selector disposition: WP377

- `flavor-critical-to-threshold-selector-disposition.md`
- `checkers/wp377_critical_to_threshold_selector_disposition.py`
- `results/wp377_critical_to_threshold_selector_disposition.json`

WP377 reconciles WP356--WP376. The invariant portal is a conditional
codimension-one CP-shell selector, but it leaves fifteen CP-even directions,
orientation, and matching normalization free. The mediator and scan branch
progressively establishes source identification and instrument design without
adding flavor-selector authority. No presently admitted numerical or full
`physical16` selector survives all gates.

## Local polynomial CP portal: WP378

- `flavor-local-polynomial-cp-portal.md`
- `checkers/wp378_local_polynomial_cp_portal.py`
- `results/wp378_local_polynomial_cp_portal.json`

WP378 clears the spectral denominators in WP377's normalized `J^2` portal.
The resulting polynomial invariant selects the same shell only on the
nondegenerate stratum, becomes blind to the source ratio at spectral
degeneracy, and its positive square has bifundamental field degree 48. Local
polynomial descent is therefore possible only as a very high-degree EFT
constructor, not yet a microscopic numerical selector.

## Gaussian portal sign obstruction: WP379

- `flavor-gaussian-portal-sign-obstruction.md`
- `checkers/wp379_gaussian_portal_sign_obstruction.py`
- `results/wp379_gaussian_portal_sign_obstruction.json`

WP379 closes the ordinary healthy linear-Gaussian mediator branch. Exact tree
elimination produces a negative-semidefinite `F^2` coefficient, while WP378
requires a positive shell penalty; multiple healthy Gaussian mediators cannot
reverse the sign. The linearized vertex also retains field degree 25, so it is
an auxiliary EFT rewrite rather than a renormalizable microscopic completion.

## Stable-mediator envelope sign theorem: WP380

- `flavor-stable-mediator-envelope-sign.md`
- `checkers/wp380_stable_mediator_envelope_sign.py`
- `results/wp380_stable_mediator_envelope_sign.json`

WP380 extends the obstruction to every smooth classically minimized healthy
mediator sector at quadratic order. The exact envelope Hessian is the Schur
complement `K-G^T H^-1 G`; without a direct positive contact it is negative
semidefinite, and nonlinear self-stabilization cannot reverse the sign. A
positive selector therefore resides in an independently authorized direct
contact or a mechanism outside stable classical minimization.

## Constrained-auxiliary authority audit: WP381

- `flavor-constrained-auxiliary-authority.md`
- `checkers/wp381_constrained_auxiliary_authority.py`
- `results/wp381_constrained_auxiliary_authority.json`

WP381 tests the two elementary escapes from WP380. A complex-contour
Hubbard--Stratonovich identity represents the positive penalty but requires a
new contour and physical recovery map. A real Lagrange multiplier also gives
the positive sign, but embeds the complete flavor residual in its constraint
and has an indefinite auxiliary Hessian. Both are representations rather than
independent source-derived selectors.

## Radiative-contact authority audit: WP382

- `flavor-radiative-contact-authority.md`
- `checkers/wp382_radiative_contact_authority.py`
- `results/wp382_radiative_contact_authority.json`

WP382 finds that a one-loop invariant mass threshold generates an exact
`F^2` running law but not a scheme-independent positive coefficient. The loop
curvature changes sign across the matching scale, statistics reverses it, and
a finite counterterm remains free. Radiative generation therefore becomes a
selector only after a physical subtraction observable or UV boundary theorem
fixes the contact before flavor readout.

## Physical-subtraction instrument audit: WP383

- `flavor-physical-subtraction-instrument.md`
- `checkers/wp383_physical_subtraction_instrument.py`
- `results/wp383_physical_subtraction_instrument.json`

WP383 removes WP382's scheme ambiguity by calibrating one invariant vertex
value and deriving scheme-independent momentum transport. The calibration
identifies but does not predict the finite boundary class. Moreover, the
formal local contact has field degree 48, so physical authority still requires
an executable composite-channel instrument or a derived lower-point matching
map.

## Reference-probe compression audit: WP384

- `flavor-reference-probe-compression.md`
- `checkers/wp384_reference_probe_compression.py`
- `results/wp384_reference_probe_compression.json`

WP384 constructs a two-point relational readout of the composite flavor
channel. A calibrated nonzero mixing reconstructs the channel kernel, but an
uncalibrated port has the exact normalization kernel
`(h,D_F)~(s*h,s^2*D_F)`. The detector valence falls while the microscopic
mixing remains field degree 25, so the new stabilizer-groupoid experiment is a
conditional separator rather than a source selector.

## Factor-port branch geometry: WP385

- `flavor-factor-port-branch-geometry.md`
- `checkers/wp385_factor_port_branch_geometry.py`
- `results/wp385_factor_port_branch_geometry.json`

WP385 factors the degree-24 residual into two degree-12 invariant branch
coordinates, lowering each probe interface to field degree 13. Two labelled
ports separate the branches, but independent positive factor penalties select
their intersection rather than the original union. Restoring exact shell
equivalence through the product restores field degree 48.

## Binary branch carrier: WP386

- `flavor-binary-branch-carrier.md`
- `checkers/wp386_binary_branch_carrier.py`
- `results/wp386_binary_branch_carrier.json`

WP386 opens a lower-degree conditional selector. A binary CP-odd carrier with
branch penalty `(C-s*beta*D)^2` preserves the two-branch shell under classical
minimization and lowers the positive operator degree from 48 to 24. Finite
thermal summation instead lifts every nonzero shell branch, so a
zero-temperature or superselection preparation law and the value of `beta`
still require independent source authority.

## Continuous CP-odd carrier: WP387

- `flavor-continuous-cp-carrier.md`
- `checkers/wp387_continuous_cp_carrier.py`
- `results/wp387_continuous_cp_carrier.json`

WP387 realizes WP386's binary carrier as two stable vacua of a continuous
CP-odd double-well field. The joint positive potential has exactly the desired
two projected shell branches and a positive-definite vacuum Hessian. The
construction is still conditional: it inserts `beta` and mixed operators of
field degree 25 and 26 rather than deriving them microscopically.

## Quartic arithmetic-circuit completion: WP388

- `flavor-quartic-arithmetic-circuit.md`
- `checkers/wp388_quartic_arithmetic_circuit.py`
- `results/wp388_quartic_arithmetic_circuit.json`

WP388 proves that positive auxiliary multiplication gates can compile a
high-degree polynomial shell into a stable potential of degree at most four
with the same projected zero set. This removes degree as an absolute
algebraic obstruction, but not source authority: changing one equally healthy
terminal gate changes the selected shell. An equivariant gate grammar must be
derived independently rather than compiled from the desired answer.

## CP rank-one saturation gate: WP389

- `flavor-cp-rank-one-saturation.md`
- `checkers/wp389_cp_rank_one_saturation.py`
- `results/wp389_cp_rank_one_saturation.json`

WP389 classifies the general CP-invariant quadratic portal. A nontrivial shell
appears only at the rank-one boundary `kappa^2=4*a*b`; generic stable
coefficients select only the intersection. The sign of `kappa` is a carrier
label before branch calibration, but saturation and the magnitude ratio
remain genuine unauthorized source data.

## Single causal channel rank theorem: WP390

- `flavor-single-causal-channel-rank.md`
- `checkers/wp390_single_causal_channel_rank.py`
- `results/wp390_single_causal_channel_rank.json`

WP390 gives a structural explanation of WP389 saturation. One positive shared
source channel induces an outer-product Gram matrix and hence forces rank one.
Two channels have determinant equal to the positive susceptibility product
times their squared coupling-vector wedge. Any noncollinear completion lifts
the shell kernel; channel uniqueness and the coupling ratio remain the live
source and instrument gates.

## Cross-context channel coherence: WP391

- `flavor-cross-context-channel-coherence.md`
- `checkers/wp391_cross_context_channel_coherence.py`
- `results/wp391_cross_context_channel_coherence.json`

WP391 strengthens WP390 from per-context rank one to a common-channel
coherence theorem. Two individually rank-one contexts share one causal middle
object only when their transported coupling vectors are collinear. Unequal
anomalous dimensions rotate a nontrivial two-component channel, yielding an
independent cross-scale falsifier even though instantaneous rank remains one.

## DPC multiplicity attack: WP392

- `flavor-dpc-multiplicity-attack.md`
- `checkers/wp392_dpc_multiplicity_attack.py`
- `results/wp392_dpc_multiplicity_attack.json`

WP392 falsifies the stated multiplicity-one DPC implication. One CP-odd source
line can map into two CP-odd response copies through a two-dimensional
intertwiner space, leaving the coupling ratio arbitrary and allowing
symmetry-preserving RG rotation. The correct gate is one-dimensional
`Hom_G(L,R)` plus commutant preservation and a calibrated physical embedding.

## Post-hoc symmetry attack: WP393

- `flavor-posthoc-symmetry-attack.md`
- `checkers/wp393_posthoc_symmetry_attack.py`
- `results/wp393_posthoc_symmetry_attack.json`

WP393 proves that every nonzero response ray admits a custom `Z2` reflection
whose fixed intertwiner space is one-dimensional. The revised DPC is therefore
explanatorily empty if its symmetry, metric, or embedding is chosen after the
flavor target. Those objects must be frozen from independent source dynamics
before the physical16 direction is revealed.

## Spectator-extension attack: WP394

- `flavor-spectator-extension-attack.md`
- `checkers/wp394_spectator_extension_attack.py`
- `results/wp394_spectator_extension_attack.json`

WP394 shows that preregistration alone does not make the WP393 symmetry hard
to vary. The extensions `S_v direct-sum +1` and `S_v direct-sum -1` agree on
all flavor predictions and disagree on spectator parity. A viable constructor
must therefore predict an independently testable action outside the flavor
target used to define its protected ray.

## Spectator probe tower: WP395

- `flavor-spectator-probe-tower.md`
- `checkers/wp395_spectator_probe_tower.py`
- `results/wp395_spectator_probe_tower.json`

WP395 computes the eight-element extension fiber for three labelled spectator
parities. Central readouts remain nonfaithful, while the complete labelled
subset-parity tower is the invertible Walsh transform. This conditionally
repairs constructor identification but not selection: the source must predict
the spectator record before the probes read it.

## Lookup-selector no-go: WP396

- `flavor-lookup-selector-no-go.md`
- `checkers/wp396_lookup_selector_no_go.py`
- `results/wp396_lookup_selector_no_go.json`

WP396 proves that complete contextual faithfulness plus simple positive
selection remains non-explanatory. Every one of the eight spectator records
is the unique minimum of an isomorphic Hamming potential with identical norm
and spectrum. A viable DPC must derive selector coefficients before the record
and entail an independent outcome not used to construct them.

## Withheld-context attack: WP397

- `flavor-withheld-context-attack.md`
- `checkers/wp397_withheld_context_attack.py`
- `results/wp397_withheld_context_attack.json`

WP397 shows that any finite aligned context set admits a higher-degree
noncollinear completion invisible on the tested points. Three contexts exclude
quadratic rotation only after a degree-at-most-two source grammar is frozen;
a cubic completion survives and fails at the next context. Universal channel
claims therefore need source-bounded context dependence and a withheld
executable prediction.

## Auxiliary-depth attack: WP398

- `flavor-auxiliary-depth-attack.md`
- `checkers/wp398_auxiliary_depth_attack.py`
- `results/wp398_auxiliary_depth_attack.json`

WP398 compiles WP397's cubic invisible completion with two stable quartic
auxiliary gates. A local degree bound therefore does not bound effective
context dependence when field count and circuit depth remain open. A decisive
withheld test requires a source-derived finite mediator grammar, not merely a
maximum local operator degree.

## Finite grammar identification: WP399

- `flavor-finite-grammar-identification.md`
- `checkers/wp399_finite_grammar_identification.py`
- `results/wp399_finite_grammar_identification.json`

WP399 gives a positive finite-test architecture for a frozen one-pole response
grammar. Three generic contexts identify its three coefficients exactly and a
fourth predicts an out-of-sample response. A cubic hidden completion matches
the calibration records and fails at the withheld context, demonstrating both
the power and the source-relative scope of the test.

## One-mediator response grammar: WP400

- `flavor-one-mediator-response-grammar.md`
- `checkers/wp400_one_mediator_response_grammar.py`
- `results/wp400_one_mediator_response_grammar.json`

WP400 realizes WP399's one-pole response with one stable real mediator whose
curvature and tadpole shift affinely under a common context knob. Three
settings identify the source packet and a fourth tests the locked transport
law. The remaining authority gate is a real flavor mediator and calibrated
operation producing those linked shifts without omitted corrections.

## Two-readout knob calibration: WP401

- `flavor-two-readout-knob-calibration.md`
- `checkers/wp401_two_readout_knob_calibration.py`
- `results/wp401_two_readout_knob_calibration.json`

WP401 supplies a rank-two detector map for independent mediator-curvature and
tadpole errors. Displacement alone has an exact first-order kernel, while the
joint pole-curvature and displacement readouts have positive Jacobian and
weighted Gram determinants. The instrument tests WP400's locked knob but does
not source-predict its slope.

## Completed mediator grammar audit: WP402

- `flavor-completed-mediator-grammar.md`
- `checkers/wp402_completed_mediator_grammar.py`
- `results/wp402_completed_mediator_grammar.json`

WP402 adds quadratic curvature and tadpole corrections, affine finite width,
and an optional extra pole to WP400. Four static contexts leave one static
kernel and are exactly blind to width. Two absorptive contexts repair the
affine-width kernel, while an extra pole mass remains unobservable at zero
residue. A completion-safe withheld protocol therefore requires both static
and dynamic calibrated probes.

## Completion-safe context design: WP403

- `flavor-completion-safe-context-design.md`
- `checkers/wp403_completion_safe_context_design.py`
- `results/wp403_completion_safe_context_design.json`

WP403 replaces displacement-only calibration by three joint
curvature-displacement contexts, two absorptive contexts, and two residual
extra-pole spectral points. The staged Jacobians are full rank on the declared
nonzero-residue completion domain and generate three frozen withheld
predictions. Physical binding to an executable trace-adjoint mediator knob
remains open.

## Probe-context versus source-knob typing: WP404

- `flavor-probe-source-knob-typing.md`
- `checkers/wp404_probe_source_knob_typing.py`
- `results/wp404_probe_source_knob_typing.json`

WP404 proves that collider energy, reconstructed mass, cuts, and luminosity
cannot be promoted to WP403's source knob merely because they change a measured
response. The dynamic readout varies with probe frequency while the source
packet has identically zero Jacobian with respect to that scan. The formal
affine knob does change both curvature and tadpole, and the joint readout
calibrates their independent errors, but no admitted apparatus map currently
implements it. The physical binding gate therefore remains open without a
coordinate shortcut.

## No-refit precommitment: WP405

- `flavor-no-refit-precommitment.md`
- `checkers/wp405_no_refit_precommitment.py`
- `results/wp405_no_refit_precommitment.json`

WP405 freezes the completed nine-parameter benchmark, calibration contexts,
three withheld contexts, exact predictions, and rejection rule under one
canonical SHA-256 digest. A failed reserved record rejects the packet without
refitting or appending a correction. This supplies prospective test integrity,
not the physical apparatus map into WP403's formal source knob.

## Executable neutral-kaon regenerator knob: WP406

- `flavor-kaon-regenerator-knob.md`
- `checkers/wp406_kaon_regenerator_knob.py`
- `results/wp406_kaon_regenerator_knob.json`

WP406 identifies a real flavor intervention rather than another collider
coordinate. Material column density changes the dispersive and absorptive parts
of the neutral-kaon forward-scattering operator through one complex amplitude.
The exact finite-thickness transfer law includes decay widths and repeated
coherent interactions; density points zero, one, and two test the first
quadratic source correction, while an extra material species is a declared
second source direction. A triple-density regenerated displacement is reserved
without refitting. This is a real relational kaon experiment, not a selector
on the quark `physical16` quotient; common-frame empirical phase/attenuation
assembly and execution of the reserved density remain.

## CPLEAR common-knob complex calibration: WP407

- `flavor-cplear-common-knob-calibration.md`
- `checkers/wp407_cplear_common_knob_calibration.py`
- `results/wp407_cplear_common_knob_calibration.json`

WP407 imports the five published CPLEAR carbon-regeneration measurements of
the real and imaginary forward-amplitude difference, including uncertainties
and correlations. Every reconstructed covariance is rank two and both response
components are nonzero. This empirically closes the same-knob dispersive and
absorptive calibration gate for a real flavor system. The absent/present
absorber design cannot test a quadratic density term; three certified densities
plus a fourth withheld displacement remain the decisive successor experiment.

## Four-thickness kaon no-refit protocol: WP408

- `flavor-four-thickness-kaon-protocol.md`
- `checkers/wp408_four_thickness_kaon_protocol.py`
- `results/wp408_four_thickness_kaon_protocol.json`

WP408 freezes an executable $0,t,2t$ carbon calibration with a sealed $3t$
record. The three open settings identify the first quadratic density correction,
and exact interpolation predicts the withheld complex displacement with weights
$(1,-3,3)$. Full covariance is propagated into a predeclared Mahalanobis test.
Finite widths and nonlinear propagation come from WP406; extra material species
must be assayed away or separately calibrated. No qualifying historical
four-thickness dataset has been located, so execution remains open.

## E773 two-thickness no-refit gate: WP409

- `flavor-e773-two-thickness-gate.md`
- `checkers/wp409_e773_two_thickness_gate.py`
- `results/wp409_e773_two_thickness_gate.json`

WP409 audits the completed Fermilab E773 experiment. Its 40 cm and 61 cm active
regenerators prove that multi-setting finite-width kaon interference is
executable, but their quadratic thickness design has rank two and one exact
kernel. E773 also lacked a vacuum input-spectrum beam and floated two flux
parameters, so the second setting was not predicted from the first without
refitting. It therefore strengthens the physical architecture while leaving
WP408's source-off, multi-setting, sealed-record gate open.

## Pre-CPLEAR optical-model withheld test: WP410

- `flavor-pre-cplear-withheld-test.md`
- `checkers/wp410_pre_cplear_withheld_test.py`
- `results/wp410_pre_cplear_withheld_test.json`

WP410 tests four complex 1994 optical-model predictions against the later CPLEAR
carbon-regeneration measurement with the published correlated covariances and
zero refitted parameters. The global statistic is 14.725 for eight components,
below the 5% critical value 15.507, while one low-momentum bin supplies a sharp
local tension. This is a chronologically genuine retrospective withheld flavor
displacement, not a prospective blind run and not a `physical16` selector.
Independence of the optical-model inputs and its nuclear completion assumptions
remain under hostile audit.

## Kaon-to-scalar transport gate: WP411

- `flavor-kaon-scalar-transport-gate.md`
- `checkers/wp411_kaon_scalar_transport_gate.py`
- `results/wp411_kaon_scalar_transport_gate.json`

WP411 prevents transport of WP406--WP410's real kaon success into WP400's
scalar-tadpole objective. Homogeneous kaon propagation fixes the zero state;
a nonzero scalar tadpole moves it, and linear conjugacy preserves this
difference. Homogenizing the affine scalar operation requires a constant
reference coordinate, which is a new source port and groupoid. The kaon branch
therefore supplies a genuine withheld flavor prediction but does not close the
original real-scalar common-shift gate.

## Higgs relative-tadpole reference port: WP412

- `flavor-higgs-reference-port.md`
- `checkers/wp412_higgs_reference_port.py`
- `results/wp412_higgs_reference_port.json`

WP412 returns to the scalar objective using the observed Higgs radial mode.
Gauge invariance forbids an absolute linear doublet source, but a
gauge-invariant mass deformation produces affine curvature and relative-tadpole
shifts when the original broken vacuum is retained as a reference port. The
same knob tangent is $(1,v_0)^T$; recentering removes the tadpole exactly. This
is a new relational experiment over the reference stabilizer groupoid. No
executable physical operation varying the Higgs mass term has yet been admitted.

## Higgs context-knob reach gate: WP413

- `flavor-higgs-knob-reach-gate.md`
- `checkers/wp413_higgs_knob_reach_gate.py`
- `results/wp413_higgs_knob_reach_gate.json`

WP413 audits thermal, curvature, and portal implementations of WP412's Higgs
mass deformation. Early-Universe thermodynamics has source and Higgs-response
authority but is not executable; heavy-ion fireballs are executable but lack a
Higgs curvature/displacement instrument. Their central temperature scales
differ by more than 348, and their valid arrows cannot be composed without a
named common-frame interface. Curvature and new-portal backgrounds likewise
fail the executable-instrument gate.

## Higgs retained-reference response-rank gate: WP414

- `flavor-higgs-response-rank-gate.md`
- `checkers/wp414_higgs_response_rank_gate.py`
- `results/wp414_higgs_response_rank_gate.json`

WP414 separates multiple readouts from multiple causal controls. The Higgs
curvature and retained-reference tadpole have the positive one-knob information
$w_H+v_0^2w_J$, but their source Jacobian has rank one. Duplicating the knob as
two source stories leaves the exact kernel $(-1,1)$ and a zero weighted Gram
determinant. An executable Higgs mass knob would therefore test one common-shift
law, not identify two source errors; a nonproportional second source operation
is still required.

## Counterfactual second-intervention gate: WP415

- `flavor-counterfactual-intervention-gate.md`
- `checkers/wp415_counterfactual_intervention_gate.py`
- `results/wp415_counterfactual_intervention_gate.json`

WP415 states the current Deutsch-Popperian conjecture as an exact experimental
gate. For a two-source, two-readout Jacobian, the positive weighted Gram
determinant is $w_Hw_J(ad-bc)^2$. Against WP412's Higgs response $(1,v_0)^T$,
a proposed second operation is distinguishing only through the wedge
$q-v_0p$, and its calibrated uncertainty interval must exclude zero. This rank
criterion is necessary but does not supply source, execution, instrument, or
precommitment authority.

## Higgs quartic second-source gate: WP416

- `flavor-higgs-quartic-second-source.md`
- `checkers/wp416_higgs_quartic_second_source.py`
- `results/wp416_higgs_quartic_second_source.json`

WP416 finds the minimal source-derived second direction: independently deform
the gauge-invariant Higgs quartic while retaining WP412's broken-vacuum
reference. Together with the quadratic deformation, the curvature/tadpole
Jacobian has determinant $-2v_0^3$ and positive weighted Gram determinant
$4v_0^6w_Hw_J$. The two source errors are therefore exactly reconstructible in
the broken phase and descend independently of quark weak-basis charts. The
remaining obstruction is physical: the Higgs quartic is measured but is not an
executable laboratory control.

## Higgs quartic measurement-versus-actuation audit: WP417

- `flavor-higgs-quartic-instrument-audit.md`
- `checkers/wp417_higgs_quartic_instrument_audit.py`
- `results/wp417_higgs_quartic_instrument_audit.json`

WP417 admits the first ATLAS triple-Higgs search as a real quartic-sensitive
measurement channel, while separating it from source actuation. Beam energy,
luminosity, selection, and simulation reweighting change the sampling or
analysis map but have zero command-to-$\kappa_4$ source Jacobian. A genuine
actuator requires an observed coupling from an independently commanded setting
to the Higgs quartic, followed by the common-frame WP412 readouts. No such
Standard Model apparatus is presently admitted.

## Analogue Higgs control domain gate: WP418

- `flavor-analogue-higgs-domain-gate.md`
- `checkers/wp418_analogue_higgs_domain_gate.py`
- `results/wp418_analogue_higgs_domain_gate.json`

WP418 identifies a realized relational Higgs-mode instrument in an iron-based
superconductor: phase-locked THz pulses execute a control and coherent
spectroscopy reads the amplitude response. It does not actuate the Standard
Model Higgs quartic. The material and electroweak fields occupy different
source domains, and no admitted interface maps the THz command to
$\kappa_4^{\mathrm{SM}}$. Cold-atom lattice gauge–Higgs work remains propositional.
The pump/reference/readout architecture transfers; physical authority does not.

## Standard Model quartic-actuator no-go: WP419

- `flavor-sm-quartic-actuator-no-go.md`
- `checkers/wp419_sm_quartic_actuator_no_go.py`
- `results/wp419_sm_quartic_actuator_no_go.json`

WP419 proves that the absent Standard Model quartic actuator is structural. The
quartic operator already has dimension four, so a renormalizable physical
multiplier must be a dimension-zero Lorentz-scalar gauge-singlet dynamical
field. No such field occurs in the Standard Model. The first Higgs-built
singlet multiplier produces $(H^\dagger H)^3$ at dimension six. A real actuator
therefore requires a new singlet/modulus, a physically prepared external
coupling field, or an observed controllable EFT source; each enlarges the
admitted theory.

## Fixed-law Higgs-quartic constructor: WP420

- `flavor-fixed-law-quartic-constructor.md`
- `checkers/wp420_fixed_law_quartic_constructor.py`
- `results/wp420_fixed_law_quartic_constructor.json`

WP420 repairs the task typing exposed by WP419. A fixed EFT interaction
$-(g/\Lambda)S(H^\dagger H)^2$ lets an apparatus command the prepared singlet
state $s=\langle S\rangle$, giving
$\partial\lambda_{\mathrm{eff}}/\partial s=g/\Lambda$. Together with the quadratic
source, its relational response wedge is $-2gv_0^3/\Lambda$. This is the minimal
fixed-law constructor and has exact zero-coupling, equal-setting, and decoupling
falsifiers. It remains conditional until an independently observed, preparable
source substrate and coupling are supplied.

## Yukawa relational core and minimal Ubersector signature: WP421

- `flavor-yukawa-ubersector-signature.md`
- `checkers/wp421_yukawa_ubersector_signature.py`
- `results/wp421_yukawa_ubersector_signature.json`

WP421 centers flavor on the basis-free Yukawa span with shared $Q_L$ port.
Individual Gram spectra give masses; relative eigenflag overlaps give CKM
moduli and signed phase data. An exact hostile pair has equal leg spectra and
different overlap moduli. Six objects, six arrows, and five coherence cells
form the minimal current Ubersector signature. WP232 witnesses the missing
source-detector common-frame cell; WP256 witnesses the missing exact or
uncertainty-authorized RG-to-detector transport cell. An ordinary span suffices
for the flavor core; no larger multicategory is yet forced.

## Electromagnetic Higgs-quartic actuation reach: WP422

- `flavor-em-higgs-quartic-reach.md`
- `checkers/wp422_em_higgs_quartic_reach.py`
- `results/wp422_em_higgs_quartic_reach.json`

WP422 identifies the first existing Standard Model substrate with formal,
source-derived quartic actuation: a commanded non-null electromagnetic
background enters the charged-particle threshold effective action and shifts
the local radial quartic. A single plane wave fails because both field
invariants vanish. A 100.75 T controlled magnetic pulse succeeds algebraically
but, even with a unit loop coefficient, gives a shift below $10^{-36}$; a unit
shift requires over $10^{20}$ T. The source and control arrows exist, but the
common-frame measurable-rank gate remains closed.

## Admission gate

## Hierarchical scalar pole, residue, and width packet: WP475

- `flavor-hierarchical-scalar-residue-packet.md`
- `checkers/wp475_hierarchical_scalar_residue_packet.py`
- `results/wp475_hierarchical_scalar_residue_packet.json`

WP475 recomputes rather than transports the scalar spectrum at WP474's exact kaon-conditioned endpoint. The canonical three-radial Hessian factorizes analytically after a unique positive Higgs-mass calibration of `eta`. The 125.20-GeV pole has Higgs residue indistinguishable from one at the `10^-9` scale; the lifted and heavy radial poles are multi-PeV and closed to Higgs decay. The independently derived leading Higgs width is correspondingly near `4.10 MeV`. This conditional packet is simultaneously compatible with the inherited provisional current endpoint and the Higgs mass, rate, and width instruments, but remains benchmark-calibrated rather than numerically source-selected.

## Kaon-conditioned Higgs alignment: WP474

- `flavor-kaon-conditioned-higgs-alignment.md`
- `checkers/wp474_kaon_conditioned_higgs_alignment.py`
- `results/wp474_kaon_conditioned_higgs_alignment.json`

WP474 composes the provisional WP461 flavor-current constraint with WP473's Higgs-rate cone. At `y=1`, the exact kaon-conditioned lower bound on `f` drives `a=3(v/f)^2` to an upper bound of order `10^-9`, far below the rate ceiling `242/2379`. The lifted dilation pole then carries below `10^-9` Higgs residue, leaving an orthogonal Higgs budget essentially equal to one. Thus the large flavor scale physically repairs the unit-geometry rate obstruction without a new production amplitude. This remains a conditional constraint, not source selection: WP461's kaon likelihood and 5-TeV pole are provisional/frozen inputs, and its `g_F f/v approximately 49.79` remains a benchmark readout.

## Dilation-residue sum rule: WP473

- `flavor-dilation-residue-sum-rule.md`
- `checkers/wp473_dilation_residue_sum_rule.py`
- `results/wp473_dilation_residue_sum_rule.json`

WP473 promotes WP472's rejection to a coefficient-independent projector theorem. The lifted common-dilation pole consumes Higgs residue `2a/(3y^2+2a+1)`, so every other single pole is bounded by the complementary budget `(3y^2+1)/(3y^2+2a+1)`. At unit geometry this ceiling is exactly `2/3`, below the PDG rate gate regardless of radial stiffness retuning. More generally, the rate requires `a <= 121(3y^2+1)/4758` and therefore imposes an exact conditional lower bound on `g_F f/v`; at `y=1` it is about `5.43 g_F`. This constrains rather than source-selects the ratio.

## Higgs rate and leading-width gate: WP472

- `flavor-higgs-rate-width-gate.md`
- `checkers/wp472_higgs_rate_width_gate.py`
- `results/wp472_higgs_rate_width_gate.json`

WP472 tests WP471's unfit residue with a calibrated rate instrument. In the explicitly closed-new-channel, mixing-only domain, the inclusive signal strength equals the frozen Higgs residue, approximately `0.66666555`. The PDG combined-final-state value is `1.03 plus or minus 0.04`, placing the prediction over nine Gaussian standard deviations low and rejecting the calibrated unit-geometry branch. The same response packet independently predicts a leading total width near `2.73333 MeV` from the PDG Standard Model width; the coarse direct width summary remains compatible, but cannot rescue the rate failure. Reopening requires a source-derived production enhancement or different portal geometry and a complete fresh spectral calculation.

## Higgs-mass-calibrated common-clock portal: WP471

- `flavor-higgs-mass-calibrated-portal.md`
- `checkers/wp471_higgs_mass_calibrated_portal.py`
- `results/wp471_higgs_mass_calibrated_portal.json`

WP471 repairs WP470 at the explicitly detector-calibrated level without smearing calibration into source selection. The reconstructed Higgs mass fixes the nuisance portal stiffness uniquely to the positive exact value `1186324514058160/13746755484562347`. The target `g_F f/v=sqrt(3)g_F` is independent of this coordinate. The calibrated radial spectrum factorizes exactly into the 125.20-GeV curvature, the unchanged lifted pole `12`, and one rational heavy pole. Exact projectors predict a Higgs-radial residue about `0.66666555` for the observed pole; this residue was not fit and becomes the next withheld rate/width falsifier.

## Higgs-pole calibration gate: WP470

- `flavor-higgs-pole-calibration-gate.md`
- `checkers/wp470_higgs_pole_calibration_gate.py`
- `results/wp470_higgs_pole_calibration_gate.json`

WP470 attaches the first unavoidable calibrated instrument to WP469. With `v=246.22 GeV`, the three unit-benchmark radial poles with nonzero Higgs residue lie near `423.256`, `603.113`, and `3508.484 GeV`. The 2025 PDG Higgs listing gives `125.20 plus or minus 0.11 GeV`; even the lightest model pole exceeds the frozen 95-percent upper edge by over `298 GeV`. The unit benchmark is therefore physically rejected before widths matter. The relational selector family survives conditionally, but tuning its coefficients to the observed pole would be detector calibration rather than source selection and would require recomputing every residue.

## Source radial lift and updated residue packet: WP469

- `flavor-source-radial-lift-packet.md`
- `checkers/wp469_source_radial_lift.py`
- `results/wp469_source_radial_lift.json`

WP469 repairs WP468's physical massless pole with an independently declared positive radial-norm square. Its Hessian is exactly the rank-one operator `2 d d^T` along the common-dilation tangent `d=(sqrt(3),sqrt(2),1)`. At the unit benchmark it creates one pole with mass squared `12` and diagonal flavor-radial, Higgs-radial, and singlet residues `(1/2,1/3,1/6)`, while orthogonality preserves both pre-existing massive radial poles and residues exactly. The full Hessian now has only eleven gauge-Goldstone zeros and no physical flat direction. The source scale `w` fixes the absolute radius but is not numerically derived; widths and detector authority remain gated on mass-eigenstate vertices and complete open-channel enumeration.

## Common-dilaton Hessian and residue packet: WP468

- `flavor-common-dilaton-hessian-residue-packet.md`
- `checkers/wp468_common_dilaton_hessian.py`
- `results/wp468_common_dilaton_hessian.json`

WP468 freezes the complete 29-real-field tree-level Hessian of WP467 at the independently declared unit coefficient benchmark. Its rank is 17 and its nullity is exactly twelve: eight flavor gauge modes, three electroweak Goldstones, and one physical common dilaton. Every massive curvature is positive, with spectrum `16` of multiplicity eight, `36` of multiplicity seven, and the two mixed radial values `206 plus or minus 2 sqrt(10009)`. Exact polynomial spectral projectors freeze the flavor-radial, Higgs-radial, and singlet residues for the massless and two massive poles. The portal is locally stable, but the physical massless dilaton prevents immediate detector composition; any source-derived lifting must trigger a fresh pole, residue, and width calculation.

## Common-dilaton flavor-clock portal: WP467

- `flavor-common-dilaton-clock-portal.md`
- `checkers/wp467_common_dilaton_clock_portal.py`
- `results/wp467_common_dilaton_clock_portal.json`

WP467 supplies the first explicit source operation that removes WP466's independent flavor/electroweak scale kernel. A positive renormalizable sum-of-squares action makes the WP447 irreducible adjoint triplet and the Higgs norm relational outputs of one dynamical singlet. Its exact global minima obey `g_F f/v=g_F y sqrt(3/a)`, invariant under the remaining common radial dilation. For fixed source coefficients this is a genuine proper-subspace selector on the physical clock ratio, not a texture rigidifier. Numerical selection remains open: the equally symmetric positive coefficient choices `(y,a)=(1,1)` and `(1,3)` give distinct ratios. The common radial scale, enlarged pole spectrum, widths, and calibrated likelihood are also not yet supplied.

## Fixed-point and relevant-deformation separation: WP466

- `flavor-fixed-point-relevant-deformation-separation.md`
- `checkers/wp466_fixed_point_relevant_deformation_separation.py`
- `results/wp466_fixed_point_relevant_deformation_separation.json`

WP466 grants the strongest favorable completion of WP465: a unique perturbative fixed point for every dimensionless gauge, Yukawa, and quartic coupling. Even then a common positive dilation of the WP447 scale and both WP435 messenger masses preserves the full fixed-point record and all messenger-to-flavon threshold ratios while multiplying `g_F f/v` by the dilation. The exact hostile pair `s=1,2` therefore differs by a factor of two in the target. A coupled fixed point may select `g_F`; it cannot select the requested physical clock ratio without a source-derived relevant trajectory or independently fixed electroweak–flavor portal.

## Messenger-assisted fixed-point threshold gate: WP465

- `flavor-messenger-fixed-point-threshold-gate.md`
- `checkers/wp465_messenger_fixed_point_threshold_gate.py`
- `results/wp465_messenger_fixed_point_threshold_gate.json`

WP465 finds a genuine weak-coupling window and its exact composition obstruction. Above both WP435 messenger thresholds, twelve Dirac fundamentals plus the three real adjoints give `b0=3/2`, `b1=-113`, and the formal gauge-only root `alpha_F=6*pi/113`, with loop coordinate only `3/226`. But the nonzero messenger masses required for Yukawa matching decouple six fundamentals. At the proposed high-spectrum root, the resulting low-spectrum beta bracket is exactly `566/113`, not zero. The massive theory therefore does not select the coupling at the physical pole without threshold ratios and a trajectory. Keeping messengers active instead invalidates WP449's quark-only width domain. The branch remains promising only after a full gauge-Yukawa fixed point, threshold matching, and all-open-channel spectral packet are derived together.

## Two-loop gauge fixed-point gate: WP464

- `flavor-two-loop-gauge-fixed-point-gate.md`
- `checkers/wp464_two_loop_gauge_fixed_point_gate.py`
- `results/wp464_two_loop_gauge_fixed_point_gate.json`

WP464 tests whether the declared `SU(3)_F` gauge dynamics selects `g_F`. For six Dirac fundamentals and three real adjoint scalars, the gauge-only coefficients are exactly `b0=11/2` and `b1=-37`, yielding the formal two-loop root `g_F^2=88*pi^2/37`. At that root WP449's leading pole ratio is `Gamma/M=22*pi/37>1`. The root is therefore outside the weak-coupling and narrow-pole domain and cannot be composed with the admitted detector packets. The flow descends under weak basis transformations, but it supplies neither an admissible selector nor a presentation rigidifier. A controlled nonperturbative or gauge-Yukawa fixed point inside a separately validated response domain would be needed to reopen this branch.

## Run-2 production-rate reach: WP463

- `flavor-run2-production-rate-reach.md`
- `checkers/wp463_run2_production_rate_reach.py`
- `results/wp463_run2_production_rate_reach.json`

WP463 executes WP462's source-specific parton channel against the ATLAS Run-2 domain. The official NNPDF2.3 LO central (d anti-s plus s anti-d) luminosity at a 5 TeV pole is (0.00117857); the maximum of all 100 replicas is (0.00611735). At WP461's conditional coupling endpoint, even that hostile maximum gives a unit-acceptance cross section below (9.90 times 10^-6 fb) and fewer than (1.38 times 10^-3) produced events in (139 inverse fb). This is over 8000 below the optimistic (0.08 fb) endpoint of ATLAS's quoted high-mass generic sensitivity. The rate map is faithful algebraically, but finite luminosity collapses all kaon-allowed points to the background-only operational class. Run 2 cannot restore the second parameter coordinate.

## Positive production-rate portal: WP462

- `flavor-positive-production-rate-portal.md`
- `checkers/wp462_positive_production_rate_portal.py`
- `results/wp462_positive_production_rate_portal.json`

WP462 replaces WP461's detector-erased width coordinate with a source-derived positive production coordinate. For the WP453 hostile transition, the signed Delta-F=2 residues are (-1/4,+1/4), but the collider sesquilinear weights are (+1/4,+1/4); on-shell production does not inherit the low-energy cancellation. The summed down-strange entrance width per multiplet is (g_F^2 m_r/(8 pi)). Conditional on a calibrated positive detector factor, the map from (g_F,mu) to triplet mass and event yield has determinant (-kappa_detector g_F^2/2) and rank two. This is formal source support, not yet reach: the flavor-changing parton luminosity, normalization, acceptance, efficiency, luminosity, and background likelihood remain to be frozen.

## Kaon-conditioned pole-width reach: WP461

- `flavor-kaon-conditioned-pole-width-reach.md`
- `checkers/wp461_kaon_conditioned_pole_width_reach.py`
- `results/wp461_kaon_conditioned_pole_width_reach.json`

WP461 tests WP457's formal mass-plus-width identification against a real detector scale. At a frozen 5 TeV triplet benchmark, a hostile envelope spanning the displayed 5 and 100 TeV SMEFT-Atlas response factors and WP460's provisional positive endpoint gives conditional working limits (g_F<9.46 times 10^-4), (mu>5.29 times 10^3 TeV), and (f>1.30 times 10^4 TeV). WP449 then gives a triplet width below (3.56 times 10^-4 GeV). ATLAS's approximate 3 percent dijet resolution is 150 GeV at that mass and treats narrower signals as zero-width templates, exceeding the source width by over (4.2 times 10^5). Detector convolution therefore deletes the width coordinate and reduces the proposed rank-two readout to at most rank one. The benchmark value (g_F f/v approximately 49.79) is a pole-mass readout, not source selection.

## Provisional CP-even kaon likelihood: WP460

- `flavor-provisional-deltamk-likelihood.md`
- `checkers/wp460_provisional_deltamk_likelihood.py`
- `results/wp460_provisional_deltamk_likelihood.json`

WP460 conditionally repairs WP459's real-ray likelihood kernel. It combines the preliminary RBC/UKQCD result (5.8 plus or minus 0.6 statistical plus or minus 2.3 systematic) with the quoted experimental (3.484 plus or minus 0.006), all in units of (10^-12 MeV). Under an explicit independent-Gaussian treatment of the estimated lattice systematic, the normalized real BSM coordinate has center (-579/871), standard deviation (sqrt(1412509)/1742), and nonzero response rank. The working 1.96-sigma interval is approximately (-2.002,0.673), including zero. This is an executable provisional likelihood, not yet an admitted WP447 bound: the systematic PDF is added by WP460, the lattice result is preliminary, and pole-by-pole matching remains open.

## Executable kaon-likelihood kernel: WP459

- `flavor-executable-kaon-likelihood-kernel.md`
- `checkers/wp459_executable_kaon_likelihood_kernel.py`
- `results/wp459_executable_kaon_likelihood_kernel.json`

WP459 attaches a real version-pinned likelihood surface and locates its kernel. `flavio` 2.7.0 registers `eps_K` with the bundled PDG kaon-CPV Gaussian measurement but no `DeltaM_K` likelihood. A real WET correlated probe (CVLL,CVRR,CVLR)=a(1,1,2) leaves the executable `eps_K` prediction exactly equal to the Standard Model value, whereas the imaginary companion produces a large response. The executable likelihood therefore detects the CP-odd direction but collapses WP453's real current direction. The missing physical instrument is an independently frozen CP-even kaon likelihood, not further operator algebra.

## Two-axis flavor-scale selector audit: WP458

- `flavor-two-axis-scale-selector-audit.md`
- `checkers/wp458_two_axis_scale_selector_audit.py`
- `results/wp458_two_axis_scale_selector_audit.json`

WP458 attacks numerical selection of (g_F f/v) directly. The admitted theory leaves both (g_F) and (mu/v) free, while current, pole, and width probes constrain or identify realized values without reducing the source-label domain. A minimal scale-invariant singlet portal removes radial-state dilation but yields (g_F f/v=g_F kappa sqrt(3c)), retaining three product-changing theory labels. On the admitted light spectrum, the one-loop (SU(3)_F) coefficient is exactly (b_0=11/2), so perturbative running has no positive finite one-loop fixed point. The present architecture therefore contains a faithful formal readout but no numerical source selector; a successor must fix the gauge normalization and relational portal product through one declared source law.

## Pole-clock parameter identifiability: WP457

- `flavor-pole-clock-parameter-identifiability.md`
- `checkers/wp457_pole_clock_parameter_identifiability.py`
- `results/wp457_pole_clock_parameter_identifiability.json`

WP457 proves that the formal pole mass and fractional width jointly identify the two positive source parameters: the Jacobian from (g_F,mu) to (m_1,Gamma_1/m_1) has determinant (-g_F^2/(2 pi)) and hence rank two. The requested product is directly readable as (g_F f/v=sqrt(6)m_1/v), while the width separates (g_F) from (mu). Quintet-to-triplet mass and width ratios both equal (sqrt3), furnishing overidentifying source tests. This is a formal parameter readout, not numerical source selection; detector-calibrated flavor-tagged reach remains open.

## Pole-resolved flavor-current complement: WP456

- `flavor-pole-resolved-current-complement.md`
- `checkers/wp456_pole_resolved_current_complement.py`
- `results/wp456_pole_resolved_current_complement.json`

WP456 resolves WP453's hostile transition across WP448's two independently frozen pole projectors. The triplet and quintet Delta-F=2 bilinear residues are exactly (-1/4) and (+1/4): their leading high-energy sum cancels, while inverse-mass weighting gives (-1/6), exactly reproducing the low-energy current coefficient. The two pole neighborhoods are therefore a source-derived complementary probe family. WP449's fixed widths are legal only near the poles; extending them to zero momentum produces a spurious imaginary Wilson coefficient and is explicitly rejected. A flavor-tagged detector response and reach remain open.

## Correlated neutral-kaon response constructor: WP455

- `flavor-correlated-kaon-response-constructor.md`
- `checkers/wp455_correlated_kaon_response_constructor.py`
- `results/wp455_correlated_kaon_response_constructor.json`

WP455 repairs WP454's operator-interface failure at the response-map level. In the published colorless-vector SMEFT Atlas at 5 TeV, freezing the source restriction (z_q^{12}=z_d^{12}=z) and all other couplings to zero gives the exact displayed contraction (-5,264,000 z^2) in the normalized kaon mixing amplitude. The vectorlike ray is therefore not in the response kernel, and the LR contribution changes the result by the exact ratio (-2632/9) relative to either same-chirality term. This is a common-frame causal response, neither selector nor rigidifier. A covariance-bearing complex-amplitude likelihood including Standard Model long-distance uncertainty remains required before admitting a numerical WP447 exclusion.

## Neutral-kaon instrument interface gate: WP454

- `flavor-kaon-instrument-interface-gate.md`
- `checkers/wp454_kaon_instrument_interface_gate.py`
- `results/wp454_kaon_instrument_interface_gate.json`

WP454 attaches the real neutral-kaon instrument class but rejects a direct numerical constraint from the available PDG excerpt. The vectorlike source fixes the correlated chiral coefficient ray (1,1,2), while the displayed PDG illustration reads only the isolated LL axis and has a two-dimensional kernel on that packet. A formal projected scale diagnostic is recorded but not admitted as a model bound. Closure requires correlated RG evolution, lattice covariance, and experimental likelihood in one operator convention.

## Flavor-current orientation fiber: WP453

- `flavor-current-orientation-fiber.md`
- `checkers/wp453_current_orientation_fiber.py`
- `results/wp453_current_orientation_fiber.json`

WP453 exhibits an exact hostile fiber after WP450. Two Yukawa pairs related by common conjugation have identical spectra and CKM record and are both realized by the universal messenger grammar, but at fixed WP447 flavon vacuum their exact (Delta F=2) current coefficients are (0) and (-1/6) before the common scale factor. The WP448 current family therefore resolves extended-theory orientation erased by Standard Model physical16 data. Neutral-meson mixing is the relevant instrument class, but calibrated constraints still require selected orientation, RG evolution, and hadronic matching.

## Dynamical coefficient-representation census: WP452

- `flavor-coefficient-representation-census.md`
- `checkers/wp452_coefficient_representation_census.py`
- `results/wp452_coefficient_representation_census.json`

WP452 identifies the minimal covariant dynamical coefficient content after WP451. Under the source (SO(3)), the spin-one matrix algebra decomposes exactly as singlet plus triplet plus quintet, with dimensions one, three, and five and pairwise orthogonal matrix bases. A triplet alone has equally spaced eigenvalues and CP-real relative frames. Generic complex flavor therefore needs dynamical singlet, triplet, and quadrupole coefficient fields per sector, or an independently justified smaller selector action; the census itself selects no values.

## Triplet-symmetry selector obstruction: WP451

- `flavor-triplet-symmetry-selector-obstruction.md`
- `checkers/wp451_triplet_symmetry_selector_obstruction.py`
- `results/wp451_triplet_symmetry_selector_obstruction.json`

WP451 applies WP447's own oriented-(SO(3)) source symmetry to WP450's messenger coefficients. There is no invariant degree-one coefficient vector, and the only invariant rank-two tensor is (delta_ij), whose spin-one Casimir gives a flavor-universal identity Yukawa. Preserving the source symmetry therefore erases flavor; arbitrary coefficients restore fitting capacity only by importing new symmetry-breaking sources. A successor must make those coefficient sources dynamical rather than treating them as selected constants.

## Irreducible-vacuum messenger word grammar: WP450

- `flavor-messenger-word-grammar.md`
- `checkers/wp450_messenger_word_grammar.py`
- `results/wp450_messenger_word_grammar.json`

WP450 freezes the finite messenger grammar over WP447. Identity and linear words span only four complex matrix directions, while words through degree two span all nine; an explicit nine-word basis gives a bijective coefficient map and reconstructs the hostile (E13) entry exactly. This repairs physical16 support at finite messenger depth but is not a selector: nine arbitrary complex coefficients per Yukawa reproduce every literal matrix, leaving their values and the physical current orientation unsourced.

## Irreducible-triplet width packet: WP449

- `flavor-triplet-width-packet.md`
- `checkers/wp449_triplet_width_packet.py`
- `results/wp449_triplet_width_packet.json`

WP449 adds independently frozen conditional widths to WP448's residues. In the declared quark-only, above-top, messenger/flavon-decoupled perturbative domain, the inclusive generation trace gives the common leading ratio (Gamma/M=g_F^2/(4pi)). The triplet and quintet widths therefore scale in the exact pole-mass ratio. The result is not detector-calibrated and is invalid as soon as any frozen threshold assumption fails.

## Irreducible-triplet pole and residue packet: WP448

- `flavor-triplet-pole-residue-packet.md`
- `checkers/wp448_triplet_pole_residue_packet.py`
- `results/wp448_triplet_pole_residue_packet.json`

WP448 independently freezes the spectral data supplied by WP447 before any detector fit. The eight flavor gauge bosons split into a mass-one triplet and mass-squared-three quintet in units of (g_F^2 mu^2). Exact rank-three and rank-five projector residues give a two-pole propagator, and the low-energy kernel again cancels (g_F). Widths remain deliberately undefined until the particle spectrum, open channels, and mass-basis transport are declared.

## Irreducible adjoint-triplet flavon vacuum: WP447

- `flavor-irreducible-adjoint-triplet.md`
- `checkers/wp447_irreducible_adjoint_triplet.py`
- `results/wp447_irreducible_adjoint_triplet.json`

WP447 replaces post-hoc matrix-entry repair with a positive representation constraint. Three dynamical adjoints are forced into the irreducible spin-one (su(2)) representation inside (su(3)); the reducible two-plus-one representation has exact positive energy. The global vacuum word algebra is all of (M3(C)), gauge rank is eight, and the complete 24-component Hessian has exactly eight gauge zeros and sixteen positive physical modes. This removes WP446's invariant-subspace obstruction, but supplies only physical16 capacity: messenger coefficients and the absolute ratio (g_Ff/v) remain unselected.

## Messenger-to-physical16 obstruction: WP446

- `flavor-messenger-physical16-obstruction.md`
- `checkers/wp446_messenger_physical16_obstruction.py`
- `results/wp446_messenger_physical16_obstruction.json`

WP446 tests the common-frame gate before attaching experiments to WP445. The associative algebra generated by the WP443 vacuum preserves an exact two-plus-one generation decomposition, so every admitted messenger Yukawa has zero third-generation mixing and zero Jarlskog invariant. The 2025 PDG global fit reports nonzero (theta13), (theta23), and (J), excluding this vacuum from the measured `physical16` domain. Full gauge Higgsing therefore does not yet authorize meson constraints on the computed current kernel.

## Flavor-current kernel: WP445

- `flavor-current-kernel.md`
- `checkers/wp445_flavor_current_kernel.py`
- `results/wp445_flavor_current_kernel.json`

WP445 derives the exact source current of the fully Higgsed diagonal-(SU(3)_F) theory. In canonical Gell-Mann normalization its dimensionless gauge-mass shape is diagonal and positive, and tree elimination gives a four-quark kernel proportional to (K^-1/f^2) with exact cancellation of (g_F). This is a source-derived current response, not a selector. Experimental meson bounds remain inadmissible until the WP443 vacuum and WP435 messenger chain supply a viable common-frame map to `physical16` quark mass eigenstates.

## Flavon scale-orbit obstruction: WP444

- `flavor-flavon-scale-orbit.md`
- `checkers/wp444_flavon_scale_orbit.py`
- `results/wp444_flavon_scale_orbit.json`

WP444 separates full Higgsing from absolute scale selection. A common positive dilation of all WP443 flavon fields, accompanied by the corresponding quadratic-mass dilation, preserves normalized vacuum shape and gauge rank eight while scaling (g_Ff/v) and every flavor-gauge pole. The hostile pair (s=1,2) differs by a factor of two in the clock ratio. The admitted action therefore does not select the absolute ratio; flavor-current observations can constrain it but cannot become its source law.

## Fundamental flavon completion: WP443

- `flavor-fundamental-flavon-completion.md`
- `checkers/wp443_fundamental_flavon_completion.py`
- `results/wp443_fundamental_flavon_completion.json`

WP443 supplies the minimal representation repair after WP442. A single complex fundamental with a tachyonic radial potential and positive Gram portal to the two adjoints is oriented into their common kernel without an imported flavor vector. At the exact unit benchmark the combined vacuum is globally minimizing, its gauge-tangent rank is eight, and the full 22-component Hessian has exactly eight gauge zeros with all 14 physical modes positive. This completes the source-free full-Higgsing vacuum gate on an open stability neighborhood. It does not select a `physical16` point or the absolute ratio (g_Ff/v).

## Anticommutator vacuum no-go: WP442

- `flavor-anticommutator-vacuum-no-go.md`
- `checkers/wp442_anticommutator_vacuum_no_go.py`
- `results/wp442_anticommutator_vacuum_no_go.json`

WP442 closes the WP440 completion negative. For (eta>lambda), an exact trace/Cauchy bound shows that every global minimizer is commuting and has gauge-mass rank at most six. WP441's entire charged-instability region satisfies (eta>3lambda), so it cannot lead to full breaking. At the frozen hostile point the exact continuation is a commuting saddle with eigenvalue (-16/13), while a rank-six commuting configuration reaches the global energy bound. The earlier “lower-symmetry branch” wording is superseded.

## Charged flavon instability threshold: WP441

- `flavor-charged-instability-threshold.md`
- `checkers/wp441_charged_instability_threshold.py`
- `results/wp441_charged_instability_threshold.json`

WP441 solves WP440's local bifurcation gate. The residual-charged Hessian has four gauge zeros and four physical eigenvalues (m^2(3\lambda-\eta)/(2\rho-\lambda)). The exact threshold is (eta=3\lambda), and the unstable side intersects the frozen coercive domain on a nonempty open region. This proves departure from the WP438 vacuum without determining the endpoint stabilizer. WP442 subsequently shows that the continuation is commuting and closes the route negative.

## Charged flavon bifurcation preregistration: WP440

- `flavor-charged-bifurcation-preregistration.md`
- `checkers/wp440_charged_bifurcation_preregistration.py`
- `results/wp440_charged_bifurcation_preregistration.json`

WP440 freezes the first curvature-driven successor to WP439. Completing the source-authorized two-adjoint product grammar adds the exchange-symmetric, sign-even, renormalizable squared-anticommutator channel. It has zero gradient at the WP438 vacuum, as required by the stabilizer theorem, but exact negative curvature in the residual-charged block. A conservative open coercivity domain and five acceptance gates are fixed before solving. No full-breaking, scale, `physical16`, current, or instrument outcome is claimed.

## Residual-stabilizer gradient obstruction: WP439

- `flavor-residual-stabilizer-gradient-obstruction.md`
- `checkers/wp439_residual_stabilizer_gradient_obstruction.py`
- `results/wp439_residual_stabilizer_gradient_obstruction.json`

WP439 proves that no renormalizable simultaneous-conjugation trace invariant can linearly push the WP438 embedded-Pauli vacuum into a direction charged under its residual (U(1)). The checker exhausts all 28 trace words of degrees two through four and both-adjoint perturbations along four charged Hermitian generators. Every derivative vanishes, while an explicitly oriented noninvariant source gives the required hostile nonzero control. Full Higgsing therefore requires a preregistered charged Hessian instability, a disconnected lower-symmetry branch, or an enlarged dynamical representation; simply adding a cubic is insufficient.

## Source-free two-adjoint vacuum solution: WP438

- `flavor-source-free-vacuum-solution.md`
- `checkers/wp438_source_free_vacuum_solution.py`
- `results/wp438_source_free_vacuum_solution.json`

WP438 solves the frozen WP437 potential. Its global minima saturate the
commutator bound and are Pauli pairs embedded in a two-dimensional subspace.
They are nonzero, noncommuting, stable on the full open coefficient domain, and
have a complete Hessian with seven gauge zero modes and nine positive modes.
However, they break (SU(3)_F) only to (U(1)); the exact gauge-mass rank is
seven, failing the preregistered rank-eight gate. A new independently justified
invariant must break the residual (U(1)), while (g_Ff/v) remains unsourced.

## Source-free two-adjoint vacuum preregistration: WP437

- `flavor-source-free-vacuum-preregistration.md`
- `checkers/wp437_source_free_vacuum_preregistration.py`
- `results/wp437_source_free_vacuum_preregistration.json`

WP437 freezes the minimal source-free symmetry-breaking successor to WP436.
Exchange symmetry, independent sign flips, renormalizability, one tachyonic
quadratic, a radial stabilizer, and the commutator term define the potential and
strict coefficient domain before solution. Six vacuum acceptance conditions
and seven falsifiers are frozen. The packet contains no stationary solution,
Hessian, gauge-mass rank, or measured flavor coordinate; the radial scale and
(g_Ff/v) remain explicitly outside its authority.

## WP128 vacuum-source obstruction: WP436

- `flavor-wp128-vacuum-source-obstruction.md`
- `checkers/wp436_wp128_vacuum_source_obstruction.py`
- `results/wp436_wp128_vacuum_source_obstruction.json`

WP436 audits the full-vacuum gate after WP435. With positive adjoint masses and
WP128's strict coercivity condition, the source-free potential has the unique
global minimum (A=D=0). The desired noncommuting vacuum arises only through
linear sources proportional to the fitted Yukawa Gram matrices, so it
reconstructs rather than selects flavor. A successor must predeclare a
source-free symmetry-breaking potential and test its complete vacuum before
comparing it with measured flavor.

## Dynamical flavon messenger completion: WP435

- `flavor-dynamical-flavon-messenger-completion.md`
- `checkers/wp435_dynamical_flavon_messenger_completion.py`
- `results/wp435_dynamical_flavon_messenger_completion.json`

WP435 promotes the WP128 adjoints to dynamical diagonal-(SU(3)_F) flavons
with covariant kinetic terms. Their direct quark-Higgs portal is dimension five;
one up-type and one down-type vectorlike messenger pair provide a fully
renormalizable completion. Exact tree elimination yields the portal coefficient
as a product of two Yukawa couplings divided by the messenger mass, and each
vectorlike pair has zero net flavor anomaly. The dynamical field grammar is
complete, but the full noncommuting vacuum and its absolute scale remain
unselected.

## Diagonal quark-flavor SU(3) anomaly completion: WP434

- `flavor-diagonal-su3-anomaly-completion.md`
- `checkers/wp434_diagonal_su3_anomaly_completion.py`
- `results/wp434_diagonal_su3_anomaly_completion.json`

WP434 repairs WP433's anomaly objection without arbitrary spectators by gauging
the diagonal (SU(3)_F) acting on all quark generations. In a left-handed
basis, the cubic coefficient is (6-3-3=0), and the mixed
(SU(3)_F^2U(1)_Y) coefficient also vanishes. Yukawa maps transform by
conjugation, so WP433's full-rank eight-direction mass shape applies. This is a
new gauged relational theory, not a weak-basis gauge fixing; its absolute scale,
dynamical flavons, flavor-current bounds, and spectral instrument remain open.

## Two-adjoint gauge-clock obstruction: WP433

- `flavor-two-adjoint-gauge-clock-obstruction.md`
- `checkers/wp433_two_adjoint_gauge_clock_obstruction.py`
- `results/wp433_two_adjoint_gauge_clock_obstruction.json`

WP433 tests the closest WP432 route by gauging the shared flavor group. Two
generic WP128 adjoints give a rank-eight mass Gram on (SU(3)_Q), but the
central identity generator commutes with every adjoint, leaving an exact
one-dimensional kernel for (U(3)_Q). Restricting to (SU(3)_Q) repairs the
algebraic rank but leaves the absolute scale (g_F f), anomaly cancellation,
and the physical portal unsourced. The adjoints rigidify spectral shape without
selecting an observed clock.

## Mediator-clock relation census: WP432

- `flavor-mediator-clock-relation-census.md`
- `checkers/wp432_mediator_clock_relation_census.py`
- `results/wp432_mediator_clock_relation_census.json`

WP432 audits classical scale invariance, gauge Higgsing, dimensional
transmutation, and UV fixed-point crossover as sources of the missing (M/v)
relation. Each supplies a conditional formula but retains at least one
continuous input: portal coupling, flavor gauge coupling and breaking ratio,
RG boundary data, or relevant amplitude. The closest progressive route is an
independently observed flavor gauge coupling and order parameter explicitly
matched to WP128, neither of which is currently admitted.

## Clock-spectrum parallelization gate: WP431

- `flavor-clock-spectrum-parallelization-gate.md`
- `checkers/wp431_clock_spectrum_parallelization_gate.py`
- `results/wp431_clock_spectrum_parallelization_gate.json`

WP431 tests whether an observed Standard Model clock repairs WP430. Writing a
mediator mass as (M=xi v) leaves the ratio (xi) free; residues and widths
can scale with it while preserving the same infrared coefficient and
dimensionless line shape. A generic Higgs-portal mass relation likewise retains
unfixed portal inputs. The missing object is a source-derived parallelization
map fixing the mediator-to-clock ratio, not another measurement of the Standard
Model clock.

## Spectral-scale underdetermination: WP430

- `flavor-spectral-scale-underdetermination.md`
- `checkers/wp430_spectral_scale_underdetermination.py`
- `results/wp430_spectral_scale_underdetermination.json`

WP430 proves that the missing WP429 spectra cannot be derived from the admitted
low-energy match. A common pole dilation preserves the zero-frequency
coefficient and dimensionless width while moving absolute masses, widths,
residues, and fixed-frequency response. WP131 realizes the same orbit in the
gauge-complete flavor portal while changing accessible poles from two to zero.
An independent physical clock or observed threshold must break this scale orbit
before WP428's response matrix is defined.

## Threshold preregistration completeness audit: WP429

- `flavor-threshold-preregistration-completeness-audit.md`
- `checkers/wp429_threshold_preregistration_completeness.py`
- `results/wp429_threshold_preregistration_completeness.json`

WP429 attempts to execute WP428 and stops before rank. The detector ports and
resolution are frozen, but no rival supplies frequency-resolved pole locations,
widths, residues, contact spectral density, or control-to-signal normalization.
WP130's old three-bin overlap matrix cannot define WP428's new Gaussian
four-port map. The response rank is therefore undefined, not rank-deficient.
Repair requires an independently frozen spectral packet in common units before
convolution; filling it after seeing rank is prohibited.

## Threshold experiment preregistration: WP428

- `flavor-threshold-experiment-preregistration.md`
- `checkers/wp428_threshold_experiment_preregistration.py`
- `results/wp428_threshold_experiment_preregistration.json`

WP428 freezes the successor threshold experiment before computing rank. The
bounded non-gauge rival class is WP128 two-adjoint, WP127 auxiliary-adjoint, and
direct contact. A common conditionally admitted scalar-current preparation,
four frequency/readout ports, Gaussian resolution, control-channel
normalization, acceptance rule, and seven falsifiers are predeclared. The
packet deliberately contains no response matrix or rank outcome. Physical
selection authority remains conditional on realizing the common portal and
source-selected preparation law.

## Post-actuator flavor-selector disposition: WP427

- `flavor-post-actuator-selector-disposition.md`
- `checkers/wp427_post_actuator_selector_disposition.py`
- `results/wp427_post_actuator_selector_disposition.json`

WP427 reconciles the law–state correction with the existing selector no-go.
Finite-time RG and `physical16` readouts separate regular physical points but
do not select a proper family; textures rigidify presentations; WP128 remains
conditional selector architecture without boundary-scale or instrument
authority. No current source-generated physical16 selector is admitted, but
the conclusion is bounded, not universal. Reopening requires a source-selected
trajectory or compact support scale relative to a clock, followed by an
executable open-rival faithful threshold instrument.

## Law–state intervention boundary: WP426

- `flavor-law-state-intervention-boundary.md`
- `checkers/wp426_law_state_intervention_boundary.py`
- `results/wp426_law_state_intervention_boundary.json`

WP426 closes the direct Standard Model quartic-actuator branch relative to an
explicit source grammar. Operators below degree four prepare states and change
lower Taylor jets but have zero command derivative of the quartic coefficient.
A nonzero derivative requires either a degree-four theory label or an enlarged
dynamical scalar port with a declared preparation map. Direct quartic actuation
is not necessary for flavor selection, so the successor returns to fixed-law
source dynamics on `physical16` rather than treating counterfactual couplings as
laboratory commands.

## Higgs-pole analyzer no-go: WP425

- `flavor-higgs-pole-analyzer-no-go.md`
- `checkers/wp425_higgs_pole_analyzer_no_go.py`
- `results/wp425_higgs_pole_analyzer_no_go.json`

WP425 tests the observed Higgs resonance as WP424's missing electroweak pole.
A collider production source changes the Higgs state through a linear source
term. Around the commanded background, curvature and cubic response change,
but the quartic coefficient and fourth derivative remain fixed. The Higgs pole
is therefore an executable self-interaction analyzer, not a quartic-law
actuator. The remaining missing arrow is an observed prepared substrate with a
nonzero command derivative of the effective quartic coefficient.

## Causal resonance companion-signal gate: WP424

- `flavor-causal-resonance-companion-gate.md`
- `checkers/wp424_causal_resonance_companion_gate.py`
- `results/wp424_causal_resonance_companion_gate.json`

WP424 turns resonance from an adjustable amplifier into a falsifiable causal
constructor. A one-pole susceptibility reaches target dispersive gain (G)
only when (A\geq2G\gamma). Above threshold, two exact detunings give the same
gain but distinct absorption, so the quartic readout alone is nonfaithful.
Resonance authority requires a calibrated frequency scan jointly measuring
dispersion, absorption, linewidth, and pole strength in the common Higgs
experiment. No admitted substrate yet supplies that instrument.

## Charged-species enhancement no-go: WP423

- `flavor-charged-species-enhancement-no-go.md`
- `checkers/wp423_charged_species_enhancement_no_go.py`
- `results/wp423_charged_species_enhancement_no_go.json`

WP423 attacks the simplest explanation of WP422's reach gap: coherently add
charged Higgs-dependent thresholds. Even granting every species a same-sign
unit loop coefficient, order-one quartic displacement needs over (10^{36})
species. The correlated gravitational species cutoff then falls below (2)
GeV, invalidating the heavy-threshold EFT across the electroweak domain. The
route is therefore self-undermining before measurement; a successor needs a
non-multiplicity enhancement with independently fixed parameters and a
correlated measurable prediction.

A successor may become a physical ensemble only if it provides, before flavor
readout, a concrete UV action and coefficient domain, an independently
normalized positive measure, an equivariant vacuum/matching map, and an
explicit RG scale/scheme contract. The decisive falsifier is two
source-equivalent UV presentations inducing different pushforward measures on
`physical16`.
## Fixed-electroweak selector fiber: WP537

- `flavor-fixed-v-selector-fiber.md`
- `checkers/wp537_fixed_v_selector_fiber.py`
- `results/wp537_fixed_v_selector_fiber.json`

WP537 exhibits two exact points in WP489's positive common-source and declared
tree-level width-closure domain with the same electroweak norm but different
physical clock ratios. Along \(a=t^2,\ w=1/t\), one has \(v^2=2\) while
\(g_Ff_{\mathrm{phys}}/v=\sqrt3/t\). The hostile points \(t=1,2\) are stationary,
radially positive above all vector half-thresholds, and satisfy every tested
vector and nonquark pair-closure inequality. Hence the present dynamics is a
conditional relational selector and presentation rigidifier, but not a
numerical selector. Reopening requires independently derived coefficient
dynamics that fixes \(t\), followed by a fresh pole, residue, width, and
instrument calculation.

## Source-to-six-port system pencil: WP538

- flavor-source-six-port-system-pencil.md
- checkers/wp538_source_six_port_system_pencil.py
- results/wp538_source_six_port_system_pencil.json

WP538 realizes WP520's exact degree-six kernel as a minimal companion system
pencil. One instantaneous scalar source command has rank one, but the six
source-generated Krylov contexts have exact joint rank six and the six-port
state readout is faithful. Scalar \(\Delta M_s\) compression is independently
rank one with a five-dimensional kernel. Along WP537's fixed-\(v\) family the
denominator-coefficient tangent is nonzero and rank one, while
\(d(g_Ff_{\mathrm{phys}}/v)/dt=-\sqrt3\) at \(t=1\); the source moves the
target ratio and pole pencil without changing the instrument class. This
closes numerical selection negative for the present constructor. The formal
uniform-scaling response obeys \(K_t(z)=t^2K(t^2z)\), so its zero-momentum
derivative is \(2K(0)\ne0\): the \(t\)-direction is not erased by the formal
scalar current. Its survival through physical \(\Delta M_s\) remains unproved
without the calibrated bilocal functional. The remaining gates are an
independent equation fixing \(t\) and a calibrated realization of six
source-derived contexts with the complete WP535 covariance.

## Common-ensemble resolvent contexts: WP539

- flavor-common-ensemble-resolvent-contexts.md
- checkers/wp539_common_ensemble_resolvent_contexts.py
- results/wp539_common_ensemble_resolvent_contexts.json

WP539 converts WP538's algebraic closure into a bounded instrument design.
The six normalized Euclidean nodes \(0,1,2,3,4,5\) give an exact nonsingular
resolvent-context matrix. Tensoring with WP525's four Ward channels produces a
rank-24 complex map, or 48 real estimators, on one common correlator ensemble.
Six source-law preparations are unnecessary: the contexts are deterministic
postprocessing weights. Every five-context deletion has rank five, and
repeating node 4 is the smallest exact rank-loss falsifier. Physical authority
still requires independently calibrated lattice momentum support and the
unavailable renormalized four-channel \(B_s\) bilocal dataset with complete
common-ensemble covariance. This design separates pole states but neither
selects \(t\) nor enlarges the source image.

## Periodic-lattice context support: WP540

- flavor-periodic-lattice-context-support.md
- checkers/wp540_periodic_lattice_context_support.py
- results/wp540_periodic_lattice_context_support.json

WP540 gives WP539 a concrete periodic-lattice momentum grammar. With
\(N=24\), \(a=1\,\mathrm{GeV}^{-1}\), and modes \(0,2,4,6,8,10\), the exact
nearest-neighbor momentum squares are
\(0,2-\sqrt3,1,2,3,2+\sqrt3\). Their companion-resolvent context matrix has
rank six, every five-context deletion has rank five, and the four-channel map
has complex rank 24. Replacing mode 10 by mode 16 repeats
\(\widehat q^2=3\,\mathrm{GeV}^2\) and lowers rank to five, proving that
distinct Fourier labels do not prevent lattice-dispersion aliasing. The
witness fixes support without fitting flavor data, but physical authority
still requires independent QCD scale setting, multiple spacings and volumes,
renormalized bilocal data, threshold matching, and continuum covariance.

## Twisted continuum context ladder: WP541

- flavor-twisted-continuum-context-ladder.md
- checkers/wp541_twisted_continuum_context_ladder.py
- results/wp541_twisted_continuum_context_ladder.json

WP541 holds WP540's six exact lattice-momentum nodes fixed across
\(a=1,1/2,1/3\,\mathrm{GeV}^{-1}\) on a common
\(24\,\mathrm{GeV}^{-1}\) extent by partially twisted valence boundary
conditions. The link-angle rule
\(\alpha_j(a)=2\arcsin(a\sqrt{z_j}/2)\) preserves rank six at all three
spacings, while the physical momentum obeys
\(p^2=z+a^2z^2/12+a^4z^3/90+O(a^6)\). The twist holonomies and Fourier-sector
labels explicitly define a new relational boundary-condition experiment; they
do not recover an absolute phase of the periodic experiment. Removing the
twist port in one Fourier sector collapses all contexts to zero and rank one.
Actual instrument authority still awaits scale setting, three-ensemble
renormalized bilocal data, and full continuum covariance.

## Continuum-volume design rank: WP542

- flavor-continuum-volume-design-rank.md
- checkers/wp542_continuum_volume_design_rank.py
- results/wp542_continuum_volume_design_rank.json

WP542 preregisters five ensembles at three spacings and two physical volumes.
For each of WP541's 48 real estimators, the columns
\(1,a^2,a^4,F(L)\) have exact rank four whenever the independently calibrated
finite-volume ratio \(r=F(30)/F(24)\) differs from one. The joint design has
240 observations, 192 parameters, rank 192, and 48 residual degrees of
freedom, requiring a \(240\times240\) covariance. Setting \(r=1\) or using
only two distinct spacings lowers the per-estimator rank to three. Scale
setting and the QCD mass gap remain external instrument calibrations; they
cannot be learned from flavor-pole data. Actual gauge ensembles,
renormalization, contact subtraction, threshold matching, and measured
covariance remain outstanding.

## Existing source-constraint kernel: WP543

- flavor-existing-source-constraint-kernel.md
- checkers/wp543_existing_source_constraint_kernel.py
- results/wp543_existing_source_constraint_kernel.json

WP543 computes the strongest currently authorized equality Jacobian in
\((\log a,\log w,\log g_F^2,\log g_P^2)\). Fixed \(v\), WP490's gauge ray,
and even a separately fixed \(g_F\) give rank three with a one-dimensional
kernel spanned by WP537's tangent \((2,-1,0,0)\). This tangent changes
\(\log(g_Ff_{\mathrm{phys}}/v)\) by \(-1\). WP491-WP495 and WP498 add
necessary running coordinates and support-closure obligations but no
beta-zero equation transverse to the kernel. WP538's readout detects the
direction, but using it as a source equation would be circular projection
authority. Numerical selection therefore closes negative for the current
source grammar. Reopening requires a completed independently frozen beta
system or threshold equation with nonzero contraction against the
\(t\)-tangent.

## Typed source-instrument pencil: WP544

- flavor-typed-source-instrument-pencil.md
- checkers/wp544_typed_source_instrument_pencil.py
- results/wp544_typed_source_instrument_pencil.json

WP544 folds WP539-WP542 back into WP538's unified pencil without smearing
instrument authority into source authority. At fixed controls the six
pencil-coefficient derivative with respect to \(t\) has rank one. The pole
readout and contextual maps retain ranks six and 24, while 29 external
coordinates comprise one scale, six twists, sixteen renormalization/mixing
entries, and six threshold matches. The tagged bundle has rank 30, but its
source projection remains rank one. Without external QCD scale calibration,
uniform source-pole scaling and inverse unit scaling are opposite columns of a
rank-one six-by-two Jacobian with kernel \((1,1)\). Thus scale calibration is
necessary for identifying \(t\), but neither it nor the higher instrument
ranks select \(t\).

## RG-completion debt: WP545

- flavor-rg-completion-debt.md
- checkers/wp545_rg_completion_debt.py
- results/wp545_rg_completion_debt.json

WP545 proves a conservative lower bound of 18 unresolved source-side
coordinates before a selector-authoritative coupled beta system can be
formed: ten messenger normalizations, three radial cross-portals, one
connector-adjoint alignment, one pure-adjoint Gram coupling, and three
\(O(2)\) connector-complement directions. These sectors are disjoint by field
content or tensor contraction and exclude WP544's 29 external instrument
controls. The count also excludes inherited and Standard Model couplings, so
it is a lower bound rather than a final beta-system dimension. Any purported
\(t\)-fixing beta zero that omits one tagged coordinate belongs to a non-closed
truncation. Selector authority requires the completed scheme-declared vector
field and a stable equation transverse to WP543's \(t\)-tangent.

## Selector transversality normal form: WP546

- flavor-selector-transversality-normal-form.md
- checkers/wp546_selector_transversality_normal_form.py
- results/wp546_selector_transversality_normal_form.json

WP546 reduces the remaining local selector test to one exact scalar. If a new
source equality has log-coordinate gradient
\(\ell=(\ell_a,\ell_w,\ell_g,\ell_p)\), its augmentation of the WP543
Jacobian has determinant \(2\ell_a-\ell_w=\ell k\), where
\(k=(2,-1,0,0)^T\) spans the surviving fixed-\(v\) fiber. Thus the new row
removes the fiber exactly when \(2\ell_a-\ell_w\ne0\). The measured
clock-ratio row is transverse but remains a readout, and WP544's 29 controls
remain external instrument coordinates; neither has source authority. A
future selected \(t\) must trigger a fresh vacuum, pole, residue, complete
width, and calibrated-response calculation. WP537's hostile pair already
shows that every vector mass squared changes by a factor of four.

## Messenger-threshold kernel transfer: WP547

- flavor-threshold-kernel-transfer.md
- checkers/wp547_threshold_kernel_transfer.py
- results/wp547_threshold_kernel_transfer.json

WP547 composes WP478 with the WP546 gate on the faithful extended source
coordinate. The messenger threshold row is transverse to the projected
four-coordinate \(t\)-tangent, but it depends on
\(y_Q^2y_\Phi^2k_\Phi/\eta\). After those coordinates are restored, the exact
compensated tangent \((2,-1,0,0,1,0,0,0)^T\) preserves the fixed-\(v\) and
threshold equations while changing \(\log(g_Ff/v)\) by \(-1\). The threshold
therefore transfers the ambiguity from \(a\) into a messenger normalization;
it rigidifies the portal form without numerically selecting the ratio.
Independently calibrated widths or residues could identify the realized
normalization, but cannot become its source law.

## Cross-locus scale-reference gate: WP548

- flavor-cross-locus-scale-reference-gate.md
- checkers/wp548_cross_locus_scale_reference_gate.py
- results/wp548_cross_locus_scale_reference_gate.json

WP548 applies a hostile interface test to Aspect's comb-referenced six-port
rank theorem. When physical flavor scale, flavor detector unit, and comb unit
are kept distinct, the six flavor rows plus the comb row have rank two and
retain the exact kernel \((1,1,0)^T\). Direct calibration therefore does not
descend across loci. A separately derived interface row \((0,1,-1)\) raises
the rank to three and removes the detector-scale kernel. This row must be
realized by a named metrology or lattice scale-setting chain with common-unit
readback and covariance. The abstract reference architecture transfers, but
the physical flavor instrument remains conditional. Even a completed
interface identifies rather than selects and leaves the source requirement
\(2\ell_a-\ell_w\ne0\) unchanged.

## Temporal scale-calibration contract: WP549

- flavor-temporal-scale-calibration-contract.md
- checkers/wp549_temporal_scale_calibration_contract.py
- results/wp549_temporal_scale_calibration_contract.json

WP549 makes the WP548 interface row history-dependent. A successful
calibration event both reveals a reference readback and establishes a shared
frame for an illustrative three-step validity budget. Accepted physics trials
consume that budget; null calibration, fitted rows, pre-calibration trials,
and expired trials are rejected by a finite support contract. The detector
Jacobian has rank three only in a valid calibration state. Deleting the
successful calibration event invalidates dependent readouts, removes the
interface row, and exactly restores rank two with kernel \((1,1,0)^T\).
Physical admission still requires an implemented transfer chain and calibrated
drift, disturbance, cost, readback, and covariance dynamics.

## Omega scale-setting constructor: WP550

- flavor-omega-scale-setting-constructor.md
- checkers/wp550_omega_scale_setting_constructor.py
- results/wp550_omega_scale_setting_constructor.json

WP550 replaces the optical analogy by a lattice-native candidate
\(P_{\mathrm{scale}}\). On each WP542 ensemble, measure \(a m_\Omega\),
gradient-flow quantities, and all six flavor pole coordinates in one joint
analysis, then use a frozen pure-QCD physical \(\Omega^-\) mass to obtain
\(\mu_i=(a\mu_i)m_\Omega^{\mathrm{phys}}/(a m_\Omega)\). The exact log
Jacobian has rank six, cancels a common lattice-unit reparameterization, and
propagates scale uncertainty as a shared correlated term. Primary lattice
calculations establish this operation type, but no WP542 ensemble data yet
exist. Importing a published \(w_0\) value without a same-ensemble
dimensionless measurement fails the interface gate.

## Omega pole-width-residue transfer: WP551

- flavor-omega-pole-width-residue-transfer.md
- checkers/wp551_omega_pole_width_residue_transfer.py
- results/wp551_omega_pole_width_residue_transfer.json

WP551 composes WP550 with the exact WP534 quantity types. Complex pole
squares have mass dimension two, widths dimension one, and mass-squared
resolvent residues dimension zero. The eighteen-output log Jacobian has rank
eighteen and cancels lattice-unit reparameterization. Its common Omega
covariance is the outer product of the dimension vector, so every pole-square
and width block is correlated while the residue block receives exactly zero
scale covariance. Deleting the Omega latent variable invalidates all twelve
dimensionful outputs together but does not invalidate dimensionless residues;
their separate authority gate is current renormalization and operator
covariance. This corrects WP550's overly broad deletion wording and remains an
unexecuted identification architecture, not a selector.

## Bilocal renormalization parallelization: WP552

- flavor-bilocal-renormalization-parallelization.md
- checkers/wp552_bilocal_renormalization_parallelization.py
- results/wp552_bilocal_renormalization_parallelization.json

WP552 locates the normalization authority exposed by WP551. The dimensionless
signed residues remain source-side coefficients. A common operator-mixing and
subtraction matrix acts instead on the four bilocal estimator channels at each
of six poles. Under an invertible scheme change, estimator columns and Ward
coefficient rows transform contragrediently, leaving every pole amplitude and
the residue-weighted scalar invariant without transforming the residues. The
exact 24-channel map has rank 24 and the Ward readout retains rank six.
Deleting the operator map invalidates all renormalized amplitudes but leaves
the Omega scale map and source residues intact. Physical authority still
requires a nonperturbative common-ensemble mixing, subtraction, matching, and
covariance calculation.

## Ward common-scale commuting square: WP553

- flavor-ward-common-scale-commuting-square.md
- checkers/wp553_ward_common_scale_commuting_square.py
- results/wp553_ward_common_scale_commuting_square.json

WP553 tests the missing common frame inside the Ward row. The ratios
\(m_b^2/\mu_i^2\), \(m_s^2/\mu_i^2\), and \(m_bm_s/\mu_i^2\) are invariant
under one shared energy-unit change, and the Omega transfer then commutes
exactly with WP552 operator parallelization. With distinct quark and pole
scale factors their log Jacobian has row \((2,-2)\), rank one, and common-scale
kernel \((1,1)^T\). The hostile choice \(k_q=2k_p\) leaves the vector Ward
coefficient fixed but multiplies all scalar coefficients by four. A joint
quark-mass, Omega, pole, and operator-renormalization analysis or an
independently calibrated matching constructor is therefore required. This
repairs an identification interface and supplies no source selector.

## Six-context conditioning gate: WP554

- flavor-six-context-conditioning-gate.md
- checkers/wp554_six_context_conditioning_gate.py
- results/wp554_six_context_conditioning_gate.json

WP554 tests whether WP540's exact rank survives a physical resolution floor.
The six supported algebraic contexts retain exact rank six, but their
high-precision singular values range from about \(11.50\) to
\(9.03\,10^{-7}\), giving spectral condition number about
\(1.27\,10^7\) and infinity-norm condition number about \(1.53\,10^7\).
A unit coefficient displacement along the smallest singular direction lies
below a \(10^{-6}\) diagnostic response floor. Hence exact rank does not grant
resolution-robust faithfulness. The physical contextual partition must be
defined using the full covariance-whitened response, an admitted source norm,
and a preregistered detection threshold. Actual WP542 covariance remains the
decisive instrument gate; no source selection follows.

## Realization-invariant conditioning: WP555

- flavor-realization-invariant-conditioning.md
- checkers/wp555_realization_invariant_conditioning.py
- results/wp555_realization_invariant_conditioning.json

WP555 attacks WP554 under the full state-realization quotient. For the same
physical resolvent, a similarity sends the context matrix to \(TC\) while
transforming \(A,B,c\) so the transfer function is exactly unchanged. Choosing
\(T=C^{-1}\) makes the context matrix exactly \(I_6\) with condition number
one; a diagonal stretch gives a condition number above \(10^{11}\). Raw
conditioning is therefore presentation data. When the source metric is
transported as \(G'=T^{-T}GT^{-1}\), the Gram matrix is exactly invariant.
WP554's unweighted numbers remain chart diagnostics, but its unit-hostile
physical interpretation is withdrawn. Faithfulness requires a source metric,
measured observation covariance, and threshold that descend together.

## Source Gramian pairing: WP556

- flavor-source-gramian-pairing.md
- checkers/wp556_source_gramian_pairing.py
- results/wp556_source_gramian_pairing.json

WP556 constructs the missing source pairing requested by WP555 from the
minimal WP520 resolvent itself. Exact controllability and observability
Lyapunov equations give two rational positive-definite rank-six Gramians. The
metric \(W_c^{-1}\) transforms covariantly under realization similarity, and
the Hankel product transforms by similarity, so the construction descends.
However, both Gramians fill the entire minimal state space: the operation
weights directions but selects no proper subspace or point. Moreover its
auxiliary inverse-mass-squared-time impulse experiment has no admitted flavor
preparation or detector. The result is a source-generated mathematical
rigidifier, not a selector or executable physical instrument.

## Physical16 Gramian pullback gate: WP557

- flavor-physical16-gramian-pullback-gate.md
- checkers/wp557_physical16_gramian_pullback_gate.py
- results/wp557_physical16_gramian_pullback_gate.json

WP557 prevents promotion of WP556's internal six-state geometry to the
faithful flavor quotient. Any smooth pullback to `physical16` has metric rank
at most six and therefore a local kernel of dimension at least ten. Combined
with measured ten, a six-row probe repairs the quotient only if the stacked
Jacobian has rank sixteen. An exact factor-through witness leaves rank ten and
kernel dimension six; an abstract complementary witness reaches rank sixteen.
No source-derived map from `physical16` to the WP556 realization currently
exists, so complementarity has no authority. Even full stacked rank would
separate rather than select. A distinct transverse source law remains needed.

## Constructor-fiber pole descent: WP558

- flavor-constructor-fiber-pole-descent.md
- checkers/wp558_constructor_fiber_pole_descent.py
- results/wp558_constructor_fiber_pole_descent.json

WP558 asks whether the missing `physical16`-to-pole map can exist on an
unrestricted constructor class. WP129's three inequivalent constructors share
one low-energy packet but have rank-three formal threshold signatures. In
exact normal form, \(L=(1,1,1)\), \(Q=I_3\), and the displacement
\((1,-1,0)^T\) lies in \(\ker L\) but not \(\ker Q\). Hence \(Q\) does not
factor through the low-energy quotient. WP556's Gramian remains valid inside
one frozen realization but cannot be promoted constructor-independently.
Restricting the constructor class requires independent authority; adding a
constructor reference port defines a new relational threshold experiment.
Neither route supplies numerical source selection.

## Connected four-point constructor task: WP559

- flavor-connected-four-point-constructor-task.md
- checkers/wp559_connected_four_point_constructor_task.py
- results/wp559_connected_four_point_constructor_task.json

WP559 derives WP133's formerly formal fourth row from a frozen source action
rather than fitting a port to the rival. For
\(V=m^2\varphi^2/2+\lambda\varphi^4/4\), the Hessian is \(m^2\) and the
connected amputated four-point vertex is \(6\lambda\). The isospectral pair
\(\lambda=0,1\) therefore agrees at two points and differs exactly at four.
Appending the normalized fourth derivative raises the bounded four-constructor
response from rank three to rank four. This is a genuine source-derived
constructor-sensitive operation, but no preparation, scattering readout,
finite-width transport, detector response, or covariance is admitted. It can
identify the frozen rivals if instrumented; it does not select a source value.

## Trace-adjoint quartic to triple-Higgs interface: WP560

- flavor-trace-adjoint-quartic-to-trihiggs-interface.md
- checkers/wp560_trace_adjoint_quartic_trihiggs_interface.py
- results/wp560_trace_adjoint_quartic_trihiggs_interface.json

WP560 composes WP559's quartic source derivative with WP237's
weak-basis-invariant trace-adjoint/Higgs mixing and WP417's ATLAS triple-Higgs
channel. The induced physical light-Higgs modifier obeys
\(\partial\kappa_4/\partial\lambda_s=\sin^4\theta/\lambda_H\), so the passive
probe is source-sensitive on the preregistered nonzero-mixing domain and blind
at \(\sin\theta=0\). Proton-collision preparation, quartic-sensitive
production, six-bottom readout, finite-exposure calibration, and a published
profile-likelihood interval are supported. But trace-adjoint/Higgs mixing also
changes production, decay, and generally the trilinear interaction, while the
published one-dimensional interval freezes those directions. A confidence
interval is also not a covariance. The mixed-scalar signal model and
common-frame covariance are both absent, so the packet identifies a candidate
interface rather than an admitted end-to-end instrument, actuator, selector,
or uncertainty-stable identification theorem.

## HS3 source-covariance pullback: WP561

- flavor-hs3-source-covariance-pullback.md
- checkers/wp561_hs3_source_covariance_pullback.py
- results/wp561_hs3_source_covariance_pullback.json

WP561 audits the released ATLAS HHH HS3 likelihood suite rather than inferring
covariance from interval endpoints. The release contains 118 fixed-signal
workspaces; the bounded TRSM example has 139 nuisance parameters but only one
physics parameter of interest, a signal-strength normalization. It contains no
source quartic or trace-adjoint/Higgs mixing coordinate, so its detector
covariance cannot yet be pulled back to the flavor source. A single HHH
normalization has rank at most one on \((\lambda_s,z)\), with
\(z=\sin^2\theta\). The hostile points \((1,1/4)\) and \((16,1/16)\) share
\(\lambda_s z^2=1/16\). Adding the source-derived single-Higgs mixing readout
\(1-z\) gives an exact rank-two Jacobian with determinant
\(z^2/\lambda_H\). Physical identification still requires portal-complete HHH
templates and a joint or proven-independent covariance across the single-Higgs
and triple-Higgs instruments.

## Cross-experiment quartic Gram: WP562

- flavor-cross-experiment-quartic-gram.md
- checkers/wp562_cross_experiment_quartic_gram.py
- results/wp562_cross_experiment_quartic_gram.json

WP562 realizes WP561's complementary mixing readout with the detector-
independent CMS HIG-21-018 inclusive Higgs measurement. Its published
symmetrization rule gives exact scalar uncertainty \(0.054\). A covariance
grammar with positive independent CMS and ATLAS residuals plus an arbitrary
shared theory nuisance remains positive definite without assuming zero
cross-correlation. Pulling its inverse through the rank-two source response
gives Gram determinant \(z^4/(\lambda_H^2\det C)\), positive off the exact
zero-mixing boundary. The remaining nonformal field is now localized to the
ATLAS side: no portal-complete bin interpolation supplies a calibrated
\(\sigma_q\), shared-theory loading, or smallest-eigenvalue resolution test.

## HHH public reinterpretation factorization: WP563

- flavor-hhh-public-reinterpretation-factorization.md
- checkers/wp563_hhh_public_reinterpretation_factorization.py
- results/wp563_hhh_public_reinterpretation_factorization.json

WP563 audits the complete public reinterpretation surface. Six ONNX networks,
six scaling packets, the truth-level selection and feature code, and 118
fixed-signal HS3 workspaces provide an executable downstream detector suffix.
The MadGraph basis events, coupling polynomial, reweight cards, normalization
map, and validated public-score-to-HS3 transfer are absent. A fixed template at
zero displacement cannot determine its source derivative: the affine
completions \(w_A(x)=w_0\) and \(w_B(x)=w_0+x(1,-1)^T\) agree on the released
template and yield different score-bin derivatives. Thus the remaining gate is
a missing source constructor and validation join, not covariance algebra or
classifier availability.

## CMS HHH empty sensitive overlap: WP564

- flavor-cms-hhh-empty-sensitive-overlap.md
- checkers/wp564_cms_hhh_empty_sensitive_overlap.py
- results/wp564_cms_hhh_empty_sensitive_overlap.json

WP564 incorporates the July 2026 CMS HIG-24-012 result. CMS now supplies a
physically executed 138-inverse-femtobarn HHH experiment with calibrated
detector readout, control-region validation, systematic uncertainties, and
observed two-dimensional kappa contours. The remaining obstruction is an
exact domain mismatch. The published scans fix the top Yukawa to its Standard
Model value and use Standard Model signal topology, whereas the admitted
universal portal obeys \(\kappa_t^2=1-z\) and has quartic source response
\(z^2/\lambda_H\). Their intersection forces \(z=0\), where the source
response vanishes. Thus the CMS result is a real kappa-framework readout but
does not realize the flavor four-point derivative. The public HEPData record
contains seven result tables and no full Combine model; a portal-complete
parameterized likelihood remains the smallest physical-instrument repair.

## CMS HHH author-repository authority join: WP565

- flavor-cms-hhh-author-repository-authority-join.md
- checkers/wp565_cms_hhh_author_repository_authority_join.py
- results/wp565_cms_hhh_author_repository_authority_join.json

WP565 finds two public executable pieces beyond the official contours. The
`multihiggs_loop_sm` generator exposes the required trilinear, quartic, and
top-contact source coordinates, while an author repository contains analysis
code, 24 ONNX networks, and 684 ROOT calibration or systematic objects. But
the latter has no release tag or publication identifier and contains no
datacard, workspace, observed-data object, or nuisance-correlation model. Two
detector extensions can therefore agree exactly on the released
fixed-top-Yukawa slice while having different source derivatives and different
responses at the portal point \((z,\kappa_t)=(3/4,1/2)\). The repositories
support an executable research surrogate, not yet a uniquely identified CMS
likelihood. A publication-bound manifest and complete statistical model are
the remaining instrument gate.

## Four-point measurement path closure: WP566

- flavor-four-point-measurement-path-closure.md
- checkers/wp566_four_point_measurement_path_closure.py
- results/wp566_four_point_measurement_path_closure.json

WP566 audits the complete admitted chain from WP559's source-derived
four-point operation through the strongest ATLAS HS3, official CMS, public CMS
code-surrogate, and cross-experiment Gram routes. Each route carries a proper
subset of the seven-field measurement contract; none carries source operation,
invariant map, same-domain scattering, detector calibration, likelihood
covariance, and an uncertainty-resolved nonzero pullback in one composable
path. The conclusion survives granting the public multi-Higgs generator as a
portal source implementation. ATLAS lacks the validated source-to-template
edge; official CMS has empty source-sensitive portal overlap; the public CMS
code route lacks the publication-bound simulation and statistical suffix; the
Gram route remains conditional. The authority graph therefore has no path
from the formal derivative to an uncertainty-supported flavor measurement.

## Four-point score-channel constructor: WP567

- flavor-four-point-score-channel-constructor.md
- checkers/wp567_four_point_score_channel_constructor.py
- results/wp567_four_point_score_channel_constructor.json

WP567 answers the constructive question left by the WP566 closure. For a
source-derived event score \(s(x)\) and an independently calibrated detector
channel \(K(y\mid x)\), the detector score is forced to be the conditional
expectation of the source score given the detector record. Detector Fisher
information is positive exactly when
\(K\operatorname{diag}(p_0)s\ne0\), and it cannot exceed the source Fisher
information. Exact keep, noisy, and erase channels share the same nominal
detector histogram while retaining respectively \(1\), \(1/4\), and zero
directional information. Thus nominal agreement cannot choose the detector
completion. The theorem supplies a preregisterable interface constructor, but
current HHH releases still lack the independently calibrated portal-score
channel, null-outcome support, covariance, and uncertainty resolution needed
to instantiate it physically.

## Four-point score uncertainty radius: WP568

- flavor-four-point-score-uncertainty-radius.md
- checkers/wp568_four_point_score_uncertainty_radius.py
- results/wp568_four_point_score_uncertainty_radius.json

WP568 makes WP567's score-channel constructor uncertainty-stable. If the
transported detector tangent is \(d\), the independently fixed detector metric
is \(W\), and the propagated calibration/nuisance uncertainty has metric
radius \(\rho\), then the exact worst-case Gram is
\(\max(\sqrt{d^TWd}-\rho,0)^2\). Robust separation therefore requires the
strict inequality \(\rho<\sqrt{d^TWd}\). For WP567's noisy binary channel the
nominal Gram is \(1/4\): radius \(1/4\) leaves exact lower bound \(1/16\),
whereas radius \(1/2\) contains the tangent-erasing completion and gives zero.
This supplies a preregisterable uncertainty gate, but no current HHH release
provides the portal-score channel and transported detector uncertainty needed
to evaluate it physically.

## Two-direction score singular gate: WP569

- flavor-two-direction-score-singular-gate.md
- checkers/wp569_two_direction_score_singular_gate.py
- results/wp569_two_direction_score_singular_gate.json

WP569 extends the robust score-channel theorem to the two-error experiment.
For response matrix \(D\), independently frozen detector metric \(W\), and
operator-norm uncertainty radius \(\rho\), the completed Gram smallest
eigenvalue is bounded below by
\(\max(\sigma_{\min}(W^{1/2}D)-\rho,0)^2\). Rank two is therefore certified
when \(\rho\) is strictly below the nominal smallest singular value. An exact
three-outcome example has nominal Gram eigenvalues \(1,3\). Radius \(1/2\)
leaves the sharp lower bound \(1/4\); radius \(1\) makes the two completed
columns exact negatives, even though both remain individually nonzero. Thus
columnwise sensitivity cannot establish joint faithfulness. The theorem is
prospective or surrogate-only until an executed portal experiment publishes
the common-frame response and uncertainty operator.

## Null-outcome rank restoration: WP570

- flavor-null-outcome-rank-restoration.md
- checkers/wp570_null_outcome_rank_restoration.py
- results/wp570_null_outcome_rank_restoration.json

WP570 proves that support completion is part of the two-error instrument. An
\(m\)-outcome normalized probability record has tangent dimension at most
\(m-1\), so rank-two local separation requires at least three typed outcomes.
An exact three-cell source-score model transported through the identity channel
realizes WP569's response and has Fisher Gram eigenvalues \(3,9\). Treating the
third record as a completed trial with no selected candidate and discarding it
forces conditional renormalization: the remaining two response columns become
proportional and rank falls to one. The null outcome is therefore a
source-derived complementary probe, not absent data. Current HHH releases do
not publish the portal-score-conditioned completed-trial channel and
null-outcome covariance needed to instantiate this theorem physically.

## Poisson exposure rank restoration: WP571

- flavor-poisson-exposure-rank-restoration.md
- checkers/wp571_poisson_exposure_rank_restoration.py
- results/wp571_poisson_exposure_rank_restoration.json

WP571 identifies the physical alternative to explicit null-outcome retention.
Two selected Poisson counts can carry rank two through one shape and one total-
rate direction. Their exact Fisher matrix decomposes into rank-one shape and
rate Grams whose sum is the identity. The rate coordinate exists only relative
to calibrated luminosity or exposure. Profiling a common exposure nuisance
with calibration precision \(\pi\) gives Gram eigenvalues
\(1\) and \(\pi/(2+\pi)\): zero precision collapses rank to one, while positive
precision formally restores rank two. The exposure is a declared relational
reference port and changes the experiment; it does not reveal an absolute rate
from shape alone. Current HHH analyses have luminosity calibration but still
lack the public portal-score-conditioned rate-and-shape response needed to
instantiate this constructor.

## D4 reweight score constructor: WP572

- flavor-d4-reweight-score-constructor.md
- checkers/wp572_d4_reweight_score_constructor.py
- results/wp572_d4_reweight_score_constructor.json

WP572 makes the quartic source-response input executable in principle at leading
order. In the public restricted multi-Higgs UFO, the \(D_4\) coupling occurs
linearly at the four-Higgs vertex and at most once in connected
\(gg\to hhh\) diagrams. Each event weight is therefore quadratic in \(D_4\),
so central plus two symmetric MadGraph reweights recover the exact signed
event-measure derivative,
not a finite-difference approximation. The frozen model repository contains no
reweight card, event sample, HHH validation packet, or score output, but the
official generic MadGraph reweight operation supplies the source-side
constructor. At the exact support-zero hostile \(1-D_4\), the central ratio is
undefined, the first signed derivative vanishes, and support enters only at
second order. A frozen dominating source mixture and the full portal local
measure jet remain necessary before detector transport.

## Symmetric support-cover measure jet: WP573

- flavor-symmetric-support-cover-measure-jet.md
- checkers/wp573_symmetric_support_cover_measure_jet.py
- results/wp573_symmetric_support_cover_measure_jet.json

WP573 replaces central-ratio score typing with a support-safe local measure
jet. Three affine-amplitude event cells have central measure \((1,1,0)\),
first signed derivative \((2,0,0)\), and second derivative \((2,0,2)\). A
symmetric proposal frozen at \(\theta=-1/2,0,1/2\) has positive mass on all
three cells; its density differences recover both derivatives exactly without
dividing by the central measure. The selected response factors into rate
derivative \(2\) and shape derivative \((1/2,-1/2)\), while the null cell is a
pure second-order support birth. The two hostiles are exact: a first-order
central score misses quadratic support entry, and a proposal enlarged only
after observing that failure lacks response authority. The theorem remains a
prospective source constructor until joined to a portal-complete detector and
uncertainty instrument.

## Detector null-exposure quotient theorem: WP574

- flavor-detector-null-exposure-quotient-theorem.md
- checkers/wp574_detector_null_exposure_quotient_theorem.py
- results/wp574_detector_null_exposure_quotient_theorem.json

WP574 freezes the sector-independent composition of WP569--WP571. One exact
three-outcome response has full Gram eigenvalues \(3,9\). The source direction
\(v=(1,2)^T\) produces completed detector tangent \((1,1,-2)^T\): a common
selected-rate increase compensated by the null outcome. Deleting null and
conditioning on selection erases \(v\) exactly. Retaining raw selected counts
keeps rank two, but their response along \(v\) is proportional to the exposure
nuisance; free exposure profiling erases the same direction. Independent
exposure precision \(\pi\) gives profiled determinant
\(27\pi/(2+3\pi)\), restoring formal rank two for \(\pi>0\). Null retention
and calibrated exposure are distinct repairs of the same quotient, with the
latter defining a new relational experiment. Aspect packet 39 physically
realizes the monitor-port branch; the flavor portal join remains prospective.

## Curvature-jet control-rank gate: WP575

- flavor-curvature-jet-control-rank-gate.md
- checkers/wp575_curvature_jet_control_rank_gate.py
- results/wp575_curvature_jet_control_rank_gate.json

WP575 prevents a false composition of WP573 with WP574. WP573's first and
second measure derivatives form a rank-two formal jet matrix with Gram
determinant (16), but their coefficients on the admitted one-parameter
source curve obey (2b=a^2). The central executable tangent is therefore only
the line (b=0), of control rank one. The smallest hostile is the formal pure
curvature coefficient ((a,b)=(0,1)), which no source setting realizes.
Symmetric reweights can estimate curvature but cannot independently excite it.
A rank-two detector claim now requires a separately admitted two-parameter
flavor source surface with a weak-basis-invariant rank-two differential.

## Portal-detector rank composition: WP576

- flavor-portal-detector-rank-composition.md
- checkers/wp576_portal_detector_rank_composition.py
- results/wp576_portal_detector_rank_composition.json

WP576 identifies a genuine two-coordinate source entrance already present in
the universal portal. The invariant map from ((z,\lambda_s)) to
((r,q)=(z,\lambda_s z^2/\lambda_H)) has determinant
(z^2/\lambda_H), so it has rank two for nonzero mixing. Conditional
composition with WP574's completed detector response has Gram determinant
\(3z^4/\lambda_H^2\). This removes the algebraic source-rank obstruction but
does not fill the authority-bearing interface: no publication-bound calibrated
transport currently identifies the detector input columns with \((r,q)\).
The exact boundary falsifier is \(z=0\), where the quartic column vanishes.
The viable source domain also requires \(\lambda_s>0\), inherited from
boundedness of the declared singlet quartic on its isolated large-field ray.

## Two-setting interface identification: WP577

- flavor-two-setting-interface-identification.md
- checkers/wp577_two_setting_interface_identification.py
- results/wp577_two_setting_interface_identification.json

WP577 gives the smallest calibration design for WP576's missing local
transport under a source-frozen affine grammar. One perturbation \(x=(1,c)\)
leaves every zero-sum completion \(H=w(-c,1)\) invisible, so distinct
normalized detector transports agree on the calibrated setting. Two
noncollinear perturbations form an invertible design matrix and reconstruct
the unique local transport as \(K=YX^{-1}\). This identifies a research
surrogate only until the common generator, detector, completed-record,
covariance, and nuisance chain is publication-bound.

## Two-setting conditioning gate: WP578

- flavor-two-setting-conditioning-gate.md
- checkers/wp578_two_setting_conditioning_gate.py
- results/wp578_two_setting_conditioning_gate.json

WP578 strengthens WP577 from exact identification to robust calibration.
For the near-collinear design \(X_\varepsilon=((1,1),(0,\varepsilon))\),
response error in the second setting is amplified by exactly
\(1/|\varepsilon|\) in the reconstructed transport. The rational hostile
\(\varepsilon=1/10\), \(\delta=1/100\) is invertible but amplifies error norm
by ten. Under the frozen budget \(\operatorname{tr}(X^TX)=2\), orthogonal
equal-norm settings uniquely attain the maximum possible smallest singular
value one. A physical design must publish its invariant source metric,
feasible perturbations, and uncertainty-supported singular-value margin.

## Portal design pullback-cost gate: WP579

- flavor-portal-design-pullback-cost.md
- checkers/wp579_portal_design_pullback_cost.py
- results/wp579_portal_design_pullback_cost.json

WP579 pulls WP578's invariant orthogonal design back through the portal
Jacobian. Unit \(r\) and \(q\) settings require physical perturbations
\((1,-2\lambda_s/z)\) and \((0,\lambda_H/z^2)\), with squared costs
\(1+4\lambda_s^2/z^2\) and \(\lambda_H^2/z^4\). The design is therefore
pointwise feasible for \(z>0\) but not uniformly bounded near zero mixing.
At \(z=1/2\), \(\lambda_H=1\), unit \(q\) requires
\(\delta\lambda_s=4\), while a unit-bounded setting reaches only \(1/4\).
A physical calibration must publish its source-setting metric, reach domain,
induced design conditioning, and finite-setting remainder.

## Exact portal setting compiler: WP580

- flavor-exact-portal-setting-compiler.md
- checkers/wp580_exact_portal_setting_compiler.py
- results/wp580_exact_portal_setting_compiler.json

WP580 removes the finite-setting remainder in WP579 by inverting the portal
map exactly. A pure invariant \(r\) step \(h\) uses
\((z+h,\lambda_s z^2/(z+h)^2)\); a pure \(q\) step uses
\((z,\lambda_s+\lambda_Hh/z^2)\). Their exact design is \(hI\).
The Jacobian-only pure-\(r\) approximation contaminates \(q\) by
\(-\lambda_s(3h^2+2h^3/z)/\lambda_H\). At the rational hostile
\(z=\lambda_s=\lambda_H=1\), \(h=1/2\), the exact setting preserves \(q\),
whereas the linearized setting changes it by \(-1\). The compiler remains a
source-side research operation until its viable domain and publication-bound
detector transport are supplied.
Every compiled endpoint must retain \(\lambda_s>0\); a negative pure-\(q\)
step is admitted only while
\(\lambda_s+\lambda_Hh/z^2>0\).

## Machian vacuum-normalization gate: WP581

- flavor-machian-vacuum-normalization-gate.md
- checkers/wp581_machian_vacuum_normalization_gate.py
- results/wp581_machian_vacuum_normalization_gate.json

WP581 rejects an untyped identification of WP580's \(h=1/2\) with vacuum
energy. A dimension-four vacuum density becomes dimensionless only relative to
a declared scale, \(\eta=\rho_{\mathrm{vac}}/M^4\). Any positive target,
including one half, can be encoded by choosing
\(M=(\rho_{\mathrm{vac}}/h)^{1/4}\); doubling \(M\) changes the readout by a
factor of sixteen. Even granting one source-derived Machian scalar, its portal
response is one column, so repeated settings remain rank one and cannot supply
WP577's two independent directions. A reference scale defines a relational
experiment rather than recovering absolute vacuum energy.

## Vacuum-stress source-rank gate: WP582

- flavor-vacuum-stress-source-rank.md
- checkers/wp582_vacuum_stress_source_rank.py
- results/wp582_vacuum_stress_source_rank.json

WP582 sharpens WP581 at the physical-source level. Lorentz-invariant vacuum
stress \(T_{\mu\nu}=-\rho g_{\mu\nu}\) and its trace reverse span one metric
line; the normalization reference obeys
\(\partial T_{\mu\nu}/\partial M=0\), so \((\rho,M)\) has physical rank one.
A nonzero traceless stress tensor supplies an algebraically independent second
channel, but it requires matter, anisotropy, boundary data, or a relational
timelike frame and therefore changes the admitted groupoid. Rank-two flavor
response additionally requires a source-derived noncollinear coupling from
the two stress channels into invariant portal or physical16 coordinates.

The operator subsequently closed the Machian successor branch. WP581 and
WP582 remain recorded negative gates and are not active research directions.

## Portal setting viability radius: WP583

- flavor-portal-setting-viability-radius.md
- checkers/wp583_portal_setting_viability_radius.py
- results/wp583_portal_setting_viability_radius.json

WP583 intersects WP580's exact compiler with the currently authorized local
domain \(0<z<1\), \(\lambda_s>0\), and \(\lambda_H>0\). The four symmetric
pure-invariant endpoints remain admitted exactly when
\(0<h<\min(z,1-z,\lambda_s z^2/\lambda_H)\). The three boundary equalities
respectively hit the zero-mixing blind point, zero Standard Model production,
and loss of strict singlet-quartic stability. This is an exact source-side
local radius, not full phenomenological viability or an executable detector
instrument.

## Inclusive-Higgs portal-setting rank: WP584

- flavor-inclusive-higgs-portal-setting-rank.md
- checkers/wp584_inclusive_higgs_portal_setting_rank.py
- results/wp584_inclusive_higgs_portal_setting_rank.json

WP584 executes the WP580 settings through the largest currently authorized
portal detector readout, \(\kappa_t^2=1-z\). Its Jacobian has rank one: the
two \(r\)-settings are distinguished and both \(q\)-settings are exactly
blind. At \(z=1/4\), \(\lambda_s=\lambda_H=1\), and \(h=1/32\), the legal
endpoints \((1/4,1/2)\) and \((1/4,3/2)\) both read \(3/4\). The first
nonfaithful arrow is therefore the available physical instrument. Rank two
requires a publication-bound completed detector response with nonzero
calibrated derivative along \(q\) at fixed \(z\).

## Inclusive-Higgs adaptive-closure no-go: WP585

- flavor-inclusive-higgs-adaptive-closure.md
- checkers/wp585_inclusive_higgs_adaptive_closure.py
- results/wp585_inclusive_higgs_adaptive_closure.json

WP585 proves that no finite contextual closure of the WP584 instrument repairs
its \(q\)-kernel. Products, mixtures, null conditioning, score construction,
and history-dependent choices between exact \(q\)-settings all preserve the
primitive factorization through \(z\). Hence the hostile pair
\((1/4,1/2)\), \((1/4,3/2)\) remains equivalent under every finite adaptive
experiment built from the authorized inclusive-Higgs kernel. A new primitive
trial kernel with calibrated nonzero \(q\)-dependence must be admitted before
context closure can become jointly faithful.

## D4 score versus portal tangent: WP586

- flavor-d4-score-portal-tangent-ambiguity.md
- checkers/wp586_d4_score_portal_tangent_ambiguity.py
- results/wp586_d4_score_portal_tangent_ambiguity.json

WP586 proves that WP572's executable \(D_4\) partial derivative is not yet the
physical portal tangent. In the minimal amplitude \(M=1+c+d\), every
completion keeps \(dc/dq=1\), but the omitted tangent coefficient
\(dd/dq=\alpha\) changes the event-weight derivative from four at
\(\alpha=1\) to zero at \(\alpha=-1\); the \(D_4\)-only value is two.
The first missing arrow is therefore the source-derived tangent into the full
generator coordinate family, before shower or detector transport.

## Portal tangent lift kernel: WP587

- flavor-portal-tangent-lift-kernel.md
- checkers/wp587_portal_tangent_lift_kernel.py
- results/wp587_portal_tangent_lift_kernel.json

WP587 separates the known portal tangent from its unknown completion. The
source-derived projection into \((\kappa_t^2,\kappa_4)\) is exactly
\(\operatorname{diag}(-1,1)\) and has rank two. Adding one omitted
detector-sensitive coordinate yields the lift family
\(((-1,0),(0,1),(a,b))\). A detector row \((0,1,1)\) has \(q\)-response
\(1+b\): the indistinguishable projected lifts \(b=0\) and \(b=-1\)
produce response one and zero. Completion requires either deriving every
detector-sensitive omitted row or proving that the publication-bound detector
annihilates the lift kernel.

## Detector annihilation of the portal lift kernel: WP588

- flavor-detector-lift-kernel-annihilation.md
- checkers/wp588_detector_lift_kernel_annihilation.py
- results/wp588_detector_lift_kernel_annihilation.json

WP588 gives the necessary-and-sufficient descent criterion for WP587:
a calibrated detector map \(D\) is independent of every full-generator lift
exactly when it annihilates \(\ker P\), equivalently when \(D=KP\) for the
known coupling projection \(P\). Inclusive Higgs satisfies this criterion
but has rank one. Adding a calibrated pure-quartic row would give the
lift-independent rank-two response \(\operatorname{diag}(-1,1)\). Any
quartic channel with sensitivity to omitted coordinates instead requires
their source-derived tangent before it can carry identification authority.

## CMS quartic factorization and support gate: WP589

- flavor-cms-quartic-factorization-support-gate.md
- checkers/wp589_cms_quartic_factorization_support_gate.py
- results/wp589_cms_quartic_factorization_support_gate.json

WP589 applies WP588 to the released CMS HHH quartic scan. A pure
\(\kappa_4\) detector row passes the lift-kernel annihilation test, but the
released \(\kappa_t=1\) domain pulls back to \(z=0\), where
\(\partial\kappa_4/\partial\lambda_s=0\). The source-sensitive
nonzero-mixing domain therefore has empty overlap with the scan, and the
formal boundary Jacobian has rank one. Detector factorization and source
support are independent acceptance gates; CMS currently passes only the
former algebraically.

## Deutschian explanatory scope of FDM-1: WP590

- flavor-fdm1-deutschian-scope.md
- checkers/wp590_fdm1_deutschian_scope.py
- results/wp590_fdm1_deutschian_scope.json

WP590 audits the strongest source constructor whose own prediction survives
the complete fitted ensemble. The family
\(V_{a,\lambda}=\lambda(s^2-a^2)^2/4\) robustly makes the CP-conserving
point unstable and selects \(J\ne0\); all 1,210 fitted sheets pass. But
\(|J|=a j(q)\), so changing \(a\) preserves the whole CP-breaking mechanism
while continuously changing the numerical prediction, and the remaining 15
local physical16 coordinates are untouched. FDM-1 is therefore a genuine
qualitative CP-breaking explanation candidate, not an explanation of the
observed flavor relations.

## Common-clock CP normalization migration: WP591

- flavor-common-clock-cp-normalization-migration.md
- checkers/wp591_common_clock_cp_normalization_migration.py
- results/wp591_common_clock_cp_normalization_migration.json

WP591 couples FDM-1 to WP467's common dilaton clock through
\(\kappa(s^2-\chi\sigma^2)^2/4\). The common scale cancels and selects
\(s^2/f^2=\chi/(6y^2)\), genuinely removing an independent dimensionful CP
scale. But \(\chi/y^2\) remains a continuously free Wilson ratio under the
same source symmetries: at \(y=1\), \(\chi=1\) and \(4\) give \(1/6\)
and \(2/3\) while preserving the mechanism. The normalization is therefore
migrated, not explained. A symmetry, anomaly, isolated fixed point, or
microscopic matching theorem must fix the ratio before a joint CP/flavor-clock
experiment becomes a numerical criticism.

## CP-clock isolated fixed-ray criterion: WP592

- flavor-cp-clock-fixed-ray-criterion.md
- checkers/wp592_cp_clock_fixed_ray_criterion.py
- results/wp592_cp_clock_fixed_ray_criterion.json

WP592 gives the first exact hard-to-vary acceptance architecture for WP591's
remaining ratio. In reduced coordinates \(x=y^2/g^2\) and
\(r=\chi/y^2\), the positive coupled flow has the isolated ray
\(x_*=B/A\), \(r_*=D/C\), with transverse determinant
\(2B^2Dg^4/A>0\). It predicts \(s^2/f^2=D/(6C)\) independently of the
overall fixed-point magnitude. This becomes explanatory only when a complete
source theory derives \(A,B,C,D\); choosing them from flavor data merely
moves the fit. The fixed-line hostile \(C=D=0\) shows why isolation is
load-bearing.

## Triplicated fixed-ray completion debt: WP593

- flavor-triplicated-fixed-ray-completion-debt.md
- checkers/wp593_triplicated_fixed_ray_completion_debt.py
- results/wp593_triplicated_fixed_ray_completion_debt.json

WP593 tests WP592 against the declared triplicated messenger theory. Its
computed gauge-only root is negative, its Yukawa ray is uncomputed, and the
CP-clock coupling is absent. Adding the CP modulus enlarges the closed radial
quartic basis from ten to fifteen coordinates: besides \(s^4\) and
\(s^2\sigma^2\), one-loop support forces \(s^2F^2\), \(s^2H^2\), and
\(s^2R^2\). Combined with WP545, the concrete unresolved source-coordinate
lower bound rises from 18 to 23. Any reduced fixed ray omitting one of these
coordinates lacks selector authority.

## Singlet O(2) symmetry versus CP selection: WP594

- flavor-singlet-o2-symmetry-selection-tradeoff.md
- checkers/wp594_singlet_o2_symmetry_selection_tradeoff.py
- results/wp594_singlet_o2_symmetry_selection_tradeoff.json

WP594 tests the strongest Ward-identity reduction compatible with the common
gauge-singlet typing of \((\sigma,s)\). An \(O(2)\) symmetry reduces the
five-field radial quartic basis from fifteen to ten coordinates, but its
vacuum circle contains the CP-conserving point and has a massless angular
mode. The minimal positive anisotropy restores orientation selection while
giving \(s^2/(\sigma^2+s^2)=\chi/(1+\chi)\); \(\chi=1\) and \(3\)
preserve source typing but select \(1/2\) and \(3/4\). Continuous symmetry
therefore trades away the desired selector, while breaking it restores an
unexplained coefficient.

## Square-symmetry CP-orientation selector: WP595

- flavor-square-symmetry-cp-orientation.md
- checkers/wp595_square_symmetry_cp_orientation.py
- results/wp595_square_symmetry_cp_orientation.json

WP595 replaces WP594's continuous singlet symmetry by the square symmetry on
\((\sigma,s)\). The two positive invariant squares select four diagonal
vacua and the coefficient-independent relation
\(s^2/(\sigma^2+s^2)=1/2\), with positive radial and angular Hessian modes.
Removing the anisotropy restores the CP-conserving vacuum circle, so the
discrete invariant is load-bearing. Correction: a quarter-turn composed with
bare CP stabilizes each diagonal vacuum. WP595 is therefore a hard-to-vary
orientation selector, not yet a physical CP-breaking selector. The portal
must remove every generalized-CP stabilizer.

## Dihedral generalized-CP obstruction: WP596

- flavor-dihedral-generalized-cp-obstruction.md
- checkers/wp596_dihedral_generalized_cp_obstruction.py
- results/wp596_dihedral_generalized_cp_obstruction.json

WP596 audits all faithful irreducible dihedral doublets. Their first angular
invariant has degree \(n\), so only \(D_3\) and \(D_4\) have
renormalizable anisotropies; orders at least five retain accidental \(O(2)\).
Every angular extremum lies on a dihedral reflection axis and therefore
preserves a generalized CP. In WP595, bare CP moves the diagonal vacuum but a
quarter turn composed with CP fixes it. The one-half orientation survives,
while the CP-breaking claim is retracted. Genuine CP breaking requires
misaligned residual reflections from multiple multiplets or a portal that
removes the generalized stabilizer.

## Two-doublet selector-versus-stability dichotomy: WP597

- flavor-two-doublet-selector-stability-dichotomy.md
- checkers/wp597_two_doublet_selector_stability_dichotomy.py
- results/wp597_two_doublet_selector_stability_dichotomy.json

WP597 tests the smallest multi-multiplet repair. An axis vacuum and a diagonal
vacuum have no common generalized CP under one common \(D_4\), but the allowed
renormalizable invariant \((\phi\mathbin{\cdot}\psi)^2\) gives angular gradient
\((\eta/2,-\eta/2)\) at that pair and moves it for every nonzero \(\eta\).
Independent square rotations forbid the cross-term, but then independent
generalized CP transformations stabilize the two components. The naive
two-doublet architecture therefore trades generalized-CP breaking against
coefficient-independent stability. A progressive successor must derive a
symmetry or representation that forbids every angle-moving cross invariant
without restoring componentwise generalized CP.

## Abelian shaping overlap no-go: WP598

- flavor-abelian-shaping-overlap-no-go.md
- checkers/wp598_abelian_shaping_overlap_no_go.py
- results/wp598_abelian_shaping_overlap_no_go.json

WP598 closes the ordinary phase-charge escape from WP597. For arbitrary
additive charges, the Hermitian overlap obeys
\(q(|\phi^\dagger\psi|^2)=(-q_\phi+q_\psi)+(q_\phi-q_\psi)=0\).
It therefore survives every product of abelian shaping symmetries and retains
the exact angle-moving gradient \((\eta/2,-\eta/2)\) at the proposed vacuum.
A viable successor now needs a non-abelian product-selection rule, a
source-derived sequestering mechanism, or a representation whose complete
invariant ring lacks the dangerous singlet.

## Twisted-exchange mixed-invariant obstruction: WP599

- flavor-twisted-exchange-mixed-invariant-obstruction.md
- checkers/wp599_twisted_exchange_mixed_invariant_obstruction.py
- results/wp599_twisted_exchange_mixed_invariant_obstruction.json

WP599 audits Nima's quarter-twisted exchange against the complete mixed
quartic bidegree-\((2,2)\) space. The symmetry leaves the two independent
invariants \((uy+vx)^2\) and \((ux-vy)^2\), whose real angular restrictions
are \(\sin^2(\alpha+\beta)\) and \(\cos^2(\alpha+\beta)\). Their coefficients
are not equated. Adding the second with unit coefficient gives gradient
\((-1,-1)\) at the axis-and-diagonal representative and moves all sixteen
opposite-parity selected vacua. Twisted exchange removes the CP stabilizers
only on a truncated anisotropy packet; an additional source-derived rule must
close the mixed invariant ring.

## Inequivalent D5 mixed-quartic window: WP600

- flavor-d5-mixed-quartic-radial-window.md
- checkers/wp600_d5_mixed_quartic_radial_window.py
- results/wp600_d5_mixed_quartic_radial_window.json

WP600 finds the first representation-level escape from WP599. For faithful
inequivalent \(D_5\) doublets of weights one and two, the complete mixed
quartic bidegree-\((2,2)\) invariant space is one-dimensional and purely
radial: \((x^2+y^2)(u^2+v^2)\). An axis and \(\pi/5\) orientation have no
common generalized-CP stabilizer. The cost is that individual angular
selection first appears at degree five. The live constructor problem is now
to derive both quintic operators and their opposite relative sign from one
microscopic mediator source, then expose those same mediators through
calibrated threshold records.

Scope correction: WP600 is a quartic-only window, not a complete
renormalizable architecture. WP601 supplies an allowed mixed cubic that moves
the candidate.

## D5 cubic versus shaping generalized CP: WP601

- flavor-d5-cubic-shaping-cp-tradeoff.md
- checkers/wp601_d5_cubic_shaping_cp_tradeoff.py
- results/wp601_d5_cubic_shaping_cp_tradeoff.json

WP601 finds the symmetry-allowed cubic
\(\operatorname{Re}(z_\phi z_\psi^2)=\cos(\alpha+2\beta)\), whose gradient is
nonzero at the WP600 representative. Of the 25 diagonal \(Z_5\) charge pairs,
exactly 20 forbid the cubic; every one is linearly independent of the common
\((1,2)\) rotation and therefore generates independent \(C_5\times C_5\)
rotations with it. Those rotations restore componentwise generalized CP on
every quintic-extremum pair. The D5 diagonal-shaping repair is therefore
closed negative.

## Prime-cyclic shaping factorization no-go: WP602

- flavor-prime-cyclic-shaping-factorization-no-go.md
- checkers/wp602_prime_cyclic_shaping_factorization_no_go.py
- results/wp602_prime_cyclic_shaping_factorization_no_go.json

WP602 generalizes WP601 to every prime cyclic two-multiplet charge system. If
\(e\cdot w=0\) makes a mixed monomial invariant under the common rotation,
then a diagonal shaping charge \(q\) forbids it exactly when
\(\det(w,q)\ne0\). The same determinant makes \(w,q\) a basis and generates
independent component rotations, which restore componentwise generalized CP
on every discrete angular pair. The surviving architecture must be
non-diagonal, non-abelian, local or collectively broken.

## Mediator interference sign instrument: WP603

- flavor-mediator-interference-sign-instrument.md
- checkers/wp603_mediator_interference_sign_instrument.py
- results/wp603_mediator_interference_sign_instrument.json

WP603 types the minimum threshold experiment for a collective mediator
constructor. Separate partial widths are locally rank two but collapse all
four coupling-sign assignments; modulo simultaneous global sign, two physical
constructor classes remain. A source-derived coherent shared-channel
interference record \(I=g_\phi g_\psi\) separates exactly those two classes.
The tree architecture then predicts \(M^2c_{\mathrm{eff}}+I=0\) and
\(I^2=\Gamma_\phi\Gamma_\psi\). Executability still requires a derived common
final state, finite-width line shape, phase calibration, detector resolution
and a portal from \(c_{\mathrm{eff}}\) to `physical16`.

## Oriented triangle collective CP selector: WP604

- flavor-oriented-triangle-collective-cp-selector.md
- checkers/wp604_oriented_triangle_collective_cp_selector.py
- results/wp604_oriented_triangle_collective_cp_selector.json

WP604 supplies the first progressive collective source selector after the
diagonal-shaping no-go. On three labelled unit phases, triangular frustration
sets \(|z_1+z_2+z_3|^2=0\) and fixes the equilateral \(2\pi/3\) relation. The
base carrier alone has an accidental reflection that restores generalized CP.
Multiplying it by the positive cyclic, CP-even orientation carrier
\(1+\epsilon F\), with \(|\epsilon|<1/3\), leaves the zero set unchanged while
reducing the exact permutation group from \(S_3\) to \(C_3\). No cyclic
permutation composed with CP stabilizes the vacuum. The remaining gates are a
microscopic derivation of the oriented higher-degree interaction, descent to
`physical16`, and a resolved mediator-interference experiment.

## Relative mediator exact sequence: WP605

- flavor-relative-mediator-exact-sequence.md
- checkers/wp605_relative_mediator_exact_sequence.py
- results/wp605_relative_mediator_exact_sequence.json

WP605 refines WP603 into sector norms, a coherent relative arc, a calibrated
`physical16` boundary channel and source composition laws. The norms collapse
four sign assignments; \(I=g_\phi g_\psi\) refines them to the two global-sign
orbits. Joint faithfulness holds only on the reachable domain
\(I^2=\Gamma_\phi\Gamma_\psi\). A nonzero calibrated portal
\(J_{16}=-\kappa I/M^2\) preserves the distinction. Detector completion
\(I_{\mathrm{det}}=\nu I\) remains exact for \(\nu>0\), loses it at \(\nu=0\),
and is robust under uncertainty only when \(\delta<\nu|I|\).

## Physical16 relative-channel construction audit: WP606

- flavor-physical16-relative-channel-construction-audit.md
- checkers/wp606_physical16_relative_channel_construction_audit.py
- results/wp606_physical16_relative_channel_construction_audit.json

WP606 closes the reverse-construction ambiguity in WP605. Two phase-flipped
shared-channel records recover the coherent arc only after a common final
state, nonzero calibrated visibility and background have been supplied. The
hostile pairs \((g_\phi,g_\psi)=(1,1)\) and \((2,1/2)\), at fixed
\(M=\kappa=1\), have the same \(J_{16}=-1\) but different width packets.
Likewise, different \((\kappa,I)\) pairs can give the same boundary record.
Thus a derived invariant portal descends forward to `physical16`, but
`physical16` cannot construct the threshold experiment or identify its source.

## Same-family Gaussian orientation no-go: WP607

- flavor-reciprocal-gaussian-orientation-no-go.md
- checkers/wp607_reciprocal_gaussian_orientation_no_go.py
- results/wp607_reciprocal_gaussian_orientation_no_go.json

WP607 proves that a reciprocal Gaussian mediator acting on one cyclic operator
family cannot generate WP604's load-bearing orientation. Its symmetric Schur
kernel forces clockwise and counterclockwise coefficients to coincide. The
exact Gaussian escape uses two inequivalent channel families with reciprocal
full block kernel \(((0,K),(K^T,0))\), where the cross-block \(K\) may be
directed. The experiment must preserve that family typing and measure a
calibrated reversal-odd difference; an untyped two-port record does not
certify the architecture.

## Charged bipartite mediator incidence: WP608

- flavor-charged-bipartite-mediator-incidence.md
- checkers/wp608_charged_bipartite_mediator_incidence.py
- results/wp608_charged_bipartite_mediator_incidence.json

WP608 hostile-audits WP607's Gaussian escape. Three mediators and a
\(Z_2^3\rtimes C_3\) charge incidence do produce a rank-three forward shift,
but independent relabelling of the \(B\) family turns that shift into the
identity. A shifted reflection on \(B\) then stabilizes the same incidence.
The apparent orientation is therefore bipartite chart data, not a physical
selector. It becomes relational only if a source-derived common \(A/B\) label
frame is added, which changes the admitted stabilizer groupoid.

## Anchored two-matching relational carrier: WP609

- flavor-anchored-two-matching-relational-carrier.md
- checkers/wp609_anchored_two_matching_relational_carrier.py
- results/wp609_anchored_two_matching_relational_carrier.json

WP609 supplies the exact relational repair of WP608. Put a diagonal anchor
\(D=I\) and forward matching \(K=P_+\) on the same physical \(A/B\) ports.
Either relation alone has a six-element stabilizer containing a reflection;
their joint stabilizer is exactly the simultaneous \(C_3\). Both source
relations are therefore necessary. The pair creates a relational carrier and
rigidifies its presentation, but fixes no numerical flavor invariant. Its
experiment must establish both support relations on the same physically
tagged ports; a detector-added alignment is a new relational experiment.

## Spectral-projector matching obstruction: WP610

- flavor-spectral-projector-matching-obstruction.md
- checkers/wp610_spectral_projector_matching_obstruction.py
- results/wp610_spectral_projector_matching_obstruction.json

WP610 tests WP609 against the natural weak-basis-invariant flavor ports. The
spectral-projector overlap \(W_{ij}=\operatorname{Tr}(P_i^uP_j^d)=|V_{ij}|^2\)
descends exactly and has a charged-current instrument. Any permutation-valued
\(W\), including \(I\) or \(P_+\), forces the two Yukawa Grams to commute and
therefore gives \(J=0\). All 1,210 stored fitted sheets have nonzero \(J\), so
the physical portal falsifies exact matching on the complete ensemble. WP609's
anchor and forward relations must be genuinely new source operations rather
than renamed copies of the Standard Model overlap.

## Physical alternating-carrier extremum: WP611

- flavor-physical-alternating-carrier-extremum.md
- checkers/wp611_physical_alternating_carrier_extremum.py
- results/wp611_physical_alternating_carrier_extremum.json

WP611 realizes the faithful alternating flavor carrier as the imaginary
spectral-projector quartet, equivalently ordered (J). It descends and has a
charged-current CP instrument, but vanishes on every permutation overlap and
therefore cannot orient WP609's exact matching locus. Coefficient-free
minimization selects (J=0); maximization selects the exact universal bound
\(J^2=1/108\), saturated by Fourier mixing. All 1,210 fitted sheets are
nonzero and strongly nonmaximal. Selecting the observed interior magnitude
requires an independently derived dimensionless scale; inserting it from the
ensemble would be target encoding.

## Krylov seed-ray descent: WP612

- flavor-krylov-seed-ray-descent.md
- checkers/wp612_krylov_seed_ray_descent.py
- results/wp612_krylov_seed_ray_descent.json

WP612 audits Nima's Krylov orientation carrier under the full flavor groupoid.
The same seed ray represented by (x) and (e^{i\pi/3}x) has one projector
but opposite Krylov determinants; equivalently, a central (U(3)) weak-basis
transformation flips the sign while leaving (A) fixed. Only the magnitude
descends: (|\Omega|^2=\Delta_A^2\prod_i p_i\). It is a positive cyclicity
readout, with (p_i=|V_{ij}|^2) for a spectral seed, not an alternating
physical selector. A volume or phase reference would define a new relational
experiment over its stabilizer.

## Krylov magnitude moment completion: WP613

- flavor-krylov-magnitude-moment-completion.md
- checkers/wp613_krylov_magnitude_moment_completion.py
- results/wp613_krylov_magnitude_moment_completion.json

WP613 proves that the descended Krylov magnitude remains nonfaithful: the
distinct distributions \((1,6,6)/13\) and \((2,2,9)/13\) have the same
product. The source-generated moment record \((\mu_0,\mu_1,\mu_2)\) is an
invertible Vandermonde transform and reconstructs all three weights for a
nondegenerate spectrum. This repairs readout faithfulness, not selection.
Measured CKM columns are hierarchical interior points, whereas monotone
extremization of the product selects either democratic support or a boundary.

## Single-spurion charge-gap architecture: WP614

- flavor-single-spurion-charge-gap-architecture.md
- checkers/wp614_single_spurion_charge_gap_architecture.py
- results/wp614_single_spurion_charge_gap_architecture.json

WP614 identifies the strongest current conditional hierarchy source. One
spurion and charges \((3,2,0)\) force the Wolfenstein exponent matrix with
gaps one, two and three, and hence (J=O(\epsilon^6)\). Central CKM data lie in
an order-one coefficient corridor. The same charges nevertheless admit both
\(J=0\) and nonzero \(J\), as well as continuously different amplitudes. The
grammar selects hierarchy powers and messenger topology, not a numerical
`physical16` point or CP phase. Independent authority for the charges and a
resolved one/two/three-stage messenger experiment remain open.

## Froggatt--Nielsen anomaly-completion kernel: WP615

- `flavor-fn-anomaly-completion-kernel.md`
- `checkers/wp615_fn_anomaly_completion_kernel.py`
- `results/wp615_fn_anomaly_completion_kernel.json`

WP615 closes anomaly cancellation as an independent source of the WP614
charge gaps on an open mirror-completed UV domain. A conjugate mirror for each
charged quark-doublet port cancels the complete tested local anomaly packet
term by term for every integral charge assignment. The inequivalent vectors
\((3,2,0)\) and \((4,1,0)\) therefore have different messenger-depth matrices
but identical zero anomaly records. Anomaly freedom is a compatibility
condition and completion rigidifier here, not a charge-gap selector. A
progressive successor must independently freeze a chiral spectrum that
forbids this mirror kernel, then recompute its anomaly equations. The physical
gate is to resolve or exclude the mirror spectrum and directly test the
flavon messenger depths in one calibrated threshold experiment.

## Minimal U(1) flavor anomaly and width probe: WP616

- `flavor-minimal-u1f-anomaly-and-width-probe.md`
- `checkers/wp616_minimal_u1f_anomaly_and_width_probe.py`
- `results/wp616_minimal_u1f_anomaly_and_width_probe.json`

WP616 removes WP615's exotic-mirror freedom by freezing exactly the Standard
Model fermions plus three right-handed neutrinos. With vectorlike family
charges, the complete local flavor-anomaly packet reduces to the single
condition \(\sum_i(3q_i+\ell_i)=0\). At fixed
\(\ell=(-5,-5,-5)\), both \((3,2,0)\) and inequivalent \((4,1,0)\) satisfy it
on the integral lattice while predicting different messenger-depth matrices.
The anomaly is origin-sensitive but its zero locus is reflection-even and
blind to charge-gap geometry. Gauging the source nevertheless supplies an
exact conditional falsifier: the fully open inclusive vector-resonance width
ratio is \(3\sum q_i^2/\sum\ell_i^2\), giving \(13/25\) for the target and
\(17/25\) for the hostile architecture. The remaining source gate is an
independently derived rule sensitive to a second charge moment or orientation.

## Single-adjoint cubic-Casimir no-go: WP617

- `flavor-single-adjoint-cubic-casimir-no-go.md`
- `checkers/wp617_single_adjoint_cubic_casimir_no_go.py`
- `results/wp617_single_adjoint_cubic_casimir_no_go.json`

WP617 tests the first correctly typed signed charge observer as an actual
source action. For one traceless Hermitian \(SU(3)_F\) adjoint, the complete
renormalizable invariant potential is generated by
\(\operatorname{Tr}\Phi^2\), its square, and
\(\operatorname{Tr}\Phi^3\). At the centered target
\((4/3,1/3,-5/3)\), the tangent \((2,-3,1)\) preserves trace and quadratic
norm but changes the cubic by exactly 18. Every nonzero cubic coefficient
therefore moves the target; setting it to zero leaves orientation flat.
Equivalently, the stationary eigenvalue equation is quadratic and admits at
most two distinct eigenvalues. The cubic Casimir is a signed observer, not a
single-field selector. The corresponding gauge-boson mass-square patterns
\(1:4:9\) for the target and \(0:1:1\) for a stationary repeated-eigenvalue
branch provide the conditional threshold criticism.

## Two-adjoint relational charge lens: WP618

- `flavor-two-adjoint-relational-charge-lens.md`
- `checkers/wp618_two_adjoint_relational_charge_lens.py`
- `results/wp618_two_adjoint_relational_charge_lens.json`

WP618 extracts the relational resource already present in the source-free
WP438 vacuum. The quadratic composite of its embedded Pauli pair is the
primitive stabilizer \(H=\operatorname{diag}(1,1,-2)\). Together with
\(A=\operatorname{diag}(1,-1,0)\), it generates the charge-lens family
\(X(r)=H+rA\). The observed centered charge ray and gap ratio \(1:2:3\) occur
at \(r=3/5\), but the same source packet admits a continuous fiber, including
\(r=1\) with gaps \(1:1:2\). Thus the vacuum supplies a source-derived
relational carrier and orientation reference, not the numerical portal
selector. Root-vector mass squares measure the gap geometry and give
\(1:4:9\) at the target, while a coherent \(H\)-referenced pairing repairs the
global-sign kernel only by defining a new relational experiment.

## Relational cubic source disturbance: WP619

- `flavor-relational-cubic-source-disturbance.md`
- `checkers/wp619_relational_cubic_source_disturbance.py`
- `results/wp619_relational_cubic_source_disturbance.json`

WP619 lifts the two-odd-port orientation mechanism into the continuous WP618
lens. The quark cubic is \(Q(s,r)=6s(r^2-1)\), while the independently
source-derived stabilizer has \(R=\operatorname{Tr}H^3=-6\).
\(\operatorname{sgn}(QR)\) faithfully separates the two
simultaneous-reflection orbits, but the polynomial interaction
\(-\lambda QR\) produces the exact target force
\((216/5)\lambda s\). It therefore orients the sign packet while moving the
portal magnitude. Positive Gaussian mediation also generates a Gram kernel:
a nonzero cross channel necessarily carries nonzero self channels. The
architecture needs an independently selected magnitude sector whose full
stationarity survives this backreaction. Its joint criticism measures the
\(1:4:9\) root-vector spectrum and the \(H\)-referenced interference sign in
the same prepared run.

## Coupled-stationarity fiber: WP620

- `flavor-coupled-stationarity-fiber.md`
- `checkers/wp620_coupled_stationarity_fiber.py`
- `results/wp620_coupled_stationarity_fiber.json`

WP620 adds the smallest bounded completion
\(V(z)=-\lambda z+\kappa z^2\) for
\(z=QR=36s(1-r^2)\). The target is stationary only at the exact free ratio
\(\kappa/\lambda=25/1152\), which rewrites the action as a square centered on
the target coordinate \(z_0=576/25\). On the full real domain it has four
minima: the target permutation pair \((1,\pm3/5)\) and a hostile outer pair
\((-1,\pm\sqrt{41}/5)\). The cubic-zero boundary \(|r|=1\) separates them, so
a source-authorized inner support component can remove the outer pair, but
that support is not supplied by the two-adjoint vacuum. The exact hostile
ratio \(1/32\) moves the inner minimum to \(\sqrt5/3\). The branch is a
conditional selector, not a hard-to-vary explanation.

## Positive Gaussian center migration: WP621

- `flavor-positive-gaussian-center-migration.md`
- `checkers/wp621_positive_gaussian_center_migration.py`
- `results/wp621_positive_gaussian_center_migration.json`

WP621 closes stable finite positive Gaussian mediation as the origin of
WP620's bounded square. Eliminating a positive-mass mediator tower gives
\(-\frac12(gz-J)^T(M^2)^{-1}(gz-J)\), so its induced quadratic coefficient is
nonpositive. Multiplicity increases this negative Gram curvature rather than
reversing it. The stationary coordinate is the weighted source ratio
\(z_*=g^T(M^2)^{-1}J/[g^T(M^2)^{-1}g]\); zero offsets give zero, and
target-proportional offsets merely insert \(576/25\). Replication leaves the
center unchanged, while \(J_a\mapsto J_a+\delta g_a\) moves it by exactly
\(\delta\). A stable positive contact, loop, constrained auxiliary, or
non-Gaussian source is required.

## Quartic mediator scale transport: WP622

- `flavor-quartic-mediator-scale-transport.md`
- `checkers/wp622_quartic_mediator_scale_transport.py`
- `results/wp622_quartic_mediator_scale_transport.json`

WP622 constructs the smallest stable non-Gaussian reopening,
\(V=K(z-\phi)^2/2+\lambda(\phi^2-v^2)^2/4\). Its two nonzero stationary
points are strict minima, while the origin is a saddle, so quartic mediation
repairs WP621's curvature obstruction and selects a proper relational
subfamily. It does not calculate the observed center: (r=3/5) requires the
free vacuum scale (v=576/25), whereas the equally stable hostile value
\(v=24\) selects (r=\sqrt3/3\). Moreover (z=QR) uses the WP618 (H)
reference, so the operation descends only in the new stabilizer-groupoid
experiment, not on the original full weak-basis quotient. It is a conditional
selector and relational rigidifier, not a source-derived numerical selector.

## Root-of-unity selector no-go: WP623

- `flavor-root-of-unity-selector-no-go.md`
- `checkers/wp623_root_of_unity_selector_no_go.py`
- `results/wp623_root_of_unity_selector_no_go.json`

WP623 tests the smallest constructor that could forbid nearby vacuum values:
one compact phase with integer harmonics and fixed readout (r=\cos\theta).
At every minimum, (2r=\zeta+\zeta^{-1}) is an algebraic integer for a root
of unity \(\zeta\). If (r) is rational, this forces
\(r\in\{-1,-1/2,0,1/2,1\}\). The observed (3/5) is therefore excluded for
every harmonic, with nearest exact residual (1/10). An affine readout can
fake the target only by inserting (3/5) into its transfer coefficient. The
single-clock branch is a genuine discrete selector in the new
(H)-referenced stabilizer-groupoid experiment, but it selects the wrong
set and has no authority on the original full weak-basis quotient.

## Five-clock fiber without selection: WP624

- `flavor-five-clock-fiber-no-selection.md`
- `checkers/wp624_five_clock_fiber_no_selection.py`
- `results/wp624_five_clock_fiber_no_selection.json`

WP624 proves that five identical equal-weight clocks are the minimal
multi-clock representation of \(r=3/5\): integrality of
\(\sum_i x_i=6N/5\) forces five to divide \(N\). At \(N=5\), however, the
target has 70 labelled realizations and five permutation-inequivalent
occupancy classes. In particular, \((-2,2,2,2,2)\) and \((1,1,1,1,2)\) are
physically distinct clock packets with the same mean. A symmetric square
centered on total six would select the mean only by importing the target
integer. Five-clock topology therefore repairs representability but supplies
neither target selection nor source identification.

## Clock second-moment rigidifier: WP625

- flavor-clock-second-moment-rigidifier.md
- checkers/wp625_clock_second_moment_rigidifier.py
- results/wp625_clock_second_moment_rigidifier.json

WP625 adds \(Q=\sum_i x_i^2\). At \(S=6\), the five WP624 orbits have
distinct values \(Q=8,10,12,14,20\), so \((S,Q)\) is faithful and positive
\(Q\) conditionally rigidifies the balanced orbit. Unconstrained positive
\(Q\), however, selects the all-zero state with \(S=0\). The second moment
repairs identification and occupancy rigidification, not source selection of
total charge six.

## Source-model compatibility registry: WP626

- `flavor-source-model-compatibility-registry.md`
- `checkers/wp626_source_model_compatibility_registry.py`
- `results/wp626_source_model_compatibility_registry.json`

WP626 assembles the largest currently source-authorized relational connector
field and interaction registry and checks its index closure exactly. The three
messenger route types close and the ten canonical up/down tensor
normalizations remain independent. A model export is nevertheless refused:
exact Standard Model messenger representations, kinetic normalizations,
threshold states, the eighteen-coordinate RG completion, and a one-scheme
finite matching map are not jointly supplied. The smallest exact falsifier is
omission of the connector-adjoint alignment coordinate. The construction is a
presentation rigidifier, not a numerical selector or calibrated instrument.

## Messenger Standard Model representation reconstruction: WP627

- `flavor-messenger-sm-representation-reconstruction.md`
- `checkers/wp627_messenger_sm_representation_reconstruction.py`
- `results/wp627_messenger_sm_representation_reconstruction.json`

WP627 closes WP626's conservative messenger-representation gap. WP435 assigns
the first stage the corresponding right-handed-quark representation; the
Standard Model singlet connector and exit flavon transport it uniquely through
the second stage. Thus both up stages are \((3,1,2/3)\), both down stages are
\((3,1,-1/3)\), and every vectorlike anomaly cancels. Gauge invariance also
forces \(\widetilde H^u\) at the up entrance. Using the unconjugated doublet
or a down-type second up stage leaves exact hypercharge residuals (1\) and
\(-1\). This is source-derived representation completion, not selection.

## Entrance kinetic-Gram obstruction: WP628

- `flavor-entrance-kinetic-gram-obstruction.md`
- `checkers/wp628_entrance_kinetic_gram_obstruction.py`
- `results/wp628_entrance_kinetic_gram_obstruction.json`

WP628 separates removable wavefunction conventions from one genuine model
gap. The two entrance doublets have identical gauge representations, so their
general positive kinetic term contains a two-by-two Hermitian Gram. The
canonical packet has orthogonal up/down axes, but the equally legal positive
Gram \(K=((2,1),(1,2))\) has determinant three and canonically normalized
axis-overlap squared \(1/4\). Canonicalizing the kinetic term while retaining
the old axis-aligned Yukawas silently deletes this coordinate. A source
symmetry must distinguish the doublets, or the full kinetic/Yukawa tensor
system must be included. This is a model-export obstruction, not a selector.

## Entrance sector-parity repair: WP629

- `flavor-entrance-sector-parity-repair.md`
- `checkers/wp629_entrance_sector_parity_repair.py`
- `results/wp629_entrance_sector_parity_repair.json`

WP629 adds the smallest algebraically sufficient repair of WP628: one exact
sector \(Z_2\). The parity equations have a unique solution once the common
entrance, up chain, connector, and exit flavon are fixed even and \(H^d\) is
fixed odd. It forbids the off-diagonal kinetic Gram and both wrong-sector
entrance vertices while preserving every declared messenger route, vectorlike
mass, and even cross-invariant needed by the noncollinear vacuum. This is a
declared source-extension rigidifier, not a derived numerical selector. Since
the down entrance vev breaks the parity, domain-wall history or explicit soft
breaking becomes a new physical gate.

## Sector-parity wall-lift no-go: WP630

- `flavor-sector-parity-wall-lift-no-go.md`
- `checkers/wp630_sector_parity_wall_lift_no_go.py`
- `results/wp630_sector_parity_wall_lift_no_go.json`

WP630 proves that one global \(Z_2\) cannot simultaneously provide exact
kinetic/Yukawa protection and explicit lifting of the sign-related odd-field
vacua. Every protecting operator is parity even and preserves the degeneracy;
every splitting operator is parity odd and removes the exact selection rule.
The smallest gauge-invariant soft candidate,
\(\mu_{ud}^2\operatorname{Re}(H^{u\dagger}H^d)\), vanishes on the orthogonal
vacuum pair but has nonzero overlap-direction gradient, so it fails to split
the old pair while destroying its stationarity. Honest successors must type a
cosmological domain history, gauge the parity in a changed groupoid, or add an
odd reference and recompute the full source.

## Parity-groupoid relative-reference theorem: WP631

- `flavor-parity-groupoid-relative-reference.md`
- `checkers/wp631_parity_groupoid_relative_reference.py`
- `results/wp631_parity_groupoid_relative_reference.json`

WP631 gives the categorical form of WP630. The original transitive sign
action groupoid has one isomorphism class: its two descended Boolean probes
are constant, while its two sign separators do not descend. Adding a second
odd source object and quotienting by diagonal sign reversal creates two
relative classes, jointly separated by the invariant \(I(x,r)=xr\). Forgetting
the reference collapses them again. Thus category theory exposes one genuine
window—a source-derived relative reference in a new diagonal stabilizer
groupoid—while forbidding its interpretation as recovery of absolute sign.

## Common-singlet relative parity reference: WP632

- `flavor-common-singlet-relative-parity-reference.md`
- `checkers/wp632_common_singlet_relative_parity_reference.py`
- `results/wp632_common_singlet_relative_parity_reference.json`

WP632 finds an existing candidate for WP631's odd reference: WP489's real
common-source singlet \(\sigma\). With \(\sigma\) and \(H^d\) odd, the complete
route and singlet-mass parity equations have one solution, with alternating
left/right messenger parities. Every declared vertex survives, kinetic mixing
and wrong-sector entrances remain forbidden, and every explicit bare messenger
mass is odd. The construction therefore exists only on the singlet-generated
threshold domain. The abstract relative product of the two signs descends, but
selector authority awaits a matched amplitude that remains sensitive after
all legal messenger rephasings.

## Common-singlet relative-sign collapse: WP633

- `flavor-common-singlet-relative-sign-collapse.md`
- `checkers/wp633_common_singlet_relative_sign_collapse.py`
- `results/wp633_common_singlet_relative_sign_collapse.json`

WP633 attacks WP632 with the full legal sign-rephasing group. Its projection
onto \((H^d,\sigma)\) contains all four sign changes. In particular, a legal
down-sector rephasing flips \(H^d\) while holding \(\sigma\) fixed, so it moves
between the proposed relative classes. Exact two-stage elimination gives a
coefficient proportional to \(1/\sigma^2\); the singlet sign cancels, while
the remaining down-Yukawa sign is removed by a right-handed quark rephasing.
The first nonfaithful arrow is the passage from the selected diagonal subgroup
to the full source rephasing groupoid, before `physical16` is reached.

## Messenger-incidence cycle no-go: WP634

- `flavor-messenger-incidence-cycle-no-go.md`
- `checkers/wp634_messenger_incidence_cycle_no_go.py`
- `results/wp634_messenger_incidence_cycle_no_go.json`

WP634 proves that the complete WP489 interaction incidence contains no closed
rephasing-invariant coupling cycle. The ten-by-sixteen signed incidence matrix
has exact row rank ten, so its continuous left kernel is zero; its modulo-two
left kernel is also zero. Thus every coupling phase and sign is removable
before `physical16`, generalizing WP633 beyond the singlet candidate. A
progressive successor needs a gauge-legal cycle-closing carrier; because the
up/down messenger hypercharges differ by one, that carrier changes the field,
threshold, anomaly, decay, and instrument census.

## Charged two-edge cycle carrier: WP635

- `flavor-charged-two-edge-cycle-carrier.md`
- `checkers/wp635_charged_two_edge_cycle_carrier.py`
- `results/wp635_charged_two_edge_cycle_carrier.json`

WP635 gives the minimal gauge-legal repair of WP634. One charged scalar
\(\chi\sim(1,1,1)\) and cross-sector couplings at both messenger stages enlarge
the incidence to twelve rows of rank eleven, producing exactly one continuous
and one sign cycle. A single cross-edge still has zero nullity. The surviving
invariant is \(\mathcal I_\chi=(Y_S^uZ_A^dC_B)/(Y_S^dZ_B^uC_A)\). The charged
field must have zero vacuum expectation value, and the invariant remains a
free coupling ratio. This supplies internal relative-probe capacity, not a
numerical selector or calibrated instrument.

## Charged-cycle tree interference: WP636

- `flavor-charged-cycle-tree-interference.md`
- `checkers/wp636_charged_cycle_tree_interference.py`
- `results/wp636_charged_cycle_tree_interference.json`

WP636 derives the first finite-mass response carrying WP635's cycle. The
charged transition from an up first-stage messenger to a down second-stage
messenger has two paths, through \(B^u\) and through \(A^d\), whose exact ratio
is \(\mathcal I_\chi\). On the unit slice their coherent rates are four for
relative sign plus and zero for relative sign minus. The cycle is therefore a
genuine source-generated threshold probe. Both signs remain legal, so it is
not a selector; masses, widths, competing decays, production, resolution, and
a common-frame likelihood remain the physical-instrument gate.

## Charged-cycle threshold-support fiber: WP637

- `flavor-charged-cycle-threshold-support-fiber.md`
- `checkers/wp637_charged_cycle_threshold_support_fiber.py`
- `results/wp637_charged_cycle_threshold_support_fiber.json`

WP637 separates interference capacity from kinematic support. Two positive
source points have the same \(\mathcal I_\chi=1\) and formal rate factor four,
with \(M_{B^d}=m_\chi=1\). At \(M_{A^u}=3\), the threshold margin is one and
the Källén polynomial is 45; at \(M_{A^u}=3/2\), they are \(-1/2\) and
\(-63/16\), so the channel is closed. The cycle does not select its on-shell
instrument domain. A successor must derive a strict threshold margin or a
quantified off-shell response.

## Charged-cycle low-energy matching: WP638

- `flavor-charged-cycle-low-energy-matching.md`
- `checkers/wp638_charged_cycle_low_energy_matching.py`
- `results/wp638_charged_cycle_low_energy_matching.json`

WP638 bypasses WP637's heavy-parent threshold fiber by integrating out the
messenger stages. Two complete tree paths generate the same dimension-seven
operator \(\bar Q_L\widetilde H^u\chi SXd_R\), and their exact ratio remains
\(\mathcal I_\chi\). Unit constructive and destructive signs give matched
coefficient squares four and zero without requiring an on-shell heavy
messenger decay. The result is a source-derived low-energy charged portal
probe, not a `physical16` selector. An accessible \(\chi\) pole, production,
widths, QCD transport, detector acceptance, and a likelihood remain open.

## Charged-cycle contact descent: WP639

- `flavor-charged-cycle-contact-descent.md`
- `checkers/wp639_charged_cycle_contact_descent.py`
- `results/wp639_charged_cycle_contact_descent.json`

WP639 closes WP638's inaccessible-charged-pole branch algebraically. Exact
tree elimination of \(\chi\) gives a neutral dimension-twelve contact operator
with coefficient magnitude \(|L_A+L_B|^2/m_\chi^2\). The unit relative signs
remain distinguishable, with contact magnitudes four and zero. However, fixed
\(\mathcal I_\chi=1\) at charged masses one and two gives magnitudes four and
one, so the cycle record alone is not faithful to the contact response. This
is source-derived contact descent, not a `physical16` selector or calibrated
instrument; a typed light channel and detector likelihood remain required.

## Charged-cycle partonic instrument: WP640

- `flavor-charged-cycle-partonic-instrument.md`
- `checkers/wp640_charged_cycle_partonic_instrument.py`
- `results/wp640_charged_cycle_partonic_instrument.json`

WP640 supplies the first executable light-particle channel after frozen vev
insertion. The contact operator mediates massless
\(u_L\bar d_R\to u_L\bar d_R\) at fixed helicity and color, with
\(|\mathcal M|^2=G^2\hat s^2\) and
\(\hat\sigma=G^2\hat s/(16\pi)\). Unit constructive, destructive, and
mass-two contexts give normalized squared amplitudes sixteen, zero, and one.
This is a source-level partonic probe, not a hadronic or detector-calibrated
instrument. Its squared-only readout also retains a sign and phase kernel that
can be removed only by a source-authorized interfering amplitude.

## Charged-cycle Standard Model interference: WP641

- `flavor-charged-cycle-sm-interference.md`
- `checkers/wp641_charged_cycle_sm_interference.py`
- `results/wp641_charged_cycle_sm_interference.json`

WP641 exactly Fierz-maps the scalar contact into the chiral neutral-current
channel, where Standard Model photon and \(Z\) exchange provide an independent
source amplitude. For a common real normalization, the response is
\(R(B,G)=(B+G/2)^2\), so interference is linear in the contact coefficient.
This improves source-level sensitivity but cannot recover the phase of the
pre-contact current: the first nonfaithful arrow is already
\(J\mapsto|J|^2/m_\chi^2\). Detector authority still requires a named dataset,
PDFs, electroweak amplitudes, running, tagging, response, uncertainties, and a
likelihood.

## Single-current phase no-go: WP642

- `flavor-single-current-phase-no-go.md`
- `checkers/wp642_single_current_phase_no_go.py`
- `results/wp642_single_current_phase_no_go.json`

WP642 proves that the one-current invariant ring is generated by \(|g|^2\):
charge neutrality forces every invariant monomial \(g^m(g^*)^n\) to have
\(m=n\). The overall current phase is therefore presentation data, while a
second charged current would define a new relative experiment over its
stabilizer. Separately, messenger matching loses genuine UV cycle data: the
path pairs \((1,1)\) and \((1+i,1-i)\) both match to \(g=2\), but have cycle
ratios \(1\) and \(-i\). A low-energy single-current instrument cannot identify
the UV constructor or select `physical16`.

## Charged-cycle physical16 surjectivity: WP643

- `flavor-charged-cycle-physical16-surjectivity.md`
- `checkers/wp643_charged_cycle_physical16_surjectivity.py`
- `results/wp643_charged_cycle_physical16_surjectivity.json`

WP643 closes the charged-cycle branch against the fitted flavor objective.
With zero charged-scalar vev and tree-level neutral matching, four predeclared
charged contexts attach to every sheet of the complete stored 1,210-sheet
`physical16` ensemble. The 4,840-state product projects onto all 1,210 sheets
with uniform fiber size four. The charged operation partitions its carrier
fiber but selects no proper flavor family. Reopening requires a computed,
source-derived weak-basis-invariant backreaction with independent
normalization, ensemble survival, and a calibrated instrument.

## Charged-cycle one-loop backreaction: WP644

- `flavor-charged-cycle-one-loop-backreaction.md`
- `checkers/wp644_charged_cycle_one_loop_backreaction.py`
- `results/wp644_charged_cycle_one_loop_backreaction.json`

WP644 computes the first finite neutral-Yukawa backreaction on a frozen
one-generation, zero-momentum benchmark. The charged scalar closes the two
cross-edges, giving a positive five-propagator kernel. At equal masses,
\(K_5=1/(192\pi^2M^4)\), and the up/down Yukawa corrections are nonzero with
magnitude \(1/(192\pi^2)\) on the unit slice. Thus WP643's product theorem is
strictly tree-level. The correction is not a selector because its coupling,
vev, and mass coordinates remain free; the next gate is a generation-tensor
lift and `physical16` response-rank audit.

## Charged-cycle physical16 response rank: WP645

- `flavor-charged-cycle-physical16-response-rank.md`
- `checkers/wp645_charged_cycle_physical16_response_rank.py`
- `results/wp645_charged_cycle_physical16_response_rank.json`

WP645 lifts the loop through the frozen messenger tensors. Identity cross
intertwiners and identical up/down connector shapes force
\(\delta Y_u=\kappa_uY_u\) and \(\delta Y_d=\kappa_dY_d\). Quotienting common
right-handed phases leaves two real dilation directions. The exact
sixteen-by-two `physical16` Jacobian has rank two on every one of the 1,210
stored sheets: only common up/down mass scales move, while four mass ratios,
nine CKM moduli, and signed \(J\) do not. Since `physical16` is a faithful
embedding of the ten-dimensional quark quotient, the intrinsic codimension is
eight; fourteen is only the ambient record-rank deficit. Free opposite
dilations remain legal, so this is aligned backreaction and instrument
enrichment, not selection.

## Non-aligned word response ladder: WP646

- `flavor-nonaligned-word-response-ladder.md`
- `checkers/wp646_nonaligned_word_response_ladder.py`
- `results/wp646_nonaligned_word_response_ladder.json`

WP646 tests the smallest existing non-aligned word grammars against ten
algebraically independent weak-basis invariants at an exact nondegenerate
CP-violating witness. The intrinsic rank ladder is two for the aligned charged
loop, nine for identity plus three linear adjoint words per sector, and ten for
WP450's degree-two complete grammar. The linear layer has conditional
codimension-one tangent capacity, but its coefficients are not source-derived;
the degree-two layer restores universal fitting capacity. Neither is presently
a selector.

## Linear-word source authority: WP647

- `flavor-linear-word-source-authority.md`
- `checkers/wp647_linear_word_source_authority.py`
- `results/wp647_linear_word_source_authority.json`

WP647 applies the independently declared oriented (SO(3)) source symmetry to
WP646's rank-nine linear window. The common fixed space of the three triplet
generators is zero, so the original source authorizes no nonzero degree-one
coefficient. Its unique quadratic invariant is the Casimir and collapses to a
flavor-universal identity. Adding one oriented reference changes the groupoid
to its (SO(2)) stabilizer; the resulting identity-plus-one-word family has
exact response rank six at the hostile witness, not nine. The rank-nine window
therefore remains fitting capacity, not a source-generated selector.

## Triplet-quintet stabilizer obstruction: WP648

- `flavor-triplet-quintet-stabilizer-obstruction.md`
- `checkers/wp648_triplet_quintet_stabilizer_obstruction.py`
- `results/wp648_triplet_quintet_stabilizer_obstruction.json`

WP648 tests the smallest dynamical coefficient carrier suggested by WP452.
For one real triplet and one real quintet, the renormalizable orientation
equation generically aligns the triplet with a quintet eigenaxis. A nontrivial
proper half-turn fixes both fields, so the stationary vacuum retains at least
a \(\mathbb Z_2\) stabilizer. The carrier breaks and rigidifies the source
symmetry but does not construct a faithful oriented frame or select a
`physical16` point. A successor needs a second independently sourced
noncollinear object and a derived relative vacuum.

## Two-triplet faithful frame: WP649

- `flavor-two-triplet-faithful-frame.md`
- `checkers/wp649_two_triplet_faithful_frame.py`
- `results/wp649_two_triplet_faithful_frame.json`

WP649 supplies the minimal constructive frame repair: a positive quartic
action forces two ordered triplets to be orthonormal. Its vacuum Hessian has
three orbit zeros and three positive physical eigenvalues, while the ordered
pair has trivial (SO(3)) stabilizer. The induced identity-plus-two-word
family has exact intrinsic response rank eight at the hostile witness. This is
a source-generated faithful frame and rigidifier, but not a numerical flavor
selector; its sector couplings and physical matching remain to be derived.

## Faithful-frame coefficient nonselection: WP650

- `flavor-frame-coefficient-nonselection.md`
- `checkers/wp650_frame_coefficient_nonselection.py`
- `results/wp650_frame_coefficient_nonselection.json`

WP650 pulls the selector question through WP649's faithful frame. The allowed
identity-plus-two-word family has twelve real scalar controls, exact intrinsic
response rank eight, and a four-dimensional local control kernel. The scalar
coefficients are (SO(3)) singlets and remain unconstrained by the frame
action. Two legal packets already differ in the weak-basis invariant
\(\operatorname{Tr}(YY^\dagger)\). The construction is therefore a faithful
rigidifier plus constrained carrier, not a coefficient selector or source
identifier.

## Frame-messenger factorization kernel: WP651

- `flavor-frame-messenger-factorization-kernel.md`
- `checkers/wp651_frame_messenger_factorization_kernel.py`
- `results/wp651_frame_messenger_factorization_kernel.json`

WP651 attaches WP435-type one-stage messenger chains to WP650's six complex
frame coefficients. The exact matching map from twelve complex vertex
couplings has rank six and a six-complex-dimensional kernel: reciprocal vertex
rescalings preserve every low-energy coefficient. A hostile UV pair has the
same matched coefficient but different vertex strength. Matching therefore
makes the constrained carrier executable at low energy while selecting no
coefficient and identifying no UV constructor. Threshold-calibrated probes are
required to refine this quotient.

## Two-width threshold instrument: WP652

- `flavor-two-width-threshold-instrument.md`
- `checkers/wp652_two_width_threshold_instrument.py`
- `results/wp652_two_width_threshold_instrument.json`

WP652 derives two labelled partial-width ports from the same messenger
vertices as WP651. After phase-space calibration, their log-response to the
two vertex magnitudes has rank two and positive Gram determinant
\(16w_Lw_R\); either port alone has rank one. The ports distinguish WP651's
hostile constructors and repair magnitude identification in the ideal
threshold experiment. Finite widths, mixing, backgrounds, branching
reconstruction, resolution, efficiencies, and uncertainty-stable rank remain
the detector-calibration gate. The experiment identifies magnitudes but does
not select their numerical values.

## Two-width confusion robustness: WP653

- `flavor-two-width-confusion-robustness.md`
- `checkers/wp653_two_width_confusion_robustness.py`
- `results/wp653_two_width_confusion_robustness.json`

WP653 pushes WP652 through a symmetric detector-confusion channel. The exact
two-port response retains rank two unless the misclassification probability is
one half, where both reconstructed channels coincide and rank collapses to
one. For a calibrated uncertainty interval, robust identification requires
\(|1-2e_0|>2\delta_e\), with an explicit positive lower bound on the smallest
singular value. This is a conditional detector theorem; no experimental
confusion calibration is yet admitted.

## Finite-width template overlap: WP654

- flavor-finite-width-template-overlap.md
- checkers/wp654_finite_width_template_overlap.py
- results/wp654_finite_width_template_overlap.json

WP654 replaces abstract channel confusion by exact equal-width Lorentzian
templates. Their normalized overlap is
\(4\gamma^2/(\Delta^2+4\gamma^2)\); the two-template Gram matrix retains
rank two for every nonzero mass separation and collapses only at exact
degeneracy. Its smallest eigenvalue gives an explicit width-relative
conditioning gate. Detector convolution, unequal widths, backgrounds,
efficiencies, and calibrated uncertainties remain open.

## Gaussian detector-convolution pullback: WP655

- flavor-gaussian-convolution-pullback.md
- checkers/wp655_gaussian_convolution_pullback.py
- results/wp655_gaussian_convolution_pullback.json

WP655 separates the three detector gates. Finite-width Gaussian convolution
has a nowhere-zero Fourier transfer and therefore preserves exact object
separation: two convolved Lorentzian templates coincide only when both their
mass and width agree. Uniform completion stability nevertheless fails as the
mass-width pairs coalesce. A positive Gram lower bound defines an operational
target domain, not detector calibration. Resolution, backgrounds,
efficiencies, and uncertainty evidence remain required.

## Independent sideband background calibration: WP656

- flavor-sideband-background-calibration.md
- checkers/wp656_sideband_background_calibration.py
- results/wp656_sideband_background_calibration.json

WP656 profiles a common additive background nuisance in the two-width signal
records. Without independent calibration, the effective source information
has rank one and loses the common-rate mode. A declared background-only
sideband with precision \(\tau>0\) restores rank two, with determinant
\(16\tau/(\tau+2)\); stability fails as \(\tau\to0\). The calibration is
authorized only when sideband support and transfer factors are measured
independently of the target signal. It repairs identification, not selection.

## Independent efficiency-control calibration: WP657

- flavor-efficiency-control-calibration.md
- checkers/wp657_efficiency_control_calibration.py
- results/wp657_efficiency_control_calibration.json

WP657 profiles separate multiplicative efficiencies in the two width ports.
Without independent controls, both magnitude directions are exactly
confounded and the source information has rank zero. Two independently
supported efficiency controls restore a diagonal rank-two response with
determinant
\(16\kappa_L\kappa_R/((1+\kappa_L)(1+\kappa_R))\). Both positive
precisions are necessary. Their support and transfer factors must be bound
outside the target signal.

## Composed detector calibration: WP658

- flavor-composed-detector-calibration.md
- checkers/wp658_composed_detector_calibration.py
- results/wp658_composed_detector_calibration.json

WP658 composes the two signal records, two efficiency controls, and one
background sideband in a common detector frame. The exact five-record
Jacobian has determinant \(4q\sqrt{\kappa_L\kappa_R\tau}\), where \(q\)
is calibrated template contrast. Joint faithfulness holds exactly when all
four factors are nonzero; approaching any boundary destroys uniform
stability. This completes the ideal identification architecture but still
requires one actual experiment binding all records and covariance. It does
not select source values.

## CMS two-port experiment-support audit: WP659

- flavor-cms-two-port-support-audit.md
- checkers/wp659_cms_two_port_support_audit.py
- results/wp659_cms_two_port_support_audit.json

WP659 tests WP658 against two current CMS vectorlike-quark searches. The
analyses establish real Standard Model Higgs and exotic neutral-scalar ports,
control regions, and cross-section-times-branching-fraction limits. Neither
fits both decay widths simultaneously in one constructor frame or publishes
the two efficiency controls and joint covariance required to identify both
WP651 vertex magnitudes. The physical-instrument branch therefore closes as an
experiment-support gap rather than an algebraic one.

## Source-generated selector branch closure: WP660

- flavor-selector-branch-closure.md
- checkers/wp660_selector_branch_closure.py
- results/wp660_selector_branch_closure.json

WP660 closes the bounded selector branch. The two-triplet action genuinely
constructs a faithful oriented frame, its word family is a rank-eight
constrained carrier, messenger matching is executable but nonfaithful on UV
constructors, and an ideal calibrated detector could identify two magnitude
directions. No admitted source operation fixes the scalar coefficients or
selects a numerical physical16 family, and no current published analysis
realizes the complete detector packet. The present flavor result is therefore
rigidification plus carrier capacity, not source-generated selection.

## Two-triplet RG-closure repair: WP661

- flavor-two-triplet-rg-closure-repair.md
- checkers/wp661_two_triplet_rg_closure_repair.py
- results/wp661_two_triplet_rg_closure_repair.json

WP661 corrects WP649's source typing. The mixed frame vertex generates the
omitted \(|n|^2|m|^2\) counterterm at one loop, so the original potential was
tree-level rather than RG closed. Adding the missing quartic shifts the exact
orthogonal vacuum norms to \(2/3\) but retains three orbit zeros, three
positive physical modes, and trivial stabilizer. The faithful rigidifier
survives minimal support closure; complete beta functions and messenger
corrections remain outstanding, and no selector follows.

## Two-triplet scalar one-loop flow: WP662

- flavor-two-triplet-scalar-one-loop-flow.md
- checkers/wp662_two_triplet_scalar_one_loop_flow.py
- results/wp662_two_triplet_scalar_one_loop_flow.json

WP662 derives the complete one-loop flow within the closed scalar subsector:
two mass parameters and four quartics. The WP661 benchmark lies in an open
forward neighborhood with positive orthogonality coupling and increasing
radial stability determinant. This supplies local scalar-flow stability, not
messenger-complete RG authority; gauge, Yukawa, and messenger terms remain the
next source gate.

## Messenger-topology RG bifurcation: WP663

- flavor-messenger-topology-rg-bifurcation.md
- checkers/wp663_messenger_topology_rg_bifurcation.py
- results/wp663_messenger_topology_rg_bifurcation.json

WP663 proves that WP651's matched \(J_n,J_m\) word packet does not determine
its scalar RG completion. Disjoint messenger chains preserve the flip-even
support, while a shared spin-one messenger generates a quadratic cross term
and two flip-odd quartics. A topology and symmetry-charge assignment must be
frozen independently before messenger-complete beta functions exist. The
ambiguity is a constructor kernel, not a selector.

## Disjoint-messenger stability bound: WP664

- flavor-disjoint-messenger-stability-bound.md
- checkers/wp664_disjoint_messenger_stability_bound.py
- results/wp664_disjoint_messenger_stability_bound.json

WP664 freezes WP651's declared disjoint-chain branch. Each Dirac spin-one
messenger preserves the scalar operator support but subtracts from the norm
quartic flow. At the repaired benchmark the radial-margin derivative is
\(1136-32(F_n+F_m)\), so nonerosion requires
\(F_n+F_m\leq71/2\). The bound defines an admissible stability region; it
does not fix the free messenger couplings or select a flavor point.

## Messenger stability-cone leak: WP665

- flavor-messenger-stability-cone-leak.md
- checkers/wp665_messenger_stability_cone_leak.py
- results/wp665_messenger_stability_cone_leak.json

WP665 attacks finite-scale promotion of WP664. On the symmetric positive
boundary of the radial-stability cone, the completed vector field satisfies
\(dD/dt=-32F\lambda\). Every positive fixed disjoint-fermion strength points
outward, so the full cone is not forward invariant. Benchmark nonerosion is
only local; Yukawa running, threshold decoupling, and a smaller scale-bounded
domain are required.

## Kinetic-normalization descent: WP666

- flavor-kinetic-normalization-descent.md
- checkers/wp666_kinetic_normalization_descent.py
- results/wp666_kinetic_normalization_descent.json

WP666 restores the missing coordinate typing in WP664. Raw \(y^4\) changes
under scalar field rescaling; the descending strength is \(y^4/Z^2\), and the
descending radial margin includes the corresponding kinetic denominators.
Two raw packets with \((Z,y)=(1,1)\) and \((4,2)\) are canonically identical
but have raw fourth powers one and sixteen. The stability bound is therefore
conditional on a source-derived kinetic Gram, not a numerical selector.

## Flip-protected kinetic interface: WP667

- flavor-flip-protected-kinetic-interface.md
- checkers/wp667_flip_protected_kinetic_interface.py
- results/wp667_flip_protected_kinetic_interface.json

WP667 shows how the kinetic interface can exist. Extending the independent
triplet flips to the disjoint messenger source forces the species kinetic Gram
diagonal, after which a label-preserving canonical map is exact. Without those
flips a positive mixed Gram is legal and canonicalization mixes the frame
axes. The conditional repair fixes no canonical Yukawa and is therefore a
rigidifier, not a selector.

## Flip-charge single-pair no-go: WP668

- flavor-flip-charge-single-pair-no-go.md
- checkers/wp668_flip_charge_single_pair_no_go.py
- results/wp668_flip_charge_single_pair_no_go.json

WP668 solves the messenger parity equations. One massive vectorlike pair
cannot also carry a Yukawa linear in an odd triplet: its mass and Yukawa charge
conditions differ by one modulo two. The minimal protected channel uses two
opposite-parity pairs and off-diagonal triplet vertices. Applied literally to
WP651, the pair census rises from six to ten. Protected matching, supertraces,
thresholds, and anomalies must therefore be recomputed.

## Protected two-pair supertrace: WP669

- flavor-protected-two-pair-supertrace.md
- checkers/wp669_protected_two_pair_supertrace.py
- results/wp669_protected_two_pair_supertrace.json

WP669 recomputes the fermion loop on the equal-mass reciprocal-vertex slice of
the protected two-pair channel. Flip-even scalar support survives, but the
norm-quartic erosion doubles. The repaired benchmark has
\(dD/dt=1136-64(P_n+P_m)\), giving the exact nonerosion gate
\(P_n+P_m\leq71/4\). Unit protected WP651 multiplicities give derivative
880. No coupling or flavor point is selected.

## Protected vertex imbalance: WP670

- flavor-protected-vertex-imbalance.md
- checkers/wp670_protected_vertex_imbalance.py
- results/wp670_protected_vertex_imbalance.json

WP670 lifts the protected loop to unequal masses and independent reciprocal
vertices. Scalar support remains flip even, but quartic erosion depends on
\(y^4+z^4\), not only the tree-product coordinate \(yz\). Reciprocal rescaling
preserves matching while making erosion arbitrarily large; balanced vertices
uniquely minimize it. A balance law or two calibrated threshold widths is a
new source/instrument requirement, not a selector consequence.

## Protected threshold-port no-go: WP671

- flavor-protected-threshold-port-no-go.md
- checkers/wp671_protected_threshold_port_no_go.py
- results/wp671_protected_threshold_port_no_go.json

WP671 shows that reciprocal protected vertices do not yield two reciprocal
on-shell decay ports: the two threshold margins sum to \(-2m_n\). The single
ordinary unpolarized width has rank one and admits hostile vertex pairs with
equal width but different loop erosion. Rank-two identification requires a
source-derived polarization or angular analyzer in the one open channel, not
a formal second directional decay.

## Protected chirality analyzer: WP672

- flavor-protected-chirality-analyzer.md
- checkers/wp672_protected_chirality_analyzer.py
- results/wp672_protected_chirality_analyzer.json

WP672 constructs the ideal repair in the one open decay. Total rate
\(W=u+v\) plus signed chirality moment \(N=\alpha(u-v)\) has determinant
\(-2\alpha\) and reconstructs the loop erosion \(u^2+v^2\) exactly. Symmetric
helicity confusion collapses rank only at one half. The probe is source-derived
at amplitude level; a physical polarimeter and calibrated likelihood remain
unproved.

## Protected conditional Gram: WP673

- flavor-protected-conditional-gram.md
- checkers/wp673_protected_conditional_gram.py
- results/wp673_protected_conditional_gram.json

WP673 conditions the ideal two-port response on an independently declared
positive detector precision. The exact Gram determinant is
\(4\alpha^2(pq-r^2)\), and a positive uncertainty-stable lower bound follows
from separate analyzer and metric calibrations. Zero chirality precision
collapses the Gram to rank one. The theorem rejects covariance fitted from the
desired answer; a named physical polarimeter remains absent.

## Source-derived cascade polarimeter: WP674

- flavor-source-derived-cascade-polarimeter.md
- checkers/wp674_source_derived_cascade_polarimeter.py
- results/wp674_source_derived_cascade_polarimeter.json

WP674 finds a source-derived ideal polarimeter in the existing route:
protected \(A\to B+n\) followed by the chiral exit \(B\to q_R+X\). An exact
charge table preserves the flip, and a positive-mass witness opens both cascade
stages. In the ideal limit, total rate plus the signed exit-quark angular
moment has determinant minus two. Finite-mass transfer and an actual calibrated
detector analysis remain absent.

## Finite-mass cascade response: WP675

- flavor-finite-mass-cascade-response.md
- checkers/wp675_finite_mass_cascade_response.py
- results/wp675_finite_mass_cascade_response.json

WP675 derives the finite-mass rate and signed angular kernels on the
positive-real, narrow-width protected slice. Their exact nonlinear Jacobian is
nonzero throughout the open threshold domain and collapses at the exact parent
threshold. The mass interference term does not erase rank. Complex phase,
finite width, off-shell transport, reconstruction, and detector calibration
remain open.

## Exchange-balance UV selector: WP676

- flavor-exchange-balance-uv-selector.md
- checkers/wp676_exchange_balance_uv_selector.py
- results/wp676_exchange_balance_uv_selector.json

WP676 tests the simplest Deutschian explanation of vertex balance. Exact
partner exchange of the internal mass block forces equal masses and reciprocal
vertices and uniquely minimizes loop erosion at fixed product. WP681 corrects
its authority: independently typed entrance and exit endpoints break the
exchange, so this is an internal-block rigidifier, not a full source selector.

## Contextual cascade quotient: WP677

- flavor-contextual-cascade-quotient.md
- checkers/wp677_contextual_cascade_quotient.py
- results/wp677_contextual_cascade_quotient.json

WP677 types the finite-mass cascade at endpoint, analyzer, phase-frame, and
ordered-factorization levels. The signed analyzer removes the endpoint swap
fiber on the real-positive interior, but complex conjugation and generic phase
fibers survive, distinct ordered constructors can give the same composite
record, and full algebraic rank has no uniform detector authority without an
independent positive precision bound. Context saturation is currently only
under the identity preparation; any enlarged source preparation family must
be closed explicitly before cascade substitution is admitted.

## Native CP-odd port no-go: WP678

- flavor-native-cp-odd-port-no-go.md
- checkers/wp678_native_cp_odd_port_no_go.py
- results/wp678_native_cp_odd_port_no_go.json

WP678 answers the Deutschian phase question negatively for the admitted
unpolarized cascade. Three-body momentum closure makes the momentum-only
scalar triple product identically zero, so the native record remains invariant
under complex conjugation. An oriented spin or beam reference can supply a
rank-restoring sine-phase port, but that is a new polarized relational
experiment with a changed stabilizer groupoid, not recovery of an absolute
phase from the original cascade.

## Identical-beam orientation no-go: WP679

- flavor-identical-beam-orientation-no-go.md
- checkers/wp679_identical_beam_orientation_no_go.py
- results/wp679_identical_beam_orientation_no_go.json

WP679 tests the smallest collider reference. At an unpolarized identical-beam
proton-proton source, the signed CP port is odd under beam exchange and its
untagged expectation vanishes. Squaring erases the phase sign. A source-derived
beam-odd event tag would make the relational product descend, but no such
associated-production constructor or calibrated tag is currently admitted.

## Associated-production beam tag: WP680

- flavor-associated-production-beam-tag.md
- checkers/wp680_associated_production_beam_tag.py
- results/wp680_associated_production_beam_tag.json

WP680 finds the missing source constructor algebraically. The admitted
entrance Yukawa and messenger QCD color generate (qg\to AH); the sign of the
associated-system rapidity is beam odd, so its product with the beam-oriented
CP statistic descends under identical-beam exchange. Nonzero calibrated tag
dilution restores generic phase rank. Finite matrix-element synthesis, PDFs,
reconstruction, dilution, covariance, and context saturation remain separate
physical-instrument gates.

## Full-grammar exchange audit: WP681

- flavor-full-grammar-exchange-audit.md
- checkers/wp681_full_grammar_exchange_audit.py
- results/wp681_full_grammar_exchange_audit.json

WP681 corrects WP676 by testing the full route rather than its internal mass
block. Fixed entrance and exit currents break partner exchange. On the balanced
block, the frame fluctuation becomes diagonal in the physical pole basis, so
the cross-pole cascade used by WP674 vanishes exactly. Exchange balance is
therefore a conditional internal rigidifier and minimizer, not a genuine
source selector, and it cannot be combined with the proposed analyzer route.

## Balance-analyzer tradeoff: WP682

- flavor-balance-analyzer-tradeoff.md
- checkers/wp682_balance_analyzer_tradeoff.py
- results/wp682_balance_analyzer_tradeoff.json

WP682 extends the WP681 closure away from the exact locus. With mass detuning
(\Delta=M_A-M_B), the cross-pole frame vertex is
(y\Delta/\sqrt{\Delta^2+4m^2}). Analyzer amplitude vanishes linearly and its
information weight quadratically as exchange balance is approached. The
proposed selector and analyzer are structurally antagonistic; a successor
requires a different source-derived operator that does not commute with the
balanced mass block.

## Endpoint-interference reference gate: WP683

- flavor-endpoint-interference-reference-gate.md
- checkers/wp683_endpoint_interference_reference_gate.py
- results/wp683_endpoint_interference_reference_gate.json

WP683 finds that the typed entrance and exit projectors do not commute with the
balanced mass tensor, but the isolated cross-endpoint probability remains even
in the mixing sign and depends only on the magnitude of complex mixing. A
coherent amplitude into the same external channel would restore sign-sensitive
interference. No independently normalized same-channel reference amplitude is
currently admitted, so algebraic noncommutation is not executable phase
control.

## Exit-flavon Higgs-portal typing: WP684

- flavor-exit-flavon-higgs-portal-typing.md
- checkers/wp684_exit_flavon_higgs_portal_typing.py
- results/wp684_exit_flavon_higgs_portal_typing.json

WP684 rejects transport of the older trace-adjoint Higgs portal to the
messenger exit field. The latter is an (SU(3)_F) adjoint and (SO(3)_P)
vector, so no invariant linear Higgs portal exists. The lowest legal term is
(\lambda_p(H^\dagger H)(X\cdot X)), which induces radial mixing only after a
nonzero exit vacuum is derived. The complete mixed potential, portal
coefficient, and common-frame vacuum are not currently admitted, leaving this
as a typed candidate rather than a coherent reference amplitude.

## Radial portal vacuum: WP685

- flavor-radial-portal-vacuum.md
- checkers/wp685_radial_portal_vacuum.py
- results/wp685_radial_portal_vacuum.json

WP685 declares the minimal radial Higgs/exit-flavon potential and proves that
a stable nonzero mixed vacuum exists on an open source domain. The exact mixing
entry is (2\lambda_phx). However, the same grammar permits
(\lambda_p=0), leaving independent stable vacua and no coherent reference.
This is an existence constructor, not a selector or a completion-safe full
scalar model; orientation invariants, RG closure, and exclusion of the
zero-portal stratum remain open.

## Radiative exit-Higgs portal: WP686

- flavor-radiative-exit-higgs-portal.md
- checkers/wp686_radiative_exit_higgs_portal.py
- results/wp686_radiative_exit_higgs_portal.json

WP686 closes the zero-portal truncation at one loop. The ordinary quark Yukawa
and messenger exit Yukawa share (q_R), and
(\operatorname{Tr}[(MM^\dagger)^2]) contains
(2y_q^2y_X^2h^2x^2) per color. The quadratic Higgs-exit portal is therefore
a required counterterm when both Yukawas are nonzero. This is source-generated
operator support and radiative rigidification, not numerical selection: a
renormalized boundary value can still cancel the portal at one scale, and the
full beta and finite threshold remain open.

## Exit-portal threshold matching: WP687

- flavor-exit-portal-threshold-matching.md
- checkers/wp687_exit_portal_threshold_matching.py
- results/wp687_exit_portal_threshold_matching.json

WP687 computes the finite one-loop heavy-messenger threshold on the declared
radial modified-minimal-subtraction slice. For
(V\supset\lambda_ph^2x^2/2), matching at (mu=M_B) gives
(\delta\lambda_p=N_cy_q^2y_X^2/(4\pi^2)>0). This fixes the sign and
normalization of one source-derived threshold contribution. It does not fix
the total portal because the independent UV boundary coupling, additional
messengers, orientation invariants, and subsequent running remain free.

## Flavor-Gram portal threshold: WP688

- flavor-gram-portal-threshold.md
- checkers/wp688_flavor_gram_portal_threshold.py
- results/wp688_flavor_gram_portal_threshold.json

WP688 lifts the threshold to the full flavor tensor. Its source factor is the
positive pairing
(P=\operatorname{Tr}[(Y_q^\dagger Y_q)(Y_X^\dagger Y_X)]), a weighted sum
of squares in the quark-mass basis. With all ordinary quark Yukawas nonzero,
the pairing is faithful on nonzero exit tensors; for the canonical exit shape
it is the sum of the three squared Yukawas. This rigidifies positive threshold
support without selecting the total renormalized portal. An exactly massless
quark direction is the boundary kernel.

## Affine portal comparison theorem: WP689

- flavor-two-scale-portal-cancellation-no-go.md
- checkers/wp689_two_scale_portal_cancellation_no_go.py
- results/wp689_two_scale_portal_cancellation_no_go.json

WP689 proves the affine theorem that an independent boundary can hide a
response in only one of two distinct contexts. For (lambda_p(L)=a+bL), the
two-context determinant is (L_2-L_1) and the exact boundary-independent floor
is (b|L_2-L_1|/2). WP690 withdraws the original assignment of probe authority
to distinct renormalization-scale choices: (L_1,L_2) must instead be distinct
source-authorized physical contexts.

## Renormalization scale is not a physical probe: WP690

- flavor-renormalization-scale-noninstrument.md
- checkers/wp690_renormalization_scale_noninstrument.py
- results/wp690_renormalization_scale_noninstrument.json

WP690 combines running with the explicit fixed-momentum logarithm and proves
that (F(Q;mu)=a+b log(Q/mu_0)) is independent of (mu). Renormalization-scale
variation therefore cannot supply complementary observations. Distinct
physical momenta retain the affine determinant (log(Q_2/Q_1)) and remove the
boundary parameter in their difference, but this becomes an admitted probe
only after a finite-momentum same-channel amplitude and two calibrated
momentum-bin measurements are constructed.

## Spacelike threshold context: WP691

- flavor-spacelike-threshold-context.md
- checkers/wp691_spacelike_threshold_context.py
- results/wp691_spacelike_threshold_context.json

WP691 replaces scale variation with the smallest genuine momentum context.
The once-subtracted equal-mass Euclidean threshold kernel is strictly
increasing in (Q^2/M^2), so two distinct momenta give a rank-two affine
response while the local heavy-mass limit remains rank one. This is a physical
context mechanism, not yet the full messenger four-point amplitude or a
calibrated exit-flavon instrument.

## Visible Higgs-port mixing kernel: WP692

- flavor-higgs-port-mixing-kernel.md
- checkers/wp692_higgs_port_mixing_kernel.py
- results/wp692_higgs_port_mixing_kernel.json

WP692 propagates a momentum-dependent radial mixing response through the
ordinary visible Higgs port. Two distinct bins are locally rank two when both
mixings are nonzero, but the readout is even in the mixing and therefore
retains the global pair identification ((a,b),(-a,-b)). The construction
supplies a legal detector projection, not a calibrated instrument or selector;
the full messenger self-energy and detector response remain open.

## Hidden-port sign groupoid: WP693

- flavor-hidden-port-sign-groupoid.md
- checkers/wp693_hidden_port_sign_groupoid.py
- results/wp693_hidden_port_sign_groupoid.json

WP693 retypes the WP692 sign pair. On the reduced radial two-point domain,
changing the mixing sign is conjugation by the hidden-port reflection that
fixes the visible Higgs source vector. The two signs are therefore one
visible-port operational class, not yet two inequivalent `physical16` points.
An exit-sensitive cross port distinguishes them only by defining a richer
relational experiment over a smaller stabilizer groupoid.

## Full-source visible-port hostile pair: WP694

- flavor-full-source-visible-port-hostile-pair.md
- checkers/wp694_full_source_visible_port_hostile_pair.py
- results/wp694_full_source_visible_port_hostile_pair.json

WP694 lifts the sign audit to the complete radial source. Retuning only the
quadratic masses constructs two stable opposite-portal branches with identical
vacuum norms, pole polynomial, and visible Higgs two-point resolvents. Their
mixed fourth derivatives remain opposite and invariant under radial sign
changes. The first nonfaithful arrow is therefore the reduction from the full
radial source to the visible two-point packet.

## Visible cubic branch separator: WP695

- flavor-visible-cubic-branch-separator.md
- checkers/wp695_visible_cubic_branch_separator.py
- results/wp695_visible_cubic_branch_separator.json

WP695 repairs the WP694 hostile pair on an exact stable radial slice. Both
portal-sign branches have spectrum ({1,5}) and equal visible overlaps, but the
on-shell heavy-to-two-light cubic is (7 sqrt(2)/2) on the positive branch and
zero on the negative branch. This is a source-derived visible branch separator
and candidate instrument topology, not a selector of which branch is realized.

## Cubic separator corridor: WP696

- flavor-cubic-separator-corridor.md
- checkers/wp696_cubic_separator_corridor.py
- results/wp696_cubic_separator_corridor.json

WP696 promotes the WP695 witness to the full symmetric corridor
(3/5<p/lambda<1). Stability and on-shell kinematics hold throughout;
the positive-portal cubic is strictly nonzero while the negative-portal cubic
vanishes identically. This is a continuum ideal-rate separator on a declared
slice, still awaiting asymmetric completion and detector calibration.

## Asymmetric cubic lifting: WP697

- flavor-asymmetric-cubic-lifting.md
- checkers/wp697_asymmetric_cubic_lifting.py
- results/wp697_asymmetric_cubic_lifting.json

WP697 attacks the symmetry-slice zero. A quartic asymmetry leaves the two
portal branches isospectral but lifts the negative-branch cubic linearly,
while the positive branch has no linear correction. The completion-stable
claim is therefore an asymmetry-suppressed rate hierarchy, not an exactly
forbidden decay.

## Finite-asymmetry cubic hierarchy: WP698

- flavor-finite-asymmetry-cubic-hierarchy.md
- checkers/wp698_finite_asymmetry_cubic_hierarchy.py
- results/wp698_finite_asymmetry_cubic_hierarchy.json

WP698 gives the exact finite-asymmetry result. In the positive mass-basis
coordinate (t), the branch amplitude ratio is ((t-1)/(t+1)) and the ideal rate
ratio is its square. The hierarchy is strict throughout the stable open-decay
domain for every finite positive (t), but still identifies rather than selects.

## Detector contrast budget: WP699

- flavor-detector-contrast-budget.md
- checkers/wp699_detector_contrast_budget.py
- results/wp699_detector_contrast_budget.json

WP699 shows why pointwise cubic separation is not uniformly faithful. On a
source-authorized reciprocal support window (1/T<=t<=T), the exact contrast
floor is (4T/(T+1)^2) and yields a finite signal-versus-uncertainty budget.
Without finite source support, the uniform floor vanishes. Detector calibration
and the source derivation of that support remain open.

## Stability-authorized contrast floor: WP700

- flavor-stability-authorized-contrast-floor.md
- checkers/wp700_stability_authorized_contrast_floor.py
- results/wp700_stability_authorized_contrast_floor.json

WP700 derives the missing support from source stability itself. On the
declared coupling corridor (1<lambda/p<5/3), every stable asymmetry lies in an
exact reciprocal (t) interval and the ideal branch contrast is uniformly
greater than three quarters. The corridor remains unselected and detector
calibration remains open.

## Coupling-corridor nonselection: WP701

- flavor-coupling-corridor-nonselection.md
- checkers/wp701_coupling_corridor_nonselection.py
- results/wp701_coupling_corridor_nonselection.json

WP701 closes the selector overreach. Stability requires only (lambda/p>1),
not the WP700 upper bound (lambda/p<5/3); an exact stable witness at ratio two
has closed cubic phase space. The same grammar also admits a stable zero-portal
stratum. Stability rigidifies support conditionally but does not select either
the instrument corridor or a portal branch.

## Affine matching nonselection: WP702

- flavor-affine-matching-nonselection.md
- checkers/wp702_affine_matching_nonselection.py
- results/wp702_affine_matching_nonselection.json

WP702 proves that finite threshold and transport corrections cannot select the
WP700 corridor while the two UV quartic boundaries remain independently free.
The matching map is an affine bijection and reaches inside, outside, and
zero-portal targets. Radiative support is a rigidifier; selection requires a
new noninvertible UV boundary constructor.

## Copositive boundary cancellation: WP703

- flavor-copositive-boundary-cancellation.md
- checkers/wp703_copositive_boundary_cancellation.py
- results/wp703_copositive_boundary_cancellation.json

WP703 closes the proposed positivity repair. Both radial quartic copositivity
and the stronger mixed-vacuum Hessian condition admit negative UV portal
boundaries. The exact stable witness with self-couplings two, positive
threshold one, and UV portal minus one has zero low-energy portal. Stability
therefore rigidifies the admissible domain but does not select nonzero portal
support or the WP700 ratio corridor.

## Scalar projective infrared ray: WP704

- flavor-scalar-projective-ir-ray.md
- checkers/wp704_scalar_projective_ir_ray.py
- results/wp704_scalar_projective_ir_ray.json

WP704 finds a source-derived candidate selector in the closed WP662 scalar
flow. On the symmetric positive subspace, the ratio flow has rays one half and
three halves; strict radial stability excludes the lower ray, and the full
stable basin approaches three halves at the Gaussian infrared limit. At every
finite matching scale the trajectory constant remains visible. The result is
therefore an asymptotic tangent-cone selector and finite-scale rigidifier, not
yet a `physical16` selector. Full gauge, Yukawa, messenger, threshold, and
instrument completion are the decisive gates.

## Projective-ray transverse saddle: WP705

- flavor-projective-ray-transverse-saddle.md
- checkers/wp705_projective_ray_transverse_saddle.py
- results/wp705_projective_ray_transverse_saddle.json

WP705 attacks the WP704 ray in the full four-quartic WP662 scalar family. The
symmetric-ratio and triplet-asymmetry modes are infrared-attractive, but the
independently allowed coefficient of ((n\mathbin\cdot m)^2) has projective
exponent minus (112\rho) and is infrared-repulsive. A positive infinitesimal
coefficient is compatible with boundedness. The ray is therefore an infrared
saddle, and its apparent selection depends on the unselected invariant slice
(lambda_c=0).

## Correlation-forbidding symmetry tradeoff: WP706

- flavor-c-forbidding-symmetry-tradeoff.md
- checkers/wp706_c_forbidding_symmetry_tradeoff.py
- results/wp706_c_forbidding_symmetry_tradeoff.json

WP706 tests the obvious symmetry repair for WP705. Independent rotations of
the two triplets forbid the correlation quartic, but also remove the angular
term that rigidifies their relative frame. The norm-only Hessian has four zero
modes against a three-dimensional diagonal orbit, leaving one physical angle
flat. Coupling both triplets to one quark or messenger flavor space breaks the
product symmetry back to the diagonal and permits the quartic again. A viable
repair needs a different grading that protects the slice without destroying
the common faithful frame.

## Two-vector angular invariant no-go: WP707

- flavor-two-vector-angular-invariant-no-go.md
- checkers/wp707_two_vector_angular_invariant_no_go.py
- results/wp707_two_vector_angular_invariant_no_go.json

WP707 completes the invariant grammar behind WP706. For two real triplets with
diagonal (SO(3)), independent flips, and field degree at most four, the only
relative-angle invariant is ((n\mathbin\cdot m)^2). The angular stiffness at
an orthogonal frame is exactly (2\lambda_c), so protecting
(lambda_c=0) makes the angle physically flat. No alternative symmetry label
on the same renormalizable field content can preserve both slice protection
and frame rigidity. A reopening must enlarge the source grammar or find a
full-domain attractive ray with nonzero (lambda_c).

## Full scalar nonzero-correlation ray no-go: WP708

- flavor-full-scalar-nonzero-c-ray-no-go.md
- checkers/wp708_full_scalar_nonzero_c_ray_no_go.py
- results/wp708_full_scalar_nonzero_c_ray_no_go.json

WP708 closes WP707's remaining same-field ray branch for the complete WP662
scalar one-loop flow. Exact elimination finds only two real rays with nonzero
correlation coupling: both have self-to-cross ratios one half and correlation
ratio one or two. Their radial stability margin is exactly zero. Thus the
(lambda_c=0) ray is an infrared saddle, while every real
(lambda_c\ne0) ray is radially marginal. A progressive successor must
derive additional beta contributions from a completed source and displace a
ray into the strict-stability interior.

## Beta-displacement acceptance functional: WP709

- flavor-beta-displacement-acceptance-functional.md
- checkers/wp709_beta_displacement_acceptance_functional.py
- results/wp709_beta_displacement_acceptance_functional.json

WP709 computes the exact first-order repair condition at the regular WP708
boundary ray. For completion corrections ((N,M,X,C)), the radial stability
margin responds as ((N+M-X)/28); the correlation-beta correction is radially
invisible at first order. This is a source-typing acceptance functional, not a
selector: the correction signs remain unauthorized until derived from one
completed gauge-Yukawa-messenger or new-field action.

## Wavefunction running is radially null: WP710

- flavor-wavefunction-running-radial-null.md
- checkers/wp710_wavefunction_running_radial_null.py
- results/wp710_wavefunction_running_radial_null.json

WP710 applies the WP709 gate to the largest model-independent correction
class. Independent triplet normalizations leave both
(lambda_n\lambda_m/\lambda_x^2) and (lambda_c/\lambda_x) exactly invariant.
Their anomalous-dimension contributions obey (N+M-X=0) for arbitrary unequal
field anomalous dimensions. Wavefunction running is therefore presentation
transport, not a stability-opening selector. Only genuine vertex corrections
can reopen the marginal ray.

## Disjoint-messenger ray displacement: WP711

- flavor-disjoint-messenger-ray-displacement.md
- checkers/wp711_disjoint_messenger_ray_displacement.py
- results/wp711_disjoint_messenger_ray_displacement.json

WP711 applies the WP709 gate to the existing source-authorized WP664 Dirac
messenger vertex correction. Disjoint chains give (N=-8F_n), (M=-8F_m),
and (X=0), hence radial displacement
(-2(F_n+F_m)/7). Every nontrivial chain moves the marginal ray toward
instability, consistently with WP665's exact cone-leak sign. A progressive
repair now requires an independently derived mixed or bosonic vertex channel
whose complete signed contribution outweighs this erosion.

## Bosonic vertex contrast gate: WP712

- flavor-bosonic-vertex-contrast-gate.md
- checkers/wp712_bosonic_vertex_contrast_gate.py
- results/wp712_bosonic_vertex_contrast_gate.json

WP712 constructs the minimal conditional bosonic reopening. A heavy real boson
with mass squared (M^2+g_n|n|^2+g_m|m|^2) supplies the positive Gram contrast
(kappa(g_n-g_m)^2). Combined with WP711, the marginal ray opens only when
(kappa(g_n-g_m)^2>8(F_n+F_m)). This is an algebraically progressive signed
vertex mechanism, not yet a flavor selector: the boson, counterterm channel,
thresholds, transverse basin, and calibrated readout remain to be derived from
one frozen source.

## Bosonic-portal scalar RG closure: WP713

- flavor-bosonic-portal-scalar-rg-closure.md
- checkers/wp713_bosonic_portal_scalar_rg_closure.py
- results/wp713_bosonic_portal_scalar_rg_closure.json

WP713 closes the scalar RG grammar of the WP712 extension. The Hessian
supertrace generates exactly seven quartics and fixes the bosonic contrast
normalization to four, so radial opening against WP711 requires
((g_n-g_m)^2>2(F_n+F_m)). The portal and boson self-couplings run and cannot
be treated as frozen response knobs. Full projective-ray and transverse-basin
classification is now the next gate.

## Exchange-symmetric bosonic ray no-go: WP714

- flavor-exchange-symmetric-bosonic-ray-no-go.md
- checkers/wp714_exchange_symmetric_bosonic_ray_no_go.py
- results/wp714_exchange_symmetric_bosonic_ray_no_go.json

WP714 solves the correlation-bearing exchange-symmetric sector of WP713.
There are four real rays, all with self-to-mixed ratio one half, zero bosonic
portal contrast, and radial margin zero. The boson self-coupling distinguishes
some rays but does not open stability. Any progressive bosonic ray must
therefore break triplet exchange and pass the full asymmetric basin test.

## Abelian moment-map selector obstruction: WP715

- flavor-abelian-moment-map-selector-obstruction.md
- checkers/wp715_abelian_moment_map_selector_obstruction.py
- results/wp715_abelian_moment_map_selector_obstruction.json

WP715 tests the first genuinely hard-to-vary source principle. One gauged
Abelian moment map fixes portal signs and relative magnitudes through quantized
charges, but its quartic Gram is identically rank one: the radial margin is
zero for every charge assignment, and no angular stiffness is generated. The
complete explanation therefore needs a rank-at-least-two non-Abelian or
multi-moment-map geometry rather than one charge square.

## Rank-two moment-map partial repair: WP716

- flavor-rank-two-moment-map-partial-repair.md
- checkers/wp716_rank_two_moment_map_partial_repair.py
- results/wp716_rank_two_moment_map_partial_repair.json

WP716 proves that two positive moment-map directions repair the WP715 radial
obstruction exactly: the stability margin is the weighted squared area of the
two triplet charge vectors. A minimal integer charge packet also forces
opposite portal signs. The repair is incomplete because common gauge-metric
rescaling leaves the charge geometry intact while changing the absolute portal
magnitude, norm-only maps produce no angular stiffness, and RG attraction,
nondecoupling threshold support, and calibrated source-incidence readout remain
unconstructed. The next source candidate must therefore unify the metric and
generate angular structure, rather than merely add an adjustable Abelian
factor.

## Non-Abelian real-triplet moment-map no-go: WP717

- flavor-nonabelian-real-triplet-moment-map-no-go.md
- checkers/wp717_nonabelian_real_triplet_moment_map_no_go.py
- results/wp717_nonabelian_real_triplet_moment_map_no_go.json

WP717 tests the direct unified non-Abelian repair on the admitted real-triplet
domain. The adjoint moment map is proportional to the conjugate cross product
and vanishes identically on the real slice. Parallel and orthogonal real
frames therefore have different faithful angular coordinates but identical
zero moment-map readout. Complex or cotangent directions repair the algebra
only by adding a reference port and changing the state domain. The surviving
source class is a real-triplet tensor or F-term constraint whose coefficient,
RG basin, threshold support, and instrument must all be derived together.

## Auxiliary-square portal Gram no-go: WP718

- flavor-auxiliary-square-portal-gram-no-go.md
- checkers/wp718_auxiliary_square_portal_gram_no_go.py
- results/wp718_auxiliary_square_portal_gram_no_go.json

WP718 classifies the complete family of real triplet auxiliary channels linear
in the portal field. Their induced portal matrix is the positive Gram
\(K=\kappa C^TC\). Independent flips require orthogonal Clebsch columns;
source exchange then forces equal norms and zero portal contrast. Unequal
representation-fixed Clebsches can rigidify a ratio, but common rescaling
changes the magnitude and the portal square supplies no angular stiffness.
The next progressive candidate must therefore combine a representation-fixed
unequal Clebsch packet with gauge–Yukawa normalization and a shared angular
constraint, rather than invoke a generic F-term.

## Gauge–Yukawa normalization fixed-point gate: WP719

- flavor-gauge-yukawa-normalization-fixed-point-gate.md
- checkers/wp719_gauge_yukawa_normalization_fixed_point_gate.py
- results/wp719_gauge_yukawa_normalization_fixed_point_gate.json

WP719 ties the Clebsch Gram normalization to a gauge coupling. This fixes the
portal ratio and the contrast sign once representations are fixed, but the
one-loop gauge trajectory retains its boundary value and selects no nonzero
magnitude. The minimal magnitude-selector candidate is an interacting zero of
the completed gauge–Yukawa–quartic beta system. Its matter content must fix the
beta coefficients, its full stability matrix must supply the basin, and its
threshold and labelled detector maps must preserve the same contrast.

## Fixed-point threshold readout factorization: WP720

- flavor-fixed-point-threshold-readout-factorization.md
- checkers/wp720_fixed_point_threshold_readout_factorization.py
- results/wp720_fixed_point_threshold_readout_factorization.json

WP720 factors the proposed selector into fixed point, relevant deformation,
threshold matching, and detector response. For affine matching
\(p_{\mathrm{low}}=p_*+A\rho\), contrast survives arbitrary threshold motion exactly
when \(dA=0\), unless the source uniquely fixes the visible components of
\(\rho\). An unlabelled total detector channel then kills the contrast even
when threshold matching preserves it; two calibrated representation-labelled
channels retain it. The required explanation must select a complete relevant
trajectory and its instrument, not merely a fixed point.

## Safe-separatrix transmutation-scale fiber: WP721

- flavor-safe-separatrix-transmutation-scale-fiber.md
- checkers/wp721_safe_separatrix_transmutation_scale_fiber.py
- results/wp721_safe_separatrix_transmutation_scale_fiber.json

WP721 tests the established asymptotically safe gauge–Yukawa source class.
Its interacting fixed point and one-dimensional safe critical surface fix
projective coupling data and transverse directions, but the trajectory retains
one translation constant, equivalently a dimensional-transmutation scale. The
portal at a fixed experimental energy varies along this fiber. A complete
source explanation must derive the relevant deformation amplitude from a
physical normalization or explicitly retain one measured dimensionful input;
detector calibration cannot be reused as source selection.

## Autonomous RG translation no-go: WP722

- flavor-autonomous-rg-translation-no-go.md
- checkers/wp722_autonomous_rg_translation_no_go.py
- results/wp722_autonomous_rg_translation_no_go.json

WP722 generalizes the WP721 residual to every autonomous dimensionless RG
system. Time translation preserves each nonconstant solution and all its
projective relations while changing any readout with nonzero Lie derivative
along the beta vector field. The orbit and basin can be rigidified without
selecting their placement at a physical energy. The minimal repair is a
source-authorized dimensionful boundary condition. No admitted flavor object
currently provides that anchor; measured electroweak or detector scales cannot
be promoted into source authority without a named interface constructor.

## Existing common-clock anchor audit: WP723

- flavor-existing-common-clock-anchor-audit.md
- checkers/wp723_existing_common_clock_anchor_audit.py
- results/wp723_existing_common_clock_anchor_audit.json

WP723 tests WP489, the closest admitted mass-generation candidate, against the
WP722 anchor gate. Its common singlet propagates one clock into every flavor,
electroweak, connector, and messenger mass, but common dilation of the input
\(w\) changes all absolute masses. Even after fixing the electroweak norm,
WP537 and WP543 leave one exact coefficient tangent that changes the flavor
clock ratio while preserving every admitted equality and strict threshold
support. The common source is therefore a parallelizer and conditional
relational selector, not a derived anchor or numerical portal selector.

## Clock-locked conditional selector: WP724

- flavor-clock-locked-conditional-selector.md
- checkers/wp724_clock_locked_conditional_selector.py
- results/wp724_clock_locked_conditional_selector.json

WP724 states the maximal noncircular explanation conditional on one
independently calibrated clock. A representation-fixed Clebsch contrast, an
interacting gauge–Yukawa normalization, a fully attractive dimensionless
critical surface, a source equality locking the crossover and messenger scales
to the common singlet, and two calibrated representation-labelled channels
would jointly fix portal sign, magnitude, mass ratios, and readout. The exact
composition works, but no admitted matter theory, matching calculation, or
actual experiment realizes all antecedents. This is an acceptance
specification, not a promoted flavor theorem.

## Real-triplet Abelian-charge typing no-go: WP725

- flavor-real-triplet-abelian-charge-typing-no-go.md
- checkers/wp725_real_triplet_abelian_charge_typing_no_go.py
- results/wp725_real_triplet_abelian_charge_typing_no_go.json

WP725 repairs a hidden carrier defect in WP715–WP716. The commutant of the real
irreducible \(SO(3)\) triplet is scalar, and kinetic-metric preservation forces
every commuting continuous Abelian generator to zero. Nonzero charge requires
doubling the real carrier to install a complex structure, changing the state
domain and physical groupoid. The moment-map identities remain conditional on
that enlargement. The progressive branch must put representation asymmetry in
charged messengers or auxiliaries and prove mediated descent back to the real
triplet quotient.

## Charged-scalar messenger descent nonselection: WP726

- flavor-charged-scalar-messenger-descent-nonselection.md
- checkers/wp726_charged_scalar_messenger_descent_nonselection.py
- results/wp726_charged_scalar_messenger_descent_nonselection.json

WP726 constructs the minimal mediated repair of WP725. Heavy charged scalars
couple through neutral real-triplet norms, and their one-loop determinant
descends to the original quotient. The exact mixed curvature proves portal
support, but its finite value vanishes at the natural scalar matching scale,
changes sign with matching presentation, and is cancellable by an allowed
renormalized boundary coupling. Representation multiplicity fixes only an
integer prefactor; continuous vertex products remain. Mediated charge repairs
typing and may supply labelled ports, but it does not select the portal.

## Safe flavor-portal exchange no-go: WP727

- flavor-safe-flavor-portal-exchange-no-go.md
- checkers/wp727_safe_flavor_portal_exchange_no_go.py
- results/wp727_safe_flavor_portal_exchange_no_go.json

WP727 audits a concrete anomaly-free asymptotically safe flavor-portal model
class. Its admitted Higgs portal is proportional to
\((H^\dagger H)\operatorname{Tr}(S^\dagger S)\), so its two-coordinate
restriction lies entirely in the exchange-even line and has exactly zero
ordered contrast. Adding the smallest exchange-odd operator produces contrast
\(2\epsilon\), but only by introducing a new continuous coefficient. The
paper's matching-scale BSM couplings are input coordinates on a viable
critical surface, not a singleton source prediction. WP728 corrects the
initial successor wording: an exchange-symmetric fixed point forces a unique
odd coordinate to zero. The viable successor must explicitly orient the
channels by non-isomorphic source representations, make fluctuations about
the resulting nonzero fixed contrast irrelevant, and separately fix the
relevant clock deformation.

## Exchange-equivariant fixed-point orientation theorem: WP728

- flavor-exchange-equivariant-fixed-point-orientation-theorem.md
- checkers/wp728_exchange_equivariant_fixed_point_orientation.py
- results/wp728_exchange_equivariant_fixed_point_orientation.json

WP728 proves that a unique fixed point of an exchange-equivariant beta field
has zero exchange-odd portal coordinate. Nonzero symmetric-source fixed points
can occur only in exchange-related pairs, so they select at most a magnitude
or orbit; distinguishing their signs requires a relational reference and a
changed stabilizer groupoid. A unique nonzero ordered contrast instead needs
non-isomorphic representation data that explicitly orient the two channels.
The fluctuation about that nonzero fixed coordinate may then be irrelevant.
An exact affine witness shows that one relevant clock direction and one
irrelevant nonzero contrast direction are algebraically compatible, but its
coefficients are not yet derived from an admitted anomaly-free matter model.

## Vectorlike singlet–triplet additive portal source: WP729

- flavor-vectorlike-singlet-triplet-additive-portal-source.md
- checkers/wp729_vectorlike_singlet_triplet_additive_portal_source.py
- results/wp729_vectorlike_singlet_triplet_additive_portal_source.json

WP729 finds a primary-source-supported exchange-odd affine beta mechanism.
The one-loop portal beta function of arXiv:2008.08606 contains the additive
term (-I_\kappa\alpha_\kappa\alpha_y/3), with (I_\kappa=12) for its
vectorlike electroweak-singlet model A and (9) for triplet model B. Equal
positive Yukawa products therefore give a nonzero oriented source contrast.
Representation data alone do not select it: the positive ratio
(q_B=4q_A/3) cancels the contrast exactly. A local affine completion fixes
contrast (q/\vartheta) with irrelevant portal fluctuations, but the paper
does not supply the simultaneous A+B beta system. The next gate is that full
direct-sum calculation with every allowed scalar cross-coupling.

## Direct-sum portal-block acceptance theorem: WP730

- flavor-direct-sum-portal-block-acceptance-theorem.md
- checkers/wp730_direct_sum_portal_block_acceptance.py
- results/wp730_direct_sum_portal_block_acceptance.json

WP730 includes the unavoidable mixed scalar-norm channel in the linearized
two-portal block. For stability matrix entries (a,b,c), the fixed contrast is
([4q_A(b+c)-3q_B(a+c)]/(ab-c^2)), and the positive cancellation fiber shifts
to (q_B/q_A=4(b+c)/[3(a+c)]). Both portal directions are predicted when the
block is positive definite. If a relevant portal mode remains, it is harmless
only when the contrast covector annihilates its eigenvector. Exact witnesses
separate a relevant even mode, which changes only the portal sum, from a
relevant odd mode, which restores a free contrast amplitude. The completed
direct-sum calculation must therefore determine the full stability
eigenvectors, not merely two diagonal portal exponents.

## Direct-sum mixed-norm radiative closure: WP731

- flavor-direct-sum-mixed-norm-radiative-closure.md
- checkers/wp731_direct_sum_mixed_norm_radiative_closure.py
- results/wp731_direct_sum_mixed_norm_radiative_closure.json

WP731 derives the first actual off-diagonal source in WP730's portal block.
Any symmetry admitting both Higgs portals also admits the neutral mixed norm
quartic (R_AR_B). The exact scalar Hessian-square divergence for component
counts (4+18+18) generates its coefficient as
(8\delta_A\delta_B) at zero mixed coupling. A nonzero mixed coupling feeds
back as (36\delta_Bw) and (36\delta_Aw) in the two portal equations.
Therefore the uncoupled A+B portal surface is not radiatively closed. The
calculation covers the radial norm sector; the next gate is enumeration and
RG closure of all additional mixed matrix-scalar tensor quartics.

## Two-matrix mixed-quartic grammar: WP732

- flavor-two-matrix-mixed-quartic-grammar.md
- checkers/wp732_two_matrix_mixed_quartic_grammar.py
- results/wp732_two_matrix_mixed_quartic_grammar.json

WP732 exposes a source-symmetry tradeoff. Independent chiral flavor groups
permit only the mixed norm product but supply no intertwiner relating the two
Yukawa products. A common biunitary frame with independent sector gradings
admits four balanced mixed quartics. A matrix-unit evaluation has determinant
minus one, proving their exact independence, while the radial identity slice
collapses them to the ratio (9:9:3:3). Thus a common flavor structure invoked
to remove WP729's Yukawa cancellation fiber also opens three tensor directions
invisible to WP731's radial calculation. The programme must either derive the
Yukawa relation while preserving independent groups or close the full
four-coupling mixed tensor beta system.

## Gauge-parallelized Yukawa contrast sign theorem: WP733

- flavor-gauge-parallelized-yukawa-contrast-sign-theorem.md
- checkers/wp733_gauge_parallelized_yukawa_contrast_sign.py
- results/wp733_gauge_parallelized_yukawa_contrast_sign.json

WP733 takes WP732's independent-flavor-group branch. The separately published
one-loop model-A and model-B Yukawa nullclines are solved over common positive
electroweak gauge coordinates and a common top-bottom contribution. Their
induced additive portal contrast is a strictly positive polynomial throughout
the domain where both displayed Yukawa solutions are positive; the WP729
cancellation ratio is absent. Thus shared gauge dynamics can orient the sign
without a common scalar flavor frame. The result is not yet the simultaneous
theory: common Standard Model fields generate cross A/B anomalous dimensions,
and the combined matter content changes the gauge beta functions. Those terms
must be derived before magnitude or basin authority is granted.

## Cross-anomalous-dimension sign falsifier: WP734

- flavor-cross-anomalous-dimension-sign-falsifier.md
- checkers/wp734_cross_anomalous_dimension_sign_falsifier.py
- results/wp734_cross_anomalous_dimension_sign_falsifier.json

WP734 attacks WP733 with the missing simultaneous-theory structure. General
nonnegative cross coefficients (x,y) are added to the two mixed-Yukawa
nullclines. Their additive portal contrast vanishes on an exact algebraic
surface (F(x,y)=0). The strictly positive witness
(x=1), (y=759/28-33\sqrt{1493}/56) lies on that surface while all four
Yukawa fixed coordinates remain positive. Therefore positivity of the shared
wavefunction contributions does not protect WP733's sign. The actual common
Higgs and lepton anomalous-dimension coefficients must be calculated and shown
to lie a strict uncertainty-stable distance from the cancellation surface.

## Simultaneous singlet-triplet nullcline no-go: WP735

- flavor-simultaneous-singlet-triplet-nullcline-no-go.md
- checkers/wp735_simultaneous_singlet_triplet_nullcline_no_go.py
- results/wp735_simultaneous_singlet_triplet_nullcline_no_go.json

WP735 derives the actual shared-field cross coefficients with an executable
PyR@TE tensor calculation and validates their normalization by reproducing the
published diagonal coefficients. They are (x=21/4) and (y=7). The exact
simultaneous one-loop nullcline then obeys
(kappa_A=-6(4T+12g_1+53g_2)/103). Hence no point in the nonnegative source
domain has all four Yukawa squared couplings strictly positive. The
gauge-parallelized singlet-triplet direct sum therefore does not provide the
sought selector: shared-field backreaction removes its candidate fully
interacting source surface. A successor must derive a structural modification
of this numerator independently before magnitude, basin, threshold, or
instrument gates can be reopened.

## Diagonal product-group Clebsch selector: WP736

- flavor-diagonal-product-group-clebsch-selector.md
- checkers/wp736_diagonal_product_group_clebsch_selector.py
- results/wp736_diagonal_product_group_clebsch_selector.json

WP736 replaces WP735's two independently fixed low-energy Yukawas by one
parent invariant. Breaking (SU(2)_A x SU(2)_B) to its diagonal decomposes a
bifundamental as (1+3) and fixes the Hiller-normalized squared-coupling ratio
(alpha_kappaB/alpha_kappaA=4). With one parent flavor Yukawa, the additive
portal contrast is strictly positive at matching. This is the first concrete
representation theorem in the branch that selects the ordered sign without
tuning a portal difference. The Clebsch ray is not invariant below breaking:
(d log(alpha_kappaB/alpha_kappaA)/dt=-12 alpha_2). Moreover, putting L and H
on different product-group sites forbids ordinary renormalizable parent SM
Yukawas. The construction is therefore a matching-scale selector and
rigidifier, not yet a complete numerical low-energy selector; it requires a
source-derived link/mediator completion, fixed breaking clock, finite matching,
and independently calibrated labelled readout.

## Minimal product-parent fixed-point no-go: WP737

- flavor-minimal-product-parent-fixed-point-no-go.md
- checkers/wp737_minimal_product_parent_fixed_point_no_go.py
- results/wp737_minimal_product_parent_fixed_point_no_go.json

WP737 tests whether WP736's minimal anomaly-compatible matter assignment also
fixes the portal magnitude. Its executable 210 gauge-Yukawa system loses
asymptotic freedom in hypercharge and (SU(2)_A), but the unique parent Yukawa
cannot generate either required interacting zero. After its nullcline is
inserted, both gauge brackets are coefficientwise strictly positive; the
reduced (SU(2)_A) bracket is at least one. A nonnegative parent flavor Yukawa
only lowers the portal Yukawa and strengthens the obstruction. Thus the
minimal product group is a genuine matching-scale sign selector but not a
magnitude selector or RG-basin constructor. Any repair requires independently
motivated additional Yukawa-active matter, not a tuned enlargement chosen to
manufacture a zero.

## Required link mediators fixed-point exhaustion: WP738

- flavor-required-link-mediators-fixed-point-exhaustion.md
- checkers/wp738_required_link_mediators_fixed_point_exhaustion.py
- results/wp738_required_link_mediators_fixed_point_exhaustion.json

WP738 adds only the vectorlike quark and lepton doublets forced by the
link-mediated completion of Standard Model Yukawas. Their five renormalizable
link and Higgs couplings supply additional source-authorized gauge screening.
An exact rational audit exhausts all 64 Yukawa subsets and all four choices in
which asymptotically free (SU(2)_B) and color are interacting or Gaussian,
while the two IR-free factors remain active. None of the 256 branches is
physical. The fully interacting solution already has negative color and
(SU(2)_B) squared coordinates. Thus even the compulsory mediator completion
does not turn WP736's matching-scale sign selector into a magnitude selector.
Further matter is admissible only if independently required by another source
principle, not selected by scanning for a fixed point.

## SO(5) singlet-multiplicity projector obstruction: WP739

- flavor-so5-singlet-multiplicity-projector-obstruction.md
- checkers/wp739_so5_singlet_multiplicity_projector_obstruction.py
- results/wp739_so5_singlet_multiplicity_projector_obstruction.json

WP739 tests the smallest simple-group source for WP736. The (5) of (SO(5))
restricts through (SO(4)) to the physical diagonal group as (3+1+1), not
(3+1). Its residual commutant contains an (O(2)) rotation of the two singlets.
A unique parent invariant therefore fixes only the complete two-singlet
isotypic packet; it does not select which rank-one singlet is the measured
model-A mediator. An exact commuting rotation changes a witness selected
coupling squared continuously from one to zero. A source-derived breaking
potential and gapped mass projector could remove the fiber, but that projector
must be derived and transported independently before the (SO(5)) beta system
has selector authority.

## SO(5) minimal projector vacuum saddle: WP740

- flavor-so5-minimal-projector-vacuum-saddle.md
- checkers/wp740_so5_minimal_projector_vacuum_saddle.py
- results/wp740_so5_minimal_projector_vacuum_saddle.json

WP740 tests the smallest dynamical repair of WP739. One real
symmetric-traceless (14) with a (Z2)-even renormalizable potential forces the
only possible (3+1+1) eigenvalue pattern to be (0,0,0,v,-v), which would fix
the singlet projectors without a mixing angle. The exact Hessian rules it out:
stabilizing the upper (3x3) shape modes requires negative (lambda_2), while
existence of the nonzero vacuum then makes the two-singlet Hessian determinant
(24 lambda_2(2 lambda_1+lambda_2)) strictly negative. The opposite sign
destabilizes the shape modes and zero leaves flats. A cubic invariant or higher
operator may repair the saddle, but its coefficient and resulting eigenvalue
ratios require independent source authority.

## SO(5) full renormalizable projector no-go: WP741

- flavor-so5-full-renormalizable-projector-no-go.md
- checkers/wp741_so5_full_renormalizable_projector_no_go.py
- results/wp741_so5_full_renormalizable_projector_no_go.json

WP741 closes WP740's cubic loophole. For the complete renormalizable potential
of one real symmetric-traceless (14), every distinct (3+1+1) stationary orbit
can be written as \(\operatorname{diag}(1,1,1,t,-3-t)\). Shape stability
requires \(\lambda_2(t-1)(t+4)<0\). Positivity of the two invariant modes
would then force \(\lambda_2+2\lambda_1<0\), but their leading principal minor is the sum of two
strictly negative terms. Degenerate parameter boundaries leave flat modes or
merge the two singlets. Thus the cubic invariant supplies neither a stable
projector rigidifier nor a selector. Any successor needs an independently
required new source object that changes this Hessian obstruction; portal
magnitude, basin, threshold, and calibrated-readout gates remain unopened.

## Orbifold projector conditional rigidifier: WP742

- flavor-orbifold-projector-conditional-rigidifier.md
- checkers/wp742_orbifold_projector_conditional_rigidifier.py
- results/wp742_orbifold_projector_conditional_rigidifier.json

WP742 tests geometric projection as the first successor to the full one-(14)
no-go. An (S^1/Z_2) parity with four positive vector eigenvalues removes the
extra (SO(5)) singlet and leaves (4=3+1) under the diagonal (SO(3)), so it
conditionally supplies the unique projector and inherits WP736's Clebsch
ratio. It does not select its own boundary or intrinsic parity class: reversing
the intrinsic parity retains only the complementary singlet. The effective
magnitude still depends on the bulk coupling and compactification length, and
residual-symmetry boundary operators shift the ordered threshold contrast by
an independent difference. No calibrated physical16 instrument follows from
the geometry. The construction is therefore a conditional rigidifier and
projector selector, not the requested source selector.

## Gauge-connection bulk contrast no-go: WP743

- flavor-gauge-connection-bulk-contrast-no-go.md
- checkers/wp743_gauge_connection_bulk_contrast_no_go.py
- results/wp743_gauge_connection_bulk_contrast_no_go.json

WP743 promotes the orbifold carrier to the fifth component of an (SO(5))
gauge connection. One-form covariance now forces the opposite (A_\mu/A_5)
parities, so the four (SO(5)/SO(4)) scalar zero modes and their common gauge
coupling are source-derived; the ordinary scalar's intrinsic-parity fiber is
gone. But the exact symmetric commutant of the bulk (SO(4)) vector is only
the scalar line, forcing zero singlet–triplet contrast. At a diagonal-(SO(3))
boundary the commutant becomes (operatorname{diag}(a,a,a,b)), so asymmetry
first becomes legal exactly where the free coefficient (b-a) reappears.
The gauge construction is a carrier selector and coupling parallelizer, not an
asymmetric portal or magnitude selector; its clock, boundary completion, RG
trajectory, thresholds, and instrument remain open.

## SO(5) anomaly-quantization type no-go: WP744

- flavor-so5-anomaly-quantization-type-no-go.md
- checkers/wp744_so5_anomaly_quantization_type_no_go.py
- results/wp744_so5_anomaly_quantization_type_no_go.json

WP744 tests whether anomaly inflow can quantize WP743's free boundary
contrast. All (10^3) symmetrized cubic tensors vanish independently in the
vector and Clifford-spinor realizations of (SO(5)); the diagonal (SO(3))
triplet tensor also vanishes. An (SU(3)) comparator is nonzero, so this is a
group-theoretic obstruction rather than a checker blind spot. Independently,
a reduced five-dimensional Chern–Simons term has the parity-odd operator type
(A_5F\wedge F), not the CP-even scalar-quadratic portal. Ordinary local
anomaly quantization therefore neither fixes nor rigidifies (b-a). Global
anomalies, larger groups, and discrete or nonlocal holonomies remain separate
successors and must pass the same operator-type gate.

## Holonomy contrast dichotomy: WP745

- flavor-holonomy-contrast-dichotomy.md
- checkers/wp745_holonomy_contrast_dichotomy.py
- results/wp745_holonomy_contrast_dichotomy.json

WP745 closes the discrete-holonomy branch for the WP743 carrier. The exact Lie
centralizer of diagonal (SO(3)) in (SO(4)) is trivial, and its group
centralizer on the vector is only ({I_4,-I_4}); both act identically on the
triplet and singlet and yield no contrast. The smallest distinguishing twist
(operatorname{diag}(-I_3,1)) has determinant minus one, so it lies outside
the admitted gauge group and defines a changed (O(4)) or defect experiment.
That reduction still admits (operatorname{diag}(aI_3,b)), leaving the
continuous contrast (b-a). Hence preserving holonomies do not distinguish,
while distinguishing holonomies change the groupoid and fail to normalize the
portal. Additional source dynamics is required before the clock, basin,
threshold, and instrument gates can open.

## SU(3) moment-map conditional selector: WP746

- flavor-su3-moment-map-conditional-selector.md
- checkers/wp746_su3_moment_map_conditional_selector.py
- results/wp746_su3_moment_map_conditional_selector.json

WP746 returns to positive moment-map geometry after the topological
operator-type failures. One simple (SU(3)) Killing metric and fundamental
weights can conditionally generate the correct CP-even portal:
(g_n=g^2/3), (g_m=-g^2/6), contrast (g^2/2), and strict radial margin
(g^4/12). This fixes relative metric, sign ratio, and stability without an
independent portal-difference coefficient. It does not yet descend: exchanging
the two weight embeddings reverses the ordered contrast, the fundamental is a
complex six-real-dimensional carrier rather than the admitted real triplet,
and common gauge rescaling changes the magnitude. An oriented anomaly-free
mediated descent, interacting normalization with a source clock,
nondecoupling threshold completion, and calibrated physical16 instrument
remain required.

## Nondecoupling D-term threshold fiber: WP747

- flavor-nondecoupling-dterm-threshold-fiber.md
- checkers/wp747_nondecoupling_dterm_threshold_fiber.py
- results/wp747_nondecoupling_dterm_threshold_fiber.json

WP747 tests threshold survival of the conditional WP746 moment map. Exact
heavy-breaking-scalar elimination multiplies its positive square by
(epsilon=m_{\mathrm{soft}}^2/(g^2M^2+m_{\mathrm{soft}}^2)). Every finite
positive (epsilon) preserves the portal sign ratio (-2) and strict radial
margin, but the supersymmetric limit gives (epsilon=0) and erases the portal.
Every value in the open unit interval is realized by a continuous soft-to-vector
mass ratio. Thus nondecoupling matching rigidifies sign and ratio but does not
select survival or magnitude. The breaking ratio, gauge normalization, clock,
complete threshold spectrum, and calibrated physical16 instrument remain
source gates.

## Fixed-point anomaly/nondecoupling incompatibility: WP748

- flavor-fixed-point-anomaly-nondecoupling-incompatibility.md
- checkers/wp748_fixed_point_anomaly_nondecoupling_incompatibility.py
- results/wp748_fixed_point_anomaly_nondecoupling_incompatibility.json

WP748 tests whether pure anomaly mediation can derive WP747's soft mass while
an interacting fixed point fixes WP746's gauge magnitude. The anomaly-mediated
maps are proportional to beta functions and their Lie derivatives, so every
required soft term vanishes at the exact fixed point. Consequently
(epsilon_*=0) and the additional (D)-term portal decouples. Moving off the
fixed point restores a soft mass proportional to a critical-mode amplitude,
RG time, and (m_{3/2}), with no automatic positive sign. The two desired
selectors are therefore incompatible in pure anomaly mediation: exact
fixed-point normalization kills nondecoupling, while nonzero nondecoupling
restores the amplitude and clock fibers. Mixed mediation mechanisms remain
possible but introduce new source data requiring independent authority.

## Single-spurion correlated-Higgsing acceptance theorem: WP749

- flavor-single-spurion-correlated-higgsing-acceptance.md
- checkers/wp749_single_spurion_correlated_higgsing_acceptance.py
- results/wp749_single_spurion_correlated_higgsing_acceptance.json

WP749 isolates the exact condition under which a successor can escape WP748's
independent-clock obstruction. If one source deformation gives
\(M_V^2=a g_*^2v^2\) and \(m_{\mathrm{soft}}^2=b g_*^2v^2\), then the common
clock cancels and the portal contrast is
\(g_*^2b/(2(a+b))>0\). This conditionally preserves the selected sign and fixes
the magnitude once \(a:b\) and \(g_*\) are source-fixed. It is not itself a
source explanation: two positive coefficient packets at identical \(g_*,v\)
give contrasts differing by \(g_*^2/8\), and threshold support still depends
on \(v\). The next admissible model must derive the ordered embedding, a unique
coefficient ray, an attractive fixed point, the finite threshold spectrum,
and a calibrated `physical16` instrument from one anomaly-free source.

## Single-spurion Wilson-coefficient dichotomy: WP750

- flavor-single-spurion-wilson-coefficient-dichotomy.md
- checkers/wp750_single_spurion_wilson_coefficient_dichotomy.py
- results/wp750_single_spurion_wilson_coefficient_dichotomy.json

WP750 tests whether WP749's common-spurion acceptance condition is already a
source explanation. It is not. The minimal gauge-invariant Kähler basis has
independent coefficients \(c_+\) and \(c_-\). Their difference mixes the
nominal heavy and light link directions, so a common spurion without exchange
symmetry is neither a selector nor a rigidifier. Exchange symmetry removes the
mixing but leaves one unrestricted coefficient \(c\), giving
\(\epsilon=c/(2q^2+c)\). At fixed \(q^2=1,g,v\), \(c=1\) and \(c=3\) produce
portal contrasts differing by \(2g^2/15\). The next source principle must both
forbid the exchange-odd operator and normalize the surviving exchange-even
operator; common source identity alone does neither.

## Extended-SUSY normalization/nondecoupling dichotomy: WP751

- flavor-extended-susy-normalization-nondecoupling-dichotomy.md
- checkers/wp751_extended_susy_normalization_nondecoupling_dichotomy.py
- results/wp751_extended_susy_normalization_nondecoupling_dichotomy.json

WP751 tests extended supersymmetry as the stronger operator principle requested
by WP750. In a canonical \(N=2\) gauge-hypermultiplet sector, the matter
interaction is tied to the gauge metric, but exact supersymmetry forces the
soft mass and additional nondecoupling portal to vanish. Breaking to \(N=1\)
restores the portal only by admitting a breaking scale and Wilson coefficient.
Even after correlating the scale with \(g^2v^2\), the threshold factor is
\(c/(2q^2+c)\), and the same \(2g^2/15\) hostile residual remains. Thus exact
extended supersymmetry is a normalizer with zero portal, whereas generic
breaking permits the portal but restores the coefficient fiber. A viable
successor must derive and quantize the breaking constructor itself.

## Radiative half-twist conditional selector: WP752

- flavor-radiative-half-twist-conditional-selector.md
- checkers/wp752_radiative_half_twist_conditional_selector.py
- results/wp752_radiative_half_twist_conditional_selector.json

WP752 finds the first progressive breaking mechanism after WP751. Two valid
orbifold boundary involutions admit a continuous relative twist, so geometry
alone does not quantize it. But a positive source-derived bulk spectral
coefficient in \(V(\omega)=A\cos(2\pi\omega)\) dynamically selects the stable
half twist with an attractive basin. With a common Kaluza–Klein clock this
gives \(\epsilon=1/(4N^2+1)\), and the unit mode predicts the positive contrast
\(g_*^2/10\), independent of the compactification radius. The result remains
conditional: boundary-localized masses continuously shift the prediction,
threshold accessibility retains the radius, and neither the complete
anomaly-free spectrum, full twist potential, gauge fixed point, physical16
descent, nor calibrated instrument has been derived.

## Full KK-tower half-twist theorem: WP753

- flavor-full-kk-tower-half-twist-theorem.md
- checkers/wp753_full_kk_tower_half_twist_theorem.py
- results/wp753_full_kk_tower_half_twist_theorem.json

WP753 proves that WP752's half-twist selector is not a first-harmonic artifact.
The complete massless tower
\(\sum_{n\geq1}\cos(2\pi n\omega)/n^5\) is a positive Laplace integral of
geometric cosine kernels strictly increasing in \(\cos(2\pi\omega)\).
Consequently a positive spectral index \(\kappa\) gives a unique half-twist
minimum, curvature \(3\pi^2\kappa\zeta(3)/R^4\), and endpoint gap
\(31\kappa\zeta(5)/(16R^4)\). The unit-mode prediction
\(\Delta=g_*^2/10\) and its attractive basin survive the full tower. The
remaining source gate is now sharply spectral: the actual anomaly-free bulk
content must derive \(\kappa>0\), while bulk masses, multiple twist charges,
boundary operators, the radius threshold, and the physical instrument remain
to be completed.

## Bulk-localization spectral-index fiber: WP754

- flavor-bulk-localization-spectral-index-fiber.md
- checkers/wp754_bulk_localization_spectral_index_fiber.py
- results/wp754_bulk_localization_spectral_index_fiber.json

WP754 computes the WP753 signed index on distinct five-dimensional lifts of
the same four-dimensional anomaly-compatible flavor grammar. Bulk gauge
multiplets and only the bifundamental link give
\(\kappa=2+15-4=13>0\), selecting the half twist. Moving the already required
\(L,H,\Psi_R\) packet into the bulk gives \(\kappa=-19\), selecting zero twist;
including the WP738 required mediators gives \(\kappa=-67\). The count uses two
5D hypermultiplets per 4D vectorlike zero-mode pair, because opposite orbifold
parities leave only one chiral zero mode per hypermultiplet. Thus the existing
four-dimensional representation packet does not authorize a spectral sign.
The next source constructor must derive bulk-versus-boundary placement through
five-dimensional locality and anomaly inflow before the radiative selector
has physical authority.

## Anomaly-inflow localization cofiber: WP755

- flavor-anomaly-inflow-localization-cofiber.md
- checkers/wp755_anomaly_inflow_localization_cofiber.py
- results/wp755_anomaly_inflow_localization_cofiber.json

WP755 tests whether anomaly inflow supplies the missing WP754 localization
constructor. For one cancellable anomaly channel,
\(A_0=b_0+B/2+k\) and \(A_\pi=b_\pi+B/2-k\). Global anomaly cancellation
fixes only \(b_0+b_\pi+B=0\); an adjustable Chern–Simons level cancels the
remaining boundary difference. The same \(+1,-1\) four-dimensional chiral
packet is locally consistent either with both modes in the bulk and \(k=0\),
or split across the boundaries and \(k=-1\), while the bulk spectral count
differs by two. Anomaly inflow therefore defines a cofiber of localization and
inflow classes, not a selector. A higher source must fix the full
Chern–Simons level vector before local consistency can constrain localization.

## Fixed-inflow anomaly-neutral localization kernel: WP756

- flavor-fixed-inflow-anomaly-neutral-localization-kernel.md
- checkers/wp756_fixed_inflow_anomaly_neutral_localization_kernel.py
- results/wp756_fixed_inflow_anomaly_neutral_localization_kernel.json

WP756 freezes the Chern–Simons level and tests the strongest surviving form of
the anomaly-localization proposal. A vectorlike \((+1,-1)\) pair can be moved
between a common boundary and the bulk without changing either local anomaly
or the fixed value \(k=0\), while the bulk realization requires two
hypermultiplets. In the flavor witness, moving only the WP738 anomaly-neutral
mediator pairs into the bulk changes \(\kappa\) from \(13\) to \(-35\) without
changing the anomaly vector or inflow class. Thus fixed inflow remains blind
on an anomaly-neutral localization kernel and cannot make the radiative portal
selector hard to vary. The next source principle must couple independently to
anomaly-neutral matter placement before the normalization, RG, threshold,
`physical16`, and detector gates can acquire authority.

## Domain-wall localization magnitude fiber: WP757

- flavor-domain-wall-localization-magnitude-fiber.md
- checkers/wp757_domain_wall_localization_magnitude_fiber.py
- results/wp757_domain_wall_localization_magnitude_fiber.json

WP757 tests the first source operation that is sensitive to the WP756
anomaly-neutral kernel. A scalar kink gives opposite normalized zero-mode
profiles with boundary-density ratio \(e^{2x}\) and exact contrast \(2x\),
where \(x=ML>0\). It therefore conditionally selects a localization side and
rigidifies a boundary coupling. The domain-wall index is nevertheless constant
throughout \(x>0\): \(x=1/2\) and \(x=3/2\) have the same chirality but
contrasts \(1\) and \(3\), and wall reversal reverses the labelled sign. The
kink is progressive but not a numerical selector. A successor must derive a
source-fixed orientation and a quantized or attractive value of \(ML\), then
prove RG, finite-wall, KK-threshold, `physical16`, and instrument survival.

## BPS-wall separation-modulus fiber: WP758

- flavor-bps-wall-separation-modulus-fiber.md
- checkers/wp758_bps_wall_separation_modulus_fiber.py
- results/wp758_bps_wall_separation_modulus_fiber.json

WP758 grants the strongest favorable BPS repair of WP757: supersymmetry fixes
a unit \(\operatorname{sech}\) zero-mode exponent. The normalized
center-to-boundary contrast is still
\(\Delta(a)=\tanh^2(a)/2\), where \(a=kd\) is the wall–boundary separation in
wall-width units. Two walls with the same BPS charge and local profile,
\(a=\operatorname{arctanh}(1/2)\) and
\(a=\operatorname{arctanh}(3/4)\), give contrasts \(1/8\) and \(9/32\).
Therefore BPS structure normalizes the local shape but leaves a global
translation/radion fiber. The next constructor must stabilize one labelled
dimensionless separation in the same source action before RG, thresholds,
`physical16`, and detector survival can be tested.

## Bulk-scalar stabilization boundary-ratio fiber: WP759

- flavor-bulk-scalar-stabilization-boundary-ratio-fiber.md
- checkers/wp759_bulk_scalar_stabilization_boundary_ratio_fiber.py
- results/wp759_bulk_scalar_stabilization_boundary_ratio_fiber.json

WP759 supplies the source-derived stabilizer requested by WP758. The leading
bulk-scalar potential has a stable minimum
\(s_*=\log(v_0/v_\pi)/\epsilon\). Even granting a common wall/stabilizer scale,
the composed portal contrast is
\(\Delta(r)=(r^2-1)^2/[2(r^2+1)^2]\), with \(r=v_0/v_\pi\). Boundary packets
\(r=2\) and \(r=3\) obey the same variational law and have stable minima but
predict \(9/50\) and \(8/25\). The stabilizer selects a separation conditional
on boundary data; it does not select the boundary data. A successor must derive
their ratio and labelled ordering from a unique or quantized source vacuum
before RG, threshold, `physical16`, and detector gates acquire authority.

## Oriented quantized-tadpole singleton gate: WP760

- flavor-oriented-quantized-tadpole-singleton-gate.md
- checkers/wp760_oriented_quantized_tadpole_singleton_gate.py
- results/wp760_oriented_quantized_tadpole_singleton_gate.json

WP760 replaces WP759's continuous boundary values by positive integer charges
with fixed total \(T\) and an oriented endpoint label. The exact asymmetric
fiber size is \(\lfloor(T-1)/2\rfloor\). It is a singleton only for \(T=3\)
or \(T=4\), selecting ratios \(2\) or \(3\) and portal contrasts \(9/50\) or
\(8/25\). At \(T=5\), pairs \((3,2)\) and \((4,1)\) already give distinct
contrasts \(25/338\) and \(225/578\). Quantization therefore supplies the
first possible discrete selector, but only if an admitted flavor topology
independently forces one exceptional minimal total and the labelled
orientation. RG-stable integers do not yet prove matching, `physical16`, or
detector survival.

## Flavor integer-numerology fork: WP761

- flavor-integer-numerology-fork.md
- checkers/wp761_flavor_integer_numerology_fork.py
- results/wp761_flavor_integer_numerology_fork.json

WP761 asks whether the admitted representation/anomaly packet derives WP760's
exceptional total. All perturbative anomaly coordinates vanish familywise,
the weak-doublet count is Witten-even familywise, and the new pairs are
vectorlike. These authorized probes return no positive tadpole. The
presentation separately contains family multiplicity \(3\) and bifundamental
dimension \(4\); reinterpreting them as \(T\) predicts different singleton
contrasts \(9/50\) and \(8/25\), while the zero anomaly vector chooses neither.
A five-family hostile remains anomaly-free but produces a nonsingleton fiber
under the family-count reinterpretation. Therefore no source index map is yet
defined. A successor must derive an integral map from compactification or
defect topology to ordered boundary charge before the WP760 theorem has flavor
authority.

## Spin(5) parent-parity interface audit: WP896

- flavor-spin5-parent-parity-interface-audit.md
- checkers/wp896_spin5_parent_parity_interface_audit.py
- results/wp896_spin5_parent_parity_interface_audit.json

WP896 attacks the source-spin boundary. WP239's dimuon selection truth-matches
the signal daughters to a PDG-25 mother, so WP893's CP-even adapter survives:
the dataset's `MA` token labels the MSSM parameter point rather than the
event-level parent used by the response. The tau pilot carries no analogous
parent-PDG or parity field, so its finite-grid detector theorem remains valid
but its Spin(5) transfer is parity-untyped. WP895 is tightened to require a
declared neutral CP-even parent, daughter ancestry, width, and source-card hash
at both direct poles.

## Universal-mixing source-card factorization: WP897

- flavor-spin5-universal-mixing-source-card-factorization.md
- checkers/wp897_spin5_universal_mixing_source_card_factorization.py
- results/wp897_spin5_universal_mixing_source_card_factorization.json

WP897 derives the direct-pole source-card family from the admitted portal.
Universal Higgs mixing multiplies every partial width, the total width, and
bottom-associated production by \(q_i=\theta_i^2\), so the physical branching
fractions are exactly independent of \(q_i\). The official calibration yields
18.7241295132 and 3.31722675436 tau pairs per inverse femtobarn per unit
\(q_i\). An unrelated MSSM spectrum is unnecessary: the two free mixing
magnitudes remain normalization/width coordinates. The unresolved gate is
detector-template stability over their width interval, followed by execution;
the factorization selects no numerical value.

## Width-response resolution bound: WP898

- flavor-spin5-width-response-resolution-bound.md
- checkers/wp898_spin5_width_response_resolution_bound.py
- results/wp898_spin5_width_response_resolution_bound.json

WP898 converts WP897's continuous mixing-width family into one conditional
detector calibration. Under a centered Gaussian response convolved with a
Breit--Wigner half-width \(\gamma\), every threshold CDF changes by at most
\(\gamma/(\sigma\sqrt{2\pi})\). The five finite boundaries of the six-bin tau
partition therefore obey
\(d_{\rm TV}\leq5\gamma/(\sigma\sqrt{2\pi})\). At a diagnostic one-percent
tolerance the two sufficient resolution floors are about 0.581 and 2.473 GeV.
The theorem reduces the scan but does not supply Gaussian/tail calibration;
that same-frame measurement remains the instrument gate.

## Tau-resolution applicability audit: WP899

- flavor-spin5-tau-resolution-applicability-audit.md
- checkers/wp899_spin5_tau_resolution_applicability_audit.py
- results/wp899_spin5_tau_resolution_applicability_audit.json

WP899 tests whether the existing tau pilot supplies WP898's \(\sigma\). It
does not: WP253 measures visible muon--hadronic-tau mass, including neutrino
loss and decay kinematics, rather than an event-joined parent-mass residual.
The pilot has none of the five required fields: true parent join, reconstructed
parent estimator, centered residual, Gaussian covariance, or tail budget.
Its applicability vector is \((0,0,0,0,0)\), and WP256's exact nonclosure
supports withholding a universal kernel. WP898 remains a conditional theorem;
the finite tau discriminator remains admitted on its original domain.

## Paired-width response experiment: WP900

- flavor-spin5-paired-width-response-experiment.md
- checkers/wp900_spin5_paired_width_response_experiment.py
- results/wp900_spin5_paired_width_response_experiment.json

WP900 replaces WP898's Gaussian assumption by a direct distribution-free
four-cell experiment: zero and maximal widths at each pole, passed through the
same CP-even source and CMS detector chain. A two-sample multinomial bound gives
the acceptance rule
\(\widehat d+r(n_0,\alpha)+r(n_1,\alpha)\leq\varepsilon\), with
\(r=\sqrt{\log(2^{k+2}/\alpha)/(2n)}\) after union over all four cells. For six bins, 95% joint coverage,
equal cells and a diagnostic one-percent tolerance, zero observed drift still
requires 170819 selected events per cell. This closes the finite statistical
grammar but does not execute the four samples or select the mixing values.

## Zero-drift width certificate: WP901

- flavor-spin5-zero-drift-width-certificate.md
- checkers/wp901_spin5_zero_drift_width_certificate.py
- results/wp901_spin5_zero_drift_width_certificate.json

WP901 instantiates the corrected four-cell WP900 theorem at exactly zero
observed drift. Simultaneous 95% coverage and a diagnostic one-percent
tolerance require exactly 170819 selected events per cell, 683276 total. The
upper bound is 0.00999997642 and the four-cell failure bound is 0.04999798594;
one fewer event per cell fails. Projecting the 140 GeV pilot acceptance gives
about 6.45 million generated events per cell, explicitly only a capacity
diagnostic. The certificate remains prospective because the four samples have
not been generated.

## Paired null-completed width test: WP902

- flavor-spin5-paired-null-completed-width-test.md
- checkers/wp902_spin5_paired_null_completed_width_test.py
- results/wp902_spin5_paired_null_completed_width_test.json

WP902 reduces WP901's independent-sample cost through a preregistered
common-random-number coupling. Each paired trial retains one of seven outputs:
six bins or a typed selection-failure null. Coupling gives
\(d_{\rm TV}\leq p_{\rm discord}\); with zero discordances the exact binomial
upper bound applies. Using the pilot acceptance only as a design floor, 95%
two-pole coverage and one-percent conditional-shape tolerance require 27856
pairs per pole, 55712 total; one fewer fails. Pairing must be executable,
frozen, replayable, null-complete, and accompanied by an independently
certified acceptance floor. Otherwise WP901 remains the fallback.

## Chiral-index vectorlike kernel: WP762

- flavor-chiral-index-vectorlike-kernel.md
- checkers/wp762_chiral_index_vectorlike_kernel.py
- results/wp762_chiral_index_vectorlike_kernel.json

WP762 tests the ordinary domain-wall index as the missing integral map. The
index \(I=n_0-n_\pi\) has the diagonal vectorlike kernel generated by
\((1,1)\). Hence \((2,1)\) and \((3,2)\) share protected index \(I=1\) but
predict portal contrasts \(9/50\) and \(25/338\). The minimal faithful packet
is rank plus index: \(T=n_0+n_\pi\) and \(I\) reconstruct the ordered pair by
\(n_0=(T+I)/2\), \(n_\pi=(T-I)/2\), subject to parity. The ordinary index is
an orientation selector, not a magnitude selector. A successor must derive a
source-fixed relative rank-index or endpoint-resolved K-class and its physical
readout before RG and threshold survival can be claimed.

## Endpoint rank-index two-port readout: WP763

- flavor-endpoint-rank-index-two-port-readout.md
- checkers/wp763_endpoint_rank_index_two_port_readout.py
- results/wp763_endpoint_rank_index_two_port_readout.json

WP763 solves the ordered integral readout problem conditionally. Aggregate rank
\(T=n_0+n_\pi\) and oriented index \(I=n_0-n_\pi\) are individually rank-one
probes, while their joint response has determinant \(-2\) and is faithful on
the parity-compatible lattice. Same-index and same-rank hostile pairs prove
both ports necessary. Separately labelling the endpoints changes the swap
quotient to a stabilizer groupoid; this is a new relational experiment, not
recovery of an absolute label. The architecture is a faithful readout and
rigidifier, not a selector of \(T=3\) or \(T=4\). Physical authority still
requires source-derived endpoint couplings, common calibration, threshold
Jacobians, `physical16` descent, and detector realization.

## Primitive-index positive-cost selector: WP764

- flavor-primitive-index-positive-cost-selector.md
- checkers/wp764_primitive_index_positive_cost_selector.py
- results/wp764_primitive_index_positive_cost_selector.json

WP764 derives rather than inserts WP760's exceptional \(T=3\), conditional on
three source premises: primitive oriented index \(I=+1\), compulsory nonempty
endpoint sectors, and strictly positive cost for each added diagonal
vectorlike pair. Every representative is \((k+2,k+1)\); an additive positive
energy increases by \(\mu_0+\mu_\pi\), uniquely selecting \((2,1)\), ratio
\(2\), and portal contrast \(9/50\). A correction preserves the selection when
its discrete step remains greater than \(-\mu_0-\mu_\pi\). This is the first
conditional gapped preparation selector. The current flavor source has not yet
derived the primitive index, nonempty-endpoint condition, positive complete
spectrum, rank-to-boundary-ratio map, RG/threshold survival, or physical
two-port instrument.

## Gapped-class affine threshold fiber: WP765

- flavor-gapped-class-affine-threshold-fiber.md
- checkers/wp765_gapped_class_affine_threshold_fiber.py
- results/wp765_gapped_class_affine_threshold_fiber.json

WP765 composes WP764's gapped class selector with WP726's allowed threshold
operator. The physical coefficient is \(\Delta_{\mathrm{IR}}=9Z/50+c\).
Changing \(c\) leaves the prepared endpoint class untouched but changes the
low-energy portal; \(c=-9Z/50\) cancels it exactly. A bounded correction can
protect the positive sign, not the magnitude. The pipeline therefore contains
a valid discrete selector followed by a nonfaithful affine threshold arrow.
A complete source must independently fix the additive boundary and
multiplicative matching, or supply a nonrenormalization theorem, before the
WP763 instrument can read a predicted physical value.

## Holomorphy protects the wrong operator class: WP766

- flavor-holomorphy-protects-wrong-operator-class.md
- checkers/wp766_holomorphy_protects_wrong_operator_class.py
- results/wp766_holomorphy_protects_wrong_operator_class.json

WP766 tests supersymmetric nonrenormalization as the WP765 repair. The CP-even
real-norm portal is an R-neutral full-superspace Kähler/D-term operator; it
contains antichiral fields and is not a holomorphic superpotential monomial.
The standard theorem therefore does not fix its additive boundary, and
\(c_K=-9/50\) cancels the selected value in unit matching. WP751 supplies the
extended-supersymmetry dichotomy: exact \(N=2\) normalizes the interaction but
sets the extra portal to zero, while the \(N=1\) breaking needed to restore it
reopens an independent Wilson coefficient. A successor must provide a genuine
D-term exact relation, not an untyped appeal to holomorphy.

## Massive-vector current exchange scale fiber: WP767

- flavor-massive-vector-current-exchange-scale-fiber.md
- checkers/wp767_massive_vector_current_exchange_scale_fiber.py
- results/wp767_massive_vector_current_exchange_scale_fiber.json

WP767 tests the minimal D-term-specific constructor: classical elimination of
one source-defined Higgsed vector current channel. It fixes the tree-level
portal sign after charge orientation is declared and cancels the gauge
coupling against the vector mass. It does not fix the numerical portal. The
coefficient remains proportional to (1/v^2), so the hostile pair (v=1,2)
changes its magnitude by a factor of four without changing the mechanism.
Moreover the symmetry-allowed Kähler boundary can cancel the exchange term.
The next source gate must fix the Higgs scale in the physical clock and supply
a D-term Ward identity or complete matching theorem that removes the additive
boundary, before RG and instrument claims are possible.

## Separated-boundary exchange completion fiber: WP768

- flavor-separated-boundary-exchange-completion-fiber.md
- checkers/wp768_separated_boundary_exchange_completion_fiber.py
- results/wp768_separated_boundary_exchange_completion_fiber.json

WP768 uses local separation to forbid WP767's additive cross-boundary Kähler
contact. A unique positive-mass bulk mediator then produces a finite endpoint
Green function whose sign is stable under passive Robin completion. This is a
real threshold improvement, but not numerical selection: endpoint-local
self-operators are legal and continuously deform the boundary-to-boundary
propagator. At (m=\ell=1,b=0), Neumann data give (1/\sinh1), whereas
(a=1) gives (e^{-1}). The source must derive its complete boundary action,
couplings, and compactification clock before the portal magnitude is fixed.

## Static gauge matching versus finite readout: WP769

- flavor-static-gauge-matching-finite-readout-fiber.md
- checkers/wp769_static_gauge_matching_finite_readout_fiber.py
- results/wp769_static_gauge_matching_finite_readout_fiber.json

WP769 specializes WP768 to an unbroken boundary gauge current. Gauge symmetry
forbids boundary Proca masses, while gauge-invariant boundary kinetic terms
enter only as (r_i p^2). Consequently the static cross propagator is exactly
(1/[m\sinh(m\ell)]), independent of the quadratic boundary completion. This
is conditional static threshold survival. It is not yet a physical readout:
at finite momentum the legal (r_i) deform the transfer function. The exact
hostile pair at (m=\ell=p=1) distinguishes (r_0=0) from (r_0=1) despite
identical static matching. A detector must calibrate this spectral response in
the same frame rather than inherit authority from the zero-momentum Wilson
coefficient.

## Two-momentum boundary-response tomography: WP770

- flavor-two-momentum-boundary-response-tomography.md
- checkers/wp770_two_momentum_boundary_response_tomography.py
- results/wp770_two_momentum_boundary_response_tomography.json

WP770 turns WP769's finite-response ambiguity into a minimal instrument
theorem. At fixed calibrated bulk mass and length, the response depends only
on (s=r_0+r_L) and (t=r_0r_L). One momentum leaves an affine fiber; the
two declared spacelike ports (p=1,2) have a rank-two response and reconstruct
((s,t)) exactly. This identifies the unordered endpoint pair, which is the
faithful coordinate for the symmetric transfer function, without claiming
labelled endpoint ontology. The momentum and amplitude standards create a new
relational experiment. Actual flavor-channel realization, uncertainty rank,
source selection of (m\ell), gauge normalization, RG basin, and `physical16`
descent remain open.

## Radius-free static portal composition: WP771

- flavor-radius-free-static-portal-composition.md
- checkers/wp771_radius_free_static_portal_composition.py
- results/wp771_radius_free_static_portal_composition.json

WP771 composes the positive full-tower half-twist branch, first vector KK
level, separated-boundary static protection, and two-momentum tomography. The
half twist gives (epsilon=1/5), while (N=1) and (ell=\pi R) give
(M_V\ell=\pi); both are radius-independent. The resulting contrast is still
(g_*^2/10). The remaining source fiber is therefore the gauge normalization,
not the compactification radius. Current packets cannot close it jointly:
the link-only lift has positive spectral sign, the portal-bulk lift reverses
that sign, and the compulsory-mediator gauge-Yukawa system has no physical
fixed-point branch. The next constructor must derive positive spectral
localization and an isolated gauge normalization in the same anomaly-complete
five-dimensional source.

## SU(4) gauge-link boundary-normalization fiber: WP772

- flavor-su4-gauge-link-boundary-normalization-fiber.md
- checkers/wp772_su4_gauge_link_boundary_normalization_fiber.py
- results/wp772_su4_gauge_link_boundary_normalization_fiber.json

WP772 supplies the first joint bulk object for two WP771 gates. Under the
parity (operatorname{diag}(1,1,-1,-1)), the (SU(4)) adjoint splits into the
seven-generator (SU(2)_A\times SU(2)_B\times U(1)) algebra and an
eight-real-dimensional complex bifundamental (A_5) sector. The link is thus
a gauge component, not a hypermultiplet, and the pure vector spectral index is
(kappa=17>0). The complete boundary ring still defeats numerical selection:
residual gauge symmetry permits independent kinetic terms, and even an exact
site exchange leaves a common coefficient \(\tau\). At fixed bulk normalization,
\(\tau=0,1\) changes the portal from \(1/10\) to \(1/20\). A further boundary
principle must fix or forbid this common mode before an isolated RG
normalization has physical authority.

## SU(4) localization-normalization trilemma: WP773

- flavor-su4-localization-normalization-trilemma.md
- checkers/wp773_su4_localization_normalization_trilemma.py
- results/wp773_su4_localization_normalization_trilemma.json

WP773 tests whether moving the portal operands into the bulk repairs WP772's
common boundary normalization. It does not. Orbifold fixed points admit the
residual-gauge-invariant kinetic term regardless of matter localization.
Boundary localization keeps the pure-vector index \(\kappa=17>0\); the bulk
portal packet retains the modulus, costs \(32\) hypermultiplet degrees, and
gives \(\kappa=-15\). Adding the compulsory mediators gives \(-63\). The
positive index budget is only \(16\). A larger source needs at least sixteen
additional vector degrees and a separate source principle fixing the common
orbifold kinetic coefficient.

## Minimal SU(6) vector budget and boundary modulus: WP774

- flavor-minimal-su6-vector-budget-boundary-modulus.md
- checkers/wp774_minimal_su6_vector_budget_boundary_modulus.py
- results/wp774_minimal_su6_vector_budget_boundary_modulus.json

WP774 computes the smallest unitary simple-group enlargement passing WP773's
bulk portal spectral budget. For \(SU(n)\), \(\kappa=n^2-31\): \(SU(5)\) gives
\(-6\), while \(SU(6)\) gives \(5\). The branching
\(35=15+3+1+8+8\) contains the original \(SU(4)\) parent and supplies twenty
extra vector degrees. This is a classification, not a selector. Bulk
compulsory mediators lower the index to \(-43\), and the orbifold common
kinetic coefficient remains legal and changes the portal magnitude. Anomaly,
chirality, and boundary dynamics must independently require the enlargement
and fix its normalization.

## SU(6) anomaly-family spectral generation gate: WP775

- flavor-su6-anomaly-family-spectral-generation-gate.md
- checkers/wp775_su6_anomaly_family_spectral_generation_gate.py
- results/wp775_su6_anomaly_family_spectral_generation_gate.json

WP775 tests whether anomaly cancellation independently selects WP774's
favorable bulk source. The minimal chiral family \(15+2\overline6\) has zero
cubic anomaly and degree \(27\). With the \(SU(6)\) vector adjoint,
\(\kappa(n_f)=37-27n_f\): zero and one bulk families give \(37,10\), while
two and three give \(-17,-44\). Thus positive half-twist selection permits at
most one complete bulk family. Anomaly cancellation derives the representation
sum but not its localization; boundary-localizing three anomaly-free families
preserves the spectral sign while retaining the common kinetic modulus. A
source-derived generation-localization and inflow law is still required.

## Five-dimensional domain-wall generation-rank no-go: WP776

- flavor-five-dimensional-domain-wall-generation-rank-no-go.md
- checkers/wp776_five_dimensional_domain_wall_generation_rank_no_go.py
- results/wp776_five_dimensional_domain_wall_generation_rank_no_go.json

WP776 closes the multi-kink economy proposed after WP775. A scalar chiral
zero-mode equation is first order and has one integration constant. The exact
profile \(M(y)=(y+1)y(y-1)\) has three sign crossings but a one-dimensional
kernel. An \(r\)-component system has at most \(r\) independent profiles, so
three generations require rank-three matter and retain the full \(81\)-degree
spectral cost, giving \(\kappa=-44\). Multiple localization peaks are a
presentation of one state, not generation multiplicity. Any escape must use a
genuine higher-dimensional index-three operator and recompute its spectral
measure in that new source frame.

## Flux-three index and spectral degeneracy: WP777

- flavor-flux-three-index-spectral-degeneracy.md
- checkers/wp777_flux_three_index_spectral_degeneracy.py
- results/wp777_flux_three_index_spectral_degeneracy.json

WP777 opens the genuine higher-dimensional escape required by WP776. Unit
charge and flux three give Dirac index three, while the opposite flux reverses
chirality. This is real kernel multiplicity. It is not a spectral economy:
every Landau level has degeneracy \(|qm|=3\), so one \(27\)-degree \(SU(6)\)
family carries weighted tower degree \(81\). The five-dimensional signed
count happens to return \(-44\), but its potential cannot be transported into
the changed six-dimensional experiment. Flux quantization also permits every
integer and selects neither magnitude three nor its orientation. A complete
six-dimensional anomaly/tadpole packet and flux-weighted effective potential
are now required.

## Flux anomaly, tadpole, and stability gate: WP778

- flavor-flux-anomaly-tadpole-stability-gate.md
- checkers/wp778_flux_anomaly_tadpole_stability_gate.py
- results/wp778_flux_anomaly_tadpole_stability_gate.json

WP778 tests the first complete consistency arrows rather than fitting another
flux integer. Local anomaly descent has the homogeneous form
\(A_4(m)=mA_6\); once the parent coefficient vanishes, every integer flux has
the same zero anomaly readout. The minimal integrated tadpole
\(c\,m+Q_{\mathrm{loc}}=0\) selects \(m=3\) only when the independently fixed
source charge obeys \(Q_{\mathrm{loc}}=-3c\), so an undeclared charge merely
relocates the tuning. Internal non-Abelian flux also has a charged-vector
lowest mode with \(M^2=-|qB|\), defeating the stable-basin gate. The smallest
remaining window is a distinct anomaly-free \(U(1)_F\) flux source with
quantized localized charge that compels oriented flux three, a tachyon-free
complete spectrum, fixed normalization, and calibrated physical16 ports.

## Minimal external-U(1) family-charge no-go: WP779

- flavor-minimal-external-u1-family-charge-no-go.md
- checkers/wp779_minimal_external_u1_family_charge_no_go.py
- results/wp779_minimal_external_u1_family_charge_no_go.json

For charges \((x,y,z)\) on \(15,\overline6,\overline6\), ordinary mixed
\(SU(6)^2U(1)_F\) and gravitational anomaly cancellation force
\((x,y,z)=(0,a,-a)\); the cubic anomaly then vanishes identically. Flux three
therefore gives indices \((0,3a,-3a)\): no \(15\) zero modes and an
oppositely oriented vectorlike antifundamental pair, not three complete chiral
families. The same packet has zero linear source charge and cannot supply the
WP778 tadpole. The next source must add \(SU(6)\)-charged matter or a
Green--Schwarz sector and derive, rather than fit, both common-sign family
charge and the oriented tadpole.

## Added-matter external-U(1) spectral no-go: WP780

- flavor-added-matter-u1-completion-spectral-no-go.md
- checkers/wp780_added_matter_u1_completion_spectral_no_go.py
- results/wp780_added_matter_u1_completion_spectral_no_go.json

WP780 constructs rather than assumes the smallest ordinary-matter repair in
the declared charge box. A common unit family charge is anomaly-completed by a
\(6+\overline6\) pair of charges \((-3,-3)\) and four singlets
\((-7,4,4,8)\). All ordinary anomalies cancel exactly. At flux three, however,
the family, vectorlike pair, and singlets contribute weighted degrees
\(81,108,69\), totaling \(258\) and giving the inherited diagnostic
\(\kappa=-220\). The charge-reversed completion is equally valid and the net
linear charge remains zero, so neither orientation nor the WP778 tadpole is
selected. Ordinary added matter therefore accommodates the desired flux but
destroys its favorable spectral basin. The surviving branch is a
geometrically quantized Green--Schwarz constructor.

## Green--Schwarz product and Stückelberg fiber: WP781

- flavor-green-schwarz-product-stueckelberg-fiber.md
- checkers/wp781_green_schwarz_product_stueckelberg_fiber.py
- results/wp781_green_schwarz_product_stueckelberg_fiber.json

WP781 tests the minimal Green--Schwarz effective constructor. Gauge invariance
fixes only \(A=kc\), leaving the continuous fiber
\((k,c)\sim(\rho k,c/\rho)\). Along this fiber the Stückelberg mass changes by
\(\rho^2\), while low-energy exchange changes by \(\rho^{-2}\). Charge,
axion-shift, and flux reversal preserves anomaly cancellation, mediator mass,
and chiral index, and the flux integer is absent from the local cancellation
equation. The construction is therefore an anomaly rigidifier, not an
oriented-flux or physical-magnitude selector. A surviving source must be a
concrete compactification intersection lattice whose primitive characteristic
vector fixes \(k,c,f_a\), and \(m=3\) in one common frame and yields calibrated
production and decay ports.

## Rank-one unimodular lattice flux-three no-go: WP782

- flavor-rank-one-unimodular-lattice-flux-three-no-go.md
- checkers/wp782_rank_one_unimodular_lattice_flux_three_no_go.py
- results/wp782_rank_one_unimodular_lattice_flux_three_no_go.json

WP782 tests the smallest integral geometry capable of replacing WP781's
effective coefficient fiber. A positive rank-one unimodular lattice has Gram
form \([1]\), and its primitive vectors pair only to \(\pm1\). Gram form
\([3]\) pairs primitive generators to three but has determinant three and is
not self-dual; the unimodular form reaches three only with the nonprimitive
vector \(3e\). The isometry \(e\mapsto-e\) preserves the lattice, and the
continuous Hodge/kinetic metric is not fixed by the integral form. Hence the
rank-one geometry either violates the quantum-consistency gate or writes the
desired integer into its source data, while still leaving orientation,
threshold normalization, and instrumentation open.

## Rank-two unimodular pairing-three fiber: WP783

- flavor-rank-two-unimodular-pairing-three-fiber.md
- checkers/wp783_rank_two_unimodular_pairing_three_fiber.py
- results/wp783_rank_two_unimodular_pairing_three_fiber.json

WP783 passes to the physical signature-\((1,1)\) rank-two charge lattices. The
even hyperbolic plane has no primitive characteristic vector. In the odd
lattice, \(b=(1,1)\) is primitive characteristic, but the primitive vectors
\(f_1=(2,-1)\) and \(f_2=(4,1)\) both pair to three while having invariant
norms \(3\) and \(15\). They are therefore inequivalent under the full lattice
isometry group. Two exact compatible positive kinetic metrics also assign the
same flux different energies, \(5\) and \(13/4\). Rank two permits primitive pairing
three but selects neither a unique flux orbit nor the physical threshold
normalization.

## Flux-energy metric rigidifier and orientation doublet: WP784

- flavor-flux-energy-metric-rigidifier-orientation-doublet.md
- checkers/wp784_flux_energy_metric_rigidifier_orientation_doublet.py
- results/wp784_flux_energy_metric_rigidifier_orientation_doublet.json

WP784 supplies the first progressive dynamics in the lattice branch. The
positive quadratic flux energy reduces the primitive pairing-three fiber to
\(f_+=(2,-1)\) and \(f_-=(1,-2)\), with invariant norms \(+3\) and \(-3\).
Joint minimization stabilizes the compatible metric ratio at \(t=\log3\) with
strict Hessian and dimensionless energy three. The two fluxes remain exactly
degenerate because the energy is orientation-even. An overall scale remains
free, and the potential is blind to the Green--Schwarz product-preserving
tangent \((k,-c)\). Flux backreaction is therefore a genuine metric
rigidifier and partial orbit selector, but not yet the sign, threshold, or
physical-readout selector.

## Orientation-odd bias and reference-port no-go: WP785

- flavor-orientation-odd-bias-reference-port-no-go.md
- checkers/wp785_orientation_odd_bias_reference_port_no_go.py
- results/wp785_orientation_odd_bias_reference_port_no_go.json

WP785 separates algebraic discrimination from physical selection. The two
WP784 minimizers already have the invariant discriminator \(q=f^2=\pm3\).
A reference-free topological factor \(\exp(i\theta q)\) changes phase but not
probability weight, so it cannot lift the energy doublet. The smallest real
bias \(\mu q\) splits the branches by \(6\mu\) and remains positive for
\(|\mu|<1\), but it descends under orientation reversal only when \(\mu\) is
itself a pseudoscalar reference. That is a new relational experiment over the
reference stabilizer groupoid. A symmetric dynamical reference leaves paired
equal-energy vacua, and constant \(\mu\) is blind to the Green--Schwarz
product kernel. The missing principle must therefore derive an asymmetric
boundary/source state, not merely permit an orientation-odd coefficient.

## Mirror-completion sign-selection no-go: WP786

- flavor-mirror-completion-sign-selection-no-go.md
- checkers/wp786_mirror_completion_sign_selection_no_go.py
- results/wp786_mirror_completion_sign_selection_no_go.json

WP786 follows the proposed asymmetric state through the complete sign
pipeline. The genuinely chiral anomaly-free packet
\((-9,-5,-1,7,8)\) and its mirror both cancel linear and cubic anomalies and
have the same quadratic RG weight \(220\). Mirror-equivariant beta functions
give paired fixed points with equal critical exponents; finite thresholds
transport both; inclusive widths identify them. A calibrated parity-labelled
instrument can separate their signs, but readout has no authority to delete a
source constructor. The sought principle must therefore be an independently
non-mirror-completable boundary or incidence object that also fixes the
continuous normalization and threshold clock.

## SU(4) cubic orientation and portal fiber: WP787

- flavor-su4-cubic-orientation-portal-fiber.md
- checkers/wp787_su4_cubic_orientation_portal_fiber.py
- results/wp787_su4_cubic_orientation_portal_fiber.json

WP787 opens the first post-SO(5) parent with both a \(3+1\) fundamental and a
nonzero cubic invariant. For
\(T=\operatorname{diag}(1,1,1,-3)\), the minimal cubic-plus-quartic adjoint
potential has the stable vacuum \(a_*=\kappa/(6\lambda)\). Its complete
adjoint Hessian consists of eight positive modes, six Goldstones, and one
positive radial mode. Thus fixed nonzero \(\kappa\) genuinely selects and
stabilizes a carrier orientation. But the smallest portal spurion gives
\(g_n-g_m=2\eta\kappa/(3\lambda)\): changing \(\eta\)'s sign reverses the
portal without changing the vacuum, and a continuous \(\kappa,\eta\) scaling
fiber survives. The parent cubic and portal vertex must therefore descend
from one quantized source operation before RG, threshold, or instrument
authority can be claimed.

## Five-dimensional supersymmetric prepotential Coulomb-modulus no-go: WP788

- flavor-5d-susy-prepotential-coulomb-modulus-no-go.md
- checkers/wp788_5d_susy_prepotential_coulomb_modulus_no_go.py
- results/wp788_5d_susy_prepotential_coulomb_modulus_no_go.json

WP788 tests the extended-gauge parallelization suggested by WP787. On the
\(SU(4)\) ray, the five-dimensional cubic prepotential gives kinetic metric
\(G(a)=12r-24ka\). At the formal fixed-point face \(r=0\), positivity fixes
the sign of \(a\) relative to the quantized level \(k\), but unbroken
supersymmetry leaves \(a\) as a flat Coulomb modulus. Gauge-fixed fundamental
weights remove the independent vertex \(\eta\) and give signed masses
\((a,a,a,-3a)\), yet scalar masses are orientation-even and the absolute
threshold remains proportional to \(\lvert a\rvert\). The exact hostile pair
\(a=-s,-2s\) shares the level, positive cone, and \(3:1\) threshold ratio
while its scalar contrast differs by four. A source-derived modulus-lifting
operation is still required, without a new arbitrary soft scale.

## Wilson-line angle and radius homogeneity no-go: WP789

- flavor-wilson-line-angle-radius-homogeneity-no-go.md
- checkers/wp789_wilson_line_angle_radius_homogeneity_no_go.py
- results/wp789_wilson_line_angle_radius_homogeneity_no_go.json

WP789 grants the most favorable radiative lift of WP788: an oriented periodic
Hosotani shape that uniquely selects a Wilson angle. For every one-scale
potential \(C F(\theta)/R^4\), however, joint stationarity forces
\(F=F'=0\), and the entire radius row of the Hessian vanishes. The exact
hostile pair \((\phi,R_0)\), \((\phi,2R_0)\) shares the selected angle and
energy while halving every absolute threshold. A second \(R^{-6}\) term can
stabilize the clock only at \(R_*^2=-3Bg/(2Af)\), transferring numerical
authority to a signed coefficient ratio. The surviving positive architecture
must derive both radius homogeneities from the same chiral source packet.

## Curvature--flux radion and magnitude selector: WP790

- flavor-curvature-flux-radion-magnitude-selector.md
- checkers/wp790_curvature_flux_radion_magnitude_selector.py
- results/wp790_curvature_flux_radion_magnitude_selector.json

WP790 realizes WP789's two-homogeneity architecture in six-dimensional
Einstein--Maxwell compactification. Curvature and flux give
\(-B/R^4+An^2/R^6\), with the strict minimum
\(R_*^2=3An^2/(2B)\). The signed threshold becomes
\(\sigma n/R_*=\sigma\sqrt{2B/(3A)}\): its magnitude is independent of the
flux integer and is fixed conditional on the gauge--gravity ratio. The
potential is exactly blind to \(\sigma\), so the mirror-sign obstruction
survives. The unlifted minimum is AdS, and a Minkowski completion requires
\(C=B^2/(4An^2)\). The positive successor must derive orientation, \(B/A\),
and any uplift relation from one non-mirror-completable gauge--gravity packet.

## Salam--Sezgin chirality, scale, and charge fiber: WP791

- flavor-salam-sezgin-chirality-scale-charge-fiber.md
- checkers/wp791_salam_sezgin_chirality_scale_charge_fiber.py
- results/wp791_salam_sezgin_chirality_scale_charge_fiber.json

WP791 finds the first non-mirror-completable orientation selector in the
branch. In chiral \(N=(1,0)\) gauged supergravity, the unit monopole has Chern
number one and its BPS spinor obeys \(\sigma_3\eta=+\eta\); reversing flux
requires the opposite chiral source. The same coupling fixes the monopole,
sphere curvature, potential, and exact consistent Minkowski reduction, thereby
parallelizing WP790's gauge--gravity coefficients. Two fibers survive. The
physical KK scale \(g e^{\phi_0/2}\) varies with the retained massless scalar,
and unit flux gives index \(q\), so three families require an independently
derived matter charge \(q=3\). The positive successor must obtain charge three
and dilaton lifting from the anomaly-complete chiral matter packet without
destroying the BPS orientation or exact reduction.

## Anomaly-complete monopole family and stability no-go: WP792

- flavor-anomaly-complete-monopole-family-stability-no-go.md
- checkers/wp792_anomaly_complete_monopole_family_stability_no_go.py
- results/wp792_anomaly_complete_monopole_family_stability_no_go.json

WP792 tests the canonical anomaly-free successor to WP791. In the
\(E_7\times E_6\times U(1)_R\) model with the monopole embedded in
\(E_6\supset SO(10)\times U(1)\), the chiral gaugino index gives
\(N_{\mathrm{fam}}=2|n|\). The complete charged-vector fluctuation spectrum
requires \(|N^I|\leq1\), leaving \(n=\pm1\) and exactly two families on the
stable nonzero branch. Thus no integer flux produces three; \(n=2\) produces
four and is unstable. The family monopole is also not the \(U(1)_R\) BPS
embedding that selected orientation in WP791. The anomaly-complete branch
therefore explains its stable two-family result but refutes itself as the
single three-family constructor. The positive successor must derive odd index
three, orientation, modulus lifting, and charged-spectrum stability from one
source embedding before RG, thresholds, or physical16 readout are tested.

## F-theory vertical-flux mirror and moduli no-go: WP793

- flavor-f-theory-vertical-flux-mirror-moduli-no-go.md
- checkers/wp793_f_theory_vertical_flux_mirror_moduli_no_go.py
- results/wp793_f_theory_vertical_flux_mirror_moduli_no_go.json

WP793 moves the odd-family problem to globally quantized \(G_4\)-flux. In the
finite vertical-flux scan over elliptic fourfolds with base \(\mathbb P^3\),
quantization, M/F-theory matching, and D3 tadpole capacity make three the
minimum permitted family number. This derives more than an inserted
charge-three field, but it does not select a unique physical point. The exact
involution \(G_4\mapsto-G_4\) preserves shifted quantization, every homogeneous
transversality and primitivity equation, and the quadratic tadpole, while
reversing all matter-surface chiral indices. Horizontal-flux and vector-like
completions also remain outside the admitted packet, and vertical flux does not
fix all moduli, portal normalization, RG thresholds, or a physical16
instrument. Global flux is therefore a family-magnitude rigidifier but not the
required asymmetric portal selector.

## Mirror-equivariant pipeline selector no-go: WP794

- flavor-mirror-equivariant-pipeline-selector-no-go.md
- checkers/wp794_mirror_equivariant_pipeline_selector_no_go.py
- results/wp794_mirror_equivariant_pipeline_selector_no_go.json

WP794 extracts the general theorem behind WP784--WP793. On a free two-point
mirror orbit, an invariant selector has equal weights on both members and
cannot have singleton support, even if an even potential fixes the portal
magnitude. Equivariant RG preserves paired basin data; inclusive thresholds
collapse the sign; signed instruments distinguish a prepared member but
cannot select its source. A reference orientation creates a relational readout
over a stabilizer groupoid, while a dynamical mirror-odd reference restores
the paired joint states. The first nonfaithful arrow is source selection. The
necessary successor is a non-mirror-completable boundary or irreversible
history constructor co-generating orientation, calibration reference,
magnitude, RG initial condition, and threshold state.

## Domain-wall inflow and flavor-overlap fiber: WP795

- flavor-domain-wall-inflow-overlap-fiber.md
- checkers/wp795_domain_wall_inflow_overlap_fiber.py
- results/wp795_domain_wall_inflow_overlap_fiber.json

WP795 tests the first constructive realization of WP794's required source
type. Ordered scalar-wall endpoints trap one chirality, and bulk
Chern--Simons inflow supplies a quantized anomalous current that survives RG
and massive thresholds. Yet the flavor Yukawa is the Gaussian overlap
\(y_{ij}=\rho e^{-\mu^2(\ell_i-\ell_j)^2/2}\), with
\(\ell_i=-M_i/(2\mu^2)\). The exact separations \(1/\mu\) and \(2/\mu\) share
all chirality and anomaly data while giving \(\rho e^{-1/2}\) and
\(\rho e^{-2}\); swapping their species assignment reverses \(g_n-g_m\).
The wall is therefore a chirality selector and anomaly rigidifier, but its
orientation history, localization geometry, portal magnitude, threshold
clock, and physical16 perturbation instrument remain unselected.

## Compact clockwork relative portal and source fiber: WP796

- flavor-compact-clockwork-relative-portal-fiber.md
- checkers/wp796_compact_clockwork_relative_portal_fiber.py
- results/wp796_compact_clockwork_relative_portal_fiber.json

WP796 discretizes WP795's localization geometry. A compact \(U(1)\) incidence
with link charges \((1,-q)\) has a unique kernel profile
\((1,q^{-1},\ldots,q^{-N})\) and a positive gear gap. It therefore genuinely
selects relative couplings once the integer incidence is fixed. Compactness
does not select the integer \(q\), chain length, orientation, or endpoint
species assignment: \(q=2\) and \(q=3\) give different ratios, while chain
reversal preserves the complete gear spectrum and reverses the endpoint
contrast. The absolute gauge coupling \(g\), threshold scale \(m\), completed
matter RG, and physical16 instrument also remain. Clockwork replaces the
continuous overlap fiber by a discrete incidence fiber and two continuous
normalizations, but does not yet supply the single source constructor.

## Affine G2 root--coroot portal typing: WP797

- flavor-affine-g2-root-coroot-portal-typing.md
- checkers/wp797_affine_g2_root_coroot_portal_typing.py
- results/wp797_affine_g2_root_coroot_portal_typing.json

WP797 tests whether the asymmetric triple bond of \(G_2\) derives WP796's
integer incidence. Finite \(G_2\) is full rank and supplies no zero mode. Its
affine extension has Kac marks \((1,3,2)\), but the same Cartan datum supports
two canonical executable quadratic packets: the root Gram form has the mark
kernel \((1,3,2)\), while the coroot Gram form has the distinct comark kernel
\((1,1,2)\). Both are positive semidefinite with exact gaps. Thus affine
\(G_2\) conditionally selects a relative ray only after a root-versus-coroot
coupling functor is declared. The bare root datum fixes neither that functor,
the node-to-species map, kernel sign, overall coefficient, completed RG and
threshold theory, nor a calibrated `physical16` instrument. The positive
successor must derive all of those interfaces from one source action.

## D4 triality-fold portal typing: WP798

- flavor-d4-triality-fold-portal-typing.md
- checkers/wp798_d4_triality_fold_portal_typing.py
- results/wp798_d4_triality_fold_portal_typing.json

WP798 derives the \(G_2\) triple bond upstream from the order-three triality
of affine \(D_4^{(1)}\). The fold is the twisted affine system \(D_4^{(3)}\),
not the untwisted \(G_2^{(1)}\) packet of WP797. Its unique source null vector
has coordinates \((1,2,1)\) in the integral orbit-sum basis,
\((1,2,3)\) in the orbit-average basis, and \((1,2,\sqrt3)\) after canonical
normalization; all three are exactly the same \(D_4\) vector. Triality
therefore makes orbit cardinality three and the long--short incidence hard to
vary, but it does not turn the displayed coefficient three into a
basis-independent portal observable. The remaining constructor must
co-generate the chiral electric representation, kinetic pairing,
node-to-species map, absolute scale, matter RG, finite thresholds, and
calibrated physical16 response.

## Monodromic G2 polarization and scale fiber: WP799

- flavor-monodromic-g2-polarization-scale-fiber.md
- checkers/wp799_monodromic_g2_polarization_scale_fiber.py
- results/wp799_monodromic_g2_polarization_scale_fiber.json

WP799 promotes WP798's fold to the physical \(N=2\) monodromic gauge
construction. Dirac integrality and the BPS category tie electric roots to
magnetic coroots and thus repair the bare algebraic pairing ambiguity. They do
not select a Standard Model portal. The fixed \(G_2\) beta coefficient gives
an asymptotically free trajectory, but dimensional transmutation replaces the
ultraviolet coupling by a free RG-invariant \(\Lambda\); \(g_0=1/4\) and
\(g_0=1/3\) are an exact hostile pair. Coulomb moduli independently vary BPS
thresholds, and the Gaussian UV endpoint gives zero portal. The monodromic
source is therefore a charge parallelizer and relative-Clebsch rigidifier,
not a nonzero magnitude, threshold-state, or physical16 selector. The next
candidate must be an isolated source with no marginal normalization or vacuum
modulus, plus chiral flavor descent and a calibrated instrument.

## Isolated fixture interface and deformation fiber: WP800

- flavor-isolated-fixture-interface-deformation-fiber.md
- checkers/wp800_isolated_fixture_interface_deformation_fiber.py
- results/wp800_isolated_fixture_interface_deformation_fiber.json

WP800 tests WP799's isolated-source successor using a three-punctured
\(Z_3\)-twisted \(D_4\) fixture. The fixture has no complex-structure coupling
modulus and can fix normalized intrinsic SCFT data. The physical portal is
not intrinsic: coupling a dimension-two fixture operator to a dimension-two
Standard Model bilinear introduces an external coefficient \(\kappa\), so the
portal is \(\kappa C\). Intrinsic probes have Jacobian \((1,0)\) on
\((C,\kappa)\) and are blind to the full interface direction. A relevant
deformation introduces a free threshold scale proportional to \(\sqrt m\),
and the rank-one Coulomb vacuum remains unselected. Isolation therefore
selects intrinsic CFT data but not portal sign, magnitude, threshold state, or
physical16 readout. The next source must contain the Standard Model operator
and portal internally, with no marginal portal direction and with a uniquely
selected massive vacuum and instrument.

## UV fixed-point portal and relevant clock fiber: WP801

- flavor-uv-fixed-point-relevant-clock-fiber.md
- checkers/wp801_uv_fixed_point_relevant_clock_fiber.py
- results/wp801_uv_fixed_point_relevant_clock_fiber.json

WP801 tests asymptotic safety as the first principle capable of internalizing
WP800's interface coefficient. An ultraviolet-repulsive portal direction is
fixed by the requirement of reaching an isolated interacting fixed point, so
the dimensionless magnitude can in principle be predicted rather than tuned.
The same fixed point retains every ultraviolet-attractive relevant mass
trajectory: (m=1) and (m=4) share the ultraviolet endpoint but give
thresholds in ratio (1:2). An even fixed-point equation also retains the two
sign branches, and detector calibration remains an independent coordinate.
Thus asymptotic safety is progressive for dimensionless portal magnitude but
is not yet a complete Deutschian explanation. A viable successor must combine
an anomaly-complete chiral fixed point, an orientation-odd invariant, a unique
massive vacuum or source-generated clock, exact threshold matching, and a
calibrated physical16 instrument in one source construction.

## Litim--Sannino fixed-point flavor audit: WP802

- flavor-litim-sannino-fixed-point-flavor-audit.md
- checkers/wp802_litim_sannino_fixed_point_flavor_audit.py
- results/wp802_litim_sannino_fixed_point_flavor_audit.json

WP802 tests WP801 against the canonical perturbative four-dimensional
gauge--Yukawa fixed point. The exact NLO beta functions fix
(alpha_y^*/\alpha_g^*=6/(13+2\epsilon)), and the two-coupling stability
matrix has one relevant and one irrelevant direction. This genuinely predicts
a dimensionless ratio on the ultraviolet critical surface. It does not predict
the requested asymmetric portal: (alpha_y\propto y^2) erases the Yukawa
sign, the Dirac fundamental matter is gauge-vectorlike, and the remaining
relevant trajectory carries a free crossover scale. Mass deformations and
detector calibration add independent fibers. The successor must instead be a
chiral anomaly-complete fixed point with a rephasing-invariant orientation-odd
portal, plus an internally selected massive vacuum and physical16 instrument.

## Chiral safe-window integrality and incidence audit: WP803

- flavor-chiral-safe-window-integrality-audit.md
- checkers/wp803_chiral_safe_window_integrality_audit.py
- results/wp803_chiral_safe_window_integrality_audit.json

WP803 tests the strongest known perturbative chiral successor. Generalized
Georgi--Glashow and Bars--Yankielowicz matter cancels the cubic gauge anomaly
exactly. Nevertheless, the finite (SU(5)) mesonic safe window is the open
interval from (51/2) to
((1997+\sqrt{12271273})/212\approx25.9436), which contains no integer matter
multiplicity. The analytically continued fixed point is exact, but it is not a
finite physical field packet. In addition, the safety-generating meson Yukawa
couples the vectorlike (F,\widetilde F) pair and omits the anomaly-essential
chiral tensor; its squared coordinate erases sign. The successor must require
integer matter content and direct incidence of the orientation-sensitive
irrelevant portal on the chiral representation itself.

## Direct chiral-tensor Yukawa safety no-go: WP804

- flavor-chiral-tensor-yukawa-safety-no-go.md
- checkers/wp804_chiral_tensor_yukawa_safety_no_go.py
- results/wp804_chiral_tensor_yukawa_safety_no_go.json

WP804 tests the complementary Higgs-like Yukawa
(T^{ab}\widetilde F_aH_b), whose incidence on the anomaly-essential chiral
tensor is nonzero. At finite (SU(5)), both sign conventions fail the
interacting-safety inequalities exactly: the upper branch requires both
(x>77/20) and (x<1601/1610), while the lower requires (x>101/20) and
(x<5107/2254). The interaction can define a relative fixed-flow ray in the
asymptotically free region but cannot select a nonzero ultraviolet portal. Its
squared coupling is sign-blind and its single hyperedge has no invariant phase
cycle. WP803 and WP804 are therefore complementary: the safe meson Yukawa
misses chirality, while the chiral-tensor Yukawa misses safety. The successor
must use a coupled chiral Yukawa cycle whose orientation-sensitive invariant
itself generates an irrelevant fixed-point direction.

## Integer coupled chiral fixed-point phase audit: WP805

- flavor-integer-coupled-chiral-fixed-point-phase-audit.md
- checkers/wp805_integer_coupled_chiral_fixed_point_phase_audit.py
- results/wp805_integer_coupled_chiral_fixed_point_phase_audit.json

WP805 combines both scalar sectors at the integer anomaly-complete packet
((N,p)=(5,26)). The truncated beta system has an exact fully interacting
solution, and the anomaly-essential chiral tensor participates directly. This
is the closest source yet. However, (a_g^*=3163/2234>1) and
(a_H^*=34182/5585>6), so the fixed point lies beyond the admitted
perturbative control. The three Yukawa phase-charge rows also have full row
rank, hence (ker Q^T=0): every Yukawa phase is removable even though their
squared magnitudes mix in the beta functions. Multiple hyperedges are
therefore necessary but not sufficient. The successor must create a genuine
rephasing-invariant phase cycle whose interference term participates in a
controlled irrelevant fixed-point direction.

## Phase-cycle weak-basis descent and CP-pair audit: WP806

- flavor-phase-cycle-weak-basis-cp-pair-audit.md
- checkers/wp806_phase_cycle_weak_basis_cp_pair_audit.py
- results/wp806_phase_cycle_weak_basis_cp_pair_audit.json

WP806 corrects the assumption that any Yukawa incidence cycle supplies a
physical orientation. The (2\times2) plaquette product is invariant under
diagonal field rephasings but changes from (i) to zero under a unitary weak-
basis transformation preserving (Y^\dagger Y). It is chart data. The first
faithful orientation tested is the three-generation invariant
(\operatorname{Im}\det[H_u,H_d]), which survives simultaneous weak-basis
conjugation and reverses under CP. A CP-even source can select its magnitude
but necessarily pairs its two signs; an exact phase potential exhibits the
degenerate minima explicitly. The remaining source principle must therefore
authorize a CP-odd datum on the faithful quotient, without inserting its sign
as a free coefficient or reference port, and must still supply thresholds and
the physical16 instrument.

## Anomaly-inflow relational orientation audit: WP807

- flavor-anomaly-inflow-relational-orientation-audit.md
- checkers/wp807_anomaly_inflow_relational_orientation_audit.py
- results/wp807_anomaly_inflow_relational_orientation_audit.json

WP807 tests anomaly inflow as WP806's source-derived CP-odd datum. A quantized
level (k) fixes the relative bias (k\eta J), and anomaly matching protects
it under symmetry-preserving RG and gapped vectorlike thresholds. This is the
first candidate to combine magnitude selection with threshold protection. It
still selects only a relational sign: the joint minima
((\eta,J)=(+1,+1)) and ((-1,-1)) are mirror partners with identical inflow
current. Fixing the boundary normal restricts the experiment to a stabilizer
groupoid rather than revealing an absolute flavor sign. The successor must
derive a unique oriented defect from the same source and provide a calibrated
physical16 current instrument.

## Compact defect charge and boundary-port audit: WP808

- flavor-compact-defect-charge-boundary-port-audit.md
- checkers/wp808_compact_defect_charge_boundary_port_audit.py
- results/wp808_compact_defect_charge_boundary_port_audit.json

WP808 tests whether WP807's source can internally generate its required
oriented defect. On a compact boundaryless transverse space, wall charges
telescopically sum to zero, so every kink has compensating antikink charge and
the inclusive anomaly inflow vanishes. An interval or noncompact line admits a
single wall only after ordered endpoint or asymptotic-sector data are supplied;
reversing those data gives the equal-energy mirror wall. Fixing one order
therefore defines a stabilizer-groupoid relational experiment. Local current
readout further requires a localization patch, signed detector normal,
calibration, and a physical16 map. The theorem is a hard-to-vary explanation
of the compact-source obstruction, not yet a positive explanation of flavor
orientation. The successor must derive a non-mirror-completable global index
and co-generate its magnitude, RG basin, thresholds, and calibrated readout.

## Invertible-anomaly mirror-completion audit: WP809

- flavor-invertible-anomaly-mirror-completion-audit.md
- checkers/wp809_invertible_anomaly_mirror_completion_audit.py
- results/wp809_invertible_anomaly_mirror_completion_audit.json

WP809 tests WP808's strongest escape hatch: a nonzero global anomaly carried
by an invertible bulk. For any finite anomaly class (a), cancellation uses the
inverse bulk class (-a), while orientation reversal exchanges the consistent
packets ((a,-a)) and ((-a,a)). If (a) is not self-inverse, the signed source
therefore retains a mirror pair. If (a=-a), it is two-torsion and carries no
opposite anomaly label. No invertible class is both signed and a mirror
singleton. Anomaly matching genuinely protects the class across RG and gapped
vectorlike thresholds, but continuous portal magnitude, RG clock, detector
calibration, and physical16 response remain independent. The surviving
candidate must prove a non-mirror-completable non-invertible or microscopic
chiral source rather than selecting one inverse completion by hand.

## Chiral gauge conjugation-closure audit: WP810

- flavor-chiral-gauge-conjugation-closure-audit.md
- checkers/wp810_chiral_gauge_conjugation_closure_audit.py
- results/wp810_chiral_gauge_conjugation_closure_audit.json

WP810 tests whether microscopic chiral gauge consistency excludes the mirror
constructor left by WP809. One Standard Model generation and its fully
conjugated generation both satisfy the complete tested local and global anomaly
conditions and the Yukawa charge-incidence equations. Complex conjugation
preserves quadratic group data, perturbative RG structure, mass singular
values, and thresholds, while reversing the faithful CP-odd invariant and any
signed portal contrast. Gauge chirality is therefore a presentation and source
rigidifier but not an absolute selector. A signed CP instrument can distinguish
a prepared member only after fixing its experimental orientation. The next
candidate must derive a physical source category not closed under conjugation,
and the same constructor must carry the portal magnitude, RG trajectory,
threshold state, and calibrated physical16 response.

## Dissipative-attractor reservoir-port audit: WP811

- flavor-dissipative-attractor-reservoir-port-audit.md
- checkers/wp811_dissipative_attractor_reservoir_port_audit.py
- results/wp811_dissipative_attractor_reservoir_port_audit.json

WP811 tests an autonomous one-way open-system operation as the first genuinely
non-conjugation-equivariant selector. At fixed reservoir, the two-state GKLS
population generator has a unique signed dark-state attractor, a global basin,
a positive dissipative gap, and an executable jump-count record. Positive rate
renormalization preserves the attractor across thresholds. The microscopic
source still admits an inverted reservoir with the same spectrum and opposite
attractor, so orientation has moved into a low-entropy preparation and physical
time contract. The attractor fixes sign but not portal eigenvalue magnitude;
the calibrated steady record has an exact magnitude--gain kernel. Dissipation
is therefore a genuine effective selector and probe, but the source principle
must still co-generate reservoir preparation, rate normalization, threshold
clock, portal scale, and physical16 calibration.

## KMS detailed-balance scale-fiber audit: WP812

- flavor-kms-detailed-balance-scale-fiber-audit.md
- checkers/wp812_kms_detailed_balance_scale_fiber_audit.py
- results/wp812_kms_detailed_balance_scale_fiber_audit.json

WP812 asks whether a thermal KMS law derives WP811's reservoir preparation.
Detailed balance produces a unique Gibbs attractor with signed bias
(tanh(beta Delta/2)) and an executable transition-count instrument. It fixes
only a rate ratio. Reversing the Hamiltonian splitting reverses the attractor
without violating KMS; the bias depends only on the product (beta Delta), and
the absolute dissipative rate remains free. Positive threshold transport can
preserve the sign and basin while changing both bias magnitude and clock. The
steady detector record retains portal-scale and gain fibers. A geometric KMS
source is the next concrete candidate, but it must derive temperature,
splitting orientation, portal normalization, threshold map, and detector frame
without inserting a horizon-orientation reference pair.

## Geometric KMS horizon-parallelization audit: WP813

- flavor-geometric-kms-horizon-parallelization-audit.md
- checkers/wp813_geometric_kms_horizon_parallelization_audit.py
- results/wp813_geometric_kms_horizon_parallelization_audit.json

WP813 tests the strongest geometric completion of WP812. If one horizon fixes
(beta=2 pi/kappa) and a chiral splitting (Delta=n kappa), then the arbitrary
surface-gravity scale cancels: the bias is (tanh(pi n)) and the transition
ratio is (exp(-2 pi n)). Common geometric threshold rescaling preserves this
prediction. This is the closest magnitude architecture yet. It remains
conditional on an unselected integer weight and horizon orientation; reversing
the generator reverses the sign, and formation supplies a low-entropy boundary
condition rather than an automatic local law. Asymmetric finite splitting
corrections break the parallelization, while portal normalization and detector
gain remain confounded. The successor must derive a unit chiral horizon index,
formation orientation, anomaly-protected flavor coupling, and calibrated
physical16 detector interaction in one source packet. Aspect's germ tester
strengthens the qualification: the horizon, flavor, and detector endpoint
germs do not determine their primitive frequency attachments. The same
endpoints with (Delta=a n kappa) at (a=1) and (a=2) yield different targets,
so endpoint-only completion fails the fiber gate. The selector is natively
ternary and its physical realization is quaternary; the required comparison
cell has no present source authority. The scale cancellation is therefore a
conditional theorem on a marked `GeometricKMSFlavorComparisonGerm`, not yet a
physical selector derived by horizon geometry alone.

## Matsubara comparison and realization audit: WP814

- flavor-matsubara-comparison-realization-audit.md
- checkers/wp814_matsubara_comparison_realization_audit.py
- results/wp814_matsubara_comparison_realization_audit.json

WP814 constructs part of WP813's missing germ. Euclidean horizon periodicity
canonically gives bosonic (omega_n=n kappa) and fermionic
(omega_n=(n+1/2) kappa) attachments, so the primitive comparison coefficient
is no longer hand-inserted. The thermal circle does not select a mode. More
importantly, a Matsubara coefficient is not a detector transition: raw discrete
samples have explicit analytic continuation kernels, while a unique physical
continuation requires a complete Osterwalder--Schrader positivity and growth
packet not present in flavor. Aspect's selector remains ternary and the
physical record quaternary after adding a Lorentzian detector-realization germ.
The next candidate must be a reflection-positive chiral flavor--horizon
correlator with unique mode incidence, threshold protection, and calibrated
physical16 coupling.

## Reflection-positive reconstruction and selection audit: WP815

- flavor-reflection-positive-reconstruction-selection-audit.md
- checkers/wp815_reflection_positive_reconstruction_selection_audit.py
- results/wp815_reflection_positive_reconstruction_selection_audit.json

WP815 grants a reflection-positive one-pole flavor--horizon correlator. Its
Euclidean reflection kernel is an exact positive rank-one Gram matrix, and its
first two moments reconstruct residue and pole on the independently declared
one-pole domain. This closes WP814's raw continuation kernel conditionally. It
does not select the domain or its parameters: every positive pole and residue
passes, the quadratic two-point function is blind to portal sign, and positive
threshold pole shifts preserve reflection positivity while changing the
prediction. A one-pole and a two-pole positive measure share the first two
moments, so finite readout cannot authorize the one-pole restriction. Detector
line position and area retain independent calibration fibers. The successor
must derive a reflection-positive odd correlator with unique chiral pole
incidence, protected normalization, and the same operator's calibrated
physical16 detector coupling.

## Mixed OS residue sign-pair audit: WP816

- flavor-mixed-os-residue-sign-pair-audit.md
- checkers/wp816_mixed_os_residue_sign_pair_audit.py
- results/wp816_mixed_os_residue_sign_pair_audit.json

WP816 adds the sign-sensitive mixed correlator missing from WP815. Reflection
positivity bounds the mixed residue by (C^2<=AB). Conditional rank-one purity
fixes the normalized magnitude (|C|/sqrt(AB)=1) but retains the exact pair
(C=plus or minus sqrt(AB)). The two saturated residue matrices are positive,
isospectral, and have identical diagonal readouts; a calibrated mixed channel
separates them only after the relative operator sign port is fixed. Positive
diagonal threshold transport preserves the normalized pair, whereas nonaligned
mixing changes the fixed-axis cross readout. The complete calibrated
three-channel residue family is faithful, but the cross channel alone retains
a source--gain kernel. The successor must derive a pre-quotient odd incidence
that selects the relative operator orientation, authorizes purity, protects
the marked lines, and realizes the calibrated physical16 cross detector.

## Three-operator Gram-loop purity selector: WP817

- flavor-three-operator-gram-loop-purity-selector.md
- checkers/wp817_three_operator_gram_loop_purity_selector.py
- results/wp817_three_operator_gram_loop_purity_selector.json

WP817 supplies the minimal odd incidence missing from WP816. For three marked
real operators, the triangle product
\(R_{12}R_{23}R_{31}\) survives every independent operator-sign change.
Positivity alone admits both signs: equal-magnitude representatives of both
classes are positive at \(r=1/4\). Conditional rank-one purity is stronger.
Every nonzero real rank-one Gram matrix has triangle product
\((v_1v_2v_3)^2>0\); with unit diagonal it also fixes every normalized edge
magnitude to one. The negative equal-magnitude class is positive only through
\(r=1/2\), where it still has rank two.

Aspect's germ tester classifies the construction as natively ternary. Its
operator germs, three primitive attachments, fiber sensitivity, and
comparison-before-quotient order are explicit. The source-authority,
physical16 descent, and common calibrated detector gates remain open.
Real congruence preserves rank-one positivity and cannot create a negative
nonzero loop, but nonaligned transport can erase an attachment. Thus WP817 is
the first intrinsic conditional loop-sign selector in this branch, not yet a
source-authorized physical flavor selector.

## Single-mediator rank-one source audit: WP818

- flavor-single-mediator-rank-one-source-audit.md
- checkers/wp818_single_mediator_rank_one_source_audit.py
- results/wp818_single_mediator_rank_one_source_audit.json

WP818 derives rather than assumes WP817's purity condition. A unique isolated
nondegenerate mediator coupled to three marked flavor operators has residue
\(R=gg^T\), so its nonzero triangle product is
\((g_1g_2g_3)^2>0\) and every squared normalized edge magnitude is one. The
positive loop sign is therefore source-generated on the isolated-pole domain.

The constructor does not select the coupling ray or absolute scale.
Equal-norm rays \((1,2,3)\) and \((1,3,2)\) generate distinct portal matrices,
while \((g,M)\mapsto(\lambda g,\lambda M)\) is an exact low-energy
source-identification kernel. Multiplicative RG preserves the rank-one
manifold but not a unique projective basin. Threshold survival requires
spectral exclusivity: an explicit positive-definite multi-channel residue has
negative triangle product. Aspect's native-quaternary and attachment gates
pass, but coupling-ray authority, scale, RG basin, threshold exclusivity,
physical16 descent, and calibrated detector gates remain open. The isolated
mediator is thus a genuine conditional sign selector, not the complete
asymmetric-portal principle.

## Unique invariant tensor authority audit: WP819

- flavor-unique-invariant-tensor-authority-audit.md
- checkers/wp819_unique_invariant_tensor_authority_audit.py
- results/wp819_unique_invariant_tensor_authority_audit.json

WP819 tests whether representation theory can select WP818's free coupling
ray. A transitive cyclic flavor action has a unique invariant line, but it is
the symmetric ray \((1,1,1)\) and gives zero component contrast. A single
transposition leaves a two-dimensional fixed space. More decisively, every
prescribed nonzero ray \(v\) can be made the unique fixed line of
\(H_v=2P_v-I\), and the target projector is recovered as
\(P_v=(H_v+I)/2\). Unique-invariant-tensor language can therefore encode any
desired answer unless the representation is derived independently.

Even after normalizing the invariant tensor, an overall coefficient \(y\)
remains. Its sign reverses the linear portal while leaving the quadratic
residue unchanged. Equivariant RG restricts evolution to a scalar beta
function without fixing its coefficients; equivariant thresholds preserve the
ray while multiplying it by an arbitrary scalar. Physical16 descent and
detector calibration remain absent. The representation is therefore a
rigidifier, not a selector, until an independent anomaly or topological
incidence fixes both its oriented ray and scalar normalization.

## Integer incidence and anomaly-inflow selector: WP820

- flavor-integer-incidence-anomaly-inflow-selector.md
- checkers/wp820_integer_incidence_anomaly_inflow_selector.py
- results/wp820_integer_incidence_anomaly_inflow_selector.json

WP820 supplies the first conditional source that fixes the asymmetric charge
ray, its orientation, and primitive lattice normalization. The rank-two
integer incidence
\(B=((2,-1,0),(3,0,-1))\) has primitive kernel
\(\pm(1,2,3)\). On that line the cubic anomaly is \(36s^3\), so an oriented
quantized inflow \(k=36\) selects \(s=1\) and hence the unit contrast
\(q_3-q_2=1\). Reversing the bulk selects the mirror. This is explicitly a
relational boundary experiment, not recovery of an absolute sign.

The physical portal remains \(e(q_3-q_2)=e\), with continuous gauge coupling
\(e\). Positive one-loop Abelian running has only the Gaussian fixed point and
retains initial data. Wess–Zumino matching protects the total anomaly across
thresholds but not the numerical mediator amplitude. A second integer
incidence selects a different primitive ray, so incidence and bulk orientation
still require independent source provenance. Physical16 descent and detector
gain calibration remain absent. The next gate is a nonzero interacting
gauge–Yukawa fixed point derived from this same chiral incidence.

## Same-incidence gauge–Yukawa fixed-point interface: WP821

- flavor-same-incidence-gauge-yukawa-fixed-point-interface.md
- checkers/wp821_same_incidence_gauge_yukawa_fixed_point_interface.py
- results/wp821_same_incidence_gauge_yukawa_fixed_point_interface.json

WP821 constructs the conditional RG completion and then tests its source
interface. The two-coupling flow
\(\beta_x=2x^2(-b+cx-dy)\),
\(\beta_y=2y(ay-fx)\) has
\(x_*=ab/(ac-df)\), \(y_*=bf/(ac-df)\). The coefficient packet
\((1,1,3,1,1)\) gives \((x_*,y_*)=(1/2,1/2)\) and exact positive infrared
stability exponents \(1/2,2\). With WP820's unit oriented charge contrast this
conditionally predicts the positive portal \(e_*=1/\sqrt2\).

The WP820 incidence does not determine those coefficients. The same charge
packet with \((1,1,1,1,1)\) has no finite fixed point, while a threshold shift
to \((1,1,4,1,1)\) moves it to \((1/3,1/3)\). The known WP805 chiral
fixed point lies in one complete action but is strongly coupled and
orientation-blind. Thus a fixed point and an oriented incidence remain valid
objects in different source frames. The successor is a finite complete-matter
census derived from the WP820 lattice, performed before any physical16 fit.

## Finite chiral matter-spectrum census: WP822

- flavor-finite-chiral-matter-spectrum-census.md
- checkers/wp822_finite_chiral_matter_spectrum_census.py
- results/wp822_finite_chiral_matter_spectrum_census.json

WP822 freezes the admitted generalized Georgi–Glashow grammar on the bounded
integer domain \(5\le N\le12,\ 1\le p\le8N\). All 544 packets are
anomaly-complete and nonsingular at the admitted fixed-flow elimination.
Exactly four have positive fixed coordinates. Two, \((6,30)\) and \((8,39)\),
keep all coordinates below one; none keeps all coordinates below \(0.1\).
Exact characteristic-polynomial root counts give one negative and three
positive stability exponents for each sub-unit survivor, so neither is a
full-dimensional infrared attractor.

The census is nonunique even on its permissive screen. More fundamentally, no
constructor maps WP820's \((B,q,k)\) incidence/inflow packet to the
\((N,p)\), representation, scalar, and Yukawa data of this grammar. Hence the
number of source-authorized WP820 completions is zero, irrespective of the two
algebraic survivors. The next source must be one quiver or chain complex that
simultaneously generates charges, matter representations, multiplicities,
hyperedges, beta coefficients, and the relevant critical-surface deformation.

## Acyclic stabilization RG-descent no-go: WP823

- flavor-acyclic-stabilization-rg-descent-no-go.md
- checkers/wp823_acyclic_stabilization_rg_descent_no_go.py
- results/wp823_acyclic_stabilization_rg_descent_no_go.json

WP823 attacks the proposed unified chain-complex source by acyclic
stabilization. The WP820 boundary \(B\) and \(B\oplus(1)\) have the same
primitive charge kernel and trivial cokernel. A physically populated unit
summand can carry the vectorlike pair \((r,-r)\), which changes neither linear
nor cubic anomaly but adds \(2r^2\) to a quadratic loop index. In the WP821
conditional flow this changes \(x_*=1/2\) to
\(x_*'=1/(2+2r^2)\); the unit pair gives \(1/4\).

Thus RG magnitude and threshold response do not descend from the full
chain-level matter complex to charge homology. Removing contractible summands
by a minimality convention also removes physical massive thresholds, so it is
not a harmless physical quotient. The first nonfaithful arrow is the passage
from full matter complex to homology/inflow. A viable unified source must be a
spectrally complete chain-level object with source-derived masses and kinetic
normalizations for every acyclic sector, followed by physical16 descent and a
calibrated threshold instrument.

## Finite spectral completion and scale-selection audit: WP824

- flavor-finite-spectral-completion-scale-selection-audit.md
- checkers/wp824_finite_spectral_completion_scale_selection_audit.py
- results/wp824_finite_spectral_completion_scale_selection_audit.json

WP824 enriches WP823's acyclic sector by
\(D_m=((0,m),(m,0))\). Its calibrated heat trace
\(2e^{-\tau m^2}\) is strictly mass-sensitive, so full spectral data repairs
the homology mass fiber. It does not select the spectrum. The normalized heat
action \(2e^{-m^2/\Lambda^2}\) has no positive finite mass extremum and is
invariant under common rescaling of \(m,\Lambda\). A polynomial action selects
\(m^2/\Lambda^2=-\alpha/(2\beta)\), moving the choice into its coefficients,
while acyclic multiplicity also remains free.

Spectral completion is therefore a faithful carrier and threshold record, not
a portal selector. The source must still derive the Dirac operator, action
coefficients, and common physical scale, and must parallelize that scale with
the gauge–Yukawa fixed point. A heat record additionally requires a calibrated
clock and detector before it can descend to physical16.

## Spectral-flow and dimensional-transmutation audit: WP825

- flavor-spectral-flow-dimensional-transmutation-audit.md
- checkers/wp825_spectral_flow_dimensional_transmutation_audit.py
- results/wp825_spectral_flow_dimensional_transmutation_audit.json

WP825 tests the proposed quantized eigenvalue and common-scale repair. For
\(H_\rho(t)=t-\rho\) on \([-1,1]\), every \(-1<\rho<1\) has spectral flow one.
In particular \(\rho=1/4\) and \(3/4\) share the same oriented index while
having different crossing locations. Index protection therefore fixes
orientation and crossing count, not a numerical eigenvalue or threshold.

For one-loop asymptotically free running,
\(\Lambda=\mu\exp[-1/(2bg(\mu)^2)]\) is exactly RG invariant, but each
\(0<\Lambda<\mu\) corresponds to a different boundary coupling. Dimensional
transmutation trades a continuous coupling for a continuous scale. Hence
\(m=\rho\Lambda\) retains independent crossing-location and boundary-condition
fibers. The next source must identify the spectral path with the RG trajectory
and derive a global condition selecting one trajectory and one physical
crossing event, which must also supply the calibrated threshold clock and
physical16 record.

## RG-spectral heteroclinic event-selection audit: WP826

- flavor-rg-spectral-heteroclinic-event-selection-audit.md
- checkers/wp826_rg_spectral_heteroclinic_event_selection_audit.py
- results/wp826_rg_spectral_heteroclinic_event_selection_audit.json

WP826 identifies the spectral path with one autonomous RG heteroclinic,
\(u_A(t)=1/(1+Ae^{-t})\), and uses the symmetric zero \(u=1/2\). Conditional
on this source vector field, the crossing has positive slope \(1/4\), fixes
dimensionless portal magnitude \(1/2\), and has the full open interval as a
monotone basin. This closes sign, normalized magnitude, spectral orientation,
and basin in one dynamics.

Global endpoint regularity leaves the autonomous translation modulus \(A\):
\(u_A(t+\delta)=u_{Ae^{-\delta}}(t)\). With \(\mu=\mu_0e^t\), the threshold is
\(\mu_*=\mu_0A\). A reference condition \(u(0)=1/2\) sets \(A=1\) only by
attaching a relational clock. Threshold-criterion shifts also move the event
without changing orientation. Thus absolute event scale, criterion authority,
physical16 descent, and detector calibration remain open. The successor must
derive a second physical anchor event and its separation from the crossing.

## Intrinsic RG curvature-anchor triplet: WP827

- flavor-intrinsic-rg-curvature-anchor-triplet.md
- checkers/wp827_intrinsic_rg_curvature_anchor_triplet.py
- results/wp827_intrinsic_rg_curvature_anchor_triplet.json

WP827 derives two anchor events from extrema of the acceleration of the same
RG vector field. For \(\dot u=\kappa u(1-u)\), the anchors occur at
\(u_\pm=(3\pm\sqrt3)/6\), symmetrically around the portal crossing \(u_0=1/2\).
Their RG-time offsets are
\(\kappa^{-1}\log(2+\sqrt3)\), independent of the WP826 translation modulus.
At \(\kappa=1\), the one-sided physical scale ratio is \(2+\sqrt3\) and the
full anchor ratio is \(7+4\sqrt3\).

This is the first source-derived relative scale prediction in the branch that
cancels both translation modulus and common reference scale. A common-gain
three-event detector would also cancel its multiplicative calibration.
However, the ratio retains the beta normalization \(\kappa\); separate event
gains destroy the readout. The complete oriented matter action must therefore
derive \(\kappa\), preserve the curvature triplet through thresholds, and
supply one common physical16 instrument. Absolute scale still requires an
independently calibrated relational anchor.

## Aspect germ tester audit: WP828

- flavor-aspect-germ-tester-audit.md
- checkers/wp828_aspect_germ_tester_audit.py
- results/wp828_aspect_germ_tester_audit.json

WP828 corrects WP827's implementation-count/native-arity conflation. The
curvature target is a ternary relation on the lower anchor, portal crossing,
and upper anchor. Its marked carrier retains one trajectory identity, beta
provenance, and a common comparison port. Full-fiber descent passes for common
translation and common detector gain, but fails for independent gains. Binary
gap factorization is valid only while both gaps retain the identical portal
record. Physical realization authority still fails: threshold survival,
`physical16` descent, ordered detector realization, and a common-calibration
instrument remain absent.

## RG curvature scheme-descent no-go: WP829

- flavor-rg-curvature-scheme-descent-no-go.md
- checkers/wp829_rg_curvature_scheme_descent_no_go.py
- results/wp829_rg_curvature_scheme_descent_no_go.json

WP829 constructs the regular monotone redefinition
\(v=u+u(1-u)/2\). It preserves the oriented logistic orbit, endpoints, RG
time, endpoint critical exponents, and the portal event, while moving both
coordinate acceleration extrema and destroying their reflection pairing. The
old anchors give nonzero values \(\pm\sqrt3/3\) in the new anchor polynomial,
and the new polynomial and its reflection have resultant 110592. Hence the
WP827 scale ratio does not descend under the admitted scheme and finite-
matching fibers. The first nonfaithful arrow is physical RG trajectory to
chosen coupling-coordinate acceleration jet. A physical running observable,
matched through thresholds and read by one calibrated instrument, must be
derived before curvature events acquire selector authority.

## Process-relative effective-charge no-go: WP830

- flavor-process-relative-effective-charge-no-go.md
- checkers/wp830_process_relative_effective_charge_no_go.py
- results/wp830_process_relative_effective_charge_no_go.json

WP830 proves that operational normalization alone does not repair WP829. The
two monotone physical records \(E_A(u)=u\) and
\(E_B(u)=u+u^2(1-u)/2\) share endpoints, tree normalization, the same RG
orbit, and endpoint critical exponents. At the same portal they read \(1/2\)
and \(9/16\), and the second channel's curvature-anchor polynomial is a
quartic with two internal roots not paired by reflection. Its resultant with
the reflected polynomial is 53084160. Thus effective-charge curvature is
process-relative. The source must derive a unique conserved-current channel
or a relation natural across the complete physical probe family; choosing an
observable after the fact is another rigidifier, not a selector.

## Primitive Ward-current threshold fiber: WP831

- flavor-primitive-ward-current-threshold-fiber.md
- checkers/wp831_primitive_ward_current_threshold_fiber.py
- results/wp831_primitive_ward_current_threshold_fiber.json

WP831 shows that WP820's one-dimensional primitive kernel and oriented inflow
do select a unique linear Ward-current channel, repairing WP830's channel
ambiguity conditionally. Its base spectral index is \(q^Tq=14\), so the
formal response \(C=14e^2\) is injective for positive \(e\) on a fixed
spectrum. The smallest anomaly-neutral vectorlike completion changes the
index to 16 without changing the current anomaly. Response continuity then
allows \(e_{\rm low}=\sqrt{8/7}e_{\rm high}\), and the packets
\((14,1)\) and \((16,\sqrt{7/8})\) share the record 14. Hence the source can
select the current channel and charge sign while failing to select magnitude,
RG basin, threshold value, or an executable physical16 readout.

## Connected-presentation acyclic-spectrum no-go: WP832

- flavor-connected-presentation-acyclic-spectrum-no-go.md
- checkers/wp832_connected_presentation_acyclic_spectrum_no_go.py
- results/wp832_connected_presentation_acyclic_spectrum_no_go.json

WP832 refutes graph connectedness as a repair of WP831. The displayed
support-connected \(3\times4\) integer matrix has no leaf row or column yet
shares the Smith form, primitive kernel \((1,2,3,0)\), anomaly 36, and trivial
cokernel of \(B\oplus(1)\). The anomaly-neutral vectorlike decoration, its
continuous mass, spectral-index shift, and the exact Ward-response fiber all
remain. Hence connectedness and permutation-level matrix indecomposability are
presentation rigidifiers. A repair requires invariant physical
irreducibility that actually excludes or fixes every anomaly-neutral sector.

## Operator-irreducible vectorlike-completion no-go: WP833

- flavor-operator-irreducible-vectorlike-completion-no-go.md
- checkers/wp833_operator_irreducible_vectorlike_completion_no_go.py
- results/wp833_operator_irreducible_vectorlike_completion_no_go.json

WP833 strengthens WP832 to a basis-invariant scalar-common-commutant test. An
irreducible three-state packet with charges \((1,2,3)\) and an irreducible
five-state packet with added anomaly-neutral charges \((1,-1)\) both have
anomaly 36 and primitive contrast one. The added states mix with the base, and
the completed mixing operator is nondegenerate, yet the current index changes
from 14 to 16. Scaling the mixing operator preserves irreducibility while
leaving a continuous spectral scale. Thus irreducibility can reject reducing
subspaces inside one packet but cannot select among distinct irreducible
physical completions.

## Minimal Ward-index neutral RG kernel: WP834

- flavor-minimal-ward-index-neutral-rg-kernel.md
- checkers/wp834_minimal_ward_index_neutral_rg_kernel.py
- results/wp834_minimal_ward_index_neutral_rg_kernel.json

WP834 tests the physical positive pairing \(S=\operatorname{Tr}Q^2\) as a
comparison principle. Minimizing it excludes every nonzero charged vectorlike
pair because the index rises by \(2r^2\). This is a genuine partial charged-
spectrum selector. An irreducible neutral completion with charges
\((1,2,3,0)\) retains index 14, anomalies, and primitive contrast. In the
declared hostile flow \(c=3+\eta^2\), the neutral direction moves the fixed
coordinate from \(1/2\) to \(1/3\) while both local stability spectra remain
positive. The first nonfaithful arrow is full RG-active spectrum to Ward-
current Gram. A complete selector needs a source-derived positive functional
faithful on neutral as well as charged active sectors.

## Ward-spectral positive-functional scale fiber: WP835

- flavor-ward-spectral-positive-functional-scale-fiber.md
- checkers/wp835_ward_spectral_positive_functional_scale_fiber.py
- results/wp835_ward_spectral_positive_functional_scale_fiber.json

WP835 adds \(\alpha\operatorname{Tr}D^2\) to the Ward pairing. At a frozen
common spectral scale it detects WP834's neutral completion: the base and
completed spectral squares are 9 and 22. Independent scaling of the completed
operator preserves irreducibility, however, and the base at scale one has the
same score as the completion at \(3/\sqrt{22}\) for every \(\alpha>0\). The
quadratic penalty has an unattained zero-scale infimum. An inverse-spectral
term selects a scale only through the new coefficient ratio
\(\lambda^4=37\beta/(352\alpha)\). Thus positivity repairs the neutral kernel
only after a charged-neutral metric and common clock have been independently
derived.

## Scale-free Ward-spectral completion selector: WP836

- flavor-scale-free-ward-spectral-completion-selector.md
- checkers/wp836_scale_free_ward_spectral_completion_selector.py
- results/wp836_scale_free_ward_spectral_completion_selector.json

WP836 replaces WP835's dimensionful spectral term by the scale-free shape
\(R_n=\operatorname{Tr}(D^TD)/\det(D^TD)^{1/n}\). AM-GM gives \(R_n\geq n\).
For the primitive base, an irreducible Householder operator saturates the
bound and gives score \(14+3\lambda\). Adding \(k\) charged vectorlike pairs
and \(\ell\) neutral states raises the score by at least
\(2\sum r_j^2+\lambda(2k+\ell)>0\) for every positive \(\lambda\). Thus the
functional genuinely and coefficient-robustly selects the minimal finite
completion and equal singular values inside the declared grammar. It remains
scale invariant and admits distinct irreducible mixing minimizers; source
authority, RG basin, matching, and instrumentation are still open.

## Primitive-current reflection Aspect-germ audit: WP837

- flavor-primitive-current-reflection-aspect-germ-audit.md
- checkers/wp837_primitive_current_reflection_aspect_germ_audit.py
- results/wp837_primitive_current_reflection_aspect_germ_audit.json

WP837 retains WP820's primitive current as an attachment port and constructs
the unique normalized Householder reflection whose negative eigenspace is the
current line. This condition removes WP836's mixing-orientation fiber and is
equivariant under simultaneous real orthogonal transport of the current and
spectral operator. Aspect's tester nevertheless prevents promotion: the
minimization has the native arity of a comparison against the whole declared
completion family; forgetting the current attachment fails the full-fiber
gate; and neither the comparison functional nor the reflection law has source
authority. The positive scale fiber \(mH_q\) survives exactly. The construction
is therefore a conditional mixing rigidifier attached to the finite-
completion selector, not yet a source-generated `physical16` selector.

## Single-constructor portal unavoidability certificate: WP838

- flavor-single-constructor-portal-unavoidability-certificate.md
- checkers/wp838_single_constructor_portal_unavoidability_certificate.py
- results/wp838_single_constructor_portal_unavoidability_certificate.json

WP838 states the exact acceptance theorem for the active objective. One
source-natural constructor must generate the oriented representation, finite
spectral action, beta system and selected basin, finite threshold map, and
calibrated labelled `physical16` realization. For the conditional coefficient
packet of WP821, the primitive unit contrast predicts the positive portal
\(1/\sqrt2\) with local stability eigenvalues \(1/2,2\). Independent exact
hostiles show why the composition is not yet authoritative: the same
incidence with \(c=4\) moves the fixed point to \(1/3\), inclusive threshold
matching erases the contrast, and inclusive detection has rank one. Aspect's
comb reference supplies a comparison frame but explicitly not source
selection. The first missing arrow is from primitive incidence plus finite
spectral data to a uniquely derived interacting action and beta coefficients.

## Spectral-action coefficient fiber transports to the portal: WP839

- flavor-spectral-action-coefficient-fiber-transports-to-portal.md
- checkers/wp839_spectral_action_coefficient_fiber.py
- results/wp839_spectral_action_coefficient_fiber.json

WP839 attacks WP838's first missing arrow. With the primitive current and
normalized reflection fixed, the polynomial spectral action is
\(S=3\alpha m^2+3\beta m^4\) and selects
\(m_*^2=-\alpha/(2\beta)\). The packets \((-2,1)\) and \((-4,1)\) have
identical upstream current, completion, mixing, and scale-free shape, but
select \(m_*^2=1,2\). Under the explicit hostile interface
\(c=2+m_*^2\), they yield fixed-point coordinates \(1/2,1/3\) and portals
\(1/\sqrt2,1/\sqrt3\). Therefore a finite spectral packet does not determine
its interacting action: the source must also derive the spectral-action
profile and normalization before its beta coefficients acquire selection
authority.

## Reciprocal spectral self-duality normalization fiber: WP840

- flavor-reciprocal-spectral-self-duality-normalization-fiber.md
- checkers/wp840_reciprocal_spectral_self_duality_normalization_fiber.py
- results/wp840_reciprocal_spectral_self_duality_normalization_fiber.json

WP840 tests spectral reciprocity as a coefficient-free repair of WP839. The
action \(R(z)=z+z^{-1}\) has a unique positive self-dual minimum and, for
\(z=m^2/L^2\), selects \(m=L\). It remains invariant under common rescaling,
so the comparison scale is not selected. Applied to a coupling coordinate
\(z=\eta x\), the same abstract reciprocity selects \(x_*=1/\eta\):
\(\eta=2,3\) give portals \(1/\sqrt2,1/\sqrt3\). Reciprocity removes a
relative coefficient only after the physical variable and its normalization
are declared. The first nonfaithful arrow is therefore the map from the
physical spectral or coupling coordinate to the normalized reciprocal
coordinate.

## Charge-diameter normalized global portal flow: WP841

- flavor-charge-diameter-normalized-global-portal-flow.md
- checkers/wp841_charge_diameter_normalized_global_portal_flow.py
- results/wp841_charge_diameter_normalized_global_portal_flow.json

WP841 closes WP840's dimensionless normalization fiber conditionally by using
the primitive charge-operator diameter \(\Delta_Q=2\). This invariant survives
weak-basis conjugation and common charge shifts; primitive integer
normalization removes rescaling. The candidate flow
\(\beta_x=\kappa x^2(1-\Delta_Qx)\) selects \(x_*=1/2\), hence the positive
unit-contrast portal \(1/\sqrt2\), and an exact Lyapunov identity proves that
the entire positive half-line is its basin. This is the first invariant
sign--magnitude--global-basin selector from the primitive current itself. It
remains a conjectured beta constructor: no microscopic action derives the
diameter coefficient. Decoupling an extremal charge changes the active
diameter from two to one and moves the selected coordinate from \(1/2\) to
\(1\), so threshold matching and calibrated labelled readout remain open.

## Charge-moment loop mismatch with diameter flow: WP842

- flavor-charge-moment-loop-mismatch-with-diameter-flow.md
- checkers/wp842_charge_moment_loop_mismatch.py
- results/wp842_charge_moment_loop_mismatch.json

WP842 tests whether the primitive charge spectrum automatically generates
WP841's beta ratio in the smallest charge-moment loop grammar. The exact
moments are \(S_2=14,S_4=98\), so the unscreened moment flow selects
\(S_2/S_4=1/7\), not \(1/\Delta_Q=1/2\). A scalar/Yukawa contribution
\(Y=70\) is required to make \(S_4-Y=\Delta_QS_2\). The same-diameter shifted
spectrum requires 295, proving that diameter alone does not reconstruct the
microscopic coefficients. After extremal threshold deletion the required
contribution becomes 84. Thus the next source object must be a unique
interaction tensor whose loop contraction and finite matching produce these
values independently of the desired portal.

## Positive tensor threshold contraction no-go: WP843

- flavor-positive-tensor-threshold-contraction-no-go.md
- checkers/wp843_positive_tensor_threshold_contraction_no_go.py
- results/wp843_positive_tensor_threshold_contraction_no_go.json

WP843 proves that WP842's required screening transition cannot come from one
fixed positive tensor by ordinary threshold restriction. Orthogonal
compression or a positive conditional expectation is Frobenius-contractive,
whereas the required contribution increases from 70 to 84. Even a full tensor
of norm squared 70 cannot restrict to norm squared 84. The smallest algebraic
repairs are a lossless squared amplification (6/5), or a new positive
threshold contribution 14. The latter equals the primitive Ward index only
numerically; this is not source authority. A viable constructor must therefore
derive a noncontractive finite matching operation or dynamically generate the
additional interaction at threshold, then realize its labelled detector
response.

## Asymmetric-charge radiative threshold splitting: WP844

- flavor-asymmetric-charge-radiative-threshold-splitting.md
- checkers/wp844_asymmetric_charge_radiative_threshold_splitting.py
- results/wp844_asymmetric_charge_radiative_threshold_splitting.json

WP844 tests whether WP836's equal singular values protect the common
three-state threshold. The covariant hostile
\(\Pi=\epsilon Q^2\) splits the squared thresholds into
\(m^2+\epsilon,m^2+4\epsilon,m^2+9\epsilon\). A shift-insensitive centered
charge square also splits them. Since (Q) has simple spectrum, its commutant
cannot mix the three charge lines; the common commutant of (Q,H_q) is scalar.
Any quadratic charge correction preserving degeneracy is constant. Protecting
the common threshold therefore requires cancellation of the full traceless
self-energy, whose squared norm is \(98\epsilon^2/3\). No admitted source
identity supplies that cancellation, so equal singular shape remains a tree-
level rigidifier rather than threshold survival.

## Holomorphic-mass wavefunction threshold splitting: WP845

- flavor-holomorphic-mass-wavefunction-threshold-splitting.md
- checkers/wp845_holomorphic_mass_wavefunction_threshold_splitting.py
- results/wp845_holomorphic_mass_wavefunction_threshold_splitting.json

WP845 tests supersymmetric holomorphy as the nonrenormalization identity
missing from WP844. A common gauge-invariant superpotential mass for three
vectorlike charge pairs can remain protected, while the allowed wavefunction
hostile (Z_i=\widetilde Z_i=e^{\kappa q_i^2t}) gives physical masses
proportional to (e^{-\kappa q_i^2t}). Their adjacent ratios are
\(e^{-3\kappa t}\) and \(e^{-5\kappa t}\). Keeping the physical thresholds
equal requires a Kähler anomalous-dimension contribution exactly canceling
\(\kappa(Q^2-14I/3)\), the same traceless operator found in WP844.
Holomorphic nonrenormalization therefore moves rather than closes the gate; an
all-order Kähler or physical-pole identity is still required.

## Equivariant-character threshold memory: WP846

- flavor-equivariant-character-threshold-memory.md
- checkers/wp846_equivariant_character_threshold_memory.py
- results/wp846_equivariant_character_threshold_memory.json

WP846 replaces failed common-mass protection by a representation-valued
threshold carrier. Ordinary linear and cubic anomalies are nonfaithful on
charge diameter: adding a vectorlike pair \(\{4,-4\}\) preserves both but
changes the diameter from two to eight. By contrast, the full character sews
exactly as \((z^2+z^3)+z=z+z^2+z^3\), restoring the ultraviolet support and
diameter two after charge one decouples. Four holonomy evaluations at
\(1,-1,i,-i\) reconstruct every coefficient on the declared support. This is
a conditional algebraic threshold repair and a finite faithful relational
probe. It requires an equivariant-index source theorem and an added
background-holonomy reference experiment; ordinary anomaly matching and the
current detector do not supply either.

## Incidence kernel is not an equivariant charge index: WP847

- flavor-incidence-kernel-is-not-an-equivariant-charge-index.md
- checkers/wp847_incidence_kernel_not_equivariant_charge_index.py
- results/wp847_incidence_kernel_not_equivariant_charge_index.json

WP847 tests whether WP820 itself sources WP846's character. It does not. The
vector \(q=(1,2,3)\) is a kernel coefficient satisfying \(Bq=0\); treating its
entries as eigenvalues of \(Q=\operatorname{diag}(1,2,3)\) would require a
target generator \(A\) with \(AB=BQ\). The necessary kernel condition fails
exactly: \(BQq=(-2,-6)\). No such \(A\) exists, and the kernel line is not
\(Q\)-stable. The current complex supplies only ordinary Euler index one, not
the character \(z+z^2+z^3\). A new independently authorized equivariant
complex is therefore required before representation-valued threshold memory
or holonomy probes become source-derived.

## Charged-spurion equivariant incidence lift: WP848

- flavor-charged-spurion-equivariant-incidence-lift.md
- checkers/wp848_charged_spurion_equivariant_incidence_lift.py
- results/wp848_charged_spurion_equivariant_incidence_lift.json

WP848 constructs the minimal typed repair of WP847 by promoting incidence
entries to spurions of weights \((-1,-2,-3)\). The lifted differential is
equivariant and has kernel
\((s_2s_3,2s_1s_3,3s_1s_2)\). Equal VEVs recover the WP820 ray, but two
projective VEV ratios remain; the hostile VEV packet \((1,2,1)\) produces the
ray \((1,1,3)\). The virtual index is \(z+z^2+z^3-2\), not WP846's positive
character, and simultaneous nonzero VEVs have trivial \(U(1)\) stabilizer.
Thus the lift repairs equivariance typing but relocates selection to a spurion
potential and changes the holonomy experiment's groupoid.

## Charge-recursive spurion alignment selector: WP849

- flavor-charge-recursive-spurion-alignment-selector.md
- checkers/wp849_charge_recursive_spurion_alignment_selector.py
- results/wp849_charge_recursive_spurion_alignment_selector.json

WP849 closes WP848's VEV-ratio fiber conditionally. The positive
charge-recursive potential enforces
\(|s_1|=v,s_2=s_1^2/v,s_3=s_1s_2/v\). Its zero locus is one (U(1)) orbit
for every positive coefficient packet; gauge fixing gives
\((s_1,s_2,s_3)=(v,v,v)\). The gauge-fixed Hessian is positive definite, and
the lifted kernel becomes \(v^2(1,2,3)\), so the projective ray is independent
of the dimensionful VEV. This is a genuine coefficient-robust alignment
selector inside the declared spurion model. The potential itself lacks
independent source authority, and the broken-group character transport, beta
law, thresholds, and physical instrument remain open.

## Aspect germ audit of the charge-recursive selector: WP850

- flavor-charge-recursive-selector-aspect-germ-audit.md
- checkers/wp850_charge_recursive_selector_aspect_germ_audit.py
- results/wp850_charge_recursive_selector_aspect_germ_audit.json

WP850 applies Aspect's germ-versus-completion distinction to WP849. The full
complex Hessian has rank five, with its unique null line exactly the
infinitesimal \(U(1)\) orbit, and the declared positive potential has one full
gauge-orbit zero fiber. Thus the chosen model passes the local-germ and
full-fiber gates. It fails source completion: the independently allowed
renormalizable invariant \(\epsilon v^2|s_2|^2\) moves the vacuum at first
order by \((-1/2,-2,-5/2)\) and changes the projective kernel ray. WP849 is
therefore a conditional selector with a nondegenerate germ, not an unavoidable
selector until a source theorem excludes or fixes every orbit-moving invariant.

## Supersymmetric recursive F-flat completion audit: WP851

- flavor-supersymmetric-recursive-f-flat-completion-audit.md
- checkers/wp851_supersymmetric_recursive_f_flat_completion_audit.py
- results/wp851_supersymmetric_recursive_f_flat_completion_audit.json

WP851 promotes the recursive alignment equations to F-term relations using
three charged driving fields. Exact supersymmetry repairs WP850's
nonholomorphic completion escape: for every positive invertible Kähler metric,
the F-term potential vanishes exactly on the same F-flat locus. However, an
exact monomial census shows that charge, \(R\)-charge, holomorphy, and
renormalizability also admit \(A_2\overline S_1S_3\), in addition to leaving
the three ratios \(b/a,d/c,f/e\) free. Turning on only this extra monomial
preserves the entire declared grammar while moving the projective kernel ray. The missing
source object is therefore a positive pairing that canonically normalizes the
graded multiplication maps in the same frame used by thresholds and readout.

## Finite-path partial-isometry normalization selector: WP852

- flavor-finite-path-partial-isometry-normalization-selector.md
- checkers/wp852_finite_path_partial_isometry_normalization_selector.py
- results/wp852_finite_path_partial_isometry_normalization_selector.json

WP852 supplies a precise candidate for WP851's missing positive pairing. On a
four-vertex charged path, every degree-one operator is a weighted shift. The
Toeplitz partial-isometry relation fixes all link magnitudes to one, while a
number-preserving diagonal unitary removes their phases, so the admitted
operator fiber is one full orbit. The cyclic descendants therefore have
canonical unit norms and multiplication coefficients, and the apparent
\(\overline S_1S_3\) channel collapses to the same charge-two descendant.
This is a genuine algebraic normalization selector conditional on the path
constructor. It does not yet establish the physical interface from that path
to flavor operators, RG transport, thresholds, or calibrated `physical16`
readout.

## Incidence does not authorize the path partial isometry: WP853

- flavor-incidence-does-not-authorize-path-partial-isometry.md
- checkers/wp853_incidence_does_not_authorize_path_partial_isometry.py
- results/wp853_incidence_does_not_authorize_path_partial_isometry.json

WP853 tests whether WP820 supplies WP852's missing physical interface. It does
not. Every positive weighted degree-one shift has the same number spectrum,
primitive charge ray, incidence, and cubic inflow, while its three singular
values remain free. The exact pair (T(1,1,1)) and (T(1,2,1)) is identical
under all current topological flavor probes but inequivalent under
number-preserving unitaries; only the first is a partial isometry. The first
nonfaithful arrow is therefore from the marked path constructor to the
incidence packet. WP852's normalization is new source data unless a microscopic
law derives (T^*T=I-P_3) or a source-calibrated `physical16` instrument
measures the discarded positive operator.

## Oriented unitary cycle boundary-compression constructor: WP854

- flavor-oriented-unitary-cycle-boundary-compression-constructor.md
- checkers/wp854_oriented_unitary_cycle_boundary_compression_constructor.py
- results/wp854_oriented_unitary_cycle_boundary_compression_constructor.json

WP854 derives WP852's partial isometry from a more primitive relational
operation. Removing one directed return channel from a lossless four-cycle
gives (C=(I-P_0)U=U(I-P_3)), hence unit surviving singular values and the
oriented boundary current (J=P_0-P_3). Reversing the cycle and port reverses
the current. The asymmetry and dimensionless normalization are therefore
unavoidable conditional on the oriented cycle and marked boundary, with the
groupoid explicitly reduced to the stabilizer of its source and sink. The
remaining physical gates are the microscopic flavor realization of this
cycle, the calibrated map from (J) to (g_n-g_m), the RG basin, marked-port
threshold intertwining, and `physical16` instrumentation.

## Boundary-current readout hierarchy: WP855

- flavor-boundary-current-readout-hierarchy.md
- checkers/wp855_boundary_current_readout_hierarchy.py
- results/wp855_boundary_current_readout_hierarchy.json

WP855 pulls WP854 through the existing charged-cycle probes. The ordinary
sum port maps both normalized boundary orientations and the absent source to
zero, so the contact, partonic, and downstream Standard Model-interference
channels cannot read the selected asymmetry. The neutral loop product retains
relative parity but identifies the two orientations. A complementary
difference port detects boundary magnitude, while intensity still loses sign.
Two coherent reference settings at that port give singleton contextual
classes on the declared orientation/absence packet. This is a new relational
experiment over the reference-phase stabilizer; no current flavor instrument
supplies the pre-projection difference channel or its calibrated reference.

## Reciprocal endpoint RG basin and threshold audit: WP856

- flavor-reciprocal-endpoint-rg-basin-threshold-audit.md
- checkers/wp856_reciprocal_endpoint_rg_basin_threshold_audit.py
- results/wp856_reciprocal_endpoint_rg_basin_threshold_audit.json

WP856 equips WP854's two marked endpoints with the unique irreducible
exchange-covariant probability generator. Its fixed point is (p_*=1/2), its
basin is the whole interval, and even a zero seed flows nonzero. Conditional
on a source-derived kinetic identification

\[
|g_n-g_m|^2=p,
\]

this selects (1/\sqrt2). The threshold audit separates stationary-weight
survival from current survival: every swap-intertwining stochastic channel
preserves (p_*), but (T_rJ=(2r-1)J). The exact hostile (r=3/4) halves the
portal current without disturbing the fixed point. Physical completion now
requires one source to derive the flavor-RG interpretation, coherent kinetic
lift, isometric marked-port threshold map, and WP855 referenced readout.

## Oriented dark-state portal attractor: WP857

- flavor-oriented-dark-state-portal-attractor.md
- checkers/wp857_oriented_dark_state_portal_attractor.py
- results/wp857_oriented_dark_state_portal_attractor.json

WP857 repairs WP856's classical-coherence gap with two Lindblad jumps pumping
the absent and symmetric sectors into the antisymmetric ray. The Liouvillian
has one stationary state, gap (\kappa/2), and a global basin containing the
absent portal. It fixes coherent relative parity and amplitudes
\((1,-1)/\sqrt2\). It does not fix global phase relative to WP855's external
reference. More importantly, an even-parity rival reservoir has the identical
spectrum and global-basin structure, so complete positivity, equal rates, and
exchange covariance do not authorize the desired odd jump. A microscopic
boundary interaction must derive that reservoir before this becomes an
explanation rather than target encoding; RG, threshold, and instrument
interfaces remain open.

## Coherent return-port dark-ray selector: WP858

- flavor-coherent-return-port-dark-ray-selector.md
- checkers/wp858_coherent_return_port_dark_ray_selector.py
- results/wp858_coherent_return_port_dark_ray_selector.json

WP858 retains WP854's removed return edge as a coherent reference port and
couples both boundary paths to one normalized rank-one junction. Its kernel is
the unique ray (d_z=(-z,1)/\sqrt2); equivalently, this is the negative
eigenray of the unit boundary-link Hamiltonian. The construction derives
WP857's parity and magnitude covariantly and can reuse the same port for
WP855's relative-sign readout. It is a new relational experiment, not recovery
of an absolute phase. Phase-shifting the junction, reversing the Hamiltonian
ordering, or using a finite-temperature bath changes the selection. Hence the
common junction, spectral ordering, pure reservoir, RG identification,
threshold isometry, and detector interface still require one microscopic
source theorem.

## Positive Kirchhoff junction selector and instrument: WP859

- flavor-positive-kirchhoff-junction-selector-instrument.md
- checkers/wp859_positive_kirchhoff_junction_selector_instrument.py
- results/wp859_positive_kirchhoff_junction_selector_instrument.json

WP859 replaces WP858's arbitrary Hamiltonian sign by the positive Gram of an
unweighted coherent Kirchhoff row. The Gram is a rank-one projector with the
normalized odd ray as its unique zero mode and the even ray at unit cost. Its
equal weights follow exactly from endpoint reciprocity plus row normalization.
canonical zero-temperature lowering dissipator has one stationary state and
gap (\kappa/2). Lossless completion of the same row forces a complementary
difference output on which the selected state has unit amplitude, thereby
joining source selection and source-level instrumentation. A weighted
junction selects unequal magnitudes, and WP856's non-isometric threshold can
preserve the ray while halving its amplitude. Microscopic equality of junction
weights, flavor-RG typing, full two-port threshold isometry, and calibrated
`physical16` realization remain open.

## Reducing-subspace threshold survival theorem: WP860

- flavor-reducing-subspace-threshold-survival-theorem.md
- checkers/wp860_reducing_subspace_threshold_survival_theorem.py
- results/wp860_reducing_subspace_threshold_survival_theorem.json

WP860 proves the exact threshold condition for WP859. In a full unitary
light/heavy block matching, the light compression obeys
(A^*A=I-C^*C); it is isometric exactly when the heavy-leakage block vanishes,
equivalently when the two-port projector is reducing. State and both detector
rows must then be transported together, preserving all relational records.
The exact three-state hostile mixes one light port with one heavy mode at
cosine (3/4): the ultraviolet map remains unitary while the light dark-vector
norm becomes (25/32) and its component ratio changes. Exact threshold
survival therefore requires a source-derived superselection projector
commuting with the complete threshold interaction algebra, not merely anomaly
matching or ambient unitarity.

## Kirchhoff dark-word physical16 interface: WP861

- flavor-kirchhoff-dark-word-physical16-interface.md
- checkers/wp861_kirchhoff_dark_word_physical16_interface.py
- results/wp861_kirchhoff_dark_word_physical16_interface.json

WP861 maps WP859's selected dark vector into WP649's oriented spin-one frame.
The return phase (z=i) gives the fixed chiral word
(F_-=(J_m-iJ_n)/\sqrt2). If this word plus a complex identity offset is the
complete Yukawa grammar in each sector, an exact nondegenerate witness has
spectral discriminants (49,316), nonzero CP invariant (6), and rank three
in ten independent weak-basis invariants. The construction is therefore a
proper conditional `physical16` selector, not a unique point. If the word is
merely added to arbitrary Yukawas, the map is an invertible translation and
selects nothing. Source authority must derive the oriented chiral interface
and grammar completeness; measured-ensemble compatibility and calibrated
instrumentation remain open.

## Kirchhoff dark-word ensemble falsifier: WP862

- flavor-kirchhoff-dark-word-ensemble-falsifier.md
- checkers/wp862_kirchhoff_dark_word_ensemble_falsifier.py
- results/wp862_kirchhoff_dark_word_ensemble_falsifier.json

WP862 applies the complete fitted-ensemble gate to WP861. Every single-sector
matrix in the proposed family obeys the exact scale-free mass-shape bound
(e_2/e_1^2\ge2/9). The WP7 central up and down values are respectively
(1.36\times10^{-5}) and (3.53\times10^{-4}). Even a conservative envelope
allowing every individual residual to reach the full
(\sqrt{20.28}\)-sigma viability radius stays below (1.76\times10^{-5}) and
(4.61\times10^{-4}). Therefore none of the 1,210 stored viable sheets lies
in the WP861 family. The complete-grammar interface closes negative, while
the additive interpretation remains an invertible nonselector. A successor
must add independently derived flavor structure without reopening arbitrary
word-coefficient fitting freedom.

## Path-polynomial Aspect-germ audit: WP863

- flavor-path-polynomial-aspect-germ-audit.md
- checkers/wp863_path_polynomial_aspect_germ_audit.py
- results/wp863_path_polynomial_aspect_germ_audit.json

WP863 tests the minimal source-closed successor (Y=aI+F+F^2) against
Aspect's marked-germ, full-fiber, native-arity, completion, and instrument
gates. The three path occurrences are independent, the polynomial transforms
covariantly under the full weak-basis groupoid, and its exact singular-value
invariants are derived. The smallest completion hostile
(Y_c=aI+F+cF^2) preserves the admitted path algebra while changing physical
invariants at first order. Thus the current source does not fix the unit
two-step coefficient: the construction is a candidate rigidifier, not an
authorized selector. A source theorem fixing the complete path functional and
a calibrated coherent three-occurrence `physical16` instrument remain open.

## Oriented-path Green operator audit: WP864

- flavor-oriented-path-green-operator-audit.md
- checkers/wp864_oriented_path_green_operator_audit.py
- results/wp864_oriented_path_green_operator_audit.json

WP864 replaces the unsupported geometric sum by an exact Green equation. If
the source kinetic operator is the normalized oriented derivative (I-F), its
unique inverse in the path algebra is (I+F+F^2), so the WP863 two-step
coefficient is forced rather than fitted. The hostile generalization
(I-\rho F-\delta F^2) has inverse
(I+\rho F+(\rho^2+\delta)F^2): locality must exclude (delta), source
normalization must fix (|\rho|=1), and a retained reference is required to
distinguish the conjugate signs. Green inversion is therefore a conditional
coefficient selector, not yet the complete end-to-end source principle. RG,
reducing-threshold, and calibrated `physical16` interfaces remain separate.

## Minimal lossless colligation source audit: WP865

- flavor-minimal-lossless-colligation-source-audit.md
- checkers/wp865_minimal_lossless_colligation_source_audit.py
- results/wp865_minimal_lossless_colligation_source_audit.json

WP865 places the dark-ray selector, global attractive channel, and
complementary bright/dark readout inside one minimal lossless Stinespring
colligation. This proves that the three interfaces can coexist in one source
object. It does not make their values unavoidable. The reciprocal phase (z)
changes the selected ray without changing the channel spectrum, while the
contraction (q) changes the basin without changing the selected ray. A full
unitary endpoint-heavy threshold rotation also remains lossless while violating
the reducing-subspace condition. Minimal dilation therefore packages a chosen
portal channel; it does not derive its sign, basin rate, threshold protection,
or detector calibration. A successor must derive the channel itself from a
microscopic flavor law.

## Dark-corner conditional expectation audit: WP866

- flavor-dark-corner-conditional-expectation-audit.md
- checkers/wp866_dark_corner_conditional_expectation_audit.py
- results/wp866_dark_corner_conditional_expectation_audit.json

WP866 strengthens WP865 by requiring the source channel to be a positive
conditional expectation onto the selected dark corner. Within the WP865
family, idempotence plus a unique stationary ray forces (q=0), eliminating
the basin modulus and yielding a normalized generator with one zero and eight
minus-one modes. The phase (z), physical RG clock, and portal-unit map remain
free. Threshold naturality also splits: dark-line invariance preserves the
selector, whereas the full bright/dark projector must reduce the threshold
algebra to preserve the complementary readout. An exact bright-heavy unitary
keeps the dark selector while attenuating the readout to (9/16). The
conditional expectation is therefore a genuine basin selector conditional on
the dark corner, but not yet the complete microscopic portal principle.

## Multiplicity-one odd boundary protection audit: WP867

- flavor-multiplicity-one-odd-boundary-protection-audit.md
- checkers/wp867_multiplicity_one_odd_boundary_protection_audit.py
- results/wp867_multiplicity_one_odd_boundary_protection_audit.json

WP867 proves that a globally multiplicity-one odd endpoint character protects
the normalized difference ray under every equivariant threshold operation.
Together with WP866, this would fix relative sign, normalized magnitude, and a
unique dimensionless basin. Ordinary anomaly matching does not derive the
multiplicity hypothesis. Adding two heavy odd carriers preserves the mod-two
anomaly class while allowing an equivariant dark-heavy rotation; the exact
cosine-(3/4) hostile leaves only (9/16) of the light dark norm. The missing
source is therefore a marked representation-valued boundary index retaining
multiplicity and detector attachment, not an ordinary anomaly class.

## Equivariant index forgets boundary attachment: WP868

- flavor-equivariant-index-forgets-boundary-attachment.md
- checkers/wp868_equivariant_index_forgets_boundary_attachment.py
- results/wp868_equivariant_index_forgets_boundary_attachment.json

WP868 proves that even a complete equivariant index and uniform spectral gap
do not retain the detector-coupled portal copy. The gapped equivariant maps
(D_0=(0,1)) and (D_*=(\sqrt7/4,3/4)) have identical source and target
characters, odd index, anomaly class, rank, and nonzero singular spectrum.
Their kernel detector Grams are (1) and (9/16). The first nonfaithful arrow
is therefore from the marked equivariant complex to its index. Exact threshold
survival requires transport of the actual kernel projector together with a
named boundary evaluation map in one calibrated frame.

## Kato kernel–detector parallel transport: WP869

- flavor-kato-kernel-detector-parallel-transport.md
- checkers/wp869_kato_kernel_detector_parallel_transport.py
- results/wp869_kato_kernel_detector_parallel_transport.json

WP869 equips WP868's gapped differential family with its canonical Kato
connection. The resulting unitary transports the actual kernel projector,
conditional expectation, and complete bright/dark detector frame. A
co-transported detector retains unit Gram where the fixed detector sees
\(9/16\). This is an exact mathematical threshold parallelization, but it
defines a new relational experiment unless the microscopic source makes the
detector coupling follow the same connection. Executable co-control and
calibrated 'physical16' units remain open.

## Ward-locked Kato detector and gain fiber: WP870

- flavor-ward-locked-kato-detector-gain-fiber.md
- checkers/wp870_ward_locked_kato_detector_gain_fiber.py
- results/wp870_ward_locked_kato_detector_gain_fiber.json

WP870 places the detector vertex in the same microscopic source action as the
Kato-matched field. The common source pullback forces the detector row to
co-transport, closing WP869's frame-attachment gap under an exact anomaly-free
Ward identity. It leaves a common coupling \(g\): \(g=1\) and \(g=2\) obey the
same Ward law and normalized geometry but give intensities \(1\) and \(4\).
Current conservation also does not fix the beta function. The Ward mechanism
is therefore a source-derived threshold intertwiner and detector rigidifier,
not a magnitude or coupling-RG selector.

## Charge-normalized reciprocal gradient selector: WP871

- flavor-charge-normalized-reciprocal-gradient-selector.md
- checkers/wp871_charge_normalized_reciprocal_gradient_selector.py
- results/wp871_charge_normalized_reciprocal_gradient_selector.json

WP871 replaces WP841's conjectured polynomial beta coefficients by the
gradient of the reciprocal source functional itself. With the primitive charge
diameter \(\Delta_Q=2\), the strictly convex action
\(\cosh(\log(\Delta_Qg^2))\) uniquely selects \(g=1/\sqrt2\), and its exact
gradient has the whole positive coupling line as basin. Combined with the odd
boundary, Kato transport, and Ward-locked detector, this is the strongest
conditional end-to-end selector yet. Source retention of the marked diameter,
physical RG typing, and calibrated 'physical16' realization remain unproved.

## Multiplicative reciprocal RG domain audit: WP872

- flavor-multiplicative-reciprocal-rg-domain-audit.md
- checkers/wp872_multiplicative_reciprocal_rg_domain_audit.py
- results/wp872_multiplicative_reciprocal_rg_domain_audit.json

WP872 corrects WP871's coupling-flow interpretation. The cosh-gradient has a
nonzero beta function at exact decoupling and is incompatible with
multiplicative Ward-coupling renormalization. The reciprocal
\(\log\cosh(\log(\Delta x))\) potential repairs this: its beta function is
\(x(1-\Delta^2x^2)/(1+\Delta^2x^2)\), remains duality covariant, selects
\(g=1/\sqrt2\) for \(\Delta=2\), and has every \(x>0\) in its basin. The exact
zero seed remains zero. Portal inevitability therefore requires an independent
source theorem excluding the decoupled cusp from the admitted physical domain.

## Primitive dual-pairing portal inevitability audit: WP873

- flavor-primitive-dual-pairing-portal-inevitability-audit.md
- checkers/wp873_primitive_dual_pairing_portal_inevitability_audit.py
- results/wp873_primitive_dual_pairing_portal_inevitability_audit.json

WP873 supplies the strongest sufficient abstract source principle found. A
primitive nondegenerate pairing \(\Delta_Qgg_D=1\) excludes zero coupling;
electric–dual self-duality then fixes \(g=g_D=1/\sqrt2\), and the WP872
log-cosh flow preserves the pairing with a global basin. Pairing preservation
alone does not protect the electric prediction: a reciprocal rescaling changes
\(g\) while preserving the product. Threshold survival therefore requires
intertwining both the pairing and duality exchange. The architecture becomes
end-to-end when joined to the odd boundary, Kato transport, and Ward detector,
but no admitted microscopic flavor dual port or calibrated 'physical16'
realization currently exists.

## Dual-pair source existence audit: WP874

- flavor-dual-pair-source-existence-audit.md
- checkers/wp874_dual_pair_source_existence_audit.py
- results/wp874_dual_pair_source_existence_audit.json

WP874 tests whether any admitted source realizes WP873. Strominger's joint
electric/magnetic theorem supplies an invertible complementary readout and
locates information loss at parity projection; it does not create a dual
flavor coupling. Monodromic \(G_2\) supplies a genuine Dirac lattice and
magnetic weights but retains the Gaussian endpoint, transmutation scale, and
Coulomb fibers. The rank-one unimodular lattice fixes an integral pairing
while leaving the positive kinetic metric free. No current source supplies the
primitive normalized dual product or calibrated 'physical16' instrument.
WP873 therefore remains an added-source architecture with a precise
microscopic reopening condition.

## Additive portal zero-exit source audit: WP875

- flavor-additive-portal-zero-exit-source-audit.md
- checkers/wp875_additive_portal_zero_exit_source_audit.py
- results/wp875_additive_portal_zero_exit_source_audit.json

WP875 separates the additively generated scalar portal from WP870's
multiplicative Ward detector gain. Messenger thresholds and the WP729
one-loop affine term can genuinely make zero portal non-invariant. The
strongest admitted simultaneous singlet–triplet completion fails earlier:
shared-field backreaction gives
\(\kappa_A=-6(4T+12g_1+53g_2)/103\), so no nonnegative point with a positive
source coordinate has all required Yukawa squares positive. Additive
generation remains the physically legitimate zero-exit mechanism, but the
current realization has an empty interacting source surface and cannot open
the magnitude, basin, threshold, or instrument gates.

## Source-compelled simultaneous portal repair closure: WP876

- flavor-source-compelled-simultaneous-portal-repair-closure.md
- checkers/wp876_source_compelled_simultaneous_portal_repair_closure.py
- results/wp876_source_compelled_simultaneous_portal_repair_closure.json

WP876 applies Aspect's kernel-descent typing to every adjacent object that
could appear to repair WP735. The WP738 link mediators are the only currently
compelled pre-quotient Lagrangian family capable of changing the beta system;
their exhaustive 256-branch calculation has zero physical fixed points.
WP744 anomaly inflow lands in the wrong operator type, WP854's return link has
no microscopic flavor-field map, and WP855 is a downstream detector port.
Consequently none supplies an authorized correction to the simultaneous
nullcline. An explicit hostile shows how an untyped coefficient can fake the
repair: at \((T,g_1,g_2)=(0,1,0)\), adding \(s=73\) changes
\(\kappa_A=-72/103\) to \(1/103\). The next source must independently force
new Yukawa-active matter and its complete interaction grammar before its
fixed-point effect is computed.

## Sequential SO(5) two-vector projector repair: WP877

- flavor-sequential-so5-two-vector-projector-repair.md
- checkers/wp877_sequential_so5_two_vector_projector_repair.py
- results/wp877_sequential_so5_two_vector_projector_repair.json

WP877 reopens a bounded simple-parent calculation without adding optional
fixed-point matter. Realizing the declared chain
\(SO(5)\to SO(4)\to SO(3)\) requires two ordered fundamental breaking
directions. A positive renormalizable sum-of-squares potential has the global
vacuum \(u=ae_5,v=be_4\), seven gauge zero modes, and exactly three positive
physical Hessian eigenvalues
\(2\lambda_u a^2,2\lambda_v b^2,\kappa(a^2+b^2)\). Retaining the two
source projectors removes WP739's continuous singlet-mixing rotation, and
source-functional mass thresholds preserve both labels. The construction is
a stable projector selector and threshold rigidifier, not a magnitude or
RG-basin selector: radial scales, couplings, mass gaps, and detector
calibration remain free. It authorizes the next exact calculation—the full
simple-parent gauge--Yukawa fixed point including both compulsory breaking
fundamentals and complete spinor/vector matter.

## Ordered singlet-plane Hodge portal normalizer: WP878

- flavor-ordered-singlet-plane-hodge-portal-normalizer.md
- checkers/wp878_ordered_singlet_plane_hodge_portal_normalizer.py
- results/wp878_ordered_singlet_plane_hodge_portal_normalizer.json

WP878 transfers Strominger's real source-Hodge theorem to WP877's ordered
singlet plane. The two source projectors define
\(J=e_ve_u^T-e_ue_v^T\). Projector diagonality, oddness under \(J\), primitive
unit normalization, and the ordered-stage sign uniquely select
\(H=P_v-P_u\), with \(H^2=P_2\) and \(JH=-HJ\). Thus the simple-parent branch
now fixes the dimensionless portal sign and unit contrast rather than merely
labelling two singlets. Grothendieck's moving-incidence result requires this
packet to co-move with its source connection; Sontag's disturbance theorem
requires two independently excited detector directions; Aspect's path audit
denies execution authority to generic rotations that leave the prepared
projector stabilizer. The common coefficient in \(G=gH\) remains free, so the
full simple-parent fixed point, global basin, finite threshold matching, and
calibrated rank-two `physical16` instrument remain the active gates.

## Spin(5) anomaly-completion beta fiber: WP879

- flavor-spin5-anomaly-completion-beta-fiber.md
- checkers/wp879_spin5_anomaly_completion_beta_fiber.py
- results/wp879_spin5_anomaly_completion_beta_fiber.json

WP879 tests whether the simple parent authorizes one complete beta system.
It does not. Per family, both the conjugate packet
\(4_{+1/2}\oplus5_{-1}\) and the chiral packet
\(4_{-3/2}\oplus1_0\oplus1_{+1}\oplus1_{+2}\) cancel the same mixed
Spin(5)-hypercharge, gravitational-hypercharge, cubic-hypercharge, and
fundamental-spinor parity obstructions of the portal packet. Their
three-family Spin(5) fermion indices differ by three. Including the WP877
breaking fundamentals and the spinor Higgs gives exact one-loop coefficients
\(b_0^A=9/2\) and \(b_0^B=13/2\). Thus the admitted anomaly probe collapses
two source spectra that the RG probe separates by \(2\). Both branches are
asymptotically free at one loop, so anomaly cancellation neither fixes the
common portal coupling nor supplies one ultraviolet interacting normalization.
A parent representation, zero-mode index, or locality theorem must select the
matter packet before a full fixed-point calculation has source authority.

## Spin(5) model audit against Aspect's six-rung tester: WP880

- flavor-spin5-model-aspect-six-rung-audit.md
- checkers/wp880_spin5_model_aspect_six_rung_audit.py
- results/wp880_spin5_model_aspect_six_rung_audit.json

WP880 applies Aspect's full tester rather than only its marked-germ gate. The
WP877--WP879 source checkers contribute 38 exact gates and detect six
directions in a frozen twelve-direction hostile carrier. Their observation
map has rank six and a six-dimensional kernel: common gain, moving-frame
transport, mass scale, detector rank, selected-port transmission zeros, and
end-to-end coherence remain unresolved. Six algebraic dual rows would close
that declared formal kernel, but Aspect's governance gate rejects or defers
all six until their source constructors and operational witnesses exist. No
acquisition-authoritative flavor candidate currently has event rates, setting
cells, detector resolution, or an executable source-excitation contract, so
the rung-six portfolio is correctly empty. The model is therefore deferred:
its bounded source geometry passes, while the full physical tester does not
close. The smallest surviving hostile changes \(g=1\) to \(g=2\) without
changing any current source observation and multiplies portal intensity by
four.

## Common-gain absolute-rate gate: WP881

- flavor-common-gain-absolute-rate-gate.md
- checkers/wp881_common_gain_absolute_rate_gate.py
- results/wp881_common_gain_absolute_rate_gate.json

WP881 attacks WP880's smallest surviving hostile. For factorized amplitudes
\(A_i=g a_i\), every normalized flavor fraction is exactly independent of the
common gain. An absolute count has nonzero gain response, but an unknown
luminosity or source-current normalization supplies the exact symmetry
\((g,\mathcal L)\mapsto(cg,\mathcal L/c^2)\). One count therefore has rank
one on \((\log g,\log\mathcal L)\); adding an independent normalization
monitor raises the formal response rank to two. Pure rates still identify
only \(|g|\), not its sign. The algebraic gain row is consequently deferred
until a completion-specific production and decay channel, luminosity,
efficiency, background-normal, and—if sign is claimed—interference-reference
contracts exist. More precise normalized flavor measurements cannot repair
this kernel.

## Ordered Hodge co-moving connection: WP882

- flavor-ordered-hodge-comoving-connection.md
- checkers/wp882_ordered_hodge_comoving_connection.py
- results/wp882_ordered_hodge_comoving_connection.json

WP882 attacks WP880's moving-frame kernel. A differentiable ordered-projector
history supplies the exact connection
\(\Omega=\dot R R^T=\dot\theta J\), obeying
\(\dot H=[\Omega,H]\), with
\(\dot\theta=\operatorname{tr}(JH\dot H)/4\). The inhomogeneous rule
\(\Omega'=U\Omega U^{-1}+\dot U U^{-1}\) makes the covariant derivative
descend under moving weak bases. Freezing \(\Omega=0\) does not descend.
Scalar RG data retain only the constant spectrum of \(H\) and cannot recover
the projector germ. For \(G=gH\), covariant transport leaves
\(D_tG=\dot gH\), so the construction removes spurious chart motion but does
not fix the beta function, common magnitude, completion, thresholds, or
instrument. It is therefore a source-authorized rigidifier on smooth ordered
histories, not a selector; threshold jumps still require a separately derived
matching intertwiner.

## Threshold Hodge intertwiner fiber: WP883

- flavor-threshold-hodge-intertwiner-fiber.md
- checkers/wp883_threshold_hodge_intertwiner_fiber.py
- results/wp883_threshold_hodge_intertwiner_fiber.json

WP883 crosses WP882's sharp-threshold boundary algebraically. Intertwining
the ordered pair \((H,J)\) fixes the orthogonal matching as
\(M=\sigma R_+R_-^T\) with \(\sigma=\pm1\); retaining only \(H\) leaves four
sign choices. The two Hodge-compatible lifts have identical conjugation
action, so their sign is invisible on the original projector/`physical16`
quotient. A coherent reference path would define a new relational experiment.
For \(G=gH\), the threshold law additionally contains the continuous jump
\(\eta=g_+/g_-\), which the Hodge geometry does not select. Thus the ordered
pair rigidifies adjoint matching but a completion-specific finite threshold
action is still required to determine portal strength.

## Spin(5) finite-threshold selector obstruction: WP884

- flavor-spin5-finite-threshold-selector-obstruction.md
- checkers/wp884_spin5_finite_threshold_selector_obstruction.py
- results/wp884_spin5_finite_threshold_selector_obstruction.json

WP884 tests whether choosing either WP879 anomaly-free completion fixes
WP883's portal jump. A completion can fix a logarithmic coefficient, but the
matching family still contains a free threshold mass and finite term:
\(\eta_C=1+\alpha_C\log(M_C/\mu)+k_C\). The local source constraint has rank
one on the three coordinates \((\eta,\log(M_C/\mu),k_C)\), leaving a
two-dimensional solution fiber. The conventional choice (M_C=\mu,k_C=0)
returns \(\eta=1\) but is not a source selection. Aspect's transverse-balance
gate makes the categorical obstruction explicit: added detector rows may
identify the realized jump but cannot provide the missing source equations.
The branch therefore closes negative until one completion supplies both a
mass action and a scheme-independent full-amplitude matching condition.

## Spin(5) completion bare-massability audit: WP885

- flavor-spin5-completion-bare-massability-audit.md
- checkers/wp885_spin5_completion_bare_massability_audit.py
- results/wp885_spin5_completion_bare_massability_audit.json

WP885 audits the smallest completion-specific mass action without inventing
new scalars. Completion A pairs (4_{-1/2}) with (4_{+1/2}) and (5_{+1})
with (5_{-1}), admitting two independent gauge-invariant bare masses per
family. Their values remain free, so immediate massability does not select a
threshold. Completion B has no charged representation-matched pair with
opposite hypercharge; its neutral singlet Majorana candidate does not repair
the charged-sector rank. That branch requires an explicit scalar/Yukawa
constructor. The result is a split negative: A defines thresholds with free
scales, while B does not yet define the charged threshold spectrum. Neither
completion supplies a numerical selector.

## Declared-scalar Spin(5) Yukawa census: WP886

- flavor-spin5-declared-scalar-yukawa-census.md
- checkers/wp886_spin5_declared_scalar_yukawa_census.py
- results/wp886_spin5_declared_scalar_yukawa_census.json

WP886 recovers the complex spinor-Higgs charge from the already-declared
portal invariant as \(\Phi=4_{-1/2}\). Using only \(\Phi,\Phi^*\) and the two
real (5_0) breakers, the exact representation/hypercharge census finds six
distinct-field Yukawa edges for Completion B. Every multiplet is incident, so
the absence of charged bare masses does not imply a representation-level
isolate. This is only a typing result: the incidence graph forgets
Clebsch--Gordan symmetry, vacuum direction, correlated matrix entries, and
family structure. The all-zero Yukawa assignment is the smallest hostile.
The next gate is an explicit Spin(5) gamma-intertwiner component mass matrix
on the declared vacuum and its symbolic generic rank.

## Completion-B component mass rank: WP887

- flavor-spin5-completion-b-component-mass-rank.md
- checkers/wp887_spin5_completion_b_component_mass_rank.py
- results/wp887_spin5_completion_b_component_mass_rank.json

WP887 constructs an exact \(4\times4\) Euclidean Spin(5) Clifford system, its
antisymmetric invariant form (C), the pseudoreal conjugate
\(\widetilde\phi=C\phi^*\), and the full one-family \(16\times16\) mass matrix
from WP886's six allowed couplings. At the integer witness
\(\phi=(1,2,3,5)^T\) and Yukawas \((2,3,5,7,11,13)\), the determinant is
the nonzero integer (468887390507036217600\), proving generic full rank on a
nonempty Zariski-open parameter set. Completion B is therefore fully massable
with the already-declared spinor Higgs. The result repairs threshold
definition but not selection: Yukawas and the Higgs vacuum remain free, and
the all-zero Yukawa locus has rank zero.

## Completion-B Yukawa fiber quotient: WP888

- flavor-spin5-completion-b-yukawa-fiber-quotient.md
- checkers/wp888_spin5_completion_b_yukawa_fiber_quotient.py
- results/wp888_spin5_completion_b_yukawa_fiber_quotient.json

WP888 follows Aspect's topology gate. On the WP887 vacuum slice, the symbolic
determinant factors as
\(85632148167696y_1^4y_2^4y_3^2y_6^2(y_1y_5-y_2y_4)^2\). The last component
is a coherent four-edge cancellation invisible to incidence coverage. The
connected six-edge Yukawa graph has cycle rank one; modulo admitted unitary
fermion rephasings, the nonzero fiber retains six magnitudes and the cycle
phase of \(\rho=y_1y_5/(y_2y_4)\), with a one-dimensional alternating-phase
stabilizer. Two exact full-rank witnesses differing only in \(y_3\) have
different scale-free spectral shapes, so generic massability forces no
universal mass ratio. Monodromy remains open pending explicit singular-vector
continuation around \(\rho=1\).

## Coherent-divisor monodromy: WP889

- flavor-spin5-coherent-divisor-monodromy.md
- checkers/wp889_spin5_coherent_divisor_monodromy.py
- results/wp889_spin5_coherent_divisor_monodromy.json

WP889 factors the Completion-B mass matrix into one \(8\times8\) bipartite
block \(K\). Its determinant contains the coherent factor only once. At an
exact generic point on \(y_1y_5-y_2y_4=0\), \(K\) has rank seven and a
nonzero transverse left--right kernel pairing. The full zero sector is
therefore locally the single Dirac cell
\(\begin{psmallmatrix}0&ct\\ct&0\end{psmallmatrix}\). Its signed branches and
projectors have trivial monodromy and share one comparison frame. A Takagi
amplitude frame acquires only a common central minus sign after one loop;
projector and quadratic mass readouts erase it. Thus the generic physical
architecture is additive, while observing the lift requires a new coherent
reference experiment. Higher-corank divisor intersections remain separate
open strata.

## Coordinate-divisor intersection strata: WP890

- flavor-spin5-coordinate-divisor-intersection-strata.md
- checkers/wp890_spin5_coordinate_divisor_intersection_strata.py
- results/wp890_spin5_coordinate_divisor_intersection_strata.json

WP890 classifies all sixteen intersections of the four coordinate divisors
\(y_1,y_2,y_3,y_6=0\) on the frozen Completion-B vacuum slice. Single-port
coranks of the \(8\times8\) block are \(2,2,1,1\). They add at every
intersection except those containing both \(y_1=y_2=0\), which automatically
lie on the coherent divisor and acquire one additional kernel dimension. The
total kernel projector remains canonical, but its splitting into named branch
frames is not canonical at corank greater than one. Static restriction and
dynamic transport therefore become distinct arrows on a higher-rank kernel
bundle; a branch-resolved reference cell would require new source-derived
splitting data rather than following from the rank table.

## Aspect retest after threshold repairs: WP891

- flavor-spin5-aspect-retest-after-threshold-repairs.md
- checkers/wp891_spin5_aspect_retest_after_threshold_repairs.py
- results/wp891_spin5_aspect_retest_after_threshold_repairs.json

WP891 reruns the architectural audit after WP881--WP890's 105 exact gates.
Only the smooth moving-frame hostile becomes a new separated source direction:
the declared twelve-coordinate source map rises from rank six to seven and
its kernel falls from six to five. Common gain, numerical mass/threshold
value, detector rank, transmission-zero classification, and end-to-end
coherence remain unresolved. Both completions now have executable mass
constructors and the source packet-zero topology is known, but neither result
adds a numerical selector or acquisition-authoritative detector row. Aspect's
classification therefore remains deferred and the experimental portfolio
remains empty.

## Source-calibrated acquisition contract: WP892

- flavor-source-calibrated-acquisition-contract.md
- checkers/wp892_source_calibrated_acquisition_contract.py
- results/wp892_source_calibrated_acquisition_contract.json

WP892 freezes the smallest acquisition contract capable of attacking common
gain and packet-versus-transmission zero classification together. It requires
two source-derived perturbation controls, an independently calibrated absolute
monitor, signal and complementary outputs, background-normal counts,
efficiency, mass/width resolution, raw null trials, covariance, and common
source/detector frame provenance. The exact gate is
\(\operatorname{rank}J_{\rm det}=2\) with positive calibrated Gram determinant
and a positive uncertainty lower bound. Current source support admits only the
transport capability and no acquisition capability or event cell. The
candidate is therefore exactly specified but `not_schedulable`; the portfolio
remains empty and no formal response row is promoted.

## Spin(5) radial dimuon instrument adapter: WP893

- flavor-spin5-radial-dimuon-instrument-adapter.md
- checkers/wp893_spin5_radial_dimuon_instrument_adapter.py
- results/wp893_spin5_radial_dimuon_instrument_adapter.json

WP893 recovers the missing current-source interface from the two WP877
breaking fields themselves. The renormalizable invariants
\(\chi_u(u\cdot u)H^\dagger H\) and
\(\chi_v(v\cdot v)H^\dagger H\) mix the two ordered radial modes with the
Standard Model Higgs, with effective WP243 couplings
\(\kappa_A=2\chi_u a\) and \(\kappa_D=2\chi_v b\). On the frozen WP243
two-pole, small-mixing, no-exotic-decay slice, the existing checksum-pinned
CMS templates and official absolute rate calibration give a rank-two map on
\(((\chi_u a)^2,(\chi_v b)^2)\). This is a conditional calibrated instrument
for the Spin(5) source, not a selector. WP245 still rejects finite-2016 power.
WP251--WP254 already provide a higher-rate finite-grid tau instrument, but
WP258--WP259 show that its actual-pole Spin(5) adapter lacks same-frame pole
samples, physical branching normalization, QCD control, and uncertainties.

## Spin(5) tau actual-pole transfer audit: WP894

- flavor-spin5-tau-actual-pole-transfer-audit.md
- checkers/wp894_spin5_tau_actual_pole_transfer_audit.py
- results/wp894_spin5_tau_actual_pole_transfer_audit.json

WP894 tests whether WP893's source-derived radial portal repairs the separate
tau actual-pole branch. It supplies the frozen pole labels and physical
Higgs-mediated branching semantics, but not six detector-transfer fields:
actual-pole tau topology, common era/reconstruction, selection at the poles,
QCD control, weighted completion, and correlated uncertainty transport. The
best preregistered scale-covariant morph retains exact total-variation residual
\(12641608/354073635\), with a nonzero first-bin witness. Therefore the
conditional dimuon instrument and finite-grid tau discriminator coexist, but
no Spin(5) actual-pole tau adapter or flavor selector follows.

## Direct-pole Spin(5) tau acquisition contract: WP895

- flavor-spin5-direct-pole-tau-acquisition-contract.md
- checkers/wp895_spin5_direct_pole_tau_acquisition_contract.py
- results/wp895_spin5_direct_pole_tau_acquisition_contract.json

WP895 replaces unauthorized interpolation with the smallest direct acquisition
specification. The official CMS 2015 tau family has no samples at either
Spin(5) pole; the nearest substitutions miss by exactly 3.774002075 and
8.712997437 GeV. The published 140 GeV record exposes the validated generator,
GEN-SIM, pile-up HLT/RECO, and MiniAOD chain. WP895 therefore freezes two new
self-consistent source cards and requires replay through that entire chain,
unchanged WP251/WP253 selection, weighted QCD/background completion, and an
uncertainty-stable rank-two Gram gate. It is executable as an acquisition
contract but has not been executed and grants no selector or identification
authority.

## CMSSW pairing executability audit: WP903

- flavor-spin5-cmssw-pairing-executability-audit.md
- checkers/wp903_spin5_cmssw_pairing_executability_audit.py
- results/wp903_spin5_cmssw_pairing_executability_audit.json

WP903 separates same seed, restored module engine state, and semantic
source-level coupling. CMSSW supplies engine-state replay infrastructure, but
the current record contains no cross-width latent coupling, generator
draw-trace certificate, full-chain paired execution, null-completed records,
or calibrated acceptance floor. One width-dependent branch that changes later
random-draw meaning is the smallest exact falsifier. WP902 therefore remains
conditional, and WP901 is the executable-design fallback until a typed
base-event coupling and replay manifest are implemented and verified.

## Semantic random-field coupling: WP904

- flavor-spin5-semantic-random-field-coupling.md
- checkers/wp904_spin5_semantic_random_field_coupling.py
- results/wp904_spin5_semantic_random_field_coupling.json

WP904 replaces sequential common seeds by a counter-style random field keyed
by seed family, pair identifier, stage, semantic address, and local index. Its
executable hostile verifies bit-identical replay and proves that inserting a
width-dependent branch draw cannot shift any registered downstream draw. This
closes WP903's defect at reference-constructor level, but not in CMSSW: every
stochastic module still needs a semantic-address adapter or immutable typed
base event, followed by null-completed execution and acceptance calibration.

## Coupling minimality correction: WP905

- flavor-spin5-coupling-minimality-correction.md
- checkers/wp905_spin5_coupling_minimality_correction.py
- results/wp905_spin5_coupling_minimality_correction.json

WP905 repairs WP903's overly strong falsifier. Any reproducible shared-seed
joint law with the correct arm marginals is a valid coupling, even if changed
control flow destroys semantic draw alignment. Exact enumeration of all 256
pairs of binary maps on a four-atom seed space verifies
(d_{\rm TV}\leq\Pr(X\ne Y)) without an alignment premise. Semantic addressing
is sufficient for auditability and likely variance reduction, not necessary
for validity. The remaining gates are independent marginal validation,
manifest replay, null retention, and an achieved disagreement rate compatible
with the planned budget.

## Finite-discordance certificate: WP906

- flavor-spin5-finite-discordance-certificate.md
- checkers/wp906_spin5_finite_discordance_certificate.py
- results/wp906_spin5_finite_discordance_certificate.json

WP906 replaces WP902's brittle zero-only rule by an exact fixed-count
binomial test for a small registered discordance count. It computes minimum
per-pole budgets using integer arithmetic and verifies that every minimum
passes while one fewer pair fails. Validity, replay, null retention,
independence, and acceptance calibration remain separate gates. Outcome-driven
budget changes are prohibited unless an anytime-valid or error-controlled
escalation rule is frozen in advance.

## Error-controlled discordance escalation: WP907

- flavor-spin5-error-controlled-escalation.md
- checkers/wp907_spin5_error_controlled_escalation.py
- results/wp907_spin5_error_controlled_escalation.json

WP907 freezes four cumulative looks with discordance caps zero through three
and spends exact error (1/160) at each look. The union bound gives per-pole
error at most (1/40) and two-pole error at most (1/20), without assuming
independence between looks. Each generated look count is an exact integer-tail
minimum. An extra look or acceptance above the registered boundary is the
smallest protocol falsifier.

## Pair-independence hostile: WP908

- flavor-spin5-pair-independence-hostile.md
- checkers/wp908_spin5_pair_independence_hostile.py
- results/wp908_spin5_pair_independence_hostile.json

WP908 proves that replay, stable addressing, and correct one-event marginals
do not imply iid pairs. One run-level Bernoulli bit copied to every event gives
the target discordance marginal but a rank-one covariance matrix and
zero-discordance probability (1-p_0), far above WP907's first-look error
allocation. A declared entropy or randomized-key acquisition contract is
therefore required; empirical dependence diagnostics remain falsifiers, not
proofs of independence.

## Cross-sector independence transfer: WP909

- flavor-spin5-cross-sector-independence-transfer.md
- checkers/wp909_spin5_cross_sector_independence_transfer.py
- results/wp909_spin5_cross_sector_independence_transfer.json

WP909 transfers Sontag's joint-failure carrier, Strominger's higher-arity
obstruction, Nima's mixed source corner, Aspect's hidden channel transport,
and Benincasa's normalization gate into the paired flavor experiment. Its
five-bit even-parity hostile matches every four-bit deletion marginal while
remaining globally non-iid. The current finite diagnostic family can falsify
specific dependence but cannot certify a product law; a full joint carrier
and calibrated event-key acquisition theorem remain necessary.

## Conditional product-law gate: WP910

- flavor-spin5-conditional-product-law.md
- checkers/wp910_spin5_conditional_product_law.py
- results/wp910_spin5_conditional_product_law.json

WP910 gives the minimal constructive factorization: a frozen run state,
independent event keys, and an event-local transform imply conditional iid
discordances. A forgotten binary run nuisance with conditional rates
(p_0\pm p_0/2) preserves every event marginal but creates positive pair
covariance and breaks WP907's first-look error allocation. Run labels must be
retained and strata tested separately unless a source theorem makes the rate
constant across the admitted nuisance domain.

## Two-stratum discordance escalation: WP911

- flavor-spin5-two-stratum-escalation.md
- checkers/wp911_spin5_two_stratum_escalation.py
- results/wp911_spin5_two_stratum_escalation.json

WP911 repairs WP910 conservatively by retaining two run-state labels and
certifying each stratum-pole cell separately. Four looks per cell each spend
(1/320), preserving (1/40) per pole and (1/20) across two poles and two
strata. If every retained stratum obeys the target, every declared mixture
does too. A hidden stratum, pooled count, or uncalibrated partition falsifies
the contract.

## Event-locality tester: WP912

- flavor-spin5-event-locality-tester.md
- checkers/wp912_spin5_event_locality_tester.py
- results/wp912_spin5_event_locality_tester.json

WP912 turns event locality into a pair-ID-joined permutation, batching, and
restart challenge. A 64-event reference transform agrees under sixteen
schedules, while a deterministic mutable-counter hostile is replayable in one
schedule but fails both reversal and batch restart. Passing finite challenges
falsifies tested cross-event state; it does not prove universal locality or
instantiate independent event-key acquisition.

## Bell-randomness reference port: WP913

- flavor-spin5-bell-randomness-reference-port.md
- checkers/wp913_spin5_bell_randomness_reference_port.py
- results/wp913_spin5_bell_randomness_reference_port.json

WP913 proposes the missing source-calibrated acquisition as a new relational
experiment: loophole-free Bell randomness expansion, quantum-proof extraction,
and immutable allocation of disjoint 256-bit event keys. A global extracted
string within soundness error of uniform transports to an approximately
product event law under deterministic partition and event-local processing.
The checker reserves (10^{-10}) of total error for the randomness port and
recomputes the exact stratified look sizes. No fresh Bell run or CMS integration
is claimed; the reference port explicitly changes the physical groupoid.

## Bell setting-seed hostile: WP914

- flavor-spin5-bell-setting-seed-hostile.md
- checkers/wp914_spin5_bell_setting_seed_hostile.py
- results/wp914_spin5_bell_setting_seed_hostile.json

WP914 attacks WP913's upstream seed premise. With measurement-independent
settings, exact enumeration gives the deterministic local CHSH maximum
(3/4). If both devices' hidden state contains the future setting pair, a
deterministic strategy wins every trial while settings remain marginally
uniform and conditional output entropy is zero. The Bell port therefore needs
an independently prepared, causally isolated setting source or a separately
typed randomness-amplification/multiple-source theorem.

## One-honest-source setting combiner: WP915

- flavor-spin5-one-honest-source-combiner.md
- checkers/wp915_spin5_one_honest_source_combiner.py
- results/wp915_spin5_one_honest_source_combiner.json

WP915 weakens WP914's single-source trust through a commit-then-reveal XOR
port. XOR is exactly uniform if at least one bound contribution is uniform and
independent of the devices and other contributions. The exact hostile has two
marginally uniform but identical bits, whose XOR is constantly zero; an
adaptive source can cancel in the same way. The combiner therefore supplies
disjunctive trust, not assumption-free randomness, and explicitly adds a new
multi-source relational groupoid.

## Spin(5) response-branch disposition: WP916

- flavor-spin5-response-branch-disposition.md
- checkers/wp916_spin5_response_branch_disposition.py
- results/wp916_spin5_response_branch_disposition.json

WP916 reconnects the zero-drift programme to the flavor-selector objective.
The chain validates conditional detector response over a free two-coordinate
Spin(5) source family; even perfect randomization and execution provide no
source-to-`physical16` selecting arrow. An exact four-card grid has full image
under response admissibility, hence zero selection reduction. The branch
closes as neither selector nor rigidifier. The successor returns upstream to
independent derivation or falsification of an invariant source portal such as
WP360.

## Spin(5) Jarlskog-portal source-support audit: WP917

- flavor-spin5-jarlskog-portal-source-support-audit.md
- checkers/wp917_spin5_jarlskog_portal_source_support_audit.py
- results/wp917_spin5_jarlskog_portal_source_support_audit.json

WP917 returns upstream and proves that the declared Spin(5) grammar does not
generate WP360's normalized Jarlskog portal. Present source scalars are
J-blind, while the proposed portal has nonzero J derivative. The nearest
weak-basis polynomial, the squared commutator determinant, scales with the
mass discriminants and is not normalized J squared. The branch therefore
closes negative at current source support: WP360 is a conditional appended
selector, neither a derived selector nor a rigidifier of the declared Spin(5)
action. The next admissible step must derive a common source-to-Yukawa
operator and its discriminant normalization independently of fitted
physical16 data.

## Deutschian CP reference-standard trichotomy: WP918

- flavor-deutschian-cp-reference-standard-trichotomy.md
- checkers/wp918_deutschian_cp_reference_standard_trichotomy.py
- results/wp918_deutschian_cp_reference_standard_trichotomy.json

WP918 separates the kinematic and dynamical parts of normalized CP. Common
scaling uniquely forces the squared up/down discriminant product in the
denominator of the commutator-determinant invariant. But a common clock leaves
spectral shape free: the exact spectra `(0,1,2)` and `(0,1/2,2)` share clock
two while their cubic discriminants are two and three-halves. Spectral
completion records this distinction without selecting it. Only a source-
derived isolated attractive fixed ray for the full Yukawa spectral-shape block
could fix the reference standard; no such Spin(5) beta system is declared.

## Spin(5) spectral-shape beta definability audit: WP919

- flavor-spin5-spectral-shape-beta-definability-audit.md
- checkers/wp919_spin5_spectral_shape_beta_definability_audit.py
- results/wp919_spin5_spectral_shape_beta_definability_audit.json

WP919 proves that the WP918 stability block cannot yet be computed from the
declared Spin(5) source. Its largest authorized flow record is the pair of
one-loop gauge coefficients, whose Jacobian along four physical Yukawa-shape
directions has rank zero. Two full-rank WP888 mass points have different
normalized spectra while sharing Completion B's gauge coefficient. This is a
definability obstruction, not evidence that an undeclared physical beta system
has four zero modes. The next constructor must independently select a
completion and declare the complete three-family renormalizable interaction
grammar before coupled beta functions are derived.

## Spin(5) completion rank-index selector gate: WP920

- flavor-spin5-completion-rank-index-selector-gate.md
- checkers/wp920_spin5_completion_rank_index_selector_gate.py
- results/wp920_spin5_completion_rank_index_selector_gate.json

WP920 transfers the rank-index kernel theorem to the Spin(5) completion
fiber. Completions A and B collide on local anomaly cancellation and global
spinor parity. Their extended representation dimension and Dynkin-index
records separate them exactly, but separation does not select a prepared
packet; selection reduction remains zero. Minimality, massability, or favorable
running cannot be promoted after inspecting downstream behavior. A parent
branching rule, endpoint-resolved rank-index class, or locality theorem must
generate a singleton completion before its beta functions acquire authority.

## Spin(7) parent branching singleton audit: WP921

- flavor-spin7-parent-branching-singleton-audit.md
- checkers/wp921_spin7_parent_branching_singleton_audit.py
- results/wp921_spin7_parent_branching_singleton_audit.json

WP921 tests the smallest natural simple parent
`Spin(7) -> Spin(5) x Spin(2)`. Charge-pair closure of complete Spin(7)
representations excludes the exact chiral Completion-B packet. Completion A
has the compatible charged pattern, but its smallest fundamental carrier
`8+21` also forces neutral `10_0+1_0`, giving dimension 29 rather than 18.
The parent therefore narrows the completion fiber without producing a
singleton exact image. A source-derived projection or localization index must
remove the neutral surplus before A and its beta system acquire authority.

## Spin(7) orbifold zero-mode projection fiber: WP922

- flavor-spin7-orbifold-zero-mode-projection-fiber.md
- checkers/wp922_spin7_orbifold_zero_mode_projection_fiber.py
- results/wp922_spin7_orbifold_zero_mode_projection_fiber.json

WP922 constructs the exact Completion-A zero-mode packet from two bulk matter
spinors `8_a,8_b` and one matter adjoint `21`. Opposite spinor intrinsic
parities retain `4_+1/2` and `4_-1/2`; negative adjoint parity retains
`5_+1+5_-1` while removing the forced neutral `10_0+1_0`. But only two of
eight intrinsic-parity assignments yield the target, and those two are the
exchange orbit of the labelled spinors. The projection is therefore an exact
conditional field-content rigidifier, not a source-derived selector. Boundary
topology or an endpoint index must fix the parities and surviving Yukawa
grammar independently.

## Spin(7) projected Yukawa-coefficient fiber: WP923

- flavor-spin7-projected-yukawa-coefficient-fiber.md
- checkers/wp923_spin7_projected_yukawa_coefficient_fiber.py
- results/wp923_spin7_projected_yukawa_coefficient_fiber.json

WP923 enumerates the renormalizable zero-mode invariants after the exact A
projection. The two conjugate-charge channels are separately gauge allowed,
but the labelled parent spinors and their opposite intrinsic parities do not
relate the coefficients. The zero-mode census has rank zero on the two
coefficient magnitudes; `(1,1)` and `(1,2)` are the smallest hostile ratio
pair. Bulk versus boundary locality remains undeclared. An independently
motivated exchange-reflection symmetry would be needed to relate the channels
before any spectral-shape beta block is source-authorized.

## Spin(7) exchange-reflection Yukawa gate: WP924

- flavor-spin7-exchange-reflection-yukawa-gate.md
- checkers/wp924_spin7_exchange_reflection_yukawa_gate.py
- results/wp924_spin7_exchange_reflection_yukawa_gate.json

WP924 proves a conditional positive result. Exchanging the two parent spinors,
reversing Spin(2) charge, and reflecting the interval acts as
`(y_minus,y_plus) -> (conj(y_plus),conj(y_minus))`. Its fixed locus has real
codimension two and enforces equal magnitudes, removing WP923's ratio fiber.
The common coefficient and all family shape remain free. An endpoint-
asymmetric counterterm immediately restores ratio two, so the exchange must be
derived for the complete bulk, brane, regulator, and anomaly-inflow action
before selector authority is granted.

## Spin(7) exchange-fixed family-tensor fiber: WP925

- flavor-spin7-exchange-fixed-family-tensor-fiber.md
- checkers/wp925_spin7_exchange_fixed_family_tensor_fiber.py
- results/wp925_spin7_exchange_fixed_family_tensor_fiber.json

WP925 promotes the WP924 coefficient pair to complex three-family tensors.
Exchange-conjugation reduces 36 real coordinates to the 18-real-dimensional
fixed locus `Y_plus=conj(Y_minus)`, leaving one arbitrary complex matrix.
The exact fixed-locus pair `diag(1,2,3)` and `diag(1,2,4)` has different
scale-free Gram discriminants, proving that exchange selects the conjugate
copy but not spectral shape. Exchange-even boundary traces retain the same
freedom. Further family dynamics or an isolated tensor fixed ray is required.

## Cubic equivariant Yukawa-shape no-go: WP926

- flavor-cubic-equivariant-yukawa-shape-no-go.md
- checkers/wp926_cubic_equivariant_yukawa_shape_no_go.py
- results/wp926_cubic_equivariant_yukawa_shape_no_go.json

WP926 exhausts the cubic biunitary-equivariant beta normal form for one complex
family tensor. Common gauge and trace terms cancel from singular-value-ratio
flow. A nonzero self-cubic coefficient forces every stationary nonzero
spectrum to have equal singular values and zero discriminant; a zero
coefficient leaves every shape marginal. Thus no coefficient choice produces
an isolated nondegenerate hierarchy. Coupled up/down tensors, higher
covariants, or source-derived boundary dynamics are now necessary rather than
optional.

## Coupled cubic two-tensor fixed-point no-go: WP927

- flavor-coupled-cubic-two-tensor-fixed-point-no-go.md
- checkers/wp927_coupled_cubic_two_tensor_fixed_point_no_go.py
- results/wp927_coupled_cubic_two_tensor_fixed_point_no_go.json

WP927 exhausts the cubic common-left up/down tensor fixed equations on the
invertible domain. Full coefficient rank forces both Grams to be scalar;
rank one makes them affine functions of each other and hence commuting while
leaving a shape continuum; rank zero leaves all shapes unconstrained. No case
isolates a nondegenerate CP-violating point. An exact rank-one pair exhibits
different normalized discriminants at identical coefficients. The first
possible escape must be a source-derived commutator-sensitive higher covariant,
nonpolynomial geometry, or boundary condition.

## Quintic commutator Lax-transport audit: WP928

- flavor-quintic-commutator-lax-transport-audit.md
- checkers/wp928_quintic_commutator_lax_transport_audit.py
- results/wp928_quintic_commutator_lax_transport_audit.json

WP928 tests the algebraically first commutator-sensitive tensor covariant.
Its Gram flow is Lax and preserves each sector's full spectrum. With a common
coefficient it is simultaneous weak-basis conjugation and descends to zero on
physical16 despite nonzero literal matrix velocity. Unequal coefficients may
transport relative orientation but remain isospectral; nonzero fixed-point
coefficients force commuting Grams. The first commutator term is therefore a
transport/rigidifier, not the missing shape selector.

## Double-commutator gradient audit: WP929

- flavor-double-commutator-gradient-audit.md
- checkers/wp929_double_commutator_gradient_audit.py
- results/wp929_double_commutator_gradient_audit.json

WP929 applies the source-authority gate before auditing the Hermitian
double-commutator candidate.  The exact gradient descends under the full
weak-basis groupoid and strictly contracts commutator energy, so it is not
another Lax reparameterization.  Its fixed set is nevertheless the entire
commuting locus, and the declared Spin5 source supplies neither the term nor
its coefficient, sign, normalization, or instrument.  It is therefore a
conditional proper-subspace selector, not an admitted physical flavor
selector or a distinguished-point prediction.

## Double-commutator Yukawa-lift source gate: WP930

- flavor-double-commutator-yukawa-lift-source-gate.md
- checkers/wp930_double_commutator_yukawa_lift_source_gate.py
- results/wp930_double_commutator_yukawa_lift_source_gate.json

WP930 separates quotient descent from tensor-level source construction.  The
WP929 Gram gradient has a unique Hermitian Sylvester lift on the positive
domain, but the lift contains inverse spectral sums and the naive polynomial
half-gradient fails.  The declared Spin5 action has no three-family Yukawa
beta vector, while finite-threshold matching is downstream and retains a
two-dimensional nuisance fiber.  Hence the conditional contraction has no
current source arrow; the Spin5 double-commutator branch closes negative.

## Declared flavor-selector exhaustion: WP931

- flavor-declared-selector-exhaustion.md
- checkers/wp931_declared_flavor_selector_exhaustion.py
- results/wp931_declared_flavor_selector_exhaustion.json

WP931 tests every declared selector candidate through WP930 against source
authority, `physical16` descent, proper reduction, point isolation, and a typed
instrument.  No candidate passes all five gates.  The only unconditional
source discriminator acts on upstream completion labels; every proposed
`physical16` reduction is conditional or unsupported, and all admitted
rigidifiers and transports leave an exact physical fiber.  This is a relative
exhaustion of the declared grammar, not a no-go theorem for unknown UV actions.

## Boolean threshold-score transfer: WP932

- flavor-boolean-threshold-score-transfer.md
- checkers/wp932_boolean_threshold_score_transfer.py
- results/wp932_boolean_threshold_score_transfer.json

WP932 transfers Benincasa's Boolean score theorem to the three labelled Spin7
bulk multiplets.  The formal eight-route zeta tower is unimodular and jointly
faithful on labelled route coefficients, but this reconstructs rather than
selects their values.  Current flavor threshold authority has rank one and
leaves a seven-dimensional route kernel; independent deletion controls and an
eight-route instrument are undeclared.  The transfer is therefore a
conditional source-story identifier, not a `physical16` selector.

## Aspect capability audit of Boolean thresholds: WP933

- flavor-aspect-capability-audit-boolean-threshold.md
- checkers/wp933_aspect_capability_audit_boolean_threshold.py
- results/wp933_aspect_capability_audit_boolean_threshold.json

WP933 applies Aspect's namespaced registry plus the domain axis.  The formal
Boolean packet is bright, matched, native, and faithful on labelled routes.
Spin7 deletion action and the physical threshold experiment are missing;
domain preservation and `physical16` descent are unknown; the source ordering
functional is independently missing.  Counterfactuals verify that authorizing
deletion cannot create ordering and postulating ordering cannot authorize
deletion.  The physical proposal is deferred while the formal theorem remains.

## Spin7 mass-deletion realization fiber: WP934

- flavor-spin7-mass-deletion-realization-fiber.md
- checkers/wp934_spin7_mass_deletion_realization_fiber.py
- results/wp934_spin7_mass_deletion_realization_fiber.json

WP934 locates the deletion-action defect upstream of calibration.  WP922 does
not type its bulk matter realization or mass action.  The same exact parity
census admits three independent scalar quadratic masses but, for chiral
five-dimensional fermions, forbids constant diagonal masses and permits at
most one even joint bilinear between the opposite-parity spinors.  Odd kink
masses localize rather than Boolean-delete protected zero modes.  The mass
control rank is therefore realization-dependent, so no eight-route physical
score tower is presently source-authorized.

## Deutschian realization-index-boundary audit: WP935

- flavor-deutschian-realization-index-boundary-audit.md
- checkers/wp935_deutschian_realization_index_boundary_audit.py
- results/wp935_deutschian_realization_index_boundary_audit.json

WP935 corrects the broad source-absence statement.  WP772's pure-vector
`SU(4)` gauge-Higgs packet is a genuine partial constructor: it realizes the
link as a gauge component and has positive full-tower index.  It does not
survive the complete hostile audit.  Exchange-even boundary kinetic packets
with `tau = 0, 1` preserve that realization and index but change the exact
contrast from `1/10` to `1/20`; admitting the required 32-degree bulk operand
packet changes the index from `17` to `-15`.  The missing arrow is therefore a
completion-stable boundary source law, not realization selection in general.

## Boundary-kinetic symmetry no-go: WP936

- flavor-boundary-kinetic-symmetry-no-go.md
- checkers/wp936_boundary_kinetic_symmetry_no_go.py
- results/wp936_boundary_kinetic_symmetry_no_go.json

WP936 proves that WP935's missing boundary law cannot be supplied by an
ordinary sign, orbifold-parity, or endpoint-exchange symmetry.  Boundary
gauge-kinetic operators are quadratic, so every sign character acts
trivially.  Endpoint exchange removes the odd coefficient but preserves the
one-dimensional common line generated by `(1,1)`.  The exact hostile packets
`(0,0)` and `(1,1)` obey all these symmetries while retaining WP935's distinct
contrasts.  Symmetry rigidifies endpoint labels but does not select `tau`.

## Boundary-kinetic RG selector gate: WP937

- flavor-boundary-kinetic-rg-selector-gate.md
- checkers/wp937_boundary_kinetic_rg_selector_gate.py
- results/wp937_boundary_kinetic_rg_selector_gate.json

WP937 tests the dynamical successor without inventing an undeclared physical
beta function.  Additive running preserves the complete `tau` separation;
finite homogeneous running is injective; and affine attraction conditionally
selects `-b/a`.  The equally attractive flows `-tau+1` and `-tau+2` select
different values, so stability has no numerical authority.  Because the
declared `SU(4)` packet supplies no boundary beta coefficients or proof of
matter-completion stability, RG remains a viable selector architecture but
not a source-authorized flavor selector.

## S1/Z2 hypermultiplet boundary-beta kernel: WP938

- flavor-s1z2-hypermultiplet-boundary-beta-kernel.md
- checkers/wp938_s1z2_hypermultiplet_boundary_beta_kernel.py
- results/wp938_s1z2_hypermultiplet_boundary_beta_kernel.json

WP938 imports the exact one-loop theorem that a five-dimensional bulk
hypermultiplet on `S1/Z2` does not renormalize brane gauge couplings.  This
makes the hypermultiplet completion invisible to that boundary-beta
contribution, but zero beta preserves the hostile `tau = 0, 1` pair and hence
selects nothing.  Meanwhile the same 32-degree completion changes the
full-tower index from `17` to `-15`.  Spectral completion sensitivity and
boundary-beta completion sensitivity are therefore independent.  The full
`SU(4)` vector-plus-boundary beta system and higher-loop closure remain open.

## Bulk-loop boundary-counterterm transport: WP939

- flavor-bulk-loop-boundary-counterterm-transport.md
- checkers/wp939_bulk_loop_boundary_counterterm_transport.py
- results/wp939_bulk_loop_boundary_counterterm_transport.json

WP939 imports the structural one-loop result that bulk interactions on
`S1/Z2` generate divergent fixed-plane contributions renormalized by
four-dimensional boundary couplings.  The renormalized inverse-kinetic
coefficient has affine form `tau_R = tau_B + L`.  Therefore any two bare
packets retain their exact difference.  The hostile pair `0,1` maps to
`3/2,5/2` under the same loop correction.  Computing the complete `SU(4)`
coefficient would improve transport but cannot select the finite bare term;
a separate noninvertible UV boundary law remains necessary.

## Boundary volume-suppression no-selector: WP940

- flavor-boundary-volume-suppression-no-selector.md
- checkers/wp940_boundary_volume_suppression_no_selector.py
- results/wp940_boundary_volume_suppression_no_selector.json

WP940 separates parametric insensitivity from selection.  For every finite
bulk inverse coupling `C`, the response `1/(C+tau)` remains injective in
`tau`.  At `C=100`, the hostile pair `tau=0,1` gives `1/100,1/101`, separated
by exactly `1/10100`.  A detector may collapse that difference only relative
to a declared resolution.  The singular `C`-infinite limit sends both
couplings to zero and changes the physical explanandum.  Volume dominance or
NDA smallness is therefore neither a selector nor a rigidifier.

## Boundaryless geometry-instrument no-go: WP941

- flavor-boundaryless-geometry-instrument-no-go.md
- checkers/wp941_boundaryless_geometry_instrument_no_go.py
- results/wp941_boundaryless_geometry_instrument_no_go.json

WP941 tests the geometric escape.  Replacing the orbifold interval by an
unmarked circle removes the exchange-even boundary coefficient, but also
removes both endpoint current ports.  The exact instrument rank drops from
two to zero.  This is a source-domain replacement, not selection of `tau=0`
inside the interval family.  Adding two marked circle ports creates a new
relational experiment over a smaller stabilizer groupoid and reopens the need
to type localized operators.  A boundaryless Wilson-line selector therefore
requires its own physical16 descent and calibrated holonomy instrument.

## Completion-stable boundary-selector exhaustion: WP942

- flavor-completion-stable-boundary-selector-exhaustion.md
- checkers/wp942_completion_stable_boundary_selector_exhaustion.py
- results/wp942_completion_stable_boundary_selector_exhaustion.json

WP942 freezes six acceptance gates and audits eight declared interval and
boundaryless routes through WP941.  No route passes all gates.  Symmetry,
perturbative RG, beta kernels, counterterms, and volume dominance retain the
one-dimensional bare `tau` fiber; the boundaryless circle removes its
instrument and changes the source domain.  The strongest existing comparator
is WP861's proper rank-three `physical16` family, which WP862 excludes from all
1,210 fitted sheets.  The surviving research space is therefore limited to a
completion-stable UV boundary law or a fully rederived boundaryless
holonomy-to-Yukawa experiment.

## Single-holonomy physical16 commuting no-go: WP943

- flavor-single-holonomy-physical16-commuting-no-go.md
- checkers/wp943_single_holonomy_physical16_commuting_no_go.py
- results/wp943_single_holonomy_physical16_commuting_no_go.json

WP943 attacks WP942's boundaryless route.  If both Yukawa sectors are
functions of one normal Wilson holonomy, their Hermitian Grams belong to the
same commutative functional calculus.  Their commutator and CP-odd cubic
invariant vanish identically, so the selected `physical16` image is the
experimentally wrong commuting locus.  An exact positive comparator has
leading minors `2,5,20` and commutator cubic `-36i`.  A viable boundaryless
source therefore requires at least two noncommuting family operators with a
source-fixed relative orientation and a calibrated holonomy instrument.

## Two-holonomy universal-algebra no-selector: WP944

- flavor-two-holonomy-universal-algebra-no-selector.md
- checkers/wp944_two_holonomy_universal_algebra_no_selector.py
- results/wp944_two_holonomy_universal_algebra_no_selector.json

WP944 tests the minimum noncommuting repair with the exact three-family Weyl
pair.  Its nine clock-shift words span all of `M3(C)`.  The same fixed carrier
therefore admits a commuting coefficient packet with CP cubic zero and a
mixed packet with CP cubic `-842400i`.  Noncommutativity removes WP943's blind
locus but, with arbitrary word coefficients, restores the full Yukawa fiber
and selects no proper `physical16` family.  The missing arrow is now a
source-derived proper executable word module, stable under completions and
equipped with a calibrated holonomy-sensitive instrument.

## Weyl executable-closure and conditional-expectation no-go: WP945

- flavor-weyl-executable-closure-conditional-expectation-no-go.md
- checkers/wp945_weyl_executable_closure_conditional_expectation_no_go.py
- results/wp945_weyl_executable_closure_conditional_expectation_no_go.json

WP945 asks whether the missing proper word module follows from ordinary
closure or intrinsic symmetry averaging.  The smallest unital adjoint-closed
algebra containing both Weyl holonomies is all of `M3(C)`, so closure remains
nonselective.  The clock twirl has the three-dimensional diagonal image and
kills both shift grades; the full Weyl twirl has the one-dimensional scalar
image `Tr(X)I/3`.  These canonical expectations are source-derived proper
projections, but they restore the commuting obstruction or erase flavor
altogether.  A viable successor needs additional asymmetric source data that
selects a proper noncommuting word module.

## Projective Weyl subgroup-twirl exhaustion: WP946

- flavor-projective-weyl-subgroup-twirl-exhaustion.md
- checkers/wp946_projective_weyl_subgroup_twirl_exhaustion.py
- results/wp946_projective_weyl_subgroup_twirl_exhaustion.json

WP946 exhausts the six linear subgroups of the projective Weyl label plane
`F3^2`.  The zero subgroup fixes all nine matrix dimensions and selects
nothing.  Each of the four lines fixes a three-dimensional commutative maximal
abelian algebra, so its two-sector image is CP-blind.  The full plane fixes
only the scalar algebra.  No canonical unweighted subgroup twirl therefore
has a proper noncommutative image.  Any viable channel must add asymmetric
source data rather than choose another subgroup of the declared pair.

## Weyl source-normal Bockstein rigidity no-go: WP947

- flavor-weyl-source-normal-bockstein-rigidity-no-go.md
- checkers/wp947_weyl_source_normal_bockstein_rigidity_no_go.py
- results/wp947_weyl_source_normal_bockstein_rigidity_no_go.json

WP947 applies Benincasa's source-normal strategy directly to the exact Weyl
relations.  Their dual-number relation tangent has dimension eight.  The
simultaneous weak-basis conjugation orbit also has dimension eight, and the
joined span remains eight, so the physical quotient tangent is zero.  The
primitive-root equation separately forces the commutation-phase tangent to
zero.  The exact Weyl source is therefore infinitesimally rigid modulo weak
basis and supplies no nontrivial flavor Bockstein.  The search must move to an
independently declared action, boundary, threshold, defect, or completion
coordinate outside the rigid Weyl relation object.

## Canonical traceless-channel full weak-basis no-go: WP948

- flavor-canonical-traceless-channel-full-weak-basis-no-go.md
- checkers/wp948_canonical_traceless_channel_full_weak_basis_no_go.py
- results/wp948_canonical_traceless_channel_full_weak_basis_no_go.json

WP948 classifies conjugation-equivariant linear idempotents on `M3(C)`.  The
only proper noncommutative image is the eight-dimensional traceless module.
Its projector is not positive and fails covariance under independent right
weak-basis transformations: an exact unitary frame flip gives descent
residual `-2I/3`.  Thus this canonical asymmetric channel is presentation
data, not a `physical16` selector.  A successor must act on full weak-basis
covariants or explicitly add a relational left-right reference experiment.

## Gram-pair positive exchange-channel no-go: WP949

- flavor-gram-pair-positive-exchange-channel-no-go.md
- checkers/wp949_gram_pair_positive_exchange_channel_no_go.py
- results/wp949_gram_pair_positive_exchange_channel_no_go.json

WP949 moves to the correctly typed left-handed Gram pair and classifies
positive unital idempotent two-sector mixing channels that are equivariant
under sector exchange.  Only identity and equal averaging survive.  Identity
selects nothing; averaging descends under the full weak-basis groupoid but
maps an exact positive pair with CP cubic `-36i` to equal Grams with cubic
zero.  Moreover up/down exchange is not an admitted Standard Model source
symmetry or executable sector swap.  The remaining channel must be
source-derived, asymmetric, full-weak-basis covariant, and instrumented.

## General positive Gram-sector mixing exhaustion: WP950

- flavor-general-positive-gram-sector-mixing-exhaustion.md
- checkers/wp950_general_positive_gram_sector_mixing_exhaustion.py
- results/wp950_general_positive_gram_sector_mixing_exhaustion.json

WP950 removes the exchange-equivariance assumption.  Every positive unital
scalar sector mixer has a row-stochastic `2x2` matrix.  Idempotence forces
either identity or identical rows `(c,1-c)`.  Thus every nonidentity channel
maps both sectors to one common positive Gram and kills the CP commutator.
The asymmetric weight remains continuous: `c=1/3` and `c=2/3` give distinct
positive common Grams with traces 9 and 8.  Scalar sector mixing therefore
cannot supply the selector; a successor must act on internal Gram geometry.

## Isotropic internal-Gram channel exhaustion: WP951

- flavor-isotropic-internal-gram-channel-exhaustion.md
- checkers/wp951_isotropic_internal_gram_channel_exhaustion.py
- results/wp951_isotropic_internal_gram_channel_exhaustion.json

WP951 classifies trace-preserving idempotent channels acting isotropically
inside each Gram.  Full `U(3)_Q` covariance leaves depolarizing form, and
idempotence leaves only identity or scalar Haar averaging.  Applied
independently to the two sectors, identity on both selects nothing, while any
scalarized sector commutes with the other and sends the exact CP cubic `-36i`
to zero.  A viable internal operation therefore requires a source-derived
anisotropic relational tensor rather than the invariant identity alone.

## Two-boundary-involution CP no-go: WP952

- flavor-two-boundary-involutions-cp-no-go.md
- checkers/wp952_two_boundary_involutions_cp_no_go.py
- results/wp952_two_boundary_involutions_cp_no_go.json

WP952 tests Deutsch's proposed two-decomposition mechanism with Hermitian
boundary involutions.  Two exact source decompositions can be noncommuting and
force a relational mixing plane.  In three dimensions, however, their pair
reduces to a common line plus one two-dimensional principal-angle block.  The
commutator has rank at most two and cubic trace zero, while each affine Gram
has at most two distinct eigenvalues.  The minimum viable constructor must
therefore add a third related decomposition or combine a simple-spectrum
source operator with an independently fixed noncommuting partner.

## Sector-character common-source authority no-go: WP953

- flavor-sector-character-common-source-authority-no-go.md
- checkers/wp953_sector_character_common_source_authority_no_go.py
- results/wp953_sector_character_common_source_authority_no_go.json

WP953 reopens the earlier WP350 three-projector branch.  Its up ray `(1,1,1)`
is the unique trivial line of the full natural `S3` permutation module.  Its
down ray `(1,-1,0)` is odd only under one marked transposition; the natural
three-object permutation module contains no full-`S3` sign line, and the down
ray's full orbit spans the standard two-dimensional representation.  Thus the
two rays require different symmetry objects.  Standard Model scalar gauge
charges commute with the projector permutations and cannot choose the marked
`Z2`.  The missing source is an `S3`-to-`Z2` flag or standard-doublet order
parameter, together with completion and instrument authority.

## S3-doublet cubic flag selector: WP954

- flavor-s3-doublet-cubic-flag-selector.md
- checkers/wp954_s3_doublet_cubic_flag_selector.py
- results/wp954_s3_doublet_cubic_flag_selector.json

WP954 supplies a minimal conditional repair for WP953.  On the real standard
doublet with fixed positive norm, the symmetric cubic `xyz` is bounded by
`-2` and `2`.  Its minimum orbit consists of the three permutations of
`(1,1,-2)`, each with a `Z2` transposition stabilizer.  The orthogonal line in
the standard plane is exactly a WP350 down ray such as `(1,-1,0)`.  The action
therefore selects the missing flag type up to simultaneous projector
permutation, without using flavor readout.  The doublet's source existence,
cubic sign, coupling rule, complex projector geometry, radial amplitudes,
completion stability, and instrument remain open.

## S3-flag projective sign/radial descent: WP955

- flavor-s3-flag-projective-sign-radial-descent.md
- checkers/wp955_s3_flag_projective_sign_radial_descent.py
- results/wp955_s3_flag_projective_sign_radial_descent.json

WP955 corrects the WP954 authority count.  Mapping a nonzero doublet vector to
its axis projector and orthogonal standard-plane line removes both sign and
radius.  The cubic minimum and maximum vector orbits are disjoint, but their
three projective `Z2` flags coincide exactly.  Thus the cubic coefficient sign
does not affect the WP350 projective down ray unless an additional coupling is
odd in the order parameter.  The remaining gate is the physical doublet and
its even projective coupling, plus general completion, descent, complex-ray,
amplitude, and instrument authority.

## Projective even down-coupling CP no-go: WP956

- flavor-projective-even-down-coupling-cp-no-go.md
- checkers/wp956_projective_even_down_coupling_cp_no_go.py
- results/wp956_projective_even_down_coupling_cp_no_go.json

WP956 executes the smallest even family-module coupling requested after
WP955.  For the exact WP350 projectors, `B=P-Q` obeys
`B^2=diag(1/2,1/2,0)`.  Every even function of `B` lies in the two-dimensional
algebra spanned by identity and `B^2`, so its down spectrum is twofold
degenerate.  The even benchmark descends under `B -> -B` but has down
discriminant zero and CP cubic zero; the oriented odd lift retains cubic
`-3658i/3`.  The minimum viable projective repair therefore needs a second
independently sourced tensor, not merely an even function of the flag line.

## Independent projective tensor CP sufficiency: WP957

- flavor-independent-projective-tensor-cp-sufficiency.md
- checkers/wp957_independent_projective_tensor_cp_sufficiency.py
- results/wp957_independent_projective_tensor_cp_sufficiency.json

WP957 proves that WP956 is a one-generator obstruction rather than a general
projective-descent obstruction.  Adding the independent rank-one projector
generated by `w=(1,2,i)` to `B^2` gives a simple down spectrum, rank-three Gram
commutator, and nonzero CP cubic, while remaining invariant under both flag
sign and ray rescaling.  Reusing the up-sector projector `R` splits the down
spectrum but leaves CP zero, proving that spectral splitting alone is not
enough.  The exact witness establishes algebraic sufficiency only: the second
projective tensor still lacks a readout-independent source constructor and a
physical instrument.

## Second-projective-source transfer audit: WP958

- flavor-second-projective-source-transfer-audit.md
- checkers/wp958_second_projective_source_transfer_audit.py
- results/wp958_second_projective_source_transfer_audit.json

WP958 searches the existing programme for WP957's missing source tensor.  The
nearest candidates do not transfer.  WP877 derives ordered real projectors on
an `SO(5)` five-vector carrier, but any real three-family forms have a real
antisymmetric commutator and identically zero CP cubic.  WP859 derives a
complex Kirchhoff projector and complementary port on a two-path relational
carrier, but its three-family embedding retains a common line and again has
zero CP cubic.  Neither candidate has a named source-to-family interface.
Coordinate compatibility therefore supplies no authority; the remaining gate
is an explicitly covariant complex source-to-family projector constructor
with relational independence, completion, and instrument transport.

## Complex projective source arity threshold: WP959

- flavor-projective-source-arity-threshold.md
- checkers/wp959_projective_source_arity_threshold.py
- results/wp959_projective_source_arity_threshold.json

WP959 identifies the canonical interface and its minimum relational arity.
The map from a nonzero complex triplet to its normalized rank-one projector is
ray-invariant and weak-basis equivariant.  One ray is a transitive `U(3)`
orbit, while two rays share an annihilated line and force zero commutator
cubic.  Three spanning rays first admit the weak-basis-invariant Bargmann
triple product; the exact witness has value `(1+i)/6`, whose imaginary part
reverses under conjugation.  This is an interface theorem, not a selector: a
readout-independent source action deriving the ordered triple or an equivalent
irreducible tensor, completion stability, and instrument transport remain
open.

## Symmetric three-triplet overlap-source no-go: WP960

- flavor-symmetric-three-triplet-overlap-source-no-go.md
- checkers/wp960_symmetric_three_triplet_overlap_source_no_go.py
- results/wp960_symmetric_three_triplet_overlap_source_no_go.json

WP960 tests the most economical source action on WP959's triplet packet.  The
permutation-symmetric sum of the three pairwise projector overlaps is bounded
between zero and three.  Positive coupling selects an orthonormal frame with
zero Bargmann invariant; negative coupling selects a collinear rank-one packet
with Bargmann invariant one; zero coupling leaves the relational packet flat.
All three cases are CP blind.  Thus the canonical interface plus its unique
pair-overlap scalar does not select a CP-bearing triple.  The next candidate
must add a readout-independent cyclic three-body invariant or an equivalent
irreducible complex tensor, while retaining conjugate minima, completion, and
instrument gates explicitly.

## Linear Bargmann-source extrema no-go: WP961

- flavor-linear-bargmann-source-extrema-no-go.md
- checkers/wp961_linear_bargmann_source_extrema_no_go.py
- results/wp961_linear_bargmann_source_extrema_no_go.json

WP961 adds the lowest CP-even ternary source term, the real part of the
Bargmann invariant, without fitting pairwise overlaps.  Its exact global range
is `[-1/8,1]`.  The minimum is the real coplanar trine with span rank two; the
maximum is the collinear rank-one triple.  Both extrema have zero Bargmann
imaginary part, while zero coupling is flat.  The real linear ternary term is
therefore orientation-even and selects only CP-blind boundary strata.  A
spanning spontaneous-CP source requires nonlinear phase frustration with
conjugate minima, or a separately authorized CP-odd source term, followed by
completion and instrument tests.

## Squared Bargmann-orientation boundary no-go: WP962

- flavor-squared-bargmann-orientation-boundary-no-go.md
- checkers/wp962_squared_bargmann_orientation_boundary_no_go.py
- results/wp962_squared_bargmann_orientation_boundary_no_go.json

WP962 tests the least adjustable nonlinear CP-even orientation source.  The
sharp global bound is `(Im B)^2 <= 1/16`, and equality gives the conjugate pair
`B=(1+-i)/4`.  However every maximizer has Gram determinant zero and span rank
two.  Exact positive-definite hostile Grams with identical pairwise overlap
magnitudes but Bargmann values `1/8` and `i/8` prove that the orientation
magnitude is genuinely ternary and cannot be generated by conjunction of the
WP960 pairwise probes.  The next gate is an independently normalized positive
volume completion that preserves nonzero orientation and full span; exact
conjugation symmetry still leaves handedness unselected.

## Linear volume-orientation endpoint-switch no-go: WP963

- flavor-linear-volume-orientation-endpoint-switch-no-go.md
- checkers/wp963_linear_volume_orientation_endpoint_switch_no_go.py
- results/wp963_linear_volume_orientation_endpoint_switch_no_go.json

WP963 adds the positive Gram determinant to the squared orientation with an
arbitrary positive relative normalization.  On the exact global envelope the
derivative factors as `(4u-3)(lambda-u^2)`, and every interior stationary point
is a minimum.  Below `lambda=1/16` the rank-two oriented endpoint wins; above
it the orthogonal CP-blind frame wins; at the threshold the endpoints tie.
Thus linear volume reward produces a first-order endpoint switch rather than a
spanning oriented maximizer.  The source remains typed as a `3+3+1` closed
triangle.  The next gate is an independently derived interior-enforcing
barrier, constraint, or completion field, with conjugate handedness and
instrument transport retained.

## CP-even invariant optimization-polarity audit: WP964

- flavor-cp-even-invariant-product-interior-sufficiency.md
- checkers/wp964_cp_even_invariant_product_interior.py
- results/wp964_cp_even_invariant_product_interior.json

WP964 corrects the scope of WP963. Maximizing a co-positive affine reward is
endpoint-selecting, but minimizing the same positive invariant is not. At
`lambda=1/16`, `q^2+lambda D` has strict conjugate interior minima at `u=1/4`,
with `D=3/8`, `q^2=3/256`, and value `9/256`, below the common endpoint value
`1/16`. Thus unrestricted affine optimization is already algebraically
sufficient; `D*q^2` is sufficient but not minimal. This is not yet a selector:
action polarity, occurrence, and normalization require independent source
derivation, followed by calibrated `physical16` transport.

## Affine-interior source-constructor census: WP965

- flavor-affine-interior-source-constructor-census.md
- checkers/wp965_affine_interior_source_constructor_census.py
- results/wp965_affine_interior_source_constructor_census.json

WP965 tests five joint gates against the existing Gaussian Schur, conditional
expectation, positive exchange, Abelian moment-map, and WP964 affine
constructors. No row jointly supplies occurrence, minimization polarity,
relative normalization, carrier descent, and the correct interior. The exact
polarity hostile uses one carrier at `lambda=1/16`: minimization selects
`u=1/4`, while maximization selects the two endpoints. Algebraic closure is not
executable source control. The next object must derive the affine action and
coefficient from one microscopic source and make an independent prediction
before calibrated `physical16` transport.
