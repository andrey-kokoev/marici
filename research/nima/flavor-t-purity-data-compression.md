# Flavor textures rigidify t-purity but do not select its value

The stationarity branch is closed by Entry 2103. A different possibility is
that the texture atlas itself selects the near-unity value of \(F_t\).
This audit compares all 1,210 viable texture sheets against 12,100 points
drawn uniformly from the full OBS17 \(\chi^2\le4\) ball.

The texture ensemble is extremely rigid:

\[
\operatorname{sd}(F_t)_{\rm sheets}=2.02\times10^{-5},
\qquad
\operatorname{sd}(F_t)_{\rm null}=8.03\times10^{-4}.
\]

Its spread is only \(2.51\%\) of the already restricted experimental
null spread. But its mean,

\[
\langle F_t\rangle_{\rm sheets}=0.9920323,
\]

lies within one null standard deviation of the null median
\(0.9914444\). The textures therefore do not significantly shift the
value toward a distinguished point; they make one data-compatible value
nearly class-constant.

This separates two operations:

- physical data locate the admissible neighborhood;
- sparse texture constraints rigidify the resulting readout across sheets.

Neither supplies a deeper source explanation for why the neighborhood is
near unity. Flavor currently exhibits reconstruction and rigidity, not a
derived numerical selector.

Verification: run check_flavor_t_purity_data_compression.py with the flavor
virtual environment. The checker passes 4/4.
