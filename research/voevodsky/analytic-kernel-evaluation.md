# Analytic kernel evaluation signature

## Question

Can the symbolic atoms be assigned the displayed exponential-cosine formulas and extended to an additive evaluation homomorphism without presupposing a particular real-number implementation?

## Claim boundary

The construction is parameterized by a value abelian group, multiplication, exponential, cosine, and halving operations. It builds the displayed terms and their additive extension. It does not supply a concrete real or complex model, prove analytic identities, inequalities, convergence, or completion naturality.

## Construction

`AnalyticKernelEvaluation.agda` defines parameters \(t,z,a,b,\varepsilon,\delta,\tau\) in a value group with the additional operations. It assigns

\[
E=e^{-ta^2}\cos(az),
\qquad
N=-\varepsilon e^{-tb^2}\cos(bz),
\qquad
H=e^{-tb^2}\cos(bz),
\qquad
D=\tau H.
\]

Normalization and deformation atoms map to \(\delta\) and \(\varepsilon\). The free-group recursion then produces an `AbGroupHom` on all symbolic coefficients. The kernel value is defined as \(E+N\), and tail evaluation computes to \(\tau H\).

## Strongest falsification attempt

`negative/DropTauFactor.agda` attempts to identify the tail value with \(H\), omitting \(\tau\). Agda rejects the boundary because the multiplication by \(\tau\) is load-bearing.

## Disposition

The atom assignment and its universal additive extension are now constructed relative to an explicit analytic signature. The remaining first missing object is a concrete value model—real, complex, or a source-authorized function algebra—with proofs that its operations satisfy the required analytic and completion laws. The signature alone supplies no such laws and does not establish source-global naturality.

## Verification

- `research/voevodsky/agda/AnalyticKernelEvaluation.agda`
- `research/voevodsky/agda/negative/DropTauFactor.agda`
- `research/voevodsky/results/cubical_agda_analytic_kernel_evaluation.json`
