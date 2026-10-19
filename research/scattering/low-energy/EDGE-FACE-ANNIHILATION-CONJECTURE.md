# Draft EF1: face capture, not assigned photon multiplicity

Status: **proposed explanatory conjecture; not an admitted live proposition or a tested physical theory**.

[Contract](contracts/edge-face-annihilation-conjecture.v1.json) · [kinematic audit](check_edge_face_hinge.py) · [receipt](results/edge-face-hinge.v1.json)

## The conjecture

> In an independently specified low-energy electron–positron preparation, the leading two- and three-photon conversion channels are two outcomes of one native, reversible encounter dynamics. Generic edge-contact release gives the two-output channel; dynamical capture into an orientation-compatible shared face gives access to the three-output channel. The latter's three outgoing carriers arise by native recombination and separation of the three internal faces around the complementary edge—not by an externally imposed photon-number selector.
>
> The same fixed dynamics determines capture versus release amplitudes, retains survival and residual information, and produces the preparation dependence of the channel weights. It does not acquire an angular tolerance or a separate coupling by fitting the desired two/three ratio.

A necessary counterfactual is: in the declared leading conversion regime, disabling face-reconnection amplitude while leaving edge release available removes the leading three-output channel, not the two-output channel. The candidate must define and justify that intervention independently; identifying "face capture" retrospectively with every three-output event would make the claim circular.

The explanation being risked is **contact geometry plus native phase dynamics selects the channel**, rather than merely illustrating an already assigned photon number. This is a candidate mechanism, not a claim that every collision converts, that all face contacts convert deterministically, or that higher photon sectors are absent. Its incoming preparation, conversion regime and event definition must be fixed before quantitative testing.

This draft sharpens the earlier [simplicial recombination construction](../../voevodsky/simplicial-recombination-particle-interactions.md) and [dimensional-resolution hypothesis](../../voevodsky/dimensional-resolution-simplex-interaction.md). It does not replace them with an unrelated annihilation model.

## 1. The geometric statement we actually have

Use the existing regular tetrahedron

```
A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1).
```

Fix edge AB and rotate a congruent second tetrahedron about it. Let M be the midpoint of AB and put c=C-M, d=D-M. Both off-edge vertices project onto M. Their perpendicular Gram matrix is

```
G_perp = [[6,2],[2,6]].
```

Consequently the internal dihedral angle alpha satisfies cos(alpha)=1/3. In the ordered perpendicular basis (c,d), the proper rotation carrying c to d is exactly

```
R_plus = [[0,-1],[1,2/3]],
R_minus = R_plus^(-1) = [[2/3,1],[-1,0]].
```

Both preserve G_perp and have determinant one. They are placements in a Euclidean hinge family, **not yet source-authorized phase/transport operations**.

At rotation minus alpha, D moves to C and C moves to

```
e = M+(2/3)c-d = (5/3,5/3,-5/3).
```

This is exactly the reflection of D across ABC used by the existing [three-tetrahedron belt](../../voevodsky/three-tetrahedron-belt.md). Thus the hinge family genuinely reaches that face-sharing pair. Rotation plus alpha supplies the analogous contact on ABD. Zero rotation instead superposes the entire tetrahedra and is not a distinct non-overlapping encounter.

For labelled, congruent tetrahedra with AB fixed pointwise, these are the two non-superposed full-face alignments in one turn. The non-overlapping hinge placements occupy the closed interval

```
alpha <= phi <= 2*pi-alpha,
Omega = 2*pi-2*alpha.
```

The endpoints are face contacts; the interior has only the shared edge. This follows from the disjoint interiors of the two dihedral sectors [0,alpha] and [phi,phi+alpha]. Here alpha is about 70.5288 degrees and Omega about 218.9424 degrees. Do not silently use 360 degrees as the non-overlapping encounter range for this constrained family.

The ABC face-sharing pair has the known alternative subdivision

```
ABCD, ABCe  <-->  ABDe, BCDe, CADe.
```

It preserves the oriented outer boundary and total volume. The three internal triangles are ADe, BDe, CDe. At this stage they still share De: **they are not three independently separated photons**. Recombination, extraction and dynamical separation are distinct obligations. Generic edge-contact's two-output construction remains unselected as well.

## 2. Why rotation alone is not a branching mechanism

