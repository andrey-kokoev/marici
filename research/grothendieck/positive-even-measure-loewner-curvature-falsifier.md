# Positive even source measure does not force Loewner positivity

The proposed route from the theta representation to a self-adjoint spectral
operator cannot use only positivity and evenness of its source measure. There
is an exact four-atom counterexample.

Let `X` have the symmetric probability law

\[
 \Pr(X=1)=\Pr(X=-1)=\frac25,\qquad
 \Pr(X=3)=\Pr(X=-3)=\frac1{10}.
\]

Write its cumulant generating function as

\[
 \ell(t)=\log \mathbb E[e^{\sqrt t X}]
 =\frac{\kappa_2}{2}t+\frac{\kappa_4}{24}t^2
  +\frac{\kappa_6}{720}t^3+\frac{\kappa_8}{40320}t^4+O(t^5),
\]

and form the same boundary source used in the Xi program,
`F(t)=(4t-1)ell'(t)`. Exact arithmetic gives

\[
 (\kappa_2,\kappa_4,\kappa_6,\kappa_8)
 =\left(\frac{13}{5},-\frac{82}{25},\frac{272}{25},\frac{304}{125}\right)
\]

and

\[
 F'(0)=\frac{821}{150}>0,\qquad
 F''(0)=-\frac{854}{375},\qquad
 F'''(0)=\frac{14261}{13125}.
\]

Nevertheless the first nontrivial diagonal Loewner condition fails:

\[
 2F'(0)F'''(0)-3F''(0)^2
 =-\frac{721471}{196875}<0.
\]

Equivalently,

\[
 \frac{F'(0)F'''(0)}6-\frac{F''(0)^2}{4}<0.
\]

## Meaning for the RH program

This kills a tempting universal explanation: a positive even theta-type
measure does not automatically make the derived boundary operator
self-adjoint or its Loewner matrices positive. The actual Xi source may still
have the required positivity, but a proof must use additional arithmetic or
transform structure.

The sharp candidate exposed by the comparison is **Stieltjes order two**:

\[
 F'(x)=\int_0^\infty \frac{d\rho(\lambda)}{(x+\lambda)^2},
 \qquad d\rho\ge0.
\]

That representation forces the curvature by a covariance-square identity.
It is far stronger than positivity, evenness, or complete monotonicity of an
upstream measure. The next attack is therefore to derive or falsify this
order-two Stieltjes property directly from the completed Xi source, without
assuming the zero locations it is meant to prove.

This counterexample does not concern the actual Xi measure and does not prove
or disprove RH.

## Durable verification

- Checker: `checkers/positive_even_measure_loewner_curvature_falsifier.py`
- Result: `results/positive-even-measure-loewner-curvature-falsifier.json`
