# Correction: the unsymmetrized C34 common/difference block has zero oriented part

## Proposed candidate

The attempted mixed block was

\[
M_{34}=C^*J_2D,
\]

with

\[
C=\frac12(F_T+F_0),
\qquad
D=\frac12(F_T-F_0),
\]

and the Tate--Hardy projection rows

\[
F_T=(Q^T,I-Q^T),
\qquad
F_0=(Q^0,I-Q^0),
\qquad
J_2=\operatorname{diag}(I,-I).
\]

## Exact evaluation

For any two projections `Q_A,Q_B`, define

\[
F_A=(Q_A,I-Q_A),
\qquad
F_B=(Q_B,I-Q_B).
\]

Then

\[
\begin{aligned}
F_A^*J_2F_B
&=Q_AQ_B-(I-Q_A)(I-Q_B)\\
&=Q_AQ_B-I+Q_A+Q_B-Q_AQ_B\\
&=Q_A+Q_B-I.
\end{aligned}
\]

This expression is symmetric under exchange of `A` and `B`, even when the two
projections do not commute. Consequently

\[
F_0^*J_2F_T=F_T^*J_2F_0=Q^0+Q^T-I.
\]

Therefore

\[
\boxed{M_{34}-M_{34}^*=0.}
\]

The proposed oriented Hermitian current

\[
\frac1{2i}(M_{34}-M_{34}^*)
\]

vanishes identically.

## Meaning

The relative C34 feature retains the symmetric projection difference

\[
C^*J_2D+D^*J_2C=Q^T-Q^0,
\]

but its two-output projection-row realization erases the oriented commutator
needed for the causal forcing difference. Unsymmetrizing the already declared
cross contraction does not recover that information.

Prime localization cannot repair the failure:

\[
P_p(M_{34}-M_{34}^*)P_p^*=0
\]

for every shell and cutoff.

## Consequence

The C34 projection feature cannot supply the mixed reciprocal-odd block

\[
R(z)-R(-z)=\langle\Phi,(H_z-H_z^*)\Phi\rangle
\]

without an additional oriented channel not present in `(Q,I-Q)` with
signature `diag(I,-I)`.

A viable extension would have to retain, independently and before Xi
specialization, one of:

- an off-diagonal symplectic target form;
- an ordered pair of projection transitions rather than their complementary
  row;
- a Hardy causal orientation distinguishing `Q^0Q^T` from `Q^TQ^0`.

Adding such a channel is new arithmetic/analytic input. It cannot be recovered
from the current C34 positive feature by polarization.

## Disposition

The proposed C34 unlock is falsified by an exact two-line operator identity.
The terminal relative-Haar energy gate remains open.