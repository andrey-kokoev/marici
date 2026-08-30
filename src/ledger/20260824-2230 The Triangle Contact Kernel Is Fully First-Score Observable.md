---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2230 — The Triangle Contact Kernel Is Fully First-Score Observable

## Rank test

For the triangle contact basis \((p_{12},p_{23},p_{31})\), Entry 2219 gives

\[
\mathcal O_1
=-8\operatorname{diag}(C_{12},C_{23},C_{31}).
\]

At generic finite contact kinematics every \(C_e\neq0\), so

\[
\det\mathcal O_1
=(-8)^3C_{12}C_{23}C_{31}\neq0.
\]

Therefore

\[
\boxed{
K^{(1)}_{\triangle,\rm ct}=0.
}

Every scalar-hidden contact direction is visible with one quadratic Gaussian
score insertion. Higher mixed-score orders are unnecessary for this kernel.

## Qualification

After physical momentum-function pullback, equal edge energies reduce the
available score rank as in Entry 2228. The labelled coefficient-level theorem
and the physical evaluation theorem must remain distinct.

## Evidence

- Entries 2196, 2219, and 2228–2229
- `research/benincasa/checkers/triangle_score_observability.rs`

