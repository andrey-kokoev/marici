# The prime-square current is the first port that rejects the positive convolution hostile

## Connected expansion of the hostile

For the positive even convolution packet from the preceding theorem, write
`r=exp(z)` and `u=exp(-z)`. In the right convergence chamber,

\[
1+\frac45\cosh z
=\frac25e^z(1+2u)(1+\tfrac12u).
\]

Removing the invertible monomial and taking the connected logarithm gives

\[
\log[(1+2u)(1+\tfrac12u)]
=\sum_{k\ge1}
\frac{(-1)^{k+1}}{k}(2^k+2^{-k})u^k.
\]

The first two coefficients are

\[
a_1=\frac52>0,
\qquad
a_2=-\frac{17}{8}<0.
\]

Thus the hostile passes a primitive-sign test and first violates positive
connected Fock grammar at grade two.

## Why the grade matters

For an Euler bosonic factor, the connected prime-power coefficients have the
same positive primitive sign at every grade. The hostile imitates that sign at
`k=1`; inspecting primitives alone does not reject it. The prime-square
current is the first typed port that distinguishes the hostile before any
zero is located.

This supplies a concrete constructor-level meaning for retaining the `k=2`
boundary channel separately from both the primitive current and trace-class
tail:

```text
k=1  accepts the hostile primitive
k=2  detects the first forbidden connected sign
k>=3 continues the alternating defect
```

Discarding the square current during determinant regularization erases the
earliest exact witness that the positive convolution factor is not generated
by the authorized Euler/Fock source grammar.

## Scope

This proves source discrimination, not RH. Standard finite-place Fock data do
not reject an independently modified archimedean carrier. The result explains
why the square current is necessary in a complete boundary-bearing normal
form; an additional archimedean coupling law is still required for global
zero confinement.

## Durable verification

- Checker: `checkers/check_prime_square_rejects_convolution_hostile.py`
- The checker verifies the exact factorization and connected coefficients
  through six grades, including the first sign failure at grade two.
