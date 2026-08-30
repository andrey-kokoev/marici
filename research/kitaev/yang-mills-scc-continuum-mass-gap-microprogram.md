# Yang–Mills SCC continuum-and-mass-gap microprogram

## Objective

Locate the first irreducible failure in the constructor chain

\[
\text{finite gauge lattice}
\longrightarrow
\text{continuum quantum field theory}
\longrightarrow
\text{physical Hilbert space}
\longrightarrow
\text{positive mass gap}.
\]

The programme must not identify a finite-cutoff gap, numerical correlation length, or formal path integral with the existence of four-dimensional quantum Yang–Mills theory.

## Scope

- Four-dimensional Euclidean spacetime as the constructive entry chart.
- A fixed compact simple gauge group \(G\).
- Gauge-invariant observables.
- Finite-volume lattice regularizations followed by declared thermodynamic and continuum limits.
- Osterwalder–Schrader reconstruction or another explicitly equivalent axiomatic target.
- Vacuum-sector spectral gap in physical units.

## SCC objects

| Role | Object |
|---|---|
| finite carrier | oriented lattice with \(G\)-valued edge variables |
| local constructor | plaquette action and Haar integration |
| gauge quotient | vertex-gauge action and invariant observable algebra |
| ordered lens | Wilson-loop holonomy |
| finite state | normalized lattice measure or transfer-matrix vacuum |
| completion diagram | volume growth, lattice refinement, and renormalization |
| continuum observer packet | Schwinger functions of gauge-invariant fields |
| reconstruction | physical Hilbert space, vacuum, fields, and Hamiltonian |
| separation margin | spectral gap above the vacuum |

## Twelve moves

### M1 — Freeze the finite gauge packet

Specify:

- compact simple \(G\);
- finite oriented four-dimensional lattice;
- boundary conditions;
- edge and plaquette conventions;
- lattice action and coupling normalization;
- normalized Haar measure;
- gauge action at vertices;
- declared gauge-invariant observables.

Changing any item creates a different realization packet.

### M2 — Derive gauge invariance and ordered holonomy

Derive the transformation of link variables and prove that closed Wilson loops are gauge invariant. Keep the ordered product primary. Trace and character projections are observer shadows and may lose noncommutative holonomy data.

### M3 — Construct the finite positive state

Construct the finite partition function and expectation functional. Verify positivity, normalization, locality, and reflection positivity where claimed. A Monte Carlo ensemble is evidence about this state, not its mathematical definition.

### M4 — Construct the finite transfer matrix

Where reflection positivity and time slicing permit it, construct the transfer matrix and finite Hamiltonian. Separate:

- kinematical link space;
- gauge-invariant physical space;
- vacuum sector;
- finite-volume excitation spectrum.

### M5 — Audit the finite mass-gap shadow

Measure or bound the first finite-volume excitation and exponential decay of selected connected correlators. Record lattice spacing \(a\), volume \(L\), bare coupling, observable family, and conversion to physical units.

Reject

\[
\Delta_{a,L}>0\quad\text{for every finite }(a,L)
\]

as insufficient for a continuum mass gap.

### M6 — Freeze the two-limit topology

Declare the thermodynamic and continuum limits:

\[
L\to\infty,
\qquad
a\to0,
\]

together with the renormalization trajectory. Test whether the limits commute, require a diagonal net, or exist only in one order. An undeclared order of limits is a typing failure.

### M7 — Construct compatible continuum correlation packets

For each finite family of gauge-invariant observables, construct renormalized Schwinger functions and require:

- Euclidean covariance;
- permutation symmetry with correct field typing;
- reflection positivity;
- cluster behavior;
- regularity and growth bounds;
- compatibility under restriction of insertion sets.

Pointwise convergence of individual correlators is not joint state construction.

### M8 — Prove tightness and nontriviality

Show that the continuum packet neither escapes nor collapses to a Gaussian, zero, or topological shadow inconsistent with four-dimensional Yang–Mills. Require a source-derived interacting observable or connected correlation surviving completion.

### M9 — Reconstruct the physical theory

Apply the declared reconstruction theorem to obtain:

- Hilbert space \(\mathcal H\);
- vacuum \(\Omega\);
- physical observable algebra;
- unitary spacetime action;
- positive Hamiltonian \(H\).

Quotient every null direction before spectral claims. Gauge redundancy is not a physical zero-energy excitation.

### M10 — Define the continuum gap

The mass-gap statement is

\[
\operatorname{spec}(H)\cap(0,\Delta)=\varnothing
\]

for some \(\Delta>0\), with the vacuum sector treated according to the chosen axioms.

Equivalent correlation-decay criteria may be used only after proving their hypotheses and faithfulness for a generating observable family.

### M11 — Prove completion-stable separation

Seek one physical scale and one positive lower bound surviving:

- volume growth;
- lattice refinement;
- renormalization;
- gauge quotient;
- reconstruction.

The target certificate is not merely

\[
\inf_{a,L}\Delta_{a,L}>0,
\]

because bare lattice energies may scale. It is a uniform positive gap after the source-derived conversion to fixed physical units and identification with the reconstructed Hamiltonian.

### M12 — Issue the first-failure certificate

Return exactly one:

1. finite lattice theory only;
2. thermodynamic limit without continuum construction;
3. continuum Schwinger packet without reconstruction;
4. reconstructed but trivial or noninteracting theory;
5. nontrivial reconstructed Yang–Mills theory with gap still open;
6. a completed positive-gap realization satisfying the frozen target axioms.

## Required hostile fixtures

- every finite lattice has a gap but the physical gap tends to zero;
- bare gap stays fixed while conversion to physical units collapses;
- volume and continuum limits disagree;
- Wilson-loop traces converge while ordered holonomy data do not;
- gauge-null vectors counted as massless physical states;
- positivity before quotient but a nonclosable reconstructed Hamiltonian;
- pointwise correlator convergence without a jointly positive Schwinger functional;
- reflection positivity lost under the chosen improvement or renormalization;
- a continuum Gaussian fixed point presented as interacting Yang–Mills;
- exponential decay for one blind observable with an ungapped hidden sector;
- confinement evidence promoted directly to a mass-gap theorem;
- numerical scaling promoted without a rigorous continuum constructor.

## Smallest finite pilot

Use the smallest periodic lattice supporting:

- a nontrivial plaquette;
- at least one noncontractible Wilson cycle;
- a reflection plane;
- a transfer-matrix time step.

Compute:

1. gauge-orbit quotient;
2. plaquette and noncontractible-loop observables;
3. reflection-positive state matrix;
4. transfer-matrix spectrum;
5. observable overlap with each excitation.

This pilot tests SCC typing and observer faithfulness. It cannot test the continuum theorem.

## First expected result

The likely first structural theorem is a no-promotion result:

\[
\text{finite reflection-positive gapped lattice family}
\not\Rightarrow
\text{nontrivial continuum Yang–Mills with a mass gap}
\]

without a common renormalized correlation packet, reconstruction map, and physical-unit separation bound.

## Falsifier of the microprogram

Revise the programme if the selected axiomatic target is not equivalent to the official existence-and-gap requirement, or if the chosen finite carrier cannot simultaneously represent gauge quotient, reflection positivity, noncontractible holonomy, and transfer dynamics.

## Source anchor

Arthur Jaffe and Edward Witten, official Clay problem description, *Quantum Yang–Mills Theory*.

