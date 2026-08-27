# The Prime-Scale Recursion Constructs the Backward Equalizer through the Square Grade

For a prime `p`, put `q=p^(-1/2-z)`. Let `F` be the full half-line theta
transform, `R_p` its `p`-primitive exclusion transform, `B_j` the full seam
integral over `j log(p)`, and `A_1` the primitive one-cell seam integral.

The exact source recursion gives

\[
(1-q)F=R_p-qB_1,
\]

and its restriction to the first seam cell gives

\[
(1+q)B_1=A_1+qB_2.
\]

Elimination yields the all-parameter backward equalizer

\[
(1+q)R_p-qA_1-q^2B_2=(1-q^2)F.
\]

At a scalar zero, the prime-exclusion channel balances independently typed
primitive and square seam currents. It does not vanish. This is the first
explicit mate/equalizer cell in the `3+2+1` architecture through grade two.

The remaining gate is to lift this linear covector identity to the
sesquilinear or exterior-square arithmetic Ward defect without fitting the
lift from the desired result.

Research packet:
`research/grothendieck/the-prime-scale-recursion-constructs-the-backward-equalizer-through-the-square-grade.md`

Exact dependency-free checker:
`research/grothendieck/checkers/check_prime_scale_backward_square_equalizer.py`

The checker passes 5/5 gates.
