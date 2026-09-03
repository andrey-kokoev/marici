# Outcome-dependent loss and tomography identifiability

## Question

When do no-click statistics make path–polarization tomography identifiable under setting-, mode-, and outcome-dependent loss?

## Claim boundary

This packet analyzes binary Pauli settings with independent outcome efficiencies. It proves a nonidentifiability result for unconstrained simultaneous state-and-efficiency estimation and gives sufficient calibration conditions. It does not model dark counts, multiphoton events, or a complete laboratory error budget.

## One binary setting

For a Pauli observable with expectation

\[
m\in[-1,1],
\]

the ideal probabilities are

\[
p_+=\frac{1+m}{2},
\qquad
p_-=\frac{1-m}{2}.
\]

Let the two detector channels have efficiencies \(\eta_+,\eta_-\in[0,1]\). The three physical record probabilities are

\[
c_+=\eta_+\frac{1+m}{2},
\]

\[
c_-=\eta_-\frac{1-m}{2},
\]

\[
c_\varnothing=1-c_+-c_-.
\]

Retaining the no-click outcome restores probability normalization, but it does not by itself identify \(m,\eta_+,\eta_-\). The no-click probability is determined by the two click probabilities and supplies no third independent equation.

## Explicit nonidentifiability

The parameter triples

\[
(m,\eta_+,\eta_-)=(0,1/2,1/2)
\]

and

\[
(m,\eta_+,\eta_-)=(1/2,1/3,1)
\]

both produce

\[
(c_+,c_-,c_\varnothing)=(1/4,1/4,1/2).
\]

Thus even complete click/no-click records cannot distinguish these state–calibration pairs. Repeating the argument independently for each Pauli setting leaves a gauge family in full tomography when each setting has unconstrained efficiencies.

## Conditional renormalization bias

Discarding no-click records and normalizing the two clicks gives

\[
m_{\rm cond}=
\frac{c_+-c_-}{c_++c_-}.
\]

This equals \(m\) when \(\eta_+=\eta_-\), but not generally. For an unpolarized setting with \(m=0\), \(\eta_+=1\), and \(\eta_-=1/2\), one obtains

\[
m_{\rm cond}=1/3.
\]

Outcome-dependent loss therefore creates a false Pauli expectation if no-click data and calibration are omitted.

## Known calibration

If \(\eta_+\) and \(\eta_-\) are known and nonzero, then

\[
p_+=c_+/\eta_+,
\qquad
p_-=c_-/\eta_-,
\]

and

\[
m=p_+-p_-.
\]

For the nine-setting path–polarization architecture, known positive efficiencies for every setting and outcome preserve joint monicity: each of the fifteen Pauli coordinates is recovered from calibrated outcome probabilities.

Zero efficiency destroys the corresponding outcome information and may destroy monicity.

## Calibration designs

A known balanced reference with \(m=0\) has ideal probabilities \(1/2,1/2\), so one exposure determines both efficiencies:

\[
\eta_+=2c_+,
\qquad
\eta_-=2c_-.
\]

Alternatively, known \(+1\) and \(-1\) eigenstate references calibrate the two channels separately. The calibration state must itself be source-authorized; assuming its expectation imports the desired answer if state preparation is unverified.

If efficiencies share a lower-dimensional physical model across settings, joint self-calibration may be possible. The exact gate is injectivity, or locally full Jacobian rank, of the combined state–calibration record map after quotienting unavoidable gauges.

## Mode-dependent loss

When loss is an operator rather than a scalar channel efficiency, the effects are

\[
V^*E_{s|j}V.
\]

Calibration must then identify the restriction of \(V\) relevant to the measured effect span. Scalar correction is valid only if \(V^*E_{s|j}V\) is a known scalar multiple of the ideal effect on the admitted state domain.

## Exact diagnostic

An exact rational checker verifies the indistinguishable parameter pairs, conditional bias \(1/3\), recovery under known nonzero efficiencies, failure at zero efficiency, and balanced-reference calibration. No floating-point arithmetic is used.

## Disposition

No-click outcomes preserve normalization but do not resolve unconstrained state–efficiency ambiguity. Robust tomography requires independently known efficiencies, source-authorized calibration states, or a constrained shared loss model whose joint record map is proved injective modulo declared gauge. Conditional click renormalization is valid only under outcome-independent loss.
