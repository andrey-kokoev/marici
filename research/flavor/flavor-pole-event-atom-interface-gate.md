# Pole-event atom interface gate: WP1065

## Question

Can WP1052's `physical16` event cell be obtained by relabeling the 23 pole
atoms from WP1053/WP1056?

## Diophantine obstruction

Let \(d\) be the integer number of pole atoms carrying detector provenance.
WP1052's event cell requires equal detector and monitor support and half
cross support:

\[
D=M=d,
\qquad
X=\frac d2.
\]

If every pole atom is used exactly once across the six event roles, the total
atom count would be

\[
D+M-X=d+d-\frac d2=\frac{3d}{2}.
\]

For 23 pole atoms this requires

\[
d=\frac{46}{3},
\]

which is not an integer. Therefore WP1052's event cell is not a relabeling of
the 23 pole atoms.

Equal-weight partition fails independently: six equal integer atom groups
would require \(6\mid23\), but

\[
23\bmod6=5.
\]

## Six-branch hostile

The localized \(SU(6)\) cell also has six branches, with dimensions

\[
(6,8,1,4,2,2).
\]

Assigning these six branches bijectively to the six WP1052 roles gives no
solution satisfying equal detector/monitor support, half cross support, and
half detected monitor support. The numerical match “six branches versus six
atoms” is therefore not an interface law.

## Boundary

A future source may derive a channel-dependent reweighting map. This gate
does not exclude that map. It excludes count-only and equal-weight
identifications. The required physical16 dynamics must derive event weights,
detector/monitor/cross labels, and null outcomes from production/decay
channels.

## Classification

Negative pole-event interface gate. It sharpens the physical16 source
blocker into a required reweighting map rather than a six-atom
identification.

Checker: `research/flavor/checkers/wp1065_pole_event_atom_interface_gate.py`

Result: `results/wp1065_pole_event_atom_interface_gate.json`
