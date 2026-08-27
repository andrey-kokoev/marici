# 3345 — The Physical e6 Betti Pairing Normalizes the Target but Not Its Extension

## Question

Entry 3341 shows that the rank-twelve reduction module leaves the amplitude of
the primitive two-soft (e_6) torsor free. Can the existing physical and
integral (e_6) results select it?

## Existing physical result

Entries 1133–1134 derive the first-Rees covector and physical node boundary

\[
\rho_{e_6}=\left(-\frac18,+\frac18\right),
\qquad
d=(-1,+1),
\]

with pairing

\[
\rho_{e_6}(d)=\frac14.
\]

Entry 1140 identifies this covector as one quarter of the primitive integral
Betti dual. Therefore the physical node canonically normalizes the (e_6)
target line.

These entries are unretracted. They repair the mistyped target-to-target map of
Entries 1127–1129 by pairing a higher-Rees covector with an actual physical
boundary.

## Extension family

The object now under study is different. It is an extension

\[
0\longrightarrow\langle e_6\rangle
\longrightarrow E_c
\longrightarrow\langle q_0\rangle
\longrightarrow0
\]

with logarithmic connection corner

\[
A_c=
\begin{pmatrix}
0&0\\
c\,\omega&0
\end{pmatrix},
\qquad
\omega=d\log\frac{v}{v-2}.
\]

For every (c), the target line and its physical pairing remain

\[
\phi(e_6)=\frac14.
\]

But two extensions differ by

\[
A_{c_1}-A_{c_2}
=
\begin{pmatrix}
0&0\\
(c_1-c_2)\omega&0
\end{pmatrix}.
\]

Because (omega) has the primitive boundary divisor ((1,-1,0)), a gauge
regular at the labelled soft boundary cannot remove this difference unless

\[
c_1=c_2.
\]

## Result

The physical node and integral Betti comparison normalize the (e_6) target
line but do not select the extension amplitude (c).

This is a variance distinction:

- Entries 1134 and 1140 define a functional on the subobject (e_6);
- Entry 3341 asks for a class in an extension of (q_0) by (e_6).

A functional on the target cannot determine how the quotient is attached.

## Required physical selector

Selection requires a comparison involving both sides of the extension:

1. a source-authorized lift of the (q_0) quotient class into the rank-twelve
   relative object;
2. transport or boundary specialization of that lift;
3. projection to (e_6);
4. pairing with the established physical Betti boundary.

No such (q_0)-lift comparison is currently frozen. Constructing it by
choosing a convenient splitting would repeat the error retracted in Entry 1132.

## Consequence

The existing physical (e_6) normalization is compatible with the candidate
amplitude (C_2=-1/8), but it does not authorize that amplitude for the
rank-twelve torsor. The current physical-selector route is therefore blocked on
a typed (q_0)-to-(e_6) comparison, not on target normalization.

## Verification

The checker is
`research/benincasa/checkers/audit_target_betti_pairing_extension_nonselection.py`;
its packet is
`research/benincasa/results/target_betti_pairing_extension_nonselection.json`.

Allocator claim: `seqclaim-15e0b8356794e0999529a472`.
