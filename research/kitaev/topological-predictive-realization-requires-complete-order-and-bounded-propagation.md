# Topological predictive realization requires complete order and bounded propagation

Owner: `marici.Kitaev`

## Bounded question

The complete scalar context tower reconstructs a minimal ordered linear
realization up to similarity. What extra operational data replace arbitrary
similarity by an equivalence appropriate to a local quantum topological
system?

The answer is a hierarchy. Positivity, ancillary reference systems, instrument
branches, spatial support, and executable generators each remove a different
part of the abstract similarity gauge. None may be inferred from the previous
level.

## Level zero: predictive similarity

Let a complete scalar process be

\[
f:E^*\longrightarrow\mathbb C.
\]

Finite Hankel rank reconstructs a minimal linear realization

\[
f(w)=\alpha M_w\beta
\]

uniquely up to an invertible similarity (T):

\[
M'_a=T^{-1}M_aT.
\]

This equivalence preserves every scalar word response. It need not preserve:

- a positive-state cone;
- normalization;
- adjoints;
- complete positivity;
- tensor products;
- spatial support;
- energy or a gap;
- authorized physical generators.

Similarity is therefore the correct gauge for an abstract linear predictor and
the wrong final gauge for a quantum many-body realization.

## Level one: order equivalence

Let (A) and (B) be finite-dimensional unital (C^*)-algebras. Suppose the
operational data reconstruct their Hermitian spaces, positive cones, and order
units. A bijection

\[
\Phi:A_{\mathrm{sa}}\longrightarrow B_{\mathrm{sa}}
\]

is an order equivalence when

\[
\Phi(A_+)=B_+,
\qquad
\Phi(1_A)=1_B,
\]

and both (\Phi) and (\Phi^{-1}) are positive.

In finite-dimensional operator algebras, a unital order isomorphism extends to
a Jordan ({}^*)-isomorphism. It preserves

\[
a\circ b=\frac12(ab+ba)
\]

but may reverse ordered products on a summand.

For a full matrix block, the residual alternatives are unitary conjugation and
unitary conjugation composed with transpose. Single-system state--effect
probabilities do not necessarily distinguish them.

Thus positivity removes arbitrary similarity but still does not reconstruct
the direction of noncommutative multiplication.

## Level two: complete-order equivalence

Ancillary reference systems test all matrix amplifications

\[
\operatorname{id}_m\otimes\Phi.
\]

If (\Phi) and its inverse are completely positive and unital, then (\Phi) is a
complete-order isomorphism. For finite-dimensional (C^*)-algebras it is a
({}^*)-isomorphism:

\[
\Phi(ab)=\Phi(a)\Phi(b),
\qquad
\Phi(a^*)=\Phi(a)^*.
\]

On a full matrix algebra this has the form

\[
\Phi(a)=UaU^*
\]

for a unitary (U), after any authorized permutation of isomorphic central
blocks.

Transpose is positive but not completely positive in dimension greater than
one. Entangled ancillary tests therefore remove the Jordan orientation
ambiguity.

This is the first level that reconstructs the quantum coefficient algebra as
an ordered noncommutative algebra rather than only as a positive state space.

## Level three: instrument equivalence

Equality of channels is insufficient when records and feedback are admitted.
For an instrument with branches (\{\mathcal I_r\}), require

\[
\Phi\mathcal I_r
=
\mathcal I'_r\Phi
\]

for every outcome (r), including any declared classical relabelling.

The weaker equation

