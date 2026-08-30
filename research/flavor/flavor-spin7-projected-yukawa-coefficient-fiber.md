# Spin(7) Projection Leaves a Yukawa-Coefficient Fiber

Work package: WP923

## Question

Does the WP922 projection that realizes exact Completion A also constrain its
surviving Yukawa interactions strongly enough to begin the spectral-shape beta
calculation?

## Zero-mode interaction census

Admit the exact projected charged packet and the complex Spin(5) spinor Higgs
(Phi_{-1/2}) already typed in WP886. At the four-dimensional zero-mode level,
both conjugate-charge invariants are allowed:

\[
y_-\,4_{-1/2}5_{+1}\Phi_{-1/2},
\]

\[
y_+\,4_{+1/2}5_{-1}\Phi_{+1/2}.
\]

Each has total (U(1)) charge zero and the same Spin(5) (4\otimes5\otimes4)
tensor typing. The WP922 parent uses two labelled bulk spinors with opposite
intrinsic parities. No declared operation exchanges those labels or equates
their interaction coefficients.

## Exact coefficient kernel

The zero-mode census is independent of (y_-) and (y_+). Its response
Jacobian along their magnitudes is therefore the zero matrix and has a
two-dimensional kernel. Field rephasings may move phases, but they cannot erase
the magnitude ratio

\[
r_y=\frac{|y_+|}{|y_-|}.
\]

The smallest hostile pair is

\[
(|y_-|,|y_+|)=(1,1),
\qquad
(1,2).
\]

Both have the same exact projected field packet and gauge symmetries, while
(r_y) equals (1) and (2). Thus exact field-content projection does not
select even the first conjugate-channel ratio.

## Bulk and boundary claim boundary

This packet enumerates allowed four-dimensional zero-mode invariants. It does
not silently assert that both arise from one parity-even bulk vertex. A bulk
orbifold parity or boundary localization can allow, forbid, or independently
renormalize the channels. Their locality and common parent provenance must be
declared before either coefficient enters a beta system.

## Verdict

WP922 is a field-content rigidifier only. It is neither a Yukawa-ratio selector
nor a physical16 selector. The four-coordinate spectral-shape beta block
remains undefined because even its first conjugate-channel magnitude ratio is
free.

The sharp successor is an exchange-reflection involution that swaps
(8_a\leftrightarrow8_b) while reversing the Spin(2) charge. If it is a
symmetry of the complete bulk and boundary action, it can require
(y_+=y_-^*), fixing (r_y=1). But the symmetry must be independently
motivated, compatible with the opposite intrinsic parities, and tested against
all boundary counterterms. Otherwise it merely encodes the desired equality.

No physical detector gate opens before this source relation and its
RG/threshold transport exist.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp923_spin7_projected_yukawa_coefficient_fiber.py
~~~
