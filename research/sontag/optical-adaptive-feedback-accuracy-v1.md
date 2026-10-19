# Adaptive optical feedback and an explicit accuracy test

## Fresh extension

The earlier same-source fixture used predeclared rational gains. This checker now selects gain from public Gamma-posterior information after a tap. Two count transcripts, (0,0) and (2,0), give different controls for the SAME requested conditional mean occupation h=1/2. Hidden preparation values are used only by the two independent realizations to test their state/resource square, never by the policy. Changing the supplied hidden-state field without changing the public posterior leaves the decision unchanged.

Both histories reuse the statistical successor's coherent preparation, fresh vacuum environments, eta=4/5, tau=1/4 and priors Gamma(2,1), Gamma(3,2) in shape/rate notation. Their original actual occupations are (3,5), retained with different phases. Counts are test transcripts, not measurements.

## Accuracy is a separate success criterion

The source target law makes the conditional mean h. Let posterior initial shapes be K1,K2 and current post-control mean contributions be m1,m2. Scaling does not change each Gamma component's coefficient of variation, so preparation-mean variance is

`v=m1²/K1+m2²/K2 >= (m1+m2)²/(K1+K2)`.

The checker verifies the exact nonnegative difference identity

`v−(m1+m2)²/(K1+K2)=(K2*m1−K1*m2)²/[K1*K2*(K1+K2)]`.

For a Chebyshev certificate at relative error epsilon_rel and failure bound delta, one needs `v/h² <= delta*epsilon_rel²`. Thus a NECESSARY condition for this particular certificate is `K1+K2 >= 1/(delta*epsilon_rel²)`. This is not a necessity theorem for the actual tail probability or every possible confidence method.

Freeze epsilon_rel=1/4 and delta=1/20. The shape sum would need at least 320 for that sufficient-certificate strategy; the two contexts have sums 5 and 7. Both fail the requested certificate. Hitting the mean is therefore not reported as precise regulation. Attenuating more cannot automatically cure relative preparation uncertainty.

A final photon-number observation has additional shot noise: with an ideal conditional Poisson final count of mean H, the unconditional variance is E[H]+Var(H), not Var(H) alone. This apparatus observation must not be conflated with uncertainty in the coherent mean. Detector efficiency and calibration add further requirements.

## Verification

`uv run --with sympy python research/sontag/checkers/optical_adaptive_feedback_accuracy_v1.py`

18 adaptive checks pass across two transcripts, including comparison at both prefixes, public-information decisions, conditional-mean targeting and rejection of the stringent accuracy certificate. Adaptive amplitude replay uses numerical gain evaluation and tolerance 1e-12; the variance-floor identity is symbolic. The 18-check rational-prefix dependency is also rerun. An import-control issue initially exited after that dependency; corrected its SystemExit to run only at the command-line entrypoint, then verified the adaptive receipt exists and passes.

Result: `results/optical-adaptive-feedback-accuracy-v1.json`.

Constructed: conditional observation-based feedback composition for the ideal physical successor. Rejected: interpreting mean-target equality as a certified 25%-relative-error, 95%-confidence result in these supplied posterior contexts. Not rejected or asserted: the actual tail probability. Next design work is an explicit confidence policy with preparation/calibration constraints, not replacing the statistical model with exact readings.
