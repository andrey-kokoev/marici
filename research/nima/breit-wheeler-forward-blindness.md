# Forward Breit-Wheeler data does not determine the transverse Bell lens

## Result

Through dimension ten, restrict the photon amplitudes

\[
\Phi_1=g_2s^2+g_3s^3,
\qquad
\Phi_2=f_2(s^2+t^2+u^2)+f_3stu,
\qquad
\Phi_5=h_3stu,
\]

with \(s+t+u=0\). On the forward locus \(t=0\),

\[
(\Phi_1,\Phi_2,\Phi_5)
=
(g_2s^2+g_3s^3,\,2f_2s^2,\,0).
\]

The forward restriction therefore erases both dimension-ten directions
\(f_3\) and \(h_3\). Its coefficient Jacobian has rank two. At the
transverse Bell point \(t=u=-s/2\), however,

\[
(\Phi_1,\Phi_2,\Phi_5)
=
\left(g_2s^2+g_3s^3,
\frac32f_2s^2+\frac14f_3s^3,
\frac14h_3s^3\right),
\]

and the coefficient Jacobian has rank three.

Hence polarized forward photon-fusion sum rules, including total
Breit-Wheeler absorption data, cannot by themselves reconstruct the
transverse Bell ratio. The missing information is angular: one needs a
nonforward, fixed-\(t\) absorptive amplitude or an equivalent tomography
that retains helicity coherence and phase.

## Meaning for the experimental route

Breit-Wheeler production remains useful as the unitarity cut of the electron
loop, but an inclusive pair-production rate is the wrong readout. The next
admissible program is to determine whether angular-resolved polarized pair
production supplies the nonforward discontinuities needed by a fixed-\(t\)
dispersion relation. If it supplies only diagonal helicity probabilities and
not interference, it remains insufficient.

This is a typing obstruction, not a no-go theorem for nonforward dispersion.

## Reproduction

Run `research/nima/check_breit_wheeler_forward_blindness.py`. The durable
packet is `research/nima/results/breit-wheeler-forward-blindness.json` with
SHA-256 `C7CCB498F7C748097A6C8CE5FE4D93819858B3372D3F66254D8A166E0FA49395`.
