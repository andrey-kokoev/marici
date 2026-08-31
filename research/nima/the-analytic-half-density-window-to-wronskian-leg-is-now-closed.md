# The analytic half-density window-to-Wronskian leg is now closed

## Reconciliation

The new explicit four-front trace does not stand alone.  Combined with the
existing exponential-conjugation theorem, it closes the analytic portion of
the corrected window-to-Wronskian comparison.

The existing theorem constructs

\[
H_-=U_-^{-1}H_0U_-,
\qquad
H_+=U_+^{-1}H_0U_+,
\]

as closed maps

\[
H_-:\mathcal E_-\to\mathcal H_-,
\qquad
H_+:\mathcal E_+\to\mathcal H_+,
\]

with continuous renormalized outgoing traces

\[
\operatorname{Tr}^{-}_{+}H_-g=M_-(g),
\qquad
\operatorname{Tr}^{+}_{+}H_+g=M_+(g).
\]

Reflection exchanges the two graph spaces and prime/grade translation gives
closed labelwise copies commuting with finite cutoffs.

## Admission of the four-front packet

For every prime \(p\),

\[
b_p
=U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0,
\qquad f_0(q)=e^{-\pi q^2},
\]

is a finite sum of translated Gaussians.  Multiplication by
\(e^{\pm q/2}\), differentiation, and every polynomial source weight preserve
Gaussian integrability.  Hence

\[
b_p\in\mathcal E_-\cap\mathcal E_+.
\]

The twisted histories and both endpoint traces are therefore defined on this
packet in the already completed graph spaces.

## Exact analytic output

The trace computation gives

\[
M_-(b_p)=-m_p,
\qquad
M_+(b_p)=m_p,
\]

where

\[
m_p
=2e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)>0.
\]

Thus

\[
w_{1/2}(b_p)=0,
\]

and

\[
j_{1/2}(b_p)=\sqrt2m_p=s_p^{(1/2)}>0.
\]

This proves on the declared completed analytic carrier that the adjacent
window boundary packet lands purely in the reciprocal-odd Wronskian trace
line, with no completion-wall component.

## Closed analytic properties

The following gates are now jointly closed for the analytic leg:

1. **graph closedness:** inherited by exponential conjugation from \(H_0\);
2. **common packet domain:** \(b_p\in\mathcal E_-\cap\mathcal E_+\);
3. **continuous traces:** inherited from the relative endpoint theorem;
4. **reciprocal exchange:** reflection swaps the two twisted channels;
5. **prime diagonality:** each translated label remains in its own fiber;
6. **cutoff naturality:** label projections commute with both histories and
   traces;
7. **odd purity:** \(M_-(b_p)+M_+(b_p)=0\);
8. **normalization:** the odd trace is the explicit positive
   \(s_p^{(1/2)}\).

Therefore the earlier instruction to “construct the twisted graph domains and
compute their window traces” is superseded.  Both tasks are complete.

## Remaining mate square

What is still missing is arithmetic, not analytic. Because the four-front
packet contains only the displacements \(L\) and \(2L\), one must prove that
the source constructor sends its retained arithmetic boundary generator
through the primitive/square Euler-to-theta incidence to

\[
\kappa_p^{(\le2)}\Phi',
\qquad
\kappa_p^{(\le2)}=\kappa_p^{(1)}+\kappa_p^{(2)}.
\]

The connected tail \(\kappa_p^{(\ge3)}\) cannot enter this strict two-endpoint
cell before a separately authorized return.

and through the analytic completion leg to the same normalized odd line, so
that

\[
\begin{array}{ccc}
\text{boundary four-front line} & \longrightarrow &
\text{twisted history odd trace}\\
\downarrow && \downarrow\\
\text{Euler prime-power line} & \longrightarrow &
\text{theta/Wronskian odd line}
\end{array}
\]

commutes with prime and grade labels retained.

If that mate square is proved, its scalar is necessarily

\[
\lambda_{p,\le2}^{(1/2)}
=\frac{-\kappa_p^{(\le2)}}{2s_p^{(1/2)}}>0,
\]

and the transported linking magnitude is

\[
\lambda_{p,\le2}^{(1/2)}s_p^{(1/2)}
=-\frac12\kappa_p^{(\le2)}.
\]

The already established determinant margin then applies without further
analytic integration.  But scalar equality alone cannot prove the mate
square: it must preserve source labels, half-density metrics, and the
primitive/square/tail split.

## Revised earliest gate

The earliest unresolved local implication is now the labelled arithmetic mate
square.  Analytic graph closure, twisted trace continuity, reciprocal
reflection, cutoff naturality, and the explicit half-density window incidence
are no longer open.

Full-pushout radical descent and global closed range remain open.  No RH
conclusion is authorized.
