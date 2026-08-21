# The Five-Site Positive Selector Does Not Descend at Branch Quotients

For a formal branch subset \(B\), Entry 1224 identifies sheets differing
inside \(B\). This gives the deck-set quotient

\[
q_B:(\mathbb Z_2)^5
\longrightarrow
(\mathbb Z_2)^5/\langle B\rangle.
\]

Suppose the corresponding Betti chain specialization

\[
(q_B)_*:\mathbb Q[G]\to\mathbb Q[G/\langle B\rangle]
\]

exists.  A generic-sheet functional descends through it precisely when it
annihilates \(\ker(q_B)_*\), equivalently when it is constant on every
quotient fiber.

The frozen positive-sheet selector is

\[
\delta_{0,G}(g)=
\begin{cases}
1,&g=0,\\
0,&g\ne0.
\end{cases}
\]

For every nonempty \(B\), the zero fiber contains both \(0\) and a
nonzero \(k\in\langle B\rangle\).  Therefore

\[
\delta_{0,G}(0)=1,
\qquad
\delta_{0,G}(k)=0,
\]

and

\[
\boxed{
\delta_{0,G}
\notin
\operatorname{im}q_B^*.
}
\]

The exact checker audits all 32 formal branch subsets. The positive selector
descends only for \(B=\varnothing\).  The invariant orbit trace is constant
on every fiber and descends in all 32 cases, but Entry 1224 already proves
that replacing the positive chamber by this trace changes the observable.

This Boolean census does not assert that every simultaneous branch locus is
geometrically realized. The later exact control in
five-site-branch-geometry-vs-boolean.md finds, on a generic complex
three-dimensional model, nonempty strata only through triple intersections;
quadruple and quintuple subsets are empty. On the real Euclidean chamber,
distinct branches do not meet. The physical conclusion nevertheless follows
already at codimension one: each of the five individually realized branch
quotients fails the selector-descent test.

## Consequence

The physical gate closes more strongly than “chain pushforward not yet
constructed.”  Even if the source supplies \((q_B)_*\), the frozen
positive-sheet readout does not descend through any nontrivial branch
geometrically realized branch quotient. A branch value requires
nearby-cycle/limiting data that retains
the approach sheet, or a new physical prescription replacing the selector.

The algebraic coefficient transfer

\[
(q_B)_!\delta_{0,G}=\delta_{0,G/\langle B\rangle}
\]

remains true, but it has the wrong variance for descent of the
coefficient--Betti pairing.  It cannot repair this obstruction.

Artifacts:

- `research/nima/check_five_site_branch_selector_descent.py`
- `research/nima/results/five-site-branch-selector-descent.json`
