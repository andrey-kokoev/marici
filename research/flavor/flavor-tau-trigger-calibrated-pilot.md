# Tau trigger-calibrated pilot (WP249)

## Bounded question

Does WP248's frozen offline two-tau selection remain count-feasible after a
named, source-local HLT decision from the same CMS simulation record?

## Exact menu join

The MiniAOD `ParameterSets` tree stores CMSSW strings as hexadecimal fields.
Decoding the declared `@trigger_paths` vector and joining its 16-byte hash to
`TriggerResults::psetid_` yields a 494-name menu for every event, with zero
menu/status length mismatches. The independently named double-tau family is

\[
\begin{aligned}
15 &: \texttt{HLT\_DoubleMediumIsoPFTau35\_Trk1\_eta2p1\_Reg\_v2},\\
16 &: \texttt{HLT\_DoubleMediumIsoPFTau40\_Trk1\_eta2p1\_Reg\_v4}.
\end{aligned}
\]

Either path fires in 613 of 14,688 events. WP248's frozen offline conjunction
has two passing taus in 811 events. Their event-level intersection contains
only 142 events, hence

\[
A_{\mathrm{pilot}}=\frac{142}{14688}=\frac{71}{7344}\approx0.00967.
\]

This is below WP246's weaker-pole 2.49% acceptance required for a 95% chance of
at least one event. Even transferring the 2015 pilot fraction directly to the
full 2016 exposure would give only about 1.16 expected weaker-pole events at
unit mixing before backgrounds.

## Disposition

The frozen double-hadronic-tau selection closes negative on count feasibility.
Trigger-object matching is not used here, but it cannot repair the failure: it
can only remove events from the event-level intersection. This packet does not
authorize post-hoc loosening. A successor must freeze a different source- and
instrument-motivated channel or selection before inspecting its efficiency,
then establish mass-grid closure, common-era calibration, backgrounds, and
rank.

Run `uv run --with sympy python research/flavor/checkers/wp249_tau_trigger_calibrated_pilot.py` to
reproduce the exact inequality and generated JSON.
