# Abelian shaping cannot remove the overlap obstruction

Work package: WP598  
Owner: marici.Figueiredo

## Bounded question

WP597 finds that the common-group invariant
\((\phi\mathbin{\cdot}\psi)^2\) moves the proposed axis-and-diagonal vacuum.
Can ordinary independent abelian shaping charges forbid its complex-field
counterpart without restoring independent generalized CP?

## Charge identity

Give \(\phi\) and \(\psi\) arbitrary additive charges \(q_\phi\) and
\(q_\psi\) under a continuous or finite abelian phase symmetry. The Hermitian
overlap has charge

\[
q(\phi^\dagger\psi)=-q_\phi+q_\psi.
\]

Its conjugate has the opposite charge. Therefore

\[
q\left(\lvert\phi^\dagger\psi\rvert^2\right)=0
\]

identically, for every charge assignment and for every direct product of
abelian phase factors. On the real two-angle slice this invariant is
\(\cos^2(\alpha-\beta)\), exactly the WP597 obstruction.

At \((\alpha,\beta)=(0,\pi/4)\), adding it with coefficient \(\eta/2\)
again gives

\[
\nabla V=
\begin{pmatrix}\eta/2\\-\eta/2\end{pmatrix}.
\]

The checker verifies the symbolic charge identity and exhausts every charge
pair for cyclic groups of orders two through twelve as a finite hostile
census. The symbolic identity supplies the unbounded abelian statement; the
census is a regression witness, not the basis of the theorem.

## Disposition

An abelian shaping charge can forbid a holomorphic bilinear or selected
holomorphic powers, but it cannot forbid the Hermitian modulus of that
bilinear. Therefore phase-charge assignment alone does not repair WP597.
Declaring the overlap coefficient zero would be a fit unless a stronger
source constructor enforces it.

The surviving options are narrower:

- a non-abelian product-selection rule for which the dangerous singlet is
  absent;
- source-derived locality or sequestering that forbids the contact term;
- a different representation whose complete renormalizable invariant ring
  contains no angle-moving singlet.

Each option must be tested against its complete invariant ring. It must also
retain only one common generalized-CP family and leave no stabilizer of the
selected full vacuum.

## Physical instrument gate

WP598 is a source-grammar obstruction, not an experiment. A progressive
architecture must transport both its CP-odd prediction and the interaction
that protects the relative angle into calibrated records. Otherwise a flavor
measurement and a scalar or threshold measurement remain valid objects in
different frames with no admitted parallelization.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp598_abelian_shaping_overlap_no_go.py

The generated result is
research/flavor/results/wp598_abelian_shaping_overlap_no_go.json.
