# Common history forces the interval-cycle quotient but does not make it a Green radical

## Question

What quotient is canonically determined by common radial history, and when may its kernel be identified with a Green radical?

## Claim boundary

On each ratio block, common history canonically determines the quotient of the polarized edge source by interval cycles. Every form pulled back through common history has a radical containing that cycle space. Equality holds only if the downstream form is nondegenerate on the common-history range. This quotient is distinct from both the minimal endpoint–Wronskian balance and any label-diagonal G4 Green radical.

## Canonical feature quotient

Let \(C_D\) be the projective edge source in ratio block \(D\), and let

\[
B_D:C_D\longrightarrow\mathcal H_D
\]

be common radial history. The interval-graph audit gives

\[
\ker B_D=Z_1(G_D).
\]

Therefore \(B_D\) factors uniquely through

\[
q_D:C_D\longrightarrow C_D/Z_1(G_D)
\]

as

\[
B_D=\widetilde B_Dq_D,
\]

where \(\widetilde B_D\) is injective onto \(\operatorname{ran}B_D\).

This is the maximal quotient forced by the feature map: two source packets have the same common history exactly when they differ by an interval cycle.

## Pulled-back forms

Let \(h_D\) be any continuous sesquilinear form on the common-history range. Pull it back to the edge source:

\[
G_D(c,d)
=
h_D(B_Dc,B_Dd).
\]

Every interval cycle lies in its radical:

\[
Z_1(G_D)
\subseteq
\operatorname{rad}G_D.
\]

If \(h_D\) is nondegenerate on \(\operatorname{ran}B_D\), then the reverse inclusion follows:

\[
G_D(c,d)=0\text{ for every }d
\Longrightarrow
h_D(B_Dc,y)=0\text{ for every }y\in\operatorname{ran}B_D
\Longrightarrow
B_Dc=0.
\]

Hence

\[
\operatorname{rad}G_D=Z_1(G_D)
\]

under precisely that nondegeneracy hypothesis.

Without it, the Green radical can be strictly larger than the feature kernel.

## Three distinct null mechanisms

The repository now contains three typed kernels that must not be identified automatically.

### Interval-cycle kernel

\[
Z_1(G_D)=\ker B_D.
\]

It arises when shell and theta path provenance is erased into common history.

### Minimal radial balance

\[
\rho_\pm=0,
\qquad
e_\pm=\frac12w_\pm.
\]

It arises when endpoint and Wronskian channels are codiagonalized into the derivative source.

### Green-form radical

\[
\operatorname{rad}G.
\]

It is defined only after a specific continuous Green form and metric have been declared. It equals a feature kernel only after nondegeneracy on the feature range is proved.

These objects live at different stages and can coexist.

## Reciprocal descent

Reciprocal exchange carries \(Z_1(G_D)\) isomorphically to \(Z_1(G_{-D})\). Therefore it descends canonically to

\[
\overline R_D:
C_D/Z_1(G_D)
\longrightarrow
C_{-D}/Z_1(G_{-D}).
\]

No forest choice is needed for quotient descent. The greedy chord port supplies coordinates on the lost cycle sector when faithful polarized recovery is required.

## Source-ray restriction

The source-fixed completed-theta ray meets \(Z_1(G_D)\) trivially after shell reconstruction. Thus quotienting by cycles preserves that one source ray, while still losing generic polarized packets. Preservation of one ray does not prove nondegeneracy of a Green form on the full quotient.

## G4 conformance test

A common-history G4 witness must expose enough data to decide:

1. whether its source map is \(B_D\) or a richer labelled feature;
2. whether it quotients by \(Z_1(G_D)\);
3. which form is placed on \(\operatorname{ran}B_D\);
4. whether that form is nondegenerate there;
5. whether the endpoint–Wronskian balance is imposed before or after the cycle quotient.

Only answers to items 3 and 4 can identify the cycle quotient with a Green radical.

## Disposition

Common history canonically authorizes the interval-cycle quotient and reciprocal descent. It does not by itself authorize the name Green radical. The current G4 interface omits the downstream form and its range nondegeneracy, so radical identification remains blocked. No RH conclusion is authorized.
