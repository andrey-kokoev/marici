---
id: 541
date: 2026-08-18
title: The Dodecagon Passes the First Four-Cut Induction Gate
---

# The Dodecagon Passes the First Four-Cut Induction Gate

Entry 540 proves framed Cut rigidity through arity ten.  The dodecagon is the
first test in which a Cut stratum contains an (n=10) factor and four
compatible restrictions can meet.

The twenty-four physical Cuts consist of twelve (4\times10) channels and
twelve (6\times8) channels.  Their noncrossing nerve has census

\[
\boxed{f=(24,156,364,273)}
\]

through dimensions zero to three, with no compatible five-Cut family.  The
integral boundary ranks are

\[
(23,133,231).
\]

Every nonzero Smith factor is one, so

\[
\boxed{H_0\cong\mathbb Z,quad H_1=H_2=0,quad
H_3\cong\mathbb Z^{42}.}
\]

## Lower-arity factorization

Every Čech stratum factors entirely through already rigid even arities:

\[
\begin{array}{c|l}
0&12(4,10)+12(6,8)\\
1&78(4,4,8)+78(4,6,6)\\
2&364(4,4,4,6)\\
3&273(4,4,4,4,4).
\end{array}
\]

Thus all local framed mapping spaces are products of the rigid (n=4,6,8,10)
spaces established previously.

## Four-Cut coherence

Each top simplex is a complete quadrangulation into five four-point factors.
All twenty-four orders of its four restrictions were evaluated.  The Koszul
permutation character and the permutation character of four odd native Thom
normals are both (operatorname{sgn}), so their product is trivial.  All

\[
273\cdot24=6552
\]

ordered composites equal the fixed positive product of five primitive units.
The physical obstruction 3-cochain is therefore literally zero on every top
simplex, and hence on all forty-two top homology coordinates.

It follows that the framed dodecagon gluing diagram is nonempty and has zero
relative deformation diagram.  Its homotopy limit is contractible:

\[
\boxed{\text{the }n=12\text{ framed Cut gluing exists and is rigid}.}
\]

This is the first verified induction step using the already proved (n=10)
case.  The next task is to extract the general even-arity induction: prove
combinatorially that every physical Cut simplex factors into smaller even
polygons, that maximal simplices are quadrangulations, and that the odd Thom
normal determinant cancels the Koszul permutation character in every degree.

The executable audit is
`research/voevodsky/check_n12_physical_cut_induction_gate.py`.
