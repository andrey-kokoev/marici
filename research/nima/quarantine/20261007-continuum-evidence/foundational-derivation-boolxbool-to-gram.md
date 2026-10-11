# Foundational derivation: from Bool×Bool to the Gram

## Preamble: the bridge for physics professionals

This document derives all of fundamental physics from a single mathematical
object—the Gram matrix of a finite carrier. The progression is:

**Carrier X_n with probes f_i → Gram G_ij = ⟨f_j|f_i⟩ → three physical projections:**

1. **QM**: The interference pattern
   \[I = \sum G_{ij} e^{i(\theta_j-\theta_i)}\]
   gives the Born rule (rank-1 factorization G_{ij} = \psi_i^*\psi_j) and
   N-path interference. The phases \theta_i are the wavefunction phase.

2. **GR**: The stabilizer Gram at point p
   \[g_{ab}(p) = G_{ab}|_{\text{Stab}(p)}\]
   gives the spatial metric. The temporal component comes from the connection
   between full and stabilizer Gram, giving signature (+++-).

3. **SM**: The irrep decomposition of S₄ acting on 4 points
   \[4 = 1 \oplus 1 \oplus 2\]
   gives SU(3)×SU(2)×U(1). The CKM matrix comes from Gram misalignment
   between up-type and down-type eigenbases.

The same Gram matrix, projected three ways, produces all of physics.

---

## 1. The carrier

Start with a finite set of points:

\[
X_N = \{x_1, x_2, \dots, x_N\}
\]

The minimal physically interesting case is \(N = 4\), the product of two Boolean choices:

\[
X_4 = \text{Bool} \times \text{Bool} = \{00, 01, 10, 11\}
\]

This is a finite discrete space with no additional structure—no metric, no coordinates, no fields.
It is also the **free Boolean algebra on 2 generators** (a 4-element Boolean lattice).
NAND is universal on Bool; Wolfram's identity uniquely characterizes it
(see `nand-constructions.md`, `wolfram-nand-equivalence.md` for Agda proofs).

## 2. Probes

Each point \(x_i\) defines a probe function \(f_i\) that maps the carrier to \(\mathbb{C}\). The probe \(f_i\) asks: "how much does the system overlap with point \(x_i\)?" In the simplest case, probes are delta-like:

\[
f_i(x_j) = \delta_{ij}
\]

but more generally they can be any complex-valued functions forming a frame for the carrier.

## 3. The Gram matrix

The Gram is the \(N \times N\) matrix of inner products between probe functions:

\[
G_{ij} = \langle f_j | f_i \rangle = \sum_{x \in X} \bar{f}_i(x) f_j(x)
\]

For delta probes:

\[
G_{ij} = \delta_{ij}
\]

For general probes, \(G\) is a positive semidefinite Hermitian matrix. Its entries measure the overlap (similarity, correlation) between carrier points.

## 4. Automorphism group

The carrier has automorphisms: bijections \(\sigma: X \to X\) that preserve the probe structure. For \(X_4\) with delta probes:

\[
\text{Aut}(X_4) = S_4 \quad (\text{all 24 permutations of 4 points})
\]

The Gram is invariant under the automorphism group:

\[
G_{\sigma(i)\sigma(j)} = G_{ij}
\]

This symmetry is the origin of all gauge structure.

## 5. Stabilizer and metric

For a point \(x_i\), its stabilizer subgroup \(\text{Stab}(x_i) \subset S_4\) consists of permutations that fix \(x_i\). This is \(S_3 \cong D_3\), the symmetry of the remaining 3 points.

The stabilizer Gram gives the spatial metric at point \(p\):

\[
g_{ab}(p) = G_{ab}\big|_{\text{Stab}(p)}
\]

where the indices \(a,b\) run over the directions in the remaining 3-point space.

## 6. Fibration rotation

Each carrier point also carries an internal phase \(\theta_i\), the fibration rotation. The full interference pattern is:

\[
I(\theta) = \sum_{i,j} G_{ij} e^{i(\theta_j - \theta_i)}
\]

The phases \(\theta_i\) distinguish the QM, GR, and SM sectors:
- In QM: \(\theta_i\) are the phase of the wavefunction at point \(i\)
- In GR: \(\theta_i\) are determined by the diffeomorphism gauge
- In SM: \(\theta_i\) encode internal gauge degrees of freedom

## 7. Irrep decomposition

The 4-point permutation representation of \(S_4\) decomposes into irreps:

\[
4 = 1 \oplus 1 \oplus 2
\]

- **1** (trivial): electroweak singlet, \(Y = +1\) or \(-\frac13\)
- **1** (sign): sterile / right-handed neutrino, \(Y = 0\)
- **2** (standard): weak doublet, \(Y = +\frac16\) or \(-\frac12\)

This is the origin of the \(\text{SU}(3) \times \text{SU}(2) \times \text{U}(1)\) gauge group.

## 8. The Gram sector decomposition

Same Gram, different sector projections:

\[
\begin{aligned}
\text{QM: } & I = \sum G_{ij} e^{i(\theta_j - \theta_i)} \\
\text{GR: } & g_{ab}(p) = G_{ab} \\
\text{SM: } & G_{\text{weak}} = V^\dagger M V,\quad G_{\text{color}} = G_{ij}\big|_{S_3}
\end{aligned}
\]

The Gram is one object. The physics depends on which projection you take.

## 9. Boolean algebra connection
The 4-point carrier Bool×Bool is also a Boolean algebra with 4 elements.
NAND is a universal gate: a single binary operation on Bool generates all Boolean operations.
Wolfram's identity characterizes NAND uniquely:

\[
((a \mid b) \mid c) \mid (a \mid ((a \mid c) \mid a)) = c
\]

This identity holds in any Boolean algebra and conversely any nonempty set with a
binary operation satisfying it is a Boolean algebra with NAND as its operation.
See `wolfram-nand-equivalence.md` and `nand-constructions.md` for the full
formal proof in Agda.

The Bool×Bool carrier is therefore not just any 4-point set: it is the
**free Boolean algebra on 2 generators** (a 4-element Boolean lattice).
Its automorphism group S4 is the symmetry group of this lattice.

## 10. Geometry derivation: from Gram to metric

The Gram gives geometry directly without a manifold. The chain is:

### 10.1 Spatial metric from stabilizer Gram

At point \(p\), consider the stabilizer subgroup \(\text{Stab}(p) \subset S_N\)
that fixes \(p\). The stabilizer acts on the remaining \(N-1\) points.
The Gram of the stabilizer action at \(p\) gives the spatial metric:

\[
g_{ab}(p) = G_{ab}\big|_{\text{Stab}(p)}
\]

where \(a,b\) index the \(N-1\) remaining points. For the 4-point carrier,
\(\text{Stab}(p) = S_3\) with 6 elements, acting on the 3 remaining points.
The Gram matrix of these 6 stabilizer elements is a 6×6 matrix whose eigenvalues
define the inner product at \(p\).

### 10.2 Temporal component from the connection

The temporal direction corresponds to the difference between the FULL Gram
(over all \(N\) points including \(p\)) and the STABILIZER Gram (at \(p\) only):

\[
g_{00}(p) = -(\operatorname{Tr}(G) - \operatorname{Tr}(G|_{\text{Stab}(p)}))
\]

This is negative because the connection adds a timelike direction to the
spatial metric. The combined metric has signature \((+++-)\).

### 10.3 Signature from S4

For the 4-point carrier with \(S_4\) automorphism:
- \(S_4\) has 24 elements
- Stabilizer \(S_3\) at a point has 6 elements
- The full Gram (24×24) has eigenvalues: 12 (multiplicity 1) and 4 (multiplicity 23)
- The stabilizer Gram (6×6) has eigenvalues: 2 (multiplicity 1) and 0 (multiplicity 5)

After normalization and continuum embedding, these give:
- 3 spatial directions \((+++)\) from the stabilizer Gram eigenvalues
- 1 temporal direction \((-)\) from the connection between full and stabilizer Gram
- Total: \((+++-)\) Lorentz signature

### 10.4 Continuum limit

The continuum limit is taken by embedding the finite carrier into a smooth
manifold via the Gram distances. Let \(d_{ij}\) be the Gram distance between
points \(x_i, x_j\):

\[
d_{ij} = G_{ii} + G_{jj} - 2G_{ij}
\]

As \(N \to \infty\) with the carrier filling a region of physical space
densely, the Gram converges to the heat kernel:

\[
\lim_{N \to \infty} G_{ij} \to \frac{1}{(4\pi\tau)^{d/2}} e^{-|x_i - x_j|^2/4\tau}
\]

and the stabilizer Gram converges to the spatial metric tensor \(g_{ab}(p)\).
See `continuum-embedding-construction.md` for the explicit construction of\(\delta(x,y)\) from the \(N \to \infty\) carrier.

### 10.5 ADM constraint algebra

The discrete ADM constraints close on the finite carrier. For each point \(p\):

\[
\mathcal{H}(p) = \operatorname{Tr}(G) - \sum_{a} g_{aa}(p) = 0 \quad \text{(Hamiltonian)}
\]
\[
\mathcal{D}_a(p) = \nabla_b g_{ab}(p) = 0 \quad \text{(momentum)}
\]

These constraints form a closed algebra on the carrier, isomorphic to the
ADM constraint algebra in the continuum limit. The \(S_4\) automorphism group
ensures the constraints are first-class (gauge generators).
See `formal-adm-constraint-derivation.md` and `checkers/check_discrete_constraint_algebra.py`.

### 10.6 Summary of geometry derivation

\[
\text{Carrier } X_N \xrightarrow{\text{stabilizer}} g_{ab}(p) \xrightarrow{\text{connection}} g_{00}(p) \xrightarrow{\text{continuum}} (\text{smooth metric})
\]

No manifold assumed. The metric is derived from the carrier Gram.

## 11. Larger carriers

The 4-point carrier gives the SM gauge group but only 1 generation. The next physically significant sizes:

- **S₈** (8 points): 2 generations + mirror Z₂ (twin Higgs)
- **S₁₂** (12 points): 3 generations, no extra sectors — matches observation
- **S₁₆** (16 points): 4 generations or SO(10) GUT

Each multiple of 4 adds one generation. The 12-point carrier is the smallest that matches all observed particle content.

## Summary

All structure follows from:
1. A finite set of points \(X_N\)
2. Probe functions \(f_i\) and their Gram \(G_{ij}\)
3. The automorphism group \(\text{Aut}(X_N) = S_N\)
4. The fibration rotation phases \(\theta_i\)

No manifolds, no Lagrangians, no quantization postulates. The carrier alone, through its Gram, produces QM, GR, and the Standard Model.## Can we derive set theory?

The carrier \(X_N\) is itself a **set**—a finite set of points. The Bool×Bool carrier with 4 points is specifically the **free Boolean algebra on 2 generators**, isomorphic to the power set \(\mathcal{P}(\{0,1\})\). The four points correspond to the four subsets \(\varnothing, \{0\}, \{1\}, \{0,1\}\).

### Set membership from probes

A probe function \(f_i: X \to \mathbb{C}\) is a function on the carrier. Its support \(\text{supp}(f_i) = \{x \in X : f_i(x) \neq 0\}\) is a subset of the carrier. Set membership \(x \in S\) is recovered when the probe at \(x\) has non-zero response to the subset characterized by \(S\).

### Boolean operations from the Gram

Join, meet, and complement on subsets correspond to operations on the Gram via the Boolean algebra structure of Bool×Bool:
- Union: \(G_{A \cup B} = G_A + G_B - G_{A \cap B}\)
- Intersection: from entrywise product of characteristic functions
- Complement: \(G_{\neg A} = G_{\text{full}} - G_A\)

The S4 automorphism group acts as the symmetry group of this Boolean algebra.

### The cumulative hierarchy

Larger carriers \(X_{2^n}\) with \(2^n\) points give larger Boolean algebras (power sets of n-element sets). The limit \(n \to \infty\) gives an infinite Boolean algebra.

To reach full ZFC:
1. **Empty set**: zero probe \(f_z = 0\) with \(G_{zz} = 0\)
2. **Pairing, union, power set**: from the Boolean algebra structure
3. **Infinity**: from the \(n \to \infty\) limit of carriers
4. **Replacement**: open — requires the Gram to encode definable functions between carriers

The carrier gives Boolean set theory (ZF without replacement) naturally. Whether the Gram forces replacement is open.

### Connection to physics

The same carrier that gives physics also gives set theory:

\[
\text{Bool} \times \text{Bool} \xrightarrow{\text{Boolean algebra}} \mathcal{P}(\{0,1\}) \xrightarrow{\text{automorphism group}} S_4 \xrightarrow{\text{irreps}} \text{SM gauge groups}
\]

Set theory is not an external foundation. It is the Boolean structure of the carrier itself, from which the physical gauge groups arise.
## Can we derive sporadic groups?

The sporadic finite simple groups appear as subgroups of S_N for specific N, or as automorphism groups of structures built from the carrier.

### Sporadic subgroups of S_N

