# Three-placement Keldysh Dyson identity

## Frozen independent-kernel test

Restore independent labels on the left Dyson leg, middle self-energy kernel,
and right Dyson leg:

\[
G_L,qquad G_M,qquad G_R.
\]

Each is a (2\times2) closed-time-path matrix satisfying its own largest-time
identity.  The middle statistical variation carries the cubic vertex signs,
and the typed output is

\[
\delta G_{\rm out}=2G_L
\begin{pmatrix}
G_M^{++}&-G_M^{+-}\\
-G_M^{-+}&G_M^{--}
\end{pmatrix}
G_R.
\]

No equality among the three kernels is imposed.

## Exact RA/Keldysh form

For each kernel (X=L,M,R), define its retarded, advanced, and statistical
coordinates (R_X,A_X,F_X).  Exact Symbolica reduction gives

\[
\boxed{
R_{\rm out}=2R_LR_MR_R,
\qquad
A_{\rm out}=2A_LA_MA_R,
}
\]

and

\[
\boxed{
F_{\rm out}
=2\left(
F_LA_MA_R
+R_LF_MA_R
+R_LR_MF_R
\right).
}
\]

The output obeys the CTP identity identically.  Thus independently labelled
convolution factors preserve the rank-three Gaussian/Keldysh coefficient
object.

## Interpretation

Statistical data may occur in exactly one of the three labelled positions.
The formula is the sum of those three occurrence-resolved placements.  It is
not a single common scalar rescaling in general.

Entry 1588 is recovered only after diagonal identification of the three
kernels.  Its occupation-ratio invariance is therefore a diagonal
specialization, not a generic convolution theorem.

This distinction is structurally useful:

\[
\text{Gaussian object preserved}
\quad\not\Rightarrow\quad
\text{occupation ratio fixed}.
\]

## Next finite falsifier

Insert the actual source Wightman functions and one explicit internal-time
integration domain.  Verify that the three terms retain their labelled
placement and source endpoint orientations.  Then test the ultraviolet order
of each placement separately after Bunch--Davies subtraction.

