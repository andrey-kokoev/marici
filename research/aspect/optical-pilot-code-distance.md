# Error-correcting optical pilot incidence

## A pilot decoder needs an authorized radius

Freeze two four-symbol optical pilot words:

```text
alpha = 0000
beta  = 1111.
```

Their Hamming distance is four, so one symbol substitution is uniquely
correctable. The record `0001` lies one step from alpha and three from beta.

The two-error record `0011` is exactly tied. A faithful event table must retain
it as ambiguous. Choosing alpha or beta from context would fit the incidence.

The three-error record `0111` is one step from beta. If it actually originated
as alpha, unrestricted nearest-neighbor decoding returns a confident but false
beta assignment. Code distance authorizes correction only inside the declared
radius; a small decoder residual is not proof of true origin outside it.

## Coding cannot distinguish an exact copy

Suppose a detector afterpulse duplicates the complete alpha pilot. Both records
decode to alpha at distance zero. Error correction verifies transport fidelity
but cannot decide whether two alpha records arose from two source pulses or one
source pulse plus a detector copy.

That distinction still requires an independent source trigger count, detector
memory intervention, or another occurrence-sensitive carrier. A longer code
does not help against perfect copying of the whole codeword.

## Optical implementation and back-action

Pilot symbols can be encoded in weak polarization, wavelength, phase, or
time-bin modulation. The code must be chosen before the science comparison and
tested for source back-action. If different pilot words alter pulse energy,
routing, or detector recovery, the code becomes a condition intervention rather
than a passive event label.

Recommended decoder records are:

- exact;
- corrected within authorized radius;
- ambiguous tie;
- rejected outside the correction contract;
- duplicated exact code requiring occurrence analysis.

## Claim boundary

The checker covers two binary codewords and substitution errors. Erasures,
soft decoding, synchronization loss, larger codebooks, and pilot-dependent
source changes remain open.

## Verification

```text
python research/aspect/checkers/check_optical_pilot_code_distance.py
```
