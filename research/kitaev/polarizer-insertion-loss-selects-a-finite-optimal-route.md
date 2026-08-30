# Polarizer insertion loss selects a finite optimal route

## Bounded question

Does the ideal crossed-polarizer refinement remain beneficial when every
inserted polarizer carries a fixed intensity survival factor?

The answer is no. Equal angular spacing remains optimal at each fixed chain
length, but any fixed insertion survival \(0<\eta<1\) destroys the infinite
refinement limit and selects a finite optimal number of steps.

## Frozen lossy model

Retain the ideal real Jones projectors and monotone shortest rotation from
horizontal to vertical. Let \(q\ge2\) be the number of angular transitions, so
there are \(q-1\) inserted intermediate polarizers. Normalize intensity after
the first preparation polarizer and treat the final analyzer as ideal.

Each inserted polarizer multiplies transmitted intensity by the same
angle-independent survival factor

\[
0<\eta\le1.
\]

This is an insertion-loss model, not a finite-extinction or depolarizing model.

## Fixed-length optimum

For increments

\[
\Delta_j\ge0,
\qquad
\sum_{j=0}^{q-1}\Delta_j=\frac{\pi}{2},
\]

the transmitted fraction is

\[
T(\Delta_0,\ldots,\Delta_{q-1};\eta)
=
\eta^{q-1}
\prod_{j=0}^{q-1}\cos^2\Delta_j.
\]

Since the loss factor is independent of the angles, strict concavity of
\(\log\cos x\) gives the same unique fixed-\(q\) optimizer as in the ideal
packet:

\[
\Delta_0=\cdots=\Delta_{q-1}=\frac{\pi}{2q}.
\]

The optimized transmission is therefore

\[
T_q(\eta)
=
\eta^{q-1}F_q,
\qquad
F_q=
\cos^{2q}\left(\frac{\pi}{2q}\right).
\]

Loss does not change the best geometry at fixed resource count. It changes the
best resource count.

## Finite-optimum theorem

For \(0<\eta<1\),

\[
T_q(\eta)\longrightarrow0
\]

as \(q\to\infty\), because \(F_q\to1\) while \(\eta^{q-1}\to0\).

Hence the operational optimum occurs at a finite \(q\). The ideal Zeno limit is
not robust to a fixed multiplicative loss per insertion.

## Exact adjacent-step criterion

Adding one further intermediate step is beneficial exactly when

\[
T_{q+1}(\eta)>T_q(\eta),
\]

or equivalently

\[
\eta>\eta_q,
\qquad
\eta_q=\frac{F_q}{F_{q+1}}.
\]

The first threshold is exact:

\[
F_2=\frac14,
\qquad
F_3=\frac{27}{64},
\qquad
\eta_2=\frac{16}{27}.
\]

Thus replacing one middle polarizer by two equally spaced middle polarizers
improves total transmission only when

\[
\eta>\frac{16}{27}.
\]

## Unimodality

Extend

\[
g(q)=\log F_q
=
2q\log\cos\left(\frac{\pi}{2q}\right)
\]

to real \(q>1\). Put \(x=\pi/(2q)\). Direct differentiation gives

\[
g''(q)
=
-\frac{2x^2\sec^2x}{q}
<0.
\]

Therefore \(g\) is strictly concave, and the increments

\[
g(q+1)-g(q)
\]

strictly decrease to zero. Consequently

\[
\frac{T_{q+1}(\eta)}{T_q(\eta)}
=
\eta\exp\bigl(g(q+1)-g(q)\bigr)
\]

strictly decreases to \(\eta<1\).

The sequence \(T_q(\eta)\) is therefore unimodal. There is one maximizing
integer \(q\), except at an exact threshold \(\eta=\eta_q\), where the adjacent
values \(q\) and \(q+1\) tie.

Equivalently, define

\[
q_*(\eta)
=
\min\left\{q\ge2:
\eta\frac{F_{q+1}}{F_q}\le1\right\}.
\]

Away from threshold equality, \(q_*(\eta)\) is the unique optimal number of
angular transitions.

## High-survival asymptotics

Let

\[
\lambda=-\log\eta.
\]

For large \(q\),

\[
g(q)
=
-\frac{\pi^2}{4q}
+O(q^{-3}).
\]

The continuous approximation to

\[
\log T_q
=(q-1)\log\eta+g(q)
\]

is stationary near

\[
q_{\mathrm{cont}}
\sim
\frac{\pi}{2\sqrt{\lambda}}
\]

as \(\eta\uparrow1\). Thus the optimal route length diverges only when
per-insertion survival approaches one.

This is an asymptotic guide, not a replacement for the exact adjacent-threshold
criterion.

## Information-versus-survival distinction

Every added polarizer can refine the ordered route and create a new intervention
context. Yet it also consumes optical survival. More contexts do not monotonically
improve executable performance.

The two quantities are:

\[
F_q
\]

for ideal geometric route quality, and

\[
\eta^{q-1}
\]

for implementation survival. Their product, not either factor alone, determines
the executable optimum.

This is the optical instance of a general compiler boundary: algebraic
factorization can improve while physical realization degrades.

## Obstruction-tower interpretation

At every fixed \(q\), the equal-step chain is algebraically well typed and has a
nonzero exact transmission. The failure occurs only along the refinement family:

\[
F_q\to1,
\qquad
T_q(\eta)\to0.
\]

This is an executable Gate 4 collapse. Finite algebraic route quality does not
supply a uniform physical lower bound through completion.

The normalized hidden sequence is the increasingly fine equal-step chain. Its
ideal record approaches perfect transmission while its lossy physical record
vanishes.

## Hostile variations still open

1. Angle-dependent survival \(\eta(\theta)\) can move the fixed-length angular
   optimizer away from equal spacing.
2. Full-rank diattenuators replace exact adjacent projection by partial
   extinction and create a nonzero crossed baseline.
3. Depolarizing channels may remove any single Jones-word realization.
4. Coherent reflections can make the scalar product law incomplete.
5. Detector noise can select a different optimum from raw transmitted power.
6. If inserted elements are active or adaptive, their control cost needs a
   separate resource model.

## Exact falsifiers

- A fixed-\(q\), angle-independent-loss model whose optimum is not equally
  spaced falsifies the fixed-length theorem.
- A value \(\eta<1\) for which \(T_q(\eta)\) remains bounded away from zero as
  \(q\to\infty\) falsifies the finite-optimum theorem.
- Two separated local maxima in \(q\) falsify unimodality.
- Improvement from \(q\) to \(q+1\) when \(\eta<\eta_q\) falsifies the adjacent
  threshold.
- Treating \(F_q\to1\) as a physical transmission theorem in the presence of
  fixed insertion loss violates the coefficient and implementation typing.

## Claim boundary

This is an exact theorem for a frozen multiplicative insertion-loss model. It
does not claim that laboratory polarizers share one angle-independent survival
factor. Aspect must derive or measure the appropriate optical efficiencies,
finite extinction, coherence, and detector model before applying the numerical
thresholds.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
9/10. The frozen alternatives were monotone operational improvement versus a
finite loss-selected optimum.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
9.5/10. Equal spacing survives at fixed length, but every fixed \(\eta<1\)
forces a unique finite optimum up to threshold ties. The ideal refinement limit
and executable refinement limit have opposite asymptotics.
