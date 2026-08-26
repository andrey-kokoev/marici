# D4 score versus portal tangent

Work package: WP586  
Owner: marici.Figueiredo

## Question

WP572 makes the leading-order partial derivative with respect to the public
generator coordinate \(D_4\) executable. WP585 requires a primitive kernel
with nonzero response along the physical portal coordinate \(q\). This packet
tests whether the \(D_4\) partial derivative already has that authority.

It does not. The portal source generally transports correlated changes in
\(D_3\), top-contact coefficients, widths, branching fractions, and
heavy-state amplitudes. A partial derivative in one generator coordinate is
not the derivative along that correlated physical path.

## Exact ambiguity

The smallest affine event amplitude carrying the issue is

\[
M(c,d)=a+cb+de,
\]

where \(c=D_4\) and \(d\) represents one omitted correlated generator
coordinate. For the event weight \(w=M^2\), a portal completion with

\[
{dc\over dq}=1,\qquad {dd\over dq}=\alpha
\]

has derivative

\[
{dw\over dq}={\partial w\over\partial c}
+\alpha{\partial w\over\partial d}.
\]

The public \(D_4\) score supplies only the first term. The coefficient
\(\alpha\) must be derived from the portal source; it cannot be fitted from
the desired detector response.

At the rational hostile amplitude \(M=1+c+d\), evaluated at \(c=d=0\),
the \(D_4\)-only derivative is two. The completion \(\alpha=1\) gives
four, while \(\alpha=-1\) gives zero. Both completions retain
\(dc/dq=1\). Thus even nonzero \(D_4\) sensitivity does not prove nonzero
portal sensitivity.

## Typing and descent

The ambiguity is among physical generator couplings, so weak-basis descent is
not the obstruction. No reference port is involved. The first undefined arrow
is the source-derived tangent from the portal domain into the complete
generator-coordinate family.

The \(D_4\) operation remains an executable source partial derivative. It is
neither a selector nor a rigidifier and is not a portal detector instrument.

## Required repair

Before shower or detector transport, derive the full tangent in

\[
(D_3,D_4,CT_1,CT_2,CT_3,\Gamma,B,A_H),
\]

where \(\Gamma\), \(B\), and \(A_H\) denote the required widths,
branching fractions, and heavy-state amplitudes. Common-support event
derivatives must then be combined by that frozen tangent. Only the resulting
signed measure is eligible for detector calibration and a rank test.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp586_d4_score_portal_tangent_ambiguity.py

The generated result is
research/flavor/results/wp586_d4_score_portal_tangent_ambiguity.json.
