# Resource-accounted optical statistical feedback v1

## Successor and physical assumptions

This is a VERSIONED successor to the exact `read-total` interface, not a proof that a physical detector implements that reader. Reuse the selected two-channel passive network, coherent signal preparations, equal calibrated frequency and fresh vacuum environments. Add an explicit ideal direct-photodetection model: a coherent mode with mean occupation a, tapped fraction τ and detector efficiency η yields N∼Poisson(ητa). This standard coherent-state counting rule is an additional physical framework assumption, not derived from WG provenance. No measured detector or apparatus calibration is supplied.

Fixed but unknown initial a,b are independent conditional preparation parameters; coherent-state phase is retained separately and irrelevant to this energy-only task. With fixed a,b, the beam splitter produces product coherent outputs, so conditioning on the tap count does not add a signal-state change beyond the deterministic tap attenuation. This special property is not asserted for arbitrary quantum states, thermal inputs or entangled signals.

## Typed event dictionary

Context: preparation/prior family, τ∈(0,1), η∈(0,1], independent equal-frequency modes, detector assumptions, control calibration and resource convention.

`tap-count(τ,η,n1,n2)`: choose tap strength as a control, then record the two nonnegative integer detector outcomes as observations. Conditional likelihood is the product of Poisson laws with means ητa and ητb. Physical surviving signal summary is `(A,B)=((1−τ)a,(1−τ)b)`. Record both outcomes, efficiencies, tap strength and the parent preparation identity. No event silently resets the signal or reuses a populated ancilla.

Resource ledger in mean occupation: signal `(1−τ)(a+b)`; detector inputs τ(a+b); detected mean ητ(a+b); unobserved detector-loss mean (1−η)τ(a+b). Do NOT equate random observed count with the exact energy removed on an individual trial. Absorbed detector energy, readout electronics and apparatus reset need their own physical ledger.

`gain(q)`: same existing source law `(A,B)→(q²A,q⁴B)`; fresh environmental outputs retain the removed mean energy. Calibration is a precondition, not inferred from observations.

State has two levels: retained physical preparation/event/outcome record and Bayesian information distribution on unknown a,b. A posterior parameter pair is not the actual physical state. Histories replay physical effects given their initial parameters and update information given recorded outcomes.

## Information update

Specify independent Gamma(shape k_i, RATE ρ_i) priors on a,b, with positive parameters and a physical preparation justification required before use. After counts n_i with c=ητ,

`a_i | n_i ∼ Gamma(k_i+n_i, ρ_i+c)`.

Current surviving posterior means and variances are

`m_i=(1−τ)(k_i+n_i)/(ρ_i+c)`

`v_i=(1−τ)²(k_i+n_i)/(ρ_i+c)²`.

This is a conjugate update, not a universal identification result. Priors are supplied context; they are not learned from one outcome. Zero counts retain uncertainty, and eta/tau miscalibration invalidates these formulas. A discrete equal-H hostile remains useful: priors on `(8,0)` and `(0,8)` with equal weight give equal zero-count likelihoods, so no clicks do not identify the hidden sector.

## Policy and declared success

Task: choose q to make CONDITIONAL EXPECTED remaining signal occupation equal h, where `0≤h≤m1+m2`. Reuse the source `target_gain(EnergyTaskState(m1,m2, transcript),h)`. Then

`E[Hfinal | transcript] = q²m1+q⁴m2 = h`.

Feedback is executed on the ACTUAL already-tapped signal, not the inferred initial preparation. This reaches an expectation, not exact energy on each unknown preparation. Amplifying targets outside the posterior-mean contraction range are rejected.

Conditional preparation uncertainty gives

`Var(Hfinal | transcript)=q⁴v1+q⁸v2`

for the independent prior model. Thus Chebyshev gives `P(|Hfinal−h|≥ε | transcript)≤min(1, Var/ε²)`. This bounds the unknown coherent MEAN occupation under the Bayesian preparation model, not photon-count fluctuations in a final detector. Those add a separate instrument distribution. No uniform small-error bound follows from the interface alone.

High realized counts can raise the posterior mean even though every fixed physical signal loses energy at the tap. Information revision is not excitation or a physical energy increase. Comparisons must use the fixed-state resource law and the conditional statistical law at their separate types.

## Same-source comparisons and hostiles

The physical gain summary commutes with the original energy `gain_step`; the physical tap summary commutes with a NEW mathematical `tap` event multiplying both components by 1−τ. Neither can be replaced by an exact identity `read-total` event. Detector likelihood and posterior update supply the new observation square in distribution. This is now a concrete stochastic event source suitable for later same-source comparison.

Hostiles: zero-count ambiguity; using the pre-tap mean as current state; conflating detected count with removed energy; claiming posterior-mean target equality as samplewise equality; using vacuum gain with populated environments. Preserve these as rejection constraints.

## Verification and remaining gates

`checkers/optical_statistical_feedback_v1.py` checks conjugate posterior moments algebraically, resource and observation-update laws, source-controller targeting on fixed declared count transcripts, residual variance, zero-count ambiguity and pre-tap reset rejection. Counts are deterministic test fixtures, not measurements or Monte Carlo evidence.

This constructs a conditional statistical-feedback model with actual back-action and information types. Physical device selection/calibration, task-specific accuracy, prior justification, disturbance model, time and apparatus resources remain open. The root is not resolved. The next substantive comparison is to instantiate both mathematical and ideal physical maps on this SAME versioned event history and test intermediate—not just final—states and likelihoods.
