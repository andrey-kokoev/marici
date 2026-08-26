# Plaquette Flatness Reduces Graph Phase to Carrier Cohomology

The graph-only blown-up phase quotient remembers every cycle of the
one-skeleton. If the nominal Carrier includes plaquette 2-cells, contractible
cycles must be typed separately from topological cycles.

Let a finite Carrier complex have cochains

\[
C^0(X;U(1))
\xrightarrow{\delta_0}
C^1(X;U(1))
\xrightarrow{\delta_1}
C^2(X;U(1)).
\]

An edge-phase packet (u\in C^1) transforms under vertex gauge by

\[
u\longmapsto u\,\delta_0g.
\]

Its plaquette curvature is

\[
F=\delta_1u.
\]

Because \(\delta_1\delta_0=1\) multiplicatively, curvature is gauge
invariant. Therefore the quotient of all edge phases by vertex gauge is not,
in general, purely topological: it includes local curvature data.

The flat phase sector satisfies

\[
\delta_1u=1.
\]

Modulo vertex gauge, it is

\[
\ker\delta_1/\operatorname{im}\delta_0
=H^1(X;U(1)).
\]

Equivalently,

\[
H^1(X;U(1))
\simeq
\operatorname{Hom}(H_1(X;\mathbf Z),U(1)).
\]

Its continuous dimension is the first Betti number; torsion in (H_1), when
present, contributes finite root-of-unity characters rather than continuous
ports.

## Filled triangle falsifier

The triangle one-skeleton has graph cycle rank one. If its triangular face is
filled, the cycle is the plaquette boundary. The chain ranks are

\[
\operatorname{rank}\partial_1=2,
\qquad
\operatorname{rank}\partial_2=1,
\]

so

\[
b_1=3-2-1=0.
\]

The graph (U(1)) holonomy survives only as local plaquette curvature. Under
flatness it is fixed to the identity and supplies no topological phase port.

Thus a graph-cycle count overprices topological boundary memory whenever it
ignores filled local cells.

## Minimal torus cell structure

For the standard one-vertex torus CW structure, there are two loop edges and
one 2-cell attached by the commutator. Its abelian cellular boundary is zero:

\[
\partial_1=0,
\qquad
\partial_2=0.
\]

Hence

\[
H^1(T^2;U(1))\simeq U(1)^2.
\]

The two noncontractible phase ports remain after every local plaquette
flatness condition and vertex gauge repair. This is the continuous
coefficient analogue of the two logical loop classes in the finite toric-code
pilot.

## Local syndrome versus logical readout

The correct hierarchy is

\[
\text{edge phase}
\longrightarrow
\text{plaquette curvature}
\quad\text{and}\quad
\text{flat cohomology class}.
\]

Curvature detects local failure of flatness. It does not choose a preferred
representative within a flat cohomology class. Noncontractible loop probes
separate the remaining classes.

This is shared Carrier geometry. The quantum coefficient lens adds a dual
electric/magnetic pair, Pauli commutation, and the primal--dual intersection
pairing that turns crossing logical loops into anticommuting operators. None
of those quantum conclusions follows from (U(1)) cohomology alone.

## Blown-up boundary consequence

At zero analytic amplitude, an edgewise phase-preserving completion can retain
local curvature provenance as well as flat topological provenance. If the
source declares the boundary phase flat, its intrinsic fiber is

\[
H^1(X;U(1)),
\]

not the cohomology of the bare incidence graph. If flatness is not imposed,
plaquette curvature rows must remain separately typed; they cannot be called
logical ports.

## Authority boundary and falsifiers

The theorem requires a source-derived 2-complex and plaquette incidence. It
does not authorize a theta plaquette structure or phase-flatness law.

Falsifiers are:

- counting every graph cycle as a topological phase after faces are filled;
- calling nontrivial plaquette curvature a flat cohomology class;
- using local curvature to select a preferred logical representative;
- discarding torsion characters by reporting only Betti dimension;
- inferring Pauli anticommutation from ordinary (U(1)) holonomy;
- importing toric plaquettes into theta/Fock incidence without a constructor.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to restore the plaquette layer omitted by graph-only phase
counting.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Local curvature and flat topological phase now separate exactly; a
filled triangle loses its graph cycle, while the torus retains two ports.
