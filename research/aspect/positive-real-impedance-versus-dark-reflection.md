# Positive-real impedance versus dark reflection

Owner: `marici.Aspect`

## Bounded question

Does strict positive-realness of a source impedance forbid an off-seam zero
of the reflection coefficient obtained from it by a Cayley transform?  No.
This packet audits the optical port typing of
`research/nima/theta-positive-real-impedance-can-have-an-off-seam-dark-scattering-zero.md`.

## Source authority and typed ports

Let `a>0` be fixed before inspecting any zero.  In the right half-plane use
the normalized driving-point impedance

`Z_a(s)=s/a`

and the reflection readout relative to the unit reference impedance

`h_a(s)=(Z_a(s)-1)/(Z_a(s)+1)=(s-a)/(s+a)`.

These are not two names for one port quantity.  `Z_a` is an effort/flow ratio
at the collocated driving port.  `h_a` is the outgoing-to-incoming wave ratio
after a reference impedance and Cayley convention have been declared.  Strict
positivity of `Re Z_a` transports through Cayley to the Schur bound
`|h_a|<1` in the open right half-plane; it does not transport to `h_a!=0`.

## Exact classification

For `s=x+iy` with `x>0`, `Re Z_a=x/a>0`.  Yet `h_a(a)=0`, while its only pole
is at `s=-a`.  The reciprocal sewing law

`h_a(-conjugate(s))=1/conjugate(h_a(s))`

pairs the right-half-plane zero with the left-half-plane pole.  On the
physical frequency seam `s=i omega`, `|h_a|=1`.

A one-state realization is

`A=-a, B=1, C=-2a, D=1`.

Its transfer is `D+C(s-A)^-1 B=(s-a)/(s+a)`.  The Rosenbrock determinant is
`s-a`, so the selected reflection row loses rank at `s=a`, even though the
one-state pair is both controllable and observable.

## Physical interpretation boundary

The algebraic zero is decisive against analytic zero exclusion, but its
off-seam location matters.  With the Laplace convention used here, `s=a` is
not a real-frequency monochromatic operating point.  It is an analytic
continuation or exponential-probe zero.  Therefore the scalar witness alone
does not authorize the stronger laboratory sentence that physical energy at
that point exits through a complementary port.

Indeed, on the physical seam this one-port response has unit reflection
magnitude.  A literal complementary output requires an explicitly declared
multiport dilation and an on-shell input.  The earlier two-path packet supplies
such a bright complementary row at its boundary zero; this half-plane witness
does not.  Calling the off-seam zero “perfect matching” is legitimate as an
analytic impedance equality `Z_a(a)=1`, but not by itself as a measured
steady-frequency absorption or transmission event.

## Constructor order and calibration frame

The order is source impedance, fixed reference-impedance normalization,
Cayley transform, then selected reflection readout.  Changing the reference
impedance after seeing a zero changes the readout constructor.  Replacing
reflection by impedance after applying positivity changes the codomain and
cannot prove the original scalar nonzero.

## Detector kernel and hostile

At `s=a`, choose state `x=1` and input `u=2a`.  The Rosenbrock equations hold
and the selected output is zero although both state and input are nonzero.
This is the smallest exact hostile to the inference

`strictly positive-real impedance => nonvanishing reflection coefficient`.

The checker also rejects the converse typing error: seam losslessness of the
reflection row is not strict positive-realness of that same scalar row.

## Conserved and dissipated quantities

Boundary magnitude one certifies conservation for the declared scalar
one-port scattering boundary values.  The open-half-plane inequality is an
analytic passivity certificate.  Neither certifies a complementary power
flux at an off-seam complex probe.  No absorption or bath port is present in
this witness.

## Completion gate

The audit does not canonically type any RH or theta scalar as a driving-point
impedance.  Such a claim needs source-derived effort and flow variables,
reference-impedance authority, an analytic domain, and proof that the target
scalar is `Z` rather than its reflection, transmission, overlap, determinant,
or selected minor.  It also does not construct a conservative multiport
dilation for off-seam exponential probes.

Run `python research/aspect/checkers/positive_real_impedance_versus_dark_reflection.py`.
The result is
`research/aspect/results/positive_real_impedance_versus_dark_reflection.json`.
