# The Finite QD Census Is Not a Dual-Number Module

Entry 512 tested whether frozen elementary Koszul columns descend to the
purported dual-number homology of the authoritative finite census.  A prior
gate is now checked: whether the admitted exact image

\[
I_D=\langle\widehat H(A_D),E(P_D)\rangle\subset G_D
\]

is stable under multiplication by `u`.  Exact matrix ranks give

\[
\begin{array}{c|c}
D&\operatorname{rk}(I_D+uI_D)-\operatorname{rk}I_D\\\hline
12&16\\
16&22\\
20&28\\
24&34
\end{array}
\]

The stable law is `3D/2-2`.  Thus

\[
uI_D\nsubseteq I_D,
\]

so the finite quotient `Q_D=G_D/I_D` does not inherit an action of
`Q[u]/(u^2)` under the accepted whole-column cutoff.

This changes the interpretation of the previously accepted census.  The
quantity printed as

\[
t_D=2\dim(Q_D/uQ_D)-\dim Q_D
\]

is only a rank statistic formed from the full matrix and its frozen-row
restriction.  The frozen restriction is not literally `Q_D/uQ_D`, and `t_D`
is not a torsion or Bockstein-homology dimension.

Accordingly, Entry 512's cycle defects remain valid matrix obstructions, but
there is no actual `H(Q_D,u)` on which its proposed filtration could live.
Adding `u`-corrections to representatives cannot repair this: the ambient
finite quotient must first be replaced by a genuinely `u`-linear object.
Merely saturating `I_D` under `u` would choose a repair after the fact.  The
next construction must instead be derived from the labelled
principal-gradient total complex, retaining the principal cell and its
coherence data before any quotient, specialization, Bockstein, or Koszul
homology is taken.  Only after that construction proves module descent may
the finite census be interpreted as nearby-cycle data.

The methodological consequence for the cosmology sector is therefore

\[
\boxed{\text{finite specialization census}\not\Rightarrow
\text{nearby-cycle module}.}
\]

The `Q`-sector must be located functorially in a Rees/Gauss--Manin complex;
it cannot be inferred from rank patterns in a quotient on which the
deformation parameter does not act.
