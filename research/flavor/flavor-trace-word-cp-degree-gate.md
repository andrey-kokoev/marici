# Trace-word CP degree gate

## Question

WP974 asks whether a renormalizable simultaneous-conjugation invariant of two
Hermitian coefficient fields can select CP orientation. The state domain and
physical16 quotient are those of WP972--WP973. No reference port or oriented
spurion is admitted.

## Reversal theorem

For Hermitian \(X,Y\), complex conjugation reverses every trace word:

\[
\operatorname{tr}(W(X,Y))^*
=\operatorname{tr}(W^{\mathrm{rev}}(X,Y)).
\]

Cyclicity identifies words differing by a cyclic rotation. Exhaustive binary
necklace enumeration shows that every word of length at most five is cyclically
equivalent to its reversal. Every such trace is therefore real and has the
same value on \((X,Y)\) and \((X^*,Y^*)\).

The first reversal-asymmetric binary necklaces occur at length six. The word
\(X^2YXY^2\) is one representative. Its imaginary part changes sign under
complex conjugation and is proportional to the three-family commutator cubic.

## Exact hostile pair

Use

\[
X=\operatorname{diag}(1,2,4),\qquad
Y=\begin{pmatrix}0&1&-i\\1&0&1\\i&1&0\end{pmatrix}.
\]

The vacua \((X,Y)\) and \((X,Y^*)\) agree on every trace word through degree
five but the selected degree-six word has opposite nonzero imaginary parts.
They are the CP-conjugate orientation pair.

## Consequence

A renormalizable two-field trace potential, whose monomials have degree at
most four, cannot select CP orientation. It may have CP-breaking minima, but
they occur in a conjugate fiber that the source action does not distinguish.
This is selection failure, not carrier failure and not a detector kernel.

The smallest algebraic repair is a degree-six CP-odd source term. Admitting it
requires an independently derived orientation object or a changed relational
experiment; writing its coefficient by hand would merely encode the desired
answer. A CP-even action can first distinguish nonzero full-rank magnitude
through still higher-degree combinations, but does not choose its sign.

## Reproduction

Run:

    python research/flavor/checkers/wp974_trace_word_cp_degree_gate.py

The generated result is
research/flavor/results/wp974_trace_word_cp_degree_gate.json.
