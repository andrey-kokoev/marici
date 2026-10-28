# Physical examples: source binding by operation, not by file label

## Result

The examples are not wholly external to the native grammar. Their **finite algebraic readouts have an existing native compiler**, now explicitly instantiated in a freshly checked Agda module. Their incoming-family promotion is a separately declared adapter, and the analytic Berry operations remain an external symbolic interpretation. These layers must not be collapsed into either 'all native' or 'only arbitrary packaging'.

## Actual source map

| Layer | Source | Binding established |
| --- | --- | --- |
| Field/parameter input | Exact source records in the example checkers | Explicit supplied coefficients, laws and regimes; not source-free physical derivation |
| Incoming-family promotion | `check_rung_transport_diagram.py:incoming_promotion` | Actual owner definitions executed twice, fresh labels and recursive members retained; explicit inherited/common policies |
| Index/recovery | `TableFibrationCycle`, raw/from/to record views | Existing table interface and exact finite tests; not an additional physical operation |
| Finite sum/product readout | `NativeAmplitudeResolution.Algebra` | Actual native Pi applications retain operator and operand packets; independently defined native readout agrees with the expression |
| Retained cone and triangle | `ThreeWitnessRetainedCone`, `RetainedDomainRepresentation` | Checked generic typed construction and full-packet recovery |
| Native history to triangle | `NativeResolvedDomainRepresentation` | Checked composition on actual original Resolve histories for arbitrary S |
| FCC chart | Decorated canonical cell in the existing example checker | Reversible finite chart on its image, not spatial lattice dynamics |

## New checked physical-readout bindings

`research/nima/agda/PhysicalDomainNativeReadouts.agda` instantiates the existing amplitude grammar with named source factors:

- Oscillator: external drive g chi, bath drive h chi, return coefficient -g. The native expressions compute `1 + return*external` and `return*bath`, exactly the response and noise formulas used by the test.
- Inflow: level k, normal eta, sign J and minus one. Native products compute `k eta J` and its negative.
- Berry: actual matrix-entry factors. Eight triple products, summed over two-valued matrix indices, compute the Bargmann contraction `Tr(P_i P_j P_k)`.

Each expression has an actual `Source.Domain` history under `NativeResolvedDomainRepresentation.ForSource`. This is a typechecked bridge, not merely a matching value type. The seed policy is the existing amplitude policy: marked factors, constants and operator tokens. The computed result is not seeded as an independent answer.

Coefficients and algebra operations are supplied. The theorem is parameterized over W, add, multiply and weights; it does not establish the physical origin of g, chi, k or the projectors. It also does not claim to have serialized every SymPy runtime object into Agda.

## Adapter boundary checked against prior work

`RetainedRelationshipPromotion.agda` supplies a related native bridge: each reciprocal two-packet fiber is assembled with the native Pi rule using only its actual packet seeds. But its shared-endpoint connection generation is an explicit additional constructor, and its `next-input` is a reified retained record. It is not the exact incoming-family/mean constructor used in our examples, and cannot silently be cited as its complete native compilation.

Thus the existence of a native grouping component does not imply every fresh-label, endpoint-policy and aggregate operation has already been reduced to the twelve-rule core. Conversely, the core is not declared to be the only possible WG signature. A provenance-preserving composite with an explicitly declared adapter is a legitimate separate source contract, not automatically a failed WG construction.

## Analytic and physical boundaries

The new formal binding covers the finite algebraic operation tree. It does not cover:

- solving the oscillator equation to derive chi, or thermal fluctuation-dissipation;
- proving anomaly quantization/matching from a UV/IR theory;
- deriving Berry frames, differentiation, integration, exponential holonomy or normalization by a complex modulus.

The CP1 symbolic test checks these latter analytic formulas in its named domain. `DomainWitnessCompiler`-style supplied-law interfaces can retain such operations, but retention is not proof that the original native arithmetic grammar generates the analytic law.

The exact remaining integration question is therefore composition of the **declared adapter and analytic interfaces** with the now-native readout histories, not another proof that arbitrary retained packets admit triangles. No claim of repository-wide absence follows from this bounded audit.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module PhysicalDomainNativeReadouts -Fresh

Exit zero, execution `structured_command_execution:e_42200_1792523008911238800_50`. Receipt: `research/nima/results/agda-PhysicalDomainNativeReadouts.json`. Fresh dependency closure includes the amplitude compiler, original/native resolution bridge and the retained-domain representation theorem. No physical evidence or blanket all-domain coverage is claimed.
