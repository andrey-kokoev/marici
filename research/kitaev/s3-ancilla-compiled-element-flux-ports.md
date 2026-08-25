# Ancilla compilation of the two element-flux ports

Owner: `marici.Kitaev`

Status: exact finite circuit theorem; hardware geometry, gate synthesis, and
fault tolerance remain outside the claim.

## Bounded question

Can the transposition and three-cycle phase ports be compiled from bounded
local interactions without treating a four-edge projector as a primitive
Hamiltonian?

Yes, conditionally on one clean six-level ancilla at the plaquette and
controlled `S3` multiplication between that ancilla and each boundary edge.
For the oriented holonomy

\[
h=g_0g_1g_2^{-1}g_3^{-1},
\]

start the ancilla in `|e>`, accumulate the four factors by controlled right
multiplication, apply a phase `exp(-i theta)` exactly when the ancilla equals
the chosen element `q`, and reverse the four multiplications.  On every edge
basis state this implements

\[
|\mathbf g\rangle|e\rangle
\longmapsto
e^{-i\theta\delta_{q,h(\mathbf g)}}
|\mathbf g\rangle|e\rangle
=e^{-i\theta B^q}|\mathbf g\rangle|e\rangle.
\]

The serial cost is exactly four two-body compute gates, one ancilla phase
gate, and four two-body uncompute gates: nine gates, with a clean ancilla at
the end.  Changing only the phase predicate compiles either the chosen
transposition or the chosen three-cycle port.

## What this realizes—and what it does not

This construction replaces the untyped four-edge analog coupling by a finite
digital interface.  It still requires a plaquette-centered ancilla capable of
coupling to all four boundary edges, exact controlled group multiplication,
an element-resolved ancilla phase, a based orientation frame, and clean
initialization.

Uncomputation does not make the port gauge invariant.  Exact enumeration
finds basis/gauge pairs on which each element predicate changes.  Replacing
the predicate by conjugacy-class membership repairs gauge invariance but
merges the element atoms required by endpoint-algebra generation.  On the
flat vacuum sector both nontrivial predicates vanish, so the circuit is
exactly trivial unless a nontrivial-flux endpoint has first been prepared.

## Verification and falsifiers

`python research/kitaev/checkers/check_s3_ancilla_flux_port_compiler.py`
checks all 1,296 edge states for each port, proves exact compute/uncompute and
phase equivalence, counts 216 marked states per element, and deliberately
exhibits gauge-frame mismatches.  Eight aggregate gates are declared.  Saved
output: `research/kitaev/results/s3-ancilla-flux-port-compiler.json`.

The result fails if the ancilla does not equal the oriented holonomy after
four gates, does not return to `e`, marks a rank other than 216, or if the
compiled phase differs from `exp(-i theta B^q)`.  Physical implementation is
falsified by absence of the six-level clean ancilla or any required
edge--ancilla multiplication coupling.
