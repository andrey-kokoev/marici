# No holomorphic scalar port is dagger-faithful on a two-prime packet

## Linear no-go theorem

Let a two-prime packet be `v=(v_2,v_3)` with dagger norm

`||v||^2=|v_2|^2+|v_3|^2`.

Any complex-linear scalar readout has the form

`ell(v)=a v_2+b v_3`.

Its kernel contains the nonzero vector `(b,-a)`.  Equivalently, the pulled-back
power form `ell^*ell` has rank at most one, whereas the faithful packet metric
has rank two.  Therefore no scalar linear port can satisfy

`ell(v)=0 if and only if v=0`

on the full packet space.

Dagger compatibility does not repair the defect.  It can restrict `a,b` to a
real locus or relate them under reciprocal conjugation, but a one-dimensional
kernel remains.

## Application to the two-prime hostile

At the off-seam root of `H_2+H_3`, the packet is proportional to `(1,-1)`.
The equal-gain codiagonal kills it, while the dagger norm remains positive.
This is exactly the unavoidable rank-one kernel, realized by the arithmetic
source curve.

The result changes the RH target.  Faithfulness of the scalar completed
section is impossible as a property of the ambient prime packet.  What can be
true is the narrower source statement

`H(z) not in ker ell for every off-seam z`.

That is a kernel-avoidance or transversality theorem for one distinguished
holomorphic source curve.  It cannot follow from detector rank, dagger
compatibility, or positivity alone.

## Additive current does not evade the no-go

The source-native endpoint ledger is additive.  A current-to-line character

`chi_kappa(Y)=exp(kappa Y)`

is multiplicative and never zero.  It can transport the current into a
determinant line, but it cannot create a divisor.  Zeros arise only after two
or more such nonzero line amplitudes are added or subtracted, reintroducing a
codiagonal kernel.

Thus the free character scale and the scalar-faithfulness defect are distinct:

- choosing `kappa` fixes current-to-line units;
- proving RH-type confinement requires the resulting source curve to avoid
  the scalar interference kernel off the dagger fixed locus.

## Minimal instrument

A faithful linear monitor for two complex prime channels needs at least two
complex outputs.  The smallest useful optical arrangement is therefore:

- one coherent scalar port carrying the candidate completed section;
- two-channel tomography, or an equivalent full-rank pair of monitors;
- one dagger power comparison to identify false dark ports.

Whenever the scalar port is dark and the packet monitor is bright, the event
is a cancellation zero rather than a packet zero.  This does not disqualify a
physical xi zero; it identifies the precise kernel the source law must
control.

## Verification

```text
uv run --with sympy --with mpmath python research/aspect/checkers/check_scalar_dagger_faithfulness_no_go.py
```
