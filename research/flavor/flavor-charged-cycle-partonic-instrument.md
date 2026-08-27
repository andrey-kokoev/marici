# Charged-cycle partonic instrument

## Bounded question

Does the WP639 contact descent admit a concrete light-particle process before
detector calibration, and exactly which information can that process retain?

## Frozen symmetry-broken normalization

Let the neutral components of \(\widetilde H^u\), \(S\), and \(X\) be replaced
by declared real insertions \(h,s,x\), with no implicit square-root factors.
The WP639 charged current then reduces to

\[
J=g\,\bar u_Ld_R,
\qquad
g=(L_A+L_B)hsx.
\]

Eliminating \(\chi\) gives

\[
\mathcal L_6=-G(\bar d_Ru_L)(\bar u_Ld_R),
\qquad
G={|L_A+L_B|^2h^2s^2x^2\over m_\chi^2}.
\]

The four-quark operator has dimension six and \(G\) has mass dimension minus
two. Each bilinear is charged, but their product is electrically neutral.

## Executable partonic channel

Consider massless \(u_L\bar d_R\to u_L\bar d_R\) at fixed color, with no spin
or color average and no competing amplitude. For the nonzero helicity channel,
the scalar-current contractions give

\[
|\mathcal M|^2=G^2\hat s^2.
\]

The response is isotropic under these declared assumptions:

\[
{d\hat\sigma\over d\cos\theta}={G^2\hat s\over32\pi},
\qquad
\hat\sigma={G^2\hat s\over16\pi}.
\]

This is an executable source-level process: its incoming state, outgoing
state, helicity, color, energy, and counting effect are specified. It is not
yet an experimentally calibrated instrument.

## Contextual partition and kernel

At unit vev insertions and \(\hat s=1\), the constructive unit path has
\(G=4\) and normalized squared amplitude 16. Equal opposite paths have
\(G=0\) and zero response. Holding the relative cycle record fixed at plus
while changing \(m_\chi\) from one to two gives \(G=1\) and normalized squared
amplitude one.

The source process therefore retains the destructive-cycle distinction and
the mass normalization. But it depends on \(|L_A+L_B|^4\), so it identifies
neither the sign nor the complex phase of the total current. Recovering that
information requires a source-authorized interfering amplitude in the same
external helicity and color channel.

## Classification and remaining gate

The operation is a source-defined executable partonic probe, not a selector,
not a texture rigidifier, and not a `physical16` operation. Detector authority
still requires parton distributions, flavor tagging, Standard Model and other
operator interference, running and mixing, cuts, resolution, backgrounds,
systematics, and a calibrated likelihood. The fixed-color result must not be
reported as a hadronic cross section.

## Reproduction

Run:

    python research/flavor/checkers/wp640_charged_cycle_partonic_instrument.py

The generated result is
`research/flavor/results/wp640_charged_cycle_partonic_instrument.json`.
