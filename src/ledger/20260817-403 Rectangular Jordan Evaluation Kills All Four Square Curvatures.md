---
id: 403
date: 2026-08-17
title: Rectangular Jordan Evaluation Kills All Four Square Curvatures
---

# Rectangular Jordan Evaluation Kills All Four Square Curvatures

Entry 402 reduced the unresolved square-curvature space to an alternating
line and a standard two-dimensional \(D_8\)-module. We now evaluate the
actual four square boundaries in the special rectangular Jordan target,
rather than infer them from their scalar augmentation.

## Typed evaluation

The twelve octagon quadrangulations have the signed ternary presentations
constructed in Entry 19. Interpret both typed operations by rectangular
triple multiplication:
\[
T_+(a,b,c)=abc,\qquad T_-(u,v,w)=uvw,
\]
with alternating shapes
\[
A_i\in\operatorname{Mat}_{2\times3},\qquad
B_i\in\operatorname{Mat}_{3\times2}.
\]
The checker assigns seven distinct exact integer matrices in the pattern
\(A_0,B_1,A_2,B_3,A_4,B_5,A_6\) and recursively evaluates all twelve
presentations. Every presentation gives the same typed product
\[
A_0B_1A_2B_3A_4B_5A_6\in\operatorname{Mat}_{2\times3}.
\]
This is an executable use of associativity, not an identification of syntax
trees by hand.

Each of the four square curvatures is the oriented boundary value
\[
\kappa_i=V_{i,0}-V_{i,1}+V_{i,2}-V_{i,3}.
\]
All four matrices vanish exactly:
\[
(\kappa_0,\kappa_1,\kappa_2,\kappa_3)=(0,0,0,0).
\]
Consequently both non-scalar projections isolated in Entry 402 vanish:
\[
\kappa_{\rm alt}=0,\qquad
\kappa_{\rm std,1}=\kappa_{\rm std,2}=0.
\]

## Scope

The rectangular Jordan target therefore has no square-curvature residue:
the invariant, alternating, and standard \(D_8\) channels all close. This
strengthens Entry 401 from a scalar endpoint statement to a complete
four-square statement in the special rectangular realization.

What remains is geometric, not algebraic. We have not yet constructed a
chain-level comparison from the log/endpoint correspondence into these
matrix-valued ternary presentations. Thus this result proves that the target
acceptance test is clean; it does not prove that the geometric source reaches
the target with zero hidden kernel.

The next gate is the comparison map itself. On the square sector it is enough
to construct one \(D_8\)-equivariant map carrying the four geometric
curvature generators to the four evaluated Jordan boundaries. Its target is
now known to be zero in every irreducible channel, so any surviving source
class would be identified unambiguously as a geometric comparison defect.

The executable audit is
\`research/voevodsky/check_rectangular_jordan_square_curvatures.py\`.
