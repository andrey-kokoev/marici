# Correction: the theta heat spectral measure is undefined until its Green metric is sourced

The cyclic-orbit reduction is correct, but the instruction to “compute the
spectral measure of \(H_1\)” was premature.

An algebraic source vector and a scale action do not determine a spectral
measure. One also needs a positive Hilbert form in which the action is
symmetric, unitary, contractive, or at least admits a declared functional
calculus.

The scalar heat line

\[
H_1(t)=\sum_{n\ge1}n^2e^{-\pi t n^2}
\]

and the recurrence

\[
D\,\operatorname{span}\{H_1,M_0,\ldots,M_k\}
\subseteq
\operatorname{span}\{H_1,M_0,\ldots,M_{k+1}\}
\]

determine algebraic cyclicity. They do not determine inner products between
two scale translates of \(H_1\). Different positive metrics on the same
orbit produce different spectral densities and different Hankel kernels.

For example, the abstract orbit

\[
a\longmapsto e^{-au}
\]

has Gram

\[
\int_0^\infty e^{-(a+b)u}w(u)\,du
\]

for any positive weight \(w\). The algebraic semigroup is unchanged, while
\(w(u)=1\), \(w(u)=u^\alpha\), and discrete \(w\) give different boundary
orders and multiplicities.

Therefore the Euler residue cannot be matched by reading a spectral measure
from the scalar theta formula alone. The source-authorized order is:

1. derive the polarized theta heat Green form;
2. quotient its radical;
3. prove compatibility of logarithmic scale transport with that form;
4. then take the cyclic spectral measure of \(H_1\);
5. compare it with the Euler Hankel density.

This returns the programme to the earlier polarization gate, now with a sharp
normalization target. The missing form \(\mathfrak g_{\mathrm{heat}}\) must
satisfy, for the boundary-scale orbit \(h_a\),

\[
\mathfrak g_{\mathrm{heat}}(h_a,h_b)
\sim
\frac{4}{\zeta(3/2)^2}\frac1{a+b}.
\]

The asymptotic is a test of a source-derived form, not a definition of that
form.

A natural \(L^2(dt/t)\), Dirichlet, or heat-energy metric may be analytically
convenient, but none is authorized merely because it yields the desired
density. Its authority must come from the complete theta Green/Stokes
identity and external boundary incidence.

The sharp hostile places the same \(H_1\) orbit in two inequivalent weighted
Hilbert spaces. Both preserve the scale semigroup algebraically; one has flat
spectral density and the other \(u^\alpha du\). Any argument using only the
recurrence cannot distinguish them.

Thus the exact earliest missing constructor is again visible:

> source-polarized theta heat Green form before spectral completion.

Once that form exists, the Euler residue supplies a stringent, computable
cross-chart audit of its cyclic spectral measure.
