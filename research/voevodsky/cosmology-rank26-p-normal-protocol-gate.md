# Rank-26 p-normal relation-module protocol gate

## Question

After the minimal \(\tau_p\) source routes fail, is there a distinct source-derived route that should replace further local residue probing?

## Claim boundary

This packet verifies the protocol for the reopened rank-26 relation-module route. It does not compute the full labelled rank-26 derivative matrix, construct a relative Bockstein, construct a global contour, or assign a physical period.

## Disposition

The minimal \(\tau_p\) routes are exhausted at the missing source-derived unit map. Mutable frontier state now opens a different route: use the complete labelled rank-26 Laurent/IBP relation module and differentiate its exact relations in a p-normal direction.

The source p-normal covector is

\[
(1,1,3).
\]

The proposed test point is

\[
(x,y,z)=(3,6,-3),
\]

so \(p=x+y+3z=0\) and total energy is \(6\). The two integral unit p-normals are

\[
n_x=(1,0,0),
\qquad
n_y=(0,1,0),
\]

with p-tangent difference

\[
n_x-n_y=(1,-1,0).
\]

They satisfy

\[
dp(n_x)=1,
\qquad
 dp(n_y)=1,
\qquad
 dp(n_x-n_y)=0.
\]

Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the span of \(n_x,n_y,n_x-n_y\) has rank \(2\), and the span of the p-normal covector with the tangent vector has rank \(2\).

The admissible protocol is:

1. evaluate the full labelled rank-26 relation matrix at \(p=0\);
2. differentiate source-generated relation rows along \(n_x\), without global division by \(p\);
3. reduce first derivatives modulo the special exact-relation image;
4. repeat along \(n_y\) and require equality modulo the p-tangent derived-relation span;
5. map any surviving line through the ordered wall-residue/exceptional-face total complex;
6. require primitive column \((1,1)\) up to sign, \(d^2=0\), Rees-shear invariance, and survival over two primes.

Restrictions: do not reuse the gamma-normal Bockstein vector, do not reuse the total-energy Rees class, do not identify cyclic Gysin charts with the internal three-wall Čech cover, do not use the \(c\) pivot as the p-normal, do not treat abstract \(\tau_p\) as source data, and do not invert the residue functor.

The next nonrepeat task is to obtain or construct the full labelled rank-26 relation matrix and implement this derivative-reduction protocol over two primes.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_protocol_gate.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_protocol_gate.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_protocol_gate.py`
