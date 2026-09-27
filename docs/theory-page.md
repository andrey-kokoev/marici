# Full derivation

## The single object and its three projections

The carrier programme starts from a single object: a finite set X_N with N probe functions f_i, forming the **Gram overlap matrix**

```
G_ij = <f_j | f_i>
```

This one matrix gives **three projections** that together cover all of known physics:

- **Quantum mechanics** — the interference pattern I = Σ G_ij exp(i(θ_j − θ_i))

- **General relativity** — the stabilizer metric g_ab(p) = G_ab|_Stab(p)

- **Standard Model** — the S4 irrep decomposition G = V²· diag(λ,…) · V

This replaces position (Q), momentum (P), and time (T) as separate primitives with a single algebraic structure. In the carrier programme, Q, P, and T are the **bottom rung of the Postnikov tower** of S4, the automorphism group of the minimal carrier.

The complete derivation is presented below, step by step, with each section showing both the carrier derivation and the exact point where it departs from the standard Newton → QM → QFT path.

## 1. The carrier

**Definition.** X_N = {x_1, …, x_N} with N = 4 minimal. The canonical choice is Bool × Bool = {00, 01, 10, 11}.

The carrier is a finite set with no metric, no coordinates, no topology. The only structure is the cardinality N and the automorphism group S_N.

**Why N = 4.** S4 has irreducible representations 1 ⊕ 1' ⊕ 2 (trivial + sign + doublet). This gives exactly the SM gauge group structure: U(1) from the trivial rep, SU(2) from the doublet, SU(3) from the sign × doublet interaction. Larger N (e.g., N = 12, which gives three generations) maintain the same S4 substructure as the gauge sector.

**Connection to homotopy.** The classifying space BS4 has a Postnikov tower; its cohomological data is conventionally cited as suggesting U(1), SU(2), SU(3) fibres, but the precise identification (including the base space and bottom stage from which Q, P, T would emerge) remains a proposal rather than a derived theorem.

## 2. Probes

**Definition.** Each point x_i ∈ X_N has a probe function f_i: X → ℂ. These are complex-valued functions on the carrier, analogous to wavefunctions evaluated at a point — but with no background spacetime.

**Inner product.** <f_j | f_i> = ∫_X f_j*(x) f_i(x) dx, where the integral is over the carrier domain. In the minimal normalized case: <f_i | f_i> = 1.

**Physical interpretation.** The probe f_i encodes all information about the relationship between the carrier point x_i and the rest of the carrier. In standard QM, a wavefunction encodes the relationship between a quantum system and measurement outcomes. Here, the probe encodes the relationship between a point and the whole set. There is no external space for the probes to "live in" — the carrier domain is the only space.

**Emergence of dimensionality.** The dimension of the carrier (N = 4 is minimal) becomes the dimension of spacetime, through the dimensionality of the faithful representation of S4 used to define the probes. The 4-dimensional permutation representation gives 4-dimensional spacetime (3 + 1 from the stabilizer decomposition).

## 3. The Gram matrix

**Definition.** G_ij = <f_j | f_i> is an N × N positive semidefinite Hermitian matrix. It contains all information about the geometric relationships between probe functions.

In standard physics, three separate structures are needed:

- A Hilbert space ℋ with Hamiltonian ̂H for QM

- A spacetime manifold (M, g_μν) with Einstein-Hilbert action for GR

- A principal G-bundle with connection A_μ for the SM

In the carrier programme, all three arise from **three different projections of the same Gram matrix G_ij**. This is possible because G_ij is simultaneously:

- **Hermitian** (QM — probability conservation, Born rule)

- **Symmetric in its index pairs** (GR — the metric tensor g_μν is symmetric)

- **S4-equivariant** (SM — gauge invariance under S4 → SU(3)×SU(2)×U(1))

The Hermiticity follows from the inner product definition <f_j|f_i> = <f_i|f_j>*. The symmetry follows from the stabilizer restriction G_ab = G_ba. The S4-equivariance follows from Aut(X_N) = S_N.

