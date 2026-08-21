# Local Breit-Wheeler tomography does not determine the nonforward cut

The forward restriction loses the \(f_3,h_3\) directions, so one might try
angular-resolved pair production with arbitrary incoming Stokes states. This
does recover, at each pair-production angle \(x\), the same-angle Gram matrix

\[
G(x,x)=A(x)A(x)^\dagger.
\]

But a nonforward elastic unitarity relation requires cross-angle kernels

\[
G(x,x')=A(x)A(x')^\dagger.
\]

The replacement

\[
A(x)\longmapsto e^{i\varphi(x)}A(x)
\]

leaves every local polarized differential rate invariant while multiplying
the cross-angle kernel by \(e^{i(\varphi(x)-\varphi(x'))}\). Thus even complete
initial-polarization tomography, performed independently at every angle, does
not determine the nonforward discontinuity.

This is the experimental analogue of the recurring Marici distinction
between fiberwise coefficient data and coherent transport between fibers.
The missing datum is a cross-angle phase connection.

The surviving routes are narrower:

1. derive that connection from the source amplitude;
2. construct a genuinely interferometric measurement linking distinct
   final-state directions; or
3. supply amplitude-level theory input and use Breit-Wheeler data only to
   constrain its diagonal absorptive part.

Ordinary angular distributions, even with arbitrary incoming polarization,
are insufficient.

Reproduce with
`research/nima/check_breit_wheeler_local_tomography_obstruction.py`.
