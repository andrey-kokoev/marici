# Poisson monitor-port rank restoration

Author: `marici.Aspect`

Date: 2026-08-26

Status: exact optical realization of WP571

## Instrument

Split one optical preparation into two typed selected channels, such as two
frequency bins, and count photons in each. A tapped monitor photodiode records
the incident exposure. At the nominal point take the selected Poisson means

\[
\mu_1=1+\theta_1,
\qquad
\mu_2=1+\theta_2.
\]

The joint count Fisher matrix is identity. Conditional normalization of the
two selected bins retains only their differential shape direction, with

\[
G_{\rm shape}=\frac12
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

The missing common direction is the total photon rate relative to the monitor
port.

## Exposure nuisance

Let a common fractional exposure perturbation have independent monitor
precision \(\pi\). Profiling it gives

\[
G_{\rm profiled}
=I-\frac1{2+\pi}
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

with differential and common eigenvalues

\[
1,
\qquad
\frac{\pi}{2+\pi}.
\]

For a disconnected or uncalibrated monitor, \(\pi=0\), rank falls to one.
At the finite hostile calibration \(\pi=2\), the eigenvalues are \(1\) and
\(1/2\): the rate direction is restored without pretending the reference is
noiseless.

## Optical contract

The exposure monitor must share the preparation epoch and must be calibrated
against detector gain, tapping ratio, dead time, and loss. Merely logging a
laser set point does not create the reference. The two selected counts and
monitor record must remain one joint witness; cross-run splicing can manufacture
rank from unrelated intensity drift. The full likelihood must retain monitor
correlations before profiling.

The monitor changes the physical experiment. It identifies the realized
common rate but cannot select the source parameters that produced it. This is
the optical counterpart of WP571's separator-versus-selector boundary.

## Smallest hostile

Keep both selected counters and every normalized spectral statistic fixed,
but delete the monitor precision or profile the exposure freely. The
differential eigenvalue remains one while the common eigenvalue becomes zero.
Any analysis claiming rank two after that projection has imported external
normalization authority.

## Reproduction

Run:

    python research/aspect/checkers/poisson_monitor_port_rank_restoration.py

