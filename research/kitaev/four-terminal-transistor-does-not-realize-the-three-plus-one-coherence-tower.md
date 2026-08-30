# Four-terminal transistor does not realize the three-plus-one coherence tower

## Question

Does the four-terminal MOSFET supply a categorical realization of the three internal coherence towers plus one functorial tower?

## Strong claim under attack

Identify source, drain, and gate with three internal coherence coordinates, identify body with the fourth functorial coordinate, and infer the coherence architecture from the four-terminal device.

## Falsifier 1: arity is not coherence dimension

A MOSFET boundary has four named electrical terminals: gate, source, drain, and body. The number four is the arity of one component presentation. It does not count semantic levels.

The same device class is routinely presented as a three-terminal component after imposing a boundary equation such as

\[
V_B=V_S.
\]

Conversely, distributed substrate contacts, multiple gates, thermal ports, and parasitic terminals can enlarge the boundary. None of these changes proves that scalar, constructor, or closure coherence has gained or lost a level.

Therefore physical terminal count cannot classify coherence-tower count.

## Falsifier 2: the body terminal is not a functor

The body terminal is another boundary variable. In a static compact model it changes the constitutive relation, for example through a body-dependent threshold. A semantic functor is instead the external assignment that maps a wiring diagram to its composite behavior and respects identities and composition.

The body belongs inside the diagram. The semantics maps the whole four-port diagram. Hence body and functor have different categorical types:

\[
B\in\partial X,
\qquad
\mathcal S:\mathsf{Wiring}\longrightarrow\mathsf{Behavior}.
\]

No relabelling makes a boundary object into the map interpreting all diagrams.

## Falsifier 3: the three coherences are not independent terminals

Scalar coherence, constructor coherence, and closure coherence form implications rather than independent material flows. Closure coherence presupposes a constructor-level object, and constructor coherence normally induces a scalar shadow after readout.

Two devices can share the same three highest supported rungs while having inequivalent constitutive laws. The triple is therefore a capability profile, not a unique factorization and not a port decomposition.

## Falsifier 4: closure coherence is relative to a boundary cut

An open subsystem can lose a distinction in its reduced state and recover it later from an excluded memory. A reduced trace distance can follow

\[
1,\;\frac12,\;0,\;\frac12,\;1,
\]

while the joint system-memory trace distance remains one. Thus no permanent reduced closure loss occurred in the enlarged system.

For a transistor, body potential is not the only possible memory locus. Charge trapping, parasitic capacitance, substrate modes, temperature, and load dynamics can carry distinctions across the chosen boundary. Closure coherence cannot be assigned to the transistor alone until the boundary cut and retained memory are declared.

## Falsifier 5: functorial composition is not transistor-specific

Resistors, capacitors, chemical reaction modules, software services, and arbitrary relations can all be assigned compositional open-system semantics. The existence of a semantics functor follows from the chosen wiring theory and behavior category, not from the component having four terminals.

Therefore the transistor does not explain why there should be exactly one fourth tower.

## What survives

The transistor remains a strong finite hostile model with the following typing:

- the terminal set specifies Carrier incidence;
- the constitutive relation specifies constructor-level behavior;
- chosen measurements provide scalar shadows;
- dynamic state, hidden memory, and quantitative margins determine closure behavior relative to a boundary cut;
- a separate semantic assignment composes wired components.

Each terminal may itself require a coherence profile. The semantics must preserve or explicitly degrade those profiles under wiring, feedback, delay, and completion.

## Repaired categorical statement

Let an open component have boundary object \(\partial X\), internal realization \(R_X\), readout \(L_X\), and declared memory cut \(M_X\). Its coherence signature is relative to this typed package, not to terminal count:

\[
\kappa(X;\partial X,R_X,L_X,M_X).
\]

A network semantics

\[
\mathcal S:\mathsf{Wiring}_{\mathrm{typed}}\longrightarrow\mathsf{Behavior}_{\mathrm{filtered}}
\]

is admissible when it maps each wiring operation to a behavior map that preserves the declared scalar and constructor distinctions and their closure margins, or reports the exact degradation.

The fourth tower belongs to \(\mathcal S\), not to any distinguished terminal.

## Verdict

The strong four-ports-equals-three-plus-one claim is false. The defensible relationship is weaker and more useful:

> A transistor is a typed open-system object on which the proposed functorial coherence laws can be tested; its fourth physical terminal is a contextual port, not the fourth coherence tower.

## First falsifier

The earliest type error is the identification of the body boundary variable with the semantic functor. They occupy different categorical levels before any device physics is calculated.

