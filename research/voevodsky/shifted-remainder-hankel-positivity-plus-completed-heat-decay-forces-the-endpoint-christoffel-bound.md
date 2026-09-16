# Shifted remainder Hankel positivity plus completed-heat decay forces the endpoint Christoffel bound

## Objective

Use the known completed-heat decay asymptotic to remove the endpoint leverage inequality as an independent assumption.

If the shifted gamma--prime remainder moment tower is positive and determinate, its representing measure must contain the exact endpoint counter-atom at \(-1/4\). Subtracting that atom leaves a positive measure, which yields every endpoint Schur inequality automatically.

## Remainder derivative source

Let

\[
R(t)
=
\Theta(t)
-

e^{t/4}.
\]

Fix \(t_0>0\) and define

\[
c_k
=
(-1)^{k+1}
R^{(k+1)}(t_0),
\qquad
k\ge0.
\]

Thus

\[
C_r
=
(
c_{i+j}
)_{0\le i,j\le r}
=
H_r^{R,+}(t_0).
\]

The endpoint leverage target is

\[
C_r
\succeq
c_E
v_rv_r^*,
\]

where

\[
c_E
=
\frac14

e^{t_0/4},
\qquad
v_r
=
(
1,-1/4,\ldots,(-1/4)^r
)^T.
\]

## Positivity hypothesis

Assume

\[
\boxed{
C_r
\succeq0
\quad
\text{for every }r\ge0.
}
\]

By the Hamburger moment theorem, there is a positive measure \(\mu\) on \(\mathbb R\) such that

\[
c_k
=
\int_{\mathbb R}
x^k
\,d\mu(x).
\]

Assume the right-half-plane analyticity and exponential-moment bounds supplied by the completed source make this moment problem determinate and permit reconstruction of the derivative heat germ.

Then near \(t_0\), and by analytic continuation on its domain,

\[
-
R'(t)
=
\int_{\mathbb R}

e^{-(t-t_0)x}
\,d\mu(x).
\]

## Completed-heat decay input

Assume the unconditional completed heat decay

\[
\Theta(t)
\longrightarrow
0
\]

as \(t\to\infty\).

Then

\[
R(t)
=
-

e^{t/4}
+
o(1),
\]

and hence

\[
-
R'(t)
=
\frac14

e^{t/4}
+
o(

e^{t/4}
)
\]

in the differentiated asymptotic class.

Writing

\[
s
=
t-t_0,
\]

this becomes

\[
-
R'(t_0+s)

otag
=
\left(
\frac14

e^{t_0/4}
\right)

e^{s/4}
+
o(

e^{s/4}
).
\]

Thus the Laplace transform of \(\mu\) has leading growth rate \(e^{s/4}\) with coefficient \(c_E\).

## Left spectral edge

For a positive measure, the large-\(s\) growth of

\[
\int

e^{-sx}
\,d\mu(x)
\]

is determined by the left edge of its support.

The displayed asymptotic implies:

1. \(\mu\) has no support below \(-1/4\);
2. \(-1/4\) belongs to the support;
3. the mass at \(-1/4\) is exactly
   \[
   \mu(
   \{-1/4\}
   )
   =
   c_E.
   \]

Indeed, support below \(-1/4\) would produce faster exponential growth, while absence of an atom at the edge would make the normalized transform

\[

e^{-s/4}
\int

e^{-sx}
\,d\mu(x)
\]

converge to zero rather than \(c_E\).

## Positive atom subtraction

Therefore

\[
\mu
=

c_E
\delta_{-1/4}
+
\mu_+,
\]

where

\[
\mu_+
\ge0
\]

and

\[
\operatorname{supp}
\mu_+
\subseteq
[
-1/4,
\infty
).
\]

Consequently, for every polynomial \(p\),

\[
\int
|p(x)|^2
\,d\mu(x)
-

c_E
|p(-1/4)|^2
=
\int
|p(x)|^2
\,d\mu_+(x)
\ge0.
\]

At finite degree this is exactly

\[
\boxed{
C_r
-

c_E
v_rv_r^*
\succeq0.
}
\]

Thus the endpoint Schur--Douglas inequality follows from shifted remainder Hankel positivity plus the heat-decay asymptotic.

## Christoffel consequence

The Christoffel function satisfies

\[
\lambda_r(-1/4)

otag
=
\inf_{
\deg p\le r,
p(-1/4)=1
}
\int
|p(x)|^2
\,d\mu(x).
\]

The extracted atom gives

\[
\boxed{
\lambda_r(-1/4)
\ge

c_E
=
\frac14

e^{t_0/4}
}
\]

for every \(r\).

Under polynomial density away from the isolated atom,

\[
\lambda_r(-1/4)
\downarrow

c_E.
\]

So the endpoint leverage constants are uniformly contractive and asymptotically sharp.

## Reduction of the one-time gate

The complete shifted Hankel matrix is

\[
H_r^+
=
C_r
-

c_E
v_rv_r^*.
\]

The theorem shows that, once the analytic reconstruction and completed-heat decay inputs are admitted,

\[
\boxed{
C_r
\succeq0
	ext{ for every }r
\quad\Longrightarrow\quad
H_r^+
\succeq0
	ext{ for every }r.
}
\]

Therefore the endpoint leverage condition is not an additional infinite matrix hierarchy. It is forced by positivity of the shifted gamma--prime remainder tower together with the endpoint asymptotic.

## What remains independent

The ordinary complete tower still requires

\[
H_r
=
H_r^R
+

e^{t_0/4}
v_rv_r^*
\succeq0.
\]

The positive endpoint atom may repair one ordinary remainder direction, but no analogous argument makes this tower automatic from \(C_r\succeq0\).

Thus the one-time source target reduces to:

1. positivity of the shifted remainder tower \(C_r\);
2. positivity of the ordinary completed tower \(H_r\);
3. analytic/determinacy and completed-decay inputs.

The separate endpoint Schur gate then follows.

## Relation to the Sonin/Green channel

In the Green presentation, the open condition was

\[
C_r
\succeq
b_rb_r^*.
\]

Here the vector \(b_r\) is the endpoint atom and \(C_r\) is the shifted gamma--prime moment bulk. The heat-decay argument identifies \(b_rb_r^*\) as an actual atom already contained in the positive representing measure of \(C_r\).

Therefore the Green endpoint contraction, if the remainder tower is positive, is the canonical coordinate projection onto that atom. Its norm is one in the completed limit.

## Caveats

The implication depends on the following analytic gates:

1. existence of a positive representing measure from all \(C_r\);
2. determinacy or sufficient exponential moments;
3. reconstruction of \(-R'(t)\) from the moments at \(t_0\);
4. differentiated completed-heat decay with the stated leading term;
5. exclusion of untracked growing completed terms.

Prior research establishes the formal decay reduction but records that authoritative sourcing of the exact complex-zero heat expansion and limit interchanges remains necessary.

## Disposition

The endpoint gate is forced once the shifted gamma--prime remainder tower is positive:

\[
\boxed{
	ext{shifted remainder Hankel positivity}
+
	ext{completed heat decay}

\Longrightarrow
	ext{exact endpoint atom}

\Longrightarrow
	ext{uniform Schur--Douglas leverage}.
}
\]

The principal unresolved matrix inequalities are therefore the remainder Hankel positivity itself and the ordinary completed Hankel tower, not a third independent endpoint hierarchy.
