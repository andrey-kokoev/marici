# Theta cubic Poisson--Hermite energy

Author: `marici.Grothendieck`

## Objective

Construct or sharply falsify a theta-specific Poisson-summed Hermite/Bezout
energy for the exceptional cubic Jensen polynomial.

## 1. Exact Hermite matrix

Write

\[
J_2^{(3)}(X)=d+3CX+3BX^2+AX^3
\]

and divide by `A`:

\[
p(X)=X^3+aX^2+bX+c,
\qquad
a=\frac{3B}{A},\quad b=\frac{3C}{A},\quad c=\frac dA.
\]

If `s_j` are the Newton power sums of the three roots of `p`, then

\[
\begin{aligned}
s_0&=3,\\
s_1&=-a,\\
s_2&=a^2-2b,\\
s_3&=-a^3+3ab-3c,\\
s_4&=a^4-4a^2b+2b^2+4ac.
\end{aligned}
\]

The Hermite matrix is

\[
\boxed{
H(p)=
\begin{pmatrix}
3&s_1&s_2\\
s_1&s_2&s_3\\
s_2&s_3&s_4
\end{pmatrix}.
}
\]

For a real cubic with nonzero leading coefficient, `H(p)` is positive
semidefinite exactly when all roots are real, with rank recording the number
of distinct roots.

## 2. Principal minors and the unique unresolved channel

The first leading minor is `3`. The second is

\[
\begin{aligned}
\det H_{[0,1]}
&=3s_2-s_1^2\\
&=2(a^2-3b)\\
&=\frac{18(B^2-AC)}{A^2}\\
&=\frac{18D}{A^2}>0.
\end{aligned}
\]

This is precisely the already-proved quadratic Jensen reserve. The full
determinant is

\[
\det H(p)=\operatorname{disc}(p)
=\frac{\operatorname{disc}(J_2^{(3)})}{A^4}.
\]

Therefore the final scalar Schur complement is

\[
\boxed{
S_{34}
=\frac{\det H(p)}{\det H_{[0,1]}}
=\frac{\operatorname{disc}(J_2^{(3)})}{18A^2D}.
}
\]

Using

\[
\mathscr R_{34}
=12\Gamma(9/2)^4Z_5^2\operatorname{disc}(J_2^{(3)}),
\]

\[
A=\frac{2Z_5}{9\Gamma(9/2)},
\qquad
D=\frac{K_4}{9\Gamma(9/2)^2},
\]

gives the exact theta normalization

\[
\boxed{
S_{34}=\frac{27\mathscr R_{34}}{32Z_5^4K_4}.
}
\]

All denominators are strictly positive. Thus the Hermite problem contains
exactly one unresolved direction, and its sign is exactly the original
exceptional residual.

## 3. Entries in completed theta moments

Let `G=Gamma(9/2)`. The normalized coefficients are

\[
A=\frac{2Z_5}{9G},
\qquad
B=\frac{Z_4}{G},
\qquad
C=\frac{7Z_3}{2G},
\qquad
d=\frac{35Z_2}{4G}.
\]

Consequently

\[
\boxed{
a=\frac{27Z_4}{2Z_5},
\qquad
b=\frac{189Z_3}{4Z_5},
\qquad
c=\frac{315Z_2}{8Z_5}.
}
\]

Substitution into the Newton sums above expresses every Hermite entry through
the single completed moment packet `(Z_2,Z_3,Z_4,Z_5)`. No zero data or
fitted spectral measure occurs.

## 4. Gaussian carrier

For a pure Gaussian source, Gaussian normalization makes

\[
b_2=b_3=b_4=b_5.
\]

Hence

\[
J_2^{(3)}(X)=b_2(1+X)^3.
\]

All three roots coincide at `-1`, and

\[
H_{m G}=3
\begin{pmatrix}
1&-1&1\\
-1&1&-1\\
1&-1&1
\end{pmatrix}.
\]