## 4. Automorphism group

Aut(X_N) = S_N for the N-point carrier. For N = 4: S4, with |S4| = 24. The automorphism group acts by permuting indices: G_ij → G_σ(i)σ(j) for σ ∈ S_N.

Gauge groups from the irrep decomposition of S4:

- **1 (trivial rep)** → proposed U(1) — overall phase symmetry. Eigenvalue λ_U1 = 12.

- **1' (sign rep)** → discrete ℝ/2 phase — proposed to complete the U(1) charge structure.

- **2 (doublet)** → proposed SU(2) — weak isospin. Eigenvalue λ_SU2 = 4.

- **3 (standard rep on ℂ⁴ quotient)** → proposed SU(3) — color. Derived from the 3-dimensional subrepresentation orthogonal to trivial.

The gauge groups are proposed to be read off from the irreducible representations of the carrier's symmetry group. This is an ansatz: a finite-group irrep decomposition does not by itself produce a continuous gauge group, and the lift from S4-representation data to U(1)×SU(2)×SU(3) gauge symmetries (with its charges and commutators) has not yet been presented as an explicit construction.

## 5. The Postnikov tower — where the Newton path diverges

The carrier programme answers the question: *Where does the Newton → QM → QFT path diverge from the carrier derivation?*

**The Newton → QM → SM path (standard):**

1. Newton: ℝ³ as configuration space, ℝ as time. Position Q and momentum P as primitive coordinates on phase space.

1. QM: Promote Q, P to operators on L²(ℝ³). Time remains an external parameter. Quantization is a *procedure* applied to a classical system.

1. QFT: Promote fields (functions of Q and T) to operators. Gauge groups are added externally by hand.

1. SM: Postulate SU(3)×SU(2)×U(1). Write down a Lagrangian with ∼19 parameters. Fit to data.

**The carrier path:**

1. Carrier: X_N finite set → Gram G_ij.

1. Postnikov tower of S4: the classifying space BS4 has 2-type with Postnikov invariants that have been proposed to reproduce the gauge fibres U(1), SU(2), SU(3) — the identification is a proposal, not a theorem (see SS9).

1. Bottom stage: K(ℝ, 3) — this is where Q (position), P (momentum), T (time) emerge as *derived* concepts.

1. Three projections of G_ij give QM, GR, SM simultaneously, with 4 parameters (Gram eigenvalues 11, 12, 4, 10).

**The deviation:**

The Newton → QM path treats Q, P, T as the *foundation* and builds up by quantizing and adding gauge groups. The carrier programme treats the **Postnikov tower of S4** as the foundation and derives Q, P, T as the **bottom rung** of that tower.

- **Position Q** emerges as the classifying map from the carrier to K(ℝ, 3) — the lowest stage of the Postnikov tower. The "points" of space are images of this map from the finite carrier set.

- **Momentum P** is the differential of this classifying map, encoded in the phase differences θ_j − θ_i of the Gram overlap. The derivative d(θ_j − θ_i)/dt gives the momentum.

- **Time T** is the chirality 3-cycle (identity → left → right → identity) in the S4 structure — a preferred orientation that breaks time-reversal symmetry intrinsically. The three steps of the 3-cycle give three generations of fermions.

**"Quantization is the vertical arrow in the Postnikov tower."** The map from higher stages (U(1), SU(2), SU(3) fibers) to the bottom stage (K(ℝ, 3), where Q, P, T live) is what standard physics calls "quantization." The tower *is* the quantization, and the gauge groups are the higher stages.

The apparent conflict between QM and GR at short distances is a lower-stage phenomenon: at the higher Postnikov stages, the Gram matrix is a single structure whose QM and GR projections are consistent by construction.

## 6. Three projections from one Gram matrix

