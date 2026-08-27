# A minimal qutrit Weyl bus compiles the joint AND phase from two marginal couplings

Owner: `marici.Kitaev`

## Bounded question

Must the remaining phase

\[
I+(\omega-1)P_A\otimes P_1
\]

be implemented by one direct qutrit--fusion interaction?

No. It can be compiled exactly through a shared qutrit bus. Couple the qutrit
vacuum predicate to one Weyl generator and the fusion-channel predicate to
the conjugate Weyl generator. Their group commutator returns the bus exactly
while depositing `omega` only when both predicates equal one.

The bus dimension three is minimal. If two finite-dimensional unitaries have
scalar commutator `omega I`, taking determinants forces the dimension to be a
multiple of three.

This replaces one direct conjunction actuator by two marginal
predicate-to-bus couplings. It is a genuine decomposition of the remaining
constructor, not a reduction to separate qutrit and fusion operations: the
same coherent bus must interact with both.

## Claim boundary

The commutator compiler, dimension lower bound, bus-return theorem, and fault
propagation statements below are exact finite-dimensional results.

The packet does not construct the two controlled Weyl couplings from
`D(S3)` lattice ribbons or identify the least anyon encoding of an additional
qutrit bus. Those are now the two source-level actuator obligations.

## The qutrit Weyl pair

Let the bus Hilbert space have basis

\[
|0\rangle_B,
\qquad
|1\rangle_B,
\qquad
|2\rangle_B.
\]

Define

\[
X|j\rangle_B=|j+1\rangle_B,
\]

and

\[
Z|j\rangle_B=\omega^j|j\rangle_B,
\]

with indices modulo three. Then

\[
ZX=\omega XZ.
\]

Consequently,

\[
ZXZ^{-1}X^{-1}=\omega I_B.
\]

The cube-root phase is the central holonomy of the smallest noncommuting Weyl
pair.

## Two marginal controlled couplings

Write

\[
P=P_A
\]

for the qutrit vacuum-line predicate and

\[
Q=P_1
\]

for the orientation fusion-channel predicate.

Define a controlled bus phase

\[
U_P
=
(I-P)\otimes I_B
+
P\otimes Z,
\]

where the unshown fusion system is untouched.

Define a controlled bus shift

\[
V_Q
=
(I-Q)\otimes I_B
+
Q\otimes X,
\]

where the unshown logical qutrit is untouched.

Each constructor sees only one source predicate. Their nontrivial interaction
arises because both act on the same bus through noncommuting bus coordinates.

## Exact commutator compiler

Consider the operator word

\[
K
=
U_PV_QU_P^{-1}V_Q^{-1}.
\]

On a simultaneous predicate eigenspace with values

\[
p,q\in\{0,1\},
\]

its bus action is

\[
Z^pX^qZ^{-p}X^{-q}
=
\omega^{pq}I_B.
\]

Therefore

\[
K
=
\left(
I+(\omega-1)P\otimes Q
\right)
\otimes I_B.
\]

This is exactly the missing controlled holonomy:

\[
K=C_H\otimes I_B.
\]

No approximation, measurement, or postselection appears.

## Bus return is state-independent

Because the commutator is scalar on the bus for every pair of predicate
values, the identity holds for every initial bus state, pure or mixed, and
even when the bus is entangled with an external reference:

\[
\rho_B\longmapsto\rho_B.
\]

The ideal compiler is therefore catalytic. It requires no special bus state
and leaves no predicate record in the bus.

This exact return is stronger than uncomputing a classical truth table. The
bus traverses a noncommuting loop whose central holonomy remains on the
controls while every bus coordinate closes.

## Dimension-three lower bound

Suppose unitaries `U,V` on a `d`-dimensional bus obey

\[
UVU^{-1}V^{-1}=\omega I_d.
\]

The determinant of every finite-dimensional group commutator is one, so

\[
1
=
\det(\omega I_d)
=
\omega^d.
\]

Hence

\[
3\mid d.
\]

The smallest nonzero bus dimension is therefore three. A qubit bus cannot
carry an exact scalar cube-root commutator, regardless of how its two
unitaries are chosen.

The qutrit Weyl representation saturates the lower bound.

## Why a classical bus fails

A classical register can accumulate the two predicate values and compute
their conjunction, but it necessarily records information that distinguishes
joint sectors. Erasing that record without reversing the measurement is not a
unitary operation on an unknown superposition.

The Weyl bus instead stores the predicates in noncommuting translations. Its
closed commutator path has zero final displacement but nonzero central phase.
The useful information is geometric holonomy, not a retained classical bit.

This is exactly the distinction between a source record and a reversible
constructor.

## Constructor factorization of the full injection

The complete algebraic stack is now:

1. prepare the four-anyon fusion controller in its intrinsic `A_F` state;
2. apply the common charged route `R`;
3. execute the controlled bus `Z` coupling from `P_A`;
4. execute the controlled bus `X` coupling from `P_1`;
5. close the Weyl commutator with the two inverse couplings;
6. perform the deterministic orientation-fusion monodromy;
7. measure the middle electric pair as `A` versus `B`;
8. accept the sixth-root success or correct and retry the failure.

