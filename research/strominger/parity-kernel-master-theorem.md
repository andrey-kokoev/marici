# Master parity-kernel theorem for arbitrary admitted depths and cutoffs

Let `g>=2`, let `A` be any finite subset of the nonnegative even pole depths,
and retain any finite Laurent source window `m_min<=m<=m_max`, with the full
target lattice.

The magnetic kernel is spanned by every admitted tower

\[
D_{g,a}=z^{-a}\bar z^{-(g+a-1)},
\qquad a\in A,
\]

together with the following classes when their complete supports are admitted:

\[
E_1^-=1-\bar z^{-2},
\]

\[
E_2^-=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6},
\]

both only at `g=2`.  The second requires `{0,4,6} subset A`; the first
requires `0 in A`.

The electric kernel is spanned only by the branch-sign partners

\[
E_1^+=1+\bar z^{-2},
\]

\[
E_2^+=\bar z^{-8}+3z^{-4}\bar z^2-2z^{-6},
\]

under the same grade, depth, and Laurent-support conditions.  It has no tower
classes.

Equivalently, with visibility indicators `v_1,v_2` for the complete supports
of the two grade-two circuits,

\[
\dim\ker M_g
=\#\{a\in A:m_{\min}\le-(g+a-1)\le m_{\max}\}
+\mathbf1_{g=2}(v_1+v_2),
\]

\[
\dim\ker E_g=\mathbf1_{g=2}(v_1+v_2).
\]

No source cutoff creates a kernel class: it only removes columns from a fixed
map, hiding a tower or making a circuit support incomplete.  No assumption of
consecutive depths is needed.  Any finite `A` is a column restriction of some
consecutive `A_k`, and restriction cannot create a linear dependence.

The complete mechanism theorem is:

\[
\begin{array}{c|c}
\text{object}&\text{result}\\
\hline
\text{one-sheet transport }A&\text{injective}\\
\text{full sheet transport }(A,B)&\text{injective}\\
\text{magnetic projection}&\text{fixed-orbit towers + two odd circuits}\\
\text{electric projection}&\text{two even circuits}\\
\text{joint }(E,M)\text{ observer}&\text{injective}
\end{array}
\]

The arbitrary-set checker exhausts all 32 subsets of `{0,2,4,6,8}`, six
independent Laurent windows, and grades `2<=g<=8`: 1,344 source configurations
for each parity readout.  The unbounded quantifier comes from the proved
consecutive-depth theorem plus the column-restriction argument, not from this
finite audit.
