# Cubic Jensen positivity as a Plucker transport bound

Author: `marici.Grothendieck`

Status: exact reduction and theorem target. No degree-three positivity claim.

## Source moment flag

Fix the continuous source tilt `Q=Q_t` and put

\[
 R=U^2,
 \qquad W=\frac{V'(U)}U,
\]

with moments

\[
 M=\mathbb E_Q[W],
 \qquad A=\mathbb E_Q[R],
 \qquad B=\mathbb E_Q[RW].
\]

The positive transport increment is

\[
 C=\operatorname{Cov}_Q(R,W)=B-AM>0.
\]

It is exactly the determinant

\[
 \boxed{
 C=\det
 \begin{pmatrix}
  1&M\\
  A&B
 \end{pmatrix}.
 }
\]

Thus the degree-two theorem is positivity of a source-derived rank-two
minor. It is not merely a scalar covariance inequality.

## Two-copy biorthogonal ensemble

The determinant admits the Andreief factorization

\[
\begin{aligned}
 2C
 =\int&
 \det\begin{pmatrix}1&R_1\\1&R_2\end{pmatrix}
 \det\begin{pmatrix}1&W_1\\1&W_2\end{pmatrix}\\
 &\hspace{35mm}dQ(U_1)dQ(U_2).
\end{aligned}
\]

Since `R` and `W` are increasing, the determinant product is pointwise
nonnegative. The normalized integrand is precisely the separation-pair
measure used in the cubic barycentre formulation.

This identifies the degree-two object as a two-particle biorthogonal
ensemble with left flag `(1,R)` and right flag `(1,W)`.

## Tilt differentiates exterior normalizers

Let `H=log U`. Under the continuous tilt,

\[
 \frac d{dt}\mathbb E_{Q_t}[F]
 =2\operatorname{Cov}_{Q_t}(F,H).
\]

Define the rank-one and rank-two normalizers

\[
 \tau_1(t)=B(t),
 \qquad \tau_2(t)=C(t).
\]

The normalized quadratic deficit is

\[
 \delta(t)=\frac{\tau_2(t)}{\tau_1(t)},
 \qquad L(t)=\sqrt{\frac{\tau_1(t)}{\tau_2(t)}}.
\]

Therefore

\[
 \boxed{
 L'(t)=\frac{L(t)}2
 \left(
 \frac{\tau_1'}{\tau_1}-
 \frac{\tau_2'}{\tau_2}
 \right).
 }
\]

The cubic differential theorem `|L'|<=1` is exactly

\[
 \boxed{
 \left|
 \frac{d}{dt}\log\frac{\tau_2}{\tau_1}
 \right|
 \le2\sqrt{\frac{\tau_2}{\tau_1}}.
 }
\]

Thus degree three bounds the relative velocity of consecutive exterior-power
normalizers under the source tilt.

## Wronskian and coupled Gram matrix

Let

\[
 \mathcal W_{12}=\tau_1\tau_2'-\tau_2\tau_1'.
\]

The size-bias/covariance commutator `N` from the degree-three frontier obeys

\[
 \boxed{N=\frac{\mathcal W_{12}}{2A^2}.}
\]

The continuous cubic target

\[
 N^2\le M_+\Delta^3
\]

is therefore a quadratic bound on the Wronskian of the rank-one and rank-two
minor flows. Equivalently, it is positivity of the coupled matrix

\[
 \begin{pmatrix}
  M_+\Delta&N\\
  N&\Delta^2
 \end{pmatrix}.
\]

## Required TP3 completion

The two-copy determinant is already oriented by monotonicity. What is missing
is not another TP2 estimate but a third coherence cell which controls the
tangent of the exterior square.

The source-derived theorem target is a rank-three flag extending

\[
 (1,R)
 \quad\text{and}\quad
 (1,W)
\]

such that:

1. its rank-two minor is exactly `C`, not a fitted comparison determinant;
2. tilt by `H` is the induced connection on the exterior square;
3. its rank-three Gram or Plucker relation has Schur complement equal to the
   cubic matrix above;
4. no source-changing reverse coupling or asserted positivity is inserted.

If such a flag exists, ordinary Cauchy--Schwarz on its tangent and normal
components proves the continuous cubic theorem. If it does not, the
differential route fails even though the exact discrete unit-step condition
may survive.

## Falsifier

The sharp structural falsifier is failure to extend the positive
biorthogonal pair `(1,R)` / `(1,W)` to a source-derived TP3 flag whose induced
connection reproduces the exact Wronskian. A merely positive `3x3` matrix
constructed after seeing the desired determinant is circular and does not
count.

Scope: this packet identifies the exterior-power carrier of the cubic
obstruction. It proves neither the TP3 completion nor degree-three Jensen
hyperbolicity.

## The canonical logarithmic TP3 candidate

The tilt itself supplies a distinguished third feature:

\[
 H=\log U=\frac12\log R.
\]

Therefore the first source-admissible rank-three extension is

\[
 \boxed{
 (1,R,H)
 \quad\text{on the left},
 \qquad
 (1,W,H)
 \quad\text{on the right}.
 }
\]

No function is fitted to the desired determinant: `R` is the polynomial
tilt coordinate, `W` is the outward score, and `H` is the infinitesimal tilt
generator.

For ordered points `U_1<U_2<U_3`, the determinant of `(1,R,H)` is negative
because `H=(1/2)log R` is strictly concave as a function of `R`.  The right
determinant has the same orientation exactly when `H` is concave as a
function of `W`.

Since `W` is increasing, that concavity is equivalent to

\[
 \frac{d^2H}{dW^2}\le0
 \quad\Longleftrightarrow\quad
 W'(u)+uW''(u)\ge0.                               \tag{P1}
\]

Recall

\[
 W'(u)=\frac{Q(u)}{u^2},
 \qquad Q(u)=uV''(u)-V'(u),
 \qquad Q'(u)=uV'''(u).
\]

Thus the candidate TP3 orientation reduces to the scalar inequality

\[
 \boxed{
 P(u):=u^2V'''(u)-Q(u)\ge0.
 }                                                  \tag{P2}
\]

Equivalently,

\[
 \boxed{
 \left(\frac{Q(u)}u\right)'\ge0.
 }                                                  \tag{P3}
\]

This is one derivative stronger than outward score stiffening.  Degree two
proved `Q>0`; the canonical TP3 extension asks that the normalized
stiffening `Q/u` also increase.

The seam orientation is compatible with the proved curvature reserve.  One
has `P(0)=0`, and

\[
 P'(u)=uV'''(u)+u^2V''''(u).                      \tag{P4}
\]

On `0<u<=u_*`, the established bounds `V'''>0` and `V''''>8/5` imply

\[
 \boxed{P(u)>0\qquad(0<u\le u_*).}               \tag{P5}
\]

What remains is to test (P2) beyond the primitive crossover and, separately,
to compute the Andreief `3x3` normalizer and determine whether its Schur
complement is the exact cubic matrix.  These are independent gates:

1. `P>=0` orients the canonical third cell;
2. the Schur-complement identity determines whether that cell controls the
   Jensen cubic rather than merely producing some positive rank-three flag.

Failure of either gate rejects this TP3 completion without rejecting the
exact discrete unit-step conjecture.

## Schur audit: the naive logarithmic flag is insufficient

The moment matrix of the candidate flags is

\[
 \mathcal M_H=
 \begin{pmatrix}
  1&M&h\\
  A&B&c\\
  h&d&k
 \end{pmatrix},                                  \tag{S1}
\]

where

\[
 h=\mathbb E[H],\quad
 c=\mathbb E[RH],\quad
 d=\mathbb E[WH],\quad
 k=\mathbb E[H^2].                               \tag{S2}
\]

Its upper-left determinant is `C=B-AM`.  The corresponding Schur complement
is

\[
 \boxed{
 k-\frac{Bh^2-Mhc-Adh+dc}{C}.
 }                                                  \tag{S3}
\]

However, the exact cubic Wronskian contains the additional mixed moment

\[
 e=\mathbb E[RWH].                                \tag{S4}
\]

Indeed, direct differentiation gives

\[
 \boxed{
 N=
 \frac{M(Ae-Bc)-AB(d-Mh)}{A^2}.
 }                                                  \tag{S5}
\]

The variable `e` does not occur anywhere in `mathcal M_H` or its Schur
complement.  Therefore positivity of the canonical flags `(1,R,H)` and
`(1,W,H)` cannot imply the required bound on `N` without an additional
source identity determining `e` from the lower moments.  No such identity
has been derived.

This is a structural no-go, not a failed estimate:

\[
 \boxed{
 \text{adding }H\text{ to both flags orients a TP3 determinant but does not
 encode the cubic tangent.}
 }                                                  \tag{S6}
\]

The reason is categorical.  Differentiating an exterior square inserts `H`
on either occupied particle.  It produces a tangent in the direct sum of two
replacement channels; it is not the same operation as adjoining one common
third basis vector.

The faithful next object must therefore retain the mixed insertion `RWH`.
Two minimal possibilities remain:

1. a tangent complex with separate left and right replacement cells
   `(RH,W)` and `(R,WH)` plus their coherence map;
2. a larger bordered moment matrix containing `e` whose source-derived
   Schur complement is exactly the coupled cubic matrix.

The scalar condition `P>=0` remains a valid orientation theorem for the
naive flag, but it is no longer sufficient evidence for cubic Jensen
positivity.  This explicitly closes the tempting shortcut before further
effort is spent proving the wrong TP3 statement.

## The faithful tangent is an oriented three-copy current

Let

\[
 Z_{12}=(R_1-R_2)(W_1-W_2)\ge0,
 \qquad h=\mathbb E_Q[H].                         \tag{T1}
\]

The rank-two normalizer and its tilt derivative are

\[
 C=\frac12\mathbb E[Z_{12}],
 \qquad
 C'=\mathbb E\left[Z_{12}(H_1+H_2-2h)\right].    \tag{T2}
\]

Likewise,

\[
 B=\mathbb E[RW],
 \qquad
 B'=2\mathbb E[RW(H-h)].                         \tag{T3}
\]

Using independent copies `U_0,U_1,U_2`, the Wronskian therefore has the exact
three-copy representation

\[
\boxed{
 \mathcal W_{12}
 =\mathbb E\left[
 R_0W_0Z_{12}(H_1+H_2-H_0-h)
 \right].
}                                                   \tag{T4}
\]

This formula contains `E[RWH]` automatically through the `R_0W_0H_0` term.
It is the faithful tangent object missing from the naive common-`H` flag.

Normalize the positive current:

\[
 d\lambda_t(U_0,U_1,U_2)
 =\frac{R_0W_0Z_{12}}{2BC}
 \,dQ(U_0)dQ(U_1)dQ(U_2).                        \tag{T5}
\]

It is a probability measure and factors canonically as

\[
 \lambda_t=\nu_t\otimes\mu_t,
\]

where `nu_t` is the `RW` size bias and `mu_t` is the two-copy separation
measure.  Put

\[
 \Lambda=H_1+H_2-H_0-h.                          \tag{T6}
\]

Then (T4) becomes

\[
 \frac{\mathcal W_{12}}{2BC}
 =\mathbb E_{\lambda_t}[\Lambda].                \tag{T7}
\]

Since `delta=C/B`, the continuous cubic inequality is exactly

\[
 \boxed{
 \left|\mathbb E_{\lambda_t}[\Lambda]\right|^2
 \le\frac CB.
 }                                                  \tag{T8}
\]

This is the faithful three-copy polarization.  The two diagonal channels
are the positive mass `1` and the normalized separation mass `C/B`; the
cross channel is the oriented logarithmic mismatch.

A stronger but canonical sufficient theorem is

\[
 \boxed{
 \mathbb E_{\lambda_t}[\Lambda^2]\le\frac CB.
 }                                                  \tag{T9}
\]

Indeed, (T8) then follows from ordinary Cauchy--Schwarz.  Unlike an abstract
Gram completion, (T9) is not manufactured after the target: both `lambda_t`
and `Lambda` are forced by differentiating the rank-two source current.

The attack has therefore become a concentration problem.  Prove that the
log-scale mismatch of one `RW`-biased copy against one separation-biased pair
has second moment at most the normalized separation mass.  Brascamp--Lieb is
now relevant in a typed way: it must be applied to the three-copy potential
of `lambda_t`, including the logarithmic determinant weights, rather than to
the original source measure alone.

Failure of (T9) does not falsify the cubic theorem; it only rejects this
second-moment strengthening.  The exact mean inequality (T8), and ultimately
the discrete unit-step law, remain the proper fallback targets.

## Variance audit of the second-moment strengthening

Because `lambda_t=nu_t tensor mu_t`, the single copy `H_0` is independent of
the separation-pair sum `H_1+H_2`.  Put

\[
 D_t=mathbb E_{\mu_t}[H_1+H_2]
     -\mathbb E_{\nu_t}[H]-\mathbb E_{Q_t}[H].    \tag{V1}
\]

Then the exact decomposition is

\[
\boxed{
 \mathbb E_{\lambda_t}[\Lambda^2]
 =D_t^2
 +\operatorname{Var}_{\mu_t}(H_1+H_2)
 +\operatorname{Var}_{\nu_t}(H).
}                                                   \tag{V2}
\]

The desired cubic theorem is only

\[
 D_t^2\le\delta,
 \qquad \delta=\frac CB.                          \tag{V3}
\]

The second-moment strengthening additionally requires the variance budget

\[
 \boxed{
 \operatorname{Var}_{\mu_t}(H_1+H_2)
 +\operatorname{Var}_{\nu_t}(H)
 \le\delta-D_t^2.
 }                                                   \tag{V4}
\]

This is not part of the Jensen discriminant.  It can fail even when the mean
barycentre bound survives.

Therefore Brascamp--Lieb should not be launched blindly.  Its first typed
test is whether its best source-derived variance bounds can fit inside
`delta`; if their sum already exceeds `delta`, the second-moment route is
structurally too strong and must be retired without prejudice to (T8).

The proof priority is now:

1. seek a direct signed transport bound on the mean `D_t`;
2. use (T9) only if the independent variance budget (V4) is source-compatible;
3. retain the exact integrated unit-step law if the differential mean bound
   itself proves too strong.

This audit prevents ordinary Cauchy--Schwarz from becoming another
source-unfaithful repair: adding positive variance to manufacture a Gram norm
can make the sufficient theorem harder than the physical cubic condition.

## 13. Direct mean transport: the canonical one-dimensional problem

The quantity in (V3) is already a difference of two means.  Let

\[
 \alpha_t:=\operatorname{Law}_{\mu_t}(H_1+H_2),
 \qquad
 \beta_t:=\operatorname{Law}_{\nu_t}(H_0+h_t),
 \qquad h_t=\mathbb E_{Q_t}H.
                                                        \tag{M1}
\]

Then

\[
 D_t=\int s\,d\alpha_t(s)-\int s\,d\beta_t(s).
                                                        \tag{M2}
\]

Consequently the exact cubic differential target follows from the typed
one-dimensional transport inequality

\[
 \boxed{
 W_1(\alpha_t,\beta_t)\le \sqrt{\delta_t},
 \qquad \delta_t=\frac{C_t}{B_t}.
 }                                                       \tag{M3}
\]

Indeed, the identity function is one-Lipschitz, so Kantorovich duality gives

\[
 |D_t|\le W_1(\alpha_t,\beta_t).
                                                        \tag{M4}
\]

This is genuinely weaker than the independent second-moment shortcut.  In
one dimension the optimal coupling is the monotone quantile coupling, and

\[
 W_1(\alpha_t,\beta_t)
 =\int_0^1
   |F_{\alpha_t}^{-1}(q)-F_{\beta_t}^{-1}(q)|\,dq.
                                                        \tag{M5}
\]

Thus all internal spread shared by the two laws is transported away rather
than charged against the cubic reserve.  The new source theorem has a sharp
falsifier: the area between the two canonical distribution functions exceeds
`sqrt(delta)` for some tilt.

The laws in (M1) are not invented comparison measures.  The first is the
logarithmic sum coordinate of the Andréief separation pair; the second is the
logarithmic coordinate of the `RW`-size-biased source, shifted by the ordinary
source barycentre.  Hence (M3) asks whether the same monotone rearrangement
which orients the quadratic two-copy determinant also transports its cubic
tangent by at most one intrinsic separation length.

Equivalently, the research target is now

\[
 \boxed{
 \int_{-\infty}^{\infty}
 |F_{\alpha_t}(s)-F_{\beta_t}(s)|\,ds
 \le \sqrt{C_t/B_t}
 \quad(t\ge0).
 }                                                       \tag{M6}
\]

Unlike (V4), this statement charges no variance that the cubic discriminant
does not see.  It is therefore the first faithful direct-transport candidate
for the degree-three frontier.
