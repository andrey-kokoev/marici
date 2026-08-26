# Four-point measurement path closure

Work package: WP566  
Owner: marici.Figueiredo

## Scope

This packet audits the complete currently admitted flavor route from WP559's
formal connected four-point derivative to a physical measurement. It includes
the strongest public ATLAS and CMS additions through WP565. The claim is
bounded to admitted artifacts and interfaces; it is not a claim that no future
experiment can measure a quartic flavor response.

An end-to-end realization must contain one composable path with all of:

1. a source-derived four-point operation;
2. a weak-basis-invariant map into physical couplings;
3. physical collision preparation and scattering;
4. detector readout and calibration;
5. a likelihood with covariance, nuisance, and uncertainty response;
6. a validated same-domain interface joining the source to that experiment;
7. an uncertainty-supported nonzero pullback to the source direction.

Possessing these fields in separate objects is insufficient. Each adjacent
pair requires a named and validated interface.

## Strongest admitted routes

### ATLAS HS3 route

The 118 ATLAS HS3 workspaces supply collision data, detector templates,
nuisance parameters, and a profile likelihood for frozen signal models. The
public ONNX and scaling packets make the downstream classifier executable.
The public surface does not supply the parameterized basis events,
source-to-event reweighting polynomial, or validated transfer from the flavor
source score into the HS3 bins. Thus the first absent arrow runs from the
portal source direction to the ATLAS calibrated signal templates.

### Official CMS route

CMS HIG-24-012 supplies executed collision preparation, calibrated resolved
and merged readout, control validation, systematic uncertainties, and a
profile-likelihood result. Its published coupling scan fixes
\(\kappa_t=1\) and Standard Model signal topology. The universal portal obeys
\(\kappa_t^2=1-z\), while its quartic source response is
\(z^2/\lambda_H\). Their intersection forces \(z=0\) and zero response.
Thus the first absent arrow is the entrance from the nonzero source-sensitive
portal domain into the official detector likelihood.

### CMS public-code surrogate route

The public `multihiggs_loop_sm` model can generate events with independent
\((D_3,D_4,CT_1,CT_2,CT_3)\). The author analysis repository exposes
selection code, networks, and calibration or systematic objects. This route
still lacks a publication-bound chain through showering, detector simulation,
NanoAOD production, exact final model selection, observed data, datacards, and
nuisance correlations. It can define a new research surrogate after those
choices are made; it does not reproduce the admitted CMS statistical
experiment.

### Cross-experiment Gram route

The CMS inclusive-Higgs mixing readout and a portal-sensitive HHH response
would be rank two away from \(z=0\). WP562 proves that a positive covariance
would preserve this rank. But the portal-complete HHH response and its
cross-experiment covariance are premises, not released instrument fields.
This route proves a conditional identifiability theorem, not a measurement.

## Exact path theorem

Represent each route by the subset of seven required capabilities it carries.
The exact checker computes the set difference from the complete contract. No
admitted route has the full set. It also constructs the directed authority
graph of validated interfaces and enumerates paths from `four_point_source` to
`uncertainty_supported_measurement`. The path set is empty.

This conclusion survives the strongest generous grant: admit the public
generator as a source-side implementation of the invariant portal coupling
path. The graph remains disconnected at the generator-to-calibrated-template
or source-domain-to-official-likelihood arrow.

The smallest exact source-domain falsifier remains

\[
(z,\kappa_t)=\left({3\over4},{1\over2}\right).
\]

It has nonzero response \(9/(16\lambda_H)\), is generatable through a
non-Standard-Model top coupling, and is excluded from the official CMS
likelihood domain. For any nonzero bin direction \(u\), the detector
completions \(T_0\) and \(T_0+(\kappa_t-1)u\) agree on every released CMS
slice point but disagree there by \(-u/2\).

## Classification

The formal four-point operation is source-derived and descends to invariant
physical couplings. Existing HHH experiments are genuine physical readouts
with calibration and uncertainty models on their own admitted signal domains.
The public generator and analysis code are executable research components.
Nevertheless, no currently admitted composable path realizes the formal
four-point derivative as a flavor measurement.

Accordingly the current operation is:

- source-sensitive but not end-to-end instrumented;
- a potential separator on a frozen constructor family;
- neither a source selector nor a presentation rigidifier;
- not an uncertainty-supported flavor measurement.

The contextual partition on `physical16` is therefore not refined by the HHH
artifacts. The largest admitted flavor probe still fixes the inclusive mixing
coordinate \(z\) and retains the quartic-source fiber. Full weak-basis descent
passes before the missing experimental interface; no reference port is used.

## Smallest repair and falsifiers

A sufficient repair is one publication-bound likelihood defined on the portal
source domain and carrying:

- a frozen source-to-event map;
- shower, detector, reconstruction, and selection provenance;
- coupling-dependent templates over the nonzero-mixing domain;
- observed data and calibrated detector response;
- nuisance correlations or covariance;
- uncertainty support proving a resolved nonzero source pullback.

The claim is falsified immediately by such an admitted object. It is also
falsified if an existing release is shown to contain a named, validated
interface completing every arrow above. Merely finding additional generator
coefficients, classifier files, confidence contours, or algebraic covariance
does not falsify it.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp566_four_point_measurement_path_closure.py

The generated result is
`research/flavor/results/wp566_four_point_measurement_path_closure.json`.