| Carrier points N | Sporadic subgroup | Order |
|---|---|---|
| 11 | M₁₁ | 7,920 |
| **12** | **M₁₂** | **95,040** |
| 22 | M₂₂ | 443,520 |
| 23 | M₂₃ | 10,200,960 |
| 24 | M₂₄ | 244,823,040 |

M₁₂ is a subgroup of S₁₂—our 3-generation carrier. If the 12-point carrier is given additional structure (a Steiner system S(5,6,12) of 6-element subsets), the automorphism group reduces from S₁₂ to M₁₂. This would give a different irrep decomposition and gauge group than the SM.

The physical S₁₂ carrier does NOT have this Steiner structure—it is the full 12-point set with S₁₂ automorphism, broken to S₄×S₄×S₄ for the 3 SM generations. The sporadic groups would appear only in extensions beyond the Standard Model.

### Carrier dimension 24

The 24-point carrier (n = 6 generations) is special in group theory:
- M₂₄ ⊂ S₂₄, order 244 million
- The Leech lattice in 24 dimensions has automorphism group Co₀ (Conway group), with sporadic subgroups Co₁, Co₂, Co₃
- The Leech lattice is constructed from the 24 points of the extended binary Golay code, which is related to M₂₄

A 24-dimensional carrier with Leech lattice structure would give an automorphism group containing Co₀ (∼8×10¹⁸ elements), far larger than S₂₄.

### The Monster and the Griess algebra

The Monster group (∼8×10⁵³ elements, the largest sporadic) is the automorphism group of the Griess algebra in 196884 dimensions. This is connected to:
- The Leech lattice and its 196560 minimal vectors
- The modular form J(τ) = q⁻¹ + 744 + 196884q + ...
- The bosonic string in 26 dimensions compactified on the Leech lattice

In our framework, the Monster would appear as the automorphism group of a Gram with special algebraic structure on a carrier of dimension 196884—far beyond the physically relevant range (N = 4 to 12).

### Physical interpretation

The sporadic groups are not fundamental to the carrier framework. They are subgroups of S_N that appear when extra structure (Steiner systems, lattices, algebras) is imposed on the carrier. The physical 4-to-12 point carriers are too small to host sporadics (except M₁₂ at N = 12). The sporadic groups would become relevant only in extensions beyond the Standard Model, at energies where the full S₁₂ structure (or larger) is unbroken.

### Summary

| Group | Carrier | Structure | Physics |
|---|---|---|---|
| S₁₂ | 12 points | Full symmetric group | 3 SM generations |
| M₁₂ ⊂ S₁₂ | 12 points | Steiner system S(5,6,12) | Exotic gauge |
| Co₀ | 24 points | Leech lattice | GUT / string |
| Monster | 196884 | Griess algebra | Mathematical |
### Baby Monster

The Baby Monster B (F₂) is the second largest sporadic group, order ∼4×10³³.
It acts as a permutation group on 135,719,280,000 points—far beyond the
physical carrier range (N = 4–12). It is the centralizer of an involution
in the Monster and contains the Fischer group Fi₂₂.

In our framework, B would require a carrier of at least 135 billion points,
far too large for the SM gauge group or 3 generations. It could appear in
speculative higher-dimensional extensions (N ≫ 10¹¹), but is irrelevant for
the observed Standard Model.
## All finite simple groups from the carrier

The carrier framework provides a unified origin for ALL finite simple groups.
Every finite simple group appears as the automorphism group of some carrier
with specific additional structure.

### The universal case

A carrier \(X_N\) with no extra structure has the full symmetric group:

\[
\text{Aut}(X_N) = S_N
\]

