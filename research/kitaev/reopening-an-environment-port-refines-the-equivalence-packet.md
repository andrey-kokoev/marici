# Reopening an environment port refines the equivalence packet

## Bounded question

Can two realizations that are indistinguishable as closed system channels become
distinguishable when an environment port is reopened, and which differences
are physical rather than dilation gauge?

## Frozen levels

Let \(S\) be a finite-dimensional system. A closed channel is

\[
\Phi:\mathcal B(S)\to\mathcal B(S').
\]

A dilation is an isometry

\[
V:S\to S'\otimes E
\]

such that

\[
\Phi(\rho)=\operatorname{Tr}_E(V\rho V^*).
\]

The closed channel packet exposes only \(S'\). A reopened packet additionally
exposes specified environment preparations, observables, records, or future
constructors on \(E\).

These are different operational theories. Reopening a port changes the tester
family and therefore refines predictive equivalence.

## Stinespring uniqueness boundary

Suppose \(V_1:S\to S'\otimes E_1\) and
\(V_2:S\to S'\otimes E_2\) are minimal dilations of the same channel. Then
there is a unitary

\[
U:E_1\to E_2
\]

such that

\[
V_2=(I_{S'}\otimes U)V_1.
\]

For nonminimal dilations the corresponding relation uses an isometry after
restricting to the generated environment support.

Therefore exact equality of the full system channel does not leave arbitrary
input-dependent dilation freedom. The complementary channel is fixed up to the
same environment isometry.

This is a correction to the loose claim that “the same channel can hide any
environment behavior.” It cannot, once full channel equality and the usual
dilation gauge are frozen.

## When reopening reveals a difference

There are three distinct cases.

### Tester deficiency

The original experiments established equality only on a restricted
preparation/readout family, not equality of channels. A larger system tester,
possibly using a reference ancilla, can distinguish the maps without opening
the environment.

### Named environment structure

The two dilations are related by an environment unitary, but the reopened
packet contains a fixed environment observable, spatial mode, detector label,
Hamiltonian, cost, or downstream coupling that is not transported by that
unitary. Then the unitary is not an admitted gauge transformation of the full
packet.

The implementations may remain equivalent as closed channels while differing
as open-port processes.

### Extra implementation coordinates

The implementations differ in energy, time, locality, fault propagation,
apparatus history, or unused environment degrees of freedom. These coordinates
are invisible to the mathematical channel unless included as readouts or
constraints.

They support implementation distinctions, not a claim that the channel map was
different.

## Port-relative equivalence theorem

Let \(\mathcal T_P\) be the tester family admitted by an interface packet \(P\).
Define

\[
R_1\equiv_P R_2
\]

when every tester in \(\mathcal T_P\) gives the same probability on both
realizations.

If packet \(P'\) exposes every port and tester of \(P\), plus additional ones,
then

\[
R_1\equiv_{P'}R_2
\quad\Longrightarrow\quad
R_1\equiv_PR_2.
\]

The reverse implication holds exactly when all newly admitted tester
functionals annihilate the difference between the two realizations.

Thus port reopening can only refine the equivalence relation. It cannot merge
classes previously distinguished by retained tests.

## Environment-isometry gauge test

An environment isometry may be quotiented only if it preserves the complete
reopened packet. For a candidate \(U:E_1\to E_2\), audit:

\[
V_2=(I\otimes U)V_1,
\]

and, for every named environment constructor or effect,

\[
C^{(2)}U=UC^{(1)},
\qquad
F^{(1)}=U^*F^{(2)}U,
\]

with the analogous equations for dynamics, records, and costs.

If these coherence cells hold, the port structures are equivalent under the
declared gauge. If one fails, the first residual identifies the physical
environment distinction.

Channel equality alone proves none of these named-port equations.

## Minimal restricted-tester witness

Consider two qubit channels:

\[
\Phi_Z(\rho)=Z\rho Z,
\qquad
\Phi_I(\rho)=\rho.
\]

On computational-basis preparations followed by computational-basis
measurement, they are indistinguishable. On the input \(|+\rangle\), followed
by an \(X\)-basis measurement, they are perfectly distinguished.

This is not a hidden-environment effect. The original tester family was simply
not tomographically complete.

The shortest distinguishing context supplies the exact missing system probe.

## Minimal named-port witness

Let \(V_2=(I\otimes U)V_1\) be two minimal dilations of the same channel. If the
environment has no named structure, they represent the same dilation class.

Now freeze an environment effect \(F\) in each apparatus coordinate system. If

\[
F^{(1)}\neq U^*F^{(2)}U,
\]

then the associated joint or complementary readouts can differ. The difference
does not refute Stinespring uniqueness; it shows that the apparatus effect was
not transported with the dilation gauge.

The enlarged object is the pair \((V,F)\), not \(V\) alone.

## Dephasing example

The dephasing channel

\[
\Phi(\rho)=P_0\rho P_0+P_1\rho P_1
\]

admits an isometry

\[
V|j\rangle=|j\rangle_S|j\rangle_E.
\]

Tracing out \(E\) erases the phase between the two branches. Measuring the
environment in the computational basis exposes the which-sector record.
Measuring it in another basis defines a different instrument decomposition of
the same closed channel.

The closed channel does not select one environment measurement as canonical.
The detector coupling and record basis must be supplied by the reopened source
packet.

## Reference systems and complete channel testing

Agreement on all isolated system density operators is mathematically enough to
establish equality of finite-dimensional linear maps when the output operators
are tomographically determined. Operational discrimination and stable norms,
however, may require entangled reference inputs.

The diamond norm freezes that enlarged tester family:

\[
\|\Phi_1-\Phi_2\|_\diamond.
\]

Using it is justified only when arbitrary reference assistance is part of the
admitted operational interface. A weaker tester family induces a weaker
seminorm and a coarser equivalence.

## Closure interpretation

Closing an environment port applies a forgetful map from the open process to
the reduced system channel. Information in its kernel is unavailable to the
closed tester family.

Reopening the port does not recover the historical information automatically.
It changes the model so that future experiments may access an environment
system that was physically preserved and coherently transported. If that
system was discarded, thermalized, or never recorded, a mathematical dilation
does not recreate it.

Therefore:

- tracing a port is a mathematical quotient;
- physically retaining a port is a constructor claim;
- later access requires a transport and interface theorem;
- and choosing a dilation does not establish that its environment exists as an
  accessible laboratory subsystem.

## Toric-code analogy

Local syndrome closes the noncontractible logical probes and yields a coarser
equivalence. Adding Wilson-loop ports refines the packet and separates logical
classes.

This is analogous to reopening an environment port only at the carrier level:
an enlarged tester family exposes distinctions killed by the smaller readout.
The coefficient lenses differ. Toric logical probes use Pauli commutation and
topological intersection; Stinespring reopening uses completely positive maps
and environment effects.

Neither case licenses reconstruction of the full microscopic realization from
the refined readout.

## Software analogy

An API response can quotient away internal event history. Adding an audit
endpoint refines operational equivalence if the history was actually retained
and the endpoint is authorized to expose it.

Inventing a hypothetical event log after the state was overwritten is like
choosing a mathematical dilation after discarding the physical environment: it
supplies a representation, not recovered history.

Two implementations can satisfy the same API contract while differing under a
new observability port. Whether that is a compatible extension or a contract
change depends on the frozen interface authority.

## DPC: port-relative equivalence

The conjecture is:

> Every operational equivalence is relative to a declared set of accessible
> ports and tester contexts. Reopening a physically retained port refines the
> equivalence exactly by the new tester functionals. A mathematical dilation or
> latent-state representation alone does not establish physical retention or
> future access.

The finite tester refinement and Stinespring uniqueness statements support the
conjecture. Its physical content is the source derivation of the retained port,
transport, and named interface structure.

## Critics

### Minimal dilations are unique, so implementations are the same

Only as channel dilations up to environment isometry. Named hardware, effects,
costs, and fault surfaces can break that gauge.

### Environment measurements are just alternative Kraus decompositions

Mathematically yes for the closed channel. Physically selecting one requires a
specific detector coupling and record map.

### A hypothetical dilation always exists

Correct. Existence of a representation does not imply accessible environment
memory or reconstruct lost history.

### Enlarging testers can be unfair

Correct if the new port was not part of the original contract. The result must
be described as equivalence refinement under a changed packet, not refutation
of the original restricted equivalence.

## Exact falsifiers

- Arbitrary hidden input-dependent environment behavior claimed behind a fully
  specified channel, ignoring Stinespring uniqueness up to isometry.
- A restricted tester coincidence called channel equality.
- An environment isometry quotiented while it fails to transport a named
  effect, constructor, record, or cost.
- A mathematical dilation presented as proof of physical environment retention.
- A reopened-port distinction presented as refuting an explicitly
  closed-port equivalence claim.
- Equal channels presented as equal instruments or hardware realizations.
- A diamond-norm claim made without reference-assisted tester authority.
- Discarded history claimed recoverable because some latent representation can
  encode it.

## Deutschian explanation

Closing a port removes a family of counterfactual questions. Two realizations
become equivalent when their difference lies entirely in the kernel of those
remaining questions. Reopening a retained port adds questions and may expose
the difference.

But exact channel equality already constrains every minimal dilation to one
environment-isometry class. The genuine new physics is not arbitrary hidden
behavior; it is named port structure that prevents the isometry from being a
gauge, or evidence that the earlier tests never determined the channel.

## Claim boundary

This packet states finite-dimensional channel and tester results. It does not
prove that any mathematical environment is physically retained or accessible.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was to distinguish latent realization differences from
tester incompleteness and dilation gauge.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Stinespring uniqueness sharply limits arbitrary hidden-dilation claims.
Port reopening refines equivalence only through physically named environment
structure or an originally incomplete tester packet.
