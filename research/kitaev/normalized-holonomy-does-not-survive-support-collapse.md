# Normalized Holonomy Does Not Survive Support Collapse

The cycle-holonomy classifier lives on a fixed nonzero support stratum. It
does not automatically extend to the closure where couplings may vanish.

For an oriented cycle (C), define the unnormalized Wilson product and its
normalized phase by

\[
W_C(z)=\prod_{e\in C} z_e^{\epsilon_e},
\qquad
h_C(z)=\frac{W_C(z)}{|W_C(z)|},
\]

where reverse traversal uses complex conjugation. The polynomial (W_C) is
continuous on the entire coupling space. The phase (h_C) is defined only
where every edge of (C) is nonzero.

There is no continuous extension of (h_C) across (W_C=0). Indeed, any
phase can approach the same zero product along a radial path. Consequently,
the quotient by channel rephasing is stratified by the support graph:

\[
\mathcal M
=
\coprod_{S\subseteq E}
\mathcal M_S,
\qquad
\mathcal M_S/U(1)^V
\text{ has phase rank }\beta_1(S).
\]

When an edge disappears, the support graph can lose a cycle and its phase
coordinate collapses rather than converges to a preferred value.

## Exact positive triangle escape

For (0<\varepsilon\le 1/2), let

\[
M_+(\varepsilon)=
\begin{pmatrix}
2&1/2&-i\varepsilon\\
1/2&2&1/2\\
i\varepsilon&1/2&2
\end{pmatrix},
\qquad
M_-(\varepsilon)=\overline{M_+(\varepsilon)}.
\]

Both matrices are positive definite by strict diagonal dominance. As
(\varepsilon\to0), both converge to the same path matrix, whose support is a
tree. Yet their normalized triangle holonomies remain (+i) and (-i).
Their unnormalized cycle products are

\[
W_+(\varepsilon)=i\varepsilon/4,
\qquad
W_-(\varepsilon)=-i\varepsilon/4,
\]

and both converge continuously to zero.

This is a finite completion-escape witness: every nonzero stage has one phase
port, while the limiting support has cycle rank zero. No amount of finite
injectivity supplies a completion-stable normalized phase.

## Quantitative gate

On a region satisfying

\[
|W_C(z)|\ge\delta_C>0,
\]

normalization is Lipschitz with a constant proportional to
(1/\delta_C\). Therefore a completion-stable holonomy coordinate requires a
uniform nonvanishing bound for each retained cycle product. Without that
bound, the only canonical continuous observation is the unnormalized product
(W_C), which records both amplitude and phase and vanishes when the cycle
breaks.

The alternatives must remain typed:

- normalized holonomy classifies a fixed nonzero support stratum;
- unnormalized Wilson product extends continuously through support collapse;
- an external phase register may preserve a historical phase, but it is then
  additional source memory, not a function of the completed coupling matrix.

## Cross-sector implication

Grothendieck's Hardy inner-factor result has the same information-loss shape:
magnitude or autocorrelation does not retain continuous phase/divisor data.
It is an independent analogue, not authority for this incidence theorem.
Conversely, the present graph theorem does not derive a theta inner factor.

The theta-specific incidence graph remains frozen. Any application must first
derive its support, its allowed channel gauge, and a uniform lower bound if a
normalized phase is claimed to survive completion.

## Falsifiers

- Extending (W/|W|) through (W=0) by assigning a preferred phase.
- Keeping the cycle rank fixed when a support edge vanishes.
- Inferring uniform phase observability from nonzero finite-cutoff products.
- Replacing a normalized phase port by an unnormalized product without
  recording the change of target type.
- Calling an external phase register intrinsic to the completed matrix.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to test whether the cycle-holonomy compiler survives
restricted-product completion.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Normalized holonomy is stratum-local; the unnormalized Wilson product
is the unique obvious continuous replacement at support collapse.