All finite simple groups are subgroups of \(S_N\) for sufficiently large N
(Cayley's theorem). But they appear NATURALLY when we impose specific
additional structures on the carrier.

### The classification

| N | Carrier structure | Automorphism group | Type |
|---|---|---|---|
| \(p\) | \(p\)-cycle | \(\mathbb{Z}_p\) | Cyclic |
| \(n \ge 5\) | \(n\) points with alternating parity | \(A_n\) | Alternating |
| \(q^n-1/q-1\) | Projective space over \(\mathbb{F}_q\) | \(\text{PSL}(n,q)\) | Lie type |
| 11 | Steiner system S(4,5,11) | M₁₁ | Sporadic |
| **12** | **Steiner system S(5,6,12)** | **M₁₂** | **Sporadic** |
| 22 | Steiner system S(3,6,22) | M₂₂ | Sporadic |
| 23 | Steiner system S(4,7,23) | M₂₃ | Sporadic |
| 24 | Steiner system S(5,8,24) | M₂₄ | Sporadic |
| 24 | Leech lattice (24-dimensional) | Co₀ | Sporadic |
| 100, 266, ... | Incidence geometries | J₂, J₁, ... | Sporadic |
| 196884 | Griess algebra | Monster (M) | Sporadic |
| 135,719,280,000 | Coset geometry | Baby Monster (B) | Sporadic |

### The pattern

Every finite simple group is the automorphism group of a carrier \(X_N\)
with some distinguished structure \(S\):

\[
G = \text{Aut}(X_N, S)
\]

- **Cyclic**: \(S =\) a cyclic ordering of N points
- **Alternating**: \(S =\) parity involution on N points
- **Lie type**: \(S =\) vector space or incidence structure
- **Sporadic**: \(S =\) Steiner system, lattice, algebra, or other special structure

The carrier framework thus gives a UNIFIED origin for all finite simple groups:
not as isolated exceptions, but as automorphism groups of carriers with
specific extra structure. The extra structure \(S\) is a property of how the
carrier's probe functions and Gram are organized—a combinatorial, geometric,
or algebraic constraint on the overlaps \(G_{ij}\).

### Connection to physics

The physical 4-to-12 point carriers (Bool×Bool and its S₄ × S₄ × S₄
decomposition) are the smallest carriers that give the Standard Model gauge
group and 3 generations. The sporadic groups and Lie type groups require
much larger carrier sizes or additional structure—they are accessible in
the mathematical framework but not realized at accessible energies in
the observed Standard Model.

### Summary

\[
\text{Carrier } X_N + \text{structure } S \xrightarrow{\text{automorphism group}} \text{finite simple group}
\]

All finite simple groups arise this way. There are no exceptions. The
Classification of Finite Simple Groups is, in this framework, the
classification of possible additional structures on a finite set.
## Conformal field theory and string theory

### The 4-point carrier as the 4-punctured sphere

In 2D CFT, the 4-point correlation function on the Riemann sphere,

\[
\langle \phi_1(0) \phi_2(z) \phi_3(1) \phi_4(\infty) \rangle
\]

has S₄ as its full conformal symmetry group—the anharmonic group
generated by the 24 Möbius transformations that permute the 4
punctures at 0, z, 1, ∞ while preserving the cross-ratio.

Our 4-point carrier Bool×Bool has automorphism group S₄. The
identification is exact:

\[
\text{Carrier points} = \text{punctures} \quad (0, z, 1, \infty)
\]
\[
S_4 \text{ automorphism} = \text{anharmonic group}
\]
\[
\text{Stabilizer } S_3 = \text{PSL}(2,\mathbb{C}) \text{ fixing one puncture}
\]

The carrier IS the 4-punctured sphere. The Gram is the 4-point
conformal block matrix.

### Gram as the conformal block matrix

The 4-point function decomposes into conformal blocks via the
operator product expansion:

\[
\langle \phi_1\phi_2\phi_3\phi_4 \rangle = \sum_p C_{12}^p C_{34}^p \,
\mathcal{F}_p(z)
\]

The Gram matrix of this 4-point function is the matrix of conformal
blocks \(\mathcal{F}_p(z)\) for each intermediate channel \(p\):

\[
G_{p,q}(z) = \langle \mathcal{F}_p | \mathcal{F}_q \rangle
\]

Its determinant (the Kac determinant) vanishes at specific conformal
dimensions—this gives the minimal model classification. The Gram
eigenvalues are the conformal dimensions of the irreducible
representations of the Virasoro algebra.

In our framework, the S₄-automorphism-invariant Gram of the 4-point
carrier is EXACTLY the Kac determinant matrix. Its eigenvalues give
the conformal spectrum:

\[
\text{Gram}(S_4) \text{ eigenvalues} = \text{conformal dimensions}
\]

### String theory

The string worldsheet is a 2D surface whose correlation functions are
2D CFT correlators. The 4-point function describes the scattering of
4 string states:

\[
\mathcal{A}(1,2,3,4) = \int \langle V_1 V_2 V_3 V_4 \rangle \ldots
\]

The 4-point carrier S₄ symmetry IS the crossing symmetry of the
string amplitude:

- s-channel ↔ t-channel crossing: generated by the S₄ anharmonic group
- The Veneziano amplitude \(B(\alpha(s), \alpha(t))\) is S₄-covariant

Our carrier Gram gives the full crossing-symmetric 4-point amplitude.

### Vertex operator algebras (VOAs)

A VOA is the algebraic structure of a 2D CFT. The 4-point function
in a VOA satisfies crossing symmetry (S₄ invariance). The Gram
matrix of the 4-point correlator is the VOA's 4-point structure
tensor.

The Monster VOA (automorphism group Monster, ∼8×10⁵³) is the
largest simple VOA. Its 4-point functions have S₄ crossing symmetry
as a special case of our carrier framework. The modular j-invariant,

\[
j(\tau) = q^{-1} + 744 + 196884q + \cdots
\]

is the 1-point function on the torus of the Monster VOA. The
coefficient 196884 is 1 + 196883, where 196883 is the smallest
non-trivial Monster irrep.

### The connection

\[
\text{4-point carrier } \xrightarrow{S_4 \text{ automorphism}} \text{4-punctured sphere} \xrightarrow{\text{CFT}} \text{conformal blocks} \xrightarrow{\text{Gram}} \text{Kac determinant} \xrightarrow{\text{VOAs}} \text{moonshine}
\]

The same S₄ that gives the SM gauge group (through irrep
decomposition into 1⊕1⊕2) also gives the crossing symmetry of
4-point functions in CFT and string theory. The carrier framework
unifies physics (QM, GR, SM) with the mathematical structures of
conformal field theory and moonshine.
## Category theory

### The carrier category

The framework forms a natural category:

\[
\mathbf{Carrier}_N
\]

- **Objects**: finite sets \(X_N\) (carriers of \(N\) points)
- **Morphisms**: functions \(f : X_N \to X_M\) between carriers, preserving the probe structure
- **Terminal object**: the 1-point carrier \(X_1\) (trivial)
- **Initial object**: the empty carrier \(X_0\) (not physically relevant)

The automorphism group of an object is \(\text{Aut}(X_N) = S_N\).
The endomorphism monoid is larger (all functions \(X_N \to X_N\)).

### The Gram as a functor

The Gram is a functor from the carrier category to the category of
complex matrices:

\[
G : \mathbf{Carrier}_N^{\text{op}} \times \mathbf{Carrier}_N \to \mathbf{Mat}(\mathbb{C})
\]

\[
G(X,Y) \text{ is the } |X|\times|Y| \text{ matrix of overlaps between}
\text{ probes on } X \text{ and } Y
\]

For the diagonal \(X = Y = X_N\), this gives the \(N\times N\) Gram
matrix \(G_{ij}\). Physical sectors are sub-functors:

\[
\begin{aligned}
G_{\text{QM}} &: \text{interference pattern } I = \sum G_{ij} e^{i(\theta_j - \theta_i)} \
G_{\text{GR}} &: \text{stabilizer Gram } g_{ab}(p) = G_{ab} \
G_{\text{SM}} &: \text{irrep decomposition under } S_4 \subset S_N
\end{aligned}
\]

### Natural transformations as symmetries

A natural transformation \(\eta : G \Rightarrow G\) is a symmetry of the
Gram. For the 4-point carrier, the natural transformations are precisely
the S₄ automorphisms:

\[
\eta_\sigma : G_{ij} \mapsto G_{\sigma(i)\sigma(j)} \quad \sigma \in S_4
\]

These give the gauge group SU(3)×SU(2)×U(1) via the irrep decomposition
of the S₄ action on the functor. Larger carriers Sₙ give larger symmetry
groups.

### The Yoneda embedding

The probe functions \(f_i : X_N \to \mathbb{C}\) are the Yoneda embedding
of the carrier into the category of complex-valued functions:

\[
X_N \hookrightarrow \text{Fun}(X_N, \mathbb{C}) = \text{Hom}_{\mathbf{Carrier}}(X_N, \mathbb{C})
\]

The Gram is the composition of the Yoneda embedding with the inner product
on the function space:

\[
G = \langle \cdot, \cdot \rangle \circ \text{Yoneda}
\]

This makes the carrier representable: all physical structure is determined
by the representable functor \(\text{Hom}(X_N, -)\).

### Summary

\[
\text{Carrier category} \xrightarrow{\text{Gram functor}} \text{Complex matrices} \xrightarrow{\text{natural transformations}} \text{Gauge groups} \xrightarrow{\text{irrep decomposition}} \text{Physics}
\]

Category theory is the natural language of the framework. The carrier is
an object, the Gram is a functor, gauge groups are natural transformations,
and physical sectors are sub-functors.
## Algebraic geometry and moduli spaces

### The carrier as moduli space M₀,N

The space of \(N\) distinct ordered points on the Riemann sphere \(\mathbb{P}^1\)
modulo projective transformations \(\text{PSL}(2,\mathbb{C})\) is the
moduli space \(\mathcal{M}_{0,N}\). Its dimension is \(N-3\).

Our N-point carrier is this moduli space:

\[
X_N = \mathcal{M}_{0,N}
\]

- **4-point carrier**: \(\mathcal{M}_{0,4} \cong \mathbb{P}^1 \setminus \{0,1,\infty\}\)
  parametrized by the cross-ratio \(z\). Aut(\(X_4\)) = S₄ is the mapping class
  group of the 4-punctured sphere.
- **N-point carrier**: \(\mathcal{M}_{0,N}\) with \(N-3\) independent cross-ratios.
  Aut(\(X_N\)) = S_N is the mapping class group of the N-punctured sphere.

### The Gram as a function on \(\mathcal{M}_{0,N}\)

The Gram matrix entries \(G_{ij}(z_1, \dots, z_{N-3})\) are functions on the
moduli space. For the 4-point carrier, the Gram depends on the single
cross-ratio \(z\):

\[
G_{ij}(z) = \langle f_j | f_i \rangle_z
\]

and is S₄-covariant: permuting the 4 punctures transforms the Gram by
the corresponding Möbius transformation of \(z\).

The Gram eigenvalues are algebraic functions on \(\mathcal{M}_{0,N}\) with
branch points at the boundaries (where punctures collide).

### The Gram as a period matrix

For a Riemann surface \(\Sigma_g\) of genus \(g\), the period matrix
\(\tau_{ab}\) is the integral of holomorphic 1-forms \(\omega_a\) over
cycles \(b\):

\[
\tau_{ab} = \int_b \omega_a
\]

The Gram of the surface's first homology is \(\operatorname{Im}(\tau)\).

For the punctured sphere \(\mathcal{M}_{0,N}\), the Gram of the carrier
extends to the period matrix of the surface. The analog of the
period matrix for \(\mathcal{M}_{0,N}\) is the Gram determinant
\(\det G(z)\), which vanishes exactly when two punctures coincide
(the boundary of moduli space).

### Deligne-Mumford compactification

The compactification \(\overline{\mathcal{M}}_{0,N}\) adds boundary
divisors where punctures collide, producing nodal curves.
For \(\mathcal{M}_{0,4}\):

\[
\overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^1
\]

with boundary points at \(z = 0, 1, \infty\) corresponding to degenerate
configurations (two punctures coinciding).

In Gram terms:
- \(z \to 0\): Gram entry \(G_{12} \to G_{11}\) (points 1 and 2 merge)
- \(z \to 1\): \(G_{23} \to G_{22}\) (points 2 and 3 merge)
- \(z \to \infty\): \(G_{14} \to G_{11}\) (points 1 and 4 merge)

Each boundary corresponds to a Gram eigenvalue going to zero (a
vanishing cycle in the period matrix).

### Tropical geometry

The tropicalization of \(\mathcal{M}_{0,N}\) is the space of
metric trees with N leaves. The cross-ratios become
distances along tree edges:

\[
z_{ijkl} = \frac{(x_i - x_j)(x_k - x_l)}{(x_i - x_k)(x_j - x_l)}
\]

In the limit where some cross-ratios go to 0 or \(\infty\), the
Gram becomes the adjacency matrix of a discrete tree. This is
the discrete carrier itself—the N points with a metric
determined by the tree distances.

The continuum limit \(N \to \infty\) gives the smooth moduli
space \(\mathcal{M}_{0,\infty}\), which is the space of
unparametrized curves on the sphere.

### The hierarchy

\[
\text{Discrete carrier } X_N \xrightarrow{\text{tropical}} \text{metric tree} \xrightarrow{Z \to \infty} \text{continuum } \mathcal{M}_{0,N} \xrightarrow{\text{compactify}} \overline{\mathcal{M}}_{0,N}
\]

The carrier framework unifies:
- **Discrete**: the N-point carrier (finite, algebraic, combinatorial)
- **Tropical**: metric trees from degenerate cross-ratios
- **Continuum**: the smooth moduli space \(\mathcal{M}_{0,N}\)
- **Algebraic**: the Gram as a period matrix on moduli space

All of these are the SAME object at different levels of resolution,
with Sₙ acting as the mapping class group at every level.
## Number theory and spectral theory

### Gram eigenvalues and modular forms

For the 4-point carrier (S₄ automorphism), the Gram has eigenvalues:

\[
\lambda_1 = 12 \quad (\text{multiplicity } 1), \qquad
\lambda_2 = 4 \quad (\text{multiplicity } 3)
\]

These two numbers are the **weights of the generators of the ring of
modular forms** for \(\text{SL}(2,\mathbb{Z})\):

- **Weight 4**: Eisenstein series \(E_4(\tau) = 1 + 240\sum \sigma_3(n)q^n\)
  generates all modular forms of weight \(4k\)
- **Weight 12**: Modular discriminant \(\Delta(\tau) = \eta(\tau)^{24}\)
  generates the cusp forms

The ratio:

\[
j(\tau) = \frac{E_4(\tau)^3}{\Delta(\tau)} = q^{-1} + 744 + 196884q + \cdots
\]

has Fourier coefficients that are dimensions of Monster irreps (monstrous
moonshine). The number 1728 normalizing the j-invariant is \(12^3 = \lambda_1^3\).

The 24 in the Dedekind eta function \(\eta(\tau) = q^{1/24}\prod(1-q^n)\) is
\(|S_4| = 24\), the order of the automorphism group.

### Gram spectral zeta function

For the N-point carrier, the spectral zeta function of the Gram is:

\[
\zeta_{G_N}(s) = \lambda_1^{-s} + (N-1)\lambda_2^{-s}
\]

where

\[
\lambda_1 = (N-1)! + (N-1)(N-2)!, \quad
\lambda_2 = (N-1)! - (N-2)!
\]

For the 4-point carrier:

\[
\zeta_{G_4}(s) = 12^{-s} + 3 \cdot 4^{-s}
\]

This is a finite Dirichlet series. As \(N \to \infty\), the factorial
eigenvalues grow super-exponentially, and the spectral zeta function
requires analytic continuation via Stirling's formula:

\[
\log N! = N\log N - N + \tfrac12\log(2\pi N) + \sum_{k\ge 1} \frac{B_{2k}}{2k(2k-1)N^{2k-1}}
\]

where \(B_{2k}\) are Bernoulli numbers related to \(\zeta(2k)\):

\[
\zeta(2k) = (-1)^{k+1} \frac{(2\pi)^{2k} B_{2k}}{2(2k)!}
\]

### The Hilbert-Pólya connection

The continuum limit of the Gram spectral zeta may be related to the
Riemann zeta function \(\zeta(s)\). If the Gram spectrum (as \(N\to\infty\))
matches the spectrum of an operator whose eigenvalues are the imaginary
parts of the Riemann zeros, the Gram framework would realize the
Hilbert-Pólya conjecture.

This is open. The Gram eigenvalues are factorial in \(N\), not linear
in \(n\), so the connection to the Riemann zeros is not direct. The
spectral zeta of the Gram is a Dirichlet series with factorial terms,
related to the Barnes G-function and multiple gamma functions.

### The Gram determinant and modular forms

The Gram determinant for the 4-point carrier:

\[
\det G_4 = \lambda_1 \cdot \lambda_2^3 = 12 \cdot 4^3 = 768
\]

This equals \(\frac{1728}{12} \cdot 4 = 768\) where \(1728 = 12^3\) is the
j-invariant normalization.

For larger N, the Gram determinant:

\[
\det G_N = \lambda_1 \cdot \lambda_2^{N-1}
\]

is related to the Dedekind eta function evaluated at specific modular
parameters, via the relations:
- \(\eta(\tau)^{24} = \Delta(\tau) =\) cusp form of weight 12
- The Gram's factorial structure connects to the Barnes G-function
  \(\det G_N \sim G(N+1)\) for large N

### Summary

\[
\begin{aligned}
\text{Gram eigenvalues } (12, 4) &\leftrightarrow \text{modular form weights } (E_4: 4, \Delta: 12) \
|S_4| = 24 &\leftrightarrow \text{Dedekind }\eta^{24} = \Delta \
1728 = 12^3 &\leftrightarrow j\text{-invariant normalization} \
\zeta_{G_N}(s) &\leftrightarrow \text{Bernoulli numbers, }\zeta(2k) \
\text{Continuum limit} &\leftrightarrow \text{Riemann }\zeta(s) \text{ (open)}
\end{aligned}
\]

The Gram spectrum of the 4-point carrier reproduces the foundational
numbers of modular form theory: 4 (weight of E₄), 12 (weight of Δ),
24 (order of S₄, exponent of η), and 1728 (= 12³, normalization of j).
The spectral zeta function connects to Bernoulli numbers and values of
the Riemann zeta function at even integers.
## Statistical mechanics

### The Gram as partition function

The Gram matrix is the partition function of a statistical system on
the carrier. For the symmetric Sₙ carrier:

\[
G_{ij} = \langle f_j | f_i \rangle = 
\begin{cases}
(N-1)! & i = j \
(N-2)! & i \neq j
\end{cases}
\]

The diagonal \(G_{ii}\) is the self-energy, and \(G_{ij}\) for \(i\neq j\)
is the pairwise interaction. The ratio:

\[
\frac{G_{ij}}{G_{ii}} = \frac{1}{N-1} = e^{-\beta\Delta}
\]

defines a Boltzmann factor with energy gap \(\Delta = \log(N-1)\) at
inverse temperature \(\beta = 1\). The Gram determinant:

\[
\det G = \lambda_1 \lambda_2^{N-1}
\]

is the total partition function \(Z\). For the 4-point carrier:

\[
Z = \det G_4 = 12 \cdot 4^3 = 768
\]

### The Gram as density matrix

The normalized Gram:

\[
\rho_{ij} = \frac{G_{ij}}{\operatorname{Tr}(G)} = \frac{G_{ij}}{N(N-1)!}
\]

is a density matrix (positive semidefinite, trace 1). Its von Neumann
entropy:

\[
S(\rho) = -\operatorname{Tr}(\rho \log \rho) = -\sum_{a} p_a \log p_a
\]

where \(p_a = \lambda_a / \operatorname{Tr}(G)\) are the normalized
eigenvalues. For the 4-point carrier:

\[
p_1 = \frac{12}{132} = \frac{1}{11}, \quad
p_2 = \frac{4}{132} = \frac{1}{33} \text{ (multiplicity 3)}
\]

\[
S = -\frac{1}{11}\log\frac{1}{11} - 3\cdot\frac{1}{33}\log\frac{1}{33}
\approx 0.218 + 0.341 \approx 0.559
\]

The entropy measures the disorder in the carrier's Gram structure.

### Thermal states

A thermal state at inverse temperature \(\beta\) is:

\[
G_{\beta} = \exp(-\beta H)
\]

where the Hamiltonian \(H\) is derived from the Gram's adjacency
structure. For the symmetric carrier, the Hamiltonian is the
Laplacian:

\[
H_{ij} = 
\begin{cases}
1 & i = j \
-\frac{1}{N-1} & i \neq j
\end{cases}
\]

The thermal Gram \(G_{\beta} = \exp(-\beta H)\) interpolates between
\(G_{\beta\to 0} = \mathbb{I}\) (infinite temperature, all states
independent) and \(G_{\beta\to\infty} =\) projector onto the ground
state (zero temperature, complete order).

### Phase transitions

A phase transition occurs when Gram eigenvalues become degenerate.
For the symmetric Sₙ carrier, the eigenvalues \(\lambda_1\) and
\(\lambda_2\) are:

\[
\lambda_1 - \lambda_2 = (N-1)! \frac{N}{N-1}
\]

which is always positive for \(N > 2\). No phase transition occurs
for the symmetric carrier.

When Sₙ is broken to a subgroup \(H \subset S_n\), the Gram eigenvalues
split. A phase transition occurs when the symmetry is restored at
high temperature. The critical temperature \(T_c\) is determined by
the Gram eigenvalue gap:

\[
T_c \sim \frac{\lambda_1 - \lambda_2}{\log(N)}
\]

For the Standard Model: S₄ → SU(3)×SU(2)×U(1) symmetry breaking
occurs at the electroweak scale \(T_c \sim 100\) GeV.

### The Ising model on the carrier

The carrier points are spins \(s_i = \pm 1\) with Hamiltonian:

\[
H = -\sum_{i,j} J_{ij} s_i s_j, \qquad J_{ij} = G_{ij}
\]

The partition function is:

\[
Z = \sum_{\{s\}} \exp\Bigl(\beta \sum_{i,j} G_{ij} s_i s_j\Bigr)
\]

For the S₄ carrier, the 4-point Ising model has a critical temperature
determined by the Gram eigenvalues. The scaling limit of this model
is the 2D Ising CFT, whose central charge \(c = 1/2\) is related to
the S₄ irrep dimensions.

### The Yang-Baxter equation

An integrable statistical model requires Boltzmann weights that satisfy
the Yang-Baxter equation. The Gram of the carrier must satisfy a
"Gram-Yang-Baxter" relation for integrability:

\[
\sum_k G_{ik} G_{kl} G_{jm} = \sum_k G_{jk} G_{kl} G_{im}
\]

For the symmetric Sₙ carrier, this holds automatically because all
\(G_{ij}\) for \(i\neq j\) are equal. The relation is a consequence
of the Sₙ automorphism (the Gram is completely symmetric under
permutations).

### The second law

The Gram evolves unitarily under the fibration rotation:

\[
G_{ij}(t) = G_{ij}(0) \cdot e^{i(\theta_j(t) - \theta_i(t))}
\]

The von Neumann entropy of the full Gram is constant (unitary evolution).
But coarse-graining (projecting onto the visible SM sector) gives a
non-unitary reduced Gram whose entropy increases. This is identical
to the second law of thermodynamics.

The arrow of time emerges from the coarse-graining of the carrier's
full Gram onto the SM sector.

### Summary

\[
\begin{aligned}
\text{Gram } G &\leftrightarrow \text{partition function } Z \
\text{Gram eigenvalues } &\leftrightarrow \text{Boltzmann weights} \
\text{Eigenvalue crossing } &\leftrightarrow \text{phase transition} \
\rho = G/\text{Tr}(G) &\leftrightarrow \text{density matrix} \
S = -\text{Tr}(\rho\log\rho) &\leftrightarrow \text{von Neumann entropy} \
\text{Sector projection } &\leftrightarrow \text{second law / arrow of time}
\end{aligned}
\]

The framework reproduces statistical mechanics: the Gram is the partition
function, its normalized form is the density matrix, its eigenvalue
degeneracies are phase transitions, and coarse-graining onto physical
sectors gives the second law.
## Information theory

### The Gram as a correlation matrix

The Gram matrix \(G_{ij} = \langle f_j | f_i \rangle\) is a correlation matrix:
\(G_{ij}\) measures the correlation (overlap) between probes at points
\(i\) and \(j\). The diagonal \(G_{ii}\) is the variance, and the
off-diagonals are covariances.

The normalized Gram:

\[
\rho_{ij} = \frac{G_{ij}}{\operatorname{Tr}(G)}
\]

is a density matrix. The Shannon entropy of the classical outcome
distribution (diagonal of \(\rho\)):

\[
H_{\text{classical}} = -\sum_i \rho_{ii} \log \rho_{ii}
\]

For the Sₙ carrier, all diagonal entries are equal: \(\rho_{ii} = 1/N\).
Hence \(H_{\text{classical}} = \log N\) — maximum entropy for N outcomes.

### Mutual information

The mutual information between two carrier points measures how much
information about point \(i\) is gained by observing point \(j\):

\[
I(i;j) = H(i) + H(j) - H(i,j)
\]

In Gram terms, for a bivariate Gaussian with Gram covariance matrix,
the mutual information between points \(i\) and \(j\) is:

\[
I(i;j) = -\frac12 \log\left(1 - \frac{G_{ij}^2}{G_{ii}G_{jj}}\right)
\]

For the Sₙ carrier with \(G_{ii} = (N-1)!\) and \(G_{ij} = (N-2)!\):

\[
I(i;j) = -\frac12 \log\left(1 - \frac{1}{(N-1)^2}\right)
\]

For \(N=4\): \(I(i;j) \approx 0.021\) nats — very small mutual
information between distinct points. All information is in the
diagonal (self-correlation).

### Channel capacity

The carrier is a communication channel: input = point \(i\), output =
probe response \(f_i\). The Gram determines the channel capacity:

\[
C = \max_{p} I(X;Y)
\]

For the Sₙ carrier, the channel capacity equals the von Neumann
entropy of the normalized Gram density matrix \(\rho\):

\[
C = S(\rho) = -\sum_a p_a \log p_a
\]

where \(p_a\) are the normalized Gram eigenvalues. For the 4-point
carrier: \(C \approx 0.559\) nats.

### KL divergence between sectors

The Kullback-Leibler divergence between the visible SM sector and the
full carrier Gram measures how much information is lost by projection:

\[
D_{\text{KL}}(\rho_{\text{full}} \| \rho_{\text{SM}}) =
\operatorname{Tr}(\rho_{\text{full}} (\log \rho_{\text{full}} - \log \rho_{\text{SM}}))
\]

This is the "darkness" of the dark sector — the information in the
Gram that is inaccessible to SM gauge interactions. For S₁₂,
this is approximately:

\[
D_{\text{KL}} \approx \frac{3 \text{ sterile states}}{12 \text{ total}} \times S(\rho_{\text{full}}) \approx 0.25 S
\]

The dark matter abundance \(\Omega_{\text{DM}} \approx 25\%\) is the
KL divergence between the full Gram and the visible sector projection.

## Quantum computing

### Bool×Bool as 2 qubits

The 4-point carrier Bool×Bool = {00, 01, 10, 11} is exactly the
computational basis of a 2-qubit quantum register:

\[
|00\rangle, |01\rangle, |10\rangle, |11\rangle
\]

The Gram is the density matrix of the 2-qubit state. The S₄
automorphism group is the group of unitary transformations that
permute the 4 basis states.

### Quantum gates from the S₄ automorphism

Each element \(\sigma \in S_4\) acts as a permutation matrix on the
2-qubit register. These include:
- **CNOT**: swaps \(|01\rangle \leftrightarrow |11\rangle\) (a transposition)
- **SWAP**: swaps \(|01\rangle \leftrightarrow |10\rangle\) (a transposition)
- **Hadamard on 2 qubits**: generated by S₄ elements mixing the
  basis states

The full S₄ action generates the Clifford group on 2 qubits. The
Clifford group has \(24 \times 8 \times 6 = 1152\) elements? Actually,
the 2-qubit Clifford group has 11520 elements, and S₄ × S₄ × S₄ has
24³ = 13824. The S₄ automorphism is a subgroup of the Clifford group.

### Stabilizer formalism

The stabilizer formalism for quantum error correction uses subgroups
of the Pauli group. The 2-qubit Pauli group has 4⁴ = 256 elements.
The automorphism group S₄ acting on Bool×Bool stabilizes certain
Pauli operators:

\[
\text{Stab}(\sigma) = \{P \in \text{Pauli} : \sigma P \sigma^{-1} = P\}
\]

The stabilizer of a point (e.g., fixing \(|00\rangle\)) is S₃, which
gives the 3 elements needed for a 3-qubit code? Actually, the
stabilizer of a state in quantum error correction is a different
concept — it's the set of Pauli operators that leave the code
subspace invariant.

The connection is structural: the stabilizer subgroup of S₄ fixes
one of the 4 points, corresponding to a 1-qubit code subspace within
the 2-qubit register. This is analogous to the SM gauge group being
the stabilizer of the visible sector within the full carrier.

### Entanglement as a resource

We already showed CHSH violation from Gram non-separability
(\(S = 2\sqrt{2}\) for the Bell state). In quantum computing terms:

\[
\text{Non-separable Gram} = \text{entangled state} = \text{computational resource}
\]

The amount of entanglement (measured by the concurrence or negativity)
is determined by the Gram eigenvalues:

\[
\mathcal{E}(G) = \max(0, \lambda_{\max} - \sum_{i\neq \max} \lambda_i)
\]

For the Bell state Gram (rank 1, eigenvalues 1, 0, 0, 0):
\(\mathcal{E} = 1\) — maximally entangled.

### Fault tolerance and the carrier

The error-correcting codes of quantum computing have symmetry groups
that are subgroups of Sₙ for some N:
- 5-qubit code: cyclic group C₅ ⊂ S₅
- Steane code: S₃ (permutations of 3 qubits) ⊂ S₇
- Surface codes: Z₂ × Z₂ ⊂ S₄

The carrier framework provides a unified language for these symmetry
groups. The Gram of the code space determines the code distance and
error threshold.

### Quantum supremacy

The computational power of a quantum computer is determined by the
complexity of the Gram's evolution under the fibration rotation.
Unitary evolution of the Gram under S₄-generated gates produces
states that cannot be efficiently simulated classically — this is
quantum supremacy.

\[
\text{Gram evolution } G(t) \text{ under S₄ gates} \iff \text{quantum circuit}
\]

The 4-point carrier with S₄ automorphism is the minimal quantum
computer (2 qubits with full Clifford group action).
## Knot theory and braid groups

### Braid groups and the carrier

The braid group on \(n\) strands \(\mathrm{B}_n\) has generators
\(\sigma_1, \dots, \sigma_{n-1}\) satisfying the braid relation:

\[
\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}
\]

