# Optical three-wing associator is an equality tester, not yet a path interferometer

## Question

Does Aspect’s existing three-wing apparatus instantiate the complete
source-to-record chain required to observe a categorical associator phase?

## Claim boundary

It instantiates a strong equality test between two completed optical
transformations. It does not yet coherently superpose and recombine the two
bracketed constructor paths. Consequently, a global phase multiplying one
entire route remains invisible.

## Existing source chain

The current Aspect programme supplies:

1. a heralded three-wing \(000\)-\(111\) coherent source;
2. direct, left-bracketed, right-bracketed, and destructive routes;
3. ternary parity analysis with all proper phase-sensitive marginals null;
4. crossed logical bracketing and hardware assignment;
5. transfer, delay, triad-phase, reset, history, environment, and detector
   controls;
6. a thirty-four-gate preregistered equality test.

This is enough to test whether the two routes induce the same observable
three-wing transformation under the declared controls.

## Missing constructor

The routes are randomized across trials and their output curves are compared.
There is no coherent control degree of freedom preparing

\[
\frac{1}{\sqrt2}
\left(
|L\rangle\otimes U_L|\psi\rangle
+
|R\rangle\otimes U_R|\psi\rangle
\right)
\]

and no final operation erasing the route implementation while recombining
\(|L\rangle\) and \(|R\rangle\).

Therefore the current instrument observes differences between the induced
route channels, not the relative global phase between route amplitudes.

## Exact blindness

Let

\[
U_R=\omega U_L,
\qquad |\omega|=1.
\]

Every separate-route probability and expectation value is identical:

\[
\langle\psi|U_R^\dagger E U_R|\psi\rangle
=
\langle\psi|U_L^\dagger E U_L|\psi\rangle.
\]

Classically subtracting those records gives zero for every \(\omega\). In
particular, the nontrivial sign associator \(\omega=-1\) is completely hidden.

The quarter-turn hostile in the existing prediction shifts the right ternary
curve relative to its own state/analyzer phase. That is an observable process
phase, not a pure global phase multiplying the complete bracketed route. The
two cases must remain typed separately.

## Coherent upgrade

A categorical associator-phase probe requires:

1. a route-control system prepared coherently;
2. controlled implementation of \(U_L\) and \(U_R\);
3. preservation of the open three-wing carrier in both arms;
4. erasure or matching of every hardware and environment route marker;
5. recombination of the route-control amplitudes;
6. complementary control-port detection before discarding route coherence;
7. a source-matched control tuple calibrating the apparatus comparison phase.

For equal route amplitudes, the control-port probabilities are

\[
p_+=\left|\frac{1+\omega}{2}\right|^2,
\qquad
p_-=\left|\frac{1-\omega}{2}\right|^2.
\]

The sign associator exchanges the bright and dark ports. A quarter-turn phase
gives equal port probabilities.

## Relationship to the current preregistration

The thirty-four existing gates remain valuable and mostly become prerequisites
for the coherent upgrade. They reject route-dependent transfer, triad phase,
memory, reset, environment, and detector alternatives.

They do not construct:

- coherent route control;
- controlled left/right sewing;
- route-marker erasure;
- a common comparison phase for the control ports.

Passing the existing null therefore cannot be promoted to an associator-class
measurement.

## DPC verdict

Current verdict: source-derived completed-channel equality tester.

Withheld verdict: coherent categorical-associator interferometer.

Finite falsifier: replace \(U_R\) by \(-U_L\). Every current separate-route
record remains unchanged, while a coherent route-control interferometer swaps
its complementary ports.

## Disposition

The optical sector is close but stops at one explicit missing constructor:
coherent control and recombination of the two bracketed sewing routes. The next
optics work should design or rule out that constructor rather than add further
classical left/right null gates.

## Verification

The checker check_optical_associator_equality_vs_interference.py verifies exact
separate-route blindness for the phases \(1,-1,i,-i\) and the corresponding
coherent control-port distributions.

Source packets audited:

- research/aspect/three-wing-associator-prediction.md
- research/aspect/three-wing-associator-preregistration.md
- research/aspect/triad-phase-associator-falsifier.md
- research/aspect/transition-balanced-associator-falsifier.md
- research/aspect/reset-insertion-associator-falsifier.md
