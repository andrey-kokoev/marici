# Prior scattering clues — iteration5 of10

## Question

Does the prior source's separate reflection record remove the positive preparation rank-loss found in iteration4?

Fresh mutable [explanation status](../conjecture_net/contracts/high-energy-scattering-explanation-status.v1.json) remains unresolved. [Iteration4](scattering-prior-clues-iteration4.md) supplied a strictly positive, non-dark density at which four excitation records retain only one local coupling direction. Operator direction authorizes this bounded source/readout test, not a physical premise.

## Claim boundary

The [autonomous source](../scattering/high-energy/pentachoron_autonomous_contact_note.md), section4, retains complex reflection/transmission matrices, r=t−I, unit-flux normalization and all open/closed channels. Its original result includes total reflection at K/ε=2.30. These existing records provide a distinct test without changing its interaction law or choosing more energies.

### Frozen operation and types

[Prospective contract](contracts/scattering-clues-iteration5.v1.json); [owner-local SCC model](scc-models/scattering-prior-clue-iteration5-v1.json). Active obligation: forward realization of direction effects, then joint preparation/gain nuisance projection and passive ground-frame transport.

Use the archived fixed-ABE20+20 local contact predecessor at ν=1,η=2. Its4-dimensional incident ground sector and the retained witness density are unchanged. The readout family is the four excitation effects F_E at K/ε=2.30,3,4,5, plus total reflected flux at2.30. Reflection is a direction in the reduced1D model, not an independently identified physical particle/detector event.

Restrict r and t to ground incident columns, retaining all open outgoing rows:

\[
R=r^*r,\qquad T=t^*t,\qquad R+T=I_4.
\]

Keep all15 traceless Hermitian perturbations of one shared density. Construct full operator derivatives before evaluating traces and projecting away their preparation image. A separate rival adds one unknown relative reflection-gain column; this is a hypothetical instrument nuisance, not a calibration supplied by the checker. No physical-time map is supplied.

### Explanatory test

- **Problem:** intensity excitation records lose a coupling direction at a positive bright preparation.
- **Bold conjecture:** calibrated total reflection supplies the missing direction at that same witness.
- **Rivals:** elastic reflection adds sensitivity; reflection only repeats existing information; an assumed relative channel gain produces a spurious improvement.
- **Risky consequence:** the second projected singular value exceeds the frozen10⁻⁵ floor with known relative response.
- **Strongest falsifier:** retain the full positive effects, compare analytic/central-difference derivatives, check transmission complement, reflected-excitation duplication, unknown relative gain and passive frame transport.

## Disposition

[Checker](checkers/scattering_reflection_record_clue.py), [result](results/scattering-clues-iteration5.json), [full packet](results/scattering-clues-iteration5-full-packet.npz). SCC check and manifest validation passed; the scientific conjecture **failed**, rather than the implementation checks.

| Readout family at the retained witness | Preparation/gain nuisance rank | Remaining coupling rank | Smallest projected singular value |
|---|---:|---:|---:|
| Four excitations |2|1|1.66×10⁻¹⁷|
| Plus total reflection, relative gain known |2|1|1.76×10⁻¹⁷|
| Plus total transmission |2|1|1.94×10⁻¹⁷|
| Plus reflected excitation only |2|1|8.86×10⁻¹⁸|
| Plus total reflection, relative gain unknown |3|1|1.87×10⁻¹⁷|

Thus reflection does not repair this rank loss **even with calibration assumed known**. Calibration is not the reason this candidate failed. No finite nonlinear parameter degeneracy or all-energy impossibility follows from the local rank result.

At the witness, total reflection is0.0668475, comprising reflected excitation0.0572951 and elastic reflection0.00955241. The full positive direction effects were checked, not just these scalar values. Complement residual1.23×10⁻¹⁵; derivative error3.14×10⁻¹¹; historical equal-mixture reflection replay error1.12×10⁻¹⁶; passive-frame error3.01×10⁻¹⁷; full source/conservation residual8.39×10⁻¹⁵.

### Localized source clue

For a ground incident state, the identity subtraction in r=t−I has no excited outgoing row. Consequently reflected and transmitted excitation amplitudes are identical:

\[
R_{\rm exc}=F_{2.30}/2.
\]

The full-operator duplication residual is9.99×10⁻¹⁸. Merely separating the two excited directions cannot add information; it is not an independent experiment.

A secondary source-operator characterization finds total R at the fixed couplings in the span of the four excitation effects, with residual5.67×10⁻¹⁶. Coefficients are stored in the result. They depend on the specified source fixture; this value relation does not by itself imply a derivative relation or a universal redundancy theorem. The derivative/nuisance test above supplies the actual failed sensitivity result.

The constructive clue is to retain **phase**, not to keep counting redundant intensity records. The source already saves the complex r,t packet. A mathematically declared coherent output-port combination can probe

\[
H_+=\frac{(r+i t)^*(r+i t)}{2}
=\frac{I_4}{2}-\frac{r^*t-t^*r}{2i}.
\]

This is a candidate readout, not a calculated restoration result or an admitted interferometer. The complementary minus port completes a positive effect pair under a unitary recombination. Source r/t conventions, phase references, detector response and native-record maps must be transported consistently; matching matrix dimensions supplies none of those physical capabilities.

### Existing gaps and continuation

`physical-preparation-calibration-and-identification` still requires independently validated preparation and record/instrument maps. `physical-source-justification` still requires kinetic/contact inputs. This failed readout extension does not refute physical scattering or repair its numerical completion; root outcome remains null. Original sources and earlier outputs are unchanged.

Next nonredundant executable test: search prior coherent-port/phase-readout research and test the declared π/2 recombination effect against the same positive witness, retaining preparation nuisance. Use the phase0 recombination as a null and an independently unknown visibility/phase-response rival; do not promote a mathematical beam-combiner matrix into physical apparatus authority. The physical capability branch stays deferred under the existing gap, not a waiting leaf.

Reproduce through the admitted structured-command binding:

```text
uv run --with scipy python research/nima/checkers/scattering_reflection_record_clue.py
uv run --with scipy python research/aspect/scc/scc.py check scattering-prior-clue-iteration5-v1
python research/aspect/scc/scc.py validate research/nima/scc-models/scattering-prior-clue-iteration5-v1.json
```

Independent source/result closure checked all14 arrays, direction complement and witness positivity. Report and bounded prior-source question to `marici.Aspect` were admitted in `ev-000000015908-9a10eeb4-4925-4092-a78c-0a9d9abce603`, proposal `ep_22d6089b-69b3-4012-851d-81b661595998`; this iteration's admitted-but-uncommitted interval is[15908,15908]. An initial graph batch was refused for an incorrect Aspect entity id; rereading the canonical id and correcting it resolved that execution defect. Communication admission supplies no scientific or apparatus authority. Four source/contract/manifest/packet files are untracked; numerical outputs are ignored. No programme proof export, physical detector/preparation authority or Git commit/push is asserted.
