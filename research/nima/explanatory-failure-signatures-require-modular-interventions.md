# Explanatory failure signatures require modular interventions

## Attack on holistic ablation

A complete lookup table can answer every ablation query if the varied cases
are also tabulated. Predicting outputs under variation is therefore not enough.

The stronger explanatory claim is modular: one mechanism can be replaced
while the identities and laws of the remaining mechanisms persist.

## Structured constructor

Let a realization be assembled from source-typed modules

\[
E=\mathcal I(M_1,\ldots,M_k),
\]

where \(\mathcal I\) is the Carrier interconnection law and each \(M_i\) has a
declared state, port type, and coefficient lens.

A modular intervention replaces one component:

\[
\operatorname{do}_i(M_i\leftarrow M_i').
\]

The explanation must predict:

- which interfaces remain valid;
- which state and readout laws remain invariant;
- which downstream consequences change;
- which coherence or compatibility condition can fail;
- whether the replacement stays inside the admitted model class.

The invariant remainder is as important as the changed output.

## Control-theoretic form

For an interconnected linear system, write the closed-loop realization as a
structured composition of plant, controller, actuator, and sensor blocks.
A perturbation of the actuator block should not silently redefine the sensor
or controller coordinates.

The local failure derivative has block columns

\[
D\Sigma_E
=
\begin{pmatrix}
D_{M_1}\Sigma_E&
\cdots&
D_{M_k}\Sigma_E
\end{pmatrix}.
\]

Its support pattern records which observed consequences are sensitive to each
module. A dense unstructured parameterization may reproduce the same transfer
function while erasing this intervention meaning.

Module-level identifiability therefore asks whether distinct admissible block
variations have distinct complete effects modulo block-preserving gauge.

## Gauge restriction

An arbitrary similarity transformation of a minimal state-space realization
can mix state coordinates belonging to different proposed mechanisms.

Such a similarity is harmless behavioural gauge but not automatically a
module-preserving explanatory gauge. It is authorized at the explanatory
level only when it transports:

- the module decomposition;
- module ports;
- permitted interventions;
- source meanings;
- and the interconnection law.

This separates realization equivalence from causal-module equivalence.

## Toric-code modular decomposition

The pinned toric system separates naturally into:

1. cellular Carrier incidence;
2. periodic global attachment;
3. primal and dual Pauli coefficient actions;
4. syndrome and logical readout ports;
5. noise and decoder dynamics.

These modules have distinct intervention signatures.

Changing periodic attachment can alter homology while leaving local boundary
composition intact. Changing the coefficient lens can alter commutation while
leaving cellular homology intact. Changing noise dynamics can alter decoder
choice while leaving both topology and Pauli algebra intact.

This sparse dependency pattern is the explanatory content. A holistic table
of all toric-code outputs does not expose why those invariances separate.

## Software modular decomposition

For a software service, transport, state transition, persistence, retry, and
authorization are distinct mechanisms even when one endpoint response
aggregates them.

A useful explanation predicts, for example, that changing retry policy:

- preserves request typing;
- changes duplicate-actuation risk;
- leaves authorization decisions invariant;
- may change Product accumulation while preserving Sum payload identity.

A trace table that changes all fields together does not encode this modular
counterfactual.

## Modules need not be spatial

Explanatory modules may be:

- spatial components;
- algebraic coefficient objects;
- symmetry sectors;
- boundary conditions;
- logical interfaces;
- timescale-separated effective mechanisms.

The requirement is independent intervention typing, not physical separability.
Entangled or topological systems can therefore have modular explanations
without decomposing into independent local substances.

## Hostile cases

- The ablation table includes every varied system but specifies no invariant
  mechanism identities.
- A module boundary is chosen only after observing a sparse response.
- An arbitrary state similarity is treated as preserving causal modules.
- Replacing one module silently refits the others.
- The predicted failure signature reports changed outputs but no invariant
  remainder.
- Two block variations remain indistinguishable under every admitted probe.
- A claimed module has no independent intervention or transport typing.
- Spatial locality is required where the source supplies only algebraic or
  topological modules.

## Revised conjecture

An explanation resolves a problem by a source-typed modular constructor. Its
hard-to-vary content is a prospective pattern of change and invariance under
independently admitted module replacements, modulo gauges that preserve the
module and intervention structure.

The Carrier gives the interconnection. The coefficient lenses give the module
effect laws. The failure signature records how changing one law propagates
through the fixed interconnection.