Exact face alignment is a finite set of angles. Its probability is zero under any absolutely continuous *static* angular distribution. Counting one rotational degree of freedom versus zero does not predict a positive three-output fraction.

But this does **not** exclude dynamical capture. A trajectory can hit a boundary with positive probability even when that boundary has zero instantaneous configuration measure.

For illustration only, normalize the allowed angular interval to x in [0,1]. With uniform initial x, constant positive speed v, a fixed contact duration tau and absorbing face capture at x=1, the first-hit fraction is

```
P_capture = min(v*tau,1).
```

A negative speed gives the corresponding result at x=0. This toy law imports speed, duration and capture; it is not a native prediction. If a persistent hinge rotates indefinitely without escape or reflection, every nonzero-speed trajectory reaches a face. Thus "face alignment is rare" does not follow from the geometry either.

A real explanation must derive **capture, escape and their competition** from the same source dynamics. A finite acceptance window is not an explanation if its width is chosen to reproduce the desired ratio. The earlier 372 is still a preparation-dependent working input, not a derived universal physical ratio.

## 3. What must be frozen to test EF1

Before generating a prediction, supply one concrete candidate packet containing:

1. **Incident data:** source carriers, opposite-orientation convention, phase/spin preparation, contact geometry, energy and event acceptance. No assigning the contact geometry retrospectively from the observed photon count.
2. **One generator or retained continuation law:** actual source-authorized edge motion and joint phase transport, including the trigger for changing incidence. A Euclidean rotation or a relabelling policy alone is insufficient.
3. **Complete state accounting:** survival, edge release, face capture, conversion and residual/record sectors; conserved norm/flux in the declared metric. No deletion of mismatch records to make conversion work.
4. **Constructive outputs:** a source-generated two-output process and the three-face process, with independently available factor controls and a separation/propagation witness. Shared triangles and port counts are not photon factors.
5. **Independent physical binding:** incoming electron/positron and outgoing photon state/detector maps, dimensional calibration and a normalized asymptotic probability prescription. Any physical input must be named, not disguised as seed-only derivation.

The candidate must make counterfactual predictions for changed incident phase/orientation or energy with the **same** law. A contact-label lookup table with fitted amplitudes is not EF1's explanation.

## 4. Criticisms that can defeat a fixed candidate

Once that packet is frozen, test:

- **Wrong support:** the candidate's claimed leading three-output mechanism operates without the required face-capture history, or its required capture-to-output construction fails.
- **No native hinge dynamics:** the needed motion, phase compatibility or reconnection is unavailable in its declared operation class.
- **No output independence:** the alleged three photons remain one shared-edge object, cannot propagate separately or lack the independent operations claimed by the detector dictionary.
- **Hidden assignment:** multiplicity, a capture window, a coupling or an event cut is selected after seeing the target ratio.
- **Wrong physics:** the frozen, independently calibrated predictions disagree with preparation dependence, exclusive rates, spectra or angular correlations, within a stated measurement/approximation regime.
- **Presentation dependence:** an incidence refinement or equivalent retained presentation changes a physical prediction without a physically specified distinguishing operation.

Failure refutes the fixed candidate or a precisely delimited operation class—not all imaginable simplicial explanations. Until the generator and physical dictionary are supplied, EF1 remains a research conjecture rather than an already executable empirical test. A failed search alone is not its refutation.

## 5. Current result and next decisive construction

The exact checker verifies the hinge matrices, the two face contacts, their identity with the existing reflected-apex geometry, generic edge-only placement, and the complementary-edge three-cell boundary/volume identity. Its finite algebra checks are not independent physical evidence or a machine-formalized proof of the analytic measure/first-hit arguments.

The [phase-continuation audit](HINGE-PHASE-CONTINUATION.md) now excludes a finite-symmetry-only implementation using the actual stored L/G/N stages and 24 binary-tetrahedral actions. It constructs the compatible moving-frame spin lift and a complete conditional coherent-controller implementation of its logical endpoint. Controller availability and the moving-face adapter are additional resources, not supplied native operations; the 3/8 herald probability is not an annihilation probability. Compatible spin transport still admits distinct norm-preserving contact mixers with different capture-label weights.

