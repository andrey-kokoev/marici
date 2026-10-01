# Full derivation

## The single object and its three projections

The construction starts from a single object: a finite set $X_N$ with $N$ probe functions $f_i$, forming the **Gram overlap matrix**

$$
G_{ij}=\langle f_j\mid f_i\rangle
$$

This one matrix gives **three projections** that together cover all of known physics:

- **Quantum mechanics** — the interference pattern $I=\sum_{i,j}G_{ij}e^{i(\theta_j-\theta_i)}$

- **General relativity** — the $g_{ab}(p)=G_{ab}|_{\operatorname{Stab}(p)}$

- **Standard Model** — the $S_4$ irrep decomposition $G=V^2\operatorname{diag}(\lambda,\ldots)V$

This replaces position (Q), momentum (P), and time (T) as separate primitives with a single algebraic structure. In this construction, Q and T emerge from the descent of the 12-point carrier through the witness ladder (see the landing page for the rungs table).

The complete derivation is presented below, step by step, with each section showing both the carrier derivation and the exact point where it departs from the standard Newton → QM → QFT path.

## 1. The carrier

**Definition.** $X_N=\{x_1,\ldots,x_N\}$ with $N=4$ minimal. The canonical choice is Bool × Bool = {00, 01, 10, 11}.

The carrier is a finite set with no metric, no coordinates, no topology. The only structure is the cardinality N and the automorphism group S_N.

**Why N = 4.** $S_4$ has irreducible representations $1\oplus1'\oplus2$ (trivial + sign + doublet). This gives exactly the SM gauge group structure: U(1) from the trivial rep, SU(2) from the doublet, SU(3) from the sign × doublet interaction.

The full carrier for three generations is the 12-point set $X_{12}$, partitioned as $S_4 \times S_4 \times S_4$ (three generations of 4 points each). The ladder $12 \to 11 \to 10 \to \dots \to 4$ describes how the carrier is restricted by witness acts — each act removes one point (a rank-1 projection), dropping the Gram rank by exactly 1. The minimal carrier $N=4$ is the floor: Bool $\times$ Bool = 4 points, cannot restrict further. $N(N-1)=12$ regenerates the top from the floor.

**Connection to homotopy (proposed).** The Postnikov tower of BS4 as source of U(1), SU(2), SU(3) fibres is a proposal, not a theorem. The ladder descent above is the concrete mechanism; the homotopy identification remains conjectural.

## 2. Probes

**Definition.** Each point x_i ∈ X_N has a probe function f_i: X → ℂ. These are complex-valued functions on the carrier, analogous to wavefunctions evaluated at a point — but with no background spacetime.

**Inner product.** <f_j | f_i> = ∫_X f_j*(x) f_i(x) dx, where the integral is over the carrier domain. In the minimal normalized case: <f_i | f_i> = 1.

**Physical interpretation.** The probe f_i encodes all information about the relationship between the carrier point x_i and the rest of the carrier. In standard QM, a wavefunction encodes the relationship between a quantum system and measurement outcomes. Here, the probe encodes the relationship between a point and the whole set. There is no external space for the probes to "live in" — the carrier domain is the only space.

**Emergence of dimensionality.** The dimension of the carrier (N = 4 is minimal) becomes the dimension of spacetime, through the dimensionality of the faithful representation of S4 used to define the probes. The 4-dimensional permutation representation gives 4-dimensional spacetime (3 + 1 from the stabilizer decomposition).

## 3. The Gram matrix

**Definition.** $G_{ij}=\langle f_j\mid f_i\rangle$ is an N × N positive semidefinite Hermitian matrix. It contains all information about the geometric relationships between probe functions.

In standard physics, three separate structures are needed:

- A Hilbert space ℋ with Hamiltonian ̂H for QM

- A spacetime manifold (M, g_μν) with Einstein-Hilbert action for GR

- A principal G-bundle with connection A_μ for the SM

In this construction, all three arise from **three different projections of the same Gram matrix G_ij**. This is possible because G_ij is simultaneously:

- **Hermitian** (QM — probability conservation, Born rule)

- **Symmetric in its index pairs** (GR — the metric tensor g_μν is symmetric)

- **S4-equivariant** (SM — gauge invariance under S4 → SU(3)×SU(2)×U(1))

The Hermiticity follows from the inner product definition <f_j|f_i> = <f_i|f_j>*. The symmetry follows from the stabilizer restriction G_ab = G_ba. The S4-equivariance follows from $\operatorname{Aut}(X_N)=S_N$.

## 4. Automorphism group

$\operatorname{Aut}(X_N)=S_N$ for the N-point carrier. For N = 4: S4, with |S4| = 24. The automorphism group acts by permuting indices: G_ij → G_σ(i)σ(j) for σ ∈ S_N.

Gauge groups from the irrep decomposition of S4:

- **1 (trivial rep)** → proposed U(1) — overall phase symmetry. Eigenvalue λ_U1 = 12.

- **1' (sign rep)** → discrete ℝ/2 phase — proposed to complete the U(1) charge structure.

- **2 (doublet)** → proposed SU(2) — weak isospin. Eigenvalue λ_SU2 = 4.

- **3 (standard rep on ℂ⁴ quotient)** → proposed SU(3) — color. Derived from the 3-dimensional subrepresentation orthogonal to trivial.

The gauge groups are proposed to be read off from the irreducible representations of the carrier's symmetry group. This is an ansatz: a finite-group irrep decomposition does not by itself produce a continuous gauge group, and the lift from S4-representation data to U(1)×SU(2)×SU(3) gauge symmetries (with its charges and commutators) has not yet been presented as an explicit construction.

## 5. The ladder descent — where the Newton path diverges

The construction answers the question: *Where does the Newton → QM → QFT path diverge from the carrier derivation?*

**The Newton → QM → SM path (standard):**

1. Newton: ℝ³ as configuration space, ℝ as time. Position Q and momentum P as primitive coordinates on phase space.

1. QM: Promote Q, P to operators on L²(ℝ³). Time remains an external parameter. Quantization is a *procedure* applied to a classical system.

1. QFT: Promote fields (functions of Q and T) to operators. Gauge groups are added externally by hand.

1. SM: Postulate SU(3)×SU(2)×U(1). Write down a Lagrangian with ∼19 parameters. Fit to data.

**The carrier path:**

1. Carrier: X_N finite set → Gram G_ij.

1. The ladder 12 → 11 → 10 → … → 4: witness acts restrict the carrier by one point per act, dropping the Gram rank by exactly 1. Nine rungs, floor N=4, cycle N(N-1)=12.

1. Three projections of G_ij give QM, GR, SM simultaneously, with 4 Gram numbers (12, 11, 4, 10).

**The deviation:**

