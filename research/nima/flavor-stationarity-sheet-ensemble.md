# The flavor purity stationarity selector fails on the fitted ensemble

Entries 2097 and 2099 left open whether

\[
\partial_r F_t(r,\gamma)=0
\]

could select a joint physical relation. The complete ensemble test evaluates
the stationary curve on all 1,210 viable flavor sheets using each sheet's
own masses, \(V_{us}\), and \(\gamma\).

The intervals are disjoint:

\[
r_{\rm sheet}\in[0.08881,0.08992],
\qquad
r_*(\gamma_{\rm sheet})\in[0.07805,0.08569].
\]

No sheet lies within one propagated standard deviation of its prediction.
The stationary curve has RMSE \(0.00703\), which is 5.58 times worse than
the constant central stationary-point predictor.

The moderate raw correlation \(0.406\) does not rescue the relation: it
tracks some variation while carrying a fatal systematic offset. Therefore
purity stationarity is not the missing source selector on the admitted
flavor ensemble.

The remaining near-unity result is only the split established in Entry
2092: hierarchy forces the \(u,c\) limits, while the \(t\) value is a
pointwise alignment whose selection mechanism remains unknown.

Verification:

    research/flavor/.venv/Scripts/python.exe research/nima/checkers/check_flavor_stationarity_sheet_ensemble.py

Run from the repository root with the equivalent relative path. The checker
passes 4/4 falsification gates.
