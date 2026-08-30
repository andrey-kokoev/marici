# All current classes descend from the finite source window

For consecutive pole depths and counterfactual source parameter \(\beta\ge2\),
let \(M\) denote the ordinary path module and \(K_a\) the current at depth
\(a\). The bounded exact evidence gives

\[
\operatorname{span}\{[K_a]:a\ge0\}
=
\operatorname{span}\{[K_0],\ldots,[K_{\beta-1}]\}
\quad\text{in }\operatorname{coker}M.
\]

This passed all 945 cases with \(2\le\beta\le8\), \(2\le g\le10\),
\(1\le q\le15\), and consecutive cutoff \(N=20\).

The statement is about generated quotient directions, not literal support.
The stronger claim that every \(K_a\) beyond one monotone threshold becomes
ordinary-exact is false: individual tail representatives can disappear and
reappear in noncontiguous patterns. Nevertheless no tail representative adds
a class outside the initial source-window span.

For native magnetism \(\beta=4\), the unbounded current classification
therefore reduces conjecturally to the four boundary classes

\[
[K_0],[K_1],[K_2],[K_3].
\]

Their span has rank two on the low and high wedges and rank one in the middle
band. This converts the growing-cutoff problem into a fixed boundary Fitting
problem.

The generating-germ explanation is that changing depth applies one invertible
unipotent transfer to the complete grade jet, while \(\beta\) specifies the
finite initial source packet. Tail currents are transported presentations of
that packet after quotienting by ordinary paths; they are not new source
classes.

The next proof target is a module recurrence of the form

\[
K_{a+\beta}\in M+\operatorname{span}(K_a,\ldots,K_{a+\beta-1}),
\]

with coefficients derived from the source generating function. Iteration
would prove finite-window generation, after which the two-wedge theorem is a
fixed-size Fitting-minor calculation.
