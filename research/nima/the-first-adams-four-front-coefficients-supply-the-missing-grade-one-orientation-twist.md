# The first-Adams four-front coefficients supply the missing grade-one orientation twist

## Source of the sign

The opposite gradewise signs in the half-density window trace are not an
unexplained defect.  They are already present in the frozen first-Adams target
identity.

In the ordered basis of shifts

\[
(-2L,-L,L,2L),
\]

the exact target coefficient vector is

\[
(1,-1,1,-1).
\]

Grouping reciprocal pairs by positive grade gives

\[
b_p^{(1)}=-U_{-L}f_0+U_Lf_0=-q_L,
\]

\[
b_p^{(2)}=U_{-2L}f_0-U_{2L}f_0=q_{2L},
\]

where

\[
q_a=U_{-a}f_0-U_af_0.
\]

Thus the grade orientation matrix is source-fixed as

\[
\boxed{S_{12}=\operatorname{diag}(-1,+1).}
\]

It is not an ad hoc repair: it is precisely the primitive/square sign pattern
of the proved four-front constructor identity.

## Half-density trace after the orientation matrix

The canonical positively oriented odd traces of the unsigned reciprocal pairs
are

\[
t_{p,1}
:=j_{1/2}(q_L)
=2\sqrt2e^{1/(16\pi)}\sinh\frac L2>0,
\]

\[
t_{p,2}
:=j_{1/2}(q_{2L})
=2\sqrt2e^{1/(16\pi)}\sinh L>0.
\]

The actual window packet has trace column

\[
S_{12}
\begin{pmatrix}t_{p,1}\\t_{p,2}\end{pmatrix}
=
\begin{pmatrix}-t_{p,1}\\t_{p,2}\end{pmatrix},
\]

exactly as found in the gradewise hostile.

The arithmetic Wronskian output column is

\[
a_p
:=
\begin{pmatrix}
-\kappa_p^{(1)}/2\\
-\kappa_p^{(2)}/2
\end{pmatrix},
\]

whose entries are both positive.

## Forced diagonal mate

A scalar mate is the wrong type.  The unique label-diagonal comparison taking
the signed boundary trace column to the arithmetic column is

\[
\boxed{
\Lambda_{p,12}
=
\operatorname{diag}
\left(
\frac{\kappa_p^{(1)}}{2t_{p,1}},
\frac{-\kappa_p^{(2)}}{2t_{p,2}}
\right).
}
\]

Indeed, because \(\kappa_p^{(1)},\kappa_p^{(2)}<0\), its sign pattern is

\[
\operatorname{sgn}\Lambda_{p,12}=(-,+)=S_{12},
\]

and

\[
\Lambda_{p,12}
\begin{pmatrix}-t_{p,1}\\t_{p,2}\end{pmatrix}
=
\begin{pmatrix}
-\kappa_p^{(1)}/2\\
-\kappa_p^{(2)}/2
\end{pmatrix}.
\]

Equivalently, separating orientation from positive magnitude,

\[
\Lambda_{p,12}=S_{12}D_{p,12},
\]

where

\[
D_{p,12}
=
\operatorname{diag}
\left(
\frac{-\kappa_p^{(1)}}{2t_{p,1}},
\frac{-\kappa_p^{(2)}}{2t_{p,2}}
\right)>0.
\]

## What is closed

The missing grade-one sign is now source-authorized by the already proved
four-front constructor coefficients.  Therefore the sign obstruction is
closed:

- grade one carries the constructor minus sign;
- grade two carries the constructor plus sign;
- the arithmetic Wronskian outputs remain positive;
- the mate is diagonal by retained grade, not one scalar after grade erasure.

The earlier summed ratio

\[
-\frac{\kappa_p^{(\le2)}}{2s_p^{(1/2)}}
\]

is not the constructor map: summing before applying \(S_{12}D_{p,12}\) loses
the two grade normalizations.

## Remaining theorem

The entries of \(D_{p,12}\) are explicit, but writing the only possible
diagonal map does not yet prove that the arithmetic constructor realizes it
as a continuous mate.  The remaining theorem must show that the established
labelwise four-front source square, exponential-conjugation history square,
and Euler-to-theta sampling square compose to exactly

\[
\Lambda_{p,12}=S_{12}D_{p,12}
\]

before grade summation.

After that, the two linking contributions must be assembled with the resolved
positive form and the connected \(k\ge3\) port must remain separate.  Global
Köthe closed range and radical descent remain open.  No RH conclusion is
authorized.
