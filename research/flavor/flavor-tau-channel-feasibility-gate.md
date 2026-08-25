# Tau-channel finite-exposure feasibility gate (WP246)

## Result

The source-derived `tau tau` channel is rate-feasible as a repair of WP245,
but it is not yet an admitted detector map. The LHC Higgs Working Group partial
widths and WP243 production normalization predict, before tau selection, enough
events that a modest acceptance could make the weaker source observable.

For each pole the checker evaluates

\[
R_i^{\tau\tau}=1000\,\sigma_{bbH}^{\rm SM}(M_i)
\operatorname{BR}^{\rm SM}_{\tau\tau}(M_i)
\]

per inverse femtobarn per unit `theta_i_squared`. At the D pole and full 2016
exposure, the minimum acceptance is about 2.5% for a 95% probability of at
least one selected event and about 8.3% for ten expected events. These are
optimistic zero-background count gates, not identification guarantees.

CMS Open Data contains 2015 bottom-associated scalar-to-tau MiniAODSIM at 130,
140, and 160 GeV. These points bracket both WP243 poles. However, they are not
in the common 2016 detector frame and supply no frozen reconstructed-tau
selection here. Interpolation must first pass closure on the three-point grid;
bracketing alone does not authorize response transport.

Admission requires validated interpolation to both actual poles, a calibrated
tau trigger/reconstruction selection, backgrounds, and a rank/power test under
tau mass resolution. The exact
falsifier is D-pole acceptance below the computed threshold or proportional
reconstructed response columns.

Run `uv run --with openpyxl python
research/flavor/checkers/wp246_tau_channel_feasibility_gate.py` to regenerate
the exact result.
