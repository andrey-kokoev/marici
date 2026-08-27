# A clean holonomy ancilla can hide a four-edge character-phase fault

## Bounded question

Does the clean-return check in the nine-gate \(S_3\) holonomy compiler detect
every single fault on its six-level ancilla?

No. The existing exact propagation census covers permutation-like group-label
errors. A single diagonal character-phase error can pass the final
computational-basis return check and kick back a correlated phase onto all four
boundary edges.

## Frozen circuit

Let the oriented plaquette holonomy be

\[
h=g_0g_1g_2^{-1}g_3^{-1}.
\]

Let \(U\) denote the four controlled group-multiplication gates that compute
this holonomy into a clean ancilla:

\[
U|\mathbf g\rangle|e\rangle
=|\mathbf g\rangle|h(\mathbf g)\rangle.
\]

Let \(D_q(\theta)\) phase the ancilla basis state \(|q\rangle\). The ideal
nine-gate constructor is

\[
U^\dagger D_q(\theta)U.
\]

On a data basis state it implements \(e^{-i\theta B^q}\) and returns the
ancilla to \(|e\rangle\).

## The missing phase fault

The sign representation is a nontrivial one-dimensional character of
\(S_3\). Define the diagonal ancilla unitary

\[
Z_{\mathrm{sgn}}|a\rangle
=\operatorname{sgn}(a)|a\rangle.
\]

Insert this single fault after the predicate phase and before uncompute. Since
both operators are diagonal on the ancilla, they commute. Acting on a basis
input gives

\[
U^\dagger Z_{\mathrm{sgn}}D_q(\theta)U
|\mathbf g\rangle|e\rangle
=e^{-i\theta\delta_{q,h(\mathbf g)}}
\operatorname{sgn}(h(\mathbf g))
|\mathbf g\rangle|e\rangle.
\]

The ancilla returns exactly to \(|e\rangle\). The clean-return test accepts
with certainty. The data receives the extra unitary

\[
Z_{\partial p}
=\operatorname{sgn}(h)
=\prod_{j=0}^{3}\operatorname{sgn}(g_j),
\]

because inversion does not change the sign character.

This is an exact one-fault witness. It requires no stochastic approximation
and no failure of ideal uncompute.

## Why the earlier census did not see it

The earlier single-fault checker inserted nontrivial group-label errors and
tracked basis labels. Such an ancilla shift remains visible as a nonidentity
final ancilla and does not propagate into data labels because the edges are
controls and the ancilla is the target.

The character fault changes no basis label. Its information propagates by
phase kickback through \(U^\dagger\). A label-only transition table therefore
reports a clean ancilla and unchanged data labels while missing the corrupted
coherent amplitude.

The two results are compatible:

- group shifts are detected by clean return in the tested model;
- diagonal character phases are not;
- a complete quantum fault census must propagate an operator basis, not only
  classical label permutations.

## Four-edge spread

The kicked-back operator factorizes into one sign-phase factor on each of the
four boundary edges. Its support is therefore four even though the original
fault acted on one ancilla.

The mobile ancilla has contacted all four controls. Target phase errors can
propagate backward through controlled multiplication onto every earlier
control during uncompute. The rule that target faults never spread to controls
is true for permutation shifts in this circuit orientation, but false for the
conjugate phase sector.

An insertion later in the uncompute sequence produces the corresponding phase
on only the controls whose inverse contacts remain. Fault time determines the
support suffix. The maximum spread is attained by insertion before all four
inverse contacts.

## Local syndrome behavior

The sign of holonomy is a conjugacy-class function. Therefore

\[
\operatorname{sgn}(xhx^{-1})=\operatorname{sgn}(h).
\]

The kicked-back operator is gauge invariant. It is diagonal in flux and
commutes with the plaquette flux projectors. Consequently it need not create a
local energy syndrome that identifies the ancilla failure.

On the flat vacuum sector \(h=e\), the phase is one. On endpoint states carrying
nontrivial flux, it distinguishes the transposition class from the identity
and three-cycle classes. It can therefore alter a coherent endpoint
superposition while remaining invisible to the final ancilla check and to the
ordinary local constraint readout.

This is a central control error rather than a changed edge label.

## Fault-filtered table for the nine-gate gadget

### Ancilla group shift

Under the previously tested permutation fault model, no data edge label is
changed and the final ancilla is nonidentity. The gadget may reject safely only
if the clean-return check occurs before the data output is used.

### Ancilla character phase

The final ancilla is clean and a correlated boundary phase remains. Neither
the computational return check nor label tracking detects it. The gadget is
not one-fault detecting under a fault family containing this operator.

### Edge permutation fault

At most one edge label is changed in the existing census. Some timings also
leave an ancilla residual. Recovery requires a declared local \(D(S_3)\)
decoder; the circuit itself does not select one.

### General two-body multiplication-gate fault

A general fault can contain both edge and ancilla operator components. Its
ancilla phase component may propagate to later controls. The group-shift census
does not justify a one-edge bound for the full quantum operator algebra.

### Predicate phase fault

