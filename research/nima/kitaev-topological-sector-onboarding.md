# Kitaev topological-sector programme: protected capability beyond local residue

Owner: `marici.Kitaev`

Commissioned by: `marici.Nima`

## Starting result

Read `~/src/marici/AGENTS.md` completely and establish your canonical Marici
identity before acting. Then reproduce:

- `research/nima/toric-code-chain-carrier-pilot.md`;
- `research/nima/checkers/check_toric_code_chain_carrier.py`;
- `research/nima/results/toric-code-chain-carrier.json`.

The pilot proves on periodic square lattices that:

\[
\partial_1\partial_2=0,
\qquad
H_1=\ker\partial_1/\operatorname{im}\partial_2\simeq\mathbf F_2^2,
\]

and that syndrome plus two loop probes is jointly faithful modulo face
repairs. It also proves that syndrome data does not select a preferred
decoder.

Do not redo that census except to verify conventions. Your job is to supply
the physical and categorical structure that the bare chain pilot omits.

## Central question

Does a source-derived topologically ordered quantum system instantiate the
Marici architecture

\[
\text{local residue}
\oplus
\text{global residue-free capability}
\oplus
\text{source-selected dynamics/readout},
\]

or does its Hamiltonian, operator algebra, or braiding force an additional
kind of object absent from our current Carrier vocabulary?

## Work programme

### WP1: freeze the physical source

Choose the standard finite toric-code Hamiltonian on an oriented periodic
square lattice. Record qubits, star and plaquette operators, sign and boundary
conventions, Hamiltonian, ground space, and admissible local Pauli operations.
Keep the primal and dual complexes distinct.

### WP2: derive both syndrome channels

Derive electric and magnetic syndromes from operator commutation, not by
declaring them copies of cellular boundary maps. Identify the exact chain and
cochain maps and verify their mutual compatibility.

### WP3: recover protected logical capability

Derive the logical operator algebra as the appropriate homology/cohomology
quotient. Verify the intersection pairing and the resulting anticommutation
law of primal and dual noncontractible loops. Determine which part is Carrier
geometry and which part requires the quantum coefficient lens.

### WP4: selection and rigidification

Separate four operations:

1. the lattice/cellulation defining admissible incidence;
2. the stabilizer Hamiltonian selecting a ground subspace;
3. local stabilizers identifying equivalent representatives;
4. a physical preparation or boundary condition selecting a state within the
   logical ground space.

Give exact counterexamples to any invalid implication among them.

### WP5: readout completeness

Classify local syndrome measurements, Wilson-loop measurements, and full
logical tomography. Establish the smallest jointly faithful legal probe
family modulo stabilizers and distinguish detection, separation, and
reconstruction.

### WP6: decoder noncanonicity

Show exactly which extra data selects a recovery: metric/noise model,
likelihood, dynamics, boundary condition, or measurement history. Test whether
two source-admissible decoder choices can agree on syndrome and logical action
while differing as physical instruments.

### WP7: braiding and transport

Construct one finite anyon-pair creation, transport, and annihilation process.
Type open strings, endpoint excitations, closed holonomy, framing, and
intersection phase. Test the Marici rule that open transport needs endpoint
framing while a closed supported cycle carries invariant holonomy.

### WP8: hostile boundary test

Repeat the classification on a planar code with at least two boundary types.
Determine whether boundary condensation converts a formerly global logical
class into a legal local repair or readout. This is the primary test of the
claim that adding relations can fill an observable port.

### WP9: perturbation test

Introduce one explicitly bounded local perturbation. Do not invoke stability
as a slogan. Determine which chain-level statements remain exact, which
become approximate spectral statements, and what source quantity controls the
splitting of the logical subspace.

### WP10: cross-sector appraisal

Compare only after the sector-native derivations are complete:

- Benincasa: local residue versus supported coefficient class;
- Strominger: failed initialization/continuation versus persistent kernel;
- Figueiredo: chart invariant versus physical quotient invariant;
- Grothendieck: bulk positivity versus boundary/seam orientation;
- Nima: selector, rigidifier, transport certificate, and readout quotient.

State what is genuinely shared and what remains a sector-specific quantum
coefficient law.

## Hard falsifiers

The proposed architecture fails or requires revision if any of the following
occurs:

- physical syndromes cannot be derived from the same source complex as legal
  repairs;
- logical operators require a structure not expressible as a supported
  quotient, pairing, extension, or transport class;
- the Hamiltonian fails to separate selection from representative
  rigidification;
- the smallest physically legal probe family differs essentially from the
  homological prediction;
- braiding cannot be typed through source-defined incidence plus quantum
  coefficient pairing;
- boundary condensation changes observables without a corresponding legal
  support/coherence map.

## Deliverables and cadence

Keep each theorem/falsifier in a bounded packet. Maintain a short programme
index; never create an append-only monolith. Provide exact finite checkers and
results where appropriate. Communicate only theorem-changing blockers,
objections to the frozen pilot, and consolidated milestones. Do not commit or
push without operator authorization.

The first milestone report should cover WP1--WP3. Continue through WP4--WP6
without waiting if no source or typing blocker occurs.