Steps three through five synthesize the route-incidence isometry. The bus is
available unchanged for reuse after the commutator closes.

## Candidate topological interpretations

The two marginal couplings ask for distinct physical actions:

- qutrit vacuum fusion controls a bus clock phase `Z`;
- orientation fusion channel controls a bus translation `X`.

In an endpoint-algebra language, the bus must expose two flux-resolved ports
whose actions obey the qutrit Weyl relation. This matches the previously
derived lesson that algebraically complete endpoint control requires
noncommuting ports rather than a larger central readout.

A lattice realization could use linked ribbon histories, charge-dependent
monodromy, or coherent fusion transport, provided it proves the displayed
controlled actions and exact inverse paths. The algebraic Weyl relation alone
does not authorize any one of those implementations.

## Source-authority gain

The direct coupling target required one operation simultaneously recognizing
`P_A` and `P_1`. The bus compiler requires only two marginal recognizers, each
touching one protected predicate and one common qutrit bus.

This may be physically easier because topological probes naturally couple to
one charge projector at a time. The joint logical phase then arises from the
ordered noncommutativity of the bus operations.

The gain is conditional. If neither marginal controlled Weyl action is
physically generated, the compiler has only moved the missing arrow. If both
are admitted with clean inverse histories, their composition proves the full
joint phase without a third interaction.

## Exact fault propagation

### Commuting bus controls

If the two bus actions commute, their group commutator is identity and no
joint phase appears. Both marginal couplings may work individually while the
incidence remains absent.

### Reversed commutator orientation

Reversing the word order gives

\[
\omega^{-PQ}
\]

and hence the conjugate controlled phase. With an unconjugated bridge
holonomy, the later LCU branch becomes the known rank-deficient filter.

### Incomplete inverse path

If either inverse coupling fails to cancel its forward action, the bus does
not return. It remains entangled with one or both predicates, and tracing it
out dephases the joint state.

### Weyl-angle drift

If the realized bus relation is

\[
ZX=e^{i\phi}XZ,
\]

the compiler produces `exp(i phi P tensor Q)`. The joint projector is correct
but the controlled angle drifts.

### Shared-bus fault

One bus fault between the four commutator legs can propagate through both
controlled couplings and become a correlated qutrit--fusion fault. The bus is
a common-mode actuator, so locality of its physical motion and reset must be
included in the fault model.

### Hidden bus sector

A higher-dimensional bus may decompose into qutrit Weyl sectors with
different central phases. If the sector label is unresolved, the controls
become entangled with it and the effective joint phase dephases.

## Minimal process audit

An implementation must certify:

1. `U_P` acts as identity on the complement of `P_A` and as `Z` on its image;
2. `V_Q` acts as identity on the complement of `P_1` and as `X` on its image;
3. the same bus carries both actions;
4. the bus relation has central phase `omega` in every occupied bus sector;
5. both inverse paths return all ribbon, position, clock, and environment
   ports;
6. the full word produces the earlier `3/4,1/4` Schmidt witness on the
   qutrit--fusion probe while returning the bus.

The final Schmidt witness tests the composed coupling. The first five checks
type its claimed mechanism and distinguish the intended compiler from an
unrelated entangling gate.

## Exact falsifiers

- A qubit bus is claimed to carry an exact scalar cube-root commutator.
- Determinant one of a commutator is ignored.
- The two controlled actions use distinct uncorrelated buses.
- The bus controls commute while a nontrivial joint phase is claimed.
- A classical conjunction record is called a catalytic quantum bus.
- The commutator orientation is reversed without conjugating the compiler
  frame.
- Forward bus actions are verified but their inverse return paths are not.
- Bus return is checked only after tracing out a persistent sector label.
- A shared mobile bus is assigned independent fault locations at its two
  interactions without a propagation analysis.
- Abstract Weyl generators in an endpoint algebra are treated as executable
  controlled lattice operations.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies a common bus, marginal interactions,
ordered commutator loops, catalytic return, common-mode fault propagation,
and the distinction between retained records and holonomy.

The quantum coefficient lens supplies qutrit Weyl pairs, controlled
projectors, scalar group commutators, determinant obstruction, central phases,
and coherent dephasing under unresolved bus sectors.

## Disposition

The last joint phase admits an exact modular compiler:

\[
C_H\otimes I_B
=
U_PV_QU_P^{-1}V_Q^{-1}.
\]

One shared qutrit bus is necessary and sufficient for this Weyl-commutator
mechanism. It couples separately to the qutrit vacuum predicate and the
orientation fusion-channel predicate, returns in every state, and leaves only
the desired cube-root phase on their conjunction.

The physical frontier is now two marginal controlled Weyl constructors rather
than one direct joint-projector actuator. The next `D(S3)` calculation should
search for charge-dependent ribbon actions realizing `U_P` and `V_Q` on one
common three-level endpoint bus, together with their clean inverse paths.

No build, checker, or Git operation was run for this research-only packet.
