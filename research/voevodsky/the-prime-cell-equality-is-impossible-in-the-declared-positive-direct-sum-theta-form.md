# The prime-cell equality is impossible in the declared positive direct-sum theta form

> **Scope correction:** this theorem rejects direct identification of the raw Stieltjes endpoint Gram with the normalized theta direct-sum form. The latest source architecture instead uses a two-output Pauli dilation. See `correction-the-even-diagonal-no-go-rejects-only-the-raw-endpoint-identification-not-the-pauli-dilated-target.md`; the dilated comparison remains open.

## Setup

The coefficient-side Stieltjes even generator is the Gaussian window

\[
W_L(q)=H(q+L)-H(q-L),
\qquad
H(x)=\int_x^\infty e^{-\pi t^2}\,dt,
\qquad L=\log p>0.
\]

Its declared diagonal is

\[
G_{p,11}^{\rm St}
=\int_{\mathbb R}|W_L(q)|^2e^{-\pi q^2}\,dq.
\]

The fixed theta even column is

\[
w_\theta=\binom{1/2}{1/2}
\]

in endpoint metric \(2I\), so its endpoint contribution is exactly

\[
\langle w_\theta,w_\theta\rangle_{2I}=1.
\]

## Exact Stieltjes upper bound

Since the Gaussian has total mass one,

\[
0<H(x)<1
\]

for every finite real \(x\). Consequently, for \(L>0\),

\[
-1<W_L(q)<0
\]

for every \(q\), and therefore

\[
0<|W_L(q)|^2<1.
\]

Integrating against the probability density \(e^{-\pi q^2}\) gives the strict source bound

\[
\boxed{0<G_{p,11}^{\rm St}<1.}
\]

This holds for every prime, without numerical quadrature.

## Theta lower bound

The declared resolved theta form is a positive direct-sum graph form. On the even generator \(e_1\):

- the endpoint leg contributes exactly one;
- wall, tail, jump, and other positive graph legs contribute nonnegative terms;
- the odd constructor satisfies \(F_{odd,p}e_1=0\);
- hence both endpoint--odd mixed Green-mate terms vanish on \((e_1,e_1)\).

Therefore

\[
\boxed{H_{p,11}^\theta\ge1.}
\]

## Contradiction

The proposed prime-cell equality requires

\[
G_{p,11}^{\rm St}=H_{p,11}^\theta.
\]

But the two certified inequalities give

\[
G_{p,11}^{\rm St}<1\le H_{p,11}^\theta.
\]

Thus the equality is impossible in the presently declared normalization and positive direct-sum architecture. No off-diagonal linking choice can repair a diagonal defect when the odd column vanishes on \(e_1\).

At \(p=2\), the existing high-precision scout gives

\[
G_{2,11}^{\rm St}\approx0.6374050022176351,
\]

consistent with the analytic obstruction, but the numerical value is not needed for the theorem.

## Consequences

At least one of the following must change:

1. the Stieltjes source metric must contain an additional positive normalization term;
2. the theta endpoint metric or even column must be renormalized by independently sourced data;
3. the purportedly positive direct-sum theta attachments must include a declared negative/indefinite diagonal contribution;
4. the two displayed forms are not the forms intended by the comparison and require a new typed bridge.

Options 2 and 3 cannot be introduced merely to force equality. Option 4 is currently the safest classification.

## Lattice update

The local comparison coordinate is no longer merely authority-blocked. Under the displayed formulas it is falsified:

\[
(b_{\rm even},b_{\rm ord})=(0_{\rm falsified},0_{\rm falsified}).
\]

The analytic theta form and Stieltjes form may each remain valid in their own roles, but they cannot be identified by the fixed \(Q_p^{\rm lin}\) with the declared positive direct-sum normalization.

## Claim boundary

This rejects the stated local metric equality. It does not reject another source-derived normalization, a different typed comparison object, the definitional G4 packet, or RH.
