# Quarter cross limit prefers pure inverse-power corrections

## Problem

The rational candidate failed a cubic inverse-power fit, but logarithmic corrections could have caused that disposition.

## Bold conjecture

The scaled cross ratio admits a pure inverse-power expansion through the tested range, without a leading \((\log n)/n\) correction.

## Named rivals

The principal rival is an equal-parameter model containing \((\log n)/n\); further rivals are slower corrections and overfitting by the cubic power model.

## Risky consequences

On rolling forward holdouts, the four-parameter cubic inverse-power model must predict unseen degrees more accurately and stabilize its fitted limit more strongly than the four-parameter logarithmic model.

## Strongest falsification attempt

Models were trained through degrees twenty-four, twenty-eight, and thirty-two, then tested on the next four exact degrees. Aggregate holdout RMSE is \(1.07\times10^{-7}\) for cubic powers and \(1.83\times10^{-6}\) for the logarithmic rival. The fitted power-model limit varies by \(7.05\times10^{-7}\), versus \(3.09\times10^{-5}\) for the logarithmic model. All six gates passed.

## Disposition

Reject the tested leading-log correction model on these holdouts. Retain the cubic inverse-power model as the finite winner, with \(\theta_2\) near \(0.216703\)–\(0.216704\), but recognize no exact replacement constant. The next leaf is `quarter-cross-limit-power-model-stabilization`: enlarge degree and correction order to test whether this interval persists.

## Claim boundary

Rolling holdout superiority is not an asymptotic theorem and does not exclude logarithms at higher order. The fitted interval is model-dependent and has no exact-status promotion.