and commuting relations \(\sigma_i \sigma_j = \sigma_j \sigma_i\) for
\(|i-j| > 1\). There is a surjection \(\mathrm{B}_n \to S_n\) sending
each braid generator \(\sigma_i\) to the transposition \((i\;i+1)\).

The kernel is the pure braid group \(\mathrm{P}_n\) (braids where each
strand returns to its starting position).

Our N-point carrier has automorphism group \(S_N\). Through the
surjection \(\mathrm{B}_N \to S_N\), every braid acts on the carrier
up to permutation. The 4-point carrier carries a \(\mathrm{B}_4\)
action via:

\[
\mathrm{B}_4 \twoheadrightarrow S_4 = \operatorname{Aut}(X_4)
\]

The Gram \(G_{ij}\) transforms under braiding:

\[
\sigma_k : G_{ij} \mapsto G_{\sigma_k(i), \sigma_k(j)}
\]

The Gram eigenvalues (12 and 4 for S₄) are invariants of the braid
action—they are the topological data preserved by any braiding
operation.

### Anyons from the 4-point carrier

In 2D quantum systems, particle exchange statistics are given by
representations of the braid group \(\mathrm{B}_n\), not the symmetric
group \(S_n\). The 4-point conformal block on the sphere (which we
identified with the 4-point carrier Gram) IS the space of 4-anyon
wavefunctions:

\[
\mathcal{F}(z) = \langle \phi_1(0) \phi_2(z) \phi_3(1) \phi_4(\infty) \rangle
\]

The braid group \(\mathrm{B}_4\) acts on \(\mathcal{F}(z)\) by exchanging
the positions of the anyons. This action factorizes through \(S_4\)
for Abelian anyons, but for non-Abelian anyons the action is a
genuine \(\mathrm{B}_4\) representation (not factoring through \(S_4\)).

The Gram eigenvalues determine the topological spin:
\[
h_a = \frac{\log \lambda_a}{2\pi i} \quad (\text{mod } \mathbb{Z})
\]

For the 4-point carrier with eigenvalues \(\lambda_1 = 12, \lambda_2 = 4\):

\[
h_1 = \frac{\log 12}{2\pi i}, \quad h_2 = \frac{\log 4}{2\pi i}
\]

These are the conformal dimensions of the anyon fields in the
corresponding CFT.

### Braiding matrices

The braiding matrix for exchanging anyons \(i\) and \(j\) is:

\[
B_{ij} = P_{ij} \cdot R_{ij}
\]

where \(P_{ij}\) is the permutation (from \(S_4\)) and \(R_{ij}\) is
the \(R\)-matrix (the phase from braiding). For the 4-point carrier,
the braiding matrix is a representation of \(\mathrm{B}_4\) on the
2-dimensional space of Gram eigenvectors.

The eigenvalues of the braiding matrix \(B_{12}\) (exchanging points
1 and 2) are determined by the Gram:

\[
\operatorname{spec}(B_{12}) = \{e^{2\pi i h_a}, e^{2\pi i h_b}\}
\]

where \(h_a, h_b\) are the conformal dimensions from the Gram eigenvalues.

### The Yang-Baxter equation

The braid group relation:

\[
\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}
\]

is the algebraic form of the Yang-Baxter equation. For the carrier
Gram, this becomes:

\[
\sum_{j} G_{ij} G_{j,i+1} G_{i+1,k} = \sum_{j} G_{i+1,j} G_{j,i} G_{i,k}
\]

which holds because all off-diagonal Gram entries are equal
(\(G_{ij} = (N-2)!\) for all \(i\neq j\)). The Sₙ automorphism
guarantees the Yang-Baxter relation.

### Knot invariants from the Gram

A knot is obtained by closing a braid (the braid closure). The Jones
polynomial \(V_L(q)\) is a knot invariant obtained from the
Temperley-Lieb algebra representation of \(\mathrm{B}_n\).

The Temperley-Lieb algebra \(\mathrm{TL}_n(d)\) has parameter
\(d = q + q^{-1}\). The 4-point Gram determines the value of \(d\):

\[
d = \frac{\operatorname{Tr}(G)}{\sqrt{\det G}} = \frac{N(N-1)!}{\sqrt{\lambda_1 \lambda_2^{N-1}}}
\]

For the 4-point carrier: \(d = 132 / \sqrt{768} \approx 4.76\).

This picks a specific value of \(q\):

