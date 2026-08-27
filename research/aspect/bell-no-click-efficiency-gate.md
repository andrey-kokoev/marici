# Bell no-click efficiency gate

## Question

When does the `2(3+2+1)+1` apparatus turn its relational fringe into a Bell
violation without discarding missing detections?

## Full-outcome law

Retain every herald. Assign every no-click outcome the fixed value `+1` before
measurement settings are revealed. For equal independent efficiency `eta`,
unbiased detected outcomes, and relational coherence `gamma`, double clicks
contribute the ideal correlation, single clicks average to zero, and double
no-clicks contribute one. The observed CHSH value therefore obeys

\[
\frac{S}{2}=\sqrt{2}\,\gamma\eta^2+(1-\eta)^2.
\]

Violation of `S <= 2` is equivalent to

\[
\eta>\frac{2}{1+\sqrt{2}\gamma}.
\]

The executable checker avoids numerical radicals by testing the exact rational
inequality

\[
2\gamma^2\eta^4>(2\eta-\eta^2)^2.
\]

## Consequences

For ideal coherence, efficiency `4/5` fails while `5/6` passes. This brackets
the familiar threshold without postselection.

For the proposed nonlocal regime `gamma = 4/5`, efficiency `9/10` still fails.
Efficiency `19/20` passes. The required threshold is slightly above 0.938.

Thus a visible relational fringe and even an ideal-state prediction above the
Bell threshold do not authorize the experimental Bell claim. The full
herald-normalized instrument must also cross its efficiency threshold.

## Apparatus rule

Freeze the outcome assignment before acquisition. Count no-click and
single-click trials in all four setting cells. Calibrate efficiency from the
same herald stream and epoch. Never infer the Bell statistic from coincidence
normalization.

## Falsification

At `gamma = 4/5` and efficiency `19/20`, failure to exceed the complete-data
Bell bound contradicts the declared quantum apparatus model after analyzer
errors and phase covariance have passed their independent gates. At lower
efficiency the experiment is inconclusive for Bell nonlocality, not negative
evidence against relational coherence.

## Disposition

The Bell module now has a detector-complete admission gate. It separates
source coherence, Bell geometry, and detection efficiency instead of allowing
coincidence postselection to combine them silently.

## Verification

Run:

```text
python research/aspect/checkers/check_bell_no_click_efficiency_gate.py
```
