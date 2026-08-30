# The rank-three odd extension has a one-parameter splitting gauge

## Minimal extension

The universal two-chart boundary has coordinates
\[
(d,p)\in \mathcal B_{\mathrm{even}}\oplus\mathcal B_{\mathrm{odd}}.
\]
To cancel a singular principal-value component while retaining odd orientation, the odd line must be lifted to at least two typed coordinates:
\[
(s,r)\in \mathcal S_{\mathrm{odd}}\oplus\mathcal R_{\mathrm{odd}},
\qquad
q(s,r)=s+r=p.
\]

Here \(s\) is the singular moment coordinate and \(r\) is the retained odd residue. Together with \(d\), this is the rank-three model forced by the preceding scalar no-go.

## Splitting gauge

The quotient map \(q\) does not canonically determine \(s\) and \(r\). For every scalar \(\alpha\), the shear
\[
T_\alpha(s,r)
=
\bigl(s+\alpha(s+r),\,r-\alpha(s+r)\bigr)
\]
satisfies
\[
qT_\alpha=q.
\]

Equivalently, after choosing one decomposition \(p=s+r\), one may replace it by
\[
s_\alpha=s+\alpha p,
\qquad
r_\alpha=r-\alpha p
\]
without changing the observable universal principal-value coordinate.

Therefore the rank-three extension exists algebraically, but the retained residue is not source-defined until a splitting or connecting morphism is supplied.

## Consequence for cancellation

Suppose an external counterterm cancels \(s\), leaving \(r\). Under the shear gauge, the claimed retained orientation becomes
\[
r_\alpha=r-\alpha p.
\]
Its magnitude, and potentially its sign, can be changed without altering the original two-chart sewing.

Thus the requirements

- total principal-value coefficient is correct;
- singular part cancels;
- a nonzero odd residue survives;

do not determine the residue. A fitted decomposition can manufacture any desired residual.

## Source authority needed

A legitimate constructor must freeze the splitting through independent data, such as:

1. a moment map \(M:\mathcal B_{\mathrm{odd}}\to\mathcal S_{\mathrm{odd}}\);
2. a connecting morphism in a relative or mapping-cone sequence;
3. orthogonality in a source-fixed Green form;
4. a causal boundary operator whose kernel defines \(\mathcal R_{\mathrm{odd}}\);
5. an archimedean sewing cell identifying the singular image.

If a projection \(P_{\mathrm{sing}}\) is supplied, then
\[
s=P_{\mathrm{sing}}p,
\qquad
r=(I-P_{\mathrm{sing}})p.
\]
The source must prove \(P_{\mathrm{sing}}\) is continuous, reciprocal-equivariant, prime/cutoff natural, and compatible with the all-order analytic cancellation.

## Completion gate

Finite source authority is still insufficient if the splitting shear grows with cutoff. If \(S_X\) is the chosen extension splitting, completion requires separate uniform bounds
\[
\sup_X\|S_X\|<\infty,
\qquad
\sup_X\|S_X^{-1}\|<\infty
\]
in the declared source topology.

A family can preserve \(q\) exactly while its residue frame becomes singular.

## Hostile

Take \(p\ne0\) and begin with \(s=p,r=0\). Choosing \(\alpha=-1\) gives \(s_\alpha=0,r_\alpha=p\). The same universal principal-value coordinate is described either as entirely singular or entirely residual.

Hence rank enlargement alone explains nothing.

## Revised frontier

The earliest missing constructor is now a source-authorized odd splitting:
\[
0
\longrightarrow
\mathcal R_{\mathrm{odd}}
\longrightarrow
\mathcal E_{\mathrm{odd}}
\longrightarrow
\mathcal S_{\mathrm{odd}}
\longrightarrow
0,
\]
together with the connecting map from the two-chart anti-diagonal class.

Only after this extension class and its splitting law are fixed can the relative interval-history lift be meaningfully constructed.
