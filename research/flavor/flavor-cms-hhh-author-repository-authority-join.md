# CMS HHH author-repository authority join

Work package: WP565  
Owner: marici.Figueiredo

## Question

WP564 found that the published CMS HIG-24-012 likelihood is restricted to
the Standard Model top-Yukawa slice. Two public repositories materially
improve the situation:

- `multihiggs_loop_sm` is an executable MadGraph model for loop-induced
  multi-Higgs production. Its restricted five-parameter model exposes
  \((D_3,D_4,CT_1,CT_2,CT_3)\), so source events need not remain on the
  fixed-\(\kappa_t\) slice.
- `hhh-analysis-framework` contains analysis code, 24 ONNX networks, 684
  ROOT calibration or systematic files, and scripts for resolved and boosted
  HHH reconstruction.

The question is whether these objects and the official CMS result compose to
an admitted source-calibrated flavor instrument.

Frozen repository revisions:

- generator: `788431390ded97d4b44c25a0013b184053b4aaad`;
- analysis framework: `b3014e3e8e95fb6398ecbe979cefb02152e69fad`.

## What is executable

The generator is a genuine source-side constructor. The analysis repository
is also more than presentation data: its networks and calibration machinery
can support a research reconstruction of detector response. This repairs the
claim that only confidence contours are public.

It does not yet repair the authority join to the reported CMS likelihood. At
the frozen revision the analysis repository has:

- no release tag, license file, or citation file;
- no occurrence of the analysis identifier `HIG-24-012` or paper identifier;
- no datacard, workspace, `fitDiagnostics`, `higgsCombine`, observed-data,
  nuisance, or correlation object identifiable by tracked filename;
- 24 alternative ONNX files, selected in scripts through author-local absolute
  paths rather than one frozen publication manifest;
- a README whose datacard link is empty, whose main production instruction is
  unfinished, and whose efficiency-map step requires input paths supplied by
  the operator.

These facts do not make the code invalid. They type it as an executable
research surrogate rather than the uniquely identified statistical model that
produced the official result.

## Exact non-uniqueness witness

Let \(a=\kappa_t-1\), and let \(T_0\) be any released or reconstructed bin
template on the published slice \(a=0\). For any nonzero detector-bin vector
\(u\), define two detector extensions

\[
T_A(a)=T_0,
\qquad
T_B(a)=T_0+a u.
\]

Both agree with every fixed-\(\kappa_t\) datum at \(a=0\), but their
derivatives are respectively zero and \(u\). At the smallest WP564 hostile
portal point \(z=3/4\), \(\kappa_t=1/2\), hence \(a=-1/2\) and

\[
T_B-T_A=-{u\over2}\ne0.
\]

Event generation does not choose between these detector completions. Neither
do unmanifested alternative networks or calibration files. The missing object
is a named, versioned interface that binds a source parameterization to the
exact final classifier, selection, templates, observed data, nuisance model,
and likelihood used for the CMS result.

## Contextual classification

On the frozen generator domain, the source probe family contains
portal-relevant trilinear, quartic, and top-contact directions. On the public
analysis-code domain, one can construct detector-level surrogate partitions
after choosing models, maps, samples, and statistical completion. Those
partitions are choice-relative and are not yet the official CMS contextual
partition.

The official transportable flavor partition therefore remains the WP564
partition: the inclusive-Higgs probe fixes \(z\) and retains the
\(\lambda_s\)-fiber. The new repositories establish possible execution, not
an authorized refinement of that partition.

The operation is neither a source selector nor a presentation rigidifier. It
is a source-sensitive generator plus a detector-surrogate toolkit with an
unfilled provenance and likelihood join. Every parameter used here is
weak-basis invariant, so full weak-basis descent passes; the failure occurs
after source generation and before the calibrated statistical readout.

## Acceptance and falsifier

The branch becomes an admitted physical instrument only if a publication-
bound manifest identifies the exact source model, classifier hashes,
calibrations, templates, observed data, nuisance correlations, and statistical
model, and validates their composition over the nonzero-mixing portal domain.

The smallest exact falsifier of identification from the present surface is
the pair \(T_A,T_B\) above. They agree on all released fixed-slice records and
disagree at \((z,\kappa_t)=(3/4,1/2)\). Thus executable pieces do not imply a
unique source-calibrated probe.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp565_cms_hhh_author_repository_authority_join.py

The generated result is
`research/flavor/results/wp565_cms_hhh_author_repository_authority_join.json`.
