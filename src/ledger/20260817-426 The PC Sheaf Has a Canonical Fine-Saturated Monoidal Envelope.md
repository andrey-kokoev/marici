---
id: 426
date: 2026-08-17
title: The PC Sheaf Has a Canonical Fine-Saturated Monoidal Envelope
---

# The PC Sheaf Has a Canonical Fine-Saturated Monoidal Envelope

Entry 425 showed why the ordinary DNC scheme is too small: its radial open
inverts the occurrence divisor. The replacement coefficient geometry is a
canonical fine-and-saturated monoidal diagram on the 215 loaded PC cells.

For a loaded cell \((S,H)\), put \(L=S\setminus H\) and define
\[
P_{S,H}=\mathbb N^9_X\oplus
 \bigoplus_{a\notin L}\mathbb N u_a\oplus
 \bigoplus_{a\in L}\mathbb Z u_a.
\]
Its monoid algebra over the coefficient ring \(R\) is exactly
\[
R[P_{S,H}]=R[X,u][u_a^{-1}:a\in L],
\]
the stalk used in Entry 422. Each \(P_{S,H}\) is a finite direct product of
copies of \(\mathbb N\) and \(\mathbb Z\), hence is integral, fine, and
saturated.

Every covering incidence changes \(L\) by one element. Its monoid map is the
face localization
\[
P_{S,H}\longrightarrow P_{S',H'}=P_{S,H}[u_a^{-1}].
\]
The exhaustive audit reconstructs all 215 charts and all 522 covering maps:
261 radial and 261 normal. In each case exactly the prescribed normal
coordinate is groupified. Thus the ringed Alexandrov diagram is already the
monoid-algebra realization of an fs Kato-style diagram; no ad hoc stalk rings
are required.

The raw generic DNC comparison is equally explicit. For every \(a\in L\), the
relation \(u_a=X_at_a\) gives
\[
t_a=u_a/X_a.
\]
Accordingly define
\[
Q_{S,H}=P_{S,H}[X_a^{-1}:a\in L].
\]
Then \(R[Q_{S,H}]\) is the corresponding raw radial DNC ring, and
\[
R[P_{S,H}]\longrightarrow R[Q_{S,H}]
\]
is precisely the generic occurrence localization found in Entry 425. Every
square formed by a finite-space incidence and this generic comparison
commutes, because both paths groupify the same coordinate subset.

This constructs the correct monoidal envelope globally. It retains the closed
faces \(X_a=0\), supports the Thom class of Entry 424, and recovers the raw DNC
only on the appropriate generic open. What remains is a realization question:
construct the associated logarithmic algebraic stack or Artin-fan morphism and
show that its constructible six-operation category is computed by this finite
Alexandrov diagram. The monoids and all their gluing maps are now fixed.

The executable audit is
`research/voevodsky/check_fs_monoidal_pc_envelope.py`.