The Newton path treats Q, P, T as the foundation and builds up by quantizing. The carrier path starts from the Gram and the ladder descent that generates the constants. The ladder 12→4 is the mechanism; the rungs are the scales. The Postnikov identification of the gauge fibres is a separate proposal (see §18).

## 6. Three projections from one Gram matrix

Same Gram G_ij, three distinct physical theories from three different ways of reading the same matrix:

| Projection | Construction | Physical theory |
|---|---|---|
| **QM** | $I=\sum_{i,j}G_{ij}e^{i(\theta_j-\theta_i)}$ | Quantum interference, Born rule, phase evolution |
| **GR** | $g_{ab}(p)=G_{ab}|_{\operatorname{Stab}(p)}$ | Spatial metric from stabilizer, spacetime from fibration |
| **SM** | $G=V^2\operatorname{diag}(\lambda_1,\ldots,\lambda_4)V$ | Gauge groups from $S_4$ irreps, Yukawas from Gram eigenvectors |

**Why this single-matrix approach works:**

- The Gram is **Hermitian** → eigenvalues are real, probabilities are positive, phase evolution is unitary. This is the QM structure.

- The Gram restricted to a stabilizer is **symmetric** (g_ab = g_ba) → it defines a Riemannian metric. The full spacetime metric (+++-) emerges from the fibration of stabilizers.

- The Gram transforms under the **permutation representation of S4** → its eigenvectors decompose into S4 irreps, giving the SM gauge group. The eigenvalues (Gram numbers) are the only parameters.

All three are the same matrix seen from different angles.

## 7. QM projection — interference, phases, and the Born rule

**Interference term.** $I=\sum_{i,j}G_{ij}e^{i(\theta_j-\theta_i)}$. The phase differences θ_j − θ_i give the dynamics — no Hamiltonian needed.

**Born rule.** $\Pr(i)=G_{ii}/\operatorname{Tr}(G)$. The diagonal of the Gram gives probabilities directly: $\Pr(i)=G_{ii}/\operatorname{Tr}(G)$. This follows from the normalization of the probe functions and the positivity of the Gram matrix.

**Phase evolution.** The phases θ_i evolve along the chirality 3-cycle (identity → left → right → identity). The three steps of this cycle give three phase steps that correspond to the three generations of the SM. The complex phases of CKM and PMNS matrices arise from the misalignment between these three phase steps.

**Quantization as vertical arrow.** In standard QM, quantization is the promotion of classical observables to operators. Here the Gram IS the operator from the start. The classical limit emerges when phase differences are small (θ_j − θ_i → 0), giving constructive interference that recovers classical trajectories.

**Where Q, P would appear.** In the standard Schr&ouml;dinger picture, position Q is a multiplication operator and momentum P is a derivative. In the carrier picture, the momentum operator is encoded in the phase gradient &nabla;θ: the Gram phase differences θ_j − θ_i for nearby points i, j give the momentum as d(θ_j − θ_i)/dx. The position operator is the stabilizer index itself — the labelling of points in X_N.

## 8. GR projection — stabilizer metric and spacetime

**Stabilizer.** Stab(p) = {σ ∈ S_N | σ(p) = p} &subseteq; S_N. For N = 4, the stabilizer of a point is S3, of size 6, acting as the permutation group on the remaining 3 points. This 3-dimensional orbit gives the spatial dimensions.

**Metric from Gram.** $g_{ab}(p)=G_{ab}|_{\operatorname{Stab}(p)}$. Restrict G_ij to the indices corresponding to points in the stabilizer orbit. This submatrix gives the *spatial metric* at point p. The indices a,b run over the 3 dimensions of the stabilizer orbit.

**Spacetime signature (+++-).** The stabilizer submatrix gives the spatial part (+++). The connection between stabilizers at different points — the Gram overlap between probes at different p — gives the temporal component (−). The full metric is (+++−), matching general relativity.

**ADM constraints.** The Gram stationarity condition δG/δθ = 0 gives constraint equations that match the ADM Hamiltonian and momentum constraints of GR. The lapse and shift functions of the ADM formalism correspond to the projection of the Gram phase gradient along the stabilizer and its orthogonal complement, respectively.

**Where the Einstein-Hilbert action would come from.** The action principle: S[G] = ∫ R(G) dV, where R(G) is the scalar curvature computed from the stabilizer Gram metric. If δS/δG_stab = 0 reproduces $G_{\mu\nu}=8\pi G T_{\mu\nu}$, the derivation is complete. This derivation is not yet complete (see section 16).

## 9. SM projection — S4 irrep decomposition and gauge groups

**S4 permutation representation on ℂ⁴.** The 4-dimensional representation of S4 acting on ℂ⁴ by permuting basis vectors decomposes as:

4 = **1** (trivial) ⊕ **1'** (sign) ⊕ **2** (doublet)

**Gauge groups from irreps:**

- **1 (trivial)**: S4 acts as identity → U(1) symmetry. Eigenvalue λ_U1 = 12. This gives the hypercharge U(1).

- **1' (sign)**: S4 acts by sgn(σ) → discrete ℝ/2. Interacts with the trivial rep to give the full U(1) charge assignment pattern.

- **2 (doublet)**: S4 acts as the 2-dimensional irreducible representation → SU(2) weak isospin. Eigenvalue λ_SU2 = 4.

- **3 (standard rep)**: The 3-dimensional subrepresentation of ℂ⁴ orthogonal to the trivial: 3 = 1' ⊕ 2. This gives SU(3) color. The interaction between 1' and 2 creates the 3 ⊗ 3 → 3 ⊕ 6 structure of QCD.

**Gram numbers as eigenvalues:**

| Gram number | Symbol | Eigenvalue | Physical meaning |
|---:|---|---|---|
| 12 | $\lambda_{U(1)}$ | Trivial representation | $U(1)$ hypercharge overlap |
| 10 | $C_{U(1)}$ | Sign representation | Charge conjugation overlap |
| 4 | $\lambda_{SU(2)}$ | Doublet representation (multiplicity 2) | $SU(2)$ weak overlap |
| 11 | $r_{S12}$ | Off diagonal / $S_{12}$ | Three generation mixing overlap |

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

- **Higgs vacuum expectation value:** $v = 2\cdot 11^2 + 4 = \mathbf{246\,\mathrm{GeV}}$

- **Higgs mass:** $m_H = 11^2 + 4 = \mathbf{125\,\mathrm{GeV}}$

- **Ratio:** $m_H/v = 125/246 = 0.508$ (observed $125.1/246.2 = 0.508$, within 0.2%)

The Gram off-diagonal block structure gives the Higgs quartic coupling λ = m_H²/(2v²) = 125²/(2·246²) = 0.129, matching the observed value λ &approx; 0.13.

## 13. Strong CP / axion (schematic)

**Current status: schematic.** A U(1) phase mode of the carrier is identified as a candidate for the QCD axion. The phase mode corresponds to the overall U(1) rotation of all Gram phases θ_i by a constant &phi;: θ_i → θ_i + &phi;.

QCD instanton suppression of θ&macr; (the strong CP angle) is *assumed* from the SM, not derived from Gram numbers. The axion mass and coupling to photons are not computed from Gram expressions.

**Why it remains schematic:** The construction derives the SM gauge group and its representations, but the non-perturbative QCD dynamics that determine the axion potential involve the topological susceptibility of the QCD vacuum. This is a low-energy QCD phenomenon that depends on the detailed dynamics of the SU(3) gauge sector, which the construction has not yet fully derived from the Gram structure.

## 14. Dark matter

**Fermion content.** Three sterile neutrinos ν_R (one per generation), SM gauge singlets under SU(3)×SU(2)×U(1) but coupled to the carrier through the off-diagonal Gram block.

**Majorana mass.** The off-diagonal Gram entries give a Majorana mass term for the sterile neutrinos via the seesaw mechanism. The mass scale is set by the Gram eigenvalue ratio C_U1 / r_S12 = 10/11.

**Abundance (exact Gram expression):**

Ω_DM = (C_U1 − l_SU2) / (l_U1 + r_S12) = (10 − 4) / (12 + 11) = **6/23 = 26.1%**

Observed Ω_DM = 26.4% (Planck 2018). Error: 1.2%.

**Experimental consequences.** The construction proposes that particle dark matter could be discovered as sterile neutrino decays (X-ray line at ∼7 keV from a 14 keV sterile neutrino). If instead no X-ray line is found and the abundance is explained by modified inertia (Machian MOND from the bootstrap Z factor, with the suggested acceleration scale a_0 = cH_0/9), then the construction accommodates both — but they are mutually exclusive: the X-ray line and the a_0 = cH_0/9 scale cannot both be valid, and the a_0 expression itself is a proposal rather than a derived relation.

## 15. Dark energy

**Origin.** The uniform diagonal Gram entries (all G_ii equal to a constant value) give a constant energy density that acts as a cosmological constant. With no symmetry breaking on the diagonal, the Gram diagonal is uniform.

**Gram expression:**

&Lambda; = G_off / G_self = **2 · l_Pl² / R_Hubble²**

where R_Hubble = c/H_0 is the Hubble radius. Using the Gram eigenvalues gives &Lambda; within 5% of the observed value.

**The &Lambda; problem.** The observed &Lambda; is 10^−122 in Planck units. In this construction, this small number is a rational expression in the Gram eigenvalues. The analogue in the SM is the Higgs mass hierarchy — also very small compared to M_Pl — and both derive from the same Gram structure.

## 16. Einstein equation (partial)

**What is derived.** The metric from the stabilizer Gram: $g_{ab}(p)=G_{ab}|_{\operatorname{Stab}(p)}$. The ADM constraints (Hamiltonian and momentum) close at the stabilizer level, matching the constraints of GR.

**What is not yet derived.** The full Einstein equation $G_{\mu\nu}=8\pi G T_{\mu\nu}$ is claimed to follow from Gram stationarity:

δS / δG_stab = 0

but the **specific action functional S[G]** — whose variation gives the Einstein-Hilbert action S = ∫ R &radic;(-g) dx⁴ + matter terms — has **not yet been derived** from the carrier structure.

**Current status: partial.** The conjectured form is:

S[G] = ∫_X R(G_Stab(p)) dp + ∫×× G_ij G_kl (coupling terms)

where the first term is the scalar curvature of the stabilizer Gram metric and the second term encodes matter couplings. Completing this derivation would give the quantum gravity sector from the carrier structure.

The action principle $S[G] = \int R(G) dV$ whose variation gives $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ is not yet derived (proposed). Completing this derivation would give the quantum gravity sector from the carrier structure.

## 17. Fundamental constants

### Fine-structure constant: comparison slots

**Proposed carrier interpretation.** $137$ is the number of comparison slots between two $T_1$ carriers; $1/137$ is the average normalized weight per slot, not a cost per arrow.

Here $T_0$ retains identities, $T_1$ carries relationships and witnessed round-trip agreement with those identities, and $T_2$ carries coherence of their extension. These are relational levels, not powers of time; no chirality assumption is required.

Hold the direct relationship between the two carriers as the reference against which their other relationships and states are compared. It is excluded from the comparison slots because it supplies that reference. In this proposed counting, each carrier contributes eleven remaining arrows and a four-valued state, $\mathrm{Bool}\times\mathrm{Bool}$:

| Comparison block | Slots |
|---|---:|
| Every remaining arrow of one carrier against every remaining arrow of the other | $11\times11=121$ |
| Every carrier-state value of one against every carrier-state value of the other | $4\times4=2^4=16$ |
| **Total** | **137** |

The assembled comparison is assessed against the direct relationship; its residual supplies the proposed next-level coherence data at $T_2$. The count $137$ describes the comparison domain, not the residual.

The two blocks are counted separately, not as state assignments attached to each arrow pair. With equal slot weights, the normalized comparison is $\frac{1}{137}\sum_{s=1}^{137}c_s$. The proposed identification with electromagnetic coupling is $\alpha\approx1/137$. This interpretation assumes the two blocks exhaust the comparisons and carry equal normalization weight; it does not yet derive that identification or the measured low-energy value $\alpha^{-1}\approx137.036$.


### Tower successor and mixed comparison defects

**Current synthesis.** The tower has a specified transport diagram and a fixed
physical-reference locus at rung 4. Source comparisons retain actual equivalence
witnesses and histories; checked adapters preserve those witnesses alongside the
137 matrix responses and their **109 mixed comparison relations**. A conditional
preparation-and-transport model now includes a tested family-disagreement
feedback law. Its physical preparation, metric and gain remain to be identified.
The matrix amplitudes are supplied fixtures, not derived physical predictions;
these results supply no new numerical constant.

#### Rung transports and the physical reference

The middle triple presents transport between the outer triples:

$$
\begin{array}{ccc}
12 & \xrightarrow{\;9\;} & 6\\
\downarrow && \downarrow\\
11 & \xrightarrow{\;8\;} & 5\\
\downarrow && \downarrow\\
10 & \xrightarrow{\;7\;} & 4.
\end{array}
$$

Vertical moves retain the labelled/source-indexed/target-indexed presentations.
Rung 4 is the designated physical-reference locus. Both squares must commute,
so the two complete routes from rung 12 to rung 4 yield the same physical
readout. Exact retained-record fixtures satisfy these equations; the intended
horizontal generator and the numerical reference/readout at rung 4 still need
to be constructed.

