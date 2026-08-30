# Hostile contexts falsify endpoint task equivalence as a license to fill cycles

Owner: marici.Kitaev

## Question

Is a cycle legitimately fillable whenever its competing paths are said to
implement the same task, or can apparently identical tasks become
distinguishable under composition, control, purification, or a richer
coefficient lens?

## Claim boundary

The unqualified fillability principle is false.

Agreement at the endpoint, agreement of scalar readout, and even equality of a
reduced system channel do not suffice to authorize a coherence cell. A path
relation may be quotiented only when it is a congruence for every authorized
constructor context.

Let (P,Q:X	o Y) be two paths. Define a declared context family
(mathcal C_{mathrm{auth}}). The relevant equivalence is

[
Psimeq_{mathcal C}Q
quadLongleftrightarrowquad
C[P]=C[Q]
	ext{ for every }Cinmathcal C_{mathrm{auth}}.
]

The contexts must include every authorized form of:

- precomposition and postcomposition;
- parallel composition with ancillary systems;
- coherent control;
- requirement pullback and intervention push-forward;
- environment or purification access retained by the source theory;
- task-localized measurement.

Only such a context-stable equivalence can be safely attached as a 2-cell.
Endpoint equality is merely one projection of it.

### Falsifier 1: global phase under coherent control

Take

[
P=I,
qquad
Q=e^{iphi}I.
]

As isolated quantum channels on density matrices, (P) and (Q) are
identical. If the task localization retains only conjugation, filling the cycle
projectively is legitimate.

Place the path under coherent control, however. The relative phase becomes a
phase on the control branch and is interferometrically observable. Then
(P) and (Q) are not contextually equivalent.

This falsifies the rule “equal channels imply a fillable cycle.” It also shows
that the authorized center depends on the admitted higher-order contexts.

### Falsifier 2: equal readout, different state update

Two instruments can have the same outcome probabilities for every admitted
input while producing different conditional post-measurement states. A scalar
observer sees identical endpoint tasks. A later constructor acting on the
post-measurement state distinguishes them.

Therefore equality of effects does not imply equality of instruments. A
coherence cell fitted from the scalar readout would erase executable
information.

### Falsifier 3: equal reduced channel, different environment record

Let two dilations induce the same channel on the retained system but write
different path labels into an environment. If the environment is permanently
discarded, the reduced task may quotient the paths. If an authorized later
interaction can return that record, the paths interfere differently and no
filler is legitimate.

Thus fillability is relative not merely to present observations but to the
declared closure of future authorized interactions.

### Falsifier 4: projective relation promoted to a linear context

A constructor representation may satisfy a group relation only up to a central
phase. Treating the relation as strict gives a valid projective theory. Tensor
products, boundary couplings, or a chosen phase reference can promote the
central phase to observable relative data.

Consequently a projective 2-cell cannot be silently replaced by an identity
2-cell. The coefficient-valued filler must be retained.

### Falsifier 5: locally removable connection with global holonomy

A connection can be gauged away on each local patch while retaining nontrivial
holonomy around a global loop. Local recalibratability therefore does not imply
global fillability. The recalibrations themselves must agree on overlaps; their
transition cocycle is precisely where the global obstruction resides.

This falsifies the simpler intervention criterion “if local recalibration
removes the mismatch, it was only frame residue.”

### What survives the attacks

A sharpened rule survives:

A cycle is fillable relative to a declared constructor theory only when a
source-derived comparison proves its two paths equivalent under every
authorized context, and that equivalence is preserved by composition,
localization, and completion.

Equivalently, the proposed path relation must define a typed congruence in the
constructor category. If there exists an authorized separating context
(C) with

[
C[P]
e C[Q],
]

then the cycle carries task-visible holonomy and cannot be filled in that
theory.

This rule remains task-relative. Enlarging the authorized context family can
split a previously valid equivalence class. That is not inconsistency: it is a
theory extension revealing distinctions that the earlier task intentionally
quotiented.

### Does the sharpened rule explain anything?

There remains a Deutschian criticism. Defining equivalence by
indistinguishability under every context risks becoming operational bookkeeping
rather than explanation.

The explanatory work must therefore come from a compact source law that
generates the congruence and predicts all contextual equalities. Examples
include:

- a stabilizer relation derived from the Hamiltonian;
- a naturality or triangle identity derived from a dual pair;
- a Hopf, monoidal, or braided coherence law;
- a gauge redundancy derived from the representation of preparations and
  observations;
- an error-correction relation derived from an explicit recovery constructor.

The context test is the Popperian critic. It can refute a proposed source law,
but the infinite conjunction of passed contexts is not itself the explanation.

### Minimal machine-independent falsifier

For any proposed filler (alpha:PRightarrow Q), the smallest rejection
certificate is:

- the typed paths (P,Q:X	o Y);
- the claimed source law deriving (alpha);
- one authorized context (C[-]);
- the unequal typed outputs (C[P]) and (C[Q]);
- the lowest coefficient lens in which the inequality is visible;
- the resource or completion assumptions needed to execute (C).

This is the constructor analogue of a distinguishing experiment.

## Disposition

The original statement “a cycle is fillable only by a source-derived
equivalence of tasks” is retained only after replacing task equivalence with
source-derived contextual congruence.

The attacks establish a hierarchy of increasingly strong shadows:

[
	ext{same scalar}
Leftarrow
	ext{same effect}
Leftarrow
	ext{same channel}
Leftarrow
	ext{same instrument}
Leftarrow
	ext{same controlled and purified constructor}.
]

None of the reverse implications holds automatically.

The best next finite audit is a controlled-phase triangle. Give two paths the
same reduced channel but a relative central phase, then add a control ancilla
that makes the phase observable. This is the smallest witness showing a cycle
that is fillable in one task localization and unfillable in a richer
constructor theory without changing its endpoint map.
