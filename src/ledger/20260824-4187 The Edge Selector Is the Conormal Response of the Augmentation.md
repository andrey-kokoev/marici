---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 4187 — The Edge Selector Is the Conormal Response of the Augmentation

## Universal weight deformation

Introduce formal edge weights only on the final-deletion routes:

\[
\epsilon_{\boldsymbol\lambda}(a_e)=8C_e,
\qquad
\epsilon_{\boldsymbol\lambda}(b_e)=-8\lambda_e C_e.
\]

The physical source is the point \(\boldsymbol\lambda=\mathbf1\). Entry 2193
proves that the frozen construction does not promote these coordinates to
physical couplings.

Nevertheless, differentiating the augmentation itself at that point is
well typed. On the kernel basis from Entry 2196,

\[
\left.
\frac{\partial}{\partial\lambda_f}
\epsilon_{\boldsymbol\lambda}(p_e)
\right|_{\boldsymbol\lambda=\mathbf1}
=-8C_e\delta_{ef}.
\]

Hence

\[
\boxed{
d\epsilon|_{\ker\epsilon_{\rm ct}}
=-8\operatorname{diag}(C_{12},C_{23},C_{31}).
}
\]

This is exactly Entry 2195's last-edge selector.

## Conceptual classification

The selector is the first fundamental or conormal response of the kernel
under deformation of the augmentation weights. It measures how an invisible
route relation becomes visible when the readout is tilted toward one final
edge.

It is therefore more canonical than an arbitrary route redistribution, but
less physical than a source derivative:

\[
\boxed{
\text{canonical infinitesimal of the augmented presentation}
\;\not\Rightarrow\;
\text{declared cosmological observable}.
}
\]

No physical interpretation is licensed until a source-derived instrument
maps into this weight-normal bundle.

## Evidence

- Entries 2193–2196
- `research/benincasa/checkers/deletion_weight_conormal.rs`