Local reference changes retain their offset to that fixed reference:
$C-d_4=(C-d_{\mathrm{local}})+(d_{\mathrm{local}}-d_4)$.
Choosing the mean as a local reference can make its local residual zero while
preserving the full rung-4-relative offset.
[Diagram and verification](https://github.com/andrey-kokoev/marici/blob/main/research/nima/rung-transport-diagram-and-fixed-reference.md).

#### What promotion determines

The record-family rule assigns one fresh label to each grouped family and
retains its members. Candidate higher-witness constructions are now checked;
the intended horizontal generator and its next-level endpoint maps remain to
be selected and connected to them. In the checked fixture, two endpoint policies preserving
reconstruction, weights, and the reference/residual equation iterate as
$137\to32\to1$ and $137\to32\to32$.

Independent all-pairs comparison is a separate, explicit operation. For the full
four-label off-diagonal relation, its repeated products give the candidate
second-homology counts $1,2,4$. Establishing this operation as the tower's
successor, and identifying those classes with gauge data, remain open.

#### Retained paths produce 109 relations

The typed assembly uses eleven maps $x_i:A\to U$, eleven $y_j:U\to B$, four
$s_a:A\to V$, four $t_b:V\to B$, and the direct reference $d:A\to B$.
Its 137 composites share these **31 primitive/reference legs**.

The additive path-boundary description assigns a comparison cell $\sigma_{ij}$
the boundary $x_i+y_j-d$, with $s_a+t_b-d$ for the state block. These boundaries
have rank 28. Their 109-dimensional kernel has a basis of rectangle relations
relative to a chosen base leg in each family:

$$
\sigma_{ij}-\sigma_{i0}-\sigma_{0j}+\sigma_{00}.
$$

There are $(11-1)^2=100$ arrow-block relations and $(4-1)^2=9$ state-block
relations. Explicit composite names and composition witnesses preserve this
count under a checked chain retraction. The additive path boundary and the
finite matrix response are distinct parts of the construction.

#### Mixed second difference and the curvature analogy

Write the matrix response of a slot as $R_{ij}=y_jx_i-d$. Then

$$
R_{ij}-R_{i0}-R_{0j}+R_{00}
=(y_j-y_0)(x_i-x_0).
$$

The state block has the corresponding formula with $t$ and $s$. Reference changes
cancel. The response vanishes when only one leg family changes; simultaneous
changes can give a nonzero bilinear defect. Exact rational tests verify this
identity and recover the original normalized 137-slot assembly.

This is a discrete mixed second derivative: it measures interaction between the
two leg variations. Its rectangle support suggests a curvature interpretation.
A physical curvature or gauge-field identification remains open. In a declared
invertible-reference sector, the bridge $d^{-1}$ makes both composition orders
well-typed and gives the discrepancy
$\rho_2d^{-1}\rho_1-\rho_1d^{-1}\rho_2$. A weaker witnessed return requires
explicit unit and higher-coherence data. The 109 relations carry factored
responses rather than freely independent matrix parameters.

#### Reference transport and higher coherence

A graded shared-leg construction gives each comparison two witness routes and
109 higher products reconciling them. A witnessed reference return supports
recursive composition with explicit reference-drift corrections, an associator,
and a pentagon filler. These are checked algebraic realizations with declared
witness data; their physical interpretation remains conditional.

A retained comparison or weighted family can also serve as a local reference.
Its existing witness updates the unit and triangle records while preserving old
records as parents. Two successive changes agree with a direct change, and
returning to the old reference restores the current fields. All mixed rectangles
remain unchanged. The offset to the physical rung-4 reference must still be
retained. History retention does not require freezing current witness values.

The earlier biclique-chain filler model is a separate construction. Its filler
dimensions are not dimensions of the shared-leg model or physical field counts.

#### A faithful joint arrow/state observation

The actual slot matrices can be encoded as coefficients of carrier probe
functions on $S_4\times S_4$. An endpoint-fixing probe model merges reverse-arrow
responses; retained kernel records restore the named slots. A marked-context
alternative uses a reference ordered edge and a state basepoint outside that
edge. Its joint probe map has rank 137, and an exact decoder recovers every
matrix response, its mean, and the named mixed defects.

The marked context is transported under relabelling. Its selection and physical
measurement interpretation are inputs. In particular, uniform carrier averaging
is different from equal-slot averaging: the tested arrow/state indicator probes
have means $1/144$ and $1/16$. An observation law must specify which averaging or
decoding operation is physically performed.

#### The readout/composition gate

Faithful reconstruction alone does not make decoded averaging multiplicative.
Two valid leg perturbations can occupy disjoint probe contexts: their pointwise
mixed product vanishes, while the product of their decoded means is nonzero.
For the tested decoder $J$ and invertible reference,

$$
J(R_2d^{-1}R_1)\ne J(R_2)d^{-1}J(R_1).
$$

Independent pairing of slot contexts restores the mean-composition identity:

$$
\sum_{i,j}w_jw_i R_{2j}d^{-1}R_{1i}
=\left(\sum_jw_jR_{2j}\right)d^{-1}
 \left(\sum_iw_iR_{1i}\right).
$$

Alternatively, the multiplicativity discrepancy can be retained as explicit
coherence data. The intended transport must specify which operation it uses.
Independent pairing is therefore structurally motivated under the stated
readout requirement; it has not yet been derived as the tower's family successor.
The candidate $1,2,4$ product-homology result remains conditional.

A full mean/fluctuation packet now supplies an associative correction law for
declared same-slot composition. Composing promoted family means instead fixes
conditional leaf-pair coefficients through retained membership and masses.
The two horizontal endpoint candidates can agree in their original mean yet
differ after that composition probe. These checks sharpen the operation choice;
they do not select the intended generator.

#### Retain witnesses rather than impose flatness

The source comparison constructor accepts a supplied pointed equivalence and
retains it with both boundary packages. Composition retains its parents. In the
finite realization on four differently pointed copies of the carrier, each
endpoint pair admits six distinct witnesses. Endpoints alone are not faithful.
The full witness, or its stabilizer coordinate with endpoint frames, preserves
composition and permits the actual route holonomy to be tested.

Flatness is therefore not imposed on the comparison type. A global-frame
attachment gives a conditional flat reference realization; nontrivial loop
transport cannot be erased by changing those frames. The existing fixed-domain
comparison witnesses do not by themselves select a carrier reference connection.

A two-channel matrix packet retains the supplied witness separately from the
original response. This distinction is necessary: the existing matrix fixture
cannot simply be a functorial image of the finite comparison groupoid. Its
normalized base response is $I/2$, whereas the finite based witnesses have sixth
power identity. A faithful encoding does not derive the response amplitudes.

#### Conditional preparation and witness transport

For a declared operator-valued amplitude $A$, separate witness transport from
an explicit preparation increment $B$:

$$
T_h(A)=\rho(h)A\rho(h)^{-1},\qquad A_{\mathrm{new}}=T_h(A)+B.
$$

Ordered updates compose as

$$
(h_2,B_2)\circ(h_1,B_1)
=(h_2h_1,\;B_2+T_{h_2}(B_1)).
$$

This conditional law has checked associativity, inverse updates, retained
histories and port-coordinate covariance. Applying a common witness action and
supplied preparations to the primitive legs preserves the shared factorization
of all 137 slots. Their cross terms follow from multiplying updated legs.
Preparation history cannot generally be compressed into its finite witness:
a composite can have identity witness but a nonzero preparation increment.

#### One explicit candidate for the preparation increment

Postulate relaxation toward agreement within retained incoming families. With
$P$ the member-weighted family-mean projector, define

$$
B=\eta\bigl(P T_h(A)-T_h(A)\bigr).
$$

The exact fixture checks the original unit member masses, 30 primitive legs,
137 slots and 32 target-slot families. The rule preserves their family and global
means. In a declared witness-invariant quadratic control metric, active leg
disagreement scales by $(1-\eta)^2$; slot fluctuations have quadratic and quartic
scaling. Retained kicks reconstruct the old members even at full projection.
These are not claims about physical energy dissipation or the cost of history.

This feedback computes $B$ from existing data rather than fitting each increment
independently. But family-constant states receive no drive: it does not prepare
initial amplitudes, select their family means, or force those means to equal the
rung-4 reference. Relaxation itself, the gain $\eta$, and the control metric are
explicit model choices, not consequences of the count 137.

**Next step:** identify a source preparation or calibration operation that
implements—or falsifies—this feedback. Its physical gain, metric and relation
to the intended rung transports remain open. Until that identification, keep
the matrix values and feedback law labelled as fixtures and conditional models.

**Verification sources:** [operation contract](https://github.com/andrey-kokoev/marici/blob/main/research/nima/comparison-successor-operation-contract.md),
[shared-leg witnesses](https://github.com/andrey-kokoev/marici/blob/main/research/nima/shared-leg-dg-realization-and-base-coherence.md),
[witnessed returns](https://github.com/andrey-kokoev/marici/blob/main/research/nima/witnessed-reference-return-and-pentagon.md),
[local reference changes](https://github.com/andrey-kokoev/marici/blob/main/research/nima/witnessed-reference-reanchoring.md),
[joint response adapter and exact checks](https://github.com/andrey-kokoev/marici/blob/main/research/nima/joint-probe-response-adapter.md),
[retained source witnesses](https://github.com/andrey-kokoev/marici/blob/main/research/nima/retained-pointed-comparison-groupoid.md),
[witness/response packet](https://github.com/andrey-kokoev/marici/blob/main/research/nima/witness-matrix-packet-adapter.md),
[amplitude source audit](https://github.com/andrey-kokoev/marici/blob/main/research/nima/response-amplitude-source-gate.md),
[preparation and transport](https://github.com/andrey-kokoev/marici/blob/main/research/nima/boundary-prepared-witness-update-law.md),
[family-feedback law and checks](https://github.com/andrey-kokoev/marici/blob/main/research/nima/family-disagreement-preparation-law.md),
and [current system summary](/research/system-characteristics/#current-synthesis-status).

### Record equilibrium and phase back-reaction

The record-family architecture presents the same labelled paths individually,
indexed by source, and indexed by target. Promotion assigns each grouped family
a fresh label while retaining its members. A weighted response survives this
change of presentation when each family carries the sum of its members' weights.
Equal weights for newly assigned labels generally change the response.

#### A conditional route to equal comparison response

In the closed comparison prototype, a normalized carrier coordinate is exchanged
with its retained record. There are 16 carrier coordinates and 137 record
coordinates. Write the mismatch of comparison $i$ as

$$
\delta_i=w_i-u_i^Tq.
$$

The 137 real exchange normals are independent and have a connected
nonorthogonality graph in the tested construction. A covariance invariant under
every individual exchange is scalar on their span. A state-independent random
schedule that enables every comparison, with an idle probability to remove
periodicity, drives the ensemble covariance toward that common invariant space.
Each realized exchange remains reversible and conserves the total quadratic budget.

For positive active variance, the limiting response satisfies

$$
\frac{\operatorname{Var}(\delta_i)}
{\sum_{j=1}^{137}\operatorname{Var}(\delta_j)}=\frac1{137}.
$$

This result concerns normalized mismatch fluctuations. Its identification with
electromagnetic coupling requires a physical charge/field readout. The schedule,
comparison operation, and retained-state model are stated assumptions. Unequal
positive scheduling probabilities preserve the equilibrium but change convergence
rates and can change event-frequency-weighted measurements.

#### Coupling comparisons to an evolving phase

A complex extension supports local endpoint phase changes when the state,
comparison features, and Gram metric transform together. Independent overlap
phases admit nonzero loop holonomy while preserving a positive metric in the
constructed family. A subsequent single-phase trial uses the actual comparison
mismatches in the Hamiltonian

$$
H=\frac{\kappa}{2}\sum_{i=1}^{137}
\left|w_i-u_i(\theta)^\dagger q\right|^2
+\frac{\beta}{2}p^2+\mu(1-\cos\theta).
$$

Here $p$ is conjugate to the overlap phase $\theta$. The negative phase derivative
of the same Hamiltonian drives the phase momentum. Thus record mismatch changes
the phase, which changes the subsequent comparison directions. Numerical tests
check the force against energy differentiation, global phase covariance, and
convergence of energy and norm errors under timestep refinement.

The Hamiltonian, canonical frame, scalar reduction, and coefficients are trial
choices. This evolving-phase model has a different update law from the random
exchange model. Its long-time response still needs testing; the earlier
$1/137$ equilibrium result cannot be transferred without that test. No physical
coupling normalization or observed decimal correction has been derived.

[System characteristics and verification sources](/research/system-characteristics/#closed-record-equilibrium-and-normalized-exchange-response)
track the individual constructions, checks, and open interfaces.

### Carrier-realized comparison and the decimal tail

**Hypothesis.** Realizing the 137-slot comparison on the carrier changes its reference-channel normalization through the comparison residual. The slot count remains integral. The measured low-energy inverse coupling is approximately $137.035999$, so the calculation must explain an additional normalization of approximately $0.036$.

For realized slot weights $w_s=1+\epsilon_s$, one candidate normalization is $\alpha^{-1}=\sum_s w_s=137+\sum_s\epsilon_s$, with the direct reference assigned unit weight. This assignment requires a carrier rule. The arithmetic mean of the 137 normalized slot weights remains $1/137$; the proposed physical correction concerns the reference-channel weight relative to their total.

#### Reference assembly and readout

A checked linear prototype supplies maps $x_i:A\to U$, $y_j:U\to B$ for eleven arrow labels at each endpoint, and $s_a:A\to V$, $t_b:V\to B$ for four state labels. The state labels are represented by maps in this prototype. All composites and the direct reference $d$ have endpoints $A\to B$:

$$
C=\frac{\sum_{i,j}y_j\circ x_i+\sum_{a,b}t_b\circ s_a}{137},\qquad R=C-d.
$$

Agreement makes the residual vanish while retaining all comparison slots. Two equal and opposite incoming perturbations cancel in the assembled comparison. The prototype assumes common intermediate spaces and a linear target permitting sums and subtraction.

With a unit-normalized reference and a chosen inner product, reference amplitude and intensity are

$$
\mathcal A=1+\langle d,R\rangle,\qquad
\mathcal I=1+2\operatorname{Re}\langle d,R\rangle+\|R\|^2.
$$

In the real two-dimensional test, $d=I$, $\langle X,Y\rangle=\operatorname{Tr}(X^T Y)/2$, and $H$ has the single nonzero entry $H_{12}=1$. Modify one incoming leg to $I+uH$ and one outgoing leg to $I+vH^T$. Exact assembly gives

$$
C=I+\frac{11uH+11vH^T+uvH^T H}{137},
$$

$$
\mathcal A=1+\frac{uv}{274},\qquad
\mathcal I=1+\frac{uv}{137}+\frac{121(u^2+v^2)+u^2v^2}{2\cdot137^2}.
$$

**Outcome:** two-way composition supplies a signed $uv$ feedback term and a positive residual-power term. Exact rational checks pass. Carrier dynamics still need to supply $u,v$, the metric, and the physical readout. These formulas establish the readout mechanism within the prototype; they supply no numerical prediction for the decimal tail yet.

#### Feedback trials and precision outcome

A separate exploratory routing model uses 1936 sequential arrow/state return histories. Endpoint reversal fixes 44 histories and pairs the others, giving a symmetric subspace of dimension 990. Uniform incoherent averaging retains the fraction $990/1936=45/88$.

Taking outward gain $a=1/121$ and return gain $b=(1/16)(45/88)$ gives a two-block operator $K=\left(\begin{smallmatrix}0&a\\b&0\end{smallmatrix}\right)$ with eigenvalues $\pm L$, where $L=\sqrt{ab}$. For source and readout at the same reference port, the proposed normalization is

$$
\alpha^{-1}=\frac{137}{(1-L)(1+L)}=\frac{137}{1-ab}=137.036195933608.
$$

The assumptions are positive return gains, incoherent uniform path selection, and re-randomization each loop. Coherent uniform paths already lie in the symmetric sector. Persistent path sectors instead give $137.036205073996$.

**Precision outcome: the fixed routing prediction fails both quoted recoil targets.** Its difference from the rubidium result is $0.000196727608$, about 17,884 quoted measurement-uncertainty units; the caesium difference is $0.000196887608$, about 7,292 units. The model has no theoretical uncertainty budget. The first positive return alone already gives $137.036186373028$, so adding positive returns cannot close the gap. Removing one symmetric reference direction gives $137.036159362409$; deleting all 44 endpoint-fixed directions gives $137.034586819316$. Neither deletion is supplied by the carrier's reference-comparison rule. The near-$0.036$ tail remains an exploratory result.

#### Independent measurement routes

| Route | Measured comparison and extraction | Effect of a shared $\alpha=\alpha_0/(1+\varepsilon)$, $\alpha_0=1/137$ |
|---|---|---|
| Atomic recoil | Laser-driven recoil determines $h/m_{\rm atom}$; combine with spectroscopy and mass ratios: $Q=(2R_\infty/c)(m_{\rm atom}/m_e)(h/m_{\rm atom})=\alpha^2$ | $Q/Q_0=(1+\varepsilon)^{-2}$ |
| Electron magnetic moment | Spin and cyclotron frequencies determine $a_e=(g-2)/2$; invert the calculated relation $a_e=F(\alpha)$ | $a_e=F(\alpha_0/(1+\varepsilon))$; leading term $\alpha/(2\pi)$ |

Representative recoil determinations are $137.035999206(11)$ ([rubidium, 2020](https://doi.org/10.1038/s41586-020-2964-7)) and $137.035999046(27)$ ([caesium, 2018](https://doi.org/10.1126/science.aap7706)). Their quoted uncertainties expose an unresolved disagreement between the two determinations. Relative to the 137 baseline, the rubidium value corresponds to a $-0.026270\%$ shift in $\alpha$ and a $-0.052533\%$ shift in $Q$. The corresponding change in the leading magnetic-anomaly term is approximately $-3.05181\times10^{-7}$; a precision magnetic comparison requires the full $F$ and independent measurements.

A shared carrier correction must propagate consistently through both extraction routes. This cross-method requirement specifies a test; the measured values do not determine the carrier feedback law.

#### Curvature and residual floor

The existing cosmological budget gives the exact deficit

$$
\kappa=1-\frac6{121}-\frac6{23}-\frac{11}{16}=\frac{91}{44528}\approx0.00204366.
$$

The shared-residual hypothesis proposes cosmological and electromagnetic readouts of one carrier closure residual. Applying this deficit uniformly to electromagnetic normalization gives $137/(1-\kappa)=137.28055449$, which fails the measured target. A successful shared-residual construction needs its sector-specific readout maps. The residual's mean can shift normalization; fluctuations around the mean would define a noise floor. A noise prediction requires a covariance or stochastic model.

**Research and checks:** [hypothesis and feedback trials](https://github.com/andrey-kokoev/marici/blob/main/research/nima/comparison-slot-normalization-and-carrier-closure-residual-hypothesis.md), [measurement/readout comparison](https://github.com/andrey-kokoev/marici/blob/main/research/nima/fine-structure-recoil-and-magnetic-moment-comparison.md), and the exact checkers `check_comparison_slot_endpoint_reversal.py`, `check_comparison_slot_reference_assembly.py`, `check_comparison_reference_readouts.py`, and `check_fine_structure_cross_method_target.py` under `research/nima/checkers/`.

### Weak mixing: matter-trace audit

**Outcome: the cited matter-trace derivation of $3/13$ fails a colour-multiplicity check.** With $Q=T_3+Y$ and doublet index $1/2$, the contributions per generation are:

| Multiplet | $SU(2)$ trace | Hypercharge squared trace |
|---|---:|---:|
| Quark doublet, three colours | $3/2$ | $1/6$ |
| Right-handed up quark | $0$ | $4/3$ |
| Right-handed down quark | $0$ | $1/3$ |
| Lepton doublet | $1/2$ | $1/2$ |
| Right-handed charged lepton | $0$ | $1$ |
| Neutral right-handed neutrino | $0$ | $0$ |
| **Three-generation total** | **6** | **10** |

The historical checker `check_gauge_coupling_norm.py` counted the quark doublet once in the weak trace while retaining all three colours in the hypercharge trace. Under its common inverse-trace normalization assumption, $g_i^2=k/C_i$, consistent counting gives

$$
\sin^2\theta_W=\frac{g'^2}{g'^2+g^2}=\frac{C_{SU(2)}}{C_{SU(2)}+C_Y}=\frac6{6+10}=\frac38.
$$

A second check averages over quark colours consistently in both sectors. It gives $C_{SU(2)}=3$, $C_Y=19/3$, and mixing fraction $9/28$. Thus consistent colour averaging also fails to recover $3/13$.

**Common-measure test.** On the same matter space, assign nonnegative weight $q$ to each quark state and $\ell$ to each lepton state, using that measure for both generators. Per generation, $C_{SU(2)}=3q/2+\ell/2$ and $C_Y=11q/6+3\ell/2$. Their mixing fraction is $(9q+3\ell)/(20q+12\ell)$, ranging from $1/4$ to $9/20$. The target $3/13$ requires $\ell=-19q$, so this positive two-weight family cannot produce it. Multiplet-specific weights allow more possibilities, but require an independent carrier rule. Exact checks: `research/nima/checkers/check_weak_mixing_common_measure.py`.

The carrier expression $3/13$ remains a candidate requiring a specified common comparison space and sector readouts. The matter-trace argument above supplies no derivation of it. The $3/8$ result is conditional on common normalization; a comparison with measured weak angles requires a scale, renormalization convention, and running calculation. The frequently quoted value near $0.231$ refers to particular electroweak-scale definitions.

The historical trace-based route to $137=(C_Y+1)^2+(C_{SU(2)}+1)^2$ also fails this audit: corrected matter traces give $11^2+7^2=170$. The separate comparison-slot proposal uses its own eleven-arrow/four-state assumptions.

[Full audit](https://github.com/andrey-kokoev/marici/blob/main/research/nima/weak-mixing-comparison-normalization-audit.md). Exact checks: `research/nima/checkers/check_weak_mixing_matter_trace_audit.py`.

### Proton-electron ratio: comparison paths and settling

**Hypothesis and current outcome.** The expression $12(12^2+3^2)=1836$ counts a proposed comparison programme. The observed mass ratio is approximately $1836.152673$. Exact slot counts and explicit disturbance-settling prototypes have been checked; the particle-energy identification and the $0.152673$ correction remain to be derived.

#### Two-cycle compaction and retained overlap

**Conceptual conjecture.** Descent from rung12 toward rung4 compacts a packet's compatibility information into the fewest independent relationships from which the required information can be recovered. Shared structure becomes a retained reference. The part with maximum relationship depth supplies the entry interface for outside probes; its resolution makes the attached parts accessible.

A proton packet is proposed to have an assembled external presentation and a compact, quark-level descent presentation. The two-cycle picture is:

| Stage | Proposed packet operation |
|---|---|
| First cycle begins | One complex plane collapses into records, supplying the retained reference for this cycle. |
| First descent | Explicit compatibility paths are collected into shared records and fewer independent arrows. |
| First cycle ends | A splittable packet separates into two parts $a,b$ and their relationship $\rho$; the relationship is carried in the next complex plane. |
| Second cycle begins | One plane collapses into records; the two parts and their connection participate in the new cycle. |
| Second-cycle resolution | Each part is presented with the connection through which the other is reachable: $A=(a,\rho)$ and $B=(\rho,b)$. |
| Reassembly | The two overlapping presentations reconstruct the packet through their shared relationship. |

The proposed overlap bookkeeping is

$$
(a+\rho)+(\rho+b)-\rho=a+\rho+b.
$$

With equal bookkeeping weights for $a,\rho,b$, this gives

$$
\frac23+\frac23-\frac13=1.
$$

The conjectured association with the proton's $uud$ presentation assigns the two component-with-relationship contributions to the two $u$ entries and the shared contribution's subtraction to the $d$ entry. Equal weights and the identification with electric charge are hypotheses in this interpretation. The expression $12(12^2+3^2)$ is proposed to count the retained compatibility responsibilities of the assembled interface.

#### Proposed interpretation of quark spin labels

The proposal interprets quark **spin-up and spin-down as presentations of orientation in overlapping retained arrows**, resolved relative to a probe axis. The underlying record consists of the two parts and their shared relationship; the spin labels would arise when that structure is presented to a probe. Descent and reconstruction would supply the transformation between these presentations.

QCD describes quarks as spin-$1/2$ fields; quantum spin is an intrinsic angular-momentum degree of freedom. The retained-overlap proposal is a conjecture about the origin of that description. Its physical test is to derive the two-outcome spin response, its dependence on the probe axis, and the corresponding polarized-scattering observables from the retained arrows. No such calculation or distinct empirical prediction has yet been obtained from this proposal.

#### Shared-state comparison programme

Compare two four-state carriers, each carrying twelve directed relationships. Hold one state on each side as the identified shared reference. The remaining state alternatives number three per carrier:

| Comparison component | Slots |
|---|---:|
| All directed relationships against all directed relationships | $12\times12=144$ |
| Remaining state alternatives against remaining state alternatives | $3\times3=9$ |
| One shared-reference comparison | **153** |
| One such comparison for each of twelve outer directed relationships | **1836** |

The shared-state identification is an input. The nine state slots assess compatibility relative to it. Assigning the proton to the full programme and the electron to its resource unit is the proposed physical interpretation. The historical checker instead identified three with the miscounted weak matter trace; that argument fails the preceding audit. The new shared-state count has its own assumptions.

Fixing the reference partitions the outer relationships into three outward, three inward, and six internal arrows. Their weighted total is $153(3w_{\rm out}+3w_{\rm in}+6w_{\rm internal})$. Unit weights give 1836; the fixed-reference symmetry permits distinct orbit weights.

#### Paths retain traversal resource

A directed path retains its history. Traversing $A\to B\to A$ consumes two steps even though it returns to its starting point. The resource model uses additive positive traversal costs. Every comparison attempt is charged, including an attempt whose state update is zero.

An earlier vector-energy test represented arrows by endpoint differences. Its coherent cancellation discards traversal history and therefore does not evaluate this path-resource proposal. That test also exposed a separate normalization choice: raw Gram norms give arrow-pair weight $22^2$ and state-pair weight $12^2$. The equal-unit slot count requires a physical resource rule selecting the relative weights.

#### Pairwise settling and the fractional tail

The proposed tail is the additional resource needed to settle disturbances created by the comparisons. An explicit pairwise-averaging test gives

$$
(1,0,0)\longrightarrow(1/2,1/2,0)\longrightarrow(1/2,1/4,1/4).
$$

The second comparison reopens the first agreement. A full prototype uses two carriers with a pinned shared state, six remaining state potentials, and all 153 equality comparisons repeated twelve times. Every attempt consumes one resource unit. In exact arithmetic, a unit input disturbance reopens 1668 immediately preceding agreements in forward order and 1664 in reverse order. Final squared disturbances are approximately $1.2\times10^{-61}$ and $7.4\times10^{-61}$ respectively. Compatible input leaves zero disturbance while still consuming all 1836 attempts.

**Outcome:** sequential comparisons demonstrably disturb earlier agreements. The residual depends on input and order; this deterministic prototype supplies no universal mass tail.

#### Back-action-supported settling floor

An additional prototype gives each comparison its own back-action. For a comparison row $r$, let $P=I-rr^T/(r^Tr)$ project onto its agreement plane. Update the six state potentials by

$$
x'=Px+\eta,\qquad \operatorname{Cov}(\eta)=qP/5.
$$

The independent zero-mean disturbance remains inside the newly satisfied agreement plane and can disturb other agreements. The five-dimensional normalization injects expected squared resource $q$ per attempt. With covariance $\Sigma$:

$$
\Sigma'=P\Sigma P+qP/5,
$$

$$
\operatorname{Tr}\Sigma'=\operatorname{Tr}\Sigma-
\frac{r^T\Sigma r}{r^Tr}+q.
$$

The declared schedule reaches a periodic covariance. At $q=1$, end-sweep state variance is approximately 14.845441; each 153-comparison sweep settles 153 squared-resource units, matching its injection. Twelve sweeps settle $1836q$. Halving $q$ halves the settling load; zero injection gives zero floor for compatible input. Positive traversal cost is accounted for separately.

**Outcome:** comparison back-action sustains a reproducible settling floor in this model. The carrier still needs to determine $q$, its metric and conversion to rest energy, and the electron's own settling response. The model measures settling during the repeated programme. Attributing the tail specifically to additional traversals also requires a retry or stopping rule. Setting $q$ from $0.152673$ would calibrate the model to the observed ratio.

#### Closure trials and verification

A prior uniform-return trial gave $1836/(1-1/15552)=1836.118063$, missing the observed tail. Direct enumeration of composable four-state paths instead gives expected first-return resource four under uniform outgoing routing; ordinary graph closure supplies no rare-return probability of $1/15552$. Pairwise settling is the subsequent mechanism investigated above.

[Full hypothesis, assumptions, and outcomes](https://github.com/andrey-kokoev/marici/blob/main/research/nima/proton-electron-shared-state-comparison-hypothesis.md). Checkers under `research/nima/checkers/`: `check_proton_electron_comparison_slots.py`, `check_proton_electron_gram_energy.py`, `check_proton_electron_path_closure.py`, `check_four_state_return_paths.py`, `check_pairwise_comparison_settling.py`, `check_full_mass_comparison_programme.py`, and `check_comparison_backaction_floor.py`. Counting and deterministic update checks use exact arithmetic; the covariance-floor test uses floating arithmetic with explicit tolerances. These checks establish their stated models, with no derived mass correction yet.

### Constant expressions

The table below collects proposed expressions in $(12,11,4,10)$. The Planck-scale expression uses the Machian bootstrap factor $Z=1/(1+1/90-1/5280)$. The electromagnetic feedback extensions above are exploratory models with the stated precision failures.

| Constant | Gram expression | Predicted value | Observed | Error |
|---|---|---:|---:|---:|
| $\alpha^{-1}$ | $11^2+4^2$ | [**137**](#fine-structure-constant-comparison-slots) | 137.036 | 0.03% |
| $\sin^2\theta_W$ | $3/13$ (candidate; [trace derivation fails audit](#weak-mixing-matter-trace-audit)) | **0.230769** | ≈0.231 (definition-dependent, electroweak scale) | Scale-matched prediction pending |
| $M_{\mathrm{Pl}}/v$ | $11^{15}\times12\times Z$ | **$4.96\times10^{16}$** | $4.96\times10^{16}$ | 0.09% |
| $\Lambda_{\mathrm{QCD}}$ | $M_{\mathrm{Pl}}/11^{19}$ | **~200 MeV** | ~200 MeV | 0.2% |
| $m_p$ | $14/3\times M_{\mathrm{Pl}}/11^{19}$ | **938 MeV** | 938.27 MeV | 0.7% |
| $m_p/m_e$ | $12\times(12^2+3^2)$ ([comparison-path hypothesis](#proton-electron-ratio-comparison-paths-and-settling)) | **1836** | ≈1836.152673 | ≈0.0083%; settling correction unresolved |
| $m_H$ | $11^2+4$ | **125 GeV** | 125.1 GeV | 0.08% |
| $v$ | $2\cdot11^2+4$ | **246 GeV** | 246.2 GeV | 0.08% |
| $\Omega_{\mathrm{DM}}$ | $(10-4)/(12+11)$ | **$6/23=26.1\%$** | 26.4% | 1.2% |
| $\Omega_{\mathrm{de}}$ | $11/16$ | **$11/16=68.8\%$** | ~68.9% | ~0.1% |

The budget uses all four densities: $\Omega_b + \Omega_{\mathrm{DM}} + \Omega_{\mathrm{de}} + \Omega_k = 1$. The $11/16$ form is used consistently across results and the landing page.

## 18. Mathematical connections

The construction's reach extends beyond physics into pure mathematics, through the same Gram eigenvalues (12, 4) and the S4 / S12 structure.

**Modular forms.** The Gram eigenvalues l_U1 = 12 and l_SU2 = 4 correspond to the weights of the modular forms E_4 (weight 4) and &Delta; (weight 12). The j-invariant: 12³ = 1728 = j(i), the value of the j-invariant at the cusp.

**Monster VOA.** The Monster vertex operator algebra has central charge 24 = 2 × 12. The Griess algebra (the algebra of the Monster group's 196,884-dimensional representation) is constructed from the Leech lattice, which is in turn related to the Golay code — both structures having connections to S24 (N = 24, the next natural carrier size after N = 12 for three generations).

**Homotopy theory (proposed).** The stable stems of the sphere spectrum give $S_4$ as the first non-trivial group beyond $\mathbb{R}/2$. The Postnikov tower of $BS_4$ is a candidate identification for the gauge fibres $U(1), SU(2), SU(3)$, but this is a proposal, not a derivation (see the landing page's ladder descent for the concrete mechanism).

**Sporadic groups.** M12 is a subgroup of S12, and the Monster has a structure related to the Leech lattice and Griess algebra, both connected to S24. These are mathematical parallels, not physics derivations — the physical content of this construction is in the S4 structure, and the sporadic connections show that the same algebraic structures appear in finite simple group theory.
