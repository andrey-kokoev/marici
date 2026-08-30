# Completed sewing source map is phase-framed but not yet controlled

## Question

Does Aspect’s completed-sewing source map provide the stronger pre-channel
object required by the coherent-control no-go?

## Claim boundary

Yes algebraically, on the injective trace range. It defines a phase-framed
linear operator before scalar readout. It does not yet provide a finite typed
matrix, physical unitary dilation, controlled implementation, or route
recombiner.

## Source operator

Let

\[
\tau:\mathcal S(\mathbb A)\longrightarrow\operatorname{Ran}\tau
\]

be the idelic trace restricted to a source domain on which it is injective.
Let \(\mathcal F\) be the source-normalized additive Fourier transform. Then

\[
J_0(\tau\phi)=\tau(\mathcal F\phi)
\]

is independent of the representative \(\phi\). On the trace range,

\[
J_0=\tau\mathcal F\tau^{-1}.
\]

This is an operator-level formula, not a CPTP channel modulo global phase.
The Fourier normalization fixes the operator convention before scalar Mellin
or determinant readout.

## Why injectivity matters

If \(\tau\phi=\tau\psi\), injectivity gives \(\phi=\psi\), hence
\(\tau\mathcal F\phi=\tau\mathcal F\psi\). Without injectivity, descent would
require the weaker but still explicit condition

\[
\mathcal F(\ker\tau)\subseteq\ker\tau.
\]

The current source claim uses injectivity and therefore supplies a well-defined
linear lift on its declared range.

## Gates already passed

The source-map packet establishes:

1. an amplitude-level source domain;
2. a fixed Fourier operator;
3. representative-independent forward and reverse trace maps;
4. authority before scalar Tate or zeta readout;
5. a prohibition against inserting a convenient discrete Fourier matrix.

These are exactly the algebraic ingredients missing from a channel-only
description.

## Gates still missing

The same packet explicitly withholds:

1. a finite typed source basis;
2. trace coordinates for that basis;
3. exact Fourier images in those coordinates;
4. the source Gram metric;
5. a cutoff-compatible graph projection;
6. a physical unitary or isometric realization;
7. coherent control of two bracketed sewing implementations;
8. erasure of implementation and environment route markers;
9. a measured comparison-phase calibration.

The preregistered uncertainty law begins only after a finite complex matrix and
physical variance bounds exist. It cannot construct those inputs.

## Algebraic controlled lift

Once a finite phase-framed operator \(J\) is supplied, the block operator

\[
C_J
=
|0\rangle\langle0|\otimes I
+
|1\rangle\langle1|\otimes J
\]

is algebraically well-defined. This statement still does not prove that the
optical source can implement \(C_J\), preserve coherence, or erase route
markers.

The distinction is:

- source operator: currently derived on an infinite trace range;
- finite controlled matrix: not constructed;
- physical controlled apparatus: not constructed.

## Finite descent witness

The exact checker uses an injective trace matrix \(\tau\) and a Fourier-swap
operator \(F\). It constructs the unique induced map \(J\) on
\(\operatorname{Ran}\tau\) and verifies \(J\tau=\tau F\).

A noninjective hostile trace has a kernel not preserved by \(F\), so two source
representatives with the same trace produce different transformed traces.
The induced operator then does not exist.

## DPC verdict

Current type: source-derived phase-framed infinite-range sewing operator.

Withheld types:

- finite completed sewing matrix;
- controlled sewing constructor;
- physical associator interferometer.

The coherent-control programme is not blocked by phase quotient at the
algebraic source. It is blocked by finite realization and physical compilation.

## Disposition

The strongest next optical task is to instantiate a finite source basis and
Gram metric for \(J_0\), then determine whether its two bracketed
implementations admit one coherent controlled dilation. More classical channel
tomography cannot cross this boundary.

## Verification

The checker check_injective_trace_phase_framed_lift.py verifies exact
representative-independent descent for an injective trace, failure for a
noninjective non-invariant kernel, and distinct operator lifts for opposite
phase representatives despite equality after channel quotient.

Source artifacts audited:

- research/aspect/completed-sewing-source-map-and-threshold-boundary.md
- research/aspect/contracts/completed-sewing-source-map.v1.json
- research/aspect/contracts/completed-sewing-uncertainty.v1.json
- research/aspect/results/completed_sewing_uncertainty_compiler.json
