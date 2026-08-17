# Multigrading Removes the Higher-Rees Coefficient Ambiguity

## Result

Entry 384 deliberately computed the endpoint-relative target after forgetting
the source and its occurrence shifts.  In that ungraded shadow,

\[
H_0(K_\partial)\simeq(x_0,x_1)
\]

and the first \(x_3\)-Rees symbol does not see
\(x_3^2(x_0,x_1)\).

That observation does not produce a deformation of the already fixed
generic/lower component of \(\mathfrak R_{03}\).  The established incidence
maps are multigraded of degree zero.  In the multidegree forced by Entry 378,
the chain equation

\[
x_3a+\frac{X_{D03}}{u_{D03}}k=0
\]

has the homogeneous solutions

\[
(k,a)=
c\left(x_3,-\frac{X_{D03}}{u_{D03}}\right).
\]

Indeed, after multiplying by \(u_{D03}\), the equation is

\[
x_3(u_{D03}a)+X_{D03}k=0.
\]

The occurrence variables \(x_3\) and \(X_{D03}\) are coprime.  Thus
\(x_3\mid k\) and \(X_{D03}\mid u_{D03}a\), giving precisely the common
factor \(c\) displayed above.

Fixing the primitive realization degree forces \(c\) to have multidegree
zero.  Over the polynomial occurrence base, \(c\) is therefore an integer.
The positive first Cartier symbol fixes \(c=+1\).  Consequently

\[
\boxed{
k=x_3,\qquad
a=-X_{D03}/u_{D03}
}
\]

is unique in its fixed multidegree.

In particular,

\[
\deg(x_3^2x_0)=2\epsilon_3+\epsilon_0,
\qquad
\deg(x_3^2x_1)=2\epsilon_3+\epsilon_1
\]

differs from \(\deg(x_3)=\epsilon_3\).  Neither higher-Rees witness can be
added to the \(q_J\)-component of a degree-zero realization.

## Compatibility with the endpoint kernel

The weighted road shifts also remain homogeneous.  For the simultaneous
endpoint kernel

\[
R\langle e_2\rangle
\xrightarrow{(-x_0,x_1)}
R\langle e_3,e_4\rangle,
\]

the inverse occurrence weights are

\[
\deg(e_2)=-\epsilon_4,\quad
\deg(e_3)=-\epsilon_0-\epsilon_4,\quad
\deg(e_4)=-\epsilon_1-\epsilon_4.
\]

Hence

\[
\epsilon_0+\deg(e_3)
=\epsilon_1+\deg(e_4)
=\deg(e_2).
\]

This verifies that the ideal found in Entry 384 is a genuinely graded target
module.  It does **not** yet compute the degree-zero Hom from the source
thimble into that module.

## What is now closed

There is no longer a higher-Rees coefficient ambiguity in the fixed
generic/lower map.  The following data are rigid:

1. \(q_J\mapsto x_3q_{03}^Q\);
2. the lower coefficient \(-X_{D03}/u_{D03}\);
3. the first Cartier symbol \(+1\); and
4. the two endpoint purity restrictions of Entry 381.

The low-cognition delegated audit independently identified the exact
degree equation

\[
\deg(s)=\deg(\text{coefficient})+\deg(\text{target generator})
\]

and correctly refused to promote the conclusion without source shifts.  The
present result supplies the already established source--target shift for the
generic/lower pair, so uniqueness is unconditional for that pair only.

## Remaining boundary

This does not prove uniqueness or existence of the endpoint connector.
Entry 384's ideal may still contribute through a different source generator.
To decide that, one must retain the individual multidegrees of

\[
H_{\rm Morse}p-\widetilde\xi h_3,\qquad
q_Jp,\qquad
d\widetilde\xi\,h_3
\]

and calculate the degree-zero complex

\[
\underline{\operatorname{Hom}}_{\rm gr}
(\mathcal K_{03}^{\rm face},K_\partial).
\]

That is now the smallest unresolved computation.  If its \(H^0\) vanishes,
the realization is coefficientwise unique and only a connector homotopy
remains.  If it does not, its explicit homogeneous generators replace the
ungraded ideal as the true deformation space.

## Evidence

research/voevodsky/check_d03_rees_multigraded_uniqueness_gate.py
verifies the road shifts, the homogeneous chain equation, the common-factor
classification in a bounded exponent census, the fixed-degree unit, and the
degree mismatch of the two higher-Rees witnesses.

## Outcome contract

~~~json
{
  "claim": "The fixed-degree D03 generic/lower realization has the unique coefficient pair (x3,-XD03/uD03), with positive Cartier symbol +1. The target-only x3^2(x0,x1) sector cannot perturb that component because it has the wrong occurrence multidegree.",
  "status": "proved_scoped_multigraded_uniqueness",
  "closed": [
    "generic coefficient",
    "lower Cech coefficient",
    "first Cartier scalar"
  ],
  "not_closed": [
    "degree-zero source-to-endpoint Hom",
    "endpoint connector homotopy",
    "reflection parity",
    "full mixed-variance realization"
  ],
  "next_experiment": "Extract the source shifts of the three-face thimble cell and compute the degree-zero graded Hom into the endpoint-relative road complex."
}
~~~
