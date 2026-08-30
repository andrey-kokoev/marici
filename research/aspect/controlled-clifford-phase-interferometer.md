# Controlled Clifford-phase interferometer

Author: `marici.Aspect`

Date: 2026-08-26

Status: finite optical falsifier

## Question

Nima's one-qubit Clifford calculation shows that complete conjugation data
cannot distinguish the route \((HS)^3\) from identity, although

\[
(HS)^3=e^{i\pi/4}I.
\]

Is that scalar phase merely gauge, or can an optical extension make it an
observable relative phase?

## Controlled optical lift

Prepare a path qubit in an equal superposition. Leave the reference arm
unchanged and apply \((HS)^3\) to an internal two-level mode in the other arm.
Balanced recombination gives

\[
p_+=\frac{|1+e^{i\pi/4}|^2}{4}
=\frac{2+\sqrt2}{4},
\qquad
p_- = \frac{2-\sqrt2}{4}.
\]

Replacing the route by identity instead gives \(p_+=1\) and \(p_-=0\).
The controlled reference therefore exposes a fringe displacement

\[
\Delta p_+=\frac{2-\sqrt2}{4}.
\]

The target's internal state is irrelevant because the route is scalar. This
is a path-relative phase measurement, not tomography of the isolated target.

## Hostile pair

The smallest hostile consists of two devices with identical conjugation on
every Pauli operator:

- an identity route;
- the Clifford word \((HS)^3\).

Every isolated process-conjugation test identifies them. The balanced
controlled-reference interferometer separates them in one output
distribution. Thus the quotient from unitary transport to adjoint transport
is faithful only while scalar phase is explicitly typed as gauge.

## Instrument contract

Source authority requires coherent preparation across both paths. The control
constructor requires a route-selective implementation of the entire Clifford
word, not independently characterized gates spliced across runs. The phase
frame is the reference-arm optical phase at recombination. Both output ports
must be retained so normalization and visibility are testable. Phase drift,
which-path leakage, and internal-mode mismatch reduce visibility and must be
bounded by calibration rather than absorbed into the predicted \(\pi/4\)
shift.

## Boundary of the result

The calculation proves the observation contract for a controlled lift. It
does not prove that the required controlled Clifford route is available in a
given platform, nor that global phase should cease to be gauge in contexts
without a coherent reference. It gives a precise retyping rule: admitting the
reference arm changes the operational quotient and therefore changes which
route equalities are valid.

## Reproduction

Run:

    python research/aspect/checkers/controlled_clifford_phase_interferometer.py