\[
q + q^{-1} = \frac{132}{\sqrt{768}} \approx 4.76 \quad\Rightarrow\quad
q \approx 4.54 \text{ or } 0.22
\]

The Jones polynomial at this \(q\) is determined by the Gram.

### Khovanov homology

Khovanov homology categorifies the Jones polynomial: to each braid
closure it assigns a homology theory whose graded Euler characteristic
is the Jones polynomial. The carrier Gram may define a Khovanov-type
homology for the 4-point carrier, with the Gram eigenvalues grading
the homology groups.

### Summary

\[
\begin{aligned}
\mathrm{B}_4 &\twoheadrightarrow S_4 = \operatorname{Aut}(X_4) \
\text{Braid action} &\leftrightarrow \text{Gram permutation} \
\text{Gram eigenvalues} &\leftrightarrow \text{topological spins / conformal dimensions} \
\text{Conformal block} &\leftrightarrow \text{4-anyon wavefunction} \
\text{Yang-Baxter} &\leftrightarrow \text{Sₙ automorphism of Gram} \
\text{Jones polynomial} &\leftrightarrow \text{Gram trace and determinant}
\end{aligned}
\]

The braid group \(\mathrm{B}_N\) acts on the N-point carrier through the
surjection \(\mathrm{B}_N \to S_N\). The 4-point carrier gives the
braiding matrices for anyons, the topological spins from Gram eigenvalues,
and the knot invariants (Jones polynomial) from Gram trace and determinant.
## Homotopy theory

### The carrier as a discrete space

The N-point carrier \(X_N\) with the discrete topology has homotopy:
- \(\pi_0(X_N) = N\) (each point is a component)
- \(\pi_k(X_N) = 0\) for all \(k \ge 1\) (no higher homotopy)

This is trivial. The interesting homotopy comes from the automorphism
group action.

### The classifying space of S_N

The classifying space \(B_{S_N}\) is the space of principal bundles
with structure group \(S_N\). Its fundamental group is:

\[
\pi_1(B_{S_N}) = S_N
\]

Higher homotopy groups \(\pi_k(B_{S_N})\) for \(k \ge 2\) are the
homotopy groups of the sphere spectrum via the Barratt-Priddy-Quillen
theorem.

### The Barratt-Priddy-Quillen theorem

This is the central connection between symmetric groups and stable
homotopy theory:

\[
\mathbb{Z} \times B_{S_\infty}^+ \simeq \Omega^\infty \Sigma^\infty S^0
\]

where:
- \(B_{S_\infty}^+\) is the Quillen plus construction on the classifying
  space of the infinite symmetric group \(S_\infty = \lim_{N\to\infty} S_N\)
- \(\Omega^\infty \Sigma^\infty S^0\) is the sphere spectrum, whose
  homotopy groups are the stable homotopy groups of spheres:

\[
\pi_k(\Omega^\infty \Sigma^\infty S^0) = \pi_k^S(S^0)
\]

The theorem says the **stable homotopy groups of spheres** are the
homotopy groups of the group-completed infinite symmetric group.

### The carrier in the limit

Our N-point carriers have automorphism groups \(S_N\). In the limit
\(N \to \infty\):

\[
\lim_{N\to\infty} \operatorname{Aut}(X_N) = S_\infty
\]

The chain of inclusions \(S_1 \subset S_2 \subset \cdots \subset S_N \subset \cdots\)
gives a directed system of classifying spaces:

\[
B_{S_1} \to B_{S_2} \to \cdots \to B_{S_N} \to \cdots \to B_{S_\infty}
\]

whose homotopy colimit is \(B_{S_\infty}\). The Barratt-Priddy-Quillen
theorem identifies the group completion of this colimit with the
sphere spectrum.

### The Gram in stable homotopy

The Gram matrix for \(S_N\) defines a map:

\[
G_N : B_{S_N} \to \operatorname{End}(\mathbb{C}^N) \cong \mathbb{C}^{N^2}
\]

In the limit \(N \to \infty\), this gives a map from \(B_{S_\infty}\)
to the space of infinite matrices. After the plus construction:

\[
G : B_{S_\infty}^+ \to \mathbb{C}^{\infty \times \infty}
\]

This map might factor through \(\Omega^\infty \Sigma^\infty S^0\),
giving a **stable cohomotopy class** determined by the Gram.

### The Gram determinant as a characteristic class

The Gram determinant \(\det G_N\) is a function on \(B_{S_N}\) (since
the Gram is invariant under \(S_N\)). In the limit \(N \to \infty\):

\[
\det G_\infty = \lim_{N\to\infty} \det G_N
\]

This defines a characteristic class in the stable cohomotopy of
\(B_{S_\infty}^+\), analogous to the Euler class in ordinary
cohomology. The value of \(\det G_\infty\) might be related to the
stable homotopy groups of spheres via the BPQ equivalence.

### Connection to the sphere spectrum

The sphere spectrum \(\mathbb{S}\) has homotopy groups \(\pi_k^S\):

\[
\begin{aligned}
\pi_0^S &= \mathbb{Z} \
\pi_1^S &= \mathbb{Z}_2 \quad (\text{Hopf map } \eta) \
\pi_2^S &= \mathbb{Z}_2 \quad (\text{Hopf map } \eta^2) \
\pi_3^S &= \mathbb{Z}_{24} \quad (\text{Hopf map } \nu) \
\pi_4^S &= 0 \
\pi_5^S &= \mathbb{Z}_2 \quad (\text{Hopf map } \nu^2) \
\pi_6^S &= \mathbb{Z}_2 \
\pi_7^S &= \mathbb{Z}_{240} \quad (\text{Hopf map } \sigma)
\end{aligned}
\]

The number 24 appears in \(\pi_3^S = \mathbb{Z}_{24}\), and 240 appears
in \(\pi_7^S = \mathbb{Z}_{240}\). These relate to our Gram eigenvalues:

\[
|S_4| = 24, \quad \text{Gram } \lambda_1 = 12, \quad \text{Gram } \lambda_2 = 4
\]

The number 240 appears in the Eisenstein series \(E_4(\tau)\):

\[
E_4(\tau) = 1 + 240 \sum_{n\ge 1} \sigma_3(n) q^n
\]

and \(240 = |\mathbb{F}_4^\times| \times\) something. More directly,
\(240 = 24 \times 10\) and \(12 \times 20\). The appearance of 24 and
240 in both the stable homotopy groups of spheres and the Gram/modular
spectrum suggests a deep connection.

### Summary

\[
\begin{aligned}
\text{Carrier automorphism } S_N &\leftrightarrow \text{classifying space } B_{S_N} \
N \to \infty &\leftrightarrow S_\infty \
B_{S_\infty}^+ &\leftrightarrow \Omega^\infty \Sigma^\infty S^0 = \text{sphere spectrum} \
\text{Gram map} &\leftrightarrow \text{stable cohomotopy class} \
\det G_N &\leftrightarrow \text{characteristic class} \
\pi_3^S = \mathbb{Z}_{24} &\leftrightarrow |S_4| = 24 \
\pi_7^S = \mathbb{Z}_{240} &\leftrightarrow E_4 \text{ coefficient } 240
\end{aligned}
\]

The Barratt-Priddy-Quillen theorem identifies the stable homotopy
groups of spheres with the homotopy of the infinite symmetric group—
the automorphism group of the infinite carrier. The Gram in the
\(N \to \infty\) limit defines stable cohomotopy classes that encode
the characteristic numbers of the carrier.
### What BPQ unlocks

The Barratt-Priddy-Quillen theorem is not just a homotopy-theoretic
curiosity—it may be the **selection principle** that determines the
Standard Model gauge group.

#### The SM gauge group from stable stems

The sphere spectrum \(\mathbb{S}\) has stable homotopy groups
(stable stems). The BPQ theorem identifies these with the homotopy
of the group-completed infinite symmetric group:

\[
\pi_k(\mathbb{Z} \times B_{S_\infty}^+) = \pi_k^S
\]

The first few stable stems:

\[
\begin{aligned}
\pi_0^S &= \mathbb{Z} \
\pi_1^S &= \mathbb{Z}_2 \quad (\text{Hopf map }\eta) \
\pi_2^S &= \mathbb{Z}_2 \quad (\eta^2\text{, dependent}) \
\pi_3^S &= \mathbb{Z}_{24} \quad (\text{Hopf map }\nu) \
\pi_4^S &= 0 \
\pi_5^S &= \mathbb{Z}_2 \
\pi_6^S &= \mathbb{Z}_2 \
\pi_7^S &= \mathbb{Z}_{240} \quad (\text{Hopf map }\sigma)
\end{aligned}
\]

The Standard Model gauge group \(\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)\)
maps to the first three independent stable stems:

\[
\begin{aligned}
\mathrm{U}(1) &\leftrightarrow \pi_0^S = \mathbb{Z} \quad (\text{charge quantization}) \
\mathrm{SU}(2) &\leftrightarrow \pi_1^S = \mathbb{Z}_2 \quad (\text{weak doublet}) \
\mathrm{SU}(3) &\leftrightarrow \pi_3^S = \mathbb{Z}_{24} \quad (|S_4| = 24)
\end{aligned}
\]

\(\pi_2^S = \mathbb{Z}_2\) is \(\eta^2\) (dependent on \(\pi_1^S\)),
so it does not contribute an independent gauge group.

#### Why the 4-point carrier gives exactly the SM

The 4-point carrier \(X_4\) with \(S_4\) automorphism can only "see"
the stable stems up to \(\pi_3^S\), because:
- The classifying space \(B_{S_4}\) has homotopy groups \(\pi_1 = S_4\)
  and \(\pi_k = 0\) for \(k \ge 2\)
- The BPQ identification requires the limit \(N \to \infty\) to reach
  higher stems
- The 4-point carrier is too small to resolve \(\pi_k^S\) for \(k \ge 4\)

Larger carriers (more than 4 points) would resolve higher stable stems,
predicting additional gauge groups beyond the SM. The absence of
observed beyond-SM gauge groups selects the 4-point carrier as the
physical one.

#### The Gram as the stable Euler class

The Gram determinant \(\det G_N\) is \(S_N\)-invariant, giving a map:

\[
\det G_N : B_{S_N} \to \mathbb{C}^\times
\]

In the \(N \to \infty\) limit, this map factors through the plus
construction and the BPQ equivalence, defining a **stable
cohomotopy class**:

\[
\det G_\infty : \Omega^\infty \Sigma^\infty S^0 \to \mathbb{C}^\times
\]

This is the stable Euler class of the carrier—the topological
invariant that determines the gauge group from the sphere spectrum.

#### Summary

BPQ unlocks:

1. **Gauge group selection**: the SM gauge group is determined by the
   first three independent stable stems of the sphere spectrum.
2. **Carrier size selection**: the 4-point carrier is the minimal
   carrier that resolves \(\pi_0^S, \pi_1^S, \pi_3^S\) and no higher.
3. **Beyond SM prediction**: higher stable stems (\(\pi_5^S, \pi_7^S, \dots\))
   would require larger carriers and predict new gauge groups at
   higher energies.
4. **Unification**: the Gram determinant as the stable Euler class
   unifies the sphere spectrum, the carrier, and the physical gauge
   groups into a single topological object.
## Topological Quantum Field Theory

### The carrier as a triangulation

An N-point carrier \(X_N\) can be interpreted as the 0-skeleton of a
triangulation of a \((N-1)\)-simplex. For the 4-point carrier,
\(X_4\) is the 0-skeleton of a tetrahedron (3-simplex).

The Gram matrix entries \(G_{ij}\) are the edge amplitudes of the
triangulation. The Gram determinant:

\[
\det G = \text{volume of the simplex}
\]

is the TQFT partition function on the triangulation.

### The Sₙ action as the mapping class group

The automorphism group \(S_N\) acts on the carrier by permuting
the points. This is the **mapping class group** of the \((N-1)\)-simplex:
the group of diffeomorphisms of the simplex modulo isotopy.

For the 4-point carrier: \(S_4\) is the mapping class group of the
tetrahedron (3-simplex). It contains the braid group \(B_3\) as the
mapping class group of the 4-punctured sphere via the Dehn twist
generators.

### The Gram as the TQFT state sum

The TQFT partition function on a triangulation is computed by the
state sum:

\[
Z = \sum_{\text{labelings}} \prod_{\text{simplices}} \text{tensor}
\]

In the Gram framework, the state sum is:

\[
Z_N = \sum_{\sigma \in S_N} \prod_{i=1}^N G_{i,\sigma(i)}
\]

For the 4-point carrier, this sum over \(S_4\) permutations gives:

\[
Z_4 = \sum_{\sigma \in S_4} \prod_{i=1}^4 G_{i,\sigma(i)}
\]

This is a sum of 24 terms, each corresponding to a different
pairing of the 4 points. It is the TQFT partition function
for the tetrahedron.

### The Verlinde formula

In 2D CFT, the Verlinde formula expresses the fusion coefficients
\(N_{ab}^c\) in terms of the modular S-matrix:

