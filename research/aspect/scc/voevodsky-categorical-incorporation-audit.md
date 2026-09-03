# Incorporating Voevodsky's categorical advances into SCC

## Question

Which changes to SCC are forced by the coherence-pyramid apparatus, its conformance profiles, the univalent handoff audit, and the categorical residual doctrine?

## Sources

- `research/voevodsky/categorical-apparatus-v2.md`
- `research/voevodsky/categorical-apparatus-v2-conformance.md`
- `research/voevodsky/aspect-univalent-coherence-handoff-audit.md`
- `research/voevodsky/categorical-residual-doctrine-and-constraint-levels.md`

## Mandatory compiler changes

### 1. Replace flat categorical success with an eight-layer dependency manifest

Every categorical SCC packet must declare the applicable subsequence of: base computad; cells and laws; partial completion; filler-fiber and selection extension; certificate transfer; sector overlap; typed horn tower; bounded completeness. The compiler must verify an acyclic dependency graph, artifact locators, and schema identities. Omitted layers remain explicit `not_constructed` values, not successes inferred from lower layers.

### 2. Emit a ten-coordinate conformance profile

SCC must report base incidence, declared cells, completion, relative filler, strict selection, certificate backend, sector vertex, sector edge, horn coverage, and physical backend independently. There is no scalar completeness score. Current SCC observational-rank and transport fields cover fragments of this vector but do not distinguish completion, selection, overlap, horns, or physical realization.

### 3. Separate localization, univalent completion, and observation

The categorical port type must distinguish:

\[
\mathcal P\xrightarrow{L}\mathcal P[W^{-1}]
\xrightarrow{j}\widehat{\mathcal P}
\xrightarrow{Q}\mathcal R.
\]

`L` requires a source-authorized weak-equivalence class and its universal inversion contract. `j` changes the identity presentation through a declared Rezk or equivalent completion. `Q` requires a detector or stable-record ontology, physical interface, and descent authority. Neither `L` nor `j` constructs `Q`; a cohomology functor is not a physical quotient merely because it preserves an equivalence.

### 4. Compile residuals as a coproduct, not a severity chain

Presentation residual, observer-invisible class, pre-descent anomaly, cutoff error, and substantive positive residual must have distinct schemas and codomains. Conversion arrows are admitted only with their named witnesses. In particular, an observer quotient is defined only with an inclusion witness from the presentation gauge into the observer kernel.

### 5. Distinguish quotient-zero from literal-zero

Joint observer faithfulness may prove that a curvature class vanishes in the observer quotient. SCC must not promote this to literal vanishing until presentation representatives are removed or a faithful coordinate on the intended quotient is proved. This is the categorical form of SCC's existing anti-kernel-promotion gate and should become a reusable residual rule.

### 6. Make comparison squares first-class

The completion–observation square must carry its bounded tail residual. The coherence–positivity square must state which equality, inequality, or positivity margin survives. A failed square produces a typed obstruction at that square; it does not trigger a replacement completion, quotient, or higher cell unless the missing constructor is source-derived.

### 7. Separate filler existence from strict selection

A nonempty filler fiber proves possible completion, not a canonical choice. SCC must require a selection extension with invariance or descent checks before emitting a strict selected filler. This blocks the RH-interface failure identified by Voevodsky: relative fillers exist while modularly invariant strict selection does not.

### 8. Bound horn coverage and completeness

Horn obligations must name dimension, boundary data, admissible filler type, and coverage bound. `complete` is permitted only relative to the declared bounded predicate. No finite horn census promotes to unbounded or global categorical completeness.

### 9. Keep mathematical realization and physical backend orthogonal

A completed bounded mathematical realization may still lack a physical backend and cross-sector edge. SCC must keep these coordinates independent and prohibit physical language unless a source-derived readout port is present.

## Implementation order

1. Add a standalone `categorical_apparatus_compiler.py` producing the eight-layer manifest and ten-coordinate profile.
2. Add typed `localization`, `univalent_completion`, and `observational_quotient` ports with arrow-specific gates.
3. Add `categorical_residual_compiler.py` with the five-way residual coproduct, inclusion-witness gate, and quotient-zero/literal-zero distinction.
4. Add comparison-square and filler-selection hostiles.
5. Integrate the two compilers into `scc.py` only after their dedicated fixtures pass; preserve existing SCC packet compatibility by marking absent new layers `not_constructed` rather than silently synthesizing them.

## Strongest falsification attempt

Search of current SCC Python sources finds no univalent-completion type. Observational handling is limited to an observational-rank certificate and a kernel-pair anti-promotion flag. Residual handling exists in several specialized compilers but not as the categorical five-way coproduct. Therefore SCC cannot currently represent the distinction among localization, completion, and physical quotient, nor emit the full conformance vector.

## Disposition

The Voevodsky advances require a new categorical intermediate representation rather than additional fields on the existing observational-rank certificate. The immediately valid incorporation is the typed architecture and migration boundary above. Implementing `Q`, strict selection, sector edges, or horn fillers for any sector still requires sector-owned source objects; SCC may check those objects but must not synthesize them.