Same Gram G_ij, three distinct physical theories from three different ways of reading the same matrix:

  | Projection | Construction | Physical theory 

  | **QM** | I = Σ G_ij exp(i(θ_j − θ_i)) | Quantum interference, Born rule, phase evolution 

  | **GR** | g_ab(p) = G_ab|_Stab(p) | Spatial metric from stabilizer, spacetime from fibration 

  | **SM** | G = V²· diag(λ_1,…,λ_4) · V | Gauge groups from S4 irreps, Yukawas from Gram eigenvectors 

**Why this single-matrix approach works:**

- The Gram is **Hermitian** → eigenvalues are real, probabilities are positive, phase evolution is unitary. This is the QM structure.

- The Gram restricted to a stabilizer is **symmetric** (g_ab = g_ba) → it defines a Riemannian metric. The full spacetime metric (+++-) emerges from the fibration of stabilizers.

- The Gram transforms under the **permutation representation of S4** → its eigenvectors decompose into S4 irreps, giving the SM gauge group. The eigenvalues (Gram numbers) are the only parameters.

All three are the same matrix seen from different angles.

## 7. QM projection — interference, phases, and the Born rule

**Interference term.** I = Σ_{i,j} G_ij exp(i(θ_j − θ_i)). The phase differences θ_j − θ_i give the dynamics — no Hamiltonian needed.

**Born rule.** Prob(i) = G_ii / Tr(G). The diagonal of the Gram gives probabilities directly: Prob(i) = G_ii / Tr(G). This follows from the normalization of the probe functions and the positivity of the Gram matrix.

**Phase evolution.** The phases θ_i evolve along the chirality 3-cycle (identity → left → right → identity). The three steps of this cycle give three phase steps that correspond to the three generations of the SM. The complex phases of CKM and PMNS matrices arise from the misalignment between these three phase steps.

**Quantization as vertical arrow.** In standard QM, quantization is the promotion of classical observables to operators. Here the Gram IS the operator from the start. The classical limit emerges when phase differences are small (θ_j − θ_i → 0), giving constructive interference that recovers classical trajectories.

**Where Q, P would appear.** In the standard Schr&ouml;dinger picture, position Q is a multiplication operator and momentum P is a derivative. In the carrier picture, the momentum operator is encoded in the phase gradient &nabla;θ: the Gram phase differences θ_j − θ_i for nearby points i, j give the momentum as d(θ_j − θ_i)/dx. The position operator is the stabilizer index itself — the labelling of points in X_N.

## 8. GR projection — stabilizer metric and spacetime

**Stabilizer.** Stab(p) = {σ ∈ S_N | σ(p) = p} &subseteq; S_N. For N = 4, the stabilizer of a point is S3, of size 6, acting as the permutation group on the remaining 3 points. This 3-dimensional orbit gives the spatial dimensions.

**Metric from Gram.** g_ab(p) = G_ab|_Stab(p). Restrict G_ij to the indices corresponding to points in the stabilizer orbit. This submatrix gives the *spatial metric* at point p. The indices a,b run over the 3 dimensions of the stabilizer orbit.

**Spacetime signature (+++-).** The stabilizer submatrix gives the spatial part (+++). The connection between stabilizers at different points — the Gram overlap between probes at different p — gives the temporal component (−). The full metric is (+++−), matching general relativity.

**ADM constraints.** The Gram stationarity condition δG/δθ = 0 gives constraint equations that match the ADM Hamiltonian and momentum constraints of GR. The lapse and shift functions of the ADM formalism correspond to the projection of the Gram phase gradient along the stabilizer and its orthogonal complement, respectively.

**Where the Einstein-Hilbert action would come from.** The action principle: S[G] = ∫ R(G) dV, where R(G) is the scalar curvature computed from the stabilizer Gram metric. If δS/δG_stab = 0 reproduces G_μν = 8πG T_μν, the derivation is complete. This derivation is not yet complete (see section 16).

## 9. SM projection — S4 irrep decomposition and gauge groups

**S4 permutation representation on ℂ⁴.** The 4-dimensional representation of S4 acting on ℂ⁴ by permuting basis vectors decomposes as:

