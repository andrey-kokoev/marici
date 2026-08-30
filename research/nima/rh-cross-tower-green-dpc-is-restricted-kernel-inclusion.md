# RH cross-tower Green DPC is restricted kernel inclusion

## The exact implication

Let (A_s) be the source-admissible solution space at spectral parameter
(s). Let

\[
L_s:A_s\to\mathbb C
\]

be the completed scalar output, and let

\[
W_s:A_s\to\mathcal Y_s
\]

be the jointly faithful arithmetic Ward packet obtained from the tensor
boundary observer.

The cross-tower implication needed before positivity can act is

\[
\ker L_s\subseteq\ker W_s.
\]

This statement is restricted to the source-admissible dynamical space. It is
not a claim that one scalar reconstructs the full labelled state.

## Factorization theorem

For linear maps on a fixed admissible space, the kernel inclusion holds if
and only if there is a linear map (R_s) on the scalar image such that

\[
W_s=R_sL_s.
\]

Consequently,

\[
\operatorname{rank}W_s
\le
\operatorname{rank}L_s
\le1.
\]

If the Ward packet has rank two or more on (A_s), scalar output nullity
cannot imply Ward nullity by any linear factorization. The source dynamics
must first reduce the relevant solution space, or the output boundary
condition must remain representation-valued rather than scalar.

The rank inequality is necessary but not sufficient. A two-dimensional
fixture can give both maps rank one while their kernels are different. The
actual kernel inclusion must be checked.

## Minimal hostile witness

Take one vacuum coordinate and two Ward-visible coordinates. Let the scalar
observer sum all three coordinates, while the Ward packet reads the last two.
Then

\[
x=(0,1,-1)
\]

has zero scalar output and nonzero Ward output. Positive input energy, complete
Fourier character resolution, and exact arithmetic typing do not remove this
witness. Only a source law excluding it from (A_s), or a Green identity
forcing its Ward output to vanish, can close the implication.

## What the Green cell must establish

The desired control cell must be derived before scalar projection and prove
one of two typed outcomes.

1. Dynamic compression: the off-seam admissible solution space is small
   enough that the scalar boundary condition is injective modulo the Ward
   kernel.
2. Representation-valued boundary nullity: the scalar zero is accompanied by
   source-derived boundary equations that kill all Ward-visible character and
   arithmetic directions.

A diagonal state-energy identity alone proves neither. A scalar continuation
formula alone proves neither. The cell must connect output boundary data,
control transport, and input Ward observability on the same admissible state.

## DPC verdicts

- Closed: 
  \(\ker L_s\subseteq\ker W_s\) is derived on (A_s), naturally in cutoff
  and continuously through completion.
- Rank obstruction: 
  \(\operatorname{rank}W_s>1\) while only scalar boundary data is available.
- Kernel-angle obstruction: ranks permit factorization but an explicit state
  lies in \(\ker L_s\setminus\ker W_s\).
- Authority obstruction: the inclusion holds only after defining (A_s)
  backward from the desired scalar zero.
- Completion obstruction: every finite cutoff satisfies inclusion but a limit
  state violates it.

## Cross-sector clarification

Figueiredo's protected flavor slice displays the same logic. The complete
admitted invariant potential loses angular stiffness when its source coupling
vanishes. Adding a reference port changes the experiment; it does not recover
the missing implication inside the old admissible domain. Here, adding label
readouts by hand would likewise change the observer rather than derive the
cross-tower Green cell.

## Next calculation

Construct the actual finite-cutoff admissible solution map (Z_{s,X}) from
the doubled theta boundary system. Compute

\[
L_{s,X}Z_{s,X}
\quad\text{and}\quad
W_{s,X}Z_{s,X}.
\]

Then test rank and kernel inclusion directly. The smallest vector in

\[
\ker(L_{s,X}Z_{s,X})
\setminus
\ker(W_{s,X}Z_{s,X})
\]

is the decisive finite falsifier.

## Verification

Run:

```powershell
python research/nima/checkers/check_rh_cross_tower_kernel_inclusion.py
```
