# The exchange-odd shape response does not recover v_alg by differentiation

## Question

Can the existing exchange-odd shape intervention turn the canonical symmetric mixed residue into the missing scalar \(v_{\rm alg}\) detector?

## Claim boundary

This packet tests the route through the currently printed marked algebraic extension. It does not exclude a different sourced logarithmic mixed observable.

## Exact cancellation as a function

The two marked mixed generators have \(v_{\rm alg}\) coefficients

\[
c_{101}(x,y)=-\frac{1}{4x^3y^3(x+y)},
\qquad
c_{110}(x,y)=+\frac{1}{4x^3y^3(x+y)}.
\]

The canonical physical mixed residue has coefficient vector \((1,1)\). Its \(v_{\rm alg}\) projection is therefore the identically zero rational function

\[
c_{101}+c_{110}=0.
\]

For the total-energy-preserving shape path

\[
x\mapsto x+t,
\qquad
y\mapsto y-t,
\]

the cancellation remains exact for every \(t\) away from the pole locus. Consequently

\[
\frac{d^n}{dt^n}
\left(c_{101}(x+t,y-t)+c_{110}(x+t,y-t)ight)_{t=0}=0
\]

for every derivative order \(n\).

## Character accounting

The first derivative of the simple symmetric pole expression is an antisymmetric doubled-pole response. This is a real, primitive vector-valued response, but its parity includes the odd tangent character. Forgetting that character and reinterpreting the doubled-pole coefficient vector as the simple-pole vector \((1,-1)\) is not a valid comparison.

The actual derivative comparison sends

\[
s_+\longmapsto p_-,
\qquad
s_-\longmapsto p_+.
\]

Hence the constructed \(p_-\) remains attached to the symmetric simple input \(s_+\), whose \(v_{\rm alg}\) projection and all shape derivatives vanish.

## Disposition

The exchange-odd shape intervention confirms that the ordered physical response retains information erased by scalar synthesis. It does not, through the existing marked extension, furnish the missing scalar \(v_{\rm alg}\) tomography channel. That channel still requires a sourced antisymmetric simple mixed observable, or a different readout defined directly on the doubled-pole module with an independently derived comparison to \(v_{\rm alg}\).

Verification:

- `research/voevodsky/checkers/check_shape_derivative_v_alg_no_go.py`
- `research/voevodsky/results/shape_derivative_v_alg_no_go.json`
