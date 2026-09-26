# A checked amplitude as a weighted fibration readout

## Result

Follow-up: [arbitrary-even-n native recursion](native-scalar-recursion.md)
now supplies a shared-current table algorithm, computationally checked through
twelve legs. The fixed four/six-point implementation and formal fixture below
remain separate reference checks.

The first independent native weighted-table amplitude evaluator is implemented for the existing **massless scalar phi-four tree benchmark at four and six points**. It constructs tables directly from external momenta and coupling, evaluates their diagram fields, and sums over the channel fiber at a declared boundary. It does not call the old evaluator or decode an old derivation to obtain its result.

For a declared boundary b, let H_b be its complete family of labelled tree channels. With the supplied field-theory weights,

\[
\mathcal M(b)=\sum_{h\in H_b}w(h),\qquad
w(h)=-\frac{\lambda^{V(h)}}{\prod_{e\in E_{\mathrm{int}}(h)}q_e^2}.
\]

For the existing rational fixtures with lambda = 3/5:

\[
\mathcal M_4=-3/5,\qquad \mathcal M_6=6/25.
\]

All ten six-point channel contributions agree individually with the existing direct evaluator. Totals agree with its recursive evaluator for every root on the declared fixtures. Tests also cover all 720 six-point leg permutations, nonuniform rational kinematics, changed couplings, momentum scaling, row permutations and separate boundary fibers.

## Native three-column construction

`amplitudes/native_scalar_fibers.py` defines native rows `(label, from, to)`.

- Boundary declaration row: theory, leg count and coupling.
- External rows: all four-momenta, with labelled external ports.
- Channel rows: recursive diagram tables attached to canonical split ports.
- Diagram rows: actual vertex couplings and internal propagator data, including its split, momentum and denominator.

The channel fiber is selected by the from-column and channel role. No amplitude subtotal is stored in a diagram. The readout multiplies its local factors and sums the resulting channel weights. Declarations and external rows specify and validate the boundary; they are not additional amplitude contributions.

Endpoint uniqueness, full channel coverage, attachment types, momentum conservation, masslessness and propagator consistency are checked before readout. Empty/missing declarations are errors, not silently assigned a zero physical amplitude. Boundaries outside the declared physical domain are not supplied with implicit couplings or momenta.

## Why it agrees with the old scalar recurrence

This is the elementary four/six-point comparison, not a general scattering theorem.

At four points, removing the chosen external root leaves three singleton currents. Each has value 1. The unique root vertex therefore contributes `-lambda`.

At six points, an unordered partition of the five remaining labels into three nonempty odd blocks must have sizes `(3,1,1)`. Choosing the triple gives exactly ten terms. Its current consists of one vertex and three singleton leaves, so its value is `lambda/q^2`. The amputated root contributes another `-lambda`, giving `-lambda^2/q^2`.

The triple not containing the root is in bijection with an unordered `3|3` split. Our native construction generates exactly those splits, once each. Conservation makes the two complementary momenta negatives of one another, with equal squared norm. Thus native and original terms have the same denominator regardless of root or which complementary triple is used for the canonical key.

There is no extra factorial or propagator on the amputated external root. For the selected fixture, the ten denominators are four copies of 8, two of -4 and four of -6. Consequently:

\[
\mathcal M_6=-\lambda^2\left(\frac4{8}+\frac2{-4}+\frac4{-6}\right)
=\frac23\lambda^2=\frac6{25}.
\]

The channel-bijection argument explains agreement throughout the stated non-pole four/six-point domain. The Python tests check the actual implementations on the recorded finite families; they are not a formal certification of Python semantics.

## What is supplied by physics

The benchmark retains its existing conventions:

- interaction `-lambda phi^4/4!`;
- metric `+---`, all external momenta incoming and exactly massless;
- vertex `-i lambda`, propagator `i/q^2`, delta-stripped contribution `i M`;
- rational kinematics away from internal poles.

For a tree with V vertices and V-1 internal edges, the product of these phases is `-i`, giving the displayed real rational coefficient M. We do not replace `i0` by a rational number or evaluate a pole.

**Fibration organizes which contributions belong together. It does not determine the coupling, propagator, phase convention or integration measure.** Those remain explicit inputs. Counting channels instead of summing their signed weights fails the benchmark.

## Formal and computational verification

`agda/FiniteFiberAmplitude.agda` uses the actual `TableFibrationCycle.Table`. It defines the finite weighted boundary readout and proves compatibility under a supplied row translation that preserves boundary membership and local weights. The finite enumeration retains multiplicity. Completeness, absence of duplicates and coefficient laws required for reordering are not conjured by that theorem.

`agda/NativeScalarFiberFixture.agda` additionally instantiates the weighted readout on a native ten-row table using the actual `ScalarSixFixture` momenta. Its independently computed denominators agree with the actual generated `ScalarSixKernel.channels` census. Every reciprocal is checked, and the native sum gives `144/600 = 6/25`, agreeing with `ScalarSixCertificate` by `refl`. The checker parses the fixture's integer data to ensure it is the same Python benchmark, not merely a different sample with the same answer.

Both the generic theorem and concrete fixture freshly compile in safe/cubical mode. The broader rational evaluator comparisons remain computational tests. This is not yet an amplitude instantiation of `NativeTableResolution.Resolve`, nor an Agda proof of Python execution or the QFT rules.

Hostile controls reject missing/duplicate channels, corrupted propagators, incompatible vertex couplings, off-shell/nonconserved inputs and poles. Other controls distinguish the correct answer from a sign reversal, a spurious permutation divisor, an omitted channel, an unweighted fiber count and a sum of absolute weights.

Run:

```powershell
pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeScalarFiberFixture -Fresh
python research/nima/amplitudes/native_scalar_fibers_check.py
python research/aspect/scc/scc.py check nima-native-scalar-fiber-amplitude
```

Receipts:

- `results/agda-NativeScalarFiberFixture.json`;
- `results/native-scalar-fiber-amplitude.json`, including all native table rows, individual channel weights and source hashes.

No loop measure, arbitrary-multiplicity theorem, weights from bare fibration, or new physical prediction is claimed. Independent review remains pending.
