# Scope correction: the Green residual is an autocorrelation separation port

## Correction

The earlier version of this packet incorrectly called the signed Green
residual an independent oriented-order port. The algebra disproves that claim:

\[
\operatorname{sgn}(x)\sinh(zx)=\sinh(z|x|).
\]

Hence

\[
K_f(z)=\iint f(q)f(v)\sinh\!\bigl(z|v-q|\bigr)\,dq\,dv.
\]

If

\[
A_f(x)=\int_0^\infty f(q)f(q+x)\,dq,
\qquad x\geq0,
\]

then

\[
K_f(z)=2\int_0^\infty A_f(x)\sinh(zx)\,dx.
\]

The kernel is exchange-even. The full one-sided autocorrelation reconstructs
it exactly. It can remain absent from a compressed curvature scalar, but it is
not independent of the full autocorrelation packet and does not remember
which source point came first.

## What survives

For a nonzero positive source, \(K_f(\sigma)\) has the sign of real
\(\sigma\). Complex oscillation can still reverse this real-axis orientation.
This makes the port a useful separation diagnostic, not a new order channel.

The explicit three-atom hostile in the successor packet shows that even this
positive separation transform can have off-seam complex zeros.

## Actual exchange-odd candidate

A genuine orientation port requires two independently typed histories. The
minimal candidate is

\[
L_{f,g}(z)=\iint f(q)g(v)\sinh\!\bigl(z(v-q)\bigr)\,dq\,dv.
\]

It obeys

\[
L_{g,f}(z)=-L_{f,g}(z),
\qquad
L_{f,f}(z)=0.
\]

This candidate is admissible only if \(f\) and \(g\) arise independently from
the theta construction. Introducing a second history merely to obtain
antisymmetry would be fitted structure.

## Revised target

Identify the two typed histories already present in the reciprocal Green
system, derive their exchange involution and modular transport before scalar
compression, and test whether \(L_{f,g}\) is nonzero. Separate marginal
histories do not determine their cross-correlation without an additional
coupling law.
# The Green residual is the oriented order port of the source pair

## Ordered forcing

For a positive half-line source (f), the doubled Green residual is

\[
\mathcal K(z)
=2\int_{0\leq q<v}
f(q)f(v)\sinh(z(v-q)),dq,dv.
\]

Introduce the order sign

\[
\varepsilon(q,v)=\operatorname{sgn}(v-q).
\]

Because both (arepsilon(q,v)) and
(sinh(z(v-q))) reverse sign under (q\leftrightarrow v), their product is
swap-even. Therefore

\[
\mathcal K(z)
=\int_0^\infty\int_0^\infty
f(q)f(v)\varepsilon(q,v)
\sinh(z(v-q)),dq,dv.
\]

This is the full two-source expectation with one explicit orientation
operator inserted.

## Unordered autocorrelation loses this port

Without the order sign, the full-plane odd separation transform vanishes:

\[
\int\!\!\int
f(q)f(v)\sinh(z(v-q)),dq,dv=0.
\]

The ordinary source-adjoint product retains only swap-even, unordered
autocorrelation data. It cannot reconstruct which member of a source pair came
first.

Thus the Green residual is not an algebraic shadow of the scalar transform or
of the self-adjoint autocorrelation face. It is the first genuinely new
relational port after static saturation: an oriented order coordinate.

## Real-axis orientation

For real (z=\sigma), positivity of (f) gives

\[
\operatorname{sgn}\mathcal K(\sigma)
=\operatorname{sgn}\sigma
\]

whenever the source is nontrivial, because every integrand on (q<v) has that
sign. Complex spectral transport introduces
(cos(\operatorname{Im}z,(v-q))), and this destroys automatic orientation.

This exactly locates the unresolved information: the source order port is
positive before oscillatory character compression but may reverse afterward.

## Zero-fiber independence

A scalar zero constrains the codiagonal value channel. It does not erase the
order sign or force (mathcal K(z)=0). Therefore the moving-window identity
is a genuine higher relation, but it remains diagnostic rather than
confining until modular sewing links scalar nullity to the oriented pair port.

## Revised target

The RH-bearing law must act on the ordered source-pair object before
oscillatory compression. It must explain why, on a completed scalar zero
state, reciprocal modular transport cannot reverse the sign selected by
(arepsilon(q,v)) away from the seam.

Any construction using only the unordered autocorrelation measure or the
scalar codiagonal has already discarded the required orientation.

## Falsifier

A positive reciprocal source with the same scalar completion law but an
off-seam zero and oppositely oriented order port disproves any claimed
universal implication. The law must use structure specific to the integer
theta source, not positivity of (f\otimes f) alone.
