# The Constructor Graph Builds a Common Finite Domain but Adds No Zero Exclusion

## Scope correction

The current boundary operations do not arrive as rows on one pre-existing
state space. At a finite cutoff, however, there is a canonical algebraic way
to build such a space without identifying their targets: take the graph of
all source constructors.

This repairs finite typing. It does not yet provide a completed topology.

## Canonical finite graph domain

Let \(S_X\) be the finite labelled source module. Suppose the independently
constructed maps are

\[
T_X:S_X\to Y_X,
\quad
J_X:S_X\to E_X,
\quad
P_X:S_X\to B_{1,X},
\quad
Q_X:S_X\to B_{2,X},
\quad
A_X:S_X\to B_{\infty,X}.
\]

They represent respectively tail or sum-carrier synthesis, seam retention,
primitive current, square current, and archimedean completion. Keep every
target distinct and form

\[
Z_X
=S_X\oplus Y_X\oplus E_X\oplus B_{1,X}
\oplus B_{2,X}\oplus B_{\infty,X}.
\]

The constructor residual is

\[
C_X(s,y,e,b_1,b_2,b_\infty)
=
\begin{pmatrix}
y-T_Xs\\
e-J_Xs\\
b_1-P_Xs\\
b_2-Q_Xs\\
b_\infty-A_Xs
\end{pmatrix}.
\]

Its kernel is exactly the common graph of the five constructors. This is the
smallest honest finite row module: no distributional, Hilbert, seam, or
endpoint target has been collapsed into another.

## Add the Evans wall

Let \(\ell_X:Y_X\to\mathbb C\) be the endpoint observer and define

\[
M_X=
\begin{pmatrix}
C_X\\
\ell_Xy
\end{pmatrix}.
\]

Let the full carrier readout be

\[
R_X(s,y,e,b_1,b_2,b_\infty)=y.
\]

Then

\[
\ker M_X
\cong
\{s\in S_X:\ell_XT_Xs=0\},
\]

and on this kernel

\[
R_X=T_Xs.
\]

Therefore

\[
\ker M_X\subseteq\ker R_X
\]

holds if and only if

\[
\ker(\ell_XT_X)\subseteq\ker T_X.
\]

The seam, primitive, square, and archimedean graph coordinates have cancelled
from the criterion. Because each is defined as an output of the same source,
their graph equations record information but impose no independent relation
on \(s\).

## Finite dimension obstruction

If \(T_X\) is injective and \(\dim S_X\ge2\), no scalar functional
\(\ell_XT_X\) can be injective. Hence the desired kernel inclusion fails
automatically on the unrestricted finite source module.

This does not prove that the physical source orbit has dimension at least two.
It proves that admitting arbitrary labelled coefficient packets while using
only constructor graph equations cannot yield zero exclusion.

## Smallest witness

Take

\[
S_X=Y_X=\mathbb C^2,
\qquad
T_X=I,
\qquad
\ell_X=(1,1).
\]

For \(s=(1,-1)^T\), set every boundary coordinate equal to its independently
declared constructor value. Then every constructor residual vanishes and

\[
\ell_XT_Xs=0,
\qquad
R_X=T_Xs=s\ne0.
\]

The witness survives arbitrary choices of \(J_X,P_X,Q_X,A_X\). Merely adding
their output coordinates cannot repair it.

## What new structure would help

The common graph domain is still useful: it is the correct carrier on which a
new relation can be stated. But zero-exclusion force requires an independent
coherence equation

\[
K_X(s,y,e,b_1,b_2,b_\infty)=0
\]

that is not one of the constructor definitions and is derived from source
symmetry, conservation, modular sewing, or a boundary law.

Equivalently, the boundary packet must do more than remember outputs. It must
constrain which joint output tuples are dynamically admissible.

Candidate sources of such a relation are:

- the doubled Green storage-and-supply identity;
- a product-formula charge relation;
- a reciprocal boundary condition coupling direct and dual sectors;
- a second endpoint observer with source-derived joint faithfulness.

## Completion gate

At finite cutoff the graph construction is canonical. At infinite cutoff one
must still choose a topology in which all constructor maps are simultaneous
continuous maps and the graph remains closed. But completion analysis is
premature until an independent finite coherence row has been found: completing
only graph equations preserves the same logical equivalence to scalar
endpoint injectivity.

## Scope

This constructs the common finite bordered domain and proves that constructor
graph rows alone add no zero-exclusion force. It does not construct the needed
independent coherence relation, completed graph topology, kernel descent,
zero confinement, or RH.
