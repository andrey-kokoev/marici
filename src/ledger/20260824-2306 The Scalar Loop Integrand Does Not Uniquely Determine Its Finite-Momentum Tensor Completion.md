---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2306 — The Scalar Loop Integrand Does Not Uniquely Determine Its Finite-Momentum Tensor Completion

## Question left by Entry 2304

Could the missing tensor vertex nevertheless be reconstructed uniquely from
the scalar three-site integrand by requiring covariance?

## Covariant ambiguity

Let \(\bar g\) be the conformally flat FRW metric used by the scalar toy
model.  Its Weyl tensor vanishes:

\[
C_{\mu\nu\rho\sigma}[\bar g]=0.
\]

Given any covariant scalar completion \(S_0[g,\phi]\), consider the
one-parameter family

\[
S_\alpha[g,\phi]
=S_0[g,\phi]
+\alpha\int d^4x\sqrt{-g}\,
C_{\mu\nu\rho\sigma}
(\nabla^\mu\nabla^\rho\phi)
(\nabla^\nu\nabla^\sigma\phi).
\]

At \(g=\bar g\), the added term vanishes identically as a functional of
\(\phi\).  Therefore every scalar vertex and every scalar loop integrand on
the frozen background is independent of \(\alpha\).  In particular,
arXiv:2408.16386 cannot distinguish these completions.

The first metric variation is different:

\[
\left.
\frac{\delta(S_\alpha-S_0)}{\delta h_{\kappa\lambda}}
\right|_{\bar g}
=
\alpha\int d^4x\sqrt{-\bar g}\,
\frac{\delta C_{\mu\nu\rho\sigma}}
     {\delta h_{\kappa\lambda}}
(\bar\nabla^\mu\bar\nabla^\rho\phi)
(\bar\nabla^\nu\bar\nabla^\sigma\phi).
\]

This is generically nonzero on a transverse-traceless tensor perturbation.
In a local inertial chart, a tensor wave along the third axis has

\[
\delta C_{0i0j}\propto q_0^2\epsilon_{ij}^{\rm TT}.
\]

For a scalar momentum with
\(p_x^2\ne p_y^2\), the plus polarization gives

\[
p_ip_j\epsilon^{ij}_{+}=p_x^2-p_y^2\ne0.
\]

Hence changing \(\alpha\) changes the finite-momentum
scalar--scalar--tensor vertex while leaving the complete frozen scalar loop
integrand unchanged.

## Result

\[
\boxed{
\text{The scalar rank-twelve source admits inequivalent covariant tensor
completions with identical scalar data.}
}
\]

Covariance, Ward identities, and the scalar Gauss--Manin system therefore do
not reconstruct the missing tensor vertex.  An upstream action together with
its allowed higher-derivative operator content is required.

This is stronger than a missing-formula observation: it is an explicit
nonuniqueness theorem.  A tensor vertex inferred from the scalar integrand
alone would choose \(\alpha\) without source authority.

## Consequence for the active objective

The interacting contextual-faithfulness test splits into:

1. a source-complete generic scalar observer problem, which can proceed now;
2. a tensor completion problem, gated on a separately frozen covariant
   action and EFT truncation.

The hard falsifier remains meaningful after that action is frozen.  Before
then, different finite-\(q\) rank-loss loci could reflect different
covariant completions rather than a Carrier-level obstruction.

## Classification

- existing Carrier: unchanged energy/Cut/Cayley--Menger support;
- scalar coefficient object: source-defined;
- finite-\(q\) tensor coefficient: underdetermined;
- new Carrier datum: none.

## Durable provenance

- Entry 2304;
- arXiv:2408.16386, equations (2.2), (4.15), and (4.21);
- allocator claim `seqclaim-a67b899f4da46d732a851002`.

