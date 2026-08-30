# Log-window Fourier sewing is maximally nonquasidiagonal

## Question

Does the native interval cutoff in logarithmic scale satisfy the authorized
quasidiagonality gate for Fourier sewing?

## Cutoff and sewing

Let \(P_R\) be multiplication by the indicator of \([-R,R]\) on
\(L^2(\mathbb R)\), and let \(\mathcal F\) be the unitary Fourier transform.
The incoming leakage block is

\[
P_R\mathcal F(I-P_R).
\]

Its norm is one for every positive \(R\).

## Escaping-packet proof

Choose the normalized packet

\[
h_{R,L}(x)=L^{-1/2}\mathbf 1_{[2R,2R+L]}(x).
\]

It lies entirely outside the visible interval, so

\[
(I-P_R)h_{R,L}=h_{R,L}.
\]

Translation of the packet changes only the Fourier phase. Its Fourier energy
has the same modulus as that of a length-\(L\) interval at the origin. With
unitary normalization, the energy outside \([-R,R]\) obeys

\[
\int_{|\xi|>R}|\widehat h_{R,L}(\xi)|^2\,d\xi
\le \frac{4}{\pi LR}.
\]

Therefore

\[
\lVert P_R\mathcal Fh_{R,L}\rVert^2
\ge1-\frac{4}{\pi LR}.
\]

Letting \(L\) grow proves that the leakage-block norm is at least one. It is
at most one because both the projection and Fourier transform are
contractions. Hence

\[
\lVert P_R\mathcal F(I-P_R)\rVert=1.
\]

## Consequence

The standard log-window filtration is not merely nonstrict at finite cutoff.
It is maximally nonquasidiagonal for Fourier sewing at every scale. Enlarging
the window does not reduce the worst-case crossing norm.

The hostile packet is source-local in the analytic carrier: it is an ordinary
normalized interval packet translated beyond the cutoff. No zero data or
retrospective multiplier enters.

## Typing boundary

This theorem applies to continuous logarithmic interval cutoffs. A discrete
Euler filtration or a pro-Gram arithmetic topology is a different object and
must be tested separately. It cannot inherit failure or success merely by
being described with the same cutoff parameter.

However, any proposed source functor that factors its cutoff topology through
the continuous log-window norm inherits this obstruction. Such a functor
cannot make Fourier sewing descend uniformly.

## Architectural verdict

Strict finite descent is closed for the continuous log-window carrier. The
leakage cell must remain as an independent boundary/seam port, or the source
topology must be strengthened by genuinely arithmetic controls that exclude
the translated long packets.

This explains why seam retention was structural rather than a temporary
regularization. The seam is the observable form of a norm-one crossing that
never vanishes uniformly.

## Verification

The checker `check_log_window_fourier_nonquasidiagonal.py` verifies the exact
tail estimate schedule using rational bounds and shows that its certified
visible energy approaches one for every fixed positive window radius.

