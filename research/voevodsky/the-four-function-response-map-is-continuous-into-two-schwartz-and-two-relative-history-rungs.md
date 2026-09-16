# The four-function response map is continuous into two Schwartz and two relative-history rungs

## Question

Is the topology used for the function-valued fourth presentation independently justified, or merely transported from the source?

## Claim boundary

It is independently realized by standard Schwartz and weighted relative-history spaces. The value and Fourier-value channels are Schwartz; the causal and principal-value channels have Schwartz derivatives and finite endpoint limits. This proves continuity and endpoint formulas on the Schwartz core.

## Schwartz channels

For \(g\in\mathcal S(\mathbb R)\),

$$
B_g(a)=g(a),
\qquad
Q_g(a)=\widehat g(a)
$$

belong to \(\mathcal S(\mathbb R)\), and both maps are continuous in the Schwartz topology.

## Causal-history channel

The function

$$
A_g(a)=\int_{-\infty}^ag(x)\,dx
$$

satisfies

$$
A_g'=B_g,
\qquad
A_g''=B_g',
$$

and

$$
A_g(-\infty)=0,
\qquad
A_g(+\infty)=Q_g(0)=\int g.
$$

Hence \(A_g\) belongs continuously to every polynomially weighted second-order relative-history graph admitted for Schwartz derivatives.

## Principal-value channel

Define

$$
C_g(a)=\operatorname{pv}\int_{\mathbb R}
\frac{e^{-2\pi iax}g(x)}x\,dx.
$$

Differentiation removes the singular denominator:

$$
C_g'(a)=-2\pi iQ_g(a),
qquad
C_g''(a)=-2\pi iQ_g'(a).
$$

Thus its first two derivatives are Schwartz. Using

$$
\mathcal F\left(\operatorname{pv}\frac1x\right)(a)
=-i\pi\operatorname{sgn}(a)
$$

with the declared Fourier convention, decomposition of \(g(x)=g(0)+x h(x)\) near zero gives the endpoint limits

$$
C_g(-\infty)=+i\pi g(0),
\qquad
C_g(+\infty)=-i\pi g(0).
$$

Their difference agrees with integration of the derivative:

$$
C_g(+\infty)-C_g(-\infty)
=-2\pi i\int Q_g(a)\,da
=-2\pi i g(0).
$$

Therefore \(C_g\) belongs continuously to the same kind of weighted second-order relative-history graph as \(A_g\).

## Intrinsic response target

The forward map is continuous

$$
\mathscr R:
\mathcal S(\mathbb R)
\longrightarrow
\mathcal S
\oplus\mathcal S
\oplus\mathcal H_{\rm rel}^2
\oplus\mathcal H_{\rm rel}^2,
$$

$$
g\longmapsto(B_g,Q_g,A_g,C_g).
$$

The inverse on its image is projection to the first Schwartz coordinate. Thus the analytic \(C_{41}^{\rm resp}\) does not depend solely on a transported topology.

The Fourier response operator \(\mathbb T\) is continuous because it uses only reflection, endpoint evaluation, and fixed linear combinations, all continuous on these rungs.

## Disposition

The four-function \(V_4^{\rm resp}\) has an independently declared multi-rung analytic topology: two Schwartz channels and two second-order relative-history channels. Forward response, inverse source projection, and the order-four Fourier action are continuous in this topology.