The [EF1-N contact-support test](NORMAL-DIRECTION-CONTACT-TEST.md) now freezes an additional triangle-normal momentum readout and tests ordinary isolated massless conservation. That restricted realization fails: the original ACE/BDF template is forbidden at every distinct hinge placement, and all ten vertex-disjoint partitions fail on an open set of generic edge angles. At the exceptional pi placement two already-present antipodal input-face pairs permit balanced two-ray momenta. The face-sharing three-face configuration permits only equal-energy, 120-degree rays under this readout. These are constraints on a particular new physical interpretation, not a refutation of all EF1 constructions or a production amplitude.

The new [EF1-B CM completion](CM-SEPARATION-MAP.md) now constructs one retained classical momentum map, treating normals as auxiliary seeds rather than final directions. A rotation-free boost plus common scaling gives on-shell, conserved two-/three-ray outputs with an exact inverse when boost/scale records are retained. The old EF1-N rejection stands: this changes the readout hypothesis, not a coupling. Baseline symmetric geometry still gives equal three-ray energies; unequal seed weights parameterize general interior energy shapes but have not been source-selected and do not predict a spectrum.

The [relative quantum continuation](RELATIVE-PHOTON-MEASURE.md) now constructs the weight-ratio/phase-space half-density unitary and normalized Bose-symmetric conditional profiles. An explicit interference observable verifies phase retention. This imports photon phase space and helicity frames; it supplies neither a native-input intertwiner nor a full total-momentum wavepacket, and normalization does not select a spectrum.

The [native-pair continuation](NATIVE-PAIR-INTERTWINER.md) now constructs diagonal-tetrahedral pair intertwiners into both two-/three-output Bose scalar coefficient spaces. It preserves all four input amplitudes but does not include physical helicity rotations. A two-ray quadrupole code has exact leakage under a nonnative 45-degree rotation, so finite symmetry must not be promoted to continuous spin selection. Both multiplicities admit intertwining isometries with freely different sector weights; these conditions do not derive a ratio.

The [three-photon helicity continuation](THREE-PHOTON-HELICITY.md) now constructs a conditional relative rotation-intertwining pair isometry, including the polarization exchange cocycle. In its co-rotating plane frame, odd permutations flip the three-polarization section; corrected odd singlet/triplet coefficients restore Bose symmetry. This is an imported fixed-total-momentum photon-sector construction, not native emission, a full Lorentz intertwiner or a physical electron/positron preparation.

The [two-photon helicity audit](TWO-PHOTON-HELICITY.md) now covers all four helicity pairs. Continuous total-J=1 covariance plus Bose exchange excludes exclusive two-real-photon output, but the native finite triplet has no such total-spin binding: its quadrupole code still admits a physical relative-photon completion under the 24 native actions. Even with continuous spin0-plus-spin1 assumed, singlet two-/three-output mixing remains free.

The [native charge/preparation audit](NATIVE-CHARGE-PREPARATION.md) now constructs a full raw linear flip between orthogonal Pauli codes while preserving the complement. The stored negative protocol annihilates the positive code and cannot generate this flip. The inspected sources leave both pair swap signs and a continuous family of rotation-invariant singlet fractions unselected; even equal one-body marginals do not fix those correlations. Existing antiunitary source limitations are replayed, not mistaken for physical field charge conjugation.

The [graded contact vertex](GRADED-CONTACT-VERTEX.md) now supplies that explicit extension: four charged CAR modes, a vacuum-fixed species flip deriving minus-swap within the extension, retained raw embeddings and a self-adjoint conversion operator. It preserves charge, C, fermion parity and native rotations but has two independent contact coefficients. Its finite closed code exhibits exact Rabi survival and recurrence, not irreversible annihilation; CAR and physical charge/preparation remain additional assumptions rather than native consequences.

The [Jacobi escape completion](CONTACT-ESCAPE-CONTINUUM.md) now constructs an infinite self-adjoint half-line model. Weak active couplings give complete local release and a free outgoing asymptote; a positive stronger example retains bound norm 1/sqrt(5), with local pair probability only 1/5. Their difference is a retained lead cloud, not escaped radiation. The band, coupling envelope and energy-uncertain localized source are new inputs, not physical photon propagation or an on-shell incident preparation.

