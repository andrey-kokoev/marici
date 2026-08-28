# Control codimension sets the recurrence robustness exponent

Owner: `marici.Kitaev`

## Question

If a `k`-parameter executable central control is dense in a
`d`-dimensional phase torus, what quantitative obstruction is imposed by
the missing `d-k` control directions?

## Claim boundary

Assume a regular linear or locally Lipschitz central flow whose parameter ball
of radius `T` has `k`-volume of order `T^k`. The
`\varepsilon`-tube around its image has volume bounded above, up to geometry
constants, by

\[
C T^k\varepsilon^{d-k}.
\]

To cover a compact `d`-torus of fixed positive volume, a uniform
`\varepsilon`-compiler must therefore reach parameter radius

\[
T(\varepsilon)
\ge
c\,\varepsilon^{-(d-k)/k}.
\]

This is a codimension bound, independent of whether arithmetic recurrence
makes the actual covering time still worse.

Suppose generator calibration has adversarial size `\delta`, and phase
sensitivity grows at least linearly with the parameter radius used by the
compiler. Robust accuracy `\varepsilon` then requires, up to metric
constants,

\[
\delta T(\varepsilon)\lesssim\varepsilon.
\]

Combining the bounds yields

\[
\varepsilon
\gtrsim
\delta^{k/d}.
\]

For `k=1,d=2`, this recovers the square-root floor.

The statement is scoped to open-loop approximation by a lower-dimensional
central flow with static coefficient uncertainty. It does not apply unchanged
to feedback, error-corrected composite pulses, discontinuous digital
constructors, or a source extension that supplies new independent directions.
Those mechanisms change either the sensitivity law or the executable
dimension.

For the frozen D(S3) endpoint algebra, the ideal two-flux dynamical Lie
algebra has central rank five while arbitrary coherent sector phases form an
eight-torus. If one attempted to obtain all missing phases by dense recurrence
without adding a control direction, the dimensional lower bound is

\[
T(\varepsilon)
\gtrsim
\varepsilon^{-3/5},
\qquad
\varepsilon_{\rm robust}
\gtrsim
\delta^{5/8}.
\]

This does not obstruct the weaker dephasing task. Dephasing requires only a
central signature separating the eight discrete sector labels, and the
existing audit finds one additional endpoint quadrature sufficient. It also
does not assert that the five-dimensional center is actually dense in the
eight-torus; density would be a further arithmetic condition. The result says
that even if density holds, it carries a codimension-priced robustness floor.

## Disposition

Attach the pair `(k,d)` to every closure-based central-control claim and
report:

1. the target torus dimension `d`;
2. the executable parameter rank `k`;
3. the covering-time law;
4. the calibration-sensitivity law;
5. the resulting robust-error floor.

For D(S3), prefer the task-native repair: add one authorized separating
central constructor for dephasing, or three independent central constructors
for arbitrary phase control. Irrational recurrence is not an equivalent
fault-tolerant substitute.
