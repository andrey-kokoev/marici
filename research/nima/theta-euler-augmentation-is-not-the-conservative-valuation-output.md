# Euler Augmentation Is Not the Conservative Valuation Output

## Finite valuation carrier

Let $H_N$ have orthonormal basis $e_0,\ldots,e_N$, and let the truncated
valuation shift be

\[
S_Ne_k=e_{k+1}\quad(0\le k<N),
\qquad
S_Ne_N=0.
\]

Its two defect projections are

\[
I-S_NS_N^*=|e_0\rangle\langle e_0|,
\qquad
I-S_N^*S_N=|e_N\rangle\langle e_N|.
\]

The primitive source input is therefore the initial defect vector $e_0$,
while positive-metric conservative completion forces the state output to be
the terminal defect row $e_N^*$, up to a unit phase.

## Conservative transfer

For a unitary discrete-time colligation with state block $S_N$ and source
column $e_0$, the block-unitarity equations force

\[
C^*C=I-S_N^*S_N=|e_N\rangle\langle e_N|.
\]

Hence

\[
C=e^{i\varphi}e_N^*
\]

for some fixed phase.  The direct block is then zero.  Its scalar transfer is

\[
\Theta_N(q)
=qC(I-qS_N)^{-1}e_0
=e^{i\varphi}q^{N+1}.
\]

This is the characteristic function of the truncated shift.  It records
transport from the primitive defect to the cutoff-terminal defect.

## Euler transfer

Euler reconstruction uses the augmentation row

\[
\ell_N=\sum_{k=0}^Ne_k^*.
\]

Its transfer is

\[
g_N(q)=\ell_N(I-qS_N)^{-1}e_0
=1+q+\cdots+q^N.
\]

For $N\ge1$, the augmentation row is not proportional to the forced
terminal-defect output:

\[
\ell_N\ne e^{i\varphi}e_N^*.
\]

Therefore no positive-metric conservative colligation with the same state
shift and primitive input has $g_N$ as its transfer function.

## Representation-independent passive no-go

The obstruction is not limited to the truncated-shift realization.  The
scalar transfer $G(q)$ of any positive-metric passive conservative
colligation is a Schur function:

\[
|G(q)|\le1
\]

throughout the unit disk.  Raw Euler augmentation satisfies

\[
g_N(0)=1
\]

and is nonconstant for every $N\ge1$.  By the strong maximum principle, it
cannot be a Schur function.  Hence no state-space enlargement with a scalar
unit input and output can realize the unnormalized $g_N$ as a positive
conservative transfer.

Scaling by $1/(N+1)$ makes the elementary boundary bound possible, but the
normalization then depends on valuation depth and tends to zero with the
cutoff.  It does not preserve the Euler section or define a
completion-stable unit.

This rate is forced.  On the unit disk,

\[
\sup_{|q|<1}|g_N(q)|=N+1.
\]

Hence any scalar normalization $a_Ng_N$ that is Schur must satisfy

\[
|a_N|\le\frac1{N+1}.
\]

For every compact subset of the open disk,

\[
\frac{g_N(q)}{N+1}\longrightarrow0.
\]

The normalized passive transfers therefore converge to the identically zero
function, while the inverse comparison units satisfy

\[
|a_N|^{-1}\ge N+1.
\]

Finite normalization preserves each cutoff zero set, but it destroys the
completed section and has no equicontinuous inverse.  This is an exact
completion-at-infinity witness rather than a failure to choose the optimal
scalar.

Thus positive conservative realization can apply to a transformed or
normalized characteristic function, but not directly to the source Euler
augmentation whose determinant grades are being compared with theta.

## Smallest witness

At depth one,

\[
S_1=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

The conservative output is $e_1^*$, giving transfer $q^2$ after the
standard one-step boundary factor.  Euler augmentation is

\[
\ell_1=(1,1),
\]

giving $1+q$.  The mismatch exists before reciprocal sewing, determinant
regularization, or completion.

## Port interpretation

The bordered valuation system has two genuinely different outputs:

1. the terminal defect required by conservative state evolution;
2. the augmentation measurement required by Euler summation.

Identifying them erases the distinction between cutoff flux and orbit
readout.  Adjoining augmentation as an external observation is legitimate,
but then conservativity of the state colligation does not orient zeros of the
augmentation transfer.

This is the multiplicative counterpart of the theta input-state-response
typing correction.  A source input, a conservative defect response, and a
scalar augmentation are three ports, not one boundary coordinate.

## The two-output system has an exact local confinement law

Keeping the terminal and augmentation outputs separate does retain useful
information.  The geometric recurrence gives

\[
(1-q)g_N(q)=1-q^{N+1}.
\]

At a scalar augmentation zero, $q\ne1$ and therefore

\[
q^{N+1}=1.
\]

Every finite augmentation zero consequently satisfies

\[
|q|=1.
\]

In state-space terms, the zero state

\[
x_N(q)=(I-qS_N)^{-1}e_0
\]

obeys

\[
\ell_Nx_N(q)=0,
\qquad
e_N^*x_N(q)=q^N\ne0.
\]

The augmentation cancellation does not annihilate the transported state or
its conservative response.  Instead, the primitive and terminal boundary
ports become equal after the additional factor $q$.  Their exact boundary
matching forces unit modulus.

This is a genuine local explanation.  Equal valuation-step incidence creates
the recurrence, and the terminal defect supplies the boundary witness.  A
weighted or type-erased orbit generally changes the right side and loses the
conclusion.

The global analogue would require a completed boundary identity in which:

1. the completed theta augmentation vanishes;
2. a source-derived terminal or infinity port remains observable;
3. reciprocal sewing equates its norm with the primitive boundary norm;
4. that equality forces the common spectral character to be unitary.

No such global identity has yet been derived.  The finite result shows what
it must look like without identifying augmentation with the conservative
output.

## Consequence for the comparison cone

The unique-factorization bulk comparison and the moving-seam endpoint cells
close at one and two prime additions.  The first operator-level extension
fails if it attempts to use the Euler augmentation as the adjoint return port.
The corresponding boundary residual is the row

\[
R_{\mathrm{aug},N}=\ell_N-e^{i\varphi}e_N^*.
\]

It is nonzero for every $N\ge1$.  Its norm grows as

\[
\lVert R_{\mathrm{aug},N}\rVert^2=N
\]

after choosing the phase that matches the terminal coefficient.  Thus the
residual does not disappear under valuation-depth completion.

## Surviving architectures

There are only three typed continuations:

1. retain terminal defect and augmentation as separate output ports;
2. enlarge the state and alter the port normalization through a
   source-derived reservoir, while proving that the change is a
   completion-stable nonzero determinant unit;
3. use an indefinite or rigged colligation and prove its metric and domains
   independently.

The first is already source-authorized and minimal.  It produces a
multi-output comparison cone, but supplies no automatic zero confinement.
The second and third require new constructors.  The passive no-go rules out a
raw positive scalar realization even after arbitrary state enlargement.  A
scalar return block derived
after observing $g_N$ is inadmissible.

## Result

The missing Schur return block cannot be the canonical positive conservative
completion of the bordered valuation shift.  Euler augmentation is an
external orbit readout, not the shift's defect output.  Any common
Euler-Evans colligation must retain both ports and explain their relation
without identifying them.
