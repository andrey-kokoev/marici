# Theory: constructions and verification boundaries

Use this page for explanations and definitions. [Architecture](/research/system-characteristics/) records construction contracts; [Results](/research/results/) summarizes checks, exclusions, and open tests.

This page develops specified mathematical constructions and keeps their proposed physical interpretations separate. Exact identities, finite checks, kernel proofs, written analytic arguments, and experimental acceptance are different evidence levels. Verification statements below summarize the linked research; this page is not a new proof certificate.

## Recent constructive results and exclusions

### Analytic return: same witness, different verification levels

The standard-complex construction uses the same source-linearized operators $H_j=\pi(I-P_j)/2$ and $U_j(t)=\exp(-itH_j)$ for local motion and whole-record return. Two reversed-order unitary pieces glue continuously on $[0,2]$, return to the source basis vector, and distinguish the retained schedule tags by their seam states. Reconstruction and schedule exchange respect the whole retained record. The all-time result is a **written analytic proof**, supported by exact finite checks and the Agda source-classification theorem; samples alone do not prove it. No derivative at the switching seam or Cubical-pointwise state decoding is claimed. [Whole-return proof](../research/nima/spectral-whole-return-proof.md).

Separately, the operational completion development reports fresh safe Agda closure for unit norm, all-scale continuity and derivative, unit-circle flow, and the assembled half-turn of the same operational phase. Its identification with **standard pi** uses an explicitly accepted written proof, not a kernel-checked ordinary-real interpretation. Operational complex/tensor whole-return assembly is still the unresolved goal in the cited net. The written standard-complex result must not be silently promoted to an operational certificate. [Assembled half-turn](../research/nima/constructed-unitary-half-turn.md) · [current completion frontier](../research/nima/completion-refinement-conjecture-net.md).

### A fixed-carrier restriction law

For the declared fixed-point probes on $S_{12}$, one normalization gives $G_{12}=10I+J$. Restriction inside that same probe space gives $G_r=10I_r+J_r$, with coefficient-Gram eigenvalues $r+10$ and 10. The correct orthogonal projection from rung $r$ has $y_i=x_i+x_r/(r+9)$, not coordinate deletion; the removed squared norm is $10(r+10)x_r^2/(r+9)$. Nested projections compose and the retained-plus-record norm budget is conserved.

The mean fraction $r/12$ requires metric-isotropic inputs and an additional norm-to-energy law. Rebuilding probes on a different $S_r$ is a different carrier construction. Neither route supplies a Hamiltonian, physical energy decay, particle identity, or the four-number spectrum $(12,11,4,10)$. [Exact restriction tower and checker](../research/nima/carrier-gram-restriction-tower.md).

### Common geometry and conditional quantum dynamics

A common orbit/facet/cone constructor takes declared rational metrics, proper affine isometries, seeds, and interface roles. Independent exact comparison recovers the tetrahedron, six-panel belt, and pentachoron: respectively four, six, and five admitted coarse cones. The belt's cap exclusions and gap are source data. The electron cones subdivide a filled four-simplex rather than giving five disjoint spatial volumes. This reconstructs specified geometry and interfaces, not arrow-only minimality, a coefficient protocol, or physical particles. [Source constructor and sensitivity controls](../research/voevodsky/relative-geometric-source-constructor.md).

A separate conditional spinor quantization has an ideal endpoint-rotor parent unitarily equivalent to its reduced Hamiltonian. Its four conserved-flux blocks form an exact invariant **16-dimensional** subspace containing the global ground and first excited energy. This is a concrete finite simulation target, not the full rotor theory or a realized device. A platform, physical charging metric, assisted transfers, preparation fidelity, and measured error budget remain required. Exact endpoint factorization is not finite-stiffness pinning of independent continuous links. [Quantum construction and physical acceptance contract](../research/voevodsky/spinor-quantum-implementation.md).

### Energy and interaction: explicit excluded branches

- **Common charging mass law:** the shared one-gap law gives $E_e=1-d$, $E_p=1836-d$, and $E_b=1836+e_b$ with $-d\le e_b<0$ and $d<1$. Thus the splitting in elementary-energy units is at most $(E_p/E_e-1836)/1835$. Matching the retained proton/electron reference permits only about **42.5 eV**, not the approximately **1.293 MeV** splitting target. No common coupling or clock rescaling repairs these simultaneous comparisons. This excludes the specified shared charging/displacement branch, not every mass model. [General bound and assumptions](../research/voevodsky/common-charging-mass-closure.md).
- **Deuterium in the current graph:** tensor-lifted rim maps solve the scalar/spinor type mismatch, but do not select a charged constituent interaction. Pair-minus-breakup energy is positive with independent exterior reservoirs and zero with the same total reservoir. The graph supplies neither attraction nor separation-dependent nuclear binding. A new bounded, number- and charge-preserving cross-carrier interaction must use identical comparison boundaries. [Typed rim and breakup test](../research/voevodsky/deuterium-typed-rim-and-breakup-test.md).
- **Compatibility as a sufficient selector:** the tested quantum-state completion preserves every admissible annotation and all its record probabilities; forgetting it recovers the original model. Prediction sets therefore remain equal. Intermediate tensor locality would be an additional selector, not a consequence already present in that test class. Maps joining the distinct spatial, flavor, and gravity sources remain unspecified. [Completion result and falsifiers](../research/nima/joint-compatibility-free-completion-result.md).
- **Braid topology as an amplitude law:** preserving one attachment restricts endpoint multiplicity to two or three components. It does not fix their probabilities. The separate two-channel Hamiltonian retains free coupling, splitting, and duration; **372:1 is an input constraint**, not a prediction. A sourced braid representation and amplitude assignment remain missing. [Constructive composition model](../research/figueiredo/braid-constrained-two-channel-composition.md).

