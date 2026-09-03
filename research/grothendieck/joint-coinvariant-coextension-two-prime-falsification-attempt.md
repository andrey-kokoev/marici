# Two-prime falsification attempt for the joint-coinvariant coextension

## Target

The surviving conjecture requires the complete normalized prime transfers to admit a minimal faithful regular joint-coinvariant coextension. Every finite coefficient Gram matrix must therefore be positive.

## Strongest existing two-prime attacks

### Orthogonal prime-penalty realization

For primes two and three, the exact centered gamma Gram is

`G(m,n)=F(log m)+F(log n)-F(log(mn))`,

with `F(a)=psi(1/4+a/2)-psi(1/4)`. Subtracting independent diagonal prime costs gives approximately

`[[1.30588065,2.06759606],[2.06759606,1.77538305]]`.

Its determinant is approximately `-1.95651509`. Therefore no Hilbert coextension can realize the complete source by an orthogonal negative coordinate for each prime. This model is decisively falsified at the `2 x 3` block.

### Arithmetic-only squarefree edge realization

On a squarefree prime cube, a kernel with identity value one, single-prime correlations `r_p`, and zero higher squarefree correlations is positive exactly when

`sum_p |r_p| <= 1`.

The raw prime weights are not summable, so independent arithmetic edges cannot admit one global regular dilation with fixed unit diagonal. This kills a second model: separate prime contractions with no completed mixed correlations.

## What survives

Neither counterexample is the complete Weil form. The gamma, endpoint, seam, and additive translation channels generate nonzero mixed correlations. The revised coextension conjecture explicitly requires those complete cross terms, so the two no-go theorems do not falsify it.

They impose a hard structural requirement: the `2 x 3` Brehmer defect must be computed only after assembling the complete source incidence. A diagonal prime penalty or zero mixed composite edge is inadmissible.

## First unavailable object

No current packet provides exact operators `C_2`, `C_3`, and `C_6` on one common radical-reduced short-support Weil block. Existing work proves the complete prime-two block positive and gives scalar/two-prime model no-gos, but not the operator-valued mixed-prime transfer triple.

Without that triple, evaluating

`Delta_(2,3)=I-C_2* C_2-C_3* C_3+(C_2C_3)*(C_2C_3)`

would substitute a model for the conjecture's object.

## Disposition

The strongest available falsification kills both naive independent-prime realizations but does not kill the complete joint-coinvariant coextension. The revised conjecture survives with narrowed scope. Its next acceptance object is the complete `2,3,6` operator triple on a common local Weil form domain; the first test is composition `C_6=C_2C_3`, followed by positivity of the Brehmer defect.