An angle error, wrong marked element, or additional diagonal ancilla phase can
return the ancilla clean while changing the compiled data unitary. This is an
actuator fault. It requires verified phase injection or an independent
constructor check, not merely bus uncomputation.

### Gauge-frame fault

A frame displacement can conjugate the meaning of \(q\) while leaving the
compute and uncompute algebra exact. It is detected only relative to the
independent frame anchor developed in the preceding packets.

## Accepted-operation failure

The character-phase witness violates the branchwise criterion for a
one-fault-tolerant gadget:

- the final clean-return branch accepts;
- the implemented endpoint operation differs from the target;
- no retained syndrome identifies the fault;
- and frame comparison does not detect it because the orientation need not
  move.

Thus the present nine-gate circuit is exact ideally and fault detecting for a
restricted permutation fault family. It is not one-fault detecting for the
full ancilla operator algebra.

## Minimal repair requirements

Any repair must distinguish at least the nontrivial character-phase sector
from the clean ancilla history. Possible architectures include:

- an encoded ancilla code detecting both group shifts and diagonal phases;
- verified preparation and verification of the multiplication bus before and
  after its contacts;
- a fault-tolerant teleportation gadget whose resource state includes phase
  checks;
- or a second independently compiled evaluation of the boundary character.

A repeated computational-basis measurement of the ancilla is insufficient.
The missing information is phase, not label.

The repair must also avoid measuring the holonomy itself, which would dephase
coherent superpositions between endpoint flux sectors. Phase-error detection
has to be compatible with coherent uncomputation.

## General finite-group theorem

Let \(G\) be a finite group with a nontrivial one-dimensional unitary character
\(\chi\). If a clean bus computes an ordered product

\[
h=\prod_j g_j^{\epsilon_j},
\]

then an ancilla fault

\[
Z_\chi|a\rangle=\chi(a)|a\rangle
\]

inserted before uncompute produces

\[
\chi(h)=\prod_j\chi(g_j)^{\epsilon_j}
\]

on the data while the bus returns clean. The fault support can therefore grow
to every control contacted by the bus.

Groups with trivial abelianization have no nontrivial one-dimensional
character, but that does not prove phase-fault safety. Higher-dimensional
Fourier sectors can still propagate nonclassical target errors. The character
construction is a minimal exact witness, not a complete classification.

## Exact falsifiers

- The sign-character insertion claimed to leave a nonidentity final ancilla.
- A label-only error census claimed complete for arbitrary quantum bus faults.
- The kicked-back sign phase claimed to have support on fewer than four edges
  when inserted before all inverse contacts.
- Computational-basis return verification claimed to detect diagonal ancilla
  phases.
- Ideal uncomputation claimed to remove a fault inserted between compute and
  uncompute.
- A clean final ancilla used as proof that the intended data unitary occurred.
- Distance-three sufficiency inferred from the one-edge permutation bound
  without propagating the ancilla phase sector.
- A phase-sensitive repair that measures and leaks the endpoint flux label.

## Machine-readable obstruction

```json
{
  "code": "clean_holonomy_bus_hides_character_phase_fault",
  "group": "S3",
  "circuit": "four_compute_plus_predicate_plus_four_uncompute",
  "fault": "ancilla_sign_character_phase_before_uncompute",
  "final_ancilla": "identity",
  "clean_return_accepts": true,
  "data_residual": "sign(g0)*sign(g1)*sign(g2)*sign(g3)",
  "data_support": 4,
  "basis_labels_changed": false,
  "gauge_invariant": true,
  "flat_vacuum_action": "identity",
  "nontrivial_flux_action": "class_dependent_phase",
  "permutation_fault_census_complete_for_this_fault": false,
  "full_one_fault_detection": false,
  "phase_sensitive_ancilla_protection_required": true
}
```

## Deutschian explanation

Uncomputation removes information written in the bus by the intended compute.
It does not reverse an error inserted after that compute. A phase error is
especially dangerous because inverse controlled multiplication converts the
bus phase into phases on the controls while still restoring the bus label.

The bus looks clean precisely because the fault left no classical residue
there. Its effect has moved into the data. Looking only at labels mistakes an
empty pointer for a faithful history of the operation.

## Shared Carrier geometry and quantum coefficient lens

The Carrier geometry is a mobile bus contacting four controls and then
retracing its path. Any bus degree of freedom capable of propagating backward
through inverse contacts has a four-edge causal cone.

The quantum coefficient lens supplies the dual phase sector and kickback. A
classical permutation lens sees only group-label shifts and therefore projects
away the hostile fault. Full constructor equivalence requires propagation of
both translation and character components of the bus operator algebra.

## Claim boundary

This packet proves one exact phase-fault witness and its four-edge spread. It
does not enumerate a complete six-level operator basis, construct an encoded
phase-protected ancilla, determine a code distance for the full microscopic
model, or prove that every phase fault is syndrome invisible.

## Process calibration

Excitement is 10/10 and confidence in the witness is 10/10. The result changes
the fault-tolerance verdict materially: the ideal nine-gate compiler and its
permutation-fault census do not yet form a one-fault-tolerant extended gadget.
The next exact task is the full Peter-Weyl propagation decomposition of the
ancilla operator algebra through controlled \(S_3\) multiplication.
