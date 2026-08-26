# Flavor Bipartite Orientation Is a Sign Local System

## Correction

The typed two-family repair retains reversal-odd information, but it does not
by itself choose an absolute orientation. Its sign is defined relative to an
ordered \(A/B\) family frame.

Let

\[
P=
\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{pmatrix}
\]

encode one cyclic direction. The reciprocal bipartite kernel is

\[
H_+=
\begin{pmatrix}
0&P\\
P^T&0
\end{pmatrix}.
\]

The opposite cyclic direction is

\[
H_-=
\begin{pmatrix}
0&P^T\\
P&0
\end{pmatrix}.
\]

Both full kernels are symmetric. Thus reciprocity is preserved.

## Family-swap conjugacy

Define the family exchange

\[
S=
\begin{pmatrix}
0&I\\
I&0
\end{pmatrix}.
\]

Then

\[
S^2=I,
\qquad
SH_+S=H_-.
\]

Therefore clockwise and counterclockwise presentations are conjugate when the
two family labels are not ordered by the source. Any scalar invariant under
family exchange assigns them the same value.

The reversal-odd cross-channel is

\[
D=P-P^T.
\]

Family exchange sends \(D\) to \(-D\). Its sign is meaningful only after an
ordered family frame has been fixed.

## Torsor interpretation

The two frame choices form a \(C_2\) torsor. There is a relative distinction
between them, but no preferred origin internal to the unordered reciprocal
block.

This is the Flavor counterpart of Benincasa's complex-lens result. Circular
analysis can reveal the missing direction while simultaneous conjugation of
state and analyzer leaves static probabilities covariant. In both cases, the
observable requires a calibrated orientation frame rather than an assumed
absolute sign.

## Transition law

If different experimental or theoretical charts use different \(A/B\) frame
choices, every transition carries a parity

\[
\epsilon_{ij}\in C_2.
\]

The holonomy around a loop is the sum of transition parities modulo two:

\[
h=\sum_{(i,j)}\epsilon_{ij}\pmod 2.
\]

Trivial holonomy returns the ordered orientation unchanged. Nontrivial
holonomy returns it with reversed sign. A source construction must either prove
trivial holonomy on admitted comparison loops or retain the sign local system
explicitly in its records.

## Relation to the six-channel adjoint

Grothendieck's correction has the same categorical shape. Passing from a
carrier to its full dual creates a canonical evaluation pairing, but does not
identify the carrier with its dual or select a presentation-dependent metric.
Likewise, the reciprocal \(A/B\) pair creates a place for the odd channel but
does not canonically order the two families.

## Finite falsifier

Any claim that the unordered reciprocal block fixes absolute Flavor
orientation is disproved by

\[
SH_+S=H_-.
\]

The two candidate signs are related by an admitted family relabelling. An
absolute sign becomes available only if a separately derived family-frame
constructor excludes or records that relabelling.

The checker also supplies two transition loops: one with even swap parity and
trivial holonomy, and one with odd parity and sign-flipping holonomy.

## Revised microscopic target

The smallest admissible mediator must now construct all of the following:

1. two inequivalent cyclic families;
2. their reciprocal directed cross-block;
3. an ordered family frame or explicit sign local system;
4. the frame-transition law and loop holonomy;
5. the temporal phase process identified previously;
6. the calibrated projection to physical16.

The typed bipartite Gaussian survivor remains viable, but only as a relative
orientation carrier. It is not yet an absolute Flavor selector.
