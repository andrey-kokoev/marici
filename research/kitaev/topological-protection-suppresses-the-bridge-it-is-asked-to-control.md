# Topological protection suppresses the bridge it is asked to control

Owner: `marici.Kitaev`

## Question

Can the missing electric bridge Hamiltonian be both local in the protected
phase and strong enough for bounded-time control?

Not on any support class for which the protected fusion space is locally
indistinguishable. If a local operator projects to a scalar on the accepted
code space, its incidence between the braid-invariant line and doublet is
exactly zero. Approximate local indistinguishability bounds the bridge margin
by the same exponentially small quantity that suppresses local logical noise.

The source must therefore open an authorized actuation corridor that violates
one storage assumption in a controlled way: use noncorrectable ribbon support,
move or fuse anyons, deform the code, couple a typed ancilla bus, or leave the
code virtually and return with bounded leakage. Topological protection and
fast actuation are not independent resources on the same local support.

## Claim boundary

Locality alone does not imply scalar action. The exact theorem applies only to
operators in a support class already proved detectable or locally
indistinguishable for the frozen code and charge sector.

The exponential and Lieb--Robinson bounds below are conditional forms. Their
constants, distance parameter, correlation length, gap, and admitted support
must be supplied by the microscopic `D(S3)` lattice source. This packet does
not manufacture them from the representation-level multiplicity space.

## Frozen protected decomposition

Let `Pi` project onto the accepted total-`C` fusion or code space. Inside that
space, let

\[
P=P_u
\]

project onto the braid-invariant line and let

\[
Q=\Pi-P
\]

project onto the standard doublet.

For a microscopic Hermitian candidate `O`, its code-space bridge margin is

\[
\beta_{\Pi}(O)
=
\|QO P\|.
\]

Since `P` and `Q` lie inside `Pi`, only the projected operator

\[
\Pi O\Pi
\]

contributes to this margin.

## Exact local-indistinguishability obstruction

Suppose an admitted support class `S` satisfies

\[
\Pi O\Pi=c_O\Pi
\]

for every operator `O` supported in `S`. Then

\[
QOP
=
Q(\Pi O\Pi)P
=
c_OQ P
=
0.
\]

Therefore

\[
\beta_{\Pi}(O)=0
\]

for every operator in that correctable support class.

If a Hamiltonian is a linear combination

\[
H=\sum_X h_X
\]

and every term belongs to the same scalar-action class for the fixed code
projector, then

\[
\Pi H\Pi
=
\left(\sum_Xc_X\right)\Pi
\]

and the first-order projected bridge remains exactly zero.

This is the direct control meaning of local error detection: the code cannot
distinguish the admitted local perturbation, so the perturbation cannot enact
a nontrivial logical bridge inside that code.

## Approximate local-indistinguishability bound

Define the scalar-action defect

\[
\epsilon_{\Pi}(O)
=
\inf_{c\in\mathbb C}
\|\Pi O\Pi-c\Pi\|.
\]

For any scalar `c`,

\[
QOP
=
Q(\Pi O\Pi-c\Pi)P,
\]

so

\[
\beta_{\Pi}(O)
\leq
\epsilon_{\Pi}(O).
\]

Thus every local-indistinguishability estimate is automatically a bridge
upper bound.

For a sum of terms,

\[
\epsilon_{\Pi}(H)
\leq
\sum_X\epsilon_{\Pi}(h_X).
\]

The sum must be retained. Exponentially small error per term does not imply an
exponentially small extensive Hamiltonian without a bound on term count,
overlap, and normalization.

## Conditional topological scaling

Suppose the microscopic phase supplies a bound for normalized operators on a
region of diameter `R` separated from the relevant topological obstruction by
distance `L`:

\[
\epsilon_{\Pi}(O)
\leq
C_R
e^{-(L-R)/\xi}.
\]

Then

\[
\beta_{\Pi}(O)
\leq
C_R
e^{-(L-R)/\xi}.
\]

If the dynamics is confined to the accepted code space and this projected
operator is the only bridge, the cross-block speed limit gives

\[
T
\geq
\frac{\pi}{2C_R}
e^{(L-R)/\xi}.
\]

