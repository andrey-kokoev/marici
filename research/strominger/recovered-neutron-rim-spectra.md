# New prior clue: source-bound two-rim frequency response

## What was found

`research/voevodsky/deuterium-two-rim-response.md` already contains exact dynamic responses of the neutron's two actual rim traces, not merely their static matching cost. This is a more specific spectral lead than assigning a fresh two-state register gap.

The hydrogen/joint-readout notes were also checked. Their invariant-mass and recoil maps retain radiation correctly, but constituent masses and binding energies are supplied. They do not calibrate the neutron source energy.

## Fresh operator and normalization comparison

The prior two-rim response was compared to the current 24-dimensional neutron/bank operator packet. The initial unscaled comparison failed. Reading the live `check_collective_carrier_spectrum.py` explained the discrepancy: it explicitly divides the native lift by four.

Exact reconstruction now verifies

    H_rim = H_native/4 + sum_e P_e

on the retained C3-aligned native sector. Equivalently, the unscaled native lift H_native+4 sum P_e is four times this historical operator. This is a recorded prior convention, not a selected physical energy scale. It must not be silently identified with the canonical pulse-angle or occupied-register unit.

## Visible spectra, with dark-mode cancellation checked

The lower/upper equal-rim channel accesses a three-dimensional even block, but its particular port observes only two poles:

    0 and 4485/3292.

The third eigenvalue 5391/3292 cancels exactly between response numerator and denominator. The reduced response is

    R_even(z)=(-z+2099/3292)/[z(z-4485/3292)],
    R(z)=<v,(H-zI)^-1 v>.

The opposite-rim port observes all three odd-block poles. Their exact characteristic polynomial is

    z³-4z²+(44361887/10837264)z-6431463/10837264.

Disjoint rational sign-changing intervals of width below 10^-18 certify all three roots, approximately

    0.17293863105936236,
    1.4339597807127251,
    2.3931015882279123.

Exact Krylov ranks are two and three respectively. Thus the odd-channel response cannot be reproduced as a closed two-dimensional linear response merely by choosing two convenient levels. No eliminated response memory was discarded in the original construction.

## A direct link to the current canonical binding

The even response's zero-mode spectral weight is

    w0=2099/4485.

This equals the total six-rim weight of the actual coherent neutron in our existing retained-record binding. In particular,

    w0/12 = 2099/53820,

reproducing the previously calculated single addressed pulse expectation. This connects the earlier response calculation to our present coefficients without choosing a coupling or fitting a mass.

The static joint rim stiffness is also retained:

    c=1499960093/591106225,
    E_boundary=c*|lower-upper|².

It is a positive compatibility penalty, not an attractive binding offset or vacuum-subtracted neutron rest mass.

## Why this is useful

The source already supplies a concrete multi-pole response at physically motivated geometric attachment ports. A future register/field adapter should match that response, its metric and retained residual—not replace it with an arbitrary two-level spectrum or identify even/odd parity with vacuum/occupied sectors.

The useful next comparison is between these full port responses and an existing source interaction's inactive/matched response. Physical time/action calibration remains separate; the recovered factor-of-four convention makes this separation particularly explicit.

## Verification

```sh
python research/strominger/checkers/check_recovered_neutron_rim_spectra.py
```

Five checks passed. Exact reduced polynomials, rational root brackets, normalization control and source hashes:

`research/strominger/results/recovered-neutron-rim-spectra.json`.

No prior checker or shared result store was overwritten.
