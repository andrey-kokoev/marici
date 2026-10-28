# External C0 has an explicit finite flux readout

Registered in net revision36 before execution:
`contracts/external-c0-finite-trace-attempt.v1.json`.

## Source and typing

The joint-graph analytical source distinguishes the compact physical analytic
core, the rank-two endpoint quotient, and the larger value/flux trace domain.
Its Volterra trace is `(0, integral q, integral_{-infinity}^a q, q(a))`.
The existing finite observer encoder already defines a candidate on five compact
physical packets, using two Mellin endpoints and three calibrated flux samples.

This attempt uses that FROZEN encoder. It does not identify the spatial point
`(-3,1,3,0)` with a logarithmic coordinate, Mellin endpoint or physical sample
site. Instead it represents the native coefficient labelled by that reference
as a functional on the admitted five-dimensional analytic packet.

## Exact result

With unchanged T and H, set

    L_a = B_a P_a H* T,
    D_a = T^-1 H P_a^-1 R_a.

All66 retained presentations decode exactly; all95 actual native interfaces
transport the encoder. The root encoder equals the previous encoder exactly.
All4 retained E histories still reproduce its two Mellin endpoint rows.

At neutron packet5 and electron packet15 the actual C0 row is

    e0^T R_5 L_5 = e0^T R_15 L_15 = (0,1,0,0,0).

In observation coordinates, ordered as two endpoints then the three flux samples,
this row is `(0,0,0,1,0)`. Hence for packet coefficients a,

    C0 = a_1 = A h(delta) = 2 A B_f(4),    delta=2 log2.

Here `f(x)=x^(-1/2) h(log x)`, `B_f=f` is the encoder's declared full-response
calibration, and A is its unchanged positive bump normalization. This result was
derived from the frozen matrices, not obtained by choosing a new complement.

For the previously declared weighted Volterra lifts
`q_sigma(u)=exp(sigma*u/2) h(u)`, the same scalar is `(A/2) q_plus(delta)` or
`2 A q_minus(delta)`: a calibrated flux coordinate of the source trace map.
This is a finite-domain coefficient/trace interpretation, not a new exterior
spatial-domain extension or a full mixed-polarization identification.

## Endpoint loss is concrete

The compact packet `(2,-5,2,0,0)` has both Mellin endpoints zero but C0=-5.
The packet `(0,2,-5,2,0)` also has zero endpoints but C0=2. Thus C0 cannot be
recovered from the two endpoints alone. Dropping the retained complement loses
an explicitly represented reference coefficient, even though endpoint matching
continues to pass.

109 checks pass, including95 individual native interface checks. The full trace
rows and counterexamples are in `results/external-c0-finite-trace/trace.json`.

## Remaining attachment

This supplies a finite analytical readout for the external coefficient, not an
actual esd7 triangle homotopy. Next identify the geometric shared face of native
NE5->15 in the authoritative fine-face registry and its incident presentation
roles. A native transfer across a shared face is not itself that face's triangular
analytical filler. Bind the intended residual/witness in those presentations;
do not choose F006 merely because an earlier generic gate used that label.

No full-observer extension, unique encoder, physical preparation, Pb construction
or114-record producer follows. The external spatial reference remains outside
the carrier and its reference-only primitive remains unoccupied.

## Reproduce

```sh
python research/strominger/checkers/check_external_c0_finite_trace.py
```

The receipt checks live attachment, encoder and field-sewing provenance. Its
matrix verification is exact; compact-packet endpoint/flux identities retain
the analytical justification and declared calibration of the original encoder.
