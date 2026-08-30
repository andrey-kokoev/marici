# Trace-adjoint source-rate detector map (WP243)

## Result

On a frozen, physically explicit subdomain of WP237, the trace-adjoint portal
has a source-parameter-identifying detector map

\[
P_{\rm det}: (\kappa_A^2,\kappa_D^2)
\longrightarrow \frac{dN_{\mu\mu}^{\rm selected}}{dm_{\mu\mu}\,d{\cal L}}.
\]

The map is executable as an expected selected-event spectrum per inverse
femtobarn. Luminosity is an exposure argument, not a source coordinate.

## Admitted source domain

The claim is conditional on all of the following source assumptions:

- two CP-even trace modes from the WP237 portal;
- distinct poles at `133.774002075` and `151.287002563 GeV`;
- perturbatively small universal Higgs mixing;
- no exotic decay channels;
- bottom-associated production through the Higgs-mixed bottom Yukawa;
- the CMS WP239/WP242 selection and reconstructed-mass responses.

The detector channel sees `kappa_i^2`, since

\[
\theta_i^2=kappa_i^2\frac{v^2}{(M_i^2-m_h^2)^2}.
\]

Accordingly, the faithful source coordinate for this experiment is
`(kappa_A_squared,kappa_D_squared)`. Independent coefficient signs remain in
the rate-channel kernel; no sign-identification claim is made.

## Independently calibrated normalization

The LHC Higgs Cross Section Working Group YR4 workbook supplies 13-TeV
bottom-associated SM-like scalar cross sections and partial widths. The exact
workbook is checksum-pinned. Both simulated pole masses lie inside published
grid brackets, so the checker uses linear bracket interpolation and prohibits
extrapolation.

For each mode,

\[
R_i=1000\,\sigma_{bbH}^{\rm SM}(M_i)
\operatorname{BR}^{\rm SM}_{\mu\mu}(M_i)A_i\epsilon_i
\]

is the selected count per inverse femtobarn per unit `theta_i_squared`. The
factor 1,000 converts `pb * fb^-1` to events. The measured coefficients are

\[
R_A=0.01975586475,\qquad R_D=0.003488916980.
\]

The branching fractions use the sum of modes explicitly listed in the YR4
BSM-width sheet. That sheet excludes NLO electroweak corrections; this is an
explicit normalization limitation, not hidden precision.

## Faithfulness

Multiplying WP242's two independent detector templates by these positive
source-derived rate factors gives a rank-two microscopic Jacobian. Its
theta-squared Gram determinant is

\[
6.6491340532\times10^{-11}>0,
\]

with smallest singular value `0.00113456585`. Applying the negative YR4
cross-section uncertainty to both columns still leaves a positive determinant
`2.4484168941e-11`. The diagonal nonzero map from `kappa_squared` to
`theta_squared` preserves rank two.

The contextual partition is therefore singleton `kappa_squared` pairs on the
admitted two-mode domain. Coincident detector templates make the columns
proportional and lower rank to one; this is the smallest exact falsifier.

The operation descends under the full weak-basis groupoid because `Tr(A)`,
`Tr(D)`, pole masses, mixing residues, and dimuon invariant mass are all
weak-basis invariant. No reference port is introduced.

## Classification boundary

This is an asymptotically source-parameter-injective calibrated rate map
conditional on the frozen WP237 Higgs-mixing grammar. WP245 shows that the
available finite exposure is insufficient for operational identification. It
does not:

- select the absolute masses or nonzero portal coefficients from flavor;
- distinguish rival scalar grammars engineered to have the same poles and
  universal Higgs mixing;
- select a proper family in `physical16`;
- identify coefficient signs through this rate-only channel.
- establish finite-exposure statistical power.

Thus it repairs the missing microscopic source-to-detector Jacobian without
turning a conditional detector inversion into a UV uniqueness or flavor
selection claim.

## Reproduction

Run:

`uv run --with numpy --with awkward --with uproot --with scipy --with openpyxl python research/flavor/checkers/wp243_trace_adjoint_rate_pdet.py`

The checker generates `results/wp243_trace_adjoint_rate_pdet.json` and fails on
workbook checksum drift, extrapolation, a nonpositive normalization, loss of
rank, loss of the Gram margin under the declared cross-section uncertainty, or
failure of the coincident-template hostile test.
