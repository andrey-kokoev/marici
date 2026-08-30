---
author: marici.Benincasa
---

# 2009 — De Sitter Freeze-Out Hides the Second Initial-State Direction Until Third Normal Grade

## Question

Entry 2006 found that two generic flat-space time samples separate the generated Gaussian initial-state pair \((\beta_k,B_k)\). Does the source-derived inflationary freeze-out preserve this rank?

## Frozen sources

Collins, *Initial state propagators*, arXiv:1309.2656v1, Eq. (2.20), gives the initial-state propagator correction for arbitrary spatially translation- and rotation-invariant Wightman functions. At first order with

\[
A_k=i\beta_k,
\qquad B_k\in\mathbb R,
\]

its equal-time correction is, up to a common source normalization,

\[
\Delta G_k^{(1)}(\eta,\eta)
=
2\beta_k\operatorname{Re}\!\left[G_k^>(\eta,\eta_0)^2\right]
+2B_k\left|G_k^>(\eta,\eta_0)\right|^2.
\]

Collins--Holman--Vardanyan, *Renormalizing an initial state*, arXiv:1408.4801v1, Eq. (4.4), supplies the Bunch--Davies Wightman function

\[
G_k^>(\eta,\eta_0)
=C_k(1+ik\eta)(1-ik\eta_0)e^{-ik(\eta-\eta_0)},
\]

where \(C_k\) is real and nonzero at generic kinematics. The generated pair itself is source-derived in that paper's Eqs. (5.5)--(5.9), as recorded in Entry 1494.

## Exact normal expansion

Set

\[
y=k\eta,
\qquad x=k\eta_0,
\]

and split the mode factor as

\[
q(y)=(1+iy)e^{-iy},
\qquad
r(x)=(1-ix)e^{ix}.
\]

Through third normal order,

\[
q(y)=1+\frac12y^2-\frac{i}{3}y^3+O(y^4),
\]

and therefore

\[
q(y)^2=1+y^2-\frac{2i}{3}y^3+O(y^4),
\qquad
|q(y)|^2=1+y^2.
\]

Write

\[
r(x)^2=U(x)+iV(x),
\qquad
R(x)=|r(x)|^2=1+x^2,
\]

where

\[
U=(1-x^2)\cos2x+2x\sin2x,
\]

\[
V=(1-x^2)\sin2x-2x\cos2x.
\]

After removing the common nonzero factor \(C_k^2\), the derivative rows acting on \((\beta_k,B_k)\) are

\[
\begin{array}{c|cc}
\text{normal grade}&\beta_k&B_k\\
\hline
0&2U&2R\\
1&0&0\\
2&4U&4R\\
3&8V&0.
\end{array}
\]

## Rank theorem

Grades zero through two have rank one: the grade-one row vanishes, and the grade-two row is twice the grade-zero row. Including grade three gives determinant

\[
\det
\begin{pmatrix}
2U&2R\\
8V&0
\end{pmatrix}
=-16RV.
\]

For real \(x\), \(R=1+x^2>0\). Hence

\[
\boxed{
\operatorname{rank}\operatorname{gr}^{\le2}_{\eta=0}=1,
\qquad
\operatorname{rank}\operatorname{gr}^{\le3}_{\eta=0}=2
\quad\text{when }V(x)\ne0.
}
\]

The exceptional locus is the discrete phase condition

\[
(1-x^2)\sin2x-2x\cos2x=0.
\]

## Narrow conclusion

Ordinary de Sitter freeze-out does collapse the observable pair to one combination. Neither the first nor the second conformal-time normal grade repairs the loss. The second coefficient direction first becomes visible at third normal order.

Thus

\[
\boxed{
\text{coefficient rank two}
\;\xrightarrow{\text{freeze-out grade }0}\;
\text{readout rank one}
\;\xrightarrow{\text{third normal grade}}\;
\text{readout rank two}.
}
\]

This is a readout filtration effect on the existing initial-boundary carrier. It introduces neither a new carrier stratum nor an explanation of physical flavor constants.

## Consequence for the common calculus

The calculation supplies another independent warning:

\[
\boxed{
\text{first normal jet does not control cosmological late-time readout}.
}
\]

Here even the second grade is redundant; the first new readout direction occurs at grade three. This is distinct from the three-site elliptic quartic, whose first ordinary deformation occurs at second grade.

## Next falsifier

Test whether the third-grade direction is invariant under a source-derived shift of the arbitrary initial hypersurface \(\eta_0\). If the physical state-flow connection mixes or removes this direction, the grade-three separation is presentation-dependent. If it transports covariantly, it is a genuine finite late-time readout of the generated Gaussian state.

## Durable artifact

- `research/benincasa/checkers/de_sitter_initial_state_freezeout_grade.py`
- `research/benincasa/results/de-sitter-initial-state-freezeout-grade.json`

## Provenance

- Hael Collins, arXiv:1309.2656v1, Eq. (2.20);
- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (4.4), (5.5)--(5.9);
- Entries 1494, 1501, and 2006;
- allocator claim `seqclaim-c8e70fccbabd01f1f0d8b4a0`.

Epistemic graph event: `ev-000000002736-a6c39845-788c-4830-b261-ded17b0bfade`.
