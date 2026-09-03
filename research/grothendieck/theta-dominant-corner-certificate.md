# Exact dominant corner certificate

## Claim

For the dominant residual quotient implemented by the approved cancellation-free
kernel,

`D(3/10,1/28) > 32`.

## Evidence

`research/grothendieck/checkers/theta_dominant_corner_exact.py` uses only
`Fraction` interval arithmetic and the outward elementary enclosures in
`theta_dominant_fraction_interval_core.py`. Its durable result is
`research/grothendieck/results/theta-dominant-corner-exact.json`; the exact
rational endpoints are encoded as hexadecimal numerator/denominator pairs.
The certified lower endpoint is approximately `32.16694268137721`. The same
outward box has upper endpoint below `33`, furnishing a tightened-threshold
failure witness: the checker certifies `D>32` and explicitly does not certify
`D>33`.

The only semantic clamp used by the evaluator is justified in
`research/grothendieck/theta-eta-convexity-lemma.md`: convexity and `m(0)=0`
imply `eta=m(4y)-4m(y)>=0`. The checker intersects only the value enclosure of
`eta` with the proved half-line and retains its propagated derivative
intervals.

Both the interval-core self-test and the corner checker pass independently.
This certificate is a single-corner theorem; it does not certify Chart 1,
Chart 2, or either global derivative sign.
