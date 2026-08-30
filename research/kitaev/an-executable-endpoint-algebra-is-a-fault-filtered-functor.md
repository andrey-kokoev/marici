# An executable endpoint algebra is a fault-filtered functor

Owner: `marici.Kitaev`

## Question

What additional structure promotes the abstract 36-dimensional endpoint
algebra of `D(S3)` to a physically executable and fault-tolerant control
system?

The missing object is not another representation of the endpoint algebra. It
is a functor from typed spacetime constructors to logical processes, equipped
with support, duration, leakage, and fault filtrations. Algebraic endpoint
generation is only the image condition of that functor after all those
filtrations have been forgotten.

## Claim boundary

This packet specifies the smallest certificate that a microscopic candidate
must supply. It does not manufacture local Hamiltonians, ancillas, ribbon
operators, measurements, or recovery maps for the frozen `D(S3)` model.

The established two-port theorem remains exact: a transposition-flux port and
a three-cycle-flux port generate the full 36-dimensional associative endpoint
algebra, while one port reaches dimension at most 24. The present result says
why that theorem is insufficient for physical controllability and identifies
the first missing source data.

## Physical constructor category

Fix a microscopic Hilbert space, an accepted code projector `Pi`, and a
logical endpoint space `H_L`. Let

\[
V:H_L\longrightarrow \operatorname{im}\Pi
\]

be the encoding isometry.

Define a typed physical constructor category `C_phys` as follows.

- Objects record the current code projector, anyon configuration, boundary
  type, ancilla inventory, and classical record algebra.
- Morphisms are finite spacetime protocols composed from the admitted local
  Hamiltonian evolutions, ribbon transports, measurements, feed-forward,
  ancilla preparations, resets, and recoveries.
- Composition is temporal concatenation only when the output typing of the
  first protocol matches the input typing of the second.
- Tensor product is spatial juxtaposition only when the declared fault domains
  and shared references permit it.

A protocol therefore carries more information than its final operator. Its
support history, intermediate code projectors, records, and recovery steps are
part of the morphism.

## Evaluation and logical compression

Let

\[
\mathcal E:\mathcal C_{\rm phys}\longrightarrow
\mathsf{CPInst}
\]

evaluate a constructor as a completely positive instrument on the microscopic
system and its declared records. For a closed protocol `c` returning to the
accepted endpoint type, define its accepted logical channel by

\[
\Lambda(c)
=
V^*\mathcal R_c\mathcal E(c)(V\,\cdot\,V^*)V,
\]

where `R_c` is the source-declared recovery and record-conditioned
continuation. If the protocol is coherently unitary and leakage-free, this
reduces to conjugation by a logical unitary. In general it is a channel, not
an element of the endpoint algebra.

The equation is meaningful only when the protocol returns every retained
record and ancilla to its declared output type. Tracing out an entangled route
record can turn a coherent constructor into dephasing while leaving some
endpoint probabilities unchanged.

## Four forgetful maps

There are four distinct losses of structure:

\[
\mathcal C_{\rm phys}
\longrightarrow
\mathsf{LogicalChannels}
\longrightarrow
\mathsf{LogicalOperators}
\longrightarrow
\mathsf{EndpointAlgebra}
\longrightarrow
\mathsf{ScalarReadouts}.
\]

The first arrow forgets the spacetime realization but retains the induced
channel. The second is defined only for coherently unitary channels. The third
forgets cost and admitted generator words. The fourth evaluates chosen
effects.

None of these arrows has an automatic inverse. In particular, equality in
the 36-dimensional endpoint algebra does not imply equality of physical
constructors, and equality of scalar readouts does not imply equality of
logical channels.

## Fault filtration

Equip every physical morphism `c` with a family of fault sets

\[
\mathfrak F_0(c)\subseteq\mathfrak F_1(c)\subseteq\cdots,
\]

where `F_t(c)` contains the microscopic fault histories admitted as at most
`t` independent faults. Independence is causal and physical; nominally
separate pulses driven by one unverified controller need not define separate
fault locations.

For a target logical channel `T`, a level-`t` implementation certificate is a
constructor `c` such that every fault history `f` in `F_t(c)` satisfies

\[
\left\|\Lambda(c,f)-T\right\|_\diamond\leq\epsilon_t.
\]

It must also report leakage

\[
\ell(c,f)
=
\sup_\rho
\operatorname{Tr}
\bigl[(I-\Pi_{\rm out})\mathcal E(c,f)(V\rho V^*)\bigr],
\]

duration, maximal support diameter, ancilla count, record fanout, and the
residual closure-holonomy bound.

The certificate is compositional only with a proved fault-spread rule. If a
single input fault can produce faults in `r` downstream locations, then a
level-`t` claim cannot compose by simply adding nominal location counts.

## Exact executable completeness

Let `A_end` be the represented endpoint algebra. A physical constructor
surface is exactly executable-complete when three conditions hold.

### Logical image

The coherently unitary accepted channels generated by closed constructors
contain the desired target group, or their linearized operator image spans the
declared algebra. This is the ordinary controllability condition.

### Typed section

There is a compiler

