# Physical neutron rest energy: authoritative reference versus derivation

## Established physical value

The freshly retrieved NIST **2022 CODATA adjustment** reports

    m_n = 1.67492750056(85) × 10^-27 kg,
    m_n c² = 1.50534976514(76) × 10^-10 J
           = 939.56542194(48) MeV.

Parentheses give standard uncertainty in the last quoted digits. The MeV uncertainty is 0.00000048 MeV, or 0.48 eV. This is an experimentally constrained recommended value, not a result derived from our carrier matrices.

Source: https://physics.nist.gov/cuu/Constants/Table/allascii.txt

The complete table was successfully retrieved over HTTPS. Individual NIST CGI pages returned HTTP 403; no claim is made to have retrieved those pages. The downloaded table is retained at `results/physical-neutron-reference/codata-allascii.txt` with its hash in the audit receipt.

## Fresh numerical verification

Using the exact SI constants c=299792458 m/s and 1 MeV=1.602176634×10^-13 J, the tabulated mass, joule energy and MeV energy agree within their displayed rounding. These entries describe the same constant; their agreement is a conversion check, not three independent measurements.

## What the repository does not yet establish

The completed internal/contact model has a conditional dimensionless gap near 0.185016977411665. Its action, positive channel threshold and physical particle identification remain assumptions. It does not independently predict the measured neutron value.

For illustration only, forcing that model gap to equal the measured neutron energy would require an energy unit near

    epsilon_fit = 5078.26597907 MeV per model unit.

This is obtained by dividing the experimental target by the model number. It is a circular calibration, not a prediction. It has **not** been applied to the model or admitted as physical calibration evidence.

The precise distinction is therefore:

- The physical neutron's positive rest energy is established empirically by the cited adjustment.
- A derivation of that physical value from this repository's model has not been established.

An independent model claim requires a justified physical action and neutron-sector identification plus independent scale information. Repeating the conditional positivity construction or choosing a scale to match the neutron cannot replace those requirements.

## Reproduction

```sh
python research/strominger/checkers/check_physical_neutron_rest_energy.py
```

Four checks passed. Receipt: `research/strominger/results/physical-neutron-rest-energy.json`.
