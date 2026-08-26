# A Zero Upgrades Only the Symmetric Two-Sector Quotient

## Scope correction

The previous next-step formulation was too strong. A zero of the completed scalar does not generally place both reciprocal sector profiles in (H^1).

Let

\[
B_\pm(L)=F_\pm-G_\pm(L),
\qquad
G_\pm\in H^1(0,\infty),
\qquad
G_\pm(L)\to0.
\]

The completed scalar readout is

\[
X=F_++F_-.
\]

Decompose the boundary pair into symmetric and antisymmetric channels:

\[
B_{\mathrm{sym}}=B_++B_-,
\qquad
B_{\mathrm{asym}}=B_+-B_-.
\]

Then

\[
B_{\mathrm{sym}}\in H^1
\quad\Longleftrightarrow\quad
X=0,
\]

whereas

\[
B_\pm\in H^1
\quad\Longleftrightarrow\quad
F_\pm=0
\]

separately. At a generic scalar zero, (F_-=-F_+\ne0). Neither individual profile is in (H^1), while their symmetric aggregate is.

## Small hostile model

Take

\[
B_+(L)=1-e^{-L},
\qquad
B_-(L)=-(1-e^{-L}).
\]

Their symmetric aggregate vanishes identically, but each individual (H^1) norm diverges linearly with the cutoff. Their antisymmetric profile tends to (2).

Thus any proposed theorem requiring simultaneous individual-sector (H^1) admission rejects the very cancellation mechanism a scalar zero represents.

## Correct geometric meaning

The limiting boundary vector is

\[
\mathbf F=(F_+,F_-).
\]

Scalar completion projects it onto the diagonal covector ((1,1)). A zero means

\[
(1,1)\mathbf F=0,
\]

so (\mathbf F) lies on the antisymmetric line. The full relationship has not vanished. Only its symmetric scalar channel has lost the constant mode and entered the finite-energy quotient.

This is exactly the distinction anticipated by the operator: the observed zero is where one projected meaning disappears while a higher relational component survives.

## Revised RH-bearing target

The two-sector problem is not to make both profiles finite-energy. It is to prove that the source-generated boundary vector can enter the antisymmetric line only on the Fourier–Tate unitary seam.

Equivalently, construct a source-derived evolution or conserved current for the projective ratio

\[
\rho(s)=\frac{F_-(s)}{F_+(s)}
\]

without dividing at points where (F_+=0), and prove that the value (ho=-1) is inaccessible off the seam. The ratio is only a local coordinate; the invariant statement is incidence of the boundary line with the antisymmetric subbundle.

This remains nontrivial. Reciprocal symmetry alone permits hostile boundary vectors to cross that line off-seam. The required exclusion must use the labelled source transport or a global current, not the scalar functional equation.

## Verification

The dependency-free checker `research/grothendieck/checkers/two_sector_symmetric_h1_upgrade.py` verifies the hostile model: individual graph energies diverge, the symmetric aggregate has zero energy, and the antisymmetric constant mode survives.
