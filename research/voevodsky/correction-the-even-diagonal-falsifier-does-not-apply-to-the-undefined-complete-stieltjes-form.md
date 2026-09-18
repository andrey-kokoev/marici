# Correction: the even-diagonal falsifier does not apply to the undefined complete Stieltjes form

## Newly exposed type ambiguity

The bound

\[
0<\langle W_L,W_L\rangle<1
\]

is exact. It applies to the object explicitly named in the source as

\[
G_{p,11}^{St,even}.
\]

The same source then declares a resolved tail attachment, including

\[
\langle BW_L,BW_L\rangle,
\]

and later writes the desired identity using the different, unexpanded symbol

\[
G_p^{St}=H_p^\theta.
\]

No intervening displayed formula defines the complete matrix \(G_p^{St}\) from \(G_p^{St,even}\) and the attachments.

Therefore the inference

\[
G_{p,11}^{St}<1
\]

was not licensed. Only

\[
G_{p,11}^{St,even}<1
\]

was proved. Positive tail, jump, wall, or graph contributions can raise the complete diagonal above one.

## What remains genuinely falsified

The argument still rejects either of these explicit claims:

1. \(G_p^{St}\) means the raw window Gram \(G_p^{St,even}\);
2. the full faithful Pauli linking Gram is built from that raw window Gram and compared to the normalized positive theta form.

Faithfulness propagates the raw mismatch exactly in that case.

It does **not** reject a full Pauli lift of an independently defined completed Stieltjes graph form.

## Exact missing definition

The repository now owes a source-level formula such as

\[
G_p^{St,comp}
=
F_{win,p}^*F_{win,p}
+F_{tail,p}^{St,*}F_{tail,p}^{St}
+F_{jump,p}^{St,*}F_{jump,p}^{St}
+\cdots,
\]

with every coefficient, sign, domain, and mixed block specified. The notation must then state unambiguously whether

\[
G_p^{St}=G_p^{St,even}
\quad\text{or}\quad
G_p^{St}=G_p^{St,comp}.
\]

Until that is done, neither the even residual nor its Pauli lift is well typed.

## First executable comparison after repair

Once the complete source form is frozen, compute

\[
r_{11,p}=G_{p,11}^{St,comp}-H_{p,11}^\theta.
\]

The raw-window estimate supplies only

\[
G_{p,11}^{St,comp}
=G_{p,11}^{St,even}+\text{attachments},
\qquad
0<G_{p,11}^{St,even}<1.
\]

It supplies no sign for \(r_{11,p}\) without the attachment table.

## Correct status

- raw-window equality: falsified;
- faithful Pauli lift of the raw-window equality: falsified;
- complete Stieltjes graph equality: undefined/blocked, not falsified;
- faithful Pauli lift of a completed Stieltjes graph: blocked on that same definition.

## Claim boundary

This correction retracts only the extension of the raw bound to the undefined complete form. It preserves the analytic window inequality and the exact injectivity of the Pauli lift.
