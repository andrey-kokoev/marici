# Theta tail--seam closability is an exact adjoint-range problem

## Bounded surviving route

Packet 154 proves that the seam cannot be a bounded function of the retained
tail. The remaining graph presentation begins with compactly supported
translation packets `c(p)` and the two synthesis operators

\[
 (Gc)(t)=\int_0^\infty\Phi(t+p)c(p)\,dp,
\]

\[
 (Hc)(t)=\int_t^\infty\Phi(p-t)c(p)\,dp.
\]

Here `Gc` is the retained tail feature and `Hc` is the seam-crossing feature.
The algebraic orbit relation is

\[
 \Gamma_0(Gc)=Hc.
\]

This packet assumes the required injectivity or quotient by `ker G` so that
the relation is well-defined. That gate must be checked separately.

## Exact adjoints

For real `Phi`, the tail operator is the symmetric Hankel operator

\[
 G^*=G.
\]

Fubini gives the seam adjoint

\[
 (H^*y)(p)=\int_0^p\Phi(p-t)y(t)\,dt.
\]

Thus `H^*` is the forward Volterra convolution complementary to the
backward seam synthesis `H`.

## Adjoint domain of the orbit relation

A vector `y` belongs to `Dom(Gamma_0^*)` exactly when there is a tail vector
`z` satisfying

\[
 \langle Hc,y\rangle=\langle Gc,z\rangle
\]

for every packet `c`. Equivalently,

\[
 H^*y=G^*z=Gz.
\]

Therefore

\[
 \operatorname{Dom}(\Gamma_0^*)
 =\{y:H^*y\in\operatorname{Ran}G\}.
\]

The standard closability criterion now becomes the concrete source theorem

\[
 \Gamma_0\text{ is closable}
 \quad\Longleftrightarrow\quad
 \{y:H^*y\in\operatorname{Ran}G\}\text{ is dense}.
\]

This is the precise next gate.

## Why the norm-ratio no-go does not decide closability

The individual orbit vectors satisfy `g_p -> 0` in tail norm while `h_p`
retains norm. But `h_p` translates toward infinity and need not converge
strongly to a nonzero vector. Hence this sequence proves unboundedness but
does not by itself violate the graph-closure condition.

A genuine nonclosability witness requires packets `c_n` with

\[
 Gc_n\to0,
 \qquad
 Hc_n\to y\ne0
\]

strongly. Equivalently, failure of density in the boxed adjoint domain
provides a separating vector.

## Transform interpretation

The operators have different geometries:

- `G` is Hankel, depending on the sum `t+p`;
- `H` is a one-sided correlation, depending on the difference `p-t` with
  `p>=t`;
- `H^*` is Volterra convolution.

Thus closability asks whether the Volterra images `H^*y` can be approximated
densely through the range of the Hankel source operator. This is not a scalar
Euler-product question and cannot be decided by comparing their kernels only
on the diagonal.

## Full-state interpretation

If `Gamma_0` is closable, its graph norm is

\[
 \lVert x\rVert_{\Gamma}^2
 =\lVert x\rVert_{\rm tail}^2
 +\lVert\overline\Gamma_0x\rVert_{\rm seam}^2.
\]

This is exactly the direct-sum relationship energy in a graph presentation.
It prevents the translated orbit from escaping because the seam norm remains
visible.

If `Gamma_0` is not closable, the seam cannot even be encoded as a closed
unbounded function of the tail. It must be retained as a genuinely
independent component or as a multivalued closed linear relation.

## Smallest decisive tests

There are now two exact falsifiers:

1. **Well-definedness failure:** find a nonzero packet `c` with `Gc=0` but
   `Hc!=0`.
2. **Closability failure:** find `c_n` with `Gc_n->0` and `Hc_n->y!=0`, or
   prove that `{y:H^*y in Ran G}` is not dense.

Neither can be replaced by a finite matrix condition unless the finite spaces
and their inclusions approximate the graph topology faithfully.

## Present obstacle

The RH programme has reached a concrete analytic range problem:

\[
 \text{Is the preimage }(H^*)^{-1}(\operatorname{Ran}G)
 \text{ dense for the completed theta source }\Phi?
\]

No existing source theorem in the programme answers it. Solving it requires
the range theory of the theta Hankel operator relative to the Volterra seam
operator, or abandonment of the graph presentation in favor of the explicit
direct-sum state.

