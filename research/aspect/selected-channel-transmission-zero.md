# Selected-channel transmission zero

Owner: `marici.Aspect`

## Bounded question

Does reciprocity and total losslessness of a two-path optical multiport imply
that one declared detector amplitude is zero-free, strictly positive-real, or
minimum phase? The exact answer for the apparatus below is no. Total
scattering, state tomography, and a selected scalar channel are different
maps with different kernels.

This packet implements the optical side of
`research/nima/theta-scalar-zero-is-a-transmission-zero-not-an-observability-defect.md`.
It classifies an optical zero and makes no RH claim.

## Source, delay, phase, and ports

The source is a two-route amplitude packet. One route carries a one-sample
delay relative to the other; the delay convention and its phase are fixed
before detector selection. With `q=z^-1`, the reciprocal two-port scattering
matrix is

`S(q)=(1/2)[[1-q,1+q],[1+q,1-q]]`.

The two rows are the selected and complementary detector amplitudes. On the
unit circle, `S(q)` is unitary: the complete output preserves total intensity
and is faithful at every frequency. Symmetry makes this displayed multiport
reciprocal in the common energy-normalized port frame.

The selected source-to-detector channel is

`h(z)=(1-z^-1)/2=(z-1)/(2z)`.

It vanishes at `z=1`, while the complementary channel
`g(z)=(1+z^-1)/2` equals one there. This is a selected-channel transmission
zero inside a lossless faithful multiport, not state annihilation.

## Rosenbrock witness and tomography

A scalar realization of `h` is

`x_(k+1)=u_k`, `y_s,k=-(1/2)x_k+(1/2)u_k`.

Thus `A=0`, `B=1`, `C_s=-1/2`, `D_s=1/2`, and the Rosenbrock determinant is
`(lambda-1)/2`. At `lambda=1`, choose `x=u` nonzero: the selected output is
dark. The state is nevertheless controllable and observable because `B` and
`C_s` are nonzero.

Add the complementary row `C_c=1/2`, `D_c=1/2`. The complete instantaneous
map from `(x,u)` to `(y_s,y_c)` has determinant `-1/2` and is faithful. At the
selected zero it reports `y_c=u`, so tomography recovers the nonzero internal
trajectory without changing `y_s=0`.

## Passivity, reciprocity, and zero exclusion

Total unitarity proves energy balance for the complete scattering family.
Reciprocity compares exchanged ports in the declared common metric. Neither
property is a lower bound on one matrix entry.

At `z=1`, `h=0`, so its boundary real part is zero rather than strictly
positive. Its zero lies on the unit circle rather than strictly inside the
stable disk, so it is not strictly minimum phase. Choosing a phase after
inspecting `h`, dividing by `z-1`, or relabelling the complementary bright row
does not make the original selected channel zero-free.

A genuinely stronger source-native law would have to declare and derive a
collocated scalar port with strict positive-realness, an outer factor with a
bounded inverse, or another zero-exclusion certificate before inspecting the
selected scalar divisor. This apparatus supplies none of those constructors.
Consequently no optical condition stronger than reciprocity and total
passivity has been derived here.

## Detector kernel and smallest hostile

At zero phase, the selected row kills the nonzero symmetric delayed
trajectory while the complementary row detects it. The smallest hostile is
therefore the exact vector `(x,u)=(1,1)`: selected scalar zero, complementary
scalar one, positive internal/input norm, and invertible full detector family.

## Completion boundary

The witness is a finite discrete-time delay model. It does not establish an
analytic continuation, continuum scattering limit, half-plane outer
factorization, or source-native strictness law. Any such promotion requires
declared function spaces, analyticity domain, boundary values, inverse bound,
and phase calibration independent of the zero being tested.

Run `python research/aspect/checkers/selected_channel_transmission_zero.py`.
The result is
`research/aspect/results/selected_channel_transmission_zero.json`.
