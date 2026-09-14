# Ordered edge-attachment spectrum reconstructs the primes

## Question

Does the Carrier filtration retain arithmetic information that disappears from its sectorwise contractible unfiltered homotopy type?

## Claim boundary

The result uses the ordered spectrum of minimal singleton-shell edge grades. It does not reconstruct primes from an unordered multiset, from ordinary homology, or from an arbitrary regraded Carrier.

## Spectrum

Let \(p_i\) be the ordered primes and let \(s_i\) be the grade of the minimal edge in shell direction \(i\). Then

\[
s_i=p_i p_{i+1}.
\]

Since \(p_1=2\), the entire prime sequence is recovered recursively:

\[
p_{i+1}=\frac{s_i}{p_i}.
\]

Without supplying the initial prime, any three consecutive spectrum entries recover the interior prime by

\[
p_{i+1}=\gcd(s_i,s_{i+1}).
\]

Thus the ordered grade spectrum contains the adjacent-prime chain.

## Bold prediction

Exact reconstruction succeeds for every tested shell. A unit perturbation of any one spectrum value should be detected by failed divisibility, failed primality, or inconsistency with the neighboring gcd reconstruction.

## Rivals

1. The attachment spectrum carries only growth rates and cannot recover exact primes.
2. Reconstruction requires the prime labels already attached to cells, making the procedure circular.
3. Local grade errors can pass undetected and silently change later reconstructed primes.

## Test

Generate the first 1001 primes but expose to the reconstruction only the 1000 ordered products \(s_i\) and the initial value 2. Require exact recovery of all primes, exact agreement with adjacent-gcd reconstruction, and primality of every recovered value.

For each of the first 200 spectrum positions, replace \(s_i\) by \(s_i+1\) and require the validation procedure to reject the perturbed spectrum. Record the first failed condition.

## Falsifier

Any incorrectly reconstructed prime or undetected unit perturbation falsifies the stated finite test. The all-dimensional formula itself follows directly from adjacent prime products and does not depend on the sample size.

## Computed result

The 1000 ordered edge grades reconstruct all 1001 primes exactly, ending at 7927. Recursive division and adjacent-gcd reconstruction agree, and every recovered value is prime. Each of 200 unit perturbations is rejected immediately by the recursive divisibility condition; none silently contaminates later terms.

## Disposition

The prediction survives and the general reconstruction formula is proved. The filtered ordered edge spectrum contains the exact adjacent-prime chain, while ordinary sector homotopy does not. This is the first explicit recovery of arithmetic source data from attachment grades alone, without interior prime labels. Ordering and the identification of minimal singleton-shell grades remain necessary inputs.
