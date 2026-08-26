# Quantum bath dilation of magneto-optic loss

Owner: `marici.Aspect`

## Result

The smallest finite quantum completion of the two circular loss channels is an
independent environmental port for each channel. The completed four-port map is
unitary. The system-only attenuation is not: it fails the canonical commutator
test even when it reproduces the correct mean amplitude.

## Source authority and typed ports

The source is one system mode and one vacuum bath mode for each circular
polarization. The input and output ports are ordered as system then bath inside
each circular block. This is a finite frequency-bin realization of loss, not a
microscopic material bath or a continuum fluctuation-dissipation derivation.

For each circular label, constructor order is preparation, system-bath mixing,
system detection, then environmental trace. With complex transmission \(t\)
and real loss amplitude \(l\), the block is

\[
U(t,l)=\begin{pmatrix}t&l\\-l&t^*\end{pmatrix},
\qquad |t|^2+l^2=1.
\]

The exact instance uses \(t_+=3/5\), \(l_+=4/5\), \(t_-=5i/13\), and
\(l_-=12/13\). Both blocks are exactly unitary. Their direct sum retains a
nonzero circular intensity contrast and a nontrivial relative phase, hence both
dichroic and birefringent magneto-optic markers survive the dilation.

## Conserved and dissipated quantities

Total system-plus-bath photon number is conserved by the unitary constructor.
System photon number is dissipated into the unobserved bath. For
\(a_{\rm out}=t a_{\rm in}+l b_{\rm in}\), the bath-vacuum term contributes no
mean counts, but its commutator contribution is indispensable:

\[
[a_{\rm out},a_{\rm out}^{\dagger}]=|t|^2+l^2=1.
\]

Deleting the bath yields \(|t|^2<1\). That scalar-preserving hostile can fit
mean attenuation while ceasing to be a valid quantum output mode.

## Detector and frame

The detector sees only the retained system outputs in a calibrated circular or
linear analyzer frame. Tracing the bath produces the loss channel. Circular
labels and phase conventions must be fixed before returning to the linear
frame; relabeling them reverses the reported rotation marker.

## Completion gate

This finite construction supplies exact commutator and vacuum-noise completion
for one frequency bin. A broadband claim still needs a continuum bath whose
coupling spectrum is fixed by the same causal material response, thermal noise,
Kramers-Kronig asymptotics, and a material-specific fluctuation-dissipation
law. Those are not inferred from this dilation.

Run:

```powershell
python research/aspect/checkers/quantum_bath_dilation_of_magneto_optic_loss.py
```
