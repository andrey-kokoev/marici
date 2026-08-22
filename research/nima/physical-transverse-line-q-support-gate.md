# WITHDRAWN — its transverse line was not well typed

> **Status correction.** The branch-to-union maps used to define
> (T_{\rm mix}) fail the complete relation-descent audit.  Consequently this
> specialization census cannot test support of a cohomologically defined
> quotient line.  The finite ranks remain reproducible matrix statistics only.

The rank-one quotient

\[
T_{\rm mix}=V_{\cup}/(V_{23}+V_{31})
\]

was evaluated directly at generic finite-field points of the algebraic quartic
\(\mathcal Q=0\).  Two independent prime/point packets were used:

\[
(p;X_1,X_2,X_3)=(32003;1,2,4182),
\]

\[
(p;X_1,X_2,X_3)=(32009;1,3,30050).
\]

At both points the complete stabilized signature remains

\[
\dim V_{\cup}=26,
\quad
\dim V_{23}=\dim V_{31}=20,
\quad
\dim(V_{23}\cap V_{31})=15,
\]

\[
\dim(V_{23}+V_{31})=25,
\quad
\operatorname{rank}\bigl(\mathrm{II}(s)\bmod(V_{23}+V_{31})\bigr)=1.
\]

Thus the transverse line neither disappears nor becomes inactive on
\(\mathcal Q=0\).  The same quotient presentations remain regular and of
generic rank there.  This is replicated finite-field evidence, not an exact
characteristic-zero factorization, but it falsifies the proposed quartic
support mechanism at the sharpest bounded gate:

\[
\boxed{
\mathcal Q=0\text{ is not the rank-drop or activation divisor of }T_{\rm mix}.
}
\]

The line remains a genuine piece of the physical marked-relative connection,
but it does not explain the special quartic.  Any surviving physical meaning
of \(\mathcal Q\) must therefore require a comparison with an independently
specified moving Betti chain/readout, or a higher extension invariant not
visible in the algebraic marked-relative connection alone.

The evaluations are reproduced by
`checkers/check_physical_union_transverse_line.py` with
`MARICI_FIELD_PRIME` and `MARICI_KINEMATICS` set to the packets above.