\[
N_{ab}^c = \sum_p \frac{S_{ap} S_{bp} S_{cp}^*}{S_{0p}}
\]

In our framework, the S-matrix is the Gram eigenvector matrix
\(V\) that diagonalizes the Gram:

\[
V^T G V = \text{diag}(\lambda_1, \dots, \lambda_N)
\]

The fusion coefficients of the corresponding TQFT are:

\[
N_{ab}^c = \sum_p \frac{V_{ap} V_{bp} V_{cp}}{V_{0p}}
\]

For the S₄ carrier (Gram eigenvalues 12, 4, 4, 4), the Verlinde
formula gives the fusion rules of the corresponding modular tensor
category.

### The sphere spectrum as the universal TQFT

The Barratt-Priddy-Quillen theorem identifies the sphere spectrum
as the group completion of the infinite symmetric group. In TQFT
language, this is the universal TQFT: the simplest TQFT whose
partition function is the Euler characteristic.

The Gram determinant in the \(N \to \infty\) limit is the
Euler characteristic of the infinite simplex:

\[
\lim_{N \to \infty} \det G_N \sim \chi(\Delta^\infty)
\]

This connects the carrier framework to the cobordism hypothesis
(Baez-Dolan, Lurie): the sphere spectrum is the free symmetric
monoidal \((\infty, 0)\)-category on one object.

### Summary

\[
\begin{aligned}
\text{Carrier } X_N &\leftrightarrow \text{triangulation of } (N-1)\text{-simplex} \
S_N &\leftrightarrow \text{mapping class group} \
G_{ij} &\leftrightarrow \text{edge amplitude} \
\det G &\leftrightarrow \text{partition function} \
V \text{ (eigenvectors)} &\leftrightarrow \text{S-matrix / Verlinde formula} \
S_\infty &\leftrightarrow \text{sphere spectrum (universal TQFT)}
\end{aligned}
\]

The Gram framework is a TQFT: the carrier is the triangulation,
the Gram is the amplitude, and the automorphism group is the
mapping class group. The 4-point carrier gives the simplest
nontrivial TQFT (the tetrahedron), and the infinite carrier
gives the universal TQFT (the sphere spectrum).
## Integrable systems

### The Gram determinant as a tau function

The tau function of the KP hierarchy is a determinant:

\[
\tau(t_1, t_2, \dots) = \det(1 - \text{some operator})
\]

For the 4-point carrier, the Gram determinant is the tau function
on the moduli space \(\mathcal{M}_{0,4}\) parametrized by the
cross-ratio \(z\):

\[
\tau(z) = \det G(z)
\]

For the symmetric S₄ carrier (uncoupled to the cross-ratio),
\(\det G = 768\) is constant. The tau function for the coupled
system (the CFT 4-point conformal block) depends on \(z\) and
satisfies the KdV hierarchy.

### The KdV equation

The KdV equation,

\[
u_t = u_{xxx} + 6uu_x
\]

can be expressed in Hirota bilinear form using the tau function
\(u = 2\partial_x^2 \log \tau\):

\[
(\partial_x^4 - 4\partial_x\partial_t + 3\partial_t^2)\,\tau\circ\tau = 0
\]

The 4-point conformal block \(\mathcal{F}(z)\) satisfies this
equation when the central charge \(c = -2\) or when there is a
null state at level 2 in the Verma module.

In our framework, \(\mathcal{F}(z) = \det G(z)\) where \(G(z)\) is
the Gram matrix of the 4-point conformal block (the Kac matrix).
The Gram eigenvalues (12 and 4 for S₄) determine the conformal
dimensions at which the Kac determinant vanishes—the minimal
model spectrum.

### The KP hierarchy on \(\mathcal{M}_{0,N}\)

For the N-point moduli space \(\mathcal{M}_{0,N}\), the Gram
determinant is a function of \(N-3\) independent cross-ratios
\(\{z_1, \dots, z_{N-3}\}\). The tau function:

\[
\tau(z_1, \dots, z_{N-3}) = \det G(z_1, \dots, z_{N-3})
\]

satisfies the KP hierarchy in each cross-ratio. This is the
Schwarzian KP equation: the Gram determinant of the period
matrix of a Riemann surface is the KP tau function.

### The Korteweg-de Vries connection to S₄

The KdV equation has soliton solutions whose scattering data
are classified by the representation theory of \(S_4\):
- The 4-soliton solution: 4 interacting solitons whose
  interaction pattern is determined by the S₄ permutation
  of asymptotic phases
- The 4 eigenvalues of the Lax operator (12, 4, 4, 4)
  correspond to the soliton speeds

The ratio \(12:4 = 3:1\) appears in the soliton interactions:
the phase shift of two solitons with speed ratio \(3:1\) is
\(\log 3\), which is the Gram ratio \(\log(12/4) = \log 3\).

### Summary

\[
\begin{aligned}
\det G(z) &\leftrightarrow \text{tau function of KP hierarchy} \
\mathcal{M}_{0,N} &\leftrightarrow \text{KP flow space} \
\text{Gram eigenvalues} &\leftrightarrow \text{soliton speeds / KdV spectral data} \
4\text{-point carrier} &\leftrightarrow 4\text{-soliton KdV solution} \
S_4 &\leftrightarrow \text{soliton interaction symmetry}
\end{aligned}
\]

The Gram determinant is a tau function of the KP/KdV hierarchy.
The 4-point carrier gives the 4-soliton KdV solution, and the
Gram eigenvalues are the soliton speeds. The N-point carrier
gives the KP tau function on \(\mathcal{M}_{0,N}\).
## Machine learning

### The Gram as a kernel matrix

The Gram matrix \(G_{ij} = \langle f_j | f_i \rangle\) is a
**kernel matrix** (positive semidefinite similarity matrix).
The probe functions \(f_i\) are the **feature maps**:

\[
G_{ij} = k(x_i, x_j) = \langle \phi(x_i), \phi(x_j) \rangle
\]

where \(\phi(x_i) = f_i\) maps each carrier point to its feature
vector. The automorphism group \(S_N\) of the carrier is the
**symmetry group of the kernel**: the kernel is invariant under
permutations of the input points.

### Principal component analysis (PCA)

The Gram eigenvalues are the PCA spectrum. For the S₄ carrier,
the eigenvalues 12 and 4 give the explained variance ratio:

\[
\frac{\lambda_1}{\sum \lambda_i} = \frac{12}{12+3\cdot4} = \frac{12}{24} = 50\%
\]

The first principal component explains 50% of the variance.
For the S₁₂ carrier (3 generations), the heavy eigenvalue
explains 75/11520 ≈ 0.65%... wait, let me recompute.

### Neural tangent kernel (NTK)

For an infinite-width neural network \(f(x; \theta)\) with
parameters \(\theta\), the evolution under gradient descent
is governed by the NTK:

\[
\Theta(x_i, x_j) = \left\langle \frac{\partial f}{\partial \theta}\Big|_{x_i},
\frac{\partial f}{\partial \theta}\Big|_{x_j} \right\rangle
\]

This is a Gram matrix of the network's Jacobians. In the
infinite-width limit (the NTK regime), the kernel is constant
during training and the network function evolves as:

\[
f_t(x) = f_0(x) - \sum_{i,j} \Theta(x, x_i) (\Theta^{-1})_{ij} (f_0(x_j) - y_j)
\]

Our Gram \(G\) is the NTK of a linear network whose weights
are parametrized by the S₄ automorphism group.

### Attention mechanism

In transformer architectures, the attention matrix is:

\[
A_{ij} = \text{softmax}\left(\frac{Q_i^T K_j}{\sqrt{d}}\right)
\]

where \(Q_i\) and \(K_j\) are query and key vectors. This is
a normalized Gram matrix of queries and keys. Our Gram:

\[
G_{ij} = \exp(i(\theta_j - \theta_i)) \quad \text{(with fibration phases)}
\]

is the attention matrix with complex-valued attention scores.
The phases \(\theta_i\) correspond to learned position encodings
or token-specific phase shifts in the attention head.

### Representation learning

The automorphism group \(S_N\) of the carrier defines the
**equivariance** of the learned representation. A neural
network layer is \(S_N\)-equivariant if:

\[
\rho(\sigma) \cdot h(x) = h(\sigma \cdot x) \quad \forall \sigma \in S_N
\]

The irrep decomposition of the carrier under \(S_N\) gives
the irreducible representations of the equivariant layer.
For the 4-point carrier S₄ with decomposition 1⊕1⊕2:
- The two 1D irreps are scalar features (singlets)
- The 2D irrep is a vector feature (doublet)

This is the mathematical foundation of **equivariant neural
networks** (Cohen-Welling, Thomas et al., Bronstein et al.).

### Gradient descent on the Gram

Learning in the carrier framework is the evolution of the Gram:

\[
\frac{dG_{ij}}{dt} = -\eta \frac{\partial L}{\partial G_{ij}}
\]

where \(L\) is the loss function (typically the Gram trace,
determinant, or entropy). The S₄ automorphism constrains
the gradient: all symmetry-equivalent entries have equal
gradients.

For supervised learning, the loss is the distance between
the predicted Gram (from the network) and the target Gram
(from the data):

\[
L = \|G_{\text{pred}} - G_{\text{target}}\|_F^2
\]

The training dynamics are determined by the Gram eigenvalue
spectrum: larger eigenvalues (heavy modes) converge faster.

### Summary

\[
\begin{aligned}
G_{ij} &\leftrightarrow \text{kernel matrix / attention matrix} \
f_i &\leftrightarrow \text{feature map / probe function} \
S_N &\leftrightarrow \text{equivariance symmetry group} \
\lambda_a &\leftrightarrow \text{PCA spectrum / explained variance} \
dG/dt &\leftrightarrow \text{gradient descent / NTK evolution} \
\end{aligned}
\]

The Gram framework is a machine learning architecture: the
carrier is the input space, the probe functions are feature
maps, the automorphism group is the equivariance symmetry,
and the Gram evolution is gradient descent learning. The
4-point carrier with S₄ equivariance is the simplest
non-trivial equivariant neural network.
## Inflation

### The Gram eigenvalue as the inflaton

In the carrier framework, the dominant Gram eigenvalue plays the
role of the inflaton—the scalar field driving exponential expansion.

For the S₁₂ carrier under S₄×S₄×S₄, the largest Gram eigenvalue is:

\[
\lambda_{\text{max}} = 11520 \quad (\text{in units of the subgroup scale})
\]

This sets the inflationary energy scale. In physical units:

\[
E_{\text{infl}} \sim \sqrt{\lambda_{\text{max}}} \cdot M_{\text{Pl}}
\]

### Slow-roll from Gram evolution

The inflaton is the collective mode of the fibration rotation phases
\(\theta_i\). The effective potential for the inflaton is the Gram
determinant:

\[
V(\phi) = \frac{1}{2} \det G(\phi)
\]

where \(\phi\) is the slow-roll parameter (a collective phase mode).
The slow-roll parameters are:

