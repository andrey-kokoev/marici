# The Gamma Wall Carries a Width-Two Pearson Ladder

## Bounded question

After increasing potential curvature failed to force the primitive cubic
gate, what exact structure distinguishes the Gamma wall from a generic
log-concave density?

This packet derives the smallest source-specific recurrence. It does not
prove the cubic gate or the Riemann hypothesis.

## Source density

Put

\[
a=\frac32,
\qquad
\rho(x)=x^{1/4}(x-a)e^{-x},
\qquad
x\ge c>a,
\]

and define the two-index moment array

\[
I_{j,q}(c)=\int_c^\infty
x^j\log(x/c)^q\rho(x)\,dx.
\]

The primitive wall-flux moments are $B_q=I_{0,q}$. Hence their adjacent
ratio is

\[
r(q)=q\frac{I_{0,q-1}}{I_{0,q}}.
\]

## Pearson identity

The density satisfies

\[
\frac{\rho'(x)}{\rho(x)}
=\frac{1}{4x}+\frac{1}{x-a}-1.
\]

With $\sigma(x)=x(x-a)$,

\[
\frac{(\sigma\rho)'(x)}{\rho(x)}
=-x^2+\frac{19}{4}x-\frac{15}{8}.
\]

More generally,

\[
\frac{(x^j\sigma\rho)'(x)}{x^j\rho(x)}
=-x^2+\left(j+\frac{19}{4}\right)x
-\frac32\left(j+\frac54\right).
\]

For $q>1$, integration by parts has no contribution at either endpoint.
Since

\[
\frac{d}{dx}\log(x/c)^q
=\frac{q}{x}\log(x/c)^{q-1},
\]

one obtains the exact ladder

\[
I_{j+2,q}
=\left(j+\frac{19}{4}\right)I_{j+1,q}
-\frac32\left(j+\frac54\right)I_{j,q}
+q\left(I_{j+1,q-1}-\frac32I_{j,q-1}\right).
\]

The recurrence is width two in $j$ and first order in the exponent shift.
All coefficients are forced by the primitive wall $a=3/2$ and the Gamma
weight $x^{1/4}e^{-x}$.

## What the recurrence explains

The scalar adjacent ratio is not the natural closed object. The natural
object is the positive bivariate array $I_{j,q}$. Compression to the
$j=0$ edge discards the $x$-weighted ports $I_{1,q}$ and $I_{2,q}$ that the
source differential equation immediately regenerates.

This explains why hypotheses stated only in terms of the scalar potential
curvature were too weak: they forget the coefficient transport in the
$x$-degree. The Gamma wall supplies an exact discrete connection between
that transport and the adjacent $q$-shift.

The ladder does not close on $I_{0,q}$ alone. Eliminating $I_{1,q}$ would
require an additional canonical relation, and no such relation has yet been
derived. Treating $I_{1,q}$ as a fitted function of $I_{0,q}$ would merely
repackage the desired theorem.

## Live theorem and falsifier

The next source-typed question is whether positivity of the complete Pearson
array, together with its Stieltjes minors in the $j$ direction, forces the
cubic response of the $j=0$ boundary ratio.

The cheapest falsifier is a positive two-index array satisfying the Pearson
ladder and all declared low-order Stieltjes minors while having
$r'''(q)\le0$. Such an array would show that even the exact ladder omits a
needed Gamma-source coherence. Conversely, a proof must use the coupled array
before scalar compression.

## Total positivity is present but insufficient by itself

The complete array has a universal orientation stronger than separate
Stieltjes positivity. Write $y=\log(x/c)$. Then

\[
I_{j,q}=\int_0^\infty e^{j\log x}e^{q\log y}\,d\mu_c(y),
\]

where $d\mu_c$ is the positive wall-flux measure. For strictly increasing
sequences $j_1<\cdots<j_n$ and $q_1<\cdots<q_n$, the kernels
$e^{j\log x}$ and $e^{q\log y}$ are strictly totally positive. The
continuous Cauchy-Binet identity therefore gives

\[
\det[I_{j_r,q_s}]_{r,s=1}^n>0
\]

whenever the source measure has at least $n$ support points in the positive
wall coordinate. The Gamma wall consequently carries strict total
positivity of every finite order.

This still does not force the cubic boundary response. Take the two-atom
moments

\[
B_q=1+e^q,
\qquad
r(q)=q\frac{1+e^{q-1}}{1+e^q}.
\]

Direct differentiation gives

\[
r'''(q)
=\frac{(e^{-1}-1)e^q}{(e^q+1)^4}
\left[
qe^{2q}-4qe^q+q-3e^{2q}+3
\right].
\]

At $q=4$, the bracket is

\[
e^8-16e^4+7>0,
\]

while $e^{-1}-1<0$, so $r'''(4)<0$. Replacing the atoms by sufficiently
narrow positive smooth bumps preserves the negative sign by continuity and
produces infinite support. Its bivariate moment kernel is then strictly
totally positive at every finite order.

Thus total positivity alone is another universal carrier property, not the
Gamma-specific Explanation. The live theorem is the compatibility of total
positivity with the exact Pearson ladder. A valid proof must use both in one
identity; citing them independently does not constrain the cubic boundary
compression.

## Exact boundary elimination and the Pearson threshold

The $j=0$ ladder eliminates the raw $q-1$ boundary moment. Normalize the
$q$-tilted wall measure and write its expectation as $\mathbb E_q$. Then

\[
r(q)=q\frac{I_{0,q-1}}{I_{0,q}}
=
\frac{
\mathbb E_q\left[x^2-\frac{19}{4}x+\frac{15}{8}\right]
}{
\mathbb E_{q-1}\left[x-\frac32\right]
}.
\]

The numerator polynomial factors at the exact roots

\[
x_\pm=\frac{19\pm\sqrt{241}}8.
\]

Hence there is a canonical Pearson threshold

\[
c_{\mathrm P}=x_+
=\frac{19+\sqrt{241}}8
\approx4.31552.
\]

For $c\ge c_{\mathrm P}$, both ports in the ratio are expectations of
pointwise positive source observables. This threshold lies slightly beyond
the potential-curvature fold near $4.06$, so it identifies a smaller
fully-positive far-wall regime without fitted partitions.

The reduction does not yet orient $r'''$. Its two expectations are taken in
adjacent tilted states, $q$ and $q-1$. Differentiation therefore generates
mixed cumulants in two different probability measures. Total positivity
orders each tilt family, but does not by itself compare their third response.
The exact remaining obstruction is a cross-tilt transport inequality for
these two positive Pearson ports.

This is more specific than the previous compatibility question. A proof in
the regime $c\ge c_{\mathrm P}$ must show that the Pearson ladder transports
third response across one unit of exponent tilt. A counterexample must obey
the ladder and positivity of both ports while reversing that response.

## The boundary two-port identity is response-neutral

The positive two-port formula must not be mistaken for a new inequality.
Define

\[
P(x)=x^2-\frac{19}{4}x+\frac{15}{8},
\qquad
Q(x)=x-\frac32.
\]

The $j=0$ Pearson identity is the partition-function equality

\[
\int P(x)y^q\rho(x)\,dx
=q\int Q(x)y^{q-1}\rho(x)\,dx.
\]

In the fully positive Pearson regime, let $\mu_q$, $\mu_q^P$, and
$\mu_{q-1}^Q$ denote the base, $P$-weighted, and $Q$-weighted probability
measures. Put

\[
L=\log y.
\]

Differentiating the partition identity gives, for every $k\ge1$,

\[
\kappa_k(\mu_q^P;L)
=\frac{d^k}{dq^k}\log q
+\kappa_k(\mu_{q-1}^Q;L).
\]

Therefore the weighted-port cumulants cancel exactly when the logarithmic
derivatives of the boundary ratio are formed. If

\[
\Delta_k
=\frac{d^k}{dq^k}\log r(q),
\]

then

\[
\Delta_k
=\frac{d^k}{dq^k}\log q
+\kappa_k(\mu_{q-1};L)
-\kappa_k(\mu_q;L).
\]

The cubic response remains

\[
\frac{r'''(q)}{r(q)}
=\Delta_3+3\Delta_1\Delta_2+\Delta_1^3.
\]

Thus the $j=0$ Pearson identity is response-neutral. It gives a useful
positive presentation and a canonical threshold, but no new force on the
sign of the cubic response. Equality of the scalar port normalizations does
not identify their probability measures or create an additional observable.

The first potentially constraining information lies in simultaneous
compatibility of all rows $j\ge0$. The recurrence should be treated as an
inhomogeneous half-line transfer system in $j$, driven by the adjacent
$q-1$ array. A proof must propagate a positive cone or sign-regular flag from
the large-$j$ boundary back to $j=0$. A boundary-only manipulation cannot
close the theorem.

## Verification

The symbolic checker
`research/grothendieck/checkers/gamma_wall_pearson_ladder.py` verifies the
Pearson polynomial and recurrence coefficients exactly. Its deliberate
wrong-wall test replaces $a=3/2$ by $a=1$ while retaining the printed
coefficients and must leave a nonzero residual. It also verifies the exact
two-atom third-derivative formula and its negative sign at $q=4$, and the
factorization defining the Pearson threshold.
