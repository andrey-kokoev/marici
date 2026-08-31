# The two-endpoint window can mate only the primitive and square Euler incidence

## Granularity correction

The adjacent-window boundary packet

\[
b_p
=U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0
\]

contains exactly the displacements \(L\) and \(2L\).  It has no fronts at
\(kL\) for \(k\ge3\).

The Euler-to-theta incidence, however, splits as

\[
\kappa_p
=\kappa_p^{(1)}+\kappa_p^{(2)}+\kappa_p^{(\ge3)},
\]

where

\[
\kappa_p^{(1)}
=2L p^{-1/2}\Phi'(L),
\]

\[
\kappa_p^{(2)}
=2L p^{-1}\Phi'(2L),
\]

and

\[
\kappa_p^{(\ge3)}
=2L\sum_{k\ge3}p^{-k/2}\Phi'(kL).
\]

Prime and grade labels are part of the source type.  Therefore the
four-front window packet can mate only

\[
\boxed{
\kappa_p^{(\le2)}
:=\kappa_p^{(1)}+\kappa_p^{(2)}.
}
\]

Using the full \(\kappa_p\) in the strict two-endpoint first-Adams cell would
silently compress the connected tail before a source-authorized Schur return.

## Corrected candidate mate

The analytic half-density odd output is

\[
s_p^{(1/2)}
=2\sqrt2e^{1/(16\pi)}
\left(\sinh L-\sinh\frac L2\right)>0.
\]

If the labelled primitive/square mate square commutes, its scalar must be

\[
\boxed{
\lambda_{p,\le2}^{(1/2)}
=\frac{-\kappa_p^{(\le2)}}{2s_p^{(1/2)}}>0.
}
\]

The transported local linking magnitude is then

\[
\boxed{
\ell_{p,\le2}
=\lambda_{p,\le2}^{(1/2)}s_p^{(1/2)}
=-\frac12\kappa_p^{(\le2)}.
}
\]

The connected-tail coefficient must remain in a separate source port:

\[
\ell_{p,\ge3}=-\frac12\kappa_p^{(\ge3)}
\]

only after the constructor supplies its own completed trace and authorized
return into the local cell.

## Sign

Strict theta monotonicity gives

\[
\Phi'(L)<0,
\qquad
\Phi'(2L)<0,
\]

so

\[
\kappa_p^{(\le2)}<0
\]

and therefore

\[
\lambda_{p,\le2}^{(1/2)}>0,
\qquad
\ell_{p,\le2}>0.
\]

Thus the corrected grade restriction preserves the established orientation.

## Determinant margin

Since every summand in \(-\kappa_p\) is positive,

\[
0<-\kappa_p^{(\le2)}<-\kappa_p.
\]

Hence the previously proved uniform estimate for the full incidence implies

\[
\frac{(\kappa_p^{(\le2)})^2}{4}
<
\frac{\kappa_p^2}{4}
<0.006.
\]

Consequently the conditional primitive/square oriented block has the stronger
margin

\[
\Delta_p^{\mathrm{res}}
-rac{(\kappa_p^{(\le2)})^2}{4}
>0.244.
\]

No new scalar estimate is needed after the granularity correction.

## Revised mate square

The next theorem must be gradewise:

\[
\begin{array}{ccc}
\text{fronts at }L,2L & \longrightarrow &
\text{twisted odd trace}\\
\downarrow && \downarrow\\
\text{Euler grades }1,2 & \longrightarrow &
\text{theta/Wronskian grades }1,2.
\end{array}
\]

It must prove the two labelwise identities before summing them.  A scalar
identity involving only their sum is weaker and cannot establish constructor
naturality.

The \(k\ge3\) tail remains a separate unresolved return channel.  Full
radical descent and global closed range remain open.  No RH conclusion is
authorized.
