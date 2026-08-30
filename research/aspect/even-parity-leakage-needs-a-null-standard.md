# Even parity leakage defeats reversal without a null standard

## The half-sum can be precisely wrong

Extend the reversal model by an orientation-even link offset `e=1/10`. With
endpoint target `1/3` and odd link bias `1/4`, the two measurements become

```text
forward:  41/60
reverse:  11/60.
```

The half-difference still returns the odd bias `1/4`. The half-sum returns
`13/30`, not the true endpoint `1/3`; it has silently estimated target plus even
link leakage.

Repeated reversal, ABBA ordering, and arbitrarily high precision do not separate
two terms in the same even representation.

## A realizable null adds the missing equation

Create a local configuration whose endpoint offset is known to be zero while
preserving the same transfer link and reversal actuation. Its forward and reverse
records are `7/20` and `-3/20`. Their half-sum identifies the even leakage
`1/10`; their half-difference independently checks the odd bias `1/4`.

Subtracting the null half-sum from the science half-sum recovers the endpoint
`1/3` exactly.

The null must preserve the nuisance mechanism. A convenient zero produced by
bypassing the relevant link would not calibrate its leakage.

## Optical instrument

Co-locate endpoint references or close a short local loop while retaining the
same switches, amplifiers, wavelengths, and direction reversal. Interleave null
and science ABBA blocks. Vary target offset independently to test that the null
term is additive and stable rather than silently assumed so.

## Claim boundary

The checker assumes additive constant even leakage shared by null and science,
constant odd bias, and an exactly known zero endpoint. Null transfer mismatch,
state dependence, temporal drift, and noise remain open.

## Verification

```text
python research/aspect/checkers/check_even_parity_leakage_needs_a_null_standard.py
```
