---
id: 401
date: 2026-08-17
title: The Even Endpoint Class Is Dihedral and Jordan Compatible
---

# The Even Endpoint Class Is Dihedral and Jordan Compatible

Entry 400 instantiated the endpoint mapping fiber and selected
\[
p_{\partial,Q}=0\in\mathbb Z/2.
\]
The first promised global acceptance test can therefore be made without
choosing a representative of the old endpoint torsor.

## Dihedral transport

Let \(r(i)=i+1\) and \(s(i)=-i\) on the eight cyclic labels. Direct
enumeration gives sixteen distinct transformations and verifies
\[
r^8=s^2=1,\qquad srs=r^{-1}.
\]
On the endpoint obstruction line, rotations preserve the scalar and
reflections carry the orientation character. Reduction modulo two erases the
sign. Consequently every one of the sixteen transports fixes the selected
class:
\[
g\,p_{\partial,Q}=0\qquad(g\in D_8).
\]
Thus the log-ray choice does not break the full dihedral symmetry at the
endpoint obstruction level.

## Jordan compatibility

The exact rectangular Jordan audit of Entry 17 established the typed
fundamental formula
\[
Q_{Q_x y}(z)=Q_x\bigl(Q_y(Q_x(z))\bigr),
\qquad Q_x(y)=xyx.
\]
The endpoint obstruction lands in its scalar specialization. The executable
audit checks the formula over a finite symmetric integer sample and, for the
geometrically selected value \(x=p_{\partial,Q}=0\), obtains
\[
Q_0(y)=0
\]
identically. Hence both sides of the fundamental formula vanish and the
endpoint class contributes no Jordan obstruction.

This is a genuine compatibility result but a deliberately narrow one. It
proves that the instantiated endpoint class is stable under \(D_8\) and is
annihilated by the induced scalar quadratic operator. It does **not** yet
identify the full octagonal geometric coherence differential with the
rectangular Jordan identity.

## Consequence and next gate

The endpoint parity/Bockstein route is now exhausted:
\[
p_{\partial,Q}=0,\qquad \beta(p_{\partial,Q})=0,
\qquad o_{D_8}=0,\qquad o_{\rm Jordan,endpoint}=0.
\]
Any remaining obstruction must live above this scalar endpoint quotient,
in the comparison between the full octagonal chain dependency and the
matrix-valued Jordan coherence. The next high-information experiment is to
construct that comparison map on the four square curvatures of the
eight-point coherence complex and test whether its kernel contains a
non-scalar residual class.

The executable audit is
`research/voevodsky/check_endpoint_d8_jordan_compatibility.py`.
