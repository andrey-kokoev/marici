# A graded history port detects all-order normalization erasure

## Exact flattened scalar

Center the spectral parameter as `z=s-1/2`.  Let the finite transition carry
two labelled odd histories,

`L_primitive(z)=a z`,

`L_square(z)=b z^3`,

and put

`L(z)=L_primitive(z)+L_square(z)`.

The raw scalar transition is

`gamma(z)=exp(L(z))`.

The all-order counterterm

`rho(z)=exp(-L(z))`

produces

`Gamma(z)=rho(z)gamma(z)=1`.

Every central derivative of the normalized scalar vanishes.  The primitive
and square constructor histories remain nonzero in the attached packet.

## Classifier result

The correct labels are:

- scalar flat: true;
- packet zero: false when either labelled history is nonzero;
- normalization erasure: true;
- lossless reconstruction: true when the history port is retained;
- arithmetic provenance retained: true only when the history remains graded.

Calling this a trivial transition from the scalar output alone confuses
successful cancellation with absence of source action.

## Aggregated history is not always enough

For scalar reconstruction, the single function `L` suffices.  For labelled
incidence, it may not.  If primitive and square channels contribute to the
same scalar basis function, then

`L_primitive=a z`, `L_square=b z`

has aggregate `(a+b)z`.  The redistribution

`(a,b)->(a+t,b-t)`

leaves every scalar output unchanged while changing the labelled currents.
Thus the apparatus must retain grade labels whenever downstream Schur jets or
prime-square countercurrents use them separately.

## Optical implementation

Apply equal and opposite programmed log-gain/phase controls so the selected
scalar transfer is flat.  Record, independently:

- primitive-labelled control history;
- square-labelled control history;
- affine Duhamel displacement;
- the final scalar amplitude.

The expected normalization-erasure signature is a flat scalar with nonzero
history norm.  Removing the history record deliberately converts the same run
into an unreconstructible packet.

This port joins the existing dark-event classifier as the fourth analytic
axis, alongside transmission-zero, incidence-alias, and packet-zero labels.
Strominger's path/coefficient audit remains a separate constructibility axis.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_graded_history_normalization_erasure.py
```
