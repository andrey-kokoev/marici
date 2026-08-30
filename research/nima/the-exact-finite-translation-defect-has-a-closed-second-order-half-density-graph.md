# The exact finite translation defect has a closed second-order half-density graph

## Second derivative under half-density transport

The first derivative intertwiner is

\[
\mathcal M_nD_x
=
n^{-1}e^{-u}
\left(\partial_u-\frac12\right)
\mathcal M_n.
\]

Let

\[
B=\partial_u-\frac12.
\]

Since

\[
B(e^{-u}g)
=
e^{-u}
\left(\partial_u-\frac32\right)g,
\]

applying the first-order identity twice gives

\[
\mathcal M_nD_x^2
=
n^{-2}e^{-2u}
\left(\partial_u-\frac32\right)
\left(\partial_u-\frac12\right)
\mathcal M_n.
\]

Define

\[
T^{(2)}
=
e^{-2u}
\left(\partial_u-\frac32\right)
\left(\partial_u-\frac12\right).
\]

Then the label-(n) second derivative is exactly \(n^{-2}T^{(2)}\).

## Closed maximal realization

Take \(T^{(2)}\) on its maximal distributional domain in
\(L^2(\mathbb R)\). If

\[
f_k\to f,
\qquad
T^{(2)}f_k\to g
\]

in \(L^2\), then on every compact interval multiplication by \(e^{2u}\)
is bounded, and

\[
\left(\partial_u-\frac32\right)
\left(\partial_u-\frac12\right)f_k
\longrightarrow
e^{2u}g
\]

distributionally. Passing to the limit proves

\[
T^{(2)}f=g.
\]

Thus the maximal second-order operator is closed.

## Enlarged joint carrier

Let

\[
T^{(1)}
=
e^{-u}
\left(\partial_u-\frac12\right),
\qquad
S=-\partial_u^2+\frac14.
\]

The exact translation-defect domain is

\[
\mathcal D_{S,T^{(1)},T^{(2)}}
=
\operatorname{dom}S^{1/2}
\cap
\operatorname{dom}T^{(1)}
\cap
\operatorname{dom}T^{(2)}
\]

with graph norm

\[
\|f\|_{(2)}^2
=
\|f\|^2
+
\|S^{1/2}f\|^2
+
\|T^{(1)}f\|^2
+
\|T^{(2)}f\|^2.
\]

Because all three component operators are closed, this intersection is
complete.

## Source Gaussian core

For

\[
f_j(x)=x^je^{-\pi x^2},
\]

the half-density image has left asymptotic

\[
\mathcal M_nf_j(u)
\sim
n^{j+1/2}e^{(j+1/2)u}.
\]

Naively, the factor \(e^{-2u}\) could destroy integrability for \(j=0,1\).
But the indicial factors cancel the leading Taylor terms:

\[
\left(\partial_u-\frac12\right)e^{u/2}=0,
\]

and

\[
\left(\partial_u-\frac32\right)e^{3u/2}=0.
\]

The next Gaussian Taylor term supplies sufficient decay. Hence the even wall
seed and odd curvature seed both lie in the second-order graph domain.

This cancellation is source-specific and would be lost in an arbitrary
Sobolev completion.

## Label-uniform suppression

For every \(n\ge1\),

\[
\|\mathcal M_nD_x^2f\|
=
n^{-2}\|T^{(2)}\mathcal M_nf\|.
\]

Thus the second-order term is more strongly suppressed across theta labels
than the first-order connection term.

## Prime defect bound

The exact prime defect is

\[
\mathcal R_p
=
U_L
\left[
-2L(A+1)D_x+L^2D_x^2
\right],
\qquad
L=\log p.
\]

On the second-order joint carrier, translation is unitary in the comoving
frame and

\[
\|\mathcal R_pf\|
\le
2L\|(A+1)D_xf\|
+
L^2\|D_x^2f\|.
\]

After label transport, the two terms carry \(n^{-1}\) and \(n^{-2}\),
respectively.

## Remaining qualification

The graph closure proves domain validity and closability. It does not prove
that the Stieltjes Green energy controls the full second-order graph norm.
Quadratic Green functoriality must either:

- transport this stronger graph energy from the source;
- show the \(D_x^2\) term is form-controlled by completion;
- or retain it as a separate even auxiliary channel.

## Frontier

The domain obstruction introduced by the exact quadratic translation defect
is closed:

\[
D_x^2
\longleftrightarrow
n^{-2}T^{(2)}
\]

on a complete source Gaussian graph.

The remaining analytic problem is energy domination and prime-weighted
assembly, not closability of the finite defect.
