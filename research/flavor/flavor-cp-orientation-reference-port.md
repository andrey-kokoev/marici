# CP-orientation reference port

## Scope

WP975 transfers the WP785 orientation-port theorem to the WP974 degree-six
flavor invariant. Let \(j\) denote the sign of the normalized CP-odd trace
word and let \(s\) be a dynamical pseudoscalar reference. On the bounded sign
domain \(s,j\in\{-1,+1\}\), the smallest CP-even relational coupling is

\[
E(s,j)=-g\,s j,\qquad g>0.
\]

CP acts simultaneously as \((s,j)\mapsto(-s,-j)\).

## Exact partition

The coupling selects the relative invariant \(sj=+1\). Its two minima are

\[
(s,j)=(+1,+1),\qquad(-1,-1).
\]

After forgetting the reference, the flavor projection still contains both
\(j=+1\) and \(j=-1\). The original experiment therefore has no absolute CP
selector.

Fixing the reference port to \(s=+1\) leaves the single minimum \(j=+1\).
This is a valid relative observable only in the new experiment whose admitted
groupoid is the stabilizer of the chosen reference. It does not reveal an
absolute sign belonging to the reference-free flavor experiment.

## Classification

The dynamical port is a relational selector and orientation rigidifier. It is
neither an absolute flavor selector nor a physical instrument by itself.
Source authority is still required for the reference preparation, magnitude,
coupling, threshold transport, and calibrated joint readout.

The smallest falsifier is a reference-free energy that distinguishes the two
simultaneous-CP minima. The declared coupling does not do so.

## Reproduction

Run:

    python research/flavor/checkers/wp975_cp_orientation_reference_port.py

The generated result is
research/flavor/results/wp975_cp_orientation_reference_port.json.