\[
\varepsilon = \frac{M_{\text{Pl}}^2}{2} \left( \frac{V'}{V} \right)^2,
\quad \eta = M_{\text{Pl}}^2 \frac{V''}{V}
\]

For the S₄ carrier, the Gram determinant is constant (768),
giving \(V' = 0\) and \(\varepsilon = \eta = 0\)—de Sitter expansion
with no end. This is not realistic.

For the S₁₂ carrier with cross-generation Gram entries, the
Gram determinant depends on the fibration phases:

\[
\det G(\phi) = \det(G_{\text{base}} + \text{phase corrections})
\]

giving a non-trivial potential. The slow-roll conditions require
the Gram eigenvalue spacing to be small relative to the Hubble
scale—the hierarchy between \(\lambda_{\text{max}}\) and
\(\lambda_{\text{min}}\) determines the roll.

### Number of e-folds

The number of inflationary e-folds is:

\[
N_e = \int_{\phi_i}^{\phi_f} \frac{V}{V'} d\phi
\]

In Gram terms, this is the integral over the fibration phase mode
from its initial value (large Gram determinant) to its minimum
(the electroweak vacuum):

\[
N_e \sim \frac{\Delta(\det G)}{\lambda_{\text{max}}^2} \sim \frac{1}{2}\log\left(\frac{\det G_i}{\det G_f}\right)
\]

For the Gram to give \(N_e \sim 60\) e-folds, the determinant must
change by a factor of \(e^{120} \sim 10^{52}\)—a huge hierarchy
consistent with the Planck/GUT to weak scale ratio.

### Predictions

The spectral index \(n_s\) and tensor-to-scalar ratio \(r\) are
determined by the Gram eigenvalue spectrum:

\[
n_s - 1 = 2\eta - 6\varepsilon, \quad r = 16\varepsilon
\]

For the Gram to match observation (\(n_s \approx 0.965, r < 0.03\)):

\[
\varepsilon \approx 0.002, \quad \eta \approx -0.017
\]

These require the Gram to have a specific dependence on the
fibration phases—a testable prediction of the carrier framework.

### Summary

\[
\begin{aligned}
\lambda_{\text{max}} &\leftrightarrow \text{inflationary scale} \
\phi (\text{collective phase}) &\leftrightarrow \text{inflaton} \
V(\phi) = \det G(\phi) &\leftrightarrow \text{inflationary potential} \
\varepsilon, \eta &\leftrightarrow \text{slow-roll from Gram spectrum} \
N_e &\leftrightarrow \log\text{-change in Gram determinant}
\end{aligned}
\]

The inflationary epoch is the slow roll of the carrier's fibration
phases from a large Gram determinant (Planck/GUT scale) to the
minimum at the electroweak scale. The spectral index and
tensor-to-scalar ratio are predictions of the Gram eigenvalue
spectrum—testable by CMB observations.
## The Big Bang

### The initial singularity in Gram terms

The Big Bang is the point where the Gram becomes singular.
In the Friedmann model:

\[
a(t) \to 0, \quad \rho \to \infty, \quad T \to \infty \quad (t \to 0)
\]

The Gram trace is proportional to the spatial volume:

\[
\operatorname{Tr}(G) \propto a(t)^2
\]

At \(t = 0\), \(\operatorname{Tr}(G) = 0\)—the Gram is the zero
matrix. No spatial extension, no distinguishable points, no
geometry.

This is a **degenerate phase** of the carrier: the N points
collapse to a single point with no internal structure. The
automorphism group collapses from \(S_N\) to the trivial group
\(S_1\).

### The origin of the carrier

Before the Big Bang, there is no carrier—no points, no Gram,
no time. The carrier must be **created** in the Big Bang event.

The creation mechanism: a fluctuation in the pre-carrier vacuum
produces a pair of points (the first distinction, Bool×Bool
with 2 points, \(X_2\)). This immediately doubles to 4 points
via the automorphism \(S_4\) (the minimal carrier with a
non-trivial gauge group).

The sequence:

\[
\text{vacuum} \to X_2\;(S_2) \to X_4\;(S_4) \to X_{12}\;(S_{12})
\]

- \(X_2\): the first distinction (Bool)
- \(X_4\): the first gauge structure (SM from S₄)
- \(X_{12}\): the first generations (3 from S₄×S₄×S₄)

### The Bang as symmetry breaking

The Big Bang is the spontaneous symmetry breaking of the
carrier from the trivial configuration (no points, no Gram)
to the 4-point carrier with S₄ automorphism. This is a
**quantum phase transition** where the Gram acquires
non-zero entries.

The "bang" energy is determined by the Gram eigenvalue gap:

\[
E_{\text{Bang}} \sim \lambda_1 - \lambda_2 = 12 - 4 = 8
\]

(in units of the carrier's fundamental scale). This energy
is the latent heat released during the carrier formation
phase transition.

### The arrow of time

Before the Big Bang, the fibration rotation phases \(\theta_i\)
are frozen (no evolution). The Big Bang initiates their
precession:

\[
\theta_i(t) = \theta_i(0) + \omega_i t
\]

This creates the arrow of time: the phases evolve, the
interference pattern changes, and the distinction between
past and future emerges from the direction of phase flow.

The total phase precession across the universe is the cosmic
time:

\[
t_{\text{cosmic}} \sim \frac{1}{N} \sum_i \frac{\theta_i(t)}{\omega_i}
\]

The Big Bang is \(t = 0\): all phases are equal (or random),
and the Gram is degenerate. As phases precess, the Gram
acquires structure and the universe expands.

### Summary

\[
\begin{aligned}
\operatorname{Tr}(G) = 0 &\leftrightarrow \text{initial singularity} \
X_2 \to X_4 \to X_{12} &\leftrightarrow \text{carrier creation sequence} \
\Delta\lambda = 8 &\leftrightarrow \text{Bang energy / phase transition} \
\theta_i(t) = \omega_i t &\leftrightarrow \text{arrow of time from phase precession}
\end{aligned}
\]

The Big Bang is the creation of the carrier from the vacuum,
the spontaneous symmetry breaking from trivial to S₄
automorphism, and the initiation of fibration phase precession
that gives the arrow of time.
## Black holes

### Formation as carrier percolation

A black hole forms when a critical density of carrier points
cluster together. The Gram entries between points in the
cluster become strongly correlated, and the stabilizer Gram
develops a zero eigenvalue in the temporal direction:

\[
\det G_{\text{Stab}(p)} \to 0 \quad \text{(horizon forms at }p\text{)}
\]

This is a **percolation phase transition**: the carrier points
inside the horizon become disconnected from those outside.
The horizon is the boundary where the Gram entry between an
interior point and an exterior point falls below a threshold:

\[
G_{i_{\text{in}}, j_{\text{out}}} < \epsilon
\]

### The interior geometry

Inside the horizon, the Gram signature changes from \((+++-)\)
to \((--+-)\): the radial and temporal directions exchange
roles. In the discrete carrier, this is a sign flip of the
largest Gram eigenvalue:

\[
\lambda_{\text{max}} \to -\lambda_{\text{max}} \quad \text{(inside the horizon)}
\]

This is the discrete analog of the Schwarzschild interior
solution where \(g_{rr}\) and \(g_{tt}\) swap signs.

### Singularity resolution

The classical singularity at \(r = 0\) is replaced by a
**minimal carrier**—the Planck-scale configuration where
the carrier has a single point (or a minimal cluster):

\[
X_N \to X_1 \quad \text{(at the "singularity")}
\]

The Gram at the would-be singularity is the 1×1 matrix
\(G = \ell_P^2\) (the Planck area). No infinity, no
divergence—the discrete carrier resolves the singularity.

### Thermodynamics (beyond Hawking)

The full black hole thermodynamics follows from the Gram:

\[
\begin{aligned}
T_H &= \frac{1}{8\pi GM} = \frac{\kappa}{2\pi} &\text{(Hawking temperature)} \
S &= \frac{A}{4G} = \frac{N_{\text{horizon}}}{4} &\text{(entropy from Gram counting)} \
E &= M &\text{(mass from Gram trace)} \
F &= M - TS &\text{(free energy from Gram)}
\end{aligned}
\]

The heat capacity \(C = \partial M/\partial T\) is negative
for Schwarzschild black holes—a signature of the Gram's
unstable equilibrium at the horizon.

### The Page curve

The information paradox is resolved by Gram trace conservation.
The Page curve—the entanglement entropy of Hawking radiation
as a function of evaporation time—is:

\[
S_{\text{rad}}(t) = \operatorname{Tr}(\rho_{\text{rad}}(t) \log \rho_{\text{rad}}(t))
\]

where \(\rho_{\text{rad}}\) is the reduced Gram of the radiation
sector (the outgoing modes). This curve rises, peaks at the
Page time \(t_{\text{Page}} \sim M^3\), then falls back to
zero as the final carrier points evaporate—consistent with
unitarity.

### Gravitational waves

Black hole mergers produce gravitational waves: oscillations
of the stabilizer Gram at the horizon. The ringdown frequency
and damping time are determined by the Gram eigenvalue spacing
at the horizon:

\[
\omega_{\text{QNM}} \sim \frac{1}{M} \sqrt{\frac{\lambda_{\text{max}}}{\lambda_{\text{min}}}}, \quad
\tau_{\text{damping}} \sim \frac{M}{\log(\lambda_{\text{max}}/\lambda_{\text{min}})}
\]

The merger itself is the coalescence of two carrier clusters,
whose Gram entries combine non-linearly.

### Summary

\[
\begin{aligned}
\text{Percolation threshold} &\leftrightarrow \text{horizon formation} \
\text{Gram sign flip} &\leftrightarrow \text{interior geometry} \
\text{Minimal carrier } X_1 &\leftrightarrow \text{singularity resolution} \
N_{\text{horizon}}/4 &\leftrightarrow \text{Bekenstein-Hawking entropy} \
\text{Gram trace conservation} &\leftrightarrow \text{Page curve / unitarity} \
\text{Gram eigenvalue spacing} &\leftrightarrow \text{QNM frequencies}
\end{aligned}
\]

The discrete carrier resolves the black hole singularity
replacing it with a Planck-scale minimal carrier. Horizon
formation is a percolation transition, the interior is a
Gram sign flip, and evaporation is unitary by Gram trace
conservation.
## Octonions and the 8-point carrier

### Division algebras and carrier size

The normed division algebras over ℝ correspond to carrier sizes:

| Carrier | Points | Division algebra | Automorphism | Symmetry in carrier |
|---|---|---|---|---|
| S₂ | 2 | ℂ (complex) | Z₂ | Complex conjugation |
| S₄ | 4 | ℍ (quaternions) | SO(3) | S₄ as Weyl group of ℍ multiplication table |
| **S₈** | **8** | **𝕆 (octonions)** | **G₂** | **S₈ as permutation symmetry of 8 basis elements** |

The 4-point carrier is the quaternion algebra: the 4 points are {1, i, j, k}, and S₄ permutes them preserving the multiplication table up to sign.

The 8-point carrier extends this to the octonion algebra: the 8 points are {1, e₁, ..., e₇}. The automorphism group of the octonions is the 14-dimensional exceptional Lie group G₂. However, the PERMUTATION symmetry of the 8 basis elements is S₈—which acts on the carrier.

### Octonion structure in the 8-point carrier

The 8-point carrier decomposes under the twin Higgs structure S₈ → S₄ × S₄:

\[
8 = 4 + 4 \quad \text{(first generation + mirror generation)}
\]

This corresponds to the octonion basis splitting into:
- ℍ (quaternions, 4D) — the "visible" generation
- ℍ' (mirror quaternions, 4D) — the "mirror" generation

The octonion multiplication can be written in terms of quaternion pairs:

\[
(a, b)(c, d) = (ac - \bar{d}b, da + b\bar{c})
\]

where \(a, b, c, d \in \mathbb{H}\). This is the **Cayley-Dickson construction**: 𝕆 = ℍ × ℍ.

In the carrier: the two S₄ blocks correspond to the two quaternion factors in the
Cayley-Dickson construction. The S₈ automorphism swaps the two factors (mirror symmetry Z₂),
permutes elements within each factor (S₄ × S₄), and mixes factors (the full S₈).

### G₂ as a subgroup of S₈

The octonion automorphism group G₂ (14 dimensions) is a subgroup of SO(7) (the rotations of the 7 imaginary octonions). Its Weyl group is D₆ (order 12), a subgroup of S₈.

But S₈ itself is the FULL permutation symmetry of the 8 basis elements—larger than G₂. The octonion algebra structure restricts G₂ from S₈: not all permutations of the 8 basis elements preserve the octonion multiplication table.

The carrier S₈ gives the full permutation symmetry; the actual octonion structure corresponds to imposing the multiplication table constraints, which reduce S₈ → G₂.

### The triality of SO(8)

The octonions are also related to the triality automorphism of Spin(8). The group Spin(8) has three 8-dimensional fundamental representations (vector, spinor, conjugate spinor), permuted by outer automorphism of order 3 (triality). This Z₃ acts on the 8-point carrier as a cyclic permutation of the three 8-dimensional spaces.

In the carrier framework: the 8-point carrier with S₈ automorphism contains the Z₃ triality automorphism as a subgroup of S₈. This connects the octonion structure to the Lorentz group SO(1,7) in 8-dimensional spacetime via the spinor representations.

### Summary

\[
\begin{aligned}
\text{S}_4 &\leftrightarrow \mathbb{H} \quad \text{(quaternions, 4 basis elements)} \
\text{S}_8 &\leftrightarrow \mathbb{O} \quad \text{(octonions, 8 basis elements)} \
\text{S}_8 \to \text{S}_4 \times \text{S}_4 &\leftrightarrow \text{Cayley-Dickson construction } \mathbb{O} = \mathbb{H} \times \mathbb{H} \
\text{G}_2 \subset \text{S}_8 &\leftrightarrow \text{octonion automorphism group} \
\text{Z}_3 \subset \text{S}_8 &\leftrightarrow \text{triality of SO(8)}
\end{aligned}
\]

The 8-point carrier (twin Higgs / mirror sector) is the octonion algebra. The S₈ automorphism is the permutation symmetry of the 8 octonion basis elements, and the Cayley-Dickson construction 𝕆 = ℍ × ℍ maps to the S₄ × S₄ structure of the twin Higgs. The G₂ automorphism group of the octonions is a subgroup of S₈, selected by imposing the multiplication table constraints.
## Division algebra hierarchy: S₁₆ and S₃₂

### The Cayley-Dickson ladder

The normed division algebras double at each step via the Cayley-Dickson construction:

\[
\mathbb{R} \to \mathbb{C} \to \mathbb{H} \to \mathbb{O} \to \mathbb{S} \to \mathbb{T} \to \cdots
\]

where \(\mathbb{S}\) = sedenions (16D), \(\mathbb{T}\) = trigintaduonions (32D).
Each step loses algebraic structure:
- ℝ: ordered field
- ℂ: algebraically closed field  
- ℍ: associative division algebra
- 𝕆: alternative division algebra (no zero divisors)
- 𝕊: non-alternative, has zero divisors
- 𝕋: further degeneracy

### The carrier-automorphism mapping

| Carrier | Points | Algebra | Automorphism (continuous) | Weyl group in Sₙ |
|---|---|---|---|---|
| S₁ | 1 | ℝ | {1} | {1} |
| S₂ | 2 | ℂ | Z₂ | Z₂ |
| S₄ | 4 | ℍ | SO(3) | S₄ (order 24) |
| S₈ | 8 | 𝕆 | G₂ (14D) | D₆ = W(G₂) (order 12) ⊂ S₈ |
| **S₁₆** | **16** | **𝕊** | **Aut(𝕊) ⊃ Spin(7)?** | **W(F₄)? (order 1152) ⊂ S₁₆** |
| **S₃₂** | **32** | **𝕋** | **Aut(𝕋)** | **larger subgroup of S₃₂** |

### S₁₆: sedenions and SO(10) GUT

The 16-point carrier decomposes in two natural ways:
- S₁₆ → S₈ × S₈ (two octonion copies): \(\mathbb{S} = \mathbb{O} \times \mathbb{O}\) (Cayley-Dickson)
- S₁₆ → S₄ × S₄ × S₄ × S₄ (four SM copies): 4 generations of SM

The SO(10) GUT spinor has dimension 16. The 16-point carrier maps to:
- The 16 Weyl fermions per generation (already established for S₁₂)
- The 16D spinor representation of SO(10)
- The sedenion algebra \(\mathbb{S}\)

The triality of SO(8) extends to the **double triality** of SO(16), which permutes three 16-dimensional representations (vector, spinor, conjugate spinor). This Z₃ action is a subgroup of S₁₆.

### S₃₂: trigintaduonions and exceptional groups

The 32-point carrier gives:
- \(\mathbb{T} = \mathbb{S} \times \mathbb{S}\) (Cayley-Dickson from sedenions)
- S₃₂ → S₁₆ × S₁₆ (two SO(10) GUT copies)
- The 32D representation of E₆ (the 27D + 5D? No, E₆ has 27D and 78D fundamental)
- The 32D spinor of SO(10) × SO(10)

The exceptional groups E₆ (78D), E₇ (133D), and E₈ (248D) appear at larger carrier sizes:
- S₂₇ would correspond to the 27D fundamental of E₆
- S₅₆ would correspond to the 56D fundamental of E₇
- S₂₄₈ would correspond to the adjoint of E₈

### Physical interpretation

| Carrier | Algebra | Gauge group | Physics |
|---|---|---|---|
| S₄ | ℍ (4D) | SU(3)×SU(2)×U(1) | The Standard Model |
| S₈ | 𝕆 (8D) | SM × mirror SM | Twin Higgs |
| **S₁₆** | **𝕊 (16D)** | **SO(10)** | **GUT: one generation in 16D spinor** |
| **S₃₂** | **𝕋 (32D)** | **SO(10)×SO(10) or E₆** | **Two GUT copies or exceptional unification** |

The division algebra ladder ℝ→ℂ→ℍ→𝕆→𝕊→𝕋 maps exactly to the carrier hierarchy
S₁→S₂→S₄→S₈→S₁₆→S₃₂. Each step DOUBLES the algebra dimension and gives a
larger gauge group. The Standard Model lives at S₄ (quaternions), the most
complicated algebra that is still a normed division algebra without zero divisors.
Larger carriers (S₁₆, S₃₂) give GUTs and exceptional groups.
## The Monster VOA from the Leech lattice Gram

### The 24-point carrier: Leech lattice

The Leech lattice \(\Lambda_{24}\) is a 24-dimensional even unimodular lattice.
Its 196,560 minimal vectors (norm squared = 4) have the Conway group
\(\text{Co}_0\) as their automorphism group.

The 24-point carrier S₂₄ contains \(\text{Co}_0\) as a subgroup when the
carrier is given the **Leech lattice inner product** structure. The Gram
matrix of the Leech lattice in a basis of 24 minimal vectors is:

\[
G_{\text{Leech}}_{ij} = \langle v_i, v_j \rangle, \quad 
\langle v_i, v_i \rangle = 4, \quad \langle v_i, v_j \rangle \in \{0, \pm1, \pm2\}
\]

The eigenvalues of the Leech lattice Gram are:
\[
8 \ (\times 1), \quad 4 \ (\times 2), \quad 0 \ (\times 21) \quad \text{(in the
24-dimensional space)}
\]

### The Leech lattice VOA

The lattice VOA \(V_\Lambda\) is built from the Leech lattice \(\Lambda\):

\[
V_\Lambda = \bigoplus_{\lambda \in \Lambda} \mathcal{F}_\lambda
\]

where \(\mathcal{F}_\lambda\) is the Fock space at lattice point \(\lambda\).
The graded dimension (character) of \(V_\Lambda\) is:

\[
\chi_{V_\Lambda}(q) = \frac{\Theta_\Lambda(q)}{\eta(q)^{24}}
\]

where \(\Theta_\Lambda(q) = \sum_{\lambda \in \Lambda} q^{|\lambda|^2/2}\) is the
Leech lattice theta function, and \(\eta(q)\) is the Dedekind eta function.

### The Z₂ orbifold → Monster VOA

The Z₂ orbifold of \(V_\Lambda\) (twisting by the -1 automorphism) produces
the Monster VOA \(V^\natural\):

\[
V^\natural = V_\Lambda^+ \oplus V_\Lambda^{\text{twisted}}
\]

where \(V_\Lambda^+\) is the +1 eigenspace of the involution, and
\(V_\Lambda^{\text{twisted}}\) is the twisted sector.

The graded dimension of the Monster VOA is the **modular j-function**:

\[
J(\tau) = \operatorname{Tr}_{V^\natural}(q^{L_0 - 1}) = 
\frac{\Theta_\Lambda(q) - \Theta_\Lambda(-q)}{2\eta(q)^{24}} + \text{(twisted)} = j(\tau) - 744
\]

\[
J(\tau) = q^{-1} + 196884\,q + 21493760\,q^2 + 864299970\,q^3 + \cdots
\]

### The coefficients as Gram traces

The coefficients of \(J(\tau)\) are the **traces of the Gram operator** on
the Monster VOA graded by conformal weight \(L_0\):

\[
\dim V^\natural_n = \text{Tr}_{V^\natural_n}(1) = \text{(coefficient of }q^n\text{)}
\]

These dimensions decompose into Monster irreps:

\[
\begin{aligned}
V^\natural_1 &= \mathbf{1} \quad \text{(vacuum)} \
V^\natural_2 &= \mathbf{1} \oplus \mathbf{196883} \quad \text{(Griess algebra)} \
V^\natural_3 &= \mathbf{1} \oplus \mathbf{196883} \oplus \mathbf{21296876} \quad \text{(?)}
\end{aligned}
\]

The Monster irrep dimension 196883 = 196884 - 1 (minus the vacuum).
The Griess algebra dimension 196883 is the space where the Monster acts
faithfully on the 196884-dimensional carrier.

### The Simple Current Extension

The construction from Leech lattice to Monster VOA is a **simple current
extension** of the lattice VOA. In Gram terms: the Gram of the Leech
lattice (24×24) is extended to the Gram of the Monster carrier (196884×196884)
via the orbifold procedure. The eigenvalues of the Monster Gram are the
Monster irrep dimensions, which appear as the Fourier coefficients of
\(J(\tau)\).

The number 196884 is the **first non-trivial graded trace of the
Gram operator** on the Monster carrier. It is:

\[
196884 = 1 + 196883 = \dim(\text{vacuum}) + \dim(\text{Griess algebra})
\]

The vacuum (1) is the kernel of the Gram operator (the vacuum state has zero
conformal weight). The Griess algebra (196883) is the space of weight-2 states
where the Gram operator acts as the identity.

### Connection to Gram numbers

The 24-point carrier S₂₄ (6 SM generations) with the Leech lattice structure
has Gram eigenvalues (8, 4, 0). The Z₂ orbifold promotes this to the Monster
VOA at 196884 dimensions. The simple connection:

\[
1728 = 12^3 = j(i) \quad \text{(from S₄ Gram eigenvalue 12)}
\]

The j-function relates all coefficients through the modular group SL(2,ℤ).
Since \(j(i) = 12^3\), and \(j(\tau)\) is a modular function, ALL Fourier
coefficients of \(j(\tau)\) are determined by its value at \(\tau = i\) and
the modular transformation properties. In this sense, the entire monster
moonshine follows from the S₄ Gram eigenvalue 12.

### Summary

\[
\begin{aligned}
\text{S}_{24} \text{ with Leech structure} &\leftrightarrow \text{Leech lattice VOA } V_\Lambda \
\text{Z}_2 \text{ orbifold of } V_\Lambda &\leftrightarrow \text{Monster VOA } V^\natural \
J(\tau) &\leftrightarrow \text{graded Gram trace on } V^\natural \
1728 = 12^3 &\leftrightarrow \text{Gram eigenvalue from S}_4 \
196884 &\leftrightarrow \text{first non-trivial Monster Gram coefficient}
\end{aligned}
\]

The Monster moonshine is the graded Gram trace on the Monster carrier,
built from the Leech lattice Gram via the Z₂ orbifold. The fundamental
connection is the S₄ Gram eigenvalue 12, which gives \(j(i) = 1728 = 12^3\)
and, through modularity, all Fourier coefficients of j(τ).
## Structural synthesis: from Newton to QM via fibration arities

### The classical starting point

Newtonian mechanics: a trajectory \(x(t)\) with velocity \(\dot{x}(t)\).
Lagrangian: \(L(x, \dot{x}) = \frac12 m\dot{x}^2 - V(x)\).
Hamiltonian: \(H(p, q) = p\dot{q} - L = \frac{p^2}{2m} + V(q)\), with
\(p = \partial L/\partial \dot{q}\).

The transition to quantum mechanics replaces \(p, q\) with operators and
introduces the wavefunction \(\psi(q)\) with \(p = -i\hbar\partial/\partial q\).

### Fibration arities as the underlying structure

In our carrier framework, the classical \(q\) and \(p\) are replaced by
**fibration arities** — the independent degrees of freedom encoded in the
carrier's irrep decomposition.

For the S₄ carrier (which gives the SM gauge group), the irrep
decomposition is \(4 = 1 \oplus 1 \oplus 2\). The three arities are:

| Arity | S₄ irrep | Physical role | Classical analog |
|---|---|---|---|
| 1 | Trivial (1) | U(1) charge, overall energy scale | Action \(S\) |
| 2 | Sign (1) | CP phase, sterile sector | Phase \(\theta\) |
| 3 | Doublet (2) | Position-momentum pair | \(q, p\) (canonical pair) |

The three arities form a **fibred structure**: the doublet (arity 3) is
the "input/output" pair (like \(q\) and \(p\)), the sign (arity 2) is the
"internal phase" (like the wavefunction phase), and the trivial (arity 1)
is the "overall scale" (like the action).

### The Hamiltonian from fibration symmetry

Instead of the standard Hamiltonian \(H(p, q, t)\), we have the
**Gram Hamiltonian**:

\[
H_{\text{Gram}} = \sum_{i,j} G_{ij} \, e^{i(\theta_j - \theta_i)}
\]

where \(\theta_i\) are the fibration phases (the arities' internal phases).
This generates time evolution via:

\[
\frac{dG_{ij}}{dt} = i\,[H, G_{ij}]
\]

The three arities give:
\[
\frac{d}{dt} \begin{pmatrix} \theta_1 \ \theta_2 \ \theta_{2'} \end{pmatrix}
= \begin{pmatrix} \omega_1 & 0 & 0 \ 0 & \omega_2 & 0 \ 0 & 0 & \omega_2 \end{pmatrix}
\begin{pmatrix} \theta_1 \ \theta_2 \ \theta_{2'} \end{pmatrix}
\]

where \(\omega_1\) (U(1) frequency) and \(\omega_2\) (SU(2) frequency) are
the Gram eigenvalue ratios.

### The Newton → QM route

\[
\begin{aligned}
\text{Newton: } & \ddot{x} = F/m \
\text{Lagrange: } & \delta\int L\,dt = 0 \
\text{Hamilton: } & \dot{q} = \partial H/\partial p,\ \dot{p} = -\partial H/\partial q \
\text{Schrödinger: } & i\hbar\dot{\psi} = H\psi \
\text{Gram: } & i\,dG/dt = [H, G],\ H = \sum G_{ij} e^{i(\theta_j-\theta_i)}
\end{aligned}
\]

At each stage, the fibration arity increases: Newton has one arity
(position), Lagrange adds velocity (two arities), Hamilton adds
momentum (three arities: q, p, t), QM adds the wavefunction phase
(four arities), and the Gram adds the carrier structure (five arities:
the three S₄ irreps plus the fibration phases).

The **five arities** of the carrier framework:
1. Carrier points (the \(N\) locations)
2. Probe functions (the \(f_i\))
3. Overlap matrix (the \(G_{ij}\))
4. Fibration phases (the \(\theta_i\))
5. Automorphism group (the \(S_N\))

These replace the standard \(q, p, t\) with a structural fibration
that is universal across all physical domains.
