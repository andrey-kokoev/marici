# Two-background mediator actuator: WP1001

## Question

What is the smallest explicit source extension that internalizes WP1000's two
parameter directions as operations on one common mediator substrate?

## Candidate source extension

Retain the WP977 fields (X,Y,A,s). Add two canonically normalized singlet
background carriers (phi_A,phi_s) with independently addressable relational
ports (epsilon_A,epsilon_s), and source terms

\[
\frac12(a_0+\kappa_A\epsilon_A)\operatorname{tr}A^2,
\qquad
\frac12(c_0+\kappa_s\epsilon_s)s^2.
\]

Equivalently, a microscopic realization may use cubic interactions
(phi_A\operatorname{tr}A^2) and (phi_s s^2), with the displayed epsilons
denoting calibrated background displacements. These interactions are
renormalizable in four dimensions. The two singlets are weak-basis scalars, so
the construction descends at the action level.

This is a declared candidate extension, not an assertion that the backgrounds
have been experimentally realized.

## Exact actuator response

At the reference setting, let (a=a_0>0), (c=c_0>0). The leading WP977
matching gives

\[
q=\frac{\mu^2}{2a},
\qquad
k=\frac{\gamma^2\mu^6}{2ca^6}.
\]

The logarithmic response to the two ports is

\[
J_\epsilon=
\frac{\partial(\log q,\log k)}{
{\partial(\epsilon_A,\epsilon_s)}}
=\begin{pmatrix}
-\kappa_A/a&0\\
-6\kappa_A/a&-\kappa_s/c
\end{pmatrix},
\]

with determinant

\[
\det J_\epsilon=\frac{\kappa_A\kappa_s}{ac}.
\]

It has rank two exactly when both port couplings are nonzero. Deleting either
coupling removes its column and restores a rank-one actuator. Sending either
background stiffness to infinity at fixed applied source suppresses that port,
providing the decoupling test.

## Operation versus selection

This source extension creates an executable operation schema in the action:
two labelled inputs generate two independent coefficient responses on one
substrate. Its positive local image is open, so it selects no preferred
((q,k)). It is an actuator, not a selector or presentation rigidifier.

The backgrounds also define a new relational experiment. Their displacements
are not absolute mass changes; they are port-relative observables over the
stabilizer of the two reference carriers.

## Instrument gates

An actual physical instrument still requires:

- source potentials fixing the two carrier response ranges and metastability;
- independent preparation and reset of both backgrounds;
- calibrated maps from applied laboratory records to (epsilon_A,epsilon_s);
- finite-width and mixing corrections to the pole masses;
- a common detector likelihood for the two coefficient responses;
- uncertainty support keeping the smallest singular value positive;
- a source-derived work or resource cost.

No existing flavor packet supplies all of these in the WP977 lineage. WP368
supplies the one-port constructor pattern; WP372-WP374 supply conditional scan
algebra, not realized mass control.

## Smallest exact falsifier

Set (kappa_s=0). The determinant vanishes and every operation leaves the
second independent mass port absent. This is the smallest deletion falsifier
of rank-two actuation. Experimentally, any uncertainty completion containing
zero smallest singular value also falsifies the instrument claim.

## Claim boundary

WP1001 constructs a renormalizable, weak-basis-descending candidate actuator
schema and proves its leading response rank. It does not prove global vacuum
stability, finite-threshold accuracy, laboratory addressability, reset,
detector calibration, or selector authority. Composition parameters are not
identified with physical time.

## Disposition

Admit the two-background action as the minimal candidate source extension for
rank-two actuation. Withhold physical-instrument and selector status pending
the listed calibration and stability gates.

