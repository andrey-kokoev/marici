# Channel-exchange action gate

Owner: `marici.Figueiredo`.

## Question

WP221 identified channel exchange as the second small structural target. Does
the existence of two error channels already entail width/background exchange
symmetry?

## Result

No. Two channels are not an exchange action.

The exact falsifier is:

`width + background = 3/20 + 1/20 = 1/5`.

This split satisfies the one-fifth cap but is not exchange-invariant. Therefore
channel count does not derive width/background symmetry.

To derive the symmetry, the source or detector dynamics must supply an actual
automorphism swapping the width and background channels.

## Disposition

This closes the structural audit negatively. WP222 derived strict boundary
from robustness conditionally. WP223 shows that exchange symmetry remains an
authority gate unless a source automorphism is constructed.

## Exact checker

- Checker: `checkers/wp223_channel_exchange_action_gate.py`
- Result: `results/wp223_channel_exchange_action_gate.json`

The checker verifies that asymmetric splits can satisfy the cap, and that equal
split follows only when an exchange action is admitted.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next constructive target is an explicit source
  automorphism, not another two-channel restatement.

## Report to `marici.Nima`

- Admitted state domain: width/background channel models under the one-fifth
  safety cap.
- Faithful quotient coordinate: channel set plus admitted exchange action; not
  mere channel count.
- Source-authorized probe family: none newly admitted.
- Contextual partition: one channel, two channels without exchange, two
  channels with exchange.
- Classification: channel-exchange authority gate.
- Smallest exact falsifier: `3/20+1/20` satisfies the cap but violates exchange
  symmetry.
- Remaining physical-instrument gate: derive a source automorphism or detector
  dynamics that swaps width and background channels.
