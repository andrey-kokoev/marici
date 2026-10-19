# Positive neutron energy: iteration 1, exact gap and full-sector control

## What is now established without adding an offset

The existing autonomous contact model has a strictly positive lowest energy in its invariant rim-accessible sector. This is now an **exact rational enclosure**, rather than only a numerical eigenvalue:

    414299230527578287/1729382256910270464
      < E_accessible <
    276199487018385525/1152921504606846976.

Thus E_accessible is approximately 0.23956486709177238 in the existing model energy unit. The interval width is below 10^-18. No baseline, charging coefficient or interaction was added for this proof.

## Exact continuum argument

Retain the prior fixture kappa=ell=1, eta=2 and lead threshold Delta=1/2. The exact five-dimensional bright basis, metric g, core K_b and contacts W_b,T_b come from the current source-bound operator packet.

For E<Delta, eliminate the two decaying half-line fields. Their quadratic form H_lead-E is positive. The remaining weighted Schur operator is

    g F(E),
    F(E)=K_b+[2q/(1+q)]W_b T_b-E I,
    q=sqrt(1/2-E).

The finite contact coefficient includes both diagonal comparisons, not only exchange.

Enclose q by rational lower/upper bounds using integer square roots, and bound the coefficient monotonically. Since

    g W_b T_b=3 T_b^T T_b >=0,

the resulting rational matrices bound the true Schur form in the quadratic-form order.

Exact LDL inertia gives five positive directions at the lower energy endpoint and four positive/one negative at the upper endpoint. The Schur form strictly decreases with E. This certifies the lowest spectral crossing and a positive lower bound for the accessible continuum/core operator. A separate count near the continuum threshold confirms two accessible bound levels.

## Why this is not yet a positive full neutron rest gap

The complete retained model still contains six explicit source-bank vectors with

    K z=0, T z=0.

With zero exterior field these are normalizable **zero-energy states of the full autonomous operator**. They were not deleted when constructing the five-dimensional scattering reduction.

Moreover, each of the eighteen actual source pulse/frame projectors has nonzero matrix elements from the bright space into bank coordinates. Thus the rim-accessible sector is not a superselection sector of the broader admitted source-operation family. Calling its lowest localized level the neutron rest mass would require a physical sector-selection argument not supplied by the bound-state calculation.

This strengthens the result in two distinct directions:

- positive accessible stationary energy is genuinely proved;
- strict positivity of the complete retained particle sector is explicitly not proved and, for the current Hamiltonian, is false.

The result is not repaired by hiding bank modes or renaming the positive level.

## Verification

```sh
python research/strominger/checkers/check_neutron_positive_gap_certificate.py
```

Six checks passed using exact rational arithmetic; no NumPy/SciPy spectrum or decimal residual was used for the certificate. The receipt retains the rational Schur enclosures and source-pulse bank-leakage ranks:

`research/strominger/results/neutron-positive-gap-certificate.json`.

## Remaining obligation

A full positive neutron rest sector needs a justified energy-bearing bank operation or a physically protected sector that excludes the zero states. Any added action must be stated as such and must not be misrepresented as the unchanged ordered-pulse dynamics. Physical energy normalization remains a separate input even after positivity is established in model units.