The same exponential suppression that protects stored information from a
normalized local perturbation makes that perturbation exponentially slow as a
logical actuator.

## Confinement and virtual-process caveat

The projected speed limit applies to dynamics generated inside the fixed
accepted subspace. A microscopic local Hamiltonian may have

\[
(I-\Pi)H\Pi\neq0
\]

and leave the code during an actuation protocol.

In that case one must derive an effective logical Hamiltonian rather than
identify it with `Pi H Pi`. Higher-order virtual processes can generate a
nonzero bridge even when the first-order projection is scalar. Their order,
energy denominators, duration, and leakage are part of the constructor packet.

The permitted conclusions are therefore distinct:

- first-order projected bridge absent;
- effective bridge generated at a declared perturbative order;
- exact time-dependent code deformation;
- uncontrolled leakage out of the accepted sector.

Only the first follows from scalar local projection alone.

## Support topology of an actuator

An operator with nonzero bridge incidence cannot belong to an exactly
correctable support class for the frozen code. A physical constructor must
therefore use at least one of the following typed mechanisms.

### Noncorrectable ribbon or network support

The operator support connects the relevant anyon neighborhoods or crosses a
topological cut. The route is extended even if each microscopic gate is local.

### Anyon motion and fusion

The excitations are transported until the fusion-channel information becomes
locally accessible. Protection changes during the motion and interaction.

### Code deformation

The accepted projector `Pi(t)` changes with time, so a term that was
correctable for the storage code need not remain correctable for the deformed
code.

### Typed ancilla bus

An ancillary quantum system carries coherence across the otherwise
correctable cut. Its preparation, transport, disentangling, and faults become
part of the logical operation.

### Virtual excursion

The system leaves the low-energy code sector and returns through a controlled
effective process. The gap and leakage bounds price the bridge.

### Measurement and coherent feed-forward

A measurement changes the Carrier and a quantum or classically conditioned
continuation returns to the desired code. A route-resolving record may destroy
the coherence, so the exact instrument must be typed rather than replaced by
its scalar probabilities.

No item in this list is automatically local, protected, or source-authorized.

## Causal support lower bound

Suppose the desired bridge must transmit a nonzero operation between endpoint
regions separated by distance `L`. Let a bounded-range microscopic evolution
satisfy a Lieb--Robinson estimate

\[
\|[A(t),B]\|
\leq
C
e^{-(L-vt)/\xi}
\]

for normalized endpoint observables. If the target operation requires the
commutator signal to reach at least `eta`, then necessarily

\[
T
\geq
\frac{
L-\xi\log(C/\eta)
}{v}.
\]

This is a causal lower bound, not an exponential protection bound. The two
obstructions can coexist:

- light-cone propagation prices how rapidly support can connect;
- local indistinguishability prices how strongly the connected process acts
  within the protected sector.

## Braid-symmetry selection rule

Support large enough to be noncorrectable is still not sufficient. Suppose a
projected candidate commutes with both electric braid generators:

\[
[H,B_{12}]=[H,B_{23}]=0.
\]

The previously derived commutant is

\[
\operatorname{span}_{\mathbb C}\{P,I-P\}.
\]

Hence every braid-invariant Hermitian candidate is block diagonal and obeys

\[
QHP=0.
\]

The group twirl makes this explicit:

\[
\mathcal T(H)
=
\frac16
\sum_{g\in S_3}
\rho(g)H\rho(g)^*.
\]

For every `H`,

\[
Q\mathcal T(H)P=0.
\]

Uncontrolled averaging over the strand-permutation frame therefore erases the
bridge even when each fixed-frame Hamiltonian has nonzero incidence.

## Operator representation content

Under conjugation by the electric braid representation

\[
\mathbf1\oplus\mathbf2,
\]

the full operator space decomposes as

\[
\operatorname{End}(\mathbf1\oplus\mathbf2)
\simeq
2\,\mathbf1
\oplus
\mathbf1'
\oplus
3\,\mathbf2.
\]

The two off-block spaces

\[
\operatorname{Hom}(\mathbf1,\mathbf2),
\qquad
\operatorname{Hom}(\mathbf2,\mathbf1)
\]

