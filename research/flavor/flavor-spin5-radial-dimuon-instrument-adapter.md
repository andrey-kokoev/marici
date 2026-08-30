# The Two Spin(5) Radial Modes Admit the Existing Calibrated Dimuon Instrument

## Source-derived interface

WP877 already requires two ordered real Spin(5) vectors \(u,v\sim5_0\) with
vacuum norms \(a,b>0\). The Standard Model Higgs bilinear permits the
renormalizable source terms

\[
V_{H\text{-portal}}=
\chi_u(u\mathbin\cdot u)H^\dagger H+
\chi_v(v\mathbin\cdot v)H^\dagger H.
\]

These are Spin(5), Standard Model gauge, Lorentz, and weak-basis invariants.
Writing the ordered radial modes as

\[
u=(a+\rho_u)e_5,
\qquad
v=(b+\rho_v)e_4,
\]

and \(H^0=(v_h+h)/\sqrt2\), the off-diagonal scalar mass-squared entries are

\[
\delta_u=2\chi_uav_h,
\qquad
\delta_v=2\chi_vbv_h.
\]

For small mixing and distinct radial masses,

\[
\theta_i=\frac{\delta_i}{m_i^2-m_h^2}.
\]

Thus the two ordered breaking fields themselves supply two labelled CP-even
Higgs-mixing source ports. No new scalar representation is required.

## Adapter to WP243

Freeze the experimentally calibrated two-pole slice

\[
m_u=133.774002075\ {\rm GeV},
\qquad
m_v=151.287002563\ {\rm GeV},
\]

with perturbatively small mixing, Standard Model-like Higgs-mediated
production and decay, and all exotic decay channels closed. On this slice,
identify WP243's dimension-one trace couplings with

\[
\kappa_A=2\chi_u a,
\qquad
\kappa_D=2\chi_v b.
\]

The existing checksum-pinned CMS response, official bottom-associated Higgs
cross sections, branching fractions, acceptance, and background frame then
apply without changing production spin or final-state grammar.

Use the nonnegative faithful rate coordinates

\[
x_u=(\chi_u a)^2,
\qquad x_v=(\chi_v b)^2.
\]

The selected count spectrum per inverse femtobarn has two independent columns,
with diagonal normalization

\[
\frac{\partial N_i}{\partial x_i}
=\frac{4v_h^2R_i}{(m_i^2-m_h^2)^2}>0,
\]

where \(R_i\) is WP243's selected count per inverse femtobarn per unit
\(\theta_i^2\). Multiplication by positive diagonal factors preserves the
rank-two CMS template map and its weak-basis descent.

## Instrument classification

This creates a conditional physical instrument for the current Spin(5)
source on the frozen two-pole, no-exotic-decay slice:

- source operations: the two independently labelled portal coefficients
  \(\chi_u,\chi_v\);
- production: bottom-associated Standard Model-like scalar production;
- decay: Higgs-mixed dimuon decay;
- detector: WP242's two-template CMS 2016 dimuon response plus sideband
  background;
- absolute calibration: WP243's official cross-section and branching inputs;
- faithful coordinate: \((x_u,x_v)\), with independent sign flips remaining
  invisible to the rate channel.

It is an identifier, not a selector. The source action permits continuous
\(\chi_u,\chi_v,a,b\) and radial masses; it does not force the frozen slice or
the observed values.

## Power and completion boundary

WP245 remains decisive: even maximal mixing gives inadequate two-source event
power in the certified 2016 dimuon exposure. The instrument is physically
typed and asymptotically faithful but not operationally identifying on that
finite dataset.

WP246 supplies the correct higher-rate successor: a \(\tau\tau\) channel is
rate-feasible. WP247--WP254 subsequently construct event-level tau trigger,
object-matching, background-pilot, and finite-grid shape instruments. WP258--
WP259 show that transport to the actual Spin(5) pole slice still lacks
same-frame actual-pole tau samples, physical branching normalization, QCD
control, weighted completion, and uncertainties. The finite-grid tau
instrument is admitted; the Spin(5)-pole tau adapter is not.

## Smallest falsifiers

1. Either radial portal coefficient vanishes.
2. The two radial masses coincide or their detector templates become
   proportional.
3. An exotic decay opens and invalidates the Standard Model branching map.
4. Mixing is large enough to invalidate the two independent small-angle
   columns.
5. The radial masses leave the calibrated interpolation support.
6. Finite exposure leaves the lower-power column observationally empty.

## Verdict

The missing current-source interface existed implicitly in the required
breaking sector and is now explicit. WP892's global zero-capability verdict is
refined: the Spin(5) source has a conditional calibrated dimuon instrument on
a frozen two-pole slice. The remaining gates are source selection of the
slice, finite-exposure power, exotic-decay closure, and a calibrated
\(\tau\tau\) successor.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp893_spin5_radial_dimuon_instrument_adapter.py
~~~
