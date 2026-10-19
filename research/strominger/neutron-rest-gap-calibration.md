# Neutron rest energy, iteration 4: exact calibration nonuniqueness

## Outcome

The current source packet does not determine a unique neutron rest energy. This is now certified even after matching the occupied register's relative frequency to the source's unit pulse frequency. Continuing to choose parameters would select another model, not calculate a source-selected mass.

The earlier 21/4 remains a valid conditional result at its explicitly supplied parameters, not a physical neutron rest-energy prediction.

## Stronger test than changing the overall energy unit

Read and validate the current charge-completed gap receipt and canonical source-energy receipt. Reuse the prior exact two-level spectral checker. Keep fixed:

- all neutron/source/bank operators and their metric;
- the conserved occupied-sector assignment;
- all 21 native seam controls;
- g=2/5 and kappa=2;
- the occupied register gap r_b=1;
- the entire matched-register ground projector, whose occupation is 4/5.

Choose J=epsilon+3/5. Then

    r_b²=(J-epsilon)²+4g²=1

for the whole family, while

    r_v=sqrt((2epsilon+3/5)²+16/25),
    E_gap=(21/2)(r_v-1).

Two exact admissible cases are:

| epsilon | J | r_b | r_v | Rest gap |
|---:|---:|---:|---:|---:|
| 9/20 | 21/20 | 1 | 17/10 | 147/20 |
| 51/40 | 15/8 | 1 | 13/4 | 189/8 |

Both have positive mixing, the same occupied relative dynamics and ground projector, and the same source energy unit. Nevertheless their vacuum-subtracted gaps differ. The difference is not merely a global unit conversion.

The supplied rest Hamiltonian's scalar occupied phase and inactive-register response do change. Neither was fixed by identifying the separate canonical source pulses with neutron modes. This test does not claim those completed Hamiltonians are operationally identical.

## Why identifying both register gaps with one pulse frequency fails

The exact identity is

    r_v²-r_b²=4epsilon J>0.

Thus both conditioned register gaps cannot equal the same unit source pulse frequency in the positive-gap domain. This excludes that literal calibration, not arbitrary future source-derived register constructions.

## What input would finish the physical calculation

A source operation must identify the inactive and matched neutral-register spectra, including scalar/reference terms. A physical energy/time normalization and occupied-sector bare baseline are also needed. The recovered angular-clock construction explicitly does not supply physical seconds.

The gap is calculable once these inputs are supplied. They cannot be inferred from the present mode/pulse/metric/charge data alone: the two exact completions above agree with those data and yield different answers.

## Verification

```sh
python research/strominger/checkers/check_neutron_rest_gap_calibration.py
```

Six checks passed. Full exact projectors, spectral values, parameter family and hashes:

`research/strominger/results/neutron-rest-gap-calibration.json`.

This closes the attempted source-only rest-energy calculation with an explicit nonuniqueness certificate. It does not close research into additional source operations or establish a no-go theorem for all possible models.
