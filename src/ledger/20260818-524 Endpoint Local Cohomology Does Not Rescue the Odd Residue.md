# Endpoint Local Cohomology Does Not Rescue the Odd Residue

The remaining obvious support choices on the weighted exceptional space are
the endpoint divisors `b=-1` and `b=1`.

At the negative endpoint, the odd residue is

\[
r_7=u a^7(b+1).
\]

It is a regular section divisible by the endpoint equation.  A torsion-free
exceptional line has no nonzero degree-zero section supported only at
`b=-1`; multiplication by `b+1` records vanishing, not local support.
Passing to derived local cohomology produces polar classes modulo regular
sections, not the regular vanishing section `r_7` itself.

At the positive endpoint, `r_7` is nonzero, but Entry 520 gives

\[
\operatorname{res}_{+}(r_7)=D(\operatorname{res}_{+}q_7),
\]

so the retained labelled source contracts it.  Supporting at the union of
the two endpoints combines these two failures and does not create a class.

Standard weighted nearby- or vanishing-cycle constructions also retain the
full filtered differential; Entry 523 then identifies `r_7` as the first
filtration differential of `q_7`.

Thus the weighted blowup, its exceptional divisor, and endpoint local
cohomology do not supply a functor that removes `q_7` while retaining
`r_7`.  The simplest geometrically available support mechanisms are
exhausted.

Any further candidate must introduce independently existing geometry not
present in `Bl_(u,a^2)`: for example an oriented integration-chain boundary
or incidence/Gysin correspondence whose source support excludes `q_7`.
Without such data, the odd rank-one resonance hypothesis is falsified for
the current algebraic model.