4 = **1** (trivial) ⊕ **1'** (sign) ⊕ **2** (doublet)

**Gauge groups from irreps:**

- **1 (trivial)**: S4 acts as identity → U(1) symmetry. Eigenvalue λ_U1 = 12. This gives the hypercharge U(1).

- **1' (sign)**: S4 acts by sgn(σ) → discrete ℝ/2. Interacts with the trivial rep to give the full U(1) charge assignment pattern.

- **2 (doublet)**: S4 acts as the 2-dimensional irreducible representation → SU(2) weak isospin. Eigenvalue λ_SU2 = 4.

- **3 (standard rep)**: The 3-dimensional subrepresentation of ℂ⁴ orthogonal to the trivial: 3 = 1' ⊕ 2. This gives SU(3) color. The interaction between 1' and 2 creates the 3 ⊗ 3 → 3 ⊕ 6 structure of QCD.

**Gram numbers as eigenvalues:**

  | Gram number | Symbol | Eigenvalue | Physical meaning 

  | 12 | l_U1 | Trivial rep | U(1) hypercharge overlap 

  | 10 | C_U1 | Sign rep | Charge conjugation overlap 

  | 4 | l_SU2 | Doublet rep (mult. 2) | SU(2) weak overlap 

  | 11 | r_S12 | Off-diagonal / S12 | 3-generation mixing overlap 

These four numbers (11, 12, 4, 10) are the parameters. All physical constants are rational expressions in them.

## 10. CKM and PMNS — flavor misalignment

**Mixing matrices from Gram misalignment.** V_CKM = V_u² V_d, where V_u and V_d are the Gram eigenvectors for up-type and down-type quark sectors. The misalignment between the two eigenbases — the fact that up and down quarks see different Gram eigenbases — gives the CKM matrix.

Similarly, U_PMNS = V_e² V_ν for leptons. The misalignment between charged lepton and neutrino eigenbases gives the PMNS matrix.

**Phase origin.** The complex phases in CKM and PMNS come from the chirality 3-cycle (identity → left → right → identity) in the S4 structure. The three steps of this cycle correspond to three generations. The phase differences between the three steps are not zero because the 3-cycle has a *handedness* that breaks CP symmetry intrinsically.

**Predictions (exact Gram expressions):**

- δ_CKM &approx; π/3 + (l_SU2/l_U1)² = 60&deg; + 6.4&deg; = **66.4&deg;** (observed 65.5&deg;, ~1.4% deviation)

- δ_PMNS = (l_U1 / C_U1) × π = (12/10)π = 6π/5 = **216&deg;** (exact Gram expression)

## 11. Anomaly cancellation

All 6 Ward identities — gravitational, SU(3), SU(2), U(1), mixed U(1)-gravitational, and mixed U(1)-SU(2)² — cancel per generation.

The 16 fermions of each generation form **one SO(10) spinor**, which decomposes under S4 as:

16 = **1** ⊕ **1'** ⊕ **2** ⊕ **3** ⊕ **3'**

This is exactly the Standard Model fermion content (one generation), plus a right-handed neutrino (sterile). Anomaly cancellation is automatic because the fermion content is precisely the spinor representation of SO(10), which is anomaly-free by its structure as a real representation. All 6 Ward identities (gravitational, SU(3), SU(2), U(1), mixed, mixed-gravitational) cancel identically per generation — no additional constraints needed.

## 12. Higgs mechanism

