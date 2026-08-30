# Spin(5) Spectral-Shape Beta Block Is Not Yet Defined

Work package: WP919

## Question

Does the declared Spin(5) model define the four-coordinate Yukawa
spectral-shape stability block required by WP918?

## Required object

For nondegenerate three-family Yukawa spectra, remove one common scale in each
sector and choose four independent shape ratios

\[
r=(r_{u1},r_{u2},r_{d1},r_{d2}).
\]

A fixed-ray test requires a source-derived beta vector (\beta_r(r,\ldots))
and its stability matrix

\[
B_{\mathrm{shape}}=\frac{\partial\beta_r}{\partial r}\bigg|_{r_*}.
\]

The matrix is meaningful only after the anomaly completion, three-family
Yukawa tensors, scalar couplings, renormalization scheme, and fixed point have
all been declared independently of the desired flavor answer.

## Largest authorized beta record

WP879 supplies two anomaly-compatible completions and their scalar one-loop
Spin(5) gauge coefficients,

\[
b_0^A=\frac92,
\qquad
b_0^B=\frac{13}{2}.
\]

These records distinguish the completions but contain no Yukawa spectral-shape
coordinate. Their Jacobian with respect to (r) is the exact zero matrix,

\[
\frac{\partial(b_0^A,b_0^B)}{\partial r}=0_{2\times4}.
\]

Thus the largest currently authorized flow probe has shape rank zero and a
four-dimensional contextual kernel.

This does not prove that a completed physical beta system has four zero modes.
It proves that its stability block is absent from the declared source packet.
Assigning eigenvalues to an undefined block would convert missing authority
into a spurious theorem.

## Exact hostile pair

WP887--WP888 define a one-family Completion-B component mass constructor. Two
full-rank coefficient points have distinct normalized spectral records,

\[
K_A=\frac{63449}{368082},
\qquad
K_B=\frac{1603}{9680}.
\]

Both share the same completion and hence the same (b_0^B=13/2). The gauge
flow record therefore collapses two explicitly different normalized spectra.
This is the smallest existing exact witness of the shape kernel.

The one-family constructor retains six Yukawa magnitudes and one cycle phase
after rephasing. It deliberately omits three-family Yukawa matrices. It cannot
be reinterpreted as the four physical16 eigenvalue-shape beta coordinates.

## Verdict

The declared Spin(5) packet supplies massability and a shape-blind gauge-flow
record. It is neither a selector nor a rigidifier of physical16 spectral
shape. The WP918 fixed-ray architecture remains conditional because its beta
vector is not yet source-defined.

The next constructor is discrete before it is perturbative: independently
select Completion A or B. Then compile the complete three-family renormalizable
interaction grammar, including every Yukawa tensor and scalar coupling, and
derive the coupled beta vector in one declared scheme. Only that object can be
projected to shape ratios and tested for relevant or zero modes.

The physical instrument remains downstream: after an attractive isolated ray
and threshold survival are proved, jointly measure CP and the four mass-gap
ratios. Detector data cannot supply the missing beta vector.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp919_spin5_spectral_shape_beta_definability_audit.py
~~~