### Storage: constructive resources, not free apparatus

The exact error-transparent pair pulse has **769 Pauli terms**, including weights six, eight, and ten. Pauli-basis uniqueness excludes a direct implementation using only one- and two-body terms on the same code qubits; ancillas, gadgets, or different encodings are not ruled out. Dropping the high-body component terms fails all fifteen nonzero single-error sectors even when clean-code action is preserved.

In the alternative finite-work route, a sine-profile packet optimizes the specified midpoint-fault fidelity at fixed ladder size, giving $[1+\cos(\pi/(M+1))]/2$. This is not a channel-wide or arbitrary-fault-time optimum: another tested input becomes worse at $M=4$. Packet preparation, a physical clock, and microscopic bath/recovery dynamics remain resources to construct. [Exact branch comparison and controls](../research/voevodsky/storage-branch-comparison.md).

The constructive results survive within their contracts; the exclusions require genuinely new source-supported selectors or interactions, not relabelling a count as energy or fitting an observed deficit. See the [public results and comparison targets](/research/results/). The legacy discussions below should be read within these boundaries.

## Witness Generator (glossary)

For a state type $S$ and a declared witness relation $R:S\to S\to\mathsf{Type}$, a **Witness Generator** (WG) has type

$$G_R:\prod_{s:S}\sum_{t:S}R(s,t).$$

It returns an output state and an actual witness connecting it to the input. This name does not imply that the output is later or different; partial operations must include admissibility evidence in their input. The path specialization uses $R(s,t)=(s=t)$. Retained histories, composition and higher coherence require the additional layers; they do not follow merely from the WG type. The names *Witnessor*, *Relational Witness Generator* and *Dependent Relational Witness Generator* refer to this same formulation.

