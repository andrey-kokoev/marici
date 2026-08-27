# Objective record fanout is bounded by a many-body light cone

Owner: `marici.Kitaev`

## Question

How rapidly can a local many-body Hamiltonian turn a localized distinction
into independently accessible classical records?

Outside the interaction light cone, no fragment can reliably distinguish two
initial states that differ only in the source region. A Lieb--Robinson
quasi-locality estimate transfers directly into an upper bound on fragment
trace distance and therefore a lower bound on record-formation time.

On a finite-dimensional lattice, the number of disjoint bounded fragments
that can carry a fixed-quality record is additionally bounded by the volume of
the causal ball. Redundancy cannot appear everywhere at once.

## Claim boundary

This packet assumes a frozen metric lattice, a bounded-range or sufficiently
decaying Hamiltonian with a declared Lieb--Robinson estimate, and two initial
states whose restrictions outside a source region agree exactly.

The result is a causal upper bound on possible record quality. It does not
prove that fragments inside the light cone actually receive a readable
record. That requires a lower bound derived from the interaction and pointer
dynamics.

The packing bound additionally assumes bounded fragment size or diameter and
polynomial volume growth. Tree-like interaction graphs, long-range couplings,
pre-shared correlations, and mobile external carriers require modified
geometry.

## Source-local distinction

Let `S` be a finite source region. Consider two initial states

\[
\rho_0,
\qquad
\rho_1
\]

whose restrictions to every observable supported in the complement of `S`
agree.

Equivalently, for every observable `A` supported outside `S`,

\[
\operatorname{Tr}(\rho_0A)
=
\operatorname{Tr}(\rho_1A).
\]

The distinction may be a local pointer label, an anyon endpoint charge, a
controller bit, or another source-typed alternative. The theorem uses only
its initial support.

Let

\[
\tau_t(A)=U(t)^*AU(t)
\]

be the Heisenberg evolution under the many-body Hamiltonian.

## Quasi-locality input

Let `F` be a candidate record fragment at distance

\[
L=d(S,F).
\]

Assume that for every observable `O_F` supported in `F` with norm at most one,
there is an observable `O_F^{(r)}` supported in the radius-`r` neighborhood of
`F` such that

\[
\left\|
\tau_t(O_F)-O_F^{(r)}
\right\|
\leq
C_F e^{-(r-v|t|)/\xi}.
\]

This is the quasi-local approximation supplied by a Lieb--Robinson theorem.
Its constants, region-size dependence, velocity, and decay length must come
from the microscopic Hamiltonian.

Choose `r` strictly below `L`, or take the limiting bound as `r` approaches
`L`. The approximant remains outside `S`, so the two initial states give it
the same expectation.

## Fragment distinguishability theorem

Let

\[
\rho_i^F(t)
\]

be the reduced state of fragment `F` at time `t`. Its pairwise trace
distinguishability is

\[
D_F(t)
=
\frac12
\left\|
\rho_0^F(t)-\rho_1^F(t)
\right\|_1.
\]

Trace-norm duality gives

\[
D_F(t)
=
\frac12
\sup_{\|O_F\|\leq1}
\left|
\operatorname{Tr}
\bigl[(\rho_0-\rho_1)\tau_t(O_F)\bigr]
\right|.
\]

Insert the quasi-local approximant. Its expectation difference is zero because
it is supported outside `S`. Since

\[
\|\rho_0-\rho_1\|_1\leq2,
\]

one obtains

\[
D_F(t)
\leq
C_F e^{-(L-v|t|)/\xi}.
\]

The right side may be capped at one. Before the light cone reaches `F`, the
fragment record quality is exponentially small.

## Record-time lower bound

For equal priors, the minimum decision error from fragment `F` is

\[
p_{\rm err}^F(t)
=
\frac{1-D_F(t)}2.
\]

Demanding error at most `eta`, with `eta` below one half, requires