\[
s:\mathcal G_{\rm target}\longrightarrow\mathcal C_{\rm phys}
\]

such that

\[
\Lambda(s(U))=\operatorname{Ad}_U
\]

and composition is preserved up to a declared, correctable coherence cell.
Surjectivity of `Lambda` without a section is not an executable compiler.

### Uniform filtered bounds

Over the intended code-size family, the support, duration, leakage, recovery,
and level-`t` logical-error bounds obey the declared scaling contract. Full
Lie rank at every finite size does not suffice when the bridge margin tends to
zero and synthesis time diverges.

These conditions respectively mean existence of logical effects, selection of
physical realizations, and stable execution.

## The `D(S3)` first missing datum

The two abstract flux ports are algebra elements. To lift them into
`C_phys`, each port needs a constructor signature

\[
\sigma(P)
=
(X(t),\Pi(t),H(t),M(t),A(t),R(t),\mathfrak F(t)).
\]

The entries record spacetime support, code-projector path, Hamiltonian control,
measurement instrument, ancilla state, recovery, and fault model.

The first currently absent arrow is

\[
\{P_{\tau},P_{\rho}\}
\longrightarrow
\operatorname{Mor}(\mathcal C_{\rm phys}).
\]

Here `tau` denotes a transposition-flux port and `rho` denotes a
three-cycle-flux port.

Until this lift is supplied, products of the two projectors are formal
endpoint-algebra products. They are not certified sequential laboratory
operations. The exact 36-dimensional closure constrains what a successful
lift must generate; it does not construct the lift.

## Constructor kernel

Two physical protocols can induce the same endpoint operator while differing
in leakage, records, holonomy, or correlated fault spread. Define

\[
c\sim_{\rm op}d
\quad\Longleftrightarrow\quad
\Lambda(c)=\Lambda(d).
\]

This operator equivalence is coarser than executable equivalence. For a frozen
resource and fault contract, define

\[
c\sim_{\rm exec}d
\]

only when their accepted logical channels, admissible compositions, fault
spread, leakage bounds, record interfaces, and resource scaling agree to the
declared tolerances.

The quotient from executable constructors to endpoint operators therefore has
a physically important kernel. Corridor loops with different hidden holonomy,
or coherent and measure-and-prepare implementations with the same selected
probabilities, are explicit inhabitants of that kernel.

## Minimal finite falsifiers

### Port collision

Map both abstract flux ports to the same physical pulse. The abstract pair
generates dimension 36, but the physical image is a one-port image and has
dimension at most 24.

### Correct algebra with route dephasing

Implement each port by an instrument that records which route occurred and
discard the record. Basis endpoint probabilities can agree with the desired
projector action while coherent products are dephased. Scalar agreement does
not lift to channel agreement.

### Full rank with vanishing bridge

Let the finite-size control Lie algebra be full for every size, but let its
only off-block bridge have norm `beta_L` tending to zero. The algebraic image
remains complete while the minimum transfer time grows at least as

\[
T_L\geq\frac{\pi}{2\beta_L}.
\]

There is no uniform executable compiler.

### Closed support with residual holonomy

Return the code projector and every local syndrome to their initial values
while applying an uncontrolled logical phase. Endpoint closure and syndrome
closure hold, but constructor closure fails.

### Nominally transversal shared controller

Apply several spatially separated primitives through one common classical
command line. One command fault changes all primitives coherently. Geometric
separation does not imply independent fault filtration.

### Recovery that destroys the target

Use a recovery map that returns all population to the code space but erases
the coherence needed by the target logical unitary. Leakage is zero after
recovery, yet the diamond-distance logical error is nonzero.

## Smallest source audit

For each proposed microscopic realization of either flux port, request the
following packet before any Lie closure is promoted to physical control:

1. input and output code/anyon/record types;
2. exact microscopic generator or instrument;
3. support path and duration;
4. accepted logical channel, including retained records;
5. leakage and recovery map;
6. one-fault propagation relation;
7. off-state residual action;
8. closure-holonomy witness;
9. composition law with the other port;
10. code-size scaling of every bound.

The first failed item is the physical frontier. Later algebraic ranks cannot
repair it.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies typed objects, spacetime support, temporal
composition, record cuts, and the distinction between a route and its scalar
shadow. The quantum coefficient lens supplies completely positive
instruments, coherent versus measured composition, diamond distance, leakage,
anyon charge, and the `D(S3)` endpoint multiplication law.

The fault filtration uses both. Its causal incidence belongs to the Carrier;
which faults preserve or change a logical sector depends on the quantum code
and coefficient algebra.

## Disposition

The physical-controllability gap is now an exact missing-functor problem. The
two flux-resolved ports prove abstract endpoint generation, but a physical
theorem must lift them to typed spacetime constructors and provide a section
whose logical action, composition, leakage, closure, and fault bounds remain
uniform over the intended family.

This reframes the research target. We should not ask whether the endpoint
algebra contains the desired operation; that is already known. We should ask
for the first microscopic port lift whose filtered logical image contains it,
and then try to break the lift by route dephasing, bridge collapse, residual
holonomy, or common-mode controller faults.

No checker, build, or Git operation was run for this research-only packet.
