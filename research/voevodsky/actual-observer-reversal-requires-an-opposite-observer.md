# Actual observer reversal requires an opposite-observer contract

## Exact witness

Using the actual 51,550-generator, 3,591-row assembled presentation, define R by reversing words and marks and mapping the corner (a,b) to (63 xor b,63 xor a). This is the candidate orientation reversal on square-free source paths.

Generator 36, in corner (0,11), is the zero-mark source relation

    z = [1,0,3] - [0,1,3].

Its full exported observer column is zero. Its reversal lies in corner (52,63):

    Rz = [3,0,1] - [3,1,0].

The checker reconstructs Rz exactly as source generator 51502 minus generator 51506, establishing membership in the exported source ideal. Actual observer row 2719 is the coefficient functional for the zero-mark path [3,0,1] in that corner. Consequently

    O(z)=0,   O(Rz)[2719]=1.

The owning raw row independently confirms the value one; no symbolic nonvanishing or numerical calibration assumption is needed.

## Consequence

The kernel of this observer is not invariant under this reversal. Hence no map on the same observer quotient can satisfy Rbar O = O R throughout the exported source domain: the representatives z and zero would require different images.

This refutes same-observer reversal descent. The broader conjecture explicitly allowing a separately transported opposite observer remains open. It also does not provide two physically admitted histories: these are elements of the authoritative linear ideal-source domain. History admission and extension matching remain separate obligations.

An algebraic candidate for the opposite observer is Oop=O R^{-1}, wherever R is established on the full relevant source domain. Its kernel is R(ker O), making quotient transport possible by construction. Checking that this transported observer is an authorized protocol with the required source actions, filtration and analytical semantics is substantive further work.

## Verification and limits

    python research/voevodsky/checkers/check_actual_observer_reversal_descent.py

The checker binds the presentation to its input hashes, searches zero exported columns, reconstructs the reversed ideal element in the rational source basis, and independently evaluates the nonzero owning raw row. Artifact: `results/actual-observer-reversal-descent.json`.

This run uses the existing full presentation; it does not freshly rebuild or independently verify all 51,550 columns. It tests an explicit reversal candidate and establishes a representative-independence obstruction for the same quotient. It does not settle coherent continuation descent or construct the full opposite observer.
