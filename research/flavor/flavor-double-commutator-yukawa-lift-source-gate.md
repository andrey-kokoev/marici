# Double-commutator Yukawa-lift source gate

Work package: WP930

## Question

Does the declared Spin5 action or its finite-threshold grammar generate the
WP929 double-commutator contraction with a fixed dissipative sign?

## The missing tensor arrow

WP929 defines a conditional flow directly on Hermitian Gram matrices.  A
physical Yukawa beta function must additionally lift that velocity through

\[
H=YY^\dagger,
\qquad
\dot H=\beta_Y Y^\dagger+Y\beta_Y^\dagger.
\]

For a common-left Hermitian lift \(\beta_Y=KY\), the required equation is the
Sylvester problem

\[
KH+HK=\dot H.
\]

On the positive nondegenerate domain this has a unique Hermitian solution.  In
an eigenbasis of \(H\),

\[
K_{ij}=\frac{\dot H_{ij}}{\lambda_i+\lambda_j}.
\]

Thus the Gram operation is mathematically liftable, but its canonical lift is
rational in the spectrum.  It is not obtained by simply multiplying the
double commutator by one half.  The exact two-dimensional hostile verifies
both statements: the Sylvester lift reproduces the target, while the naive
polynomial lift has a nonzero residual and the off-diagonal solution contains
the inverse sum \((x+y)^{-1}\).

## Source-support audit

The declared Spin5 packet contains anomaly completions, scalar gauge beta
coefficients, one-family Yukawa incidence and mass-rank information.  WP919
proved that it contains no three-family Yukawa beta vector at all.  It
therefore cannot determine this rational lift, its coefficient, its sign, or
its normalization.

WP884's threshold grammar is downstream and leaves a two-dimensional matching
fiber.  Threshold data can transport or identify a source-defined coupling;
they cannot supply authority for a UV beta operator absent from the source
action.

## Verdict

The WP929 flow is a valid conditional quotient-level contraction, but the
current Spin5 branch does not generate it.  It is neither an admitted selector
nor a chart rigidifier.  No detector instrument is presently owed, because the
source operation it would instrument has not been constructed.

This closes the declared Spin5 double-commutator branch negative.  Reopening
requires an independently declared three-family action and a derivation of the
lift with fixed sign and normalization.  Detector calibration or finite
threshold fitting cannot substitute for that constructor.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp930_double_commutator_yukawa_lift_source_gate.py
```

The generated result is
`research/flavor/results/wp930_double_commutator_yukawa_lift_source_gate.json`.
