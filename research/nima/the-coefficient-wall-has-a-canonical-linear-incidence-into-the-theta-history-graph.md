# The coefficient wall has a canonical linear incidence into the theta-history graph

## Coefficient wall representation

Let \(e_{\mathrm{wall}}\) be the constant-wall coefficient vector. The
source linear multiplication representation fixes

\[
\pi(e_{\mathrm{wall}})=-I.
\]

At the scalar history level, this is the constant function

\[
J_{\mathrm{in}}e_{\mathrm{wall}}
=
-\mathbf 1.
\]

The sign is source-fixed by the window convention.

## Relative-history carrier

The weighted bilateral relative-history space retains constant functions
through its endpoint coordinates. For \(c\mathbf1\),

\[
(c\mathbf1)'=0,
\qquad
\operatorname{Tr}_-(c\mathbf1)
=
\operatorname{Tr}_+(c\mathbf1)
=
c.
\]

Thus \(-\mathbf1\) is a legitimate wall vector in the relative graph even
though it is not in unweighted \(L^2(\mathbb R)\).

This supplies the previously missing linear upper arrow from the coefficient
wall into the theta-history input wall.

## Theta output

The completed-theta convolution sends a constant to its mass multiple:

\[
H_\Phi\mathbf1=M_\Phi\mathbf1.
\]

Therefore

\[
H_\Phi J_{\mathrm{in}}e_{\mathrm{wall}}
=
-M_\Phi\mathbf1.
\]

The complete wall incidence is the graph vector

\[
e_{\mathrm{wall}}
\longmapsto
(-\mathbf1,-M_\Phi\mathbf1).
\]

Its relative orientation and theta mass are both fixed.

## Quadratic image

The coefficient wall Gram is

\[
R_{\mathrm{coeff}}
=
|e_{\mathrm{wall}}\rangle
\langle e_{\mathrm{wall}}|.
\]

Under the quadratic multiplication representation its input component is

\[
\Gamma_\pi(R_{\mathrm{coeff}})=I.
\]

The output component is

\[
M_\Phi^2I,
\]

and their graph coefficient is

\[
(1+M_\Phi^2)I.
\]

Hence the analytic two-wall graph derived previously is the quadratic image
of this single linear incidence, subject only to the endpoint metric
normalization described below.

## Endpoint metric normalization

With the unscaled relative norm

\[
\|f\|_{\mathrm{rel}}^2
=
\int w|f'|^2
+
|f(-\infty)|^2
+
|f(+\infty)|^2,
\]

a constant satisfies

\[
\|c\mathbf1\|_{\mathrm{rel}}^2=2|c|^2.
\]

Therefore an isometric coefficient-wall incidence uses either

\[
e_{\mathrm{wall}}
\mapsto
-2^{-1/2}\mathbf1,
\]

or a source endpoint metric with half weight on each endpoint.

This factor is not optional. It is the only remaining normalization choice in
the wall arrow.

The existing Wronskian endpoint columns must decide which convention is
source-authorized.

## Reciprocal character

Reflection fixes \(\mathbf1\) and exchanges the two equal endpoint traces.
Thus the incidence is reciprocal-even. The linear minus sign does not survive
as a negative Gram sign:

\[
(-I)^*(-I)=I.
\]

## What is now closed

The carrier map itself is no longer missing:

\[
e_{\mathrm{wall}}
\longmapsto
-\mathbf1
\longmapsto
-M_\Phi\mathbf1.
\]

It preserves the wall character and produces the exact theta-history graph
transport.

## Remaining wall theorem

The only unresolved wall datum is the source metric coefficient. One must
compare:

1. the coefficient Gram normalization of \(e_{\mathrm{wall}}\);
2. the two endpoint weights in the relative-history norm;
3. the Wronskian trace normalization;
4. any bilateral factor in the theta cosine convention.

Once these agree, the wall part of the quadratic comparison square commutes
exactly.

## Hostile

Map \(e_{\mathrm{wall}}\) to \(-\mathbf1\), call the map isometric, and
forget that the two endpoint traces contribute twice. The linear history is
correct while the quadratic wall coefficient is off by a factor of two.

## Frontier

The first Adams comparison no longer lacks a wall incidence. It lacks only
the endpoint-metric calibration of that incidence, plus the already isolated
front/derivative quadratic Green descent.
