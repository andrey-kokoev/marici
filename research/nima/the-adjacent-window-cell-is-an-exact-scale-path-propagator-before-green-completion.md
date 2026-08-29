# The adjacent window cell is an exact scale-path propagator before Green completion

## Continuous scale path

For \(t>0\), the reciprocal window is

\[
W_t(q)=H(q+t)-H(q-t),
\]

where the Gaussian tail satisfies

\[
H'(x)=-e^{-\pi x^2}.
\]

Fix a prime \(p\) and put

\[
L=\log p.
\]

The primitive and square windows are the endpoint states

\[
W_L,
\qquad
W_{2L}.
\]

The adjacent bulk cell is

\[
\alpha_{p,1}=W_{2L}-W_L.
\]

## Exact propagation identity

Differentiate along the scale path:

\[
\partial_tW_t(q)
=
-e^{-\pi(q+t)^2}
-e^{-\pi(q-t)^2}.
\]

Therefore the fundamental theorem of calculus gives

\[
\alpha_{p,1}(q)
=
\int_L^{2L}\partial_tW_t(q)\,dt.
\]

Equivalently,

\[
\alpha_{p,1}(q)
=
-\int_{q-2L}^{q-L}e^{-\pi v^2}\,dv
-\int_{q+L}^{q+2L}e^{-\pi v^2}\,dv.
\]

This is the missing non-diagonal geometry at the window level. The source does not insert a translation kernel between two unrelated atoms; it supplies the full path

\[
t\longmapsto W_t,
\qquad
L\le t\le2L.
\]

## Chain-homotopy interpretation

Let

\[
\operatorname{ev}_L,
\qquad
\operatorname{ev}_{2L}
\]

be endpoint evaluation on the scale-path bundle, and let

\[
D_t=\partial_t.
\]

Then integration along the interval defines a homotopy operator \(K_{[L,2L]}\) satisfying

\[
K_{[L,2L]}D_t
=
\operatorname{ev}_{2L}-\operatorname{ev}_L
\]

on the window family.

Thus \(\alpha_{p,1}\) is an exact chain homotopy between primitive-scale and square-scale endpoint evaluation. This is stronger than support overlap and weaker than the desired Green/Stokes theorem.

## Oriented boundary

The interval orientation gives

\[
\partial[L,2L]=[2L]-[L].
\]

Accordingly,

\[
W_{2L}-W_L
\]

has the square endpoint positive and primitive endpoint negative. Reversing the path reverses \(\alpha_{p,1}\).

This supplies the source-fixed sign frame required by the wall-character selection theorem.

## Why a diagonal kernel fails

A pointwise scale kernel has support only on

\[
t=t'.
\]

It pairs endpoint atoms at \(L\) and \(2L\) to zero. The path propagator instead retains every intermediate scale \(t\in[L,2L]\). Any nonzero primitive-to-square mixed form must factor through this interval history or through an independently authorized equivalent.

The source path therefore supplies a necessary continuation constructor without fitting a translation.

## What is still missing

The identity above transports analytic windows, not yet the typed arithmetic endpoint currents

\[
p^{-1/2}\delta_L,
\qquad
\frac12p^{-1}\delta_{2L}.
\]

The next theorem must lift the endpoint current maps into a path rigging on which \(D_t\) has a Green identity.

Let \(\mathcal H_p\) be the history space over \([L,2L]\). Seek trace maps

\[
\tau_L:\mathcal H_p\to E_P,
\qquad
\tau_{2L}:\mathcal H_p\to E_Q,
\]

and a closed first-order history operator \(\mathcal D_p\) such that

\[
\langle\mathcal D_pu,v\rangle
+
\langle u,\mathcal D_pv\rangle
=
\langle\tau_{2L}u,\tau_{2L}v\rangle_Q
-
\langle\tau_Lu,\tau_Lv\rangle_P.
\]

The endpoint forms must use their distinct primitive and square riggings.

## Candidate mixed identity

With the independently derived incidence lifts \(L_{P,p}\) and \(L_{Q,p}\), the desired mixed form must be induced by the history propagator:

\[
b_{\alpha,p}(x,y)
=
\left\langle
L_{Q,p}^*y,\,
\mathsf U_p(2L,L)L_{P,p}^*x
\right\rangle,
\]

where \(\mathsf U_p(2L,L)\) is derived from the closed history problem and has

\[
W_{2L}-W_L
\]

as its boundary defect.

The notation does not assert that \(\mathsf U_p\) already exists. It states the exact operator that the window homotopy must induce.

## Rigged-domain gate

The history space cannot use one ordinary \(L^2\) trace norm for both endpoints:

- the primitive current requires exponential/Laplace rigging;
- the square current is tempered but non-finite.

The Green identity must therefore be a rigged correspondence, with a canonical test-dual transpose before any Hilbert adjoint.

## Closability gate

At finite regularization, define history forms \(b_{\alpha,p}^{(\epsilon)}\). The required limit is not merely

\[
b_{\alpha,p}^{(\epsilon)}(x,y)\to b_{\alpha,p}(x,y)
\]

on selected vectors. The limiting graph must be closable, equivalently its adjoint domain must be dense in the declared target rigging.

A convergent scalar boundary value can coexist with a nonclosable distributional graph.

## Normalization

The path generator transports geometry only. It must not absorb arithmetic coefficients. The endpoint maps remain

\[
L_{P,p}\sim p^{-1/2},
\qquad
L_{Q,p}\sim\frac12p^{-1}.
\]

Moving a factor of \(p^{1/2}\), \(2\), or \(p\) into the propagator changes its source type and is forbidden without an authorized metric transport law.

## New frontier

The non-diagonal continuation constructor now exists exactly at the analytic-window level:

\[
W_L
\xrightarrow{\ t\in[L,2L]\ }
W_{2L}.
\]

The remaining irreducible theorem is to promote this scale-path chain homotopy to a closed rigged Green history whose endpoint traces are the independently fixed primitive and square incidence maps.

That promotion, rather than invention of a translation kernel, is the precise Adams-edge construction problem.