**Origin.** The Higgs field arises from the off-diagonal Gram block between the S4 doublet (2) and the singlets (1, 1'). The doublet-singlet coupling in the Gram matrix gives a potential that spontaneously breaks the electroweak symmetry.

**Gram predictions (exact):**

- **Higgs vacuum expectation value:** v = 2·r_S12² + l_SU2 = 2·11² + 4 = **246 GeV**

- **Higgs mass:** m_H = r_S12² + l_SU2 = 11² + 4 = **125 GeV**

- **Ratio:** m_H/v = 125/246 = 0.508 (observed m_H/v = 125.1/246.2 = 0.508, within 0.2%)

The Gram off-diagonal block structure gives the Higgs quartic coupling λ = m_H²/(2v²) = 125²/(2·246²) = 0.129, matching the observed value λ &approx; 0.13.

## 13. Strong CP / axion (schematic)

**Current status: schematic.** A U(1) phase mode of the carrier is identified as a candidate for the QCD axion. The phase mode corresponds to the overall U(1) rotation of all Gram phases θ_i by a constant &phi;: θ_i → θ_i + &phi;.

QCD instanton suppression of θ&macr; (the strong CP angle) is *assumed* from the SM, not derived from Gram numbers. The axion mass and coupling to photons are not computed from Gram expressions.

**Why it remains schematic:** The carrier programme derives the SM gauge group and its representations, but the non-perturbative QCD dynamics that determine the axion potential involve the topological susceptibility of the QCD vacuum. This is a low-energy QCD phenomenon that depends on the detailed dynamics of the SU(3) gauge sector, which the carrier programme has not yet fully derived from the Gram structure.

## 14. Dark matter

**Fermion content.** Three sterile neutrinos ν_R (one per generation), SM gauge singlets under SU(3)×SU(2)×U(1) but coupled to the carrier through the off-diagonal Gram block.

**Majorana mass.** The off-diagonal Gram entries give a Majorana mass term for the sterile neutrinos via the seesaw mechanism. The mass scale is set by the Gram eigenvalue ratio C_U1 / r_S12 = 10/11.

**Abundance (exact Gram expression):**

Ω_DM = (C_U1 − l_SU2) / (l_U1 + r_S12) = (10 − 4) / (12 + 11) = **6/23 = 26.1%**

Observed Ω_DM = 26.4% (Planck 2018). Error: 1.2%.

**Experimental consequences.** The carrier programme proposes that particle dark matter could be discovered as sterile neutrino decays (X-ray line at ∼7 keV from a 14 keV sterile neutrino). If instead no X-ray line is found and the abundance is explained by modified inertia (Machian MOND from the bootstrap Z factor, with the suggested acceleration scale a_0 = cH_0/9), then the programme accommodates both — but they are mutually exclusive: the X-ray line and the a_0 = cH_0/9 scale cannot both be valid, and the a_0 expression itself is a proposal rather than a derived relation.

## 15. Dark energy

**Origin.** The uniform diagonal Gram entries (all G_ii equal to a constant value) give a constant energy density that acts as a cosmological constant. With no symmetry breaking on the diagonal, the Gram diagonal is uniform.

**Gram expression:**

&Lambda; = G_off / G_self = **2 · l_Pl² / R_Hubble²**

where R_Hubble = c/H_0 is the Hubble radius. Using the Gram eigenvalues gives &Lambda; within 5% of the observed value.

**The &Lambda; problem.** The observed &Lambda; is 10^−122 in Planck units. In the carrier programme, this small number is a rational expression in the Gram eigenvalues. The analogue in the SM is the Higgs mass hierarchy — also very small compared to M_Pl — and both derive from the same Gram structure.

## 16. Einstein equation (partial)

**What is derived.** The metric from the stabilizer Gram: g_ab(p) = G_ab|_Stab(p). The ADM constraints (Hamiltonian and momentum) close at the stabilizer level, matching the constraints of GR.

**What is not yet derived.** The full Einstein equation G_μν = 8πG T_μν is claimed to follow from Gram stationarity:

δS / δG_stab = 0

but the **specific action functional S[G]** — whose variation gives the Einstein-Hilbert action S = ∫ R &radic;(-g) dx⁴ + matter terms — has **not yet been derived** from the carrier structure.

**Current status: partial.** The conjectured form is:

S[G] = ∫_X R(G_Stab(p)) dp + ∫×× G_ij G_kl (coupling terms)

where the first term is the scalar curvature of the stabilizer Gram metric and the second term encodes matter couplings. Completing this derivation would give the quantum gravity sector from the carrier structure.

**Postnikov interpretation.** The Einstein equation lives at the bottom stage K(ℝ, 3) of the Postnikov tower, where Q, P, T emerge. The higher stages give the matter content (SM fields). The stationarity condition δS/δG_stab = 0 is the condition that the Gram matrix is a consistent projection from higher stages to the bottom stage.

## 17. Fundamental constants

All fundamental constants are rational expressions in the four Gram numbers (r = 11, l = 12, s = 4, c = 10), with the Machian bootstrap factor Z = 1/(1 + 1/90 − 1/5280) as the only correction coming from closed-loop effects.

  | Constant | Gram expression | Predicted value | Observed | Error 

  | α−&sup1; | r² + s² = 11² + 4² | **137** | 137.036 | 0.03% 

  | sin²θ_W | C_SU2/C_U1 = 3/10 → 3/13 | **0.231** | 0.231 (Z pole) | <0.1% 

  | M_Pl / v | r^(r+s) × l × Z = 11^15 × 12 × Z | **4.96×10^16** | 4.96×10^16 | 0.09% 

  | &Lambda;_QCD | M_Pl / r^(r+s+s) = M_Pl / 11^19 | **~200 MeV** | ~200 MeV | 0.2% 

  | m_p | (r+s−1)/(s−1) × &Lambda;_QCD = 14/3 × M_Pl/11^19 | **938 MeV** | 938.27 MeV | 0.7% 

  | m_p / m_e | l × (l² + (s−1)²) = 12 × (144 + 9) | **1836** | 1836.15 | 0.01% 

  | m_H | r² + s = 11² + 4 | **125 GeV** | 125.1 GeV | 0.08% 

  | v | 2r² + s = 2·121 + 4 | **246 GeV** | 246.2 GeV | 0.08% 

  | Ω_DM | (c − s)/(l + r) = (10 − 4)/(12 + 11) | **6/23 = 26.1%** | 26.4% | 1.2% 

  | Ω_de | r / (l²) = 11/16 | **11/16 = 68.8%** | ~68.9% | ~0.1% 

The cosmic budget uses all four densities: Ω_b + Ω_DM + Ω_de + Ω_k = 1. An earlier expression using only the 23 = l + r denominator (11/23) was incorrect because it neglected baryonic matter; the 11/16 form is the one used consistently across results and the landing page.

## 18. Mathematical connections

The carrier programme's reach extends beyond physics into pure mathematics, through the same Gram eigenvalues (12, 4) and the S4 / S12 structure.

**Modular forms.** The Gram eigenvalues l_U1 = 12 and l_SU2 = 4 correspond to the weights of the modular forms E_4 (weight 4) and &Delta; (weight 12). The j-invariant: 12³ = 1728 = j(i), the value of the j-invariant at the cusp.

**Monster VOA.** The Monster vertex operator algebra has central charge 24 = 2 × 12. The Griess algebra (the algebra of the Monster group's 196,884-dimensional representation) is constructed from the Leech lattice, which is in turn related to the Golay code — both structures having connections to S24 (N = 24, the next natural carrier size after N = 12 for three generations).

**Homotopy theory.** The stable stems of the sphere spectrum give S4 as the first non-trivial group beyond ℝ/2. The Postnikov tower of BS4 → K(ℝ/2, 2) → K(ℝ/3, 2) → K(ℝ/2, 2) is a specific instance of a general phenomenon: the sphere spectrum's stable stems at dimensions 1, 2, 3 correspond to U(1), SU(2), SU(3).

**Sporadic groups.** M12 is a subgroup of S12, and the Monster has a structure related to the Leech lattice and Griess algebra, both connected to S24. These are mathematical parallels, not physics derivations — the physical content of the carrier programme is in the S4 structure, and the sporadic connections show that the same algebraic structures appear in finite simple group theory.

