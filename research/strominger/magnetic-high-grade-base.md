# Every initialization block is injective in the cone g>=q>1

Let

\[
a_{\max}=q+(q\bmod2).
\]

For `g>=q>1`, choose the source observations

\[
0,\qquad q,
\]

at depth zero and

\[
-g-a,\qquad q-g-a
\]

for every positive even depth `a<=a_max`.  These rows are all distinct in the
high-grade cone.  The interval support graph leaf-peels completely, so the
selected determinant has a unique endpoint product:

\[
\boxed{
D_{g,q}^{\mathrm{base}}
=(q^2-1)\bigl(4^{\overline g}\bigr)^2
\prod_{\substack{2\le a\le a_{\max}\\a\text{ even}}}
\left[
-\bigl(a^{\overline g}\bigr)^2
(a+g-q-1)(a+g+q-1)
\right].
}
\]

Every factor is nonzero when `g>=q>1`: in particular,

\[
a+g-q-1\ge1.
\]

Therefore every such initialization block has full column rank.  The already
proved odd/even boundary and stable transfer laws then propagate injectivity
to arbitrary pole cutoff.

This is the first uniform, unbounded-in-`q` initialization theorem.  It moves
the remaining classification problem entirely into the complementary wedge

\[
g<q.
\]

That localization is structurally appropriate: endpoint rows collide only
when reflection distance exceeds grade, and the genuine `(g,q)=(2,7)` circuit
lies in precisely this wedge.

The checker verifies complete support peeling and exact determinants for 240
generated blocks with `2<=q<=16`, `q<=g<=24`, while the displayed inequalities
and endpoint factors give the arbitrary-parameter proof.
