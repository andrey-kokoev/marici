# A finite gauge frame cannot be invariant, sharp, and exactly catalytic

## Bounded question

Can the six-state relational (S_3) frame be prepared in a gauge-invariant
state, used to implement a noncentral element-flux operation on the data, and
returned exactly unchanged and uncorrelated for reuse?

## Frozen symmetry surface

Let the data Hilbert space carry a gauge representation

\[
U_x:H_D\longrightarrow H_D
\]

and let the reference carry the left-regular representation

\[
L_x:H_R\longrightarrow H_R.
\]

An allowed symmetric joint unitary (V) satisfies

\[
[V,U_x\otimes L_x]=0
\]

for every (x\in S_3).

Let the reference begin in a gauge-invariant pure state 

\[
L_x|\eta\rangle=|\eta\rangle.
\]

For the regular representation, the invariant line is spanned by

\[
|+\rangle
=
\frac{1}{\sqrt6}
\sum_{r\in S_3}|r\rangle.
\]

## Exact catalytic no-go

Assume the joint unitary returns the reference exactly and without correlation:

\[
V(|\psi\rangle\otimes|\eta\rangle)
=
W|\psi\rangle\otimes|\eta\rangle
\]

for every data state (|\psi\rangle).

Then the induced data unitary (W) must commute with every gauge action:

\[
[W,U_x]=0.
\]

To prove this, apply (V) after a joint gauge transformation. Symmetry and
reference invariance give

\[
V(U_x|\psi\rangle\otimes|\eta\rangle)
=
(U_x\otimes L_x)V(|\psi\rangle\otimes|\eta\rangle).
\]

Using exact return on both sides yields

\[
WU_x|\psi\rangle\otimes|\eta\rangle
=
U_xW|\psi\rangle\otimes|\eta\rangle.
\]

Hence (WU_x=U_xW).

An invariant, exactly reusable, uncorrelated reference cannot induce a
gauge-noninvariant operation on the data.

## Consequence for element-flux phases

For noncentral (q), the based element-flux phase

\[
W_q(\theta)=e^{-i\theta B^q}
\]

does not commute with the base-vertex gauge action for generic (	heta).
Therefore it cannot be implemented under all three assumptions:

1. invariant reference preparation;
2. symmetric joint dynamics;
3. exact uncorrelated reference return.

The relational projector

\[
P_q
=
\sum_rB^{rqr^{-1}}\otimes|r\rangle\langle r|
\]

is gauge invariant and may be exponentiated jointly. What cannot be done is
discard the reference afterward while claiming that a noncentral absolute
element phase remains on the data alone.

## The reference trilemma

An exact implementation must choose among three source types.

### Retained relational frame

Keep the six-state reference as part of the predictive carrier. The operation
is gauge invariant jointly, and element identity remains relational. The
reference may become correlated with endpoint flux and must be included in all
future constructors, noise models, and cleanup claims.

### Sharp boundary frame

Prepare a sharp orientation such as 

\[
|e\rangle.
\]

This selects a frame and recovers the based element-flux compiler. The state is
not invariant under left gauge action. It must be typed as a boundary condition,
external reference, gauge fixing, or symmetry-breaking apparatus resource.

### Gauge-averaged data control

Demand an invariant state and exact catalytic return. Then the induced data
operation lies in the gauge commutant. Element-flux control collapses to a
conjugacy-class or other gauge-invariant operation.

No route provides absolute element resolution for free.

## Invariant local frame Hamiltonian

The one-register Hamiltonian

\[
H_+=I-|+\rangle\langle+|
\]

is gauge invariant and has the unique invariant frame state 

\[
|+\rangle
\]

as its ground state. It prepares symmetry, not a sharp orientation.

Conversely,

\[
H_e=I-|e\rangle\langle e|
\]

selects a sharp frame but fails to commute with left gauge transformations.

Thus a local gauge-invariant Hamiltonian on one regular reference register
cannot have a unique sharp orientation as its nondegenerate ground state.

## Two-reference locking

Introduce two regular reference registers (R_1,R_2). A gauge-invariant
interaction can lock their relative orientation. For example, the projector
onto equal group labels,

\[
P_{=}=
\sum_r|r,r\rangle\langle r,r|,
\]

commutes with the diagonal left action

\[
L_x\otimes L_x.
\]

This stabilizes the relation between the frames but leaves their common global
orientation unresolved. Relative locking can distribute one frame consistently
across apparatus components; it cannot manufacture an absolute origin from
symmetric dynamics.

The remaining global torsor is exactly the common-mode frame degree of freedom.

## No independent reference by copying

Copying one sharp frame label to several registers produces correlated
references with one common origin. A frame displacement before copying moves all
copies together and remains invisible to equality checks.

Independent frame verification requires a second preparation path whose common
causes are separately typed. Redundant labels derived from one frame increase
readout reliability but do not certify the origin.

This is the gauge-frame instance of the fanout fault-locality theorem.

## Approximate catalytic use

A large or specially prepared asymmetric reference may approximate repeated
noncovariant operations while changing only slightly per use. That does not
contradict the exact theorem.

An approximate claim must state:

