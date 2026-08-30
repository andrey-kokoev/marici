# Source Tightness Upgrades Core Convergence to Uniform Closure

Let (P_M) be a source-authorized increasing family of finite-core projections
on a Hilbert state space. Suppose (T_N\) and (T) satisfy:

\[
\lim_{M\to\infty}\sup_N\|T_N(I-P_M)\|=0,
\]

\[
\lim_{M\to\infty}\|T(I-P_M)\|=0,
\]

and, for every fixed (M),

\[
\|(T_N-T)P_M\|\to0.
\]

Then (T_N\to T) in operator norm. Indeed,

\[
\|T_N-T\|
\le
\|(T_N-T)P_M\|
+\|T_N(I-P_M)\|
+\|T(I-P_M)\|.
\]

Choose the core large enough to control both tails, then the cutoff large
enough to control the finite core.

This is the precise positive theorem excluding moving normalized escape states.
The projections (P_M) and their tail estimates must come from the source
topology; choosing a core that discards an authorized seam or arithmetic port
is not admissible.

## Passing fixture

Let

\[
D=\operatorname{diag}(1,1/2,1/3,\ldots)
\]

and (T_N=P_NDP_N). For (N\ge M), the finite core is exact, while

\[
\sup_{N\ge M}\|T_N(I-P_M)\|
\le\frac1{M+1},
\qquad
\|D(I-P_M)\|=\frac1{M+1}.
\]

Moreover (\|T_N-D\|=1/(N+1)\), so uniform closure holds.

## Hostile fixture

For moving tail projections (E_N=|e_N\rangle\langle e_N|), every fixed core
eventually sees zero, but

\[
\sup_N\|E_N(I-P_M)\|=1
\]

for every (M). The theorem rejects them exactly at source tightness.

## RH-facing interpretation

To exclude normalized theta/Tate escape states, Grothendieck may establish:

1. a finite source core containing the required primitive, square, seam, and
   archimedean coordinates;
2. uniform smallness of the complementary tail in the full constructor Gram
   norm;
3. exact or norm convergence on each core;
4. preservation of these estimates under Fourier–Tate and real-frame
   transport.

This produces operator-norm closure, after which uniform lower frame bounds can
be transferred by standard perturbation estimates.

## Falsifiers

- Tail norms remain order one outside every fixed core.
- The core omits an authorized discrete or seam coordinate.
- Tightness holds only for each fixed state, not uniformly over normalized
  states.
- Core convergence is scalar rather than operator-norm convergence.
- The limiting operator has an uncontrolled tail.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Core error, approximant tail, limit tail, and global norm were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. A source-tightness theorem supplied the exact positive upgrade from
finite-core convergence to operator-norm closure. The moving projection hostile
failed at one explicit tail supremum.
