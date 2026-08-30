# Causal dispersive magneto-optic response

Owner: `marici.Aspect`

## Bounded question

What is the smallest frequency-dependent completion of the earlier Faraday
Jones constructor that exposes causality, absorption, circular birefringence,
and the failure of a frequency-independent rotation law?

## Source authority and typed ports

Take one declared transverse laboratory Jones port.  The circular basis is
fixed by `e_+=(H+iV)/sqrt(2)` and `e_-=(H-iV)/sqrt(2)`.  The material response
is a deliberately minimal pair of scalar retarded susceptibilities

`chi_+(z)=1/(gamma-i(z-Omega))`,
`chi_-(z)=1/(gamma-i(z+Omega))`,

with positive damping `gamma` and real bias splitting `Omega`.  This is a
phenomenological response constructor, not a microscopic derivation of a
particular medium.

The frequency variable is a complex probe coordinate.  Both poles lie in the
lower half-plane, at `Omega-i gamma` and `-Omega-i gamma`, so the response is
analytic in the upper half-plane and is compatible with retarded propagation.

## Constructor order and frame

The ordered laboratory constructor is

`J(z)=C diag(t_+(z),t_-(z)) C^{-1}`,

where `C` is the fixed circular-to-linear calibration map.  Propagation laws
`t_+` and `t_-` must be formed before returning to the linear analyzer frame.
Swapping the circular labels reverses the reported Faraday angle; it is a
calibration change, not a new physical prediction.

For the exact checker, the thin-sample response is represented by
`t_sigma=1+i chi_sigma`.  This truncation is used only to expose the typed
frequency dependence algebraically.  It is not asserted to be an exactly
unitary finite-thickness transfer.

## Causality, dissipation, and symmetry

At real frequency `w`,

`Re chi_+(w)=gamma/(gamma^2+(w-Omega)^2)>0`.

With the declared Fourier convention this positive absorptive component is
the passive sign.  The bias-reversed circular channels obey

`chi_+(-w)=conjugate(chi_-(w))`.

This is the appropriate real-field conjugation condition.  It does not imply
same-bias reciprocity: the two circular eigenchannels remain split when
`Omega` is nonzero.

## Detector kernel and conserved quantities

A single fixed linear analyzer returns one scalar and therefore cannot recover
both complex circular transfers.  Two calibrated independent Jones analyzer
rows are faithful on the retained two-dimensional polarization port at a
fixed frequency.  They do not recover the environmental bath responsible for
damping, nor do finitely many frequency samples determine an unrestricted
causal transfer function.

The retained thin-sample Jones map is generally not norm preserving.  Damping
is a declared dissipative quantity and requires bath/noise ports for a quantum
unitary completion.  Causality alone does not supply that dilation.

## Smallest scalar-preserving hostile

At `gamma=1`, `Omega=1`, the response difference
`Delta(w)=chi_+(w)-chi_-(w)` is nonzero at `w=0` but takes a different value at
`w=2`.  A constant Faraday rotation calibrated at one frequency can therefore
preserve that scalar datum while failing at the second frequency.  The checker
records the exact nonzero residual.

Further hostiles are also explicit:

- moving a pole into the upper half-plane preserves a real-axis formula shape
  while destroying retarded causality;
- setting `Omega=0` erases circular splitting and hence the nonreciprocal
  polarization signal;
- discarding damping while continuing to claim absorption confuses a
  dispersive lossless limit with a passive lossy medium;
- one analyzer scalar remains nonfaithful on the Jones port.

## Completion gate

This packet does not derive oscillator strength, thickness exponentiation,
spatial dispersion, bath commutators, fluctuation-dissipation noise, or a
material-specific permeability/permittivity tensor.  A quantum optical device
model must add bath ports with commutators and noise fixed by the same loss
kernel; a broadband material claim must establish the full Kramers-Kronig
integrability and high-frequency asymptotics rather than infer them from two
samples.

Run
`python research/aspect/checkers/causal_dispersive_magneto_optic_response.py`.
The result is
`research/aspect/results/causal_dispersive_magneto_optic_response.json`.
