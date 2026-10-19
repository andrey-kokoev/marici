# Physics source/provenance register — iteration 2

## Deliverable and disposition

The [register](contracts/physics-source-register.v1.json) instantiates the existing programme source interface for eleven distinct source objects. Its [checked result](results/physics-source-register-v1.json) expands 25 ingredient specifications into complete source records, each with a source identity, role, SHA-256 origin, verification level, scope, future freeze boundary and permitted/forbidden uses.

The central `common-witness-provenance-register` task is complete as a candidate register with typed presentation maps and exact comparison residuals. The common physical witness remains unconstructed. The physical target set awaits the next iteration's charter.

## Source inventory

| Source | Current construction | Principal missing comparison |
|---|---|---|
| `native-bool-square-pilot` | Retained Bool words, delta/permutation encoding, accepted spectral/real structural reference | Physical source/preparation/time/readout |
| `conditional-six-port-retained-exchange` | Typed 22-coordinate exchange; anchor/mismatch encoder with positive metric | Source-selected preparation; Bool comparison; control authorization |
| `marked137.T9.exact-domain.v1` | Exact-domain retained T9, supplied fixture, declared compatible coefficient law | Independent law selection and physical binding |
| `scattering.native-pair-orbital.v1` | Native pair, encounter and orbital channels with supplied laws | Coefficient-operation transport; scale/species/readout binding |
| `scattering.high-energy-endpoint.v1` | Conditional endpoint/contact model with 2+8 product-record leads | Numerical completion, source law and physical binding; map to the native-pair branch |
| `wg.fixed-refinements.FG` | Reviewed fixed-Composite history transport | Marked relation-algebra attachment comparison |
| `energy.gain-exact-reader.v1` | Exact gain/probe task quotient | Physical exact reader and full-source reconstruction |
| `context.authority-resource.v1` | External context transitions and continuation policy | Source-specific authority/resource/task binding |
| `optical.coherent-gamma-tap.v1` | Conditional modewise optical/statistical comparison | Independent apparatus/prior/calibration evidence and instrument overlap |
| `instrument.reciprocal-lossy-cavity.v1` | Ordered cavity/loss/delay source model | Common-carrier and measured-parameter binding |
| `instrument.dead-time-detector.v1` | Sequential destructive counting with ready/dead memory | Common-carrier and measured recovery/efficiency binding |

Every entry supplies operations, composability, event/history identity, geometry, dynamics, observation and missing ports. Separate presentation views point back to exactly one source instance. No cross-source identification is inferred from a view, source tag or common interface.

## Ingredient provenance

`native_source_data` means native to the specified mathematical/software source. For example, the marked137 numerical responses, weights, reference and flat attachments are supplied fixture data, with physical calibration still open.

The declared T9 grouping policy and coefficient-law class have separate constructor-convention records. The retained chart/energy transport is derived conditional on those records. The energy normalization and clock are therefore visible premises.

The optical coherent/Poisson law is imported physical theory. Independent Gamma preparation is a supplied model convention. Gain/efficiency/prior boxes are instrument specifications. Cavity mirror/loss/delay parameters and detector efficiency/recovery values likewise remain specifications. This register admits no measured-calibration, fitting or held-out observation record.

The checked output includes all required shared-witness fields as **candidate binding slots**. `common_carrier_id` and its embedding are null, overlap-map lists are empty, and the missing constructor is stated for each source. Same-source presentation maps are listed separately from these unsupplied common-carrier maps.

## One independently checked operation-preserving map

For the Bool fragment, write a path as `(s,w)`, with initial Bool pair s and its complete word w in left/right flips. Map it to

`(source_id, delta(s), U_w, w, delta(trace(s,w)))`.

Here `U_w` is the ordered product of the independently specified four-by-four permutation matrices, and the implementation retains s itself for decoding. There are two relevant levels:

1. **State/action square.** On each of four basis labels, `P_op delta(s) = delta(op(s))`. Linear extension proves the primitive square on C4. Matrix associativity and induction on word length give the square for every finite word.
2. **Record composition.** For source-attached p and q, `U_(p;q)=U_q U_p`; the retained word concatenates and the traces concatenate at their shared endpoint. The empty word is the identity. Reading the initial label and complete word decodes the original path, so the enriched record map is injective.

The matrix component by itself is a quotient. `left;right` and `right;left` have the same matrix and endpoint but distinct retained paths. The empty word and `left;left` likewise have the same matrix but distinct histories. Repeated equal paths retain different occurrence IDs during grouping.

Fresh exact checks cover all eight primitive basis squares, all 508 source/word pairs through word length six, and all 3076 composition splits. The all-finite-word claim uses the preceding generator/induction argument; the bounded enumeration is its implementation regression test.

The image adapter rejects mixed source tags, corrupt traces, mismatched attachments and duplicate occurrence identities. Source tagging here is a guard on composition, not permission to create cross-source arrows.

## Retained comparisons and residuals

- **Bool/exchange:** the existing fixed-fibre single-port C4 intertwiner has rank at most one for distinct ports and two for identical ports. A tagged C4 direct-sum C22 package preserves alternatives; it supplies no common physical source or mixed-source operation.
- **Native pair/marked137:** fourteen native pair energies cannot injectively intertwine with the tested five-eigenvalue coefficient generator under a nonzero affine rate. The encounter restriction has a metric embedding, but its nontrivial fifth-order cycle cannot be transported to the existing involutive target relabellings.
- **Native scale:** selected encounter flux depends on `delta=s*e_i`. The rival scale `s1=e0/e1` makes the two doublet cores equal. Independent scale or source-selection information is required by a discriminating target.
- **Exact energy/optical:** the gain law compares, while exact identity reading and state-changing tap-count have different event signatures. Their relationship remains a versioned event change.
- **WG/marked attachment:** fixed-Composite history transport leaves a separate map to the marked nonsplit relation-algebra attachment open.
- **Optical/cavity/detector:** common optics terminology does not supply a map. The optical summary loses phase needed by an interference extension; the detector retains memory absent from ideal independent Poisson counting. Their preparation, phase/clock, environment, memory and complete-record interfaces must be compared explicitly.

The registry keeps the native-pair/orbital scattering branch separate from the high-energy endpoint/contact child. A future comparison must name actual state, operation and record maps between them.

## Verification and next step

```sh
python research/nima/checkers/check_physics_source_register.py
python research/aspect/scc/scc.py check physics-programme-v18
```

The register pins 25 source/interface files. Eleven corrupted register variants are rejected, including false common-witness promotion, fixture-as-measurement, mixed-source maps, cyclic provenance, lost obstructions, collapsed event versions and stale hashes. Other source algebra results retain their cited review strength; their producer suites were not rerun.

Iteration 3 can now select a bounded physical target pair with the ingredient provenance and missing maps visible. A useful comparison is the phase-retaining cavity plant against the memory-retaining detector instrument, with the optical statistical controller as a conditional contribution. The charter must decide the exact instances and discriminate imported-law reproduction from a future source-derived explanation.
