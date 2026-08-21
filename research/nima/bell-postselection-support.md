# Bell normalization is a relative-support theorem

## Hostile control

The source photon state and analyzer effects give a normalized no-signalling
Born table before detector acceptance. That property need not survive
coincidence postselection.

At the maximally entangled point \(r=s\), the source settings \((A_1,B_2)\)
have correlation \(1/\sqrt2\) and unbiased marginals. If every \(B_1\) outcome
is retained but only the \(+\) outcome of \(B_2\) is accepted, the selected
Alice marginal changes by

\[
\boxed{
P(A{=}+\mid B_2{=}+\text{ accepted})
-P(A{=}+\mid B_1\text{ accepted})
=\frac{\sqrt2}{4}.
}
\]

This is not operational faster-than-light signalling: construction of the
selected coincidence sample requires Bob's record. It is a failure of the
postselected table to qualify as a loophole-free Bell readout.

## Exact support condition

For one binary analyzer with effects \(E_\pm=(1\pm O)/2\) and efficiencies
\(\eta_\pm\), the total accepted effect is

\[
F=\eta_+E_+ + \eta_-E_-
=
\frac{\eta_++\eta_-}{2}1
+\frac{\eta_+-\eta_-}{2}O.
\]

It is scalar for all states exactly when

\[
\eta_+=\eta_-.
\]

Under this state-independent fair-sampling condition, acceptance factors out
and cancels in the normalized table. More general detector support is allowed
only if the corresponding state-specific marginal identities are proved.

## Marici consequence

The normalization denominator is not harmless arithmetic applied after the
physics. It is a relative-support pushforward. The Bell readout therefore
requires a source-defined acceptance map whose total effect is scalar on the
retained polarization object—or explicit proof of the weaker no-signalling
square for the chosen state.

This makes Bell directly sensitive to the same supported-versus-absolute
distinction found throughout cosmology and strings:

\[
\boxed{
\text{normalized absolute Born table}
\not\Rightarrow
\text{normalized supported detector table}.
}
\]

The next test must use an actual detector/phase-space support packet rather
than an arbitrary efficiency model.
