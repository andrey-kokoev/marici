# Triad-phase associator falsifier

## Question

Can matched pairwise mode overlaps still produce a false three-wing associator
residual?

## Exact hostile

Let three photon internal modes have pairwise overlap magnitudes `1/2`. Every
pairwise HOM visibility is then `1/4`. Pairwise calibration sees no difference
between a zero triad phase and a `pi` triad phase.

The three-mode Gram determinant is

\[
\det G=1-3r^2+2r^3\cos\theta.
\]

At `r=1/2`, the two cases give

\[
\operatorname{Re}B=\pm\frac18,
\qquad
\det G=\frac12\text{ or }0.
\]

Both Gram matrices are positive semidefinite and physically admissible. Their
cyclic three-photon contributions are `+1/4` and `-1/4`, differing by `1/2`.

Thus identical pairwise HOM data can coexist with a large difference in the
native ternary interference term.

## Consequence for the associator experiment

Matching left and right single-particle transfer matrices, delays, and all
three pairwise overlap magnitudes does not close the instrumental null. The two
routes may realize different complex Bargmann invariants

\[
B=\langle A|B\rangle\langle B|C\rangle\langle C|A\rangle.
\]

That route-dependent triad phase can imitate a bracketing residual without any
failure of quantum associativity.

## Repair

Calibrate both real and imaginary quadratures of `B` for each bracketing route
inside the science epoch. Perform a three-photon cyclic-permutation scan, not
only three pairwise HOM scans. Require the complex triad invariant to match
between left and right routes before opening the associator channel.

Exchange the internal-mode labels and reverse one controlled overlap phase.
A genuine calibrated associator residual follows the declared bracketing
transformation; a triad-mode hostile follows the Bargmann phase.

## Disposition

The pairwise mode-matching gate was insufficient and is repaired. The native
arity theorem predicted this exact loophole: a ternary observable requires a
ternary calibration standard.

## Verification

Run:

```text
python research/aspect/checkers/check_triad_phase_associator_falsifier.py
```