are two of the standard-doublet summands. A bridge Hamiltonian must carry a
nonzero standard component under braid conjugation. Purely invariant and sign
components cannot couple the invariant line to the doublet.

This is a source search rule: calculate the conjugation type of a microscopic
candidate before performing a full Lie closure. The correct character is
necessary but still not sufficient for locality, strength, or leakage.

## Protection--actuation tradeoff

For one frozen support class and code projector, storage and actuation demand
opposite inequalities.

Passive topological protection seeks

\[
\sup_{O\in\mathcal S}
\epsilon_{\Pi}(O)
\longrightarrow0.
\]

Fast control from the same normalized support class would require

\[
\sup_{H\in\mathcal C}
\beta_{\Pi}(H)
\geq
\beta_0>0.
\]

Because

\[
\beta_{\Pi}(H)
\leq
\epsilon_{\Pi}(H),
\]

the same class cannot satisfy both limits. Fast control must use a support,
time dependence, ancillary route, or effective process outside the passive
error class.

The correct design objective is not to abolish protection. It is to open and
close a controlled actuation corridor.

## On-state and off-state contract

A candidate physical bridge must report at least two operating regimes.

### Storage state

\[
\beta_{\mathrm{off}}
\leq
\epsilon_{\mathrm{protect}}.
\]

Residual bridge incidence is suppressed together with local logical noise.

### Actuation state

\[
\beta_{\mathrm{on}}
\geq
\beta_{\mathrm{control}}>0.
\]

The authorized corridor supplies bounded-time cross-block transfer.

The switch between them additionally needs:

- a source-derived trigger;
- a switching-time bound;
- leakage bounds during opening and closure;
- proof that the corridor closes again;
- a one-fault propagation contract;
- an independent record that distinguishes commanded opening from an
  uncontrolled logical fault.

An error with the same support and symmetry type as the bridge can imitate the
command. Topological syndrome alone need not distinguish them.

## Hostile fixtures

### Correctable local bridge

Declare a bounded local operator inside an exactly scalar-action support class
to be a logical bridge. Its projected incidence is identically zero.

### Extensive sum without normalization

Add exponentially many individually tiny local defects and quote the
single-term exponential bound for the total Hamiltonian. The omitted term
count can remove the suppression.

### Symmetry-twirled actuator

Average a fixed-frame bridge over all strand permutations. The bridge norm
vanishes after twirling even if every orbit representative is nonzero.

### Strong bridge through leakage

Use a local term with large incidence only by leaving the accepted code sector
and omit the return and leakage analysis.

### Permanent corridor

Install a noncorrectable bridge with no verified off state. Fast control is
obtained by permanently weakening the storage code against the same fault
channel.

### Slow local bridge

Use exponentially small splitting as the control interaction. Algebraic
reachability survives, while operation time grows exponentially with
separation.

## Falsifiers

- Locality by itself is asserted to imply scalar code action.
- A scalar first-order projection is claimed to exclude all virtual effective
  processes.
- Per-term indistinguishability bounds are summed without term-count and norm
  control.
- A braid-invariant Hamiltonian is claimed to cross the invariant line.
- A standard conjugation character is promoted to sufficient physical
  realization.
- A projected speed limit is applied while uncontrolled leakage leaves the
  projected space.
- A Lieb--Robinson causal bound is substituted for an exponential logical
  matrix-element bound or conversely.
- Fast control and passive protection are demanded from the same correctable
  support class without a changing projector or ancillary route.
- A permanently open noncorrectable corridor is called fault-tolerant storage.

## Disposition

The physical bridge obstruction is now tied to topological protection itself.
Every operator in an exactly locally indistinguishable support class has zero
bridge margin. Approximate indistinguishability transfers directly into a
bridge upper bound and, under confined dynamics, a control-time lower bound.

The missing electric actuator must therefore come with an explicit spacetime
corridor and a standard braid-conjugation component. The source must show how
that corridor opens, carries coherence, avoids or repairs leakage, closes, and
returns the system to a protected storage regime. This is the physical content
that algebraic endpoint generation and associator tomography do not provide.

No checker, build, or Git operation was run for this research-only packet.