[Layer-1 formulation](../research/nima/typed-witness-generator-layer.md) · [retained Layer 2](../research/nima/typed-generator-layer-2.md) · [ledger glossary entry 4296](https://github.com/andrey-kokoev/marici/blob/main/src/ledger/4296%20Witness%20Generator%20Glossary%20and%20Scope.md).

### Visual guide: retaining marked typed faces

![Four state occurrences and the fifteen marked nonempty faces in their barycentric incidence presentation; drawing crossings are not new incidences.](/experiments/barycentric-witness-packet.svg)

For one generated tetrahedron, each presentation vertex retains its face occurrence mark, witness type, and witness term. The displayed subdivision has 15 vertices, 50 edges, 60 triangles, and 24 tetrahedra. Equal underlying typed values do not recover occurrence marks; equal volume scores do not recover maximal flags. Those distinctions are retained as records, not reconstructed from the drawing.

This is a chosen finite affine realization, not physical geometry or a general identification of types with barycenters. [Read the diagram and information-loss controls](/experiments/barycentric-witness) · [source and reported verification](../research/nima/barycentric-witness-packet.md).

### Family formation is not execution

A dependent `Pi-package` retains a family of witnessed values $\prod_{i:I}B(i)$. The original native `P-kind` rule derives that family when **every component already has a derivation**; it can recover a certified component premise from such a derivation. Merely storing or seeding the family does not derive a selected output from a function and input. An explicit dependent application/elimination rule can do that while retaining both operands and its beta witness, but this has been checked only in the **application-extended runtime**, not as a theorem of the original twelve-rule closure. This separation matters for the proposed domain-specific constructor compiler: [scoped experiment](../research/nima/meta-witness-native-bridge.md) and [open conjecture](https://github.com/andrey-kokoev/marici/blob/main/src/ledger/4295%20Domain-Specific%20Constructors%20from%20Retained%20Domain%20Presentations.md).

## Finite-place incidence and physical descent

Two constructions must be kept separate: an explicit local Tate operator and a proposed comparison with the marked-relative cosmology source. The former has exact finite checks; the latter still needs its source-labelled comparison matrix. Neither matching ranks nor matching scalar readouts identifies the two sources.

### Tate residue-to-valuation incidence

For a prime $p$ and integer $N\ge1$, use the Schwartz–Bruhat packet

$$
V_N=\{f:\operatorname{supp}f\subset p^{-N}\mathbb Z_p,\quad
f(x+a)=f(x)\text{ for }a\in p^N\mathbb Z_p\}.
$$

It has dimension $p^{2N}$. With an additive character of conductor $\mathbb Z_p$ and self-dual Haar measure, Fourier transform preserves this packet. Normalized unit averaging $R_p$ is the orthogonal projection onto its valuation shells. Translation $T_hf(x)=f(x-h)$ preserves $V_N$ when $h\in p^{-N}\mathbb Z_p$.

The off-diagonal operator

$$
C_{p,h}=R_pT_h(I-R_p):(I-R_p)V_N\longrightarrow R_pV_N
$$

measures the radial information exposed by translating an input erased by unit averaging. Translation descends through $R_p$ exactly when $C_{p,h}=0$. On the full packet,

$$
C_{p,h}^2=0,\qquad
C_{p,h}^{\dagger}=(I-R_p)T_{-h}R_p,\qquad
\mathcal F_pC_{p,h}\mathcal F_p^{-1}=R_pM_{\chi_h}(I-R_p).
$$

The character sign follows the Fourier convention. Unitary dilation gives $D_aC_{p,h}D_a^{-1}=C_{p,h/a}$ on the full local carrier or transported packets; a nonunit dilation need not preserve a fixed $V_N$.

**Exact finite result.** Put $m=v_p(h)$, with $-N\le m<N$. The only possible nonzero singular values are

$$
1,\qquad \sqrt{1-(p-1)^{-2}},
$$

with active rank $N-m-1$ at $p=2$ and $N-m$ at odd primes. Thus every nonzero active sector has gap $1$ at $p=2$ and at least $\sqrt3/2$ at odd primes, uniformly across these finite refinements. Exact kernels remain; at $p=2,m=N-1$ the operator is zero. Translations in $p^N\mathbb Z_p$ are the identity on the packet and also give zero incidence.

For $p=2,N=1,h=1/2$, the operator sends $e_1-e_3$ to $e_2-e_0$ and is a rank-one partial isometry. Keeping $h=1/2$ and refining to $N=2$ gives rank two. The all-packet formula follows from the radial compression; the independent rational audit passes 48 cases at $p=2,3,5,7$, $N=1,2,3$, plus the full four-state fixture.

**Remaining arithmetic comparison.** This constructs a residue-to-radial incidence, not its identification with the primitive/square valuation boundary packet. That comparison must supply the boundary labels, metric, $\log p$ normalization and cycle $1/k$ law. Positivity of the associated block square does not establish completed Weil positivity, a global prime-to-Tate equivalence, or the Riemann hypothesis. Restricted-product/corona completion is a separate gate, not a consequence of the finite gap.

[Proof and conventions](../research/nima/tate-residue-radial-mixed-incidence.md) and [exact checker](../research/nima/checkers/check_tate_radial_mixed_incidence.py). Running the dependency-free checker regenerates the local audit output at `research/nima/results/tate-radial-mixed-incidence.json`.

### The circuit-to-cosmology comparison certificate

The nine oriented closed-circuit states resolve three circuit supports, each with multiplicity three. Their class map $\epsilon_{\rm circ}:C^{\rm or}_9\to\mathbb Z^2$ has saturated rank-seven kernel, with filtration

$$
0\longrightarrow K_6\longrightarrow\ker\epsilon_{\rm circ}
\longrightarrow K_{\rm rel}\longrightarrow0,\qquad
K_6\cong A_2^{\oplus3}.
$$

The six directions compare representatives of the same support; the final line records the relation among the three oriented circuit classes. Its character is $\chi_{\rm rel}(g)=(-1)^{\operatorname{core\ swap}(g)}\det(g|_{\rm roads})$. The ordinary 243-state transition graph cannot fill the unpointed three-tag diagonal: its edge boundaries have augmentation zero, while that diagonal has augmentation three. The oriented two-term resolution retains the relation without dividing by three.

This circuit module is **not yet identified** with the marked-relative $M_9$ in

$$
0\longrightarrow M_9\xrightarrow{\iota}M_{15}
\xrightarrow{\pi}Q_6\longrightarrow0.
$$

The missing comparison is the source-derived composite $J=\iota\Phi:C^{\rm or}_9\to M_{15}$, not an arbitrary isomorphism between rank-nine spaces. Its certificate must export an ordered source basis $\mathcal B_{15}$, the coefficient domain, $\pi$, $J$, the elliptic quotient $\bar q_\ell$ on $\ker\pi$, and the symmetry actions. Required checks include

$$
\pi J=0,\qquad \operatorname{rank}J=9,\qquad
\operatorname{im}J=\ker\pi,\qquad
\bar q_\ell J=\epsilon_{\rm circ},\qquad
J\rho_{\rm circ}(g)=\rho_{15}(g)J.
$$

These action equations use a fixed common coefficient domain; parameter-changing symmetries require the corresponding semilinear transport. Compatibility with the relative Gauss–Manin quotient must be derived, not assigned by matching circuit labels to master indices. Integral saturation and unit Smith factors require a declared integral lattice: the generic de Rham quotient alone does not supply one. The split-coordinate candidate $\begin{pmatrix}A&B\\0&I_2\end{pmatrix}$ must intertwine the symmetry extension classes, not merely preserve quotient dimensions.

Only a passing comparison identifies $JT$ with the physical rank-seven kernel, where the columns of $T$ form the circuit kernel basis. No such $J$ is constructed by these rank calculations.

### Green homotopy rather than an arbitrary absolute lift

For the actual elliptic quotient $E:M_9\to V_{\rm ell}$, inclusion matrix $I$, physical route $B$, and target differential $D$, the finite descent equation is

$$
BI=DH+C^{\rm ell}_pE.
$$

It says that the route depends on an ambiguity only through its elliptic class, up to the specified Green homotopy. Over a field, or a split free integral sequence, this is equivalent to filling the seven kernel columns; its benefit is a basis-independent formulation retaining the homotopy, not a stronger existence test.

The circuit filtration separates the six representative comparisons from the relation line. Strict vanishing on $K_6$ makes the relation image representative-independent as a chain. Null-homotopies on $K_6$ give that independence only in homology and must be retained in the symmetry comparison. An equivariant boundary need not have an integral equivariant primitive, so the final filler is tested in the equivariant mapping complex, not just a character component of ordinary homology.

A successful filler gives homotopical descent through $P_8=M_{15}/T_7$ and a map to $H_0(W_p)$. The extension $0\to V_{\rm ell}\to P_8\to Q_6\to0$ does not itself supply a zero elliptic coordinate over a fixed sewn class. A source-defined elliptic readout $\widetilde\epsilon:M_{15}\to V_{\rm ell}$ extending $E$ would supply that origin. Thus the $T_7$ ambiguity can be removed by homotopy without selecting an absolute lift, but the physical elliptic origin remains a separate datum.

**Sources.** [Circuit resolution, Entry 60](https://github.com/andrey-kokoev/marici/blob/main/src/ledger/20260813-60%20Integral%20Circuit%20Resolution%20and%20the%20True%20Skein%20Target.md); [generic de Rham Gysin quotient, Entry 150](https://github.com/andrey-kokoev/marici/blob/main/src/ledger/20260815-150%20Explicit%20Infinity-Gysin%20Projection%20and%20the%20Rank-Seven%20Algebraic%20Kernel.md); [marked-relative interface preflight](../research/nima/qG12-finite-quotient-interface-preflight.md); [lift audit](../research/nima/sewn-qG12-conductor-and-lift-audit.md).

## The single object and its three projections

The programme starts with a finite carrier and declared probe data, not a completed physical theory. Probes in a specified inner-product space define

$$
G_{ij}=\langle f_j\mid f_i\rangle.
$$

The historical proposal to obtain QM, GR, and the Standard Model as three projections of this matrix remains a set of **separate comparison problems**. Position, momentum, time, a field action, and gauge interactions are not derived merely by naming matrix sectors. The current [results and exclusions](/research/results/) distinguish bounded constructions from their physical interpretations.

## 1. The carrier

**Definition.** $X_N=\{x_1,\ldots,x_N\}$ is a finite set. A selected example is $X_4=\mathrm{Bool}\times\mathrm{Bool}=\{00,01,10,11\}$, with set automorphism group $S_4$. A bare finite set supplies no metric or physical spacetime. Boolean operations or a distinguished square structure are additional data if retained, and can change which symmetries are allowed.

The irreducible complex representations of $S_4$ have dimensions $1,1,2,3,3$; its natural four-point permutation representation is $\mathbf1\oplus\mathbf3$. This does not prove physical minimality, spatial spin, or a continuous gauge group. Partitioning a twelve-point set into three four-point blocks supplies a subgroup $S_4\times S_4\times S_4$ of its permutations, not three derived Standard Model generations.

A four-point floor is a chosen model boundary. Smaller subsets exist; they leave that selected carrier presentation, not a proved physically forbidden state space. The Postnikov/gauge-fibre identification remains conjectural.

## 2. Probes

Probes $f_i$ are elements of a declared function or vector space, with a chosen inner product and measure. They need not be functions on the label set itself. In the fixed-carrier realization, $f_i$ indicates permutations fixing label $i$ on $S_{12}$, and counting measure gives diagonal $11!$ and off-diagonal $10!$.

These choices have an exact finite realization but are not selected as physical wavefunctions. Probe normalization, a measurement rule, and the relation to a spatial or tensor structure require their own specification. The number of labels and the dimension of a permutation representation do not determine spacetime dimension or signature.

[Probe construction and count audit](../research/nima/carrier-gram-restriction-tower.md).

## 3. The Gram matrix

A Gram matrix is positive semidefinite and Hermitian: $G_{ij}=\overline{G_{ji}}$. It is real symmetric only under additional reality assumptions. Its spectrum is nonnegative, but it need not be invertible; linear independence of the probes gives positive definiteness.

Carrier relabelling transports probe data. **Invariance** of a fixed Gram under every permutation requires an equivariant probe/inner-product construction; it does not follow from the bare set's automorphism group. With common diagonal $s$ and off-diagonal one, the invariant example is

$$
G=(s-1)I+J.
$$

On four points its eigenvalues are $s+3$ and $s-1$, the latter with multiplicity three. Choosing $s=12$ gives 15 and 11, not a spectrum of $(12,11,4,10)$. Here $J$ denotes the all-ones matrix.

The distinct fixed-$S_{12}$ realization, divided once by $10!$, instead has $G_r=10I_r+J_r$ on $r$ surviving probes. Its norm eigenvalues are $r+10$ once and 10 with multiplicity $r-1$. A norm matrix is not automatically a Hamiltonian, Lorentzian metric, or gauge-field action.

## 4. Automorphism group

For the bare $N$-point set, $\operatorname{Aut}(X_N)=S_N$. Relabelling permutes Gram indices. The natural $S_4$ representation provides a constant line and a three-dimensional sum-zero subspace; sign and doublet representations exist elsewhere but are absent from this permutation carrier.

Assignments of these dimensions or selected integers to $U(1)$, $SU(2)$, or $SU(3)$ do not construct those continuous gauge actions, charges, or commutators. A binary tetrahedral spinor bridge supplies an explicit representation comparison, not a Standard Model derivation. [Bridge and native-selection test](#tetrahedral-geometry-spinors-and-the-native-loop-test).

## 5. The ladder descent — restriction versus promotion

The proposed $12\to11\to\cdots\to4$ ladder groups several distinct operations. They must not be interchanged by matching ranks or labels.

- **Gram restriction:** project between nested spans of independent probes in one fixed inner-product space. The rank decreases by one under the specified deletion order. Orthogonal projection is not simple coefficient deletion when probes overlap.
- **Retained-family promotion:** group records, retain their members and weights, and introduce fresh labels. Next-level endpoints and operations remain part of its contract.
- **Physical descent:** interpreting a norm, count, or rung as an energy or coupling requires an observation and dynamical adapter.

For the real coefficient realization $G_r=10I_r+J_r$, the exact restriction is

$$
y_i=x_i+\frac{x_r}{r+9},\qquad
x^T G_r x=y^T G_{r-1}y+\frac{10(r+10)}{r+9}x_r^2.
$$

Retaining the signed residual reconstructs the original state; nested orthogonal restrictions compose. The mean retained fraction $r/12$ requires a metric-isotropic ensemble. No clock, Hamiltonian, or GeV conversion follows from this norm identity. Rebuilding probes on each $S_r$ gives a different tower with different normalization.

[Fixed-carrier derivation and exact checker](../research/nima/carrier-gram-restriction-tower.md) · [separate record transport diagram](#tower-successor-and-mixed-comparison-defects).

## 6. Three projections from one Gram matrix

| Proposed reading | Available mathematical structure | Missing physical identification |
|---|---|---|
| Quantum | Positive overlaps, a normalized density matrix for nonzero $G$, and declared interference readouts. | State/preparation semantics, measurement effects, tensor locality, and an evolution law. |
| Gravitational | Finite stabilizer covariance and positive inner-product geometry. | Lorentzian field geometry, continuum limit, action, and smeared Poisson constraints. |
| Standard Model | Finite permutation representations and specified sector operators. | Continuous gauge actions, matter representations, symmetry breaking, and physical couplings. |

Diagonalization of a Hermitian operator uses a unitary change of basis, $G=U D U^\dagger$. This is a spectral identity, not a construction of the three physical theories.

## 7. QM projection — interference, phases, and the Born rule

The expression $I=\sum_{i,j}G_{ij}e^{i(\theta_j-\theta_i)}$ is a declared interference functional. Specifying phase values does not select their evolution; a generator or other update law is required. The earlier claim “no Hamiltonian needed” as a dynamics derivation is withdrawn.

For nonzero positive $G$, $\rho=G/\operatorname{Tr}G$ is a density matrix in the chosen coordinate Hilbert space. Its diagonal entries give probabilities **under the additional Born-rule measurement interpretation in that basis**. Positivity normalizes this model; it does not select the physical measurement rule. Rank-one factorization is a pure-state case, not a general Gram identity. Entanglement and Bell tests require specified tensor factors, states, and observables.

The recent local-lift construction supplies a different, explicit conditional dynamics. Linearize the two native Bool flips as commuting Hermitian involutions $P_j$ on standard $\mathbb C^4$, then set $Q_j=(I-P_j)/2$, $H_j=\pi Q_j$, and $U_j(t)=\exp(-itH_j)$. With declared standard analytic semantics this gives unitary local legs and external metric whole-return paths retaining schedule information. The written all-time existence proof, exact finite checks, and source-classification theorem have distinct roles; this is not unique selection of physical dynamics by bare Tick.

[Standard-complex whole-return construction](../research/nima/spectral-whole-return-proof.md). Operational completion proofs, standard-pi identification, and whole-return assembly are separately scoped; neither this written existence theorem nor a chosen three-cycle establishes physical flavor phases or an arrow of time.

## 8. GR projection — finite geometry is not ADM gravity

For a point of the four-label set, its stabilizer is $S_3$, acting on the other three labels. This finite action gives covariance, not three-dimensional space. A positive Gram submatrix can define an inner product on an independent span. It cannot acquire a negative temporal direction merely by restriction or by connecting stabilizers.

**Withdrawn legacy promotions:** finite stabilizer conjugation as a verification of ADM Poisson brackets; a Lorentzian-signature certificate from an antisymmetric curvature form; and the asserted continuum interpolant. These failed or unsupported routes do not exclude other gravitational constructions.

The conditional rotor and its canonical cotangent lift remain valid finite mechanical comparisons. A positive rotor Hamiltonian with empty zero level cannot simply be renamed a vanishing GR constraint. Adding a clock momentum can parametrize that mechanical system, but does not construct field constraints or a physical-time map.

The missing comparison must provide a field phase space, actual smeared Hamiltonian and momentum constraints, their Poisson brackets, continuum geometry, and a source-selected action. An Einstein-Hilbert-shaped formula without those data is not a derivation.

[ADM correction and stopping boundary](../research/nima/formal-adm-constraint-derivation.md) · [finite canonical actions versus field constraints](../research/nima/finite-canonical-actions-versus-adm-constraints.md) · [continuum evidence boundary](../research/nima/continuum-embedding-evidence-boundary.md).

## 9. SM projection — S4 irrep decomposition and gauge groups

**Corrected permutation representation.** The natural action on $\mathbb C^4$ splits into the constant line and the sum-zero subspace:

$$
\mathbb C^4=\mathbf1\oplus\mathbf3.
$$

The standard three-dimensional representation is irreducible; it is not $\mathbf1'\oplus\mathbf2$. Sign and doublet representations exist elsewhere in the representation theory of $S_4$, but are absent from this permutation carrier. The previous table assigning its sectors to hypercharge, weak isospin, and colour is withdrawn.

An ordinary two-dimensional finite-group representation is not by itself a spatial spin-$1/2$ representation or a weak-isospin doublet. The checked spatial bridge instead uses the binary tetrahedral group $2T\subset SU(2)$ above $A_4\subset SO(3)$. Its defining doublet has $\operatorname{End}(S)=\mathbf1\oplus\mathbf3$, with the central sign cancelling on operators. [Exact bridge and physical-selection test](#tetrahedral-geometry-spinors-and-the-native-loop-test).

The numerical expressions in $(12,11,4,10)$ elsewhere on this page remain proposals with their own assumptions. They are not derived continuous gauge couplings or particle constants merely because those numbers label a chosen matrix.

## 10. CKM and PMNS — flavor misalignment

For **supplied** sector diagonalizations, basis changes can define mixing matrices, for example $V_{\mathrm{CKM}}=U_u^\dagger U_d$ and $U_{\mathrm{PMNS}}=U_e^\dagger U_\nu$ with the appropriate physical left-handed bases. This does not select sector operators, their eigenbases, or physical flavor labels from a common Gram matrix. Degenerate eigenspaces do not fix a preferred basis.

The targets $\pi/3+(4/12)^2\approx66.4^\circ$ and $(12/10)\pi=216^\circ$ are arithmetic expressions, not derived flavor observables. An oriented three-cycle does not establish three generations or CP-violating dynamics. A test needs source-selected sector operators, rephasing-invariant observables, conventions, and uncertainties.

## 11. Anomaly cancellation

Anomaly tests concern specified chiral matter representations and charges. Conventional Standard Model matter can satisfy them; verifying its trace identities does not derive that matter from a finite carrier. Local anomaly conditions and global consistency conditions must be distinguished rather than counted as interchangeable Ward identities.

One Standard Model generation plus a right-handed neutrino can be placed in the chiral 16-dimensional spinor of $\operatorname{Spin}(10)$ as an additional representation choice. The former displayed decomposition into one each of $1,1',2,3,3'$ is withdrawn: those dimensions sum to 10, not 16. No embedding and multiplicities selecting a 16-dimensional matter representation from the four-point carrier are supplied here. Anomaly cancellation for specified matter content does not derive that content from the carrier.

## 12. Higgs mechanism

**Proposed origin.** A doublet-singlet coupling could be specified on an enlarged representation, but the natural four-point permutation carrier has only $\mathbf1\oplus\mathbf3$. The previously asserted doublet/singlet Gram blocks and symmetry-breaking potential are not derived from that carrier.

The identities $11^2+4=125$ and $2\cdot11^2+4=246$ yield candidate targets. Assigning GeV units and a Higgs interpretation requires a derived gauge action, potential, vacuum, and scale; none follows from the integer identities.

Their ratio is $125/246\approx0.50813$. Inserting them into the conventional relation $\lambda=m_H^2/(2v^2)$ gives about 0.1291, not a derived quartic potential.

## 13. Strong CP / axion (schematic)

A global phase analogy does not supply an axion mechanism. It needs a physical field, symmetry breaking, coupling to QCD topology, and a potential. Neither a continuous Standard Model gauge sector nor its nonperturbative dynamics is derived by the finite comparison. Axion mass, photon coupling, and suppression of the strong CP parameter remain unconstructed.

## 14. Dark matter

Sterile-neutrino content, a seesaw interaction, and modified inertia are candidate additional models, not deductions from Gram entries. The ratio $10/11$ supplies no dimensionful Majorana mass.

The proposed abundance $(10-4)/(12+11)=6/23\approx0.26087$ is exact arithmetic. Observational comparison needs a production/evolution law and cosmological readout. No source-selected sterile-neutrino mass, X-ray line, or modified-inertia law is supplied. These candidate mechanisms are not proved mutually exclusive.

## 15. Dark energy

Uniform Gram diagonal entries are equal probe norms, not automatically vacuum stress-energy. A cosmological interpretation needs an action, energy reference, units, and field equations.

The expression $2\ell_{\mathrm{Pl}}^2/R^2$ is dimensionless. Identifying it with a cosmological constant needs an explicit convention, such as $\Lambda\ell_{\mathrm{Pl}}^2$; dimensionful $\Lambda$ has inverse-length-squared units. The carrier does not select $R$ or this normalization. The cosmological-constant and hierarchy problems are not solved by matching a chosen ratio.

## 16. Einstein equation (unconstructed physical comparison)

The assertion that ADM constraints already close at the stabilizer level is withdrawn. Finite covariance, a positive Gram inner product, and a parametrized mechanical rotor do not construct a GR field phase space or its constraint algebra.

The historical proposal to vary a curvature functional of a stabilizer Gram does not establish Einstein's equation. A manifold, Lorentzian metric, curvature, measure, matter action, boundary conditions, and source map must first be defined; the resulting field equations and constraints must then be proved. Even a successful classical variation would not alone supply quantum gravity.

Neither that field construction nor a continuum limit is supplied by the legacy finite calculations. [Correction and missing typed comparison](../research/nima/formal-adm-constraint-derivation.md). This rejects the claimed promotion route, not every gravitational construction.

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

**Hypothesis and current boundary.** The expression $12(12^2+3^2)=1836$ counts a proposed comparison programme, not a derived mass ratio. The observed value is approximately $1836.152673$. Exact slot counts and disturbance-settling prototypes have been checked; their physical energy law and fractional correction remain unconstructed. A separate [tetrahedral projector realization and spinor audit](#tetrahedral-geometry-spinors-and-the-native-loop-test) now distinguishes its exact geometry from the missing particle interpretation.

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

QCD describes quarks as spin-$1/2$ fields. The retained-overlap proposal has not derived the two-component physical state, its probe-axis response, or polarized-scattering observables. The native-loop test below rejects the specific claim that existing tetrahedral transport already selects the spinorial sign; adding a doublet remains a new input.

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

### Tetrahedral geometry, spinors, and the native-loop test

**Current status:** exact geometry and representation comparison; physical proton identification unproved. The two seed rotations generate $A_4$ and twelve centroid-edge triangles on a closed tetrahedron. Twelve three-axis fibers give a 36-dimensional complex carrier. Its local, symmetry and collective projectors satisfy

$$
L^2=L,\qquad R^2=R,\qquad N^2=N,\qquad LR=RL=N,
$$

with ranks $12,3,1$. The reference vector has squared norm $20/3$ and the assembled vector $u$ has squared norm 80, so $N=uu^*/80$.

**What 1836 counts.** In the inherited axis basis, the specified three-stage network has $108+432+1296=1836$ nonzero arrows. Distinct stage ports and dense collective feedback are explicit choices. This is neither a basis-independent minimum nor a mass. The separate 153-slot comparison programme has the same integer count; equal counts do not identify their dynamics. [Geometry and implementation](https://github.com/andrey-kokoev/marici/blob/main/research/nima/twelve-triangle-positive-geometry.md).

**The spinorial bridge.** The binary tetrahedral cover $2T\to A_4$ has kernel $\{\pm1\}$ and restricts to $Q_8\to V_4$. For its defining two-component spinor $S$, Pauli conjugation recovers the three-axis action:

$$
\Phi(v)=\sum_{a=1}^3v_a\sigma_a,\qquad
U(q)\Phi(v)U(q)^*=\Phi(r(q)v),\qquad
\operatorname{End}(S)=\mathbf1\oplus\mathbf3.
$$

Thus $2\otimes2^*=1+3$ relates state and operator spaces. It is not a simplex-doubling law for quantum numbers. Spatial spin and weak isospin are distinct, and a finite-group doublet alone does not derive either physical identification.

The original projectors survive as Hilbert-Schmidt superoperators on twelve traceless operator fibers; their central action is even. Adding an independent factor $S$ gives $V_{36}\otimes S$ of dimension 72 and a rank-two collective sector $\operatorname{span}(u)\otimes S$ with central action $-I_2$. Replacing three-component fibers with two-component spinors instead gives dimension 24 and no invariant vector. Neither operation proves that the additional spinor is physical. [Exact bridge and hostiles](https://github.com/andrey-kokoev/marici/blob/main/research/nima/binary-tetrahedral-spinor-bridge.md).

**Independent selection test.** The conjecture was that native coherent transport, without inserted spinors, requires a relative minus sign for an orthogonal-half-turn commutator. The native selected-line maps instead obey

$$
T_{yx}=\frac{v_yv_x^*}{20/3},\qquad T_{zy}T_{yx}=T_{zx}.
$$

Every closed selected-line route therefore returns +1. All six ordered half-turn commutators confirm this. Bare projector products also give positive commutator amplitudes, even though a different three-step loop gives $-13/3375$. A negative interference coefficient alone is not spinorial transport. Inserting one negative edge forces the desired sign but breaks a native composition cell, with squared defect norm 4.

The native-selection conjecture fails **within this endpoint/filter model**. The broader physical conjecture is untested: a rotation-path-dependent physical interaction and coherent readout have not been independently specified. The local triangle cycle is also nonorthogonal; it cannot silently be treated as unitary spinor transport. [Native-loop falsification and source audit](https://github.com/andrey-kokoev/marici/blob/main/research/nima/tetrahedral-native-rotation-loop.md).

**Charge correction.** The earlier universal charge no-go is withdrawn. Both $I$ and $N$ commute with the combined $A_4$ action and give eigenvalue +1 on $u$; $N$ has spectrum $\{0,1\}$ and $2N-I$ has spectrum $\{-1,1\}$. Conversely, a half-turn scaled by -3 has expectation +1 but variance 8, so $u$ is not its charge eigenstate. These algebraic candidates do not identify electric charge without independent sectors and electromagnetic coupling. [Corrected charge scan](https://github.com/andrey-kokoev/marici/blob/main/research/nima/tetrahedral-axis-sign-charge-operator.md).

**Verification.** The dependency-free checkers `check_twelve_triangle_positive_geometry.py`, `check_binary_tetrahedral_spinor_bridge.py`, `check_tetrahedral_native_rotation_loop.py`, and `check_tetrahedral_axis_charge_operator.py` use exact arithmetic. The bridge tests 576 group products and 1,728 cocycle triples; the native-loop audit tests 1,728 composition triples for each of its two transport laws. An audit pass records these identities and the failed native-selection consequence, not an experimental confirmation of a proton model.

### Constant expressions

The assigned numbers $(12,11,4,10)$ generate arithmetic identities and candidate comparisons; they are not the fixed-carrier Gram spectrum. The factor $Z=1/(1+1/90-1/5280)$ is a proposed feedback assignment, not a selected gravitational normalization.

| Candidate identification | Expression | Verification boundary |
|---|---|---|
| Electromagnetic coupling | $11^2+4^2=137$ | A [slot count](#fine-structure-constant-comparison-slots), not an electromagnetic readout. The routing trial fails precision recoil targets. |
| Weak mixing | $3/13$ | The cited [matter-trace derivation fails](#weak-mixing-matter-trace-audit); scale, scheme, and running remain required. |
| Planck/weak hierarchy | $11^{15}\,12\,Z$ | No carrier-selected scale-generation law is established. |
| QCD scale and proton mass | $M_{\mathrm{Pl}}/11^{19}$ and $(14/3)M_{\mathrm{Pl}}/11^{19}$ | Require a Planck-mass convention, dynamical QCD scale, and mass observable. Approximate agreement is not a source derivation. |
| Proton/electron mass | $12(12^2+3^2)=1836$ | [Comparison and implementation counts](#proton-electron-ratio-comparison-paths-and-settling), not the measured approximately 1836.152673 mass ratio. |
| Higgs mass and vev | $11^2+4=125$, $2\cdot11^2+4=246$ | Assigning GeV units and a Higgs sector is additional unestablished physics. |
| Cosmological fractions | $6/121$, $6/23$, $11/16$, $91/44528$ | Their sum is exactly one; density and curvature readouts require dynamics and independent normalization. |

A statistical test needs independently sourced measurements, units and conventions, experimental and theoretical uncertainties, and a traceable derivation. The previous percentage-agreement table did not supply that evidence. [Public comparison targets](/research/results/#numerical-comparison-targets).

## 18. Mathematical connections

**Carrier and Boolean structure.** $\mathrm{Bool}\times\mathrm{Bool}$ has four elements; the free Boolean algebra on two generators has 16. Four classical labels can index a two-qubit basis after linearization and tensor structure are supplied. Their permutation group $S_4$ is not the Clifford group.

**Modular forms.** $E_4$ and $\Delta$ have weights 4 and 12, and $j(i)=1728=12^3$. The point $i$ lies in the upper half-plane, not at a cusp. These identities do not identify modular forms with carrier operators or physical couplings; an explicit map and its laws remain needed.

**Monster and sporadic groups.** Appearances of 24, the Leech lattice, the Griess algebra, and finite permutation actions motivate possible comparisons. They do not make $S_{24}$ the Monster or establish a next physical carrier. The embedding $M_{12}\subset S_{12}$ is a finite permutation representation, not a physical-generation theorem.

**Homotopy theory.** Stable homotopy and the Postnikov tower of $BS_4$ are proposed comparison tools. Stable-stem groups do not simply become $S_4$ or continuous Standard Model gauge groups. A gauge correspondence needs an explicit construction, not matching orders or dimensions.

**Scope.** Moduli, division algebras, TQFT, integrability, and other suggested connections remain separate research hypotheses. Publish exact identities and specified maps with their verification scope, not as evidence that all physics follows from one Gram matrix.