This matrix has rank one. Gaussian normalization has therefore removed a
universal carrier sitting on the codimension-two boundary of the Hermite
cone. Quadratic positivity opens one transverse direction; the exceptional
cubic theorem asks theta arithmetic to open the final direction with the
correct sign.

The near-Gaussian hostile examples are dangerous precisely because the final
Schur complement is born from zero. Generic positive perturbations need not
enter the Hermite cone on its positive side.

## 5. Poisson-completed carrier and positive lattice tail

Let

\[
\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}
\]

and define

\[
h(u)=\frac12e^{u/2}\vartheta(e^{2u}).
\]

Poisson summation gives

\[
\vartheta(e^{2u})=e^{-u}\vartheta(e^{-2u}),
\]

so

\[
\boxed{h(-u)=h(u).}
\]

Writing

\[
A(u)=\sum_{n\ge1}e^{-\pi n^2e^{2u}},
\qquad
h(u)=e^{u/2}\left(\frac12+A(u)\right),
\]

one obtains the exact source identity

\[
\boxed{
\Phi(u)=\left(\partial_u^2-\frac14\right)h(u).
}
\]

Indeed, on each nonzero lattice label,

\[
e^{u/2}(\partial_u^2+\partial_u)e^{-\pi n^2e^{2u}}
=e^{u/2}(4x_n^2-6x_n)e^{-x_n},
\quad x_n=\pi n^2e^{2u}.
\]

The zero mode `e^(u/2)/2` is annihilated by the differential operator. It is
the universal growing carrier.

For `u>0`, remove it and define the decaying positive lattice tail

\[
\boxed{
q(u)=h(u)-\frac12e^{u/2}
=e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}>0.
}
\]

On the positive chart,

\[
\Phi=(\partial_u^2-1/4)q.
\]

The full even extension of `q` has the cusp complementary to the removed
homogeneous carrier. Distributionally its point mass restores smoothness of
`h`; for all moments used here (`t>=2`) that point mass is killed by the
factor `u^(2t)`.

## 6. Simultaneous summation by parts

Put

\[
M_t=\int_0^\infty u^{2t}q(u)\,du.
\]

The lattice tail is positive and decays super-exponentially at `+infinity`.
For `t>=1`, both integrations by parts have zero endpoint terms, giving

\[
\boxed{
Z_t=2t(2t-1)M_{t-1}-\frac14M_t.
}
\]

In particular,

\[
\begin{aligned}
Z_2&=12M_1-\frac14M_2,\\
Z_3&=30M_2-\frac14M_3,\\
Z_4&=56M_3-\frac14M_4,\\
Z_5&=90M_4-\frac14M_5.
\end{aligned}
\]

This is the first representation in the programme that distinguishes theta
from a generic positive even source while retaining a positive underlying
measure. Poisson summation supplies the even carrier; removal of its
homogeneous zero mode leaves the positive full-lattice tail `q`.

The pointed term `Z_2` is now typed: it is the lowest member of the same
lattice-tail moment ladder, not an independently fitted boundary repair.
There is no surviving seam scalar at these orders; its role was to define the
correct carrier subtraction before integration by parts.

## 7. Revised energy question

Substituting the four displayed formulas into the Hermite matrix converts its
unique Schur complement into a polynomial in the five consecutive positive
tail moments

\[
(M_1,M_2,M_3,M_4,M_5).
\]

The sharp question is now whether the special lattice density

\[
q(u)=e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}
\]

forces that polynomial to be nonnegative. Positivity of an arbitrary measure
`q(u)du` may be tested first; failure would identify the extra lattice
property still needed without reverting to the generic hostile source.

## 8. Self-dual scale-pair sources

Let `Phi_0` be the standard completed theta source. For any real `L`, define

\[
\Phi_L(u)=\Phi_0(u-L)+\Phi_0(u+L).
\]

This is not an arbitrary even deformation. If `a=e^L`, the two terms arise
from the lattice `a Z` and its dual `a^(-1) Z`. At the carrier level,

