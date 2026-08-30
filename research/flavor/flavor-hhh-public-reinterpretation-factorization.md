# HHH public reinterpretation factorization

Work package: WP563  
Owner: marici.Figueiredo

## Public executable suffix

The ATLAS HIGP-2024-32 reinterpretation surface exposes a substantial physical
instrument suffix:

- six ONNX networks: even and odd folds for nonresonant, resonant, and
  heavy-resonant classifiers;
- six corresponding variable-standardization JSON files;
- `ANA-HIGP-2024-32.cxx`, implementing object selection, jet pairing, analysis
  regions, feature construction, and DNN evaluation;
- 118 fixed-signal HS3 likelihood workspaces with detector and theory
  nuisances.

The public SimpleAnalysis repository was inspected at commit
`5a33033d788619bb1039a5b8116fdf43c46fc72a`. The analysis source has blob id
`c28e56eaa988327b6a3d9da791a8c55db0c4a3f5`. A recursive repository census
finds exactly the thirteen HIGP-2024-32 artifacts listed above.

This is enough to map an externally supplied simulated event sample through a
public reconstruction approximation and the released classifiers. It is not
the full fitted source-to-detector map.

## Missing prefix and join

ATLAS presentations state that the nonresonant coupling variations were built
with an internal MadGraph leading-order reweighting procedure from basis
samples at selected cubic and quartic couplings. The public repository does not
contain:

1. the basis event samples;
2. the basis coupling points and polynomial coefficients;
3. the reweight cards or event weights;
4. the normalization and higher-order correction map for arbitrary couplings;
5. a validation map from public SimpleAnalysis histograms to the detector-level
   bins used by the HS3 likelihood.

The HS3 workspaces start with fixed signal histograms and expose only a signal
normalization parameter. The public truth-level code and ONNX files end with
score histograms. No admitted constructor identifies those histograms with the
fixed detector templates, including their systematic variations.

The factorization is therefore

\[
(\lambda_s,z)
\mathrel{\dashrightarrow}E_{\kappa_3,\kappa_4}
\longrightarrow H_p
\mathrel{\dashrightarrow}T_h
\longrightarrow \mathcal L,
\]

where both dashed arrows lack public source authority.

## Exact underdetermination

Let \(x\) be the source quartic displacement and \(w(x)\) the vector of basis
event weights entering the public suffix \(S\). A released fixed template at
\(x=0\) determines only \(w(0)=w_0\). For any vector \(u\), both completions

\[
w_A(x)=w_0,
\qquad
w_B(x)=w_0+xu
\]

reproduce the same released template at \(x=0\), while

\[
{d\over dx}S w_A(0)=0,
\qquad
{d\over dx}S w_B(0)=Su.
\]

Choose \(S=I_2\) and \(u=(1,-1)^T\). The two completions agree on every
released fixed-template datum but give distinct nonzero bin derivatives. Thus
the downstream classifier and likelihood release cannot reconstruct the
four-point source response.

This is not a lack of algebraic span. It is a missing executable source
constructor and a missing validation join.

## Disposition

The currently public artifacts establish physical preparation, event
selection, classifier readout, and a nuisance-bearing fixed-template
likelihood. They do not realize the WP559 four-point derivative as a calibrated
flavor measurement because its source-to-bin Jacobian is not determined.

The smallest repair is one of:

- release the exact MadGraph basis events, reweight cards, coupling polynomial,
  and normalization prescription used by the analysis, together with the
  detector-template validation;
- publish a parameterized HHH likelihood whose bin yields and nuisance
  variations are functions of \((\kappa_3,\kappa_4)\);
- provide a validated response matrix from the public reinterpretation output
  to every HS3 signal and nuisance template.

Without one, independent regeneration would define a new phenomenological
experiment, not reproduce the admitted ATLAS instrument. The smallest exact
falsifier is the affine completion pair above.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp563_hhh_public_reinterpretation_factorization.py

The generated result is
research/flavor/results/wp563_hhh_public_reinterpretation_factorization.json.