The [unbounded energy-tail audit](PHOTON-ENERGY-TAIL.md) now supplies orthogonal, phase-volume-compatible photon profiles with a normalizable unbounded envelope. Arbitrarily small positive tails remove the cutoff bound sector, although finite-time propagators differ by at most |delta*t|. Thus late retention is not controlled by a small finite-time error. The envelope and strength remain added assumptions, not a native emission law.

The [total-momentum packet](TOTAL-MOMENTUM-PACKET.md) now supplies a full normalizable Bose-Fock state and an eight-mode coarea isometry with retained mass/boost measure, Bose factors and helicity transport. It intertwines an imported photon Lorentz carrier, not a source-derived charged-pair action. Lab energy is M*u0, not CM mass M; a packet alone does not lift the rest escape dynamics.

The [covariant escape lift](COVARIANT-ESCAPE-LIFT.md) now supplies an active Poincare completion under P^mu=u^mu*H_rest, with correct lab wave operators and a full photon readout. Bound/spectator records remain; no Lorentz action is silently assigned to untyped raw records. Its cutoff control retains bound mass weight 1/sqrt(5) despite continuous lab energy and vanishing global return amplitude, so dephasing is not release.

The [local-source audit](LOCAL-SOURCE-VERTEX.md) now constructs conditional Dirac/Maxwell Wick-density candidates with the required C signs, nonzero gauge-invariant photon amplitudes and a restricted envelope obstruction: a finite-derivative point-current tree contact cannot exactly supply the chosen rational mass envelope. Composite sources, mediators and UV completions are not excluded. The cubic candidate also has a nonzero mixed-helicity amplitude outside the preceding equal-helicity code; it does not close on those selected modes. Formal local density is not a self-adjoint interacting QFT or a native source licensing.

The [full helicity projection](LOCAL-HELICITY-PROJECTION.md) now gives exact coherent overlaps: the cubic candidate's prior all-plus profile span retains 1/4 of its conditional norm and leaves 3/4 orthogonal, including 3/8 in mixed helicities. The scalar candidate produces a coherent ++/-- superposition. Old band support is not erased; these are subspace overlaps, not multiplicity rates.

The [incoming Dirac packet](INCOMING-DIRAC-PACKET.md) now constructs a declared normalizable imported charged pair with threshold, spin transport and mass/boost measures. Its pseudoscalar and vector transition currents retain coherent S-wave averaging and the possible D-wave contribution, without selecting a physical preparation or singlet fraction.

The [outgoing Born maps](OUTGOING-BORN-MAP.md) now supply finite compact-packet strengths with full photon profiles, phase volumes, Bose factors, mass powers and independent dimensionful couplings. Exact threshold integrals and the coherent current-null alternative are retained. Keeping the incoming state unchanged plus the Born output gives norm 1+W, not a unitary scattering operator or an annihilation rate.

The [on-shell completion audit](ON-SHELL-UNITARY-COMPLETION.md) now constructs two unitary controls sharing the Born and second-order forward terms but not finite conversion strengths. Survival, inverse channels, dark S/D states and full photon complements remain. The declared pure S-wave triplet packet retains at least 1/33 charged norm within this completion family, not as a physical survival prediction.

The [packet weak-coupling audit](PACKET-WEAK-COUPLING-TAIL.md) now certifies compact errors and a normalizable finite-energy mass tail outside the Born domain. Its model strengths scale as epsilon2 and sqrt(epsilon3), with completion-dependent leading constants. Ordinary cutoff/weak limits commute; specified rescaled limits do not.

The [bright-tail domain audit](BRIGHT-TAIL-DOMAIN.md) now gives sharp power/log boundaries after coherent projection and two normalized damping controls preserving the low-mass wavefunction and tail norm. They restore finite-order Born recovery; even the exponential control has a zero-radius coupling series in the eta=0 model.

The [complex-mass audit](COMPLEX-MASS-ANALYTICITY.md) now finds that the eta=1 scalar analytic candidate fails subthreshold open-photon contractivity, while both identity patches differ from their upper germs. Certified imaginary-mass poles map to negative s, not a general local-QFT exclusion.

The [scalar dispersive response](SCALAR-DISPERSIVE-RESPONSE.md) now matches the charged-pair cut with four full-response subtractions (two after Ward factoring), retaining free s^2 and s^3 terms and a nonzero dispersive phase. It is a right-cut control, not an exact unitary or crossing-complete amplitude.