\[
D_F(t)\geq1-2\eta.
\]

Combining this with the causal upper bound yields the necessary condition

\[
|t|
\geq
\frac{
L-\xi\log\bigl(C_F/(1-2\eta)\bigr)
}{v}.
\]

If the numerator is negative, the bound is vacuous. Otherwise a readable
record at distance `L` needs at least ballistic propagation time up to the
Lieb--Robinson tail.

This lower bound is independent of how clever the final fragment measurement
is. Trace distance already optimizes over every local measurement on `F`.

## Causal redundancy bound

Suppose the interaction graph has volume growth

\[
|B_R(S)|
\leq
C_{\rm vol}(R+R_0)^d.
\]

Fix a record threshold `eta`. Assume every admitted fragment:

- has at most `f_max` sites, so its quasi-locality prefactor is bounded by one
  common `C_max`;
- has diameter at most `R_F`;
- contains at least `m` sites;
- is disjoint from every other admitted fragment.

Any fragment meeting the threshold must intersect the causal ball of radius

\[
R_\eta(t)
=
v|t|
+
\xi\log\bigl(C_{\max}/(1-2\eta)\bigr).
\]

Its bounded diameter places it inside the enlarged ball with radius

\[
R_\eta(t)+R_F.
\]

Therefore the number `N_eta(t)` of disjoint readable fragments satisfies

\[
N_\eta(t)
\leq
\frac{
C_{\rm vol}
\bigl(R_\eta(t)+R_F+R_0\bigr)^d
}{m}.
\]

In fixed spatial dimension, causally available redundancy grows at most
polynomially with time under these assumptions. The exponential improvement
in discrimination with copy number from the pointer-Gram theorem must be
composed with this causal limit on how many copies can exist by time `t`.

## Combined record-quality envelope

Suppose each independently formed fragment eventually carries pure pointer
overlap magnitude `g`, and `N_eta(t)` fragments are accessible by time `t`.
The ideal product model gives global visibility

\[
V(t)=|g|^{N_\eta(t)}
\]

and global distinguishability

\[
D(t)=\sqrt{1-|g|^{2N_\eta(t)}}.
\]

The light-cone theorem bounds `N_eta(t)` from above; it does not guarantee that
the bound is achieved. Thus it supplies a speed limit on redundant
objectivity, not a formation law by itself.

The complete derivation needs both arrows:

1. locality bounds which fragments can depend on the source;
2. conditional pointer dynamics bounds how strongly they depend on it.

## Pre-shared-correlation caveat

If the initial environment is entangled across long distances, a local source
interaction still cannot signal outside the Lieb--Robinson cone through
ordinary reduced-state distinguishability. Local operations cannot change a
spacelike separated reduced state without propagation.

But pre-shared correlations can alter conditional and postselected tasks. A
distant observer given an additional classical message, a jointly accessed
port, or a postselection flag is using a larger causal protocol. Those ports
must appear in the Carrier before the simple fragment bound is applied.

## Long-range and mobile carriers

Power-law interactions can have polynomial or modified light cones. A photon,
phonon, mobile ancilla, or other carrier can transport the record through a
different metric and velocity than the static lattice graph.

These are not violations. They change the source geometry and hence the
quasi-locality input. The theorem must be rerun with the admitted interaction
graph, propagation law, and fragment locations.

Declaring a mobile carrier but omitting its launch, path, loss, and capture
ports is not a physical explanation of fast record formation.

## Redundancy versus fault independence

Many readable fragments need not define many independent fault domains. Their
causal pasts overlap near the source. A single early fault can be copied into
every downstream record.

Let `Past(F_k)` denote the spacetime support capable of influencing fragment
`F_k`. The common-mode fault locus contains

\[
\bigcap_k\operatorname{Past}(F_k).
\]

Fanout enlarges the support of an upstream error. It does not turn that error
into independent late faults.

Thus objective agreement and fault-tolerant correctness require different
certificates:

