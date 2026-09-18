# Radiative generator-map no-go for degree-zero targets

## Question

Can cluster generators be mapped nontrivially to gauge-invariant radiative observables without first defining a radiative chain complex?

## Chain-map constraint

For a map from Coherent Resolution to a radiative complex, degree one requires

\[
F_0d_{\rm CR}=d_{\rm rad}F_1.
\]

If the target consists only of gauge-invariant records or charges in degree zero, then `d_rad=0`. Consequently

\[
F_0d_{\rm CR}=0.
\]

The type-A flip graph is connected. A function on cluster vertices annihilating every signed mutation edge is therefore constant.

## Result

Every chain map to a target concentrated in degree zero sends all cluster generators to the same radiative object. No cluster-dependent assignment of canonical weights, insertion/reflow labels, or boundary updates can descend this way.

A nontrivial comparison requires at least

\[
R_1\xrightarrow{d_{\rm rad}}R_0,
\]

where `R1` contains declared gauge, flux, or interpolation generators and

\[
d_{\rm rad}F_1=F_0d_{\rm CR}.
\]

This identifies the missing radiative datum more sharply: it is not only a vertex assignment to Bondi data but a target differential and mutation-edge map.

## Claim boundary

The obstruction applies to targets with zero differential. It does not exclude a nontrivial map after a source-defined radiative chain complex is supplied.

Verification:

- `research/nima/checkers/check_radiative_generator_map_no_go.py`
- `research/nima/results/radiative-generator-map-no-go.json`
