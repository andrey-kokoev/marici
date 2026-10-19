# Frozen rival coverage and source-dependence audit

## Decision

Accept `rival-and-prediction-contract` as a scoped specification for the frozen target pair. Nine named alternatives now have fixed changes, shared predictions, exact operation/record controls, parameter policy and explicit separation/alias dispositions.

Contract: `contracts/physics-rival-prediction-table.v1.json`.
Checker: `checkers/check_physics_rival_prediction_table.py`.

No empirical exclusion, physical authorization or native source-law derivation follows from this specification. Measurement work remains parked.

## Fixed policy

The executable controls use the frozen nominal mirror/loss amplitudes 3/5 and 4/5, p=q=1, and eta=gamma=9/25. Preparations, routing and parameters do not change after a control is evaluated. These are mathematical model inputs, not measured calibration. A different parameter regime requires a separately versioned control, not fitting to the desired answer.

For scalar probability/norm controls, differences exceeding twice the 1/100 discrepancy allowance separate the two enlarged nominal prediction sets. The round-order coefficient residual is an exact map distinction, not a probability confidence interval.

## Coverage

| Rival | Exact control/result | Disposition |
|---|---|---|
| Delete returning state after dark reflection | Prepare u=4/5,x=3/5: reflected field is zero but x_next=12/25. With next external inputs zero, reflected amplitude is 48/125 and occupation 2304/15625; deletion predicts zero. | Ordered continuation distinguishes hidden stored state. |
| Three-port compression is closed unitary | Unit returning input has retained norm 13321/15625 and environment norm 2304/15625. | Reject closed-unitary claim; the compressed **open** plant remains valid. |
| Exchange round order without relabelling witness | On e0, squared coefficient residual between W1 W0 and W0 W1 is 227000018/244140625. | Labelled operation transport fails. |
| Reset detector ready each bin | P(CC given 11)=0 versus 81/625. P(CNC given 101)=729/15625 versus 81/625. | Complete histories distinguish retained memory. |
| No-click implies ready | Starting readiness 1/2, a photon/no-click leaves readiness 25/41. Next conditional click is 9/41, not 9/25. | Same current record does not imply same predictive state. |
| Discard no-click records | First-click selected mass is 9/25; omitted mass is 16/25. Selected frequency 1 is a conditional statistic, not the full first-click probability. | Invalid complete-record comparison, not another normalized model of the original target. |
| Active-port nonlinear phase completion | Preserves all total-N<=1 overlap histories but fails 16 active creation squares. The fixed finite-sector reflected mean is -1/5 instead of 3/5. | Countermodel to weak law-selection premises; not an alternative satisfying full passive coherent recovery. |
| Merge two no-click environment labels | Complete CP laws agree on 252 classical sharp-photon histories. An out-of-charter coherent-memory X probe gives 0 versus 4/5. | **Not identified** by the charter; no in-scope discriminator claimed. |
| Reproduce imported W/Kraus laws in another adapter | Identical operations give identical output predictions by induction. | Output alias; common-source derivation and provenance cannot be inferred from the fit. |

The phase and CP controls are rerun through the existing side-effect-free exact dynamics-audit functions. Their earlier residuals remain intact; they are not relabelled as measured exclusions.

## Source dependence

The Fock/coherent construction and Born/CP law are imported physical theory. W, mirror/loss amplitudes, efficiency and recovery are supplied source/instrument specifications. Retained mode/history maps, overlap squares and the controls above are constructed consequences.

Neither agreement of the two conditional overlap routes nor rejection of memory-reset/deletion shortcuts independently supplies creation covariance, W, a physical clock/energy scale or preparation authority. An adapter with the same imported law can reproduce every numerical answer while failing the explanatory provenance obligation. This is an explicit alias, not something that a new scalar output test can remove.

The next source-law step must identify a native principle that implies the selected operation, or record the precise obstruction if the reviewed sources contain no such principle. The conditional creation-covariance uniqueness theorem remains useful but cannot certify its own premise.

## Structural robustness and remaining work

The dark-continuation occupation, missing environment norm, reset CC/CNC and no-click continuation differences each exceed 2/100 at the frozen fixture. This is an exact nominal separation margin, not full nuisance robustness. Phase rivals remain aliases on the single-excitation domain, and CP completions remain aliases on classical memory. Those failure regions are part of the rival coverage.

The programme identifiability/robustness node remains open: broader parameter/nuisance coverage and its original prerequisites are not bypassed. Physical-sector and common-witness assemblies also remain open.

Fresh checker controls reject missing/duplicate rival coverage, promoting the CP alias to a classical exclusion, adding an empirical exclusion and declaring imported laws source-derived. All source inputs are hashed before and after checking.

```
python research/nima/checkers/check_physics_rival_prediction_table.py
python research/aspect/scc/scc.py check physics-programme-v18
```
