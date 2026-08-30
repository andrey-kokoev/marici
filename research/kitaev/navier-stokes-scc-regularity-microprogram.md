# Navier–Stokes SCC regularity microprogram

## Objective

Locate the first irreducible failure in

\[
\text{smooth divergence-free data}
\longrightarrow
\text{local classical flow}
\longrightarrow
\text{weak global completion}
\longrightarrow
\text{global smooth flow}.
\]

The programme distinguishes existence of weak observational shadows from continuation of the classical solution constructor.

## Scope

- Three-dimensional incompressible Navier–Stokes on \(\mathbf R^3\), with a separately typed periodic variant if used.
- Smooth divergence-free initial data of the class required by the official problem.
- Leray–Hopf weak solutions as a completion fixture.
- Global smooth existence versus finite-time breakdown.

## Twelve moves

### M1 — Freeze the PDE packet

Record domain, viscosity, initial-data class, pressure normalization, decay or periodic conditions, and the exact solution concept.

### M2 — Derive the local constructor

Construct the local smooth solution and its maximal interval. Record uniqueness and continuous dependence only in the topology actually proved.

### M3 — Freeze scaling and critical quantities

Derive the Navier–Stokes scaling and classify every norm used as subcritical, critical, or supercritical. Reject estimates whose constants hide a scale drift.

### M4 — Derive the energy channel

Derive the classical energy identity and the Leray–Hopf energy inequality. Keep equality and inequality as different coherence cells.

### M5 — Freeze continuation criteria

State source-authorized criteria under which bounded control of a declared norm extends the classical flow. A criterion is an implication, not an a priori bound.

### M6 — Construct the frequency and local-energy packet

Decompose the flow into scale-localized or spatially localized packets with exact reconstruction, flux, pressure, and commutator terms.

### M7 — Audit nonlinear transfer

Track how the transport nonlinearity moves energy between scales and locations. Scalar total-energy conservation cannot rule out concentration.

### M8 — Construct the weak completion

Pass finite approximations to a global weak solution. Record which products, local balances, and uniqueness properties survive the limit.

### M9 — Type every completion residue

Retain concentration, oscillation, anomalous flux, pressure, and defect-measure residues. Vanishing in the distributional equation does not imply vanishing in the regularity topology.

### M10 — Seek the completion-stable regularity margin

Find a scale-uniform estimate controlling a continuation norm from authorized source data. The estimate must survive approximation, localization, and completion.

### M11 — Separate the two terminal constructors

Return either:

- a global smooth continuation constructor; or
- a finite-time singularity constructor satisfying the official breakdown requirements.

Numerical blowup and loss of one estimate are neither.

### M12 — Issue the first-failure certificate

Classify the selected packet as local-only, weak-global, conditionally regular, globally smooth, or rigorously singular, and identify the earliest unavailable estimate or limit passage.

## Hostile fixtures

- bounded total energy with unbounded critical norm;
- smooth finite approximations converging only weakly;
- energy inequality promoted to energy equality;
- pressure or commutator residue discarded under localization;
- regularity of one component promoted without a reconstruction theorem;
- a continuation criterion presented as proof that its hypothesis holds;
- finite-resolution numerical regularity promoted to a uniform bound;
- apparent blowup caused by a coordinate, discretization, or boundary artifact;
- uniqueness in a strong class promoted to uniqueness of weak solutions.

## First expected result

\[
\text{global weak observability}
\not\Rightarrow
\text{global classical constructibility}.
\]

The first useful SCC result should identify the exact residue or critical norm not controlled by the energy channel.