The [crossed four-photon audit](CROSSED-FOUR-PHOTON.md) now supplies the leading Bose/Ward tensor and scalar cuts at +/-4. It preserves J0 parity in the photon-elastic block but gives a nonzero orthogonal-channel response, not J0-to-J2 leakage. The massive-pair-only leading response is analytic at zero, unlike the zero-phase Cayley germ.

The [photon unitarity-cut audit](PHOTON-UNITARITY-CUT.md) now fixes Im B=A^dagger*A/8 for the pure subthreshold g2^4 coefficient on the Bose carrier, including the orthogonal scalar and mixed-helicity channels. It classifies subtraction-dependent infrared powers and right-cut logarithms without claiming the full crossed germ.

The [crossed photon IR-log audit](CROSSED-PHOTON-IR-LOGS.md) now crosses the leading-IR pure-g2^4 photon cuts in all three subtraction regimes. Both scalar parity real logs survive in these controls, with partial cancellations and sign changes; right-cut positivity is unchanged. This is a leading-IR kernel, not the full quartic spectrum.

The [local counterterm audit](PHOTON-COUNTERTERM-RUNNING.md) now supplies 3, 5 and 6 independent on-shell coefficients in the parity-even log-supported sectors at q=4,6,8, with beta=-h for log(nu); finite matching remains free. This is not a complete off-shell EFT basis or anomalous-dimension matrix.

The [mixed photon IR-log audit](MIXED-PHOTON-IR-LOGS.md) now constructs the degree-five `c0*c1` cuts and their three local running coefficients. Its scalar real-log coefficients are 31/144 and 5/144 with `c0*c1` stripped; signed interference preserves positivity of the complete two-term square.

The [degree-six audit](DEGREE6-PHOTON-IR-LOGS.md) now includes both `c1^2` and `c0*r4` in the declared kernel. It classifies distinct scalar-log zero loci and a rank-two input-to-running map; simultaneous scalar-log cancellation requires both input monomials to vanish. Finite matching and the spectral input remain unselected.

The [bilinear IR-series audit](BILINEAR-PHOTON-IR-SERIES.md) now supplies the general cut/scale functional and a physical-window convergence certificate for 0<s<1, uniform in angle, with explicit homogeneous tails. This does not prove full-amplitude or coupling-series convergence.

The [windowed dispersion audit](WINDOWED-PHOTON-DISPERSION.md) now supplies a prescribed crossing-compatible Cauchy representative, reproduces the retained photon cut and bounds its analytic remainder. The window endpoint is artificial; UV matching remains unselected and unbounded.

The [forward moment audit](FORWARD-PHOTON-MOMENTS.md) now constructs coherent positive cut moments with exact IR convergence limits and a certified indefinite IR-subtracted counterexample. These are not finite matching bounds.

The [forward crossing audit](FORWARD-CROSSING-POSITIVITY.md) now derives the partial-transpose crossing map and preparation cones, with certified negative entangled crossed-moment controls. Dispersion bounds remain conditional; cut-free matching polynomials remain free.

The [forward IR-subtraction audit](FORWARD-IR-SUBTRACTION.md) now constructs a whole-window forward cut subtraction, certifies its analytic remainder and derives all-degree window transport. Shell ordering depends on preparation; physical matching and UV assumptions remain unselected.

**Next:** construct a Ward/Bose off-forward lift and compare its analytic shift with the symmetric-flow representative, retaining forward-invisible matching freedom. A leading dispersive response is not a full unitary local QFT. Source preparation must remain distinct from an interaction form factor. Such on-shell controls must not be promoted to local/cluster dynamics or native source licensing. Native support and cluster assumptions remain open; a selected-mode projection does not inherit a field algebra's microcausality. Independently bind the incident preparation, envelope/scale, thresholds and couplings without fitting counts. Source-native operation and contact-generator obligations remain open. The classical CM assignment alone is not a native physical emission operator. If this requires an extra physical interaction, expose it as a new assumption and test the resulting narrower theory. Repeating stationary port calculations does not supply this missing interaction.

No C1–C12 disposition, protocol budget or historical owner receipt is changed. High-energy execution remains paused. This proposal does not renew C12 or admit a physical outcome.

```sh
python -S research/scattering/low-energy/check_edge_face_hinge.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_edge_face_hinge.py
```
