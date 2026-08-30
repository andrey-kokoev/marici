# Two source additions force a shared moving-seam corner

## Objective

The first Euler–theta comparison cell contains one moving window. The next
gate is whether two labelled additions compose without fitting a coherence
term afterward.

## Source shifts

Let

\[
F(z)=\int_0^\infty\phi(v)e^{zv}\,dv
\]

and let \(S_a\) be the normalized source shift through length \(a>0\). Write
\(q_a=e^{-sa}\), with \(s=1/2+z\), and define

\[
B_a(z)=\int_0^a\phi(v)e^{zv}\,dv.
\]

The undivided endpoint identity is

\[
E_zS_a\phi=q_a(F-B_a).
\]

Since source shifts form a semigroup,

\[
S_bS_a=S_{a+b}=S_aS_b.
\]

Therefore the mixed endpoint coefficient is forced:

\[
E_zS_bS_a\phi=q_aq_b(F-B_{a+b}).
\]

No logarithm and no division by \(F\) is used.

## Complete two-addition section

Introduce formal addition amplitudes \(\varepsilon\) and \(\delta\). The
source-derived section is

\[
\begin{aligned}
F_{\varepsilon,\delta}
={}&F
+\varepsilon q_a(F-B_a)
+\delta q_b(F-B_b)\\
&+\varepsilon\delta q_aq_b(F-B_{a+b}).
\end{aligned}
\]

The bare Euler scalar product contributes

\[
(1+\varepsilon q_a)(1+\delta q_b)F.
\]

Their exact difference contains three typed seam cells:

\[
-\varepsilon q_aB_a
-\delta q_bB_b
-\varepsilon\delta q_aq_bB_{a+b}.
\]

The mixed window is not derivable by merely summing the two first-order
windows. It is the shared corner created by composing the two source shifts.

## Order coherence

The total window has two source-derived shell decompositions:

\[
B_{a+b}=B_a+B_{a,b}=B_b+B_{b,a},
\]

where

\[
B_{a,b}=\int_a^{a+b}\phi(v)e^{zv}\,dv,
\qquad
B_{b,a}=\int_b^{a+b}\phi(v)e^{zv}\,dv.
\]

The intermediate windows differ, but both paths reach the same total interval
state. Their coherence is interval concatenation, not fitted equality of
scalar residuals.

Consequently:

- addition order may retain different intermediate seam states;
- the completed mixed coefficient is order independent;
- omitting \(B_{a+b}\) leaves an exact second-order residual;
- equality only after scalar projection is insufficient unless the shared
  interval state is present.

## Relation to cyclic Euler grades

For distinct independent Euler loops, the logarithmic determinant is additive
and carries no mixed cyclic cumulant. The mixed term above belongs to the
undivided endpoint section and its chart comparison, not to a new primitive or
square cumulant. This keeps the determinant grading separate from the
state-composition corner.

Repeated addition of the same loop is different: its second cyclic return is
the square grade. The comparison architecture must distinguish repeated-loop
cyclicity from composition of two labelled shifts.

## DPC verdict

Resolved:

- the exact undivided two-addition endpoint section;
- the shared moving-seam corner;
- order coherence by interval concatenation;
- separation of mixed section composition from cyclic determinant grades.

Withheld:

- a completed operator colligation realizing these cells;
- reciprocal dagger compatibility;
- locally uniform control over infinitely many additions;
- the zero-state-to-flux implication.

The finite falsifier is the mixed coefficient after deleting the total window:
the residual is \(-q_aq_bB_{a+b}\), nonzero whenever the source has nonzero
mass on the total interval.

## Verification

The checker `check_two_addition_shared_seam_corner.py` verifies the complete
formal section, both shell decompositions, order independence, and the exact
mixed residual produced by deleting the shared corner.
