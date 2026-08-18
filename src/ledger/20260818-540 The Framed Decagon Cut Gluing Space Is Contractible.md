---
id: 540
date: 2026-08-18
title: The Framed Decagon Cut Gluing Space Is Contractible
---

# The Framed Decagon Cut Gluing Space Is Contractible

Entry 539 proves that the physical associator obstruction vanishes on every
top simplex of the decagon Cut nerve.  This entry determines the remaining
gluing choices without enumerating the full loaded decagon carrier.

The exact region profiles on all Čech strata are:

\[
\begin{array}{c|c}
\text{stratum}&\text{factor profiles}\\ \hline
15\text{ vertices}&10(4,8)+5(6,6)\\
55\text{ edges}&55(4,4,6)\\
55\text{ triangles}&55(4,4,4,4).
\end{array}
\]

Thus every factor appearing anywhere in the nerve has arity (4), (6), or
(8).  The four-point factor is the primitive unit, the six-point framed line
is unique by Entries 421 and 436, and the eight-point framed line is rigid by
Entry 537.  Products of these pointed contractible mapping spaces remain
pointed and contractible.

Consequently the relative deformation and automorphism diagrams are zero in
all Čech degrees:

\[
C^0_{m rel}=C^1_{m rel}=C^2_{m rel}=0.
\]

Entry 539 supplies the missing existence datum: the unique local points obey
strict triple coherence, so they define an actual global section rather than
a family obstructed by an associator.  The homotopy limit is therefore
terminal:

\[
\boxed{\text{the framed decagon Cut gluing space is contractible}.}
\]

In particular, the fourteen ambient top classes of Entry 538 neither obstruct
nor deform the framed physical line once its primitive boundary values are
fixed.  A full (850{,}000+)-generator loaded decagon enumeration is not
needed for this framed rigidity theorem.

This closes the (n=10) Cut descent problem in the cellular fs/Kato sector.
The next structural question is whether the argument inducts over all even
arities.  The first honest test is (n=12), whose Cut strata can contain an
(n=10) factor.  One should enumerate its nerve, verify that every stratum
factors into previously rigid even arities, and test the four-Cut permutation
character and top obstruction before stating an induction theorem.

The executable audit is
`research/voevodsky/check_n10_framed_cut_gluing_rigidity.py`.
