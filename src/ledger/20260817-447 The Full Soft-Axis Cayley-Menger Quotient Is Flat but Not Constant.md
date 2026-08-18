---
id: 447
date: 2026-08-17
title: The Full Soft-Axis Cayley-Menger Quotient Is Flat but Not Constant
---

# The Full Soft-Axis Cayley-Menger Quotient Is Flat but Not Constant

Benincasa Entries 441--442 identify the associated-graded soft-axis tail
\(\mathbf F[a,b]/(a^4)\) and show that the frozen physical chain supplies no
canonical cone killing it. The geometry-first continuation is to retain the
full Cayley--Menger relation along the frozen soft parameter \(u=X_2\), before
adding any support quotient.

In the audited chart \(X_1=1\), with the same fixed transverse coordinate as
the exact-form calculation, the full polynomial has unit \(a^4\) coefficient:
\[
K(u;a,b)=a^4+u,a^2(1-b^2)+O(u^2).
\]
Consequently
\[
\mathcal M_{CM}=\mathbb Q[u,a,b]/(K)
\]
is canonically free of rank four over \(\mathbb Q[u,b]\), with basis
\((1,a,a^2,a^3)\). Its special fibre is exactly
\[
\mathcal M_{CM}/u\mathcal M_{CM}
\cong\mathbb Q[a,b]/(a^4).
\]
Thus the persistent quartic tail has a finite geometric presentation over
the polynomial soft base even though it is infinite when graded only by
total polynomial degree.

The family is flat but not constant. Differentiating the defining relation
at \(u=0\) gives
\[
\partial_u K|_{u=0}=a^2(1-b^2),
\]
which is nonzero modulo \((a^4)\). Hence coefficientwise \(\partial_u\) does
not descend to the quotient. A Gauss--Manin correction must be derived from
the relative de Rham complex; choosing one merely to preserve the four basis
vectors would be a fitted connection.

This entry constructs a source-native candidate coefficient geometry, not a
physical class. It does not yet identify \(\mathcal M_{CM}\) with the full
filtered exact-form cokernel, and it supplies neither a relative-support
pushforward nor the admissible homotopies needed to lift Entry 446. The next
gate is to derive the relative de Rham/Gauss--Manin reduction of this monic
quartic family and compare its filtered associated graded with the actual
exact-form image.

The executable audit is
research/voevodsky/check_soft_axis_full_cayley_menger_module.py.
