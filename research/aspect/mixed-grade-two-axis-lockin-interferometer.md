# Mixed-grade two-axis lock-in interferometer

Author: `marici.Aspect`

Date: 2026-08-26

Status: exact optical realization of the mixed-Rees hostile

## Two source-derived normals

Use one optical preparation with two independently controlled small
coordinates:

- \(E\), a signed temporal delay or boundary-displacement modulation;
- \(\Delta\), a signed difference between two interferometer branches.

Let a phase-sensitive output quadrature have local form

\[
f(E,\Delta)=a_{00}+a_{10}E+a_{01}\Delta+a_{11}E\Delta.
\]

Pulling back to \(\Delta=0\) erases the mixed coefficient. Specializing to
\(E=0\) does the same. Taking either first derivative after the other
specialization cannot recover \(a_{11}\).

## Four-corner detector

Drive both modulators prospectively through the four settings

\[
(E,\Delta)=(h,k),(h,-k),(-h,k),(-h,-k)
\]

within one phase-calibrated run. Double demodulation gives

\[
\widehat a_{11}=
\frac{f(h,k)-f(h,-k)-f(-h,k)+f(-h,-k)}{4hk}.
\]

For the declared bilinear model this is exact for arbitrary nonzero \(h,k\).
It cancels the offset and both one-axis responses while retaining only the
mixed grade.

The smallest hostile is \(f(E,\Delta)=E\Delta\). Both restricted responses
and both post-restriction first derivatives vanish, but the four-corner
readout returns one.

## Optical implementation contract

A phase-locked balanced heterodyne detector must retain signed quadrature;
intensity-only detection can introduce even-order aliases. Both modulation
clocks, signs, amplitudes, and epochs must be recorded in one joint witness.
The policies must be common across hypotheses and chosen before inspecting
the response. Drift rejection requires interleaved corner ordering or an
independently certified transport between corner frames.

Deleting either modulation clock makes the mixed coefficient unavailable; it
must not be reported as zero. Separate delay and branch scans are therefore
not a substitute for the joint four-corner experiment.

## Boundary

This instrument realizes Nima's mixed-grade theorem and supplies a practical
detector architecture for source-authorized mixed responses. It does not show
that a cosmological, flavor, or theta coefficient occupies the mixed grade.
That assignment requires both normals and their common carrier to be derived
from the relevant source theory before the quotient.

## Reproduction

Run:

    python research/aspect/checkers/mixed_grade_two_axis_lockin_interferometer.py

