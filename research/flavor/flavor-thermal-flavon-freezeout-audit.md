# Thermal matrix-flavon freeze-out audit (WP122)

Owner: `marici.Figueiredo`.

## Bounded question

Can a local thermal matrix-flavon model supply the unvalidated bath in WP121
and thereby turn its Gaussian law into a source-derived ensemble of stable
Yukawa couplings?

Pre-objective process report: excitement `7/10`, confidence `3/10` that the
route survives, expected information gain `8/10`. The attraction is that the
fluctuation--dissipation calculation is exact; the low confidence reflects the
known distinction between thermal fluctuations and frozen couplings. These
ratings are non-evidential and may be confounded by the tractability of the
quadratic model.

Frozen optionality snapshot: one source-admissible branch (finite-volume
thermal zero mode), two necessary successor arrows (quench and stabilization),
and six hostile controls. Admission requires a source-fixed correlation
volume, freeze time, quench law, stabilization law, and matching scale. No
phenomenological flavor datum may fix them.

## Source model and fluctuation--dissipation reduction

Let `Phi_u` and `Phi_d` be complex `3 x 3` bifundamental scalar fields. For a
homogeneous real coordinate `X` averaged over a correlation volume `V_c`, take

\[
F(X)=\frac{V_c m^2}{2}X^2,
\qquad
dX_t=-\frac{m^2}{\eta}X_t\,dt
 +\sqrt{\frac{2T}{\eta V_c}}\,dW_t .
\]

Here `m^2>0`, `eta>0`, `T>0`, and `V_c>0`. The Einstein relation gives

\[
\kappa=\frac{m^2}{\eta},\qquad
D=\frac{T}{\eta V_c},\qquad
\beta_{\rm eff}=\frac{\kappa}{2D}=\frac{V_c m^2}{2T}.
\]

Applied isotropically to all 36 real matrix coordinates, this reproduces
WP121's equivariant OU generator and normalized Gaussian law. Thus the OU
drift/noise ratio is derived *conditional on* the thermal matrix-flavon field,
its overdamped limit, and its finite correlation volume.

The full weak-basis group acts orthogonally on these coordinates. The
quadratic free energy, scalar mobility, and scalar noise covariance are
invariant, so the thermal semigroup descends to the stacky `physical16`
quotient. A component-dependent mass, mobility, temperature, or correlation
volume tied to a texture chart fails descent.

## Exact obstruction: equilibrium is not a stable Yukawa draw

The equilibrium mean is zero and the variance of every real zero-mode
coordinate is

\[
\sigma_*^2=\frac{T}{V_c m^2}.
\]

Two failures follow.

1. At fixed `T` and `m^2`, the thermodynamic limit `V_c -> infinity` collapses
   the ensemble to the zero matrix. A macroscopic homogeneous Yukawa parameter
   is not produced by ordinary equilibrium fluctuations.
2. At finite `V_c`, leaving the bath active makes the candidate Yukawa matrices
   time-dependent stochastic variables. That is not yet a stable set of quark
   couplings.

The smallest repair is a new relational history,

\[
\text{thermal preparation}
\longrightarrow \text{quench at }t_f
\longrightarrow \text{post-quench stabilization}
\longrightarrow \text{matching to Yukawas}.
\]

It is a new experiment, not a reinterpretation of thermal equilibrium.

For initial variance `v_0`, the frozen pre-quench variance is

\[
v_f=e^{-2\kappa t_f}v_0
 +\frac{T}{V_c m^2}(1-e^{-2\kappa t_f}).
\]

This formula exposes the remaining selector data: `V_c`, `t_f`, the initial
law, and the quench/stabilization dynamics. Choosing any of them from the
observed hierarchy merely relocates the fit upstream.

## Hostile controls

1. **Infinite volume:** `V_c -> infinity` gives a delta law at zero.
2. **No quench:** the matrices remain stochastic rather than stable couplings.
3. **Quench without stabilization:** subsequent drift or diffusion changes
   the frozen law.
4. **Chart thermostat:** anisotropic masses or noise fail full weak-basis
   descent unless independently sourced as new physical tensors.
5. **Target freeze time:** solving for `t_f` from flavor data is not a
   prediction.
6. **Isotropic anarchy:** the quadratic source supplies no independent
   hierarchy or ratio-alignment selector; its `physical16` pushforward remains
   the WP120 Wishart/Haar ensemble.

## Classification and smallest falsifier

Classification:

`finite-volume thermal producer; freeze-out selector not source-authorized`.

The thermal operation is a source-derived producer conditional on the stated
field/bath model and it descends to `physical16`. It is neither a numerical
flavor selector nor a presentation rigidifier. The untyped quench can select a
smaller history-dependent ensemble, but currently has no independently
declared physical instrument.

The smallest exact falsifier is

\[
V_c\,\sigma_*^2=\frac{T}{m^2},
\qquad
\lim_{V_c\to\infty}\sigma_*^2=0.
\]

Therefore an equilibrium fluctuation cannot remain a nonzero homogeneous
coupling in the macroscopic limit without new scaling or freeze-out data.

## Disposition

WP122 derives WP121's OU coefficients one arrow deeper, then locates the first
nonfaithful physical step at the conversion of a thermal fluctuation into a
stable coupling. A viable successor must provide, before flavor readout, a
local flavon action, microscopic bath, finite correlation-volume mechanism,
quench trigger, post-quench stabilization, and RG/matching contract.

Post-objective process report: excitement `8/10`, confidence `2/10` that this
quadratic thermal route becomes a physical selector, realized information
gain `8/10`. Raw delta: fluctuation--dissipation and quotient descent were
constructed; the equilibrium-as-coupling branch was eliminated; one new
freeze-out branch opened with five missing source data; all six declared
hostile controls were typed. The ratings remain non-evidential.

