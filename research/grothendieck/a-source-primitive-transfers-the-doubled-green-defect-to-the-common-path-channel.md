# A source primitive transfers the doubled Green defect to the common path channel

## Provenance correction

The full complex primitive-current calculation was already established in
[Theta primitive seam current leaves an explicit mixed bulk residual](theta-primitive-seam-current-leaves-an-explicit-mixed-bulk-residual.md).
The calculation below is its real specialization. Its new contribution is the
identification of the surviving common-mode residual with the independently
found endpoint-to-path lifting obstruction; it is not a second independent
derivation of a new residual.

## Reciprocal doubled flow

Use a real centered spectral coordinate `z` and the reciprocal pair

\[
u'=-zu-cf,
\qquad
v'=+zv-cf,
\qquad
c'=0.
\]

The opposite signs are the local algebraic shadow of the two open sectors.
Direct differentiation gives

\[
(u^2-v^2)'
=-2z(u^2+v^2)-2cf(u-v).
\]

Thus the desired positive bulk appears without assumption:

\[
2z(u^2+v^2)
=-(u^2-v^2)'-2cf(u-v).
\]

The entire obstruction is the relative forcing channel `2cf(u-v)`.

## Minimal source-primitive lift

Adjoin the actual source primitive

\[
h'=f.
\]

This is the differential form of retaining the moving seam window. Define

\[
J_{\rm p}=2hc(u-v).
\]

Because the forcing cancels in the derivative of `u-v`,

\[
(u-v)'=-z(u+v),
\]

and therefore

\[
J_{\rm p}'
=2cf(u-v)-2zhc(u+v).
\]

Substitution into the doubled Green identity yields

\[
2z(u^2+v^2)
=-\bigl(u^2-v^2+J_{\rm p}\bigr)'
-2zhc(u+v).
\]

The primitive seam coordinate absorbs the forcing exactly, but leaves one
common-path residual.

## Meaning

The defect has not proliferated arbitrarily. It has moved one rung upward:

```text
relative forcing f(u-v)
    -> source primitive h
    -> common-path residual h(u+v)
```

If the common path vanished pointwise, `u+v=0`, the current would close and
the positive bulk would force `z=0` under vanishing endpoint flux. But scalar
Evans nullity supplies only a terminal common-mode condition. It does not
imply `u(q)+v(q)=0` for every `q`.

Thus the conservation calculation has recovered the previously identified
endpoint-to-path lifting problem rather than bypassing it.

## Exact conditional closure

Suppose a nonzero admissible state satisfies:

- `u+v=0` throughout the interval;
- the completed current `u^2-v^2+J_p` has equal endpoint values;
- the integral of `u^2+v^2` is finite and positive.

Then integration gives

\[
2z\int(u^2+v^2)=0,
\]

and hence `z=0`. The algebraic zero-confinement implication is therefore
complete conditional on the pointwise common-path lift and endpoint closure.

## Hostile boundary

Terminal equality `u(0)+v(0)=0` does not imply path equality. For example,
one may choose nonzero initial derivatives whose sum is not zero. The doubled
flow itself gives

\[
(u+v)'=-z(u-v)-2cf,
\]

so preservation of `u+v=0` requires the additional source constraint

\[
z(u-v)+2cf=0
\]

at every scale. This is not a consequence of terminal scalar nullity.

## Next theorem-shaped gate

The missing relation is now explicit: derive, from Fourier--Tate modular
sewing, either pointwise common-path cancellation or an additional current
whose derivative is `2zhc(u+v)`. A formal antiderivative is inadmissible.

This is a substantially narrower target than arbitrary boundary positivity:
the source must control one common-path residual created by the canonical
primitive lift.
