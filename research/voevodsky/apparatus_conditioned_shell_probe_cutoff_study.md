# Apparatus-conditioned shell-probe cutoff study

## Question

At what finite arithmetic cutoff does the shell-generating family cease to have a usable response margin for the conducted-RF apparatus, even when exact algebraic injectivity survives?

## Claim boundary

The study computes exact finite-field ranks and Euclidean singular margins for declared finite graphs. Before measured KrakenSDR calibration and noise bounds are supplied, it does not certify an apparatus cutoff. Numerical singular values depend on the declared Euclidean edge and vertex coordinates; they are not canonical physical metrics.

## Finite graphs

At cutoff \(L\), consecutive primes \(p_j<q_j\) contribute edges

\[
kp_j\longrightarrow kq_j
\]

when \(kp_jq_j\leq L\). Let \(\partial_L\) be the incidence matrix and let \(F_L\) be an orthonormal numerical basis of its cycle kernel in the declared edge-coordinate norm.

Study

\[
L\in\{70,120,240,480,522,525,960\}
\]

using

\[
(t_0,t_1,t_2,t_3)=
\left(\frac56,\frac34,\frac7{10},\frac23\right).
\]

## Exact and numerical tests

For each cumulative family of the first \(m\) settings, exact injectivity on the cycle sector is equivalent to full column rank of

\[
\begin{pmatrix}
\partial_L\\
\partial_LD_{t_0}\\
\vdots\\
\partial_LD_{t_{m-1}}
\end{pmatrix}.
\]

Compute this rank over two large prime fields, representing each rational \(t_n\) exactly modulo the prime. Matching full ranks provide finite exact evidence, not a characteristic-zero proof by themselves.

For apparatus conditioning, compute

\[
R_{L,m}=
\begin{pmatrix}
\partial_LD_{t_0}F_L\\
\vdots\\
\partial_LD_{t_{m-1}}F_L
\end{pmatrix}
\]

and report its smallest and largest singular values and condition number. A measured apparatus error bound \(\eta_{L,m}\) certifies this coordinate model only when

\[
\sigma_{\min}(R_{L,m})>\eta_{L,m}.
\]

## Dynamic-range diagnostic

For every setting report the smallest programmed shell factor

\[
t_n^{j_{\max}(L)}
\]

and its amplitude decibels. This is a source dynamic-range requirement, not the complete response margin: incidence cancellation and correlated noise can produce a smaller singular margin.

## Risky consequences

- A setting count that is algebraically deficient must have zero numerical singular margin on the full cycle sector.
- Once exact full rank is reached, the numerical margin must be positive above the stated floating-point tolerance.
- Stacking an additional setting cannot decrease the smallest singular value in exact Euclidean arithmetic.
- Increasing cutoff may reduce usable margin even when exact rank remains full.
- No apparatus cutoff may be reported until measured transfer, calibration, and joint-noise errors are compared with the computed margin in the same normalized coordinates.

## Strongest falsification attempt

The hostile asks whether the first scalar setting already detects every cycle at small cutoff and then silently extrapolates that observation. The study must include cutoff 960, where a single shell-index code is already known to have a counterkernel, and must show the first cumulative setting count that restores exact rank. A numerical routine that reports a positive margin while modular rank remains deficient is rejected as a tolerance defect.

## Computed result

The two modular ranks agree and all 63 protocol checks pass.

| cutoff | edges | cycle dimension | shells | first full setting count | four-setting smallest singular value | condition number |
|---:|---:|---:|---:|---:|---:|---:|
| 70 | 17 | 1 | 3 | 1 | 0.384616 | 1.000 |
| 120 | 32 | 3 | 4 | 1 | 0.343652 | 1.926 |
| 240 | 67 | 9 | 6 | 1 | 0.246307 | 3.563 |
| 480 | 138 | 20 | 8 | 1 | 0.133205 | 7.872 |
| 522 | 148 | 21 | 8 | 1 | 0.133199 | 7.872 |
| 525 | 150 | 22 | 8 | 2 | 0.013980 | 75.006 |
| 960 | 279 | 45 | 10 | 2 | 0.013965 | 84.756 |

The first single-setting defect occurs exactly at cutoff 525, rather than 960. The transition from 522 to 525 adds the two edges

\[
105\longrightarrow175
\quad\text{in shell }2,
\qquad
75\longrightarrow105
\quad\text{in shell }3.
\]

Edge count rises from 148 to 150, vertex count from 165 to 166, and cycle dimension from 21 to 22. The one-setting response rank remains 21. Thus the newly admitted cycle direction is exactly the first direction invisible to that probe. Two settings restore exact full rank with smallest singular value 0.006018; four raise it to 0.013980.

At cutoff 960, four settings give a Euclidean margin 0.013965 and condition number about 84.8. The weakest programmed factor at \(t=2/3\) and shell 10 is about \(-35.2\) dB. Thus the immediate obstruction is cancellation conditioning, not the much larger shell counts conjectured before the full finite graph was enumerated.

## Acceptance and disposition

The checker passes when the two exact modular ranks agree at every cutoff and setting count, numerical zero versus positivity agrees with exact deficiency versus full rank, and cumulative singular margins are monotone up to declared rounding tolerance. The physical finite ceiling remains pending until calibrated KrakenSDR error and noise operators are inserted. In the declared coordinate normalization, cutoff 960 requires total response-operator error below 0.013965 for the four-setting certificate.