\[
\Phi\sum_r\mathcal I_r
=
\left(\sum_r\mathcal I'_r\right)\Phi
\]

preserves only the unrecorded channel. It can erase differences in branch
states, retained environment correlations, and future conditional control.

Complete instrument tomography must therefore include:

- arbitrary admitted preparations and reference systems;
- each classical outcome label;
- branch-conditioned continuations;
- coherent open slots when the apparatus port is retained.

Minimal Stinespring dilations of one channel are unique only up to an isometry
on the inaccessible environment. Reopening that environment port refines the
equivalence and requires tomography of the enlarged process.

## Level four: bounded-propagation net equivalence

Let a lattice realization carry a net of local algebras

\[
O\longmapsto A(O).
\]

A global ({}^*)-isomorphism may scramble a one-site operator across the entire
system. Global operational equivalence does not certify locality.

Fix an identification (f) of carrier regions. A uniformly
locality-preserving equivalence has a radius (R), independent of system size,
such that

\[
\Phi(A(O))
\subseteq
B(N_R(f(O)))
\]

and

\[
\Phi^{-1}(B(O'))
\subseteq
A(N_R(f^{-1}(O'))).
\]

Here (N_R) is the radius-(R) neighbourhood. This is a reversible bounded-speed
map of local observables, of the type represented by a quantum cellular
automaton or a quasi-local automorphism.

Region-labelled testers reconstruct this property only when the experiment
packet records where every preparation, intervention, and effect is supported.
Erasing support labels before tomography makes bounded propagation
unrecoverable.

## Level five: stable phase equivalence

A locality-preserving automorphism need not be a finite-depth local circuit.
It may carry a nontrivial QCA index or another obstruction to finite-depth
implementation.

Two realizations lie in the same stable circuit phase only after supplying a
uniform finite-depth local circuit, possibly after adjoining declared product
ancillas or invertible resources, that transports the relevant ground-space and
operator data.

An alternative phase witness is a uniformly gapped path with its
quasi-adiabatic continuation and locality bounds. Merely matching spectra at
one size or matching a protected algebra does not supply such a path.

The equivalence relation must say whether stacking with invertible phases is
ignored. A braided fusion category alone can miss invertible or gravitational
data such as chiral response. General phase classification therefore cannot be
identified with category equivalence without freezing this stable quotient.

## Level six: executable constructor equivalence

Even a finite-depth unitary equivalence may use gates absent from the admitted
apparatus. For constructor equivalence, require a bidirectional compiler
between the frozen generator families.

For every authorized local generator (C_a), there must be a uniformly bounded
word (w_a) in the second apparatus such that

\[
\Phi C_a\Phi^{-1}=C'_{w_a}
\]

as an instrument, not only as an unrecorded channel. The reverse compilation
must also exist.

The compiler contract must preserve:

- spatial support and causal ordering;
- branch records and retained environment ports;
- source and reference-frame typing;
- approximation tolerance under composition;
- fault domains and common-mode correlations;
- uniformly bounded resource overhead.

Without these conditions, two realizations may be phase-equivalent while one
cannot execute the other's declared control programme.

## Conditional predictive-realization theorem

Consider two finite local quantum process packets. Assume:

1. their scalar tester towers are complete for every exposed input, output,
   and sequential slot;
2. arbitrary admitted ancillary reference systems are included;
3. positive normalization and every instrument branch are reconstructed;
4. every test and constructor carries a region label;
5. the induced support correspondence has a system-size-independent radius.

Then equality of the complete operational towers reconstructs their minimal
instrument nets up to a bounded-propagation complete-order isomorphism.

### Proof structure

Complete scalar contexts first identify the minimal predictive linear spaces
and intertwine every ordered constructor. Positive preparations and effects
identify the cones and order units. Ancillary completeness upgrades the
intertwiner to a complete-order isomorphism, hence a ({}^*)-isomorphism.
Outcome-conditioned contexts intertwine individual instrument branches.
Region-labelled completeness reconstructs the local subalgebras; the assumed
uniform support bound makes the isomorphism locality preserving.

The conclusion does not include stable finite-depth implementation, a gapped
path, or an executable bidirectional compiler. Those require independent
witnesses at levels five and six.

## Topological-sector transport

Suppose the admitted constructor packet also contains localized charge-pair
creation, transport ribbons, fusion, exchange, and coherent reassociation
contexts. A bounded-propagation instrument-net isomorphism transports:

- localized superselection sectors;
- fusion multiplicities;
- braiding operators;
- associator-sensitive process amplitudes;
- the tensor unit and reference-frame action;
- the protected logical operator algebra.

The resulting categorical equivalence is derived from the transported
constructor net. It is not inferred from a short list of scalar invariants.

Modular (S,T) data, fusion rules, or central Wilson values may be incomplete as
realization probes. They can agree while associator data, defect structure,
boundary theory, invertible stacking sector, or executable ribbon apparatus
differs.

## `D(S3)` status under the ladder

The current finite `D(S3)` programme has established several different levels:

- eight central sectors are separated by central readout;
- one transposition and one three-cycle port generate the 36-dimensional
  endpoint associative algebra abstractly;
- the source-generated Lie algebra is projectively almost complete but retains
  central deficits;
- exact modular and ribbon data establish an algebraic topological packet;
- a six-state relational frame is required to name both noncentral ports;
- the frozen stabilizer apparatus does not execute controlled multiplication,
  coherent lookup, or all controlled phases;
- coherent protection of the relational frame crosses the same missing
  controlled-inversion boundary.

Therefore the present result is stronger than scalar sector equivalence and
weaker than executable local realization equivalence. Algebraic endpoint
generation does not close the level-six compiler gate.

The 36-dimensional endpoint algebra also does not become the full
256-dimensional ambient Hermitian algebra. The equivalence packet must name
which algebra is being reconstructed.

## Transpose hostile witness

Let (A=M_n(\mathbb C)) with (n>1), and define

\[
\tau(a)=a^{\mathsf T}.
\]

The map is positive, unital, and reverses multiplication order:

\[
\tau(ab)=\tau(b)\tau(a).
\]

It preserves the single-system positive cone but is not completely positive.
An entangled reference detects the failure of

\[
\operatorname{id}_n\otimes\tau.
\]

This is the smallest exact witness that positivity without ancillary tests
cannot recover the ordered quantum algebra.

## Nonlocal-unitary hostile witness

For each lattice size, choose a global unitary (U_L) that maps a fixed one-site
operator to support of diameter proportional to (L). Conjugation by (U_L) is a
complete-order isomorphism and preserves all globally transported statistics.

No uniform radius (R) satisfies the net condition. Hence complete global
tomography can identify the algebra while failing to identify a local
realization class.

## QCA hostile witness

A bounded-propagation automorphism can shift every on-site degree of freedom by
one lattice cell. It has finite propagation radius but need not be generated by
a finite-depth circuit under the declared boundary and stability convention.

Thus bounded propagation is weaker than stable circuit equivalence.

## DPC: topological realization is similarity with its physical gauges removed

The conjecture is:

> Complete topological operational data reconstruct a local quantum
> realization only when the context tower is complete at every ancillary,
> instrument, and spatial support level. The resulting gauge is a
> bounded-propagation complete-order isomorphism, not arbitrary similarity.
> Stable phase equivalence and executable constructor equivalence require
> additional gapped-path or compiler witnesses.

This is explanatory because each additional experiment family removes one
specific hostile ambiguity: cone distortion, transpose, hidden branch update,
nonlocal scrambling, QCA index, or unavailable physical gates.

## Critics

### Complete scalar contexts already reconstruct order

They reconstruct the order of abstract transition matrices. They do not
reconstruct the positive cone, adjoint, or product of a quantum coefficient
algebra unless the tester packet includes the corresponding physical
structure.

### Positivity should force a unitary equivalence

Order equivalence permits Jordan anti-isomorphisms such as transpose.
Ancilla-complete positivity is the gate that selects a ({}^*)-isomorphism.

### Equal process tensors identify the physical mechanism

They identify the exposed multi-time process under a complete tester family.
Different internal dilations and inaccessible environment dynamics may realize
the same process.

### A locality-preserving isomorphism proves the same phase

Not automatically. A nontrivial QCA can be locality preserving without being
a finite-depth stable circuit. The phase equivalence convention and witness
must be stated.

### Equal anyon data prove equal topological order

Only relative to a classification theorem whose invariant packet is complete.
Fusion and modular data can omit associators, defects, boundaries, invertible
stacking information, and physical constructor availability.

### If both systems generate the same endpoint algebra, they are equivalent

They may differ in generator locality, reference requirements, reachable Lie
group, records, costs, or fault propagation. Abstract algebra generation is
one level of the packet.

## Exact falsifiers

- A predictive similarity that fails positivity but is called quantum
  realization equivalence.
- A positive order isomorphism with a transpose component promoted to a
  ({}^*)-isomorphism without ancillary tests.
- Equal unrecorded channels used to infer equal instrument branches.
- A global unitary with propagation radius growing with system size called a
  local equivalence.
- A bounded-propagation QCA called finite depth without an index or circuit
  witness.
- Equal braided data used to infer equality after stacking conventions have
  been left unspecified.
- An abstract endpoint-algebra isomorphism called executable despite an absent
  generator compiler.
- A compiler that preserves ideal gates while changing fault correlations or
  reference-frame semantics.

## Machine-readable theorem summary

```json
{
  "code": "topological_predictive_realization_ladder",
  "scalar_context_completion": "minimal_similarity",
  "bidirectional_positivity": "jordan_star_isomorphism",
  "ancilla_complete_order": "star_isomorphism",
  "branch_complete_tomography": "instrument_intertwining",
  "region_complete_tomography": "local_net_reconstruction",
  "uniform_support_bound": "bounded_propagation",
  "bounded_propagation_implies_finite_depth": false,
  "stable_phase_witness_required": true,
  "bidirectional_executable_compiler_required": true,
  "d_s3_current_level": "algebraic_topological_packet_with_executable_obstruction"
}
```

## Claim boundary

This packet states and derives the finite conditional reconstruction ladder. It
does not prove completeness of the current `D(S3)` tester family, classify all
two-dimensional phases, construct a gapped interpolation, or compile the
missing nonstabilizer gates.

Its structural conclusion is that the quantum-local replacement for similarity
is a bounded-propagation complete-order instrument equivalence. Phase identity
and executable constructor identity remain strictly stronger claims.
