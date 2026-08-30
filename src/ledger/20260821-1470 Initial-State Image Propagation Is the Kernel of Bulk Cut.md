---
author: marici.Benincasa
---

# 1470 — Initial-State Image Propagation Is the Kernel of Bulk Cut

## Status

Explicit source-level Cut/restriction calculation for the free internal line
of Collins--Holman, arXiv:hep-th/0507081v1, Eqs. (3.13)--(3.17). This is the
first nonzero supported comparison class in the Big-Bang/background-boundary
lane.

## Frozen propagator

For times \(t,t'>t_0\), the source massless propagator with general initial
boundary condition is

\[
G_k(t,t')
=
G_{k,\mathrm{vac}}(t,t')
+
G_{k,\mathrm{img}}(t,t'),
\]

where

\[
G_{k,\mathrm{vac}}
=
\vartheta(t-t')\frac{i}{2k}e^{-ik(t-t')}
+
\vartheta(t'-t)\frac{i}{2k}e^{ik(t-t')},
\]

and

\[
\boxed{
G_{k,\mathrm{img}}(t,t')
=
\frac{i}{2k}e^{\widetilde\alpha_k}
e^{ik(2t_0-t-t')}.
}
\]

The source structure function is

\[
e^{\widetilde\alpha_k}
=
\frac{k-\kappa_k}{k+\kappa_k}.
\]

## Boundary factorization

Set

\[
b_k(t)=e^{-ik(t-t_0)}.
\]

Then the image term is exactly rank-one:

\[
\boxed{
G_{k,\mathrm{img}}(t,t')
=
\frac{i}{2k}e^{\widetilde\alpha_k}
b_k(t)b_k(t').
}
\]

It factors through the initial hypersurface coefficient line. Restriction of
one endpoint gives

\[
i^*G_{k,\mathrm{img}}(t')
=
\frac{i}{2k}e^{\widetilde\alpha_k}b_k(t'),
\]

which is generically nonzero.

## Bulk Cut

In the source Wightman decomposition, the same image term occurs in
\(G_k^>\) and \(G_k^<\). Therefore it cancels from the bulk spectral
discontinuity:

\[
\boxed{
G_k^>-G_k^<
=
G_{k,\mathrm{vac}}^>-G_{k,\mathrm{vac}}^<,
\qquad
\operatorname{Cut}_{\rm bulk}G_{k,\mathrm{img}}=0.
}
\]

Explicitly,

\[
G_k^>-G_k^<
=
\frac{\sin k(t-t')}{k},
\]

independent of the initial-state structure function.

## The comparison kernel

The two operations detect different parts of the source propagator:

\[
\operatorname{Cut}_{\rm bulk}
\quad\text{forgets}\quad
G_{\rm img},
\]

while

\[
i^*
\quad\text{retains}\quad
G_{\rm img}|_\Sigma.
\]

Thus boundary restriction does not factor faithfully through the ordinary
bulk Cut quotient. Its canonical relative kernel is

\[
\boxed{
\mathcal L_{\rm img}(k)
=
\mathbb C\left\langle
\frac{i}{2k}e^{\widetilde\alpha_k}b_k
\right\rangle_\Sigma.
}
\]

This line is source-defined; no splitting or fitted endpoint term has been
introduced.

## Classification

\[
\boxed{
\text{existing background boundary support}
+
\text{rank-one initial-state coefficient excess}.
}
\]

The result is not a new bulk energy/Cut carrier incidence. It is precisely a
supported coefficient class on the already declared stratum \(\Sigma\). It
demonstrates concretely why the cosmological comparison must be relative:

\[
\text{bulk Cut data}
\not\Rightarrow
\text{initial-boundary data}.
\]

This strongly supports H2's support-sensitive calculus and falsifies any
stronger claim that ordinary bulk Cut completely determines a general
initial-state cosmological observable.

## Next finite falsifier

Insert one source boundary operator from Entry 1468 and one bulk interaction
connected by this propagator. Compute whether the boundary counterterm
differential kills, renormalizes, or extends \(\mathcal L_{\rm img}\). The
calculation must retain:

- the boundary-condition parameter \(\kappa_k\);
- normal derivatives at \(\Sigma\);
- the boundary-local operator grading;
- bulk and boundary variance separately.

Only a residual class outside the boundary operator/counterterm complex would
indicate missing carrier structure.

## Provenance

- Collins--Holman, arXiv:hep-th/0507081v1, Eqs. (3.13)--(3.17);
- Entry 1468;
- allocator claim `seqclaim-aeb70451600e40a13e2d0072`.
