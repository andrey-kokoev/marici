# The Pick condition is angular monotonicity around the quarter point

Define

\[
 X(t)=\Xi\!\left(\frac12+\sqrt t\right),\qquad
 \ell(t)=\log X(t),\qquad
 F(t)=(4t-1)\ell'(t).
\]

Write an upper-half-plane point in polar coordinates about the quarter point:

\[
 t=\frac14+r e^{i\theta},\qquad r>0,\quad 0<\theta<\pi.
\]

Away from a zero of `X`, differentiation along the circle gives

\[
 \partial_\theta\log|X(t)|
 =\operatorname{Re}\!\left(i(t-\tfrac14)\ell'(t)\right)
 =-\operatorname{Im}\!\left((t-\tfrac14)\ell'(t)\right).
\]

Since `F(t)=4(t-1/4)ell'(t)`, this is the exact identity

\[
 \boxed{\operatorname{Im}F(t)
 =-4\,\partial_\theta\log|X(t)|.}                       \tag{1}
\]

Consequently the global Pick condition is equivalent to

\[
 \boxed{\theta\longmapsto
 |X(\tfrac14+r e^{i\theta})|\text{ is nonincreasing on }(0,\pi)}             \tag{2}
\]

for every radius, with zeros handled by the corresponding limiting statement.

## Why RH predicts exactly this geometry

Under the Stieltjes/RH factorization, an individual squared-zero factor has
the form `1+t/lambda` with `lambda>=0`. On a quarter-centered circle,

\[
 \left|1+\frac{t}{\lambda}\right|^2
 =\left(1+\frac{1}{4\lambda}\right)^2
  +\frac{r^2}{\lambda^2}
  +\frac{2r}{\lambda}\left(1+\frac{1}{4\lambda}\right)\cos\theta.
\]

Its derivative with respect to `theta` is nonpositive. Products and convergent
regularized limits preserve logarithmic angular monotonicity. Thus (2) is the
geometric shadow of putting every squared zero on the nonnegative spectral
axis.

## Explanatory value

This replaces an infinite family of matrix inequalities by one visual law:
completed Xi loses modulus while rotating from the positive ray toward the
negative ray around the forced quarter point. It also gives a direct hostile
falsifier: one radius and two angles with a strict modulus increase disprove
the universal Pick conjecture.

## The endpoint comparison is an unconditional theta theorem

Theta positivity already proves the total comparison between the two ends of
every semicircle:

\[
 \left|X(\tfrac14-r)\right|\le X(\tfrac14+r).           \tag{3}
\]

If `0<r<=1/4`, both arguments are nonnegative. Writing
`X(t)=B(sqrt(t))` with

\[
 B(q)=\int_0^\infty\Phi(u)\cosh(qu)\,du,
\]

the inequality follows because `B` is increasing for real `q>=0`.

If `r>1/4`, put `q=sqrt(r-1/4)` and `p=sqrt(r+1/4)`. Then

\[
 |X(\tfrac14-r)|
 =\left|\int\Phi(u)\cos(qu)\,du\right|
 \le\int\Phi(u)\,du
 \le\int\Phi(u)\cosh(pu)\,du
 =X(\tfrac14+r).
\]

Thus the source proves the net angular loss without RH. The open content is
strictly stronger: exclude an interior rebound of the modulus along the arc.
Endpoint estimates alone cannot do that.

## Every arc also has an unconditional decreasing envelope

Let `z(theta)=a(theta)+ib(theta)=sqrt(1/4+r exp(i theta))` on the principal
branch. The real part `a(theta)` is nonincreasing: both
`Re(t)=1/4+r cos(theta)` and `|t|` are nonincreasing on the upper semicircle,
and

\[
 a(\theta)^2=\frac{|t|+\operatorname{Re}t}{2}.
\]

Positivity of the theta density gives

\[
 |B(a+ib)|
 \le\int\Phi(u)|\cosh((a+ib)u)|\,du
 \le\int\Phi(u)\cosh(au)\,du=B(a),                    \tag{4}
\]

because `|cosh(a+ib)|<=cosh(a)`. Since `B(a)` increases with `a`, every point
of the arc obeys

\[
 |X(\tfrac14+r e^{i\theta})|
 \le B(a(\theta))
 \le B(a(0))=X(\tfrac14+r).                            \tag{5}
\]

So an RH violation cannot appear as an overshoot above the initial modulus.
It must be an interior rebound below this decreasing theta envelope.

This can be stated probabilistically. Extend `Phi` evenly and let `nu_a` be
its exponential tilt. Then

\[
 \frac{B(a+ib)}{B(a)}
 =\mathbb E_{\nu_a}e^{ibU}=:\chi_a(b),
\]

and hence

\[
 \log|B(a+ib)|=\log B(a)+\log|\chi_a(b)|.              \tag{6}
\]

The first term is a decreasing envelope along the arc. The second is a
nonpositive phase-coherence deficit. The remaining RH-equivalent assertion is
that this deficit can never relax rapidly enough to overpower the envelope
loss. This identifies a narrower source target than raw theta positivity: a
two-parameter contraction inequality for tilted characteristic functions.

## Maximum-principle warning

`Im F` is harmonic only where `X` has no zero. Applying a minimum principle to
deduce its sign in the upper half-plane would therefore require excluding the
very off-axis zeros that the argument is intended to exclude. Any such proof
must either handle logarithmic singularities directly or establish a
source-side positive representation first; silently assuming a zero-free
domain is circular.

The identity is unconditional. Proving angular monotonicity for every radius
is still the RH-equivalent step, so RH is not proved. The source-side research
question is whether the theta modular equation supplies a rotation-comparison
principle for this modulus without invoking its zero divisor.

## Durable verification

- Checker: `checkers/quarter_centered_angular_modulus_pick_equivalence.py`
- Result: `results/quarter-centered-angular-modulus-pick-equivalence.json`