- the reference asymmetry resource;
- the distance from its initial state after each use;
- correlations accumulated with the data;
- the number of permitted reuses;
- and the operational error in the induced element-flux pulse.

A finite six-state frame has no automatic unlimited-reuse guarantee.

## Implication for the nine-gate flux compiler

The existing nine-gate ancilla circuit exactly computes, phases, and uncomputes
a based holonomy. Its clean six-level holonomy ancilla is not automatically the
gauge reference proved necessary here.

There are two six-state registers with different types:

- the computational ancilla temporarily stores holonomy and is returned clean;
- the relational frame defines which conjugate element is called (q).

Conflating them would erase the gauge-authority problem. One register may carry
both roles only if the circuit proves the correct joint transformation law and
restores both the computational workspace and the frame resource.

The exact catalytic no-go shows that such restoration cannot leave a
noncentral data-only pulse under invariant symmetric conditions.

## Fault-tolerance consequence

The frame has at least three fault classes.

1. A pure gauge transformation applied jointly to data and frame changes no
   relational observable.
2. A frame-only displacement changes the relative element labels and can
   conjugate both control ports coherently.
3. Decoherence or leakage of the frame can erase relational resolution and
   reduce control to class information.

The second fault is common mode across both flux ports. The third is a loss of
control capacity, not merely a wrong scalar record.

A fault-tolerant compiler must preserve the frame relation throughout the
endpoint pulse sequence or detect its displacement with an independent
relational check.

## General symmetry theorem

Let (G) be any group, (U_g) and (L_g) representations on data and
reference, and let (|\eta\rangle) be (L_g)-invariant. If a joint
(G)-symmetric unitary returns (|\eta\rangle) exactly and uncorrelated while
inducing (W) on all data states, then (W) lies in the commutant of (U(G)).

The theorem does not depend on the details of (D(S_3)). It is a finite exact
reference-frame obstruction for any symmetric constructor theory.

## DPC: reference use must be thermodynamically and causally typed

The conjecture is:

> A noninvariant control cannot be obtained from an invariant, exactly reusable,
> uncorrelated reference through symmetric dynamics. A programme claiming
> element-resolved control must retain the relational frame, supply a sharp
> boundary reference, or quantify consumption of an asymmetric reference.

This turns gauge-frame language into a constructor and resource statement.

## Critics

### Gauge fixing is mathematically harmless

It may be harmless for calculation. Operational element control still requires
an apparatus whose interactions implement that fixing. The theorem identifies
the missing source resource.

### The uniform state contains all orientations coherently

It does, but no preferred orientation. Symmetric catalytic use cannot leave a
noninvariant operation on the data while returning that state exactly.

### The reference can be uncomputed

Workspace information can be uncomputed. Asymmetry cannot be both used to
induce a noncovariant data operation and returned as an invariant uncorrelated
catalyst under the stated exact conditions.

### A second reference solves the problem

It can supply a relational anchor. Symmetric coupling only locks the two
references relative to one another; their shared global orientation remains a
torsor unless an external boundary condition is added.

### Real reference frames are macroscopic

Then approximate asymmetry-resource and degradation bounds are required. The
finite theorem remains the exact zero-error boundary.

## Exact falsifiers

- A symmetric joint unitary and invariant exactly returned reference inducing a
  data unitary outside the gauge commutant.
- A unique sharp-frame ground state of a one-register gauge-invariant
  Hamiltonian.
- Relative locking of two frames claimed to select their global orientation.
- A clean holonomy workspace ancilla treated as a gauge reference without its
  transformation law.
- A copied frame label called an independent origin check.
- An approximate reusable frame claimed exact without degradation or
  correlation bounds.
- A forgotten relational frame claimed to leave noncentral element control on
  data alone.

## Machine-readable trilemma

```json
{
  "code": "finite_gauge_frame_catalytic_no_go",
  "reference_invariant": true,
  "joint_dynamics_symmetric": true,
  "reference_returned_exactly": true,
  "reference_uncorrelated": true,
  "induced_data_operation_gauge_invariant": true,
  "noncentral_element_flux_data_pulse_possible": false,
  "allowed_repairs": [
    "retain_relational_frame",
    "supply_sharp_boundary_frame",
    "accept_gauge_averaged_control",
    "quantify_approximate_reference_consumption"
  ]
}
```

## Deutschian explanation

A reference frame is useful because it carries asymmetry. If the reference
begins completely symmetric, undergoes only symmetric dynamics, and returns
exactly unchanged, no asymmetry has entered the data. The induced operation must
respect the symmetry.

Element identity becomes actionable only as a relation to a retained frame or
to a boundary that selects one. The frame is part of the physical explanation,
not a coordinate convention that can disappear after the calculation.

## Claim boundary

This packet proves the exact catalytic symmetry no-go and the one- and
two-reference Hamiltonian statements. It does not quantify approximate
reference degradation, construct a macroscopic boundary frame, or provide a
fault-tolerant relational-frame code.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was a physical preparation and reuse theorem
for the six-state relational frame.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Exact invariant catalytic use is impossible; the source
must retain, break, or consume the frame resource explicitly.
