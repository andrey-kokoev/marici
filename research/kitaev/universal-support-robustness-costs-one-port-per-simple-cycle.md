# Universal Support Robustness Costs One Port per Simple Cycle

Fix a finite graph (G). Consider interfaces whose phase-sensitive rows are
the unnormalized monomials

\[
W_C=\prod_{e\in C}z_e^{\epsilon_e}
\]

for selected unoriented simple cycles (C), together with every edge
magnitude. Suppose the interface must separate channel-gauge orbits on every
support stratum of (G).

Then every simple cycle of (G) must be selected.

Indeed, omit a simple cycle (C) and restrict to the support consisting
exactly of its edges. Every selected simple-cycle product other than (W_C)
vanishes on that support: a distinct simple cycle cannot have its entire edge
set properly contained in the edge set of (C). Edge magnitudes remain blind
to phase. Assigning opposite nonreal holonomies to (C) therefore gives two
gauge-inequivalent packets with identical retained outputs.

Conversely, retaining every simple-cycle product and every magnitude supplies
the polynomial invariant generators from the previous packet, hence
separates the compact channel-torus orbits.

Thus, within this typed cycle-monomial family, the universally
support-robust list is exactly

\[
\{|z_e|^2:e\in E\}
\cup
\{W_C:C\text{ an unoriented simple cycle}\}.
\]

## Generic compression versus robust closure

On a connected nonzero support graph, only

\[
\beta_1=|E|-|V|+1
\]

normalized fundamental holonomies are needed. Universal support robustness
can be much more expensive because every possible surviving cycle must carry
its own division-free monomial.

For (K_4),

\[
\beta_1=6-4+1=3,
\]

but there are seven unoriented simple cycles: four triangles and three
Hamiltonian four-cycles. Hence the generic phase interface has three
coordinates, while the universally support-robust cycle-monomial interface
has seven complex ports.

This is not gratuitous redundancy. If any one of those seven ports is removed,
restricting support to that cycle produces an immediate phase-blind pair.

## What the theorem does not say

The lower bound is relative to an explicitly typed interface family:
individual cycle monomials plus magnitudes, with faithfulness required on all
support strata. It does not prove that every downstream task needs full orbit
separation. Nor does it exclude a different nonlinear encoding tailored to a
restricted state family or a declared finite set of consumers.

This yields a compiler choice:

- generic-stratum reconstruction: choose a spanning forest and retain
  \(\beta_1\) normalized phases, backed by nonvanishing bounds;
- universal closure reconstruction: retain every authorized simple-cycle
  monomial;
- consumer-relative reconstruction: solve only the kernel-separation problem
  for the declared downstream rows.

The third can be much smaller, but its authority comes from the frozen
consumer list rather than from abstract orbit geometry.

## Shared geometry and authority boundary

The support restriction argument and cycle counts are shared Carrier
geometry. Whether the coefficient group is complex (U(1)), real (C_2), or
otherwise is a coefficient-lens choice. Which supports and consumers are
admissible remains source authority.

No theta graph is assumed. A theta application must derive its actual support
family before paying the universal seven-versus-three type of cost.

## Falsifiers

- Claiming universal support robustness from one fixed fundamental-cycle
  basis.
- Calling the simple-cycle lower bound coefficient-independent.
- Applying the lower bound when only one fixed support stratum is admissible.
- Retaining all simple cycles when the declared consumers need only a smaller
  separating quotient.
- Bundling multiple cycles into a scalar and calling it faithful without an
  injectivity proof on the admitted state family.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to determine whether closure redundancy is optional.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Universal support robustness forces every simple-cycle monomial within
the typed family; (K_4) exhibits the first sharp three-versus-seven gap.
