# Three-configuration relative-energy probe

Work package: WP991  
Owner: marici.Figueiredo

## Question

Can the two quotient coordinates \((q,k)\) be read from the exact WP978 energy
responses without importing an absolute energy reference?

## Two-state obstruction

Write the source energy on a configuration with invariants \((K,P)\) as

\[
E=c-qK-kP,
\]

where \(c\) is the physically irrelevant additive energy origin. WP978 gives

\[
(K_2,P_2)=(2,0),\qquad
(K_3,P_3)=\left(\frac29,\frac2{27783}\right).
\]

Conditional on a fixed \(c\), the two energy rows have determinant
\(4/27783\) with respect to \((q,k)\). But without an absolute energy
reference, only \(E_3-E_2\) is observable. That is one scalar response and
has rank one. Two-state spectroscopy therefore does not realize WP990.

## Minimal internal reference

Add a commuting source configuration with

\[
(K_0,P_0)=(0,0),\qquad E_0=c.
\]

The three response rows on \((c,q,k)\) are

\[
J=
\begin{pmatrix}
1&0&0\\
1&-2&0\\
1&-2/9&-2/27783
\end{pmatrix},
\qquad
\det J=\frac4{27783}.
\]

Equivalently, the relative records

\[
\Delta_2=E_2-E_0=-2q,
\qquad
\Delta_3=E_3-E_0=-\frac29q-\frac2{27783}k
\]

have rank two and reconstruct

\[
q=-\frac{\Delta_2}{2},\qquad
k=-\frac{27783}{2}
\left(\Delta_3-\frac{\Delta_2}{9}\right).
\]

Three configurations are minimal when the additive energy origin is admitted
as a nuisance coordinate.

## Typing

The commuting baseline is internal to the same field domain. It does not
recover an absolute energy; it defines a relational three-configuration
experiment over the energy-shift quotient. All three \((K,P)\) labels are
weak-basis invariants, so the formal response descends under the full
weak-basis groupoid.

The current source declares an energy functional but no operation that
prepares the commuting, rank-two, and full-rank configurations on command, no
reset protocol, and no calibrated relative-energy instrument. The three
configurations were selected by the analyst as exact witnesses. Algebraic
availability is not executable control.

## Classification and falsifier

This is a minimal formal instrument architecture and a faithful quotient
separator, neither selector nor rigidifier. It requires no external reference
port, but it does require an added relational preparation experiment.

The smallest exact algebraic falsifier is any collapse of the determinant
\(4/27783\) to zero. The physical falsifier is failure to prepare one of the
three configurations independently, or an uncertainty set whose calibrated
relative-response matrix has rank below two.

## Reproduction

Run:

    python research/flavor/checkers/wp991_three_configuration_relative_energy_probe.py

The generated result is
research/flavor/results/wp991_three_configuration_relative_energy_probe.json.
