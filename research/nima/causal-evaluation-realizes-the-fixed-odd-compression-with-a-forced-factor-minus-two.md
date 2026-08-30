# Causal evaluation realizes the fixed odd compression with a forced factor minus two

## Three objects must not be conflated

The odd endpoint column, the odd history operator, and the synthesized
Stieltjes vector are different types:

\[
j_\theta
\in E_\theta,
\qquad
H_{\mathrm{jump}}:\mathcal E\to\mathcal H_{\mathrm{win}},
\qquad
d_p\in\mathcal H_{\mathrm{win}}.
\]

The source identities are

\[
j_\theta=\frac14S_{\mathrm{ord}},
\qquad
S_{\mathrm{ord}}=-2H_{\mathrm{jump}},
\]

where the first equation is in the endpoint-column representation and the
second is the primitive bilateral Volterra identity.

Therefore

\[
H_{\mathrm{jump}}=-2j_\theta
\]

after applying the declared endpoint-column representation. The factor
\(-2\) is mandatory.

## Evaluation on the four-front source

The Stieltjes source satisfies

\[
d_p=-\frac12S_{\mathrm{ord}}b_p.
\]

Using \(S_{\mathrm{ord}}=-2H_{\mathrm{jump}}\),

\[
d_p
=
H_{\mathrm{jump}}b_p.
\]

Combining the two identities gives

\[
d_p
=
-2\,j_\theta b_p.
\]

Thus causal evaluation realizes the theta-to-window odd synthesis by the
bilinear map

\[
\mathsf E_p:
E_\theta^{\mathrm{odd}}\times\operatorname{span}\{b_p\}
\longrightarrow
\operatorname{span}\{d_p\},
\]

\[
\mathsf E_p(j_\theta,b_p)=d_p,
\]

where

\[
\mathsf E_p(y,b)
=
-2\,\pi_{\mathrm{ord}}(y)b
\]

and \(\pi_{\mathrm{ord}}\) is the endpoint-column operator representation.

## Relation to the rank-one coefficient map

The coefficient-level map

\[
K_p^{\mathrm{odd}}j_\theta=d_p
\]

is the currying of \(\mathsf E_p\) at the fixed source vector \(b_p\):

\[
K_p^{\mathrm{odd}}
=
\mathsf E_p(\,\cdot\,,b_p).
\]

Hence the earlier rank-one formula is realized analytically, but not by
identifying the numerical vector \(j_\theta\) directly with the function
\(d_p\). The missing constructor is evaluation against \(b_p\), including the
factor \(-2\).

This resolves the apparent normalization mismatch between

\[
j_\theta=\frac14S_{\mathrm{ord}}
\]

and

\[
K_p^{\mathrm{odd}}j_\theta=d_p.
\]

## Commuting diagram

On the rapid zero-mass core, the diagram is

\[
\begin{array}{ccc}
E_\theta^{\mathrm{odd}}\otimes\operatorname{span}\{b_p\}
&\xrightarrow{\pi_{\mathrm{ord}}\otimes I}&
\operatorname{Op}(\mathcal E,\mathcal H_{\mathrm{win}})
\otimes\operatorname{span}\{b_p\}\\
\downarrow\mathsf E_p
&&
\downarrow -2\,\operatorname{ev}\\
\operatorname{span}\{d_p\}
&=&
\operatorname{span}\{d_p\}.
\end{array}
\]

For the generator,

\[
-2\,\operatorname{ev}
\left(
\pi_{\mathrm{ord}}(j_\theta)\otimes b_p
\right)
=
-\frac12S_{\mathrm{ord}}b_p
=
d_p.
\]

Every scalar and sign is fixed independently.

## Closure

The bilateral Volterra history is closed on the weighted relative graph, and
\(b_p\) lies in its rapid zero-mass core. Endpoint-column representation is
continuous on the finite odd line. Therefore \(\mathsf E_p\) is continuous on
the source-generated tensor line.

Across primes, its curried map is the already trace-class family

\[
K_p^{\mathrm{odd}}
=
d_p\otimes\ell_{\mathrm{jump}}.
\]

Thus the analytic realization passes to the labelled completed direct sum in
the theta-to-window direction.

## Scope

This closes the linear analytic realization:

\[
\text{theta odd column}
+
\text{four-front source}
\longrightarrow
\text{odd bilateral history}
\longrightarrow
d_p.
\]

It does not yet prove equality of the quadratic Green forms. The remaining
local theorem is now exactly

\[
G_{\mathrm{win},p}
=
(K_p^{\mathrm{odd}})
G_{\theta,p}
(K_p^{\mathrm{odd}})^*
\]

or its correctly oriented form-adjoint variant on reduced supports.

That equality requires both sides to use the same source-derived Green metric
and radical quotient. Linear evaluation alone does not authorize it.

## Hostiles

Omitting the factor \(-2\) sends \(j_\theta b_p\) to \(-d_p/2\).

Using \(+2\) reverses reciprocal orientation.

Applying the theta convolution history instead of the primitive bilateral
Volterra history is untyped unless a kernel-synthesis comparison is supplied.

These distinguish the exact source realization from a fitted rank-one map.

## Verdict

The causal-history trace does implement the unique odd compression. The exact
identity is

\[
d_p
=
H_{\mathrm{jump}}b_p
=
-2j_\theta b_p.
\]

The first Adams edge is therefore closed at the linear, endpoint, orientation,
primewise, and completion-direction levels. The live local gate is purely
quadratic Green-form functoriality.