\[
a^{1/2}\vartheta(a^2x)+a^{-1/2}\vartheta(a^{-2}x)
\]

is fixed by the Poisson transformation `x -> 1/x` with the correct weight.
Since the completion operator commutes with translation, `Phi_L` is a
positive, even, entire, genuinely Poisson-closed scale-pair source.

Let

\[
\mu_{2j}=\int_{\mathbb R}v^{2j}\Phi_0(v)\,dv.
\]

Evenness gives the exact half-line moments

\[
\boxed{
Z_t[L]
=\sum_{j=0}^t\binom{2t}{2j}L^{2t-2j}\mu_{2j}.
}
\]

In particular,

\[
Z_t[L]=\mu_0L^{2t}+O(L^{2t-2})
\qquad(L\longrightarrow\infty).
\]

A single far-separated reciprocal scale pair therefore approaches one
positive radial atom.

## 9. One scale orbit is asymptotically safe

For a single positive atom with moments

\[
Z_t=w y^t,
\]

one has

\[
K_4=(9-7)w^2y^8=2w^2y^8,
\]

\[
\mathcal E_{34}=(35+162-189)w^3y^{12}=8w^3y^{12},
\]

and hence

\[
\boxed{
\mathscr R_{34}=224w^6y^{24}>0.
}
\]

Thus one reciprocal scale orbit cannot provide the asymptotic falsifier. Two
distinct scale orbits are the first possible obstruction.

## 10. Minimal two-orbit Poisson-closed falsifier

For `T>0`, form the positive integer-weighted completed source

\[
\boxed{
\Psi_T(u)
=1000\Phi_T(u)+3\Phi_{\sqrt3T}(u).
}
\]

It is a disjoint weighted union of two lattice/dual-lattice scale pairs, so
it is positive, even, entire, and exactly Poisson-closed. Its moments satisfy

\[
Z_t[\Psi_T]
=\mu_0T^{2t}(1000+3\cdot3^t)+O(T^{2t-2}).
\]

For `t=2,3,4,5`, the leading packet is

\[
\boxed{(z_2,z_3,z_4,z_5)=(1027,1081,1243,1729).}
\]

Exact integer arithmetic gives

\[
\begin{aligned}
k&=9z_4^2-7z_3z_5=822098>0,\\
e&=35z_2z_5^2+162z_4^3-189z_3z_4z_5\\
 &=-20514280744,
\end{aligned}
\]

but

\[
\boxed{
36k^3-e^2
=-400833721223554606624<0.
}
\]

Because the residual is homogeneous of total scale degree `48`, it follows
that

\[
\mathscr R_{34}[\Psi_T]
=\mu_0^6T^{48}(36k^3-e^2)+O(T^{46}).
\]

Therefore

\[
\boxed{
\mathscr R_{34}[\Psi_T]<0
\quad\text{for every sufficiently large }T.
}
\]

At the same time `K_4[Psi_T]>0` for sufficiently large `T`, because its
leading coefficient is `k>0`. The quadratic layer survives while the unique
Hermite Schur direction is negative.

This is a two-orbit Poisson-closed analytic falsifier. It is minimal within
the scale-separated atomic mechanism: one atomic scale orbit has strictly
positive residual, while two suffice for failure. No claim is made here that
every finite-width one-orbit deformation is positive at every scale.

## 11. Polarized two-orbit obstruction

Retain symbolic weight `lambda` for the second asymptotic orbit and use
squared shifts `1` and `3`. The leading moments are

\[
z_t(\lambda)=1+\lambda3^t.
\]

Exact polarization gives

\[
k(\lambda)=2-432\lambda+13122\lambda^2,
\]

\[
e(\lambda)
=8-9648\lambda+34992\lambda^2+4251528\lambda^3,
\]

and

\[
\boxed{
\begin{aligned}
r(\lambda)={}&224-32256\lambda-47664288\lambda^2\\
&-4744075392\lambda^3
+382484464992\lambda^4\\
&-8331090195456\lambda^5
+63264216171744\lambda^6.
\end{aligned}
}
\]