- objective agreement: many disjoint fragments carry distinguishable labels;
- differential reliability: enough fragment paths have independent faults;
- source correctness: an independent anchor detects common relabeling before
  fanout.

## Topological-sector application

A topological sector record requires an environment coupling that can
distinguish the relevant sector on its admitted support.

If local indistinguishability makes every operator in a support class scalar
on the sector code, that support cannot seed a distinguishing pointer state.
The source must expose an anyon endpoint, boundary, noncorrectable ribbon,
code-deformation corridor, or another typed sector-sensitive port.

Once such a local seed exists, its record can propagate only through the
many-body light cone. If the sector distinction itself remains globally
encoded with no exposed local seed, propagation bounds are secondary: there
is no source-local record for the environment to copy.

For `D(S3)`, the central algebra identifies the sector labels compatible with
within-block control. A physical objective-record theorem must additionally
show:

1. where the microscopic Hamiltonian first distinguishes those labels;
2. the quasi-locality constants of the record carrier;
3. the conditional fragment overlaps or trace distances;
4. the number and geometry of independently accessible fragments;
5. the common causal fault locus.

Centrality alone supplies none of these propagation data.

## Hostile fixtures

### Instant distant record

Claim a high-quality fragment record at distance `L` for time much smaller
than `L/v` under a bounded-range Hamiltonian, without a long-range or mobile
carrier port.

### Global environment distinguishability

Show that the entire environment distinguishes the source, then infer that
many disjoint small fragments do. Global and fragment trace distances are
different coordinates.

### Volume called successful redundancy

Count every site inside the light cone as a record copy without computing its
conditional reduced state.

### Readable copies called independent faults

Produce many fragments through one branching causal tree and count a fault at
the root as one independent fault per leaf.

### Topological record without a seed

Apply local environment couplings entirely inside a correctable support class
and claim they distinguish globally encoded sectors.

### Pre-shared entanglement called signaling

Infer a changed distant reduced state from entanglement alone, without a
propagating interaction or classical side port.

### Static-lattice metric applied to a mobile carrier

Use the wrong distance and velocity after admitting a photon or ancilla bus.

## Falsifiers

- A fragment outside the declared light cone has order-one trace
  distinguishability despite the frozen quasi-locality estimate and
  source-local initial difference.
- A record-time bound is stated without the source-to-fragment distance and
  Lieb--Robinson constants.
- The causal upper bound is promoted to a lower bound proving record
  formation.
- Disjoint fragments are counted without a packing or accessibility
  condition.
- Polynomial lattice volume growth is applied to a tree or long-range graph.
- Fragment redundancy is promoted to independent fault tolerance despite a
  shared causal past.
- A locally indistinguishable topological sector is claimed to seed local
  pointer discrimination.

## Shared Carrier geometry and coefficient lens

Shared Carrier geometry supplies source support, metric distance, causal
past, fragment cuts, fanout incidence, and packing. The quantum coefficient
lens supplies state trace distance, optimized discrimination, Heisenberg
quasi-locality, and the controlled pointer dynamics.

The causal theorem is a bridge: locality of observable transport becomes a
bound on record availability. Its numerical constants and sector meaning
remain source- and coefficient-dependent.

## Disposition

Redundant objective records have a finite propagation speed in a local
many-body system. A fragment at distance `L` cannot reliably distinguish a
source-local alternative before the interaction light cone reaches it, up to
the Lieb--Robinson tail. On polynomial-growth lattices, the number of disjoint
bounded readable fragments is correspondingly volume-limited.

This completes another arrow in the record-formation programme. The pointer
Gram matrix governs how record quality trades against coherence once a
fragment is correlated; the light cone governs when and where such correlated
fragments can exist. The remaining physical task is deriving matching lower
bounds, stability, and fault independence from a specific many-body
Hamiltonian.

No checker, build, or Git operation was run for this research-only packet.
