# The grade commutator constructs the finite Pauli derivative but not return triangularity

## Question

Is there a source-native finite analogue of additive differentiation on the strict primitive-square seam plane, and does it constrain the enlarged Green return?

## Finite derivative

On the ordered primitive-square basis \((e_1,e_2)\), the normalized Euler current and first jet are the Pauli ports

\[
Y=\begin{pmatrix}0&i\\-i&0\end{pmatrix},
\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The source grade operator is

\[
N=\begin{pmatrix}1&0\\0&2\end{pmatrix}.
\]

Its inner derivation gives

\[
[N,X]=iY,
\qquad
[N,Y]=-iX.
\]

Thus the strict boundary plane already carries a canonical finite differentiation operation: the grade commutator rotates the two source-normalized arithmetic ports with the exact quarter phase. This uses the primitive/square grading rather than scalar phase fitting.

## Return hostile

The same finite plane admits the return

\[
R=X.
\]

With forward and reverse grade projectors

\[
P_+=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
P_-=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\]

one has

\[
P_-RP_+\ne0.
\]

Equivalently,

\[
[N,R]\ne0.
\]

Therefore construction of the finite derivative does not force the Green return to preserve the grade filtration. Reverse triangularity follows only if the physical return is independently proved to intertwine the filtration or its associated graded action.

## Typed outcome

The finite prime-seam derivative half of the requested square is constructed on the strict two-grade arithmetic frame. The comparison into the enlarged wall–history–tail/PV return remains undefined because the physical return constructor is still missing. No arrow from \(\operatorname{ad}_N\) to \(R_p\) follows from the Pauli identities alone.

## Strong falsifier

Any proposed finite comparison must reject \(R=X\) by a source law stronger than existence of \(N\), exact Pauli covariance, or prime-uniform frame positivity. The acceptance test is an explicit identity such as

\[
R_pF^j\subseteq F^j
\]

for the source grade filtration, followed by calculation of \(P_-R_pP_+\). Declaring that identity solely because its failure permits cancellation is circular.

## Verification

`research/aspect/checkers/check_finite_grade_commutator_return.py` verifies the two commutator identities, exact Pauli frame, nonzero reverse return block, and failure of grade commutation using exact Gaussian integers.

## Disposition

The finite derivative exists as \(\operatorname{ad}_N\), but the derivative-to-return coherence square does not. The next gate is not another parity construction; it is source-derived filtration preservation by the physical Green return.
