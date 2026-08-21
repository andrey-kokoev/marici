# Exact one-loop QED Bell onset

## Result

The exact massive-fermion one-loop helicity amplitudes of arXiv:2312.16966v2 were evaluated at the transverse angle using their uniform-transcendental one-loop master-integral basis and below-threshold continuation.

The common normalization cancels from the Bell readout. In the paper's all-incoming convention, the three required channels are

\[
\Phi_1\leftrightarrow\mathcal M_{--++},\qquad
\Phi_2\leftrightarrow\mathcal M_{++++},\qquad
\Phi_5\leftrightarrow\mathcal M_{-+++}.
\]

Before looking for a crossing, the implementation was required to reproduce the low-energy (g_2,f_2,h_3) coefficients. At (y=s/m_e^2=0.01), the stripped amplitudes agree with

\[
\frac{11}{360}y^2,qquad
-\frac1{80}y^2,qquad
-\frac1{10080}y^3
\]

to better than (0.2\%), consistent with the omitted higher powers of (y).

The exact normalized Bell magnitude crosses (2) in the certified numerical bracket

\[
0.4201576087391004
<\frac{s}{m_e^2}<
0.4201576087623835.
\]

Equivalently,

\[
\boxed{\frac{\sqrt{s}}{m_e}=0.6481956562\ldots.}
\]

For comparison, the dimension-ten and dimension-twelve truncated-amplitude estimates were (0.46803) and (0.42369). The dimension-twelve value is already within one percent of the exact result.

Therefore the finite-energy Bell crossing is not an EFT truncation artifact. The exact one-loop QED amplitude produces a transverse fixed-analyzer Bell violation well below the electron-pair threshold.

A symmetric 25-point half-interval census was also performed at (y=0.40) and (y=0.43). In both cases the Bell magnitude decreases monotonically toward the transverse point. At (y=0.40), the transverse value is (1.999093\ldots); at (y=0.43), it is (2.000445\ldots), while every other sampled angle already exceeds (2). Thus the exact crossing closes the last observed angular nonviolation window.

The finite census strongly supports an all-angle interpretation but is not a continuum proof. Two-loop radiative corrections are not included.

## Analytic-branch regression

The auxiliary \((w,z)\) equations have several algebraic solutions. The evaluator therefore validates every numerical root against the paper's below-threshold Region I, II, or III conditions before accepting it. This is essential away from the transverse neighborhood: accepting the first converged root can jump to a nonphysical sheet and create a spurious discontinuity.

A separate 15-point regression grid checks all three crossed master-integral channels at

\[
x\in\{0.1,0.2,0.3\},\qquad
y\in\{0.5,0.6,0.7,0.8,0.9\}.
\]

The largest branch-relation defect is \(1.66\times10^{-36}\), and the largest adjacent \(y\)-step in the Bell magnitude is \(3.41\times10^{-3}\). The low-energy gate, transverse onset, and replicated angular monotonicity are unchanged by this repair.

The defining weight-two GPL integrals were also reduced to closed logarithm/dilogarithm expressions. Forty-eight comparisons across Regions I--III reproduce the direct quadratures to a maximum absolute error of \(3.71\times10^{-36}\). With this faster representation, a 3,072-point angular falsifier at \(y=0.4\), the exact onset, and \(y=0.43\) is strictly decreasing toward the transverse point on every half-interval step. The smallest observed decrease is \(3.91\times10^{-7}\), and the transverse curvature estimate stays positive near \(3.3\).

This is strong global numerical evidence, but it remains distinct from a proof over a continuum. A rigorous result still requires interval enclosures for the logarithms, dilogarithms, algebraic branch variables, and the derivative of the normalized Bell readout.

An Arb prototype now supplies those primitives and rigorously certifies the negative physical Bell derivative at four interior points and on nonzero angular boxes. It also diagnoses why naive adaptive intervals do not close globally: the source helicity formulas contain strong correlated cancellations. A second-order centered form proves the sign on boxes of width \(10^{-10}\). An order-eight Taylor model widens this to \(10^{-7}\), but its interval remainder becomes indeterminate by width \(10^{-6}\), even at 256-bit precision. The next proof technology must therefore use a cancellation-adapted amplitude basis or complex-disk/Cauchy remainder bounds; merely increasing precision does not solve this dependency loss.

## Reproduction

```text
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_exact_qed_bell_onset.py
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_exact_qed_bell_replication.py
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_exact_qed_branch_continuity.py
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_exact_qed_polylog_reduction.py
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_exact_qed_global_angular_audit.py
/home/andrey/miniforge3/envs/sage/bin/sage research/nima/check_exact_qed_angular_interval.sage
```

The durable outputs are the corresponding JSON packets under `research/nima/results/`.
