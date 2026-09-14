# The exchange-odd shape intervention constructs a primitive physical response

The canonical mixed residue is

\[
f=\frac1{b-x}+\frac1{a-y}.
\]

Apply the source-level shape intervention

\[
x\mapsto x+t,
\qquad
y\mapsto y-t,
\qquad z\mapsto z.
\]

It preserves total energy and has tangent

\[
D_{\rm shape}=\partial_x-\partial_y.
\]

Direct differentiation gives

\[
D_{\rm shape}f
=rac1{(b-x)^2}-\frac1{(a-y)^2}.
\]

Therefore the ordered doubled-wall principal-part covector is

\[
(1,-1).
\]

It is primitive and exchange-odd. This confirms C15b at the vector-valued response level: the source supplies a physical operation that distinguishes the two mixed occurrences.

The same antisymmetric covector on the simple mixed marked basis would map to

\[
\frac{1}{4xy}(e_2-e_4)
-rac{2}{4x^3y^3(x+y)}v_{\rm alg},
\]

and therefore has a nonzero candidate \(v_{\rm alg}\) projection.

One typed interface remains: reduce the doubled-wall principal-part module to the simple mixed basis \((g_{101},g_{110})\) through the Gauss--Manin/IBP relation and fix its integral Betti normalization. This interface converts the confirmed vector-valued physical response into a scalar \(v_{\rm alg}\) period detector.

Certificate:

- `research/voevodsky/checkers/construct_exchange_odd_physical_shape_response.py`;
- `research/voevodsky/results/exchange_odd_physical_shape_response.json`.
