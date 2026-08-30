# Executable kaon-likelihood kernel: WP459

## Question

Does an available, version-pinned flavor likelihood provide the missing experimentally calibrated constraint on WP453's real vector-current direction?

## Frozen executable surface

Use `flavio` 2.7.0 with its bundled measurement database, `wilson` through that dependency set, Python 3.12, and `particle` 0.25.4. The particle version is pinned because later data packages remove the 2022 table expected by this `flavio` release. A Windows-only multiprocessing compatibility shim maps the unavailable `fork` context to `spawn`; it does not alter physics data or predictions.

The registered neutral-kaon mixing observables on this surface are mechanically inspected rather than presumed. The result is:

- `eps_K` is registered and has the bundled `PDG kaon CPV` measurement;
- `DeltaM_K` is not registered as a likelihood observable.

The bundled measurement is Gaussian with central value (0.002228) and standard deviation (0.000011).

## Correlated source probe

At 160 GeV in the `WET/flavio` basis, test the correlated vector-current packet

\[
(C_{VLL},C_{VRR},C_{VLR})=a(1,1,2),
\qquad a=10^{-15}\ {\rm GeV}^{-2}.
\]

This normalization is a fixed sensitivity probe, not a fitted value. For real (a), the executable predictions are exactly equal at machine representation:

\[
|\epsilon_K|_{\rm SM}=0.0019528919765385057,
\]

\[
|\epsilon_K|_{\rm real\ ray}=0.0019528919765385057.
\]

For the hostile complementary probe (a to ia), the prediction becomes

\[
|\epsilon_K|_{\rm imaginary\ ray}=0.04733363710200577.
\]

Thus the instrument detects the CP-odd direction but has zero response to the real correlated ray. WP453's hostile coefficient (-1/6) before its real common factor is in this real direction.

## Contextual partition

Relative to this executable likelihood, all real values along the tested correlated ray are equivalent at the `eps_K` readout, while imaginary values are generally separated. The likelihood therefore has a source-relevant kernel even though the underlying neutral-kaon experiment is physical.

This is not a failure of algebraic transport: WP455 supplies the full correlated mixing-amplitude response. Information is lost at the available observable/likelihood selection, which omits (Delta M_K) because its Standard Model long-distance component is not supplied as a controlled prediction on this surface.

## Disposition

- source-authorized probe: correlated vector-current Wilson ray;
- executable physical instrument: bundled `eps_K` likelihood;
- separation: CP-odd component yes, real WP453 component no;
- selector: no;
- rigidifier: no;
- reference port: none;
- actual WP447 real-current constraint: unavailable on this likelihood surface.

The smallest exact falsifier is any nonzero change of `eps_K` under the declared real correlated probe. The checker finds exact equality.

The remaining instrument gate is an executable (Delta M_K) likelihood with an independently frozen Standard Model long-distance nuisance model, or another source-derived CP-even observable sensitive to the same real current direction. A hand-imposed no-overshoot interval is not a substitute.