The constant and leading coefficients are positive, agreeing with
positivity of either pure scale orbit. The first mixed coefficient is
negative, and `lambda=3/1000` gives the exact negative integer packet above
after clearing the common weight.

Thus the first irreducible obstruction is genuinely cross-orbit. Negative
packets do not cancel within either fixed reciprocal-scale orbit; they arise
from interference between two separately Poisson-closed positive sectors.
This explicitly supplies the polarized Schur-complement audit requested by
the programme.

The pointed channel can also be tracked without ambiguity. At first order in
`lambda`, the three parts of `e(lambda)` contribute

\[
\begin{array}{c|r}
\text{term}&[\lambda]\,e\\
\hline
35z_2z_5^2&17325\\
162z_4^3&39366\\
-189z_3z_4z_5&-66339.
\end{array}
\]

Thus `e'(0)=-9648`. Since `k(0)=2`, `k'(0)=-432`, and `e(0)=8`,

\[
r'(0)=108k(0)^2k'(0)-2e(0)e'(0)=-32256.
\]

As a signed-channel audit, if the pointed `35z_2z_5^2` contribution were
omitted, the same derivative would instead be `+244944`. This omission is
not an admissible modification of the theorem; it diagnoses the role of the
required endpoint. In the hostile two-orbit packet, the pointed `Z_2` channel
consumes the first-order reserve rather than repairing it.

## 12. Consequences for summation-by-parts energy

No positive-bulk-plus-pointed-boundary identity can follow solely from:

- positivity and analyticity of the completed source;
- exact Poisson reciprocal closure;
- removal of the Gaussian zero mode;
- positivity of the lattice tail;
- positivity of the quadratic companion; and
- inclusion of the lowest pointed moment `Z_2`.

The source `Psi_T` has all these properties and nevertheless makes the final
Schur complement negative. In particular, the `Z_2` term does not
canonically repair the negative channel for general Poisson-closed sources.

The simultaneous summation-by-parts formula remains exact, but its resulting
moment polynomial cannot be rearranged into universally nonnegative bulk and
boundary pieces on this class. Any such rearrangement would contradict the
integer leading packet above.

## 13. What is special about the standard theta source

The falsifier identifies the missing arithmetic property sharply. The
standard source is not merely Poisson-closed; it is a single primitive
self-dual scale orbit. The counterexample becomes possible when two distinct
reciprocal scale orbits are superposed with independent multiplicities.

Thus the surviving theorem must use a property destroyed by that
superposition, for example:

\[
\boxed{
\text{primitive single-scale indecomposability of the theta lattice.}
}
\]

Neither linear Poisson summation nor positive Gram construction can detect
this property, because both are stable under positive direct sums. The
exceptional inequality, if true for the standard theta source, is therefore
*non-additive across Poisson sectors*.

This is an important structural conclusion: the desired explanation cannot
be a functorial positive energy on the category of Poisson-completed sources.
It must recognize which completed source is primitive before taking its
scalar moments.

## 14. Final disposition

The proposed theta-specific Poisson--Hermite energy is sharply falsified in
its additive form:

1. the Hermite matrix has one unresolved Schur direction;
2. Poisson summation produces a positive lattice-tail moment ladder;
3. Gaussian removal leaves no boundary seam at the relevant orders;
4. one reciprocal scale orbit is asymptotically positive;
5. two reciprocal scale orbits give an exact negative leading packet;
6. hence no additive Poisson-summed Gram energy can prove the exceptional
   gate.

The next faithful residual object is the Hermite Schur complement restricted
to the *primitive single-scale* completed theta source. A future proof must
derive a nonlinear indecomposability invariant before moment projection; a
linear full-lattice energy is now excluded.

## Scope

The Hermite matrix and Schur reduction are exact. They do not yet construct a
theta Gram energy and do not prove RH.
