# Global PN candidate and a two-channel electron return interface

## Global 36-component PN map

Constructed an explicit map S from the native P field to the native N field.
It is not restricted to the shared face. The construction uses each source's
exact metric, the previously derived grid, and its native return-column phases.

In metric-normalized, phase-adjusted coordinates, the two projector pairs have
real tensor forms. Their selected factor vectors have entries equal to square
roots of the native row/column probabilities. Two real orthogonal maps send
P's factor vectors to N's, one in dimension 12 and one in dimension 3.

An ordered sequence of plane rotations defines each map exactly. Undoing the
metric and phase coordinate changes gives the full 36-by-36 S. All native
operator coefficients are checked against the tensor forms, and exact factor
identities establish

```
S* M_N S = M_P
S L_P = G_N S
S G_P = L_N S
S N_P = N_N S.
```

The receipt contains the full matrix in exact multiradical arithmetic. This is
a global metric-unitary algebraic candidate and necessarily couples beyond the
previous six-component boundary block. It does not preserve that block as an
isolated face-to-face map.

The ordered rotations choose one extension on complementary modes; the source
does not uniquely prescribe that choice. In particular this map is not yet
bound to the native five-slot PN action or the observed whole-path five-cycle.
The earlier fixed-alignment holonomy obstruction is not removed merely by
constructing a globally valid pair isometry.

## Two independent baryon returns can feed the full E return image

Let u be the metric-normalized native N return vector. Take two independent
copies, giving a two-dimensional return sector inside a 72-coordinate direct
sum. Let J be the native eight-by-two electron return frame obtained by
stacking its four face projectors and dividing by sqrt(2). Then

```
J*J=I_2,  JJ*=N_E.
```

Read the two source amplitudes using u's metric adjoint, and apply J. The
resulting explicit 8-by-72 map S_E satisfies

```
S_E S_Esharp = N_E
S_Esharp S_E = diag(N_N,N_N).
```

It preserves the norm of the two source return amplitudes and reaches both
native E return directions. It discards the 70-dimensional source complement;
it does not populate E's six-dimensional raw complement. This is a return-sector
partial isometry, not a surjective full-field NE transfer.

## Two frames are not automatically two physical input modes

Tested the two contact-witnessed native histories with relative five-cycle H.
For the geometric P candidate, a fixed return readout ell and ell H have overlap
3/4 and Gram determinant 7/16: they would be independent readouts if held fixed
in that interpretation.

But if H is a coordinate-frame change, the readout must transform as ell H^-1
while the state transforms as Hx. Their composition is still ell x. They then
represent only one physical channel.

Consequently the two-input electron construction cannot be justified merely by
counting two frame-related histories. It needs two genuinely independent
incoming responses, or a justified interaction law under which their readouts
are physically different. That source selection remains open.

## Verification and remaining gates

```sh
python research/strominger/checkers/construct_global_PN_transport.py
python research/strominger/checkers/check_two_channel_electron_interface.py
```

Evidence: `results/global-PN-transport/verification.json` and
`results/two-channel-electron-interface/verification.json`.

These are explicit algebraic connections, not yet a physical PN/NE law. The
remaining requirements are the native five-slot binding, the physical source
of the second E input, and consistent whole-path sewing. Production/viewer
unchanged.
