# Corrected support-window scaling exposes vanishing margins

## Problem

Does the certified first-prime construction retain a usable margin as the support admits additional Mangoldt terms?

## Bold conjecture

The same concentration decomposition retains a positive margin bounded away from zero across increasing support windows.

## Named rivals

1. the margin collapses at the next prime threshold;
2. fixed frequency cutoff or polynomial degree creates the apparent collapse;
3. an endpoint normalization defect controls the sign.

## Strongest falsification attempt

The initial scout used the polar endpoint matrix

\[
a_+a_-^*+a_-a_+^*.
\]

The source formula instead contains the half-sum of the two polar evaluations, requiring

\[
\frac{a_+a_-^*+a_-a_+^*}{2}.
\]

The omitted factor \(1/2\) was a checker defect. It generated the previously reported negative next-window values and invalidated that disposition.

After repair, a 400-node, degree-159 floating scout gives selected-block minima

\[
\begin{array}{c|c|c}
L & \{n:\log n\leq2L\} & \lambda_{\min}(F)\\
\hline
0.35 & \{2\} & 5.5940963\times10^{-4}\\
0.55 & \{2,3\} & 2.3345909\times10^{-8}\\
0.70 & \{2,3,4\} & 1.7281115\times10^{-13}.
\end{array}
\]

At \(L=0.9\) and \(1.1\), the reported negative values are only \(4\times10^{-15}\), at floating roundoff scale. These are not evidence of mathematical negativity. The trace residual remains below \(1/130\) in every row.

The corrected directed first-prime pipeline still passes all 25 \(LDL^*\) pivots, but its minimum pivot lower bound falls from the invalid \(0.242885\ldots\) to

\[
0.0017645830061413439.
\]

## Disposition

Rival 3 is verified: the endpoint normalization defect caused the apparent next-window falsifier. The first-prime theorem for the coded form survives after repair. Rival 1 remains a serious scaling obstruction: the floating selected margin loses roughly four orders of magnitude at the next prime threshold and reaches numerical zero by \(L=0.9\). No uniform positive margin follows from these samples, and a fixed-window computation cannot promote them to RH.

The source-identity gate remains independently open: the repository still lacks a fully instantiated compact-support identity contract and Dirichlet comparison map. Until that object is supplied, these calculations remain statements about the explicitly coded form.

## Verification

- `research/voevodsky/checkers/scout_support_window_scaling.py`
- `research/voevodsky/results/support_window_scaling_scout.json`
- `research/voevodsky/checkers/check_arb_cutoff_form_legendre_matrix.py`
- `research/voevodsky/results/arb_cutoff_form_legendre_matrix.json`
