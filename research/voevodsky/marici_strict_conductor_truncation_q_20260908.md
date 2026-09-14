# Strict conductor truncation on the 50-state dualizing model

Date: 2026-09-08

## Result

The strict map previously denoted

\[
q:\omega[2]\longrightarrow C\Pi^\vee[3]
\]

is recovered from the complete normalization-fibre comparison in `marici_joint_conductor_dual_endpoints`.

Let \(P_B\) be the ordered node resolution with ranks

\[
(1,9,18,15,6,1)
\]

and top state \(p_{E,O}\), where \(E=(0,2,4)\), \(O=(1,3,5)\). Use

\[
\omega=\operatorname{Hom}_A(P_B,A\Omega_6)[6].
\]

The joint comparison has

\[
H(p_{E,O})=-e_{0,2,4,1,3,5},
\qquad \kappa=H^*(e_{0,2,4,1,3,5}^\vee)=-p_{E,O}^\vee.
\]

Define the strict truncation in this ordered frame by

\[
q(p_{E,O}^\vee)=-1,
\qquad q(p_{U,V}^\vee)=0\quad((U,V)\ne(E,O)),
\]

with coefficients reduced along \(A\to C=A/(X_0,\ldots,X_5)\). Then

\[
q(\kappa)=1.
\]

Every one of the six differential columns entering \(p_{E,O}^\vee\) has coefficient \(\pm X_i\). All vanish in \(C\); all other target coordinates of \(q\) are zero. Hence

\[
q d_\omega=d_Cq=0
\]

strictly on all fifty dual basis states. After shifting by `[2]`, this is the required map to \(C\Pi^\vee[3]\). The polarity line is retained and no scalar splitting of the normalization sequence is used.

## Consequence

The previously unresolved square-zero block of the strict pullback differential now vanishes. Together with the explicit two-layer projection \(\pi_k\), the strict complex

\[
D_k^n=\omega[2]^n\oplus(E_{\beta,k}\Pi^\vee[3])^n
\oplus(C\Pi^\vee[3])^{n-1}
\]

has differential

\[
d(z,e,h)=(d_\omega z,d_Ee,qz-\pi_ke-d_Ch).
\]

The framed Branch B map remains kernel-valued, so its spatial insertion is

\[
b_{\sigma,T}=(0,j_k\kappa_{\sigma,T},0).
\]

## Reproduction

```sh
python research/voevodsky/check_marici_strict_conductor_truncation_q_20260908.py \
  --root . \
  --output research/voevodsky/marici_strict_conductor_truncation_q_certificate_20260908.json
```

The checker reconstructs the complete node and dual differentials, checks all fifty source columns, and records the six incoming top columns individually.
