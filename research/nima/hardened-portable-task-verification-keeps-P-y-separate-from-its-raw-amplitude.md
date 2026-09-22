# Hardened portable task verification keeps P_y separate from its raw amplitude

## Deliverable

The numerical verifier now has strict input validation, semantic corruption tests and isolated execution. A first explicit bridge to the filtered-obstruction certificate retains the distinction

`z_y=E_y P_y`,

between an acquired raw scalar and its normalized private source coefficient.

Fresh actual-theta calibration encloses

`10^(-240665)<=E_y<=10^(-240664)`.

For a declared synthetic raw reading in that same interval and a path budget of 32 on the real source line spanned by v_y, the portable numerical certificate proves

`P_y>1/20`.

It does NOT claim that the raw reading equals one, that a physical experiment acquired this amplitude, or that the numerical verifier reconstructs a filtered extension class.

## 1. Hardened verifier boundary

`certificates/verify_diagonal_task.py` now rejects:

- duplicate JSON keys, including nested duplicates;
- floating-point and nonfinite JSON numbers;
- boolean values where integer protocol labels or rational strings are required;
- unknown problem, row, target, certificate, dual and witness fields;
- status-inappropriate evidence fields;
- unsupported metadata fields and malformed coordinate labels.

Rational values remain strings. Scientific-notation strings are parsed as exact rationals, not binary floating point. This permits the very small bridge calibration to be exchanged without expanding hundreds of thousands of decimal zeros.

The problem digest binds the complete numerical input. Recomputing that digest does not excuse an invalid budget inequality, witness or dual bound. It also does not authorize changing the bridge protocol's typed endpoints, seam marks or normalization equation.

The direct Python API expects already parsed objects; duplicate-key detection necessarily occurs in the strict JSON loader. The command-line verifier always uses that loader. These checks do not claim cryptographic authentication or denial-of-service hardening against arbitrarily large rational inputs.

## 2. Freeze the actual private row

The source is

`v_y=mixed(2,3) forgotten(5,7) mixed(11,13)`

in the outer corner [2,60060]. The selected seams are

- 2->4 retained;
- 12->60 forgotten;
- 420->4620 retained;

with vacuum coefficient buffers. The structural certificate verifies the normalized coefficient P_y(v_y)=1 and the right-ideal obstruction P_y(NI)=0 under its owning hypotheses.

For the numerical bridge, restrict explicitly to real sources x=a v_y. Its unweighted path norm is 32|a|. This is not an identification of the full source with a one-dimensional state space.

At spectral point 3i and receiver gamma=2, the two retained unit residual evaluations give

`E_y=K_[2,4] K_[420,4620]/5`,

where K=J-LX is the actual completed-theta residual moment. The forgotten seam contributes its prescribed unit observation. Source forcing beta remains 4; no physical seam constant is reassigned.

## 3. A conservative but genuine raw-data certificate

The producer integrates the boundary-scaled K moments with full theta and integral-tail bounds. It computes log10(E_y), avoiding amplitude underflow, and chooses outward integer decimal exponents. The certified enclosure above is broad but sufficient for this task.

The synthetic acquisition interval for z_y is set to [10^(-240665),10^(-240664)]. It includes the prediction for source v_y throughout the calibration enclosure. This is a test fixture, not a performed measurement or an assertion of achievable precision.

For every compatible calibration and raw reading,

`P_y=z_y/E_y >=1/10`.

The solver supplies the strict target P_y>1/20 with its rational dual certificate and fixed source witness a=1, whose path cost is 32. The separate verifier checks both existence and the universal target inequality.

There is no hidden replacement of raw acquisition error by coefficient error. The acquisition interval is explicitly on z_y and contains the full prescribed uncertainty.

## 4. Assumptions manifest and structural link

`results/py-bridge-manifest.json` binds the numerical problem to:

- the exact source line, outer endpoints and marked seams;
- the raw label z_y and normalized label P_y;
- the equation z_y=E_y P_y;
- the fixed analytical parameters and calibration enclosure;
- explicit external assumptions covering actual calibration, actual acquisition, source membership, the source budget and the structural/category comparison hypotheses.

It also records SHA-256 references to the calibration artifact and Voevodsky's structural problem/certificate files.

The manifest checker validates the supported protocol and its binding to the numerical problem. Those external evidence digests are REFERENCES, not proof that their contents were reverified by the numerical program. Authentication and truth of external assumptions are not inferred from hashes.

The structural verifier was separately rerun successfully on its saved bundle: 240 local kernels, 360 prefix generators, 720 right actions and the 270-column private matrix. Its own analytical and categorical assumptions remain explicit. Neither verifier silently takes responsibility for the other's external hypotheses.

## 5. Adversarial and portability results

The verifier-only audit imports no solver, producer, source recorder or numerical integration package. It checks:

- rejection of 33 semantic corruptions, including recomputed problem digests, wrong endpoints, wrong seam marks, a changed normalization equation, false target bounds and missing assumptions;
- rejection of seven duplicate-key, floating-point or nonfinite JSON fixtures;
- isolated Python execution outside the repository with exactly four files: the verifier, problem, certificate and manifest.

The original numerical suites also pass after hardening: 400 generated engine cases, the physical acquisition fixtures, and 180 parametric-witness cases. Version-1 and version-2 certificate meanings remain distinct.

## Reproduction

Produce the bridge calibration and evidence:

`uv run --with python-flint --with sympy python research/nima/checkers/export_py_acquisition_bridge.py`

Verify the portable numerical bundle:

`python research/nima/certificates/verify_diagonal_task.py research/nima/results/py-bridge-problem.json research/nima/results/py-bridge-certificate.json research/nima/results/py-bridge-manifest.json`

Run verifier-only hardening and portability tests:

`python research/nima/checkers/check_portable_task_verifier.py`

Separately verify the linked structural bundle:

`python research/voevodsky/certificates/verify_filtered_obstruction.py research/voevodsky/results/filtered-obstruction-problem.json research/voevodsky/results/filtered-obstruction-certificate.json`

Test summary: `research/nima/results/portable-task-verifier-tests.json`.

## Scope

The bridge makes the shared labels and normalization auditable. It does not merge numerical source feasibility with filtered-derived nonvanishing, add a new physical measurement, establish all-depth observability or supply a source-comparison map from numerical states alone.
