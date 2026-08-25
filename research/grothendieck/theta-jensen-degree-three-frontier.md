# Theta Jensen degree-three frontier

Author: `marici.Grothendieck`

## Exact discriminant reduction

For

\[
 \mathcal J_3^{(r)}(z)
 =a+3bz+3cz^2+dz^3,
\]

put

\[
 x=\frac{ac}{b^2},
 \qquad y=\frac{bd}{c^2}.
\]

The quadratic theorem gives `0<x,y<=1`. Direct discriminant reduction gives

\[
 \frac{\Delta_3}{27b^2c^2}
 =3-4x-4y+6xy-x^2y^2.
\]

Writing

\[
 u=1-x,
 \qquad v=1-y
\]

produces the exact coupled form

\[
 \boxed{
 \frac{\Delta_3}{27b^2c^2}
 =uv(2u+2v-uv)-(u-v)^2.
 }
\]

Hence degree-three hyperbolicity is equivalent to

\[
 \boxed{(u-v)^2\le uv(2u+2v-uv).}
\]

The simpler condition

\[
 (u-v)^2\le uv(u+v)
\]

is sufficient.

## Source meaning

Let

\[
 \rho_n=\frac{b_n}{b_{n-1}}
 =\frac1{m_n},
 \qquad m_n=\mathbb E_{Q_n}[W],
 \qquad W(U)=\frac{V'(U)}U.
\]

Then

\[
 x=\frac{\rho_{r+2}}{\rho_{r+1}},
 \qquad y=\frac{\rho_{r+3}}{\rho_{r+2}}.
\]

Since `Q_{n+1}` is the `U^2` reweighting of `Q_n`,

\[
 m_{n+1}-m_n
 =\frac{\operatorname{Cov}_{Q_n}(U^2,W)}
        {\mathbb E_{Q_n}[U^2]}.
\]

Therefore the two deficits are consecutive normalized score covariances:

\[
 u=\frac{\operatorname{Cov}_{Q_{r+1}}(U^2,W)}
          {\mathbb E_{Q_{r+1}}[U^2]m_{r+2}},
 \qquad
 v=\frac{\operatorname{Cov}_{Q_{r+2}}(U^2,W)}
          {\mathbb E_{Q_{r+2}}[U^2]m_{r+3}}.
\]

Degree two proves that each covariance is positive. Degree three asks that
their consecutive change remain inside the coupled cone.

## Interpretation and falsifier

Near the Gaussian boundary the exact condition requires

\[
 |u-v|=O((u+v)^{3/2}).
\]

Thus mere comparability is insufficient: adjacent coercivity losses must
vary one half-order more smoothly than their common magnitude.

The sharp falsifier is local: find the first `r` for which the two normalized
covariances leave the cone. The theorem-shaped source target is a signed
`3x3` minor or three-copy transport derived from the totally-positive tilt
kernel

\[
 K(n,U)=U^{2n}.
\]

No finite census is proposed as proof. The desired result is a uniform
source-derived covariance-transport inequality.

## Scope

This packet derives the exact degree-three obstruction and its source typing.
It does not assert that theta satisfies the coupled inequality.

## The cubic cone is a unit-step Lipschitz law

The nonlinear cone has a canonical coordinate.  Regard its boundary as a
quadratic equation in `v`:

\[
 (1-u)^2v^2-2u(1+u)v+u^2=0.                     \tag{1}
\]

Its two roots are

\[
 v_-(u)=\frac{u}{(1+\sqrt u)^2},
 \qquad
 v_+(u)=\frac{u}{(1-\sqrt u)^2}.                 \tag{2}
\]

Therefore, for `0<u,v<1`, the exact degree-three condition is

\[
 \frac{u}{(1+\sqrt u)^2}
 \le v\le
 \frac{u}{(1-\sqrt u)^2}.                        \tag{3}
\]

Taking positive square roots and reciprocals turns both bounds into one
statement:

\[
 \boxed{
 \left|\frac1{\sqrt v}-\frac1{\sqrt u}\right|\le1.
 }                                                  \tag{4}
\]

The boundary cases are continuous: `u=v=0` is the Gaussian equality case,
whereas exactly one zero deficit violates cubic hyperbolicity.

Define the inverse coercivity length

\[
 L_r:=u_r^{-1/2},
 \qquad
 u_r=1-\frac{\rho_{r+2}}{\rho_{r+1}}.             \tag{5}
\]

Then the entire degree-three Jensen hierarchy is equivalent to

\[
 \boxed{|L_{r+1}-L_r|\le1\qquad(r\ge0).}          \tag{6}
\]

This is the sought higher-order orientation law.  Degree two constructs a
positive length at each tilt.  Degree three says the source transport changes
that length by at most one unit per insertion of `U^2`.

Using the covariance formula already derived,

\[
 L_r=\left(
 \frac{\mathbb E_{Q_{r+1}}[U^2]m_{r+2}}
      {\operatorname{Cov}_{Q_{r+1}}(U^2,W)}
 \right)^{1/2}.                                   \tag{7}
\]

Thus the live theta theorem is now a discrete contraction estimate for a
single source-derived observable:

\[
 \boxed{
 \left|
 \sqrt{\frac{\mathbb E_{Q_{r+2}}[U^2]m_{r+3}}
 {\operatorname{Cov}_{Q_{r+2}}(U^2,W)}}
 -
 \sqrt{\frac{\mathbb E_{Q_{r+1}}[U^2]m_{r+2}}
 {\operatorname{Cov}_{Q_{r+1}}(U^2,W)}}
 \right|\le1.
 }                                                  \tag{8}
\]

The constant `1` is not fitted: it is forced exactly by the binomial
coefficients of the cubic Jensen polynomial.  This gives a hard falsifier
and a Deutschian explanation simultaneously.  The next attack should seek a
one-step coupling of `Q_{r+1}` and `Q_{r+2}` under multiplication by `U^2`
whose transport cost is precisely the difference in (8).

## A continuous self-concordance theorem would imply every cubic gate

The tilt family exists for every real `t>=0`:

\[
 dQ_t(U)=\frac{U^{2t}\,dP(U)}{\mathbb E[U^{2t}]},
 \qquad
 m(t)=\mathbb E_{Q_t}[W].                         \tag{9}
\]

Define the one-step deficit and its inverse length by

\[
 \delta(t)=1-\frac{m(t)}{m(t+1)},
 \qquad
 L(t)=\delta(t)^{-1/2}.                           \tag{10}
\]

At integral arguments, this is exactly the sequence in (5).  Therefore the
differential estimate

\[
 \boxed{|L'(t)|\le1\qquad(t\ge1)}                \tag{11}
\]

implies every discrete cubic gate by integration over `[r+1,r+2]`.

Differentiating (10) shows that (11) is equivalent to

\[
 \boxed{
 |\delta'(t)|\le2\delta(t)^{3/2}.
 }                                                  \tag{12}
\]

In terms of the score means alone,

\[
 \delta'(t)
 =\frac{m(t)m'(t+1)-m'(t)m(t+1)}{m(t+1)^2}.
                                                               \tag{13}
\]

Consequently the sufficient source theorem is

\[
\boxed{
 |m(t)m'(t+1)-m'(t)m(t+1)|
 \le
 2m(t+1)^{1/2}\{m(t+1)-m(t)\}^{3/2}.
}                                                   \tag{14}
\]

The derivative is itself a source covariance:

\[
 m'(t)=2\operatorname{Cov}_{Q_t}(W,\log U).       \tag{15}
\]

Thus (14) is a two-time covariance-determinant inequality.  It is stronger
than the exact discrete requirement, but it has two advantages: it is local
in the continuous tilt parameter, and its constant is still the forced unit
constant from the cubic discriminant.

This supplies a precise attack hierarchy:

1. derive (14) from a three-copy oriented integral or a TP3 minor;
2. if (14) fails, test the exact integrated bound
   `|L(t+1)-L(t)|<=1` before rejecting degree three;
3. if the integrated bound fails, the corresponding integer interval gives
   the first exact cubic falsifier.

The distinction prevents a failed differential strengthening from being
misreported as failure of the Jensen gate itself.

## One-tilt form of the differential target

Fix `t` and work entirely under `Q=Q_t`.  Put

\[
 R=U^2,
 \qquad H=\log U,
 \qquad M=\mathbb E_Q[W],
 \qquad A=\mathbb E_Q[R],
 \qquad B=\mathbb E_Q[RW].                        \tag{16}
\]

The next tilt is the `R`-size-biased law

\[
 dQ^R=\frac{R}{A}\,dQ,
 \qquad
 M_+:=\mathbb E_{Q^R}[W]=\frac BA.               \tag{17}
\]

Equations (15) and (17) turn (14) into the single-law inequality

\[
\boxed{
 \left|
 M\operatorname{Cov}_{Q^R}(W,H)
 -M_+\operatorname{Cov}_{Q}(W,H)
 \right|
 \le
 M_+^{1/2}
 \left(
 \frac{\operatorname{Cov}_{Q}(R,W)}{A}
 \right)^{3/2}.
}                                                   \tag{18}
\]

Every object in (18) is now evaluated on one source tilt and its canonical
size bias.  No comparison of independently normalized measures remains.

The right side is exactly the three-halves power of the positive transport
increment

\[
 M_+-M=\frac{\operatorname{Cov}_{Q}(R,W)}A.       \tag{19}
\]

The left side is the failure of logarithmic score covariance to commute with
that size-bias transport.  Thus the continuous cubic theorem has the form

\[
 \boxed{
 \text{size-bias/covariance commutator}
 \ \le\
 \text{transport increment}^{3/2}.
 }                                                  \tag{20}

This is the first formulation whose homogeneity explains the exponent
`3/2` in the cubic cone.  A three-copy proof should expand the commutator in
(18), orient the copies by `R_1<R_2<R_3`, and seek a Cauchy--Schwarz or
Gram determinant whose squared norm is bounded by the cube of the positive
two-copy transport (19).  Failure of that construction would falsify the
differential strengthening (14), while leaving the exact discrete unit-step
law (6) available.

## The first universal coupled positivity matrix

Let

\[
 \Delta:=M_+-M
 =\frac{\operatorname{Cov}_{Q}(R,W)}A>0,          \tag{21}
\]

and let

\[
 N:=M\operatorname{Cov}_{Q^R}(W,H)
    -M_+\operatorname{Cov}_{Q}(W,H).              \tag{22}
\]

The differential cubic condition (18) is exactly

\[
 N^2\le M_+\Delta^3.                              \tag{23}
\]

Equivalently, the symmetric matrix

\[
 \boxed{
 \mathcal G_t^{(3)}=
 \begin{pmatrix}
  M_+\Delta & N\\
  N & \Delta^2
 \end{pmatrix}
 \succeq0.
 }                                                  \tag{24}
\]

Both diagonal entries are already positive by the degree-two outward-score
theorem.  The determinant is

\[
 \det\mathcal G_t^{(3)}=M_+\Delta^3-N^2.          \tag{25}
\]

Thus degree three is the first universal *coupled* positivity problem: two
separately positive source channels must possess a coherent polarization
whose cross term is the size-bias commutator.

The theorem would close immediately if the theta source canonically supplied
features `X_t,Y_t` in one Hilbert space with

\[
 \|X_t\|^2=M_+\Delta,
 \qquad
 \|Y_t\|^2=\Delta^2,
 \qquad
 \langle X_t,Y_t\rangle=N.                       \tag{26}
\]

Then (23) would be ordinary Cauchy--Schwarz.  Conversely, manufacturing such
features from the desired inequality would be circular.  They must arise
from the oriented three-copy theta transport before the scalar moments are
taken.

This cleanly separates the two proof levels:

- the exact discrete theorem asks for the unit-step law (6);
- the stronger continuous theorem asks for the Gram matrix (24).

A negative determinant in (25) falsifies only the continuous strengthening
unless it occurs in a way whose integral over one tilt interval also violates
(6).

## The coupled matrix is a barycentre inequality on the separation measure

The one-step deficit has a simpler expression than (10).  Under `Q=Q_t`,

\[
 \delta
 =1-\frac{M}{M_+}
 =\frac{\operatorname{Cov}_Q(R,W)}{\mathbb E_Q[RW]}.
                                                               \tag{27}
\]

Put

\[
 C=\operatorname{Cov}_Q(R,W),
 \qquad B=\mathbb E_Q[RW].                        \tag{28}
\]

Because `R=U^2` and `W` are both increasing, the two-copy identity

\[
 C=\frac12\mathbb E_{Q\otimes Q}
 \left[(R_1-R_2)(W_1-W_2)\right]                 \tag{29}
\]

has a pointwise nonnegative integrand.  It therefore defines a canonical
probability measure on ordered source pairs:

\[
 d\mu_t(U_1,U_2)
 =\frac{(R_1-R_2)(W_1-W_2)}{2C}
 \,dQ_t(U_1)dQ_t(U_2).                            \tag{30}
\]

There is also a canonical single-copy size bias

\[
 d\nu_t(U)=\frac{R(U)W(U)}B\,dQ_t(U).             \tag{31}
\]

Let `H=log U` and `h_t=E_{Q_t}[H]`.  Differentiation of the exponentially
tilted measures gives

\[
 \frac d{dt}\log C
 =2\left(\mathbb E_{\mu_t}[H_1+H_2]-2h_t\right), \tag{32}
\]

and

\[
 \frac d{dt}\log B
 =2\left(\mathbb E_{\nu_t}[H]-h_t\right).         \tag{33}
\]

Since `delta=C/B`,

\[
 \frac{\delta'}{2\delta}
 =\mathbb E_{\mu_t}[H_1+H_2]
  -\mathbb E_{\nu_t}[H]-h_t.                    \tag{34}
\]

Substitution into (12) proves that the continuous cubic theorem is exactly
the barycentre bound

\[
\boxed{
 \left|
 \mathbb E_{\mu_t}[H_1+H_2]
 -\mathbb E_{\nu_t}[H]
 -\mathbb E_{Q_t}[H]
 \right|
 \le
 \sqrt{\frac{C}{B}}.
}                                                   \tag{35}
\]

This is a source-derived statement with no hidden moment normalization:

- `mu_t` is the positive two-copy separation current;
- `nu_t` is the `RW` physical size bias;
- `Q_t` is the undeformed source tilt;
- the right side is the square root of their normalized transport mass.

The exponent `3/2` and the Gram matrix (24) are shadows of this barycentre
comparison.  The next proof question is now geometric: can the ordering of
the theta score force the separation-pair log barycentre to stay within one
standard deviation `sqrt(C/B)` of the two single-copy barycentres?  A
Poincare, Brascamp--Lieb, or monotone-coupling proof must use the completed
theta potential; monotonicity of `W` alone only makes `mu_t` positive.
