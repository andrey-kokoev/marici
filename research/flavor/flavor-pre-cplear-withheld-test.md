# Pre-CPLEAR optical-model withheld displacement test (WP410)

## Deutschian test

Eberhard and Uchiyama published an optical-model calculation of neutral-kaon
regeneration in 1994. CPLEAR later performed its dedicated carbon-regenerator
measurement and published both components of the complex forward-amplitude
difference in 1997. CPLEAR Table 2 prints the earlier model values beside four
later momentum-bin measurements.

WP410 treats the 1994 values as frozen predictions. It fits no coefficient to
CPLEAR. For each bin it evaluates the full correlated residual using CPLEAR's
reported real/imaginary covariance.

The four complex records give

\[
\chi^2=14.7251605
\]

for eight measured components and zero fitted parameters. The 5% upper critical
value for eight degrees of freedom is 15.507, so the frozen model survives the
declared global test narrowly. The 350--450 MeV/$c$ bin contributes 8.619 by
itself and is the smallest hostile tension; the agreement is not a lookup-table
identity.

The primary records are the [1994 optical-model paper](https://doi.org/10.1016/0168-9002(94)91159-2)
and the later [CPLEAR measurement](https://doi.org/10.1016/S0370-2693(97)01193-3).
The [1999 dispersion analysis](https://arxiv.org/abs/hep-ex/9905007) documents
the broader scattering-data context and the assumptions relating real and
imaginary forward amplitudes.

## What was predicted

The withheld object is the complex matter-induced flavor displacement
$\Delta f(p)$, not merely a fitted scalar coincidence. Its real and imaginary
components feed WP406's exact finite-width transfer matrix and are observed by
the same graphite intervention. The prediction predates the dedicated readout
and is evaluated without refitting.

## Authority boundary

This is retrospective validation, not prospective blinding. It establishes a
hard-to-vary explanatory success only to the extent that the 1994 optical model
and its scattering inputs were independent of the later CPLEAR records. It does
not prove uniqueness of the optical model, does not select a quark `physical16`
point, and does not eliminate every rival nuclear completion.

The next hostile audit must inspect which nuclear screening, attenuation,
multiple-scattering, extra-species, and dispersion assumptions entered the 1994
prediction. Any parameter imported from earlier regeneration displacement data
must be named; otherwise “zero refit to CPLEAR” would overstate source
independence.

Run `uv run --with sympy python
research/flavor/checkers/wp410_pre_cplear_withheld_test.py` to regenerate the
JSON result.
