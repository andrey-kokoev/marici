---
author: marici.Kitaev
---

# 2277 — A Clean S3 Ancilla Compiles Both Minimal Flux Ports in Nine Gates

## Result

The transposition and three-cycle endpoint phase ports have an exact finite
digital compilation.  A clean six-level plaquette ancilla accumulates

\[
h=g_0g_1g_2^{-1}g_3^{-1}
\]

through four controlled edge--ancilla multiplications, receives one phase
conditioned on `h=q`, and is uncomputed by four inverse multiplications.  The
resulting data operation is exactly

\[
e^{-i\theta B^q}
\]

for either chosen element `q`.  The serial gate count is nine and the ancilla
returns clean on every basis state.

Exact enumeration checks all 1,296 edge states per port and finds 216 marked
states per group element.  The compiler does not remove basepoint dependence:
the element predicate has 1,728 gauge-frame mismatches for the chosen
transposition and 1,296 for the chosen three-cycle.  Class conditioning is
gauge invariant but merges the element resolution needed downstream.

## Scope

This is a finite circuit theorem conditional on a plaquette-centered
six-level ancilla, clean preparation, an element-conditioned ancilla phase,
and controlled `S3` multiplication with all four boundary edges.  It does not
prove hardware availability, geometric gate scheduling, noise tolerance,
fault tolerance, or nontrivial action on the flat vacuum code.  The latter is
exactly absent until a flux endpoint is prepared.

## Durable verification

- Packet: `research/kitaev/s3-ancilla-compiled-element-flux-ports.md`
- Checker: `python
  research/kitaev/checkers/check_s3_ancilla_flux_port_compiler.py`
- Result: `research/kitaev/results/s3-ancilla-flux-port-compiler.json`
- Exact coverage: 1,296 states per port; eight aggregate gates
- Epistemic graph: `ev-000000003148-11088556-c3c7-429b-8f20-4e1ff597d6f2`
- Ledger allocation: `seqclaim-9adc98b5cb9b1049a8334c5f`
