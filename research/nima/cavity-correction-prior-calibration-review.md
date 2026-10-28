# Prior calibration work relevant to the compiled cavity correction

## Question and disposition

Does prior work already address the two residuals after the full-port prefix-removal compilation: physical inverse/replay control and interval encoding?

A further search found the completed optical/endpoint synthesis programme, including timed frames and a full-history calibration certificate. These are more directly reusable than a new generic apparatus proposal. They do not supply measured calibration or an interval encoding.

This review inspected the source notes only. No dependency chain, numerical checker, calibration acquisition or hardware run was executed.

## Existing full-history certificate

`optical-exchange-history-calibration-certificate.md` retains 155 complex amplitudes, including two coherently reused environment modes. Its event operator bound is

    epsilon_event = ||B_hat-B_ideal||_2
                    +4 epsilon_entry+sqrt(2) epsilon_router.

For unitary event implementations, its telescoping argument bounds the full word error by the sum of event errors. Consistent intermediate frame timestamps cancel; initial/final timestamp errors remain. Its validator rejects stale or missing calibration and environment reset inconsistent with coherent reuse.

This answers how to organize a bounded multi-event certificate once independently justified component errors exist. It does not authorize the inverse controls in the newly compiled cavity word. Each actual forward/inverse/replay implementation still needs its own control and error binding; an exact model transpose is not a measurement of the inverse device.

## Timing and storage were already isolated as separate assumptions

`optical-exchange-timed-endpoint-frames.md` uses

    F_new(t_out,t_in)=S(t_out) F S(t_in)^dagger.

It explicitly observes that emitted ports leave at different times and assumes capture/storage to assemble them at an event boundary. A gap requires its own laboratory evolution. Thus storing all amplitudes in one matrix state does not construct synchronized hardware access. Its phases and timestamp traces are synthetic.

The newly tested correction must retain that distinction. Reversing the mathematical component order does not reverse elapsed laboratory time, and replay is a new controlled sequence.

## A prior model comparison already rejected an overly strong shortcut

`optical-plant-endpoint-exchange.md` and `optical-endpoint-exchange-verdict.md` compare the actual four-port plant with addressed exchange. At the frozen lossy parameters the retained pair has singular values 1 and 0.48: it is not a swap, and phase correction cannot fix the deficient singular value. Exact swap occurs only at a declared lossless delay-line boundary with different parameters.

This is not a contradiction to the new full-port inverse comparison. The old negative result concerns the compressed retained pair as an exchange; the new construction keeps all ports and assumes inverse component controls. Do not replace the frozen cavity by the ideal swap boundary while claiming to preserve the source law.

The synthesis also identifies a return-phase omission in the earlier prose extension: q must enter both outputs of the loss coupler. The new prefix-removal checker is frozen at p=q=1, so it is unaffected. Any extension to general phases must use the corrected ordered dilation and conjugate adjoints, not silently extrapolate its real transpose formulas.

## What the completed programme actually requests

The final optical/endpoint verdict calls for independently calibrated complex four-port probe records, phase-sensitive router characterization, endpoint timestamps and uncertainty, a validity interval, an environment access/storage policy, and held-out observations. Its test data are synthetic. `exchange-detector-calibration-and-identifiability.md` separately shows that preparation/loss ambiguity and a local-oscillator phase reversal can imitate the predicted signed response.

These are existing protocol requirements, not new missing-object abstractions. Reuse them only after changing the carrier/control bindings explicitly: their 155-coordinate source with two reused environment modes is not the ten-mode three-round source with fresh input slots. The abstract telescoping inequality is reusable; the numerical certificate, router dimension, error values and reuse policy are not transferable unchanged.

## Interval-encoding search result

`wg-interval-operation-bridge.md` supplies a complete selected-history/interval dictionary on NNMHV compiler records, not optical states. It preserves full records and move histories, so it is a possible source-side interface, not the missing optical realization.

The apparent optical hit `research/aspect/interval-window-fourier-moment-gate.md` instead concerns smooth spatial/periodic windows and a Fourier commutator bound. It neither identifies optical process segments with the NNMHV intervals nor authorizes physical trim. Its finite-mode localization obstruction has a different source and must not be imported as a no-go for labelled finite path encoding.

No interval-to-cavity operation/readout map was found in the inspected sources. That statement is a bounded search result, not an exhaustive theorem of absence.

## Consequence

Generic calibration design and inverse-word mathematics already have prior work. What is not supplied is a measured, source-matched control package for this ten-mode correction or a justified optical realization of the NNMHV interval objects. The full-history certificate can be adapted as a conditional error calculation, but doing that alone would not remove either blocker. No ready physical task, new measurement request or broader conjecture promotion follows from this search.
