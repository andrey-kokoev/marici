# The primitive-square linking margin survives both saturated and codiagonal assembly

## Two positive arithmetic outputs

After the source-fixed grade orientation matrix is applied, the primitive and
square Wronskian linking magnitudes are

\[
\ell_{p,1}=-\frac12\kappa_p^{(1)}>0,
\qquad
\ell_{p,2}=-\frac12\kappa_p^{(2)}>0.
\]

There are two distinct ways these outputs may appear, depending on the
source-authorized stage of the constructor.

## Saturated assembly

Before codiagonalization, the grade outputs remain in the direct sum

\[
\mathbb C_{p,1}\oplus\mathbb C_{p,2}.
\]

Their squared linking cost is then

\[
E_p^{\mathrm{sat}}
=\ell_{p,1}^2+\ell_{p,2}^2
=\frac14\left((\kappa_p^{(1)})^2+(
\kappa_p^{(2)})^2\right).
\]

This is the correctly typed cost for the selected saturated resolved branch.

## Codiagonal assembly

If a later source-authorized return applies the codiagonal

\[
\nabla(z_1,z_2)=z_1+z_2,
\]

then the linking magnitude becomes

\[
\ell_p^{\nabla}
=\ell_{p,1}+\ell_{p,2}
=-\frac12\kappa_p^{(\le2)},
\]

and the squared cost is

\[
E_p^{\nabla}
=\frac14(\kappa_p^{(\le2)})^2.
\]

Because both \(-\kappa_p^{(1)}\) and \(-\kappa_p^{(2)}\) are positive,

\[
E_p^{\mathrm{sat}}
\le E_p^{\nabla}.
\]

Thus codiagonalization is the more demanding scalar hostile.  It includes the
positive cross term between grades.

## Uniform domination

The full incidence has one additional same-sign tail:

\[
-\kappa_p
=-\kappa_p^{(1)}-\kappa_p^{(2)}-\kappa_p^{(\ge3)}>0.
\]

Therefore

\[
E_p^{\mathrm{sat}}
\le E_p^{\nabla}
<\frac14\kappa_p^2
<0.006.
\]

The resolved area satisfies

\[
\Delta_p^{\mathrm{res}}>0.25.
\]

Hence both possible primitive/square assembly stages obey

\[
\boxed{
\Delta_p^{\mathrm{res}}-E_p^{\mathrm{sat}}>0.244,
}
\]

and

\[
\boxed{
\Delta_p^{\mathrm{res}}-E_p^{\nabla}>0.244.
}
\]

## Typing consequence

This does not authorize premature codiagonalization.  It proves only that the
local scalar positivity margin is robust under either stage once the
corresponding source map exists.

The saturated direct-sum cost is the relevant one for the selected resolved
graph.  The codiagonal cost is a conservative hostile and applies only after
a source-declared return.  Since it is larger, the same uniform estimate
covers both without identifying their carriers.

## Remaining gate

Local scalar positivity no longer distinguishes the saturated and
codiagonalized branches.  The remaining distinction is categorical:

- prove the labelwise mate realizes the explicit diagonal map
  \(S_{12}D_{p,12}\);
- retain the primitive and square outputs separately through the saturated
  Green lift;
- apply a codiagonal only where the constructor declares it;
- prove continuity and radical compatibility of that operation in the common
  completion.

The connected tail and global closed-range problem remain separate.  No RH
conclusion is authorized.
