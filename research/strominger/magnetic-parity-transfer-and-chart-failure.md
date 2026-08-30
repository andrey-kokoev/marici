# Uniform parity characters meet their first chart failure

Companion to checkers/magnetic_parity_transfer_checks.py (9/9, exit 0) and
results/magnetic_parity_transfer.json.

For every tested stable component through \(q=11\), with \(a=2k\), nested
determinant ratios obey two parity formulas:

\[
q\text{ even}:\quad
R_{g,q}(a)=
qg(g+3)a^{\overline g}a^{\overline{g-1}}(a+g+q-1),
\]

\[
q\text{ odd}:\quad
R_{g,q}(a)=
-\left(a^{\overline g}\right)^2
(a+g-q-1)(a+g+q-1).
\]

The checker verifies 552 exact stable ratios over \(2\le g\le8\), \(2\le
q\le11\). The displayed stable factors never vanish. The odd singular
equation

\[
a+g=q+1
\]

detects the known \((g,q,a)=(2,7,6)\) birth exactly.

## First scalar-chart failure

The one-chart global conjecture is false. At

\[
\boxed{(g,q,k)=(2,12,5)}
\]

the deterministic nested Hall minor has determinant zero. But the full
component matrix has column rank 12, and an alternate maximal minor has
determinant

\[
-195441246545970423398400000000\ne0.
\]

Therefore this event is not a kernel class and not failed transport. It is a
coordinate-chart singularity: one chosen determinant vanishes while the
underlying linear map remains injective.

This forces a refinement:

\[
\text{global transfer proof}
\ne
\text{one scalar minor for all parameters}.
\]

The correct object must be a finite atlas of overlapping maximal minors, or
an invariant-factor/exterior-power state that does not depend on one chart.
Chart transitions must be proved nonzero where the active minor changes.

The parity formulas remain exact and informative through \(q=11\), but they
cannot be extrapolated as a single global coordinate theorem. The next target
is to construct the first q=12 chart transition and show that the alternate
minor resumes nonsingular transport.

