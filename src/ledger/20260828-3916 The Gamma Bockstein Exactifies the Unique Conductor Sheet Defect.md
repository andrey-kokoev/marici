# 3916 — The Gamma Bockstein Exactifies the Unique Conductor Sheet Defect

## Typed specialization complex

Let \(N\) be the 28-dimensional degree-six numerator packet and \(R\subset N\) its two-dimensional exact-relation space. The absolute source complex is

\[
C=[R\longrightarrow N].
\]

Its differential is the literal relation inclusion.

Let \(S_4\) be the four source-weighted sheet outputs from the two independently labelled conductor systems. Naive evaluation

\[
J:N\longrightarrow S_4
\]

does not define a map from the absolute quotient because

\[
\operatorname{rank}(J|_R)=1.
\]

Entry 3902 supplies the source gamma-Bockstein

\[
\beta:R\longrightarrow B,
\]

where \(B\) is one-dimensional and \(\ker\beta=\ker(J|_R)\). Therefore there is a unique source-normalized boundary

\[
\lambda:B\longrightarrow S_4
\]

such that

\[
\lambda\beta=J|_R.
\]

The corrected target is the two-term complex

\[
D=[B\xrightarrow{\lambda}S_4].
\]

## Exact finite-field result

At primes \(32009\) and \(31957\):

\[
\operatorname{rank}(R\to N)=2,
\qquad
H^{-1}(C)=0,
\qquad
\dim H^0(C)=26.
\]

For the target:

\[
\operatorname{rank}\lambda=1,
\qquad
H^{-1}(D)=0,
\qquad
\dim H^0(D)=3.
\]

The complete chain residual vanishes on both relation generators:

\[
\lambda\beta-J|_R=0.
\]

The raw four-sheet map has rank four. Modding out by the single exact boundary leaves a rank-three descended readout, and the induced map onto \(H^0(D)\) has rank three.

Thus precisely one sheet direction becomes exact—the same direction that obstructed naive descent. No negative-degree class or additional cokernel appears.

## Full mapping cone

For the chain map \(f:C\to D\), the cochain mapping cone is

\[
R[-2]
\longrightarrow
B\oplus N[-1]
\longrightarrow
S_4[0],
\]

with differentials

\[
d_{-2}(r)=(\beta(r),-r),
\qquad
d_{-1}(b,n)=\lambda(b)+J(n).
\]

The complete matrices were exported. At both primes their ranks are

\[
\operatorname{rank}d_{-2}=2,
\qquad
\operatorname{rank}d_{-1}=4,
\]

and the square-zero residual vanishes on both source generators. The graded cone homology is

\[
\dim H^{-2}=0,
\qquad
\dim H^{-1}=23,
\qquad
\dim H^0=0.
\]

The rank-23 middle group is exactly the kernel of the descended rank-three readout from the rank-26 absolute quotient; it is not an additional conductor obstruction.

The sheet-defect vector \(\lambda\) has the explicit middle-degree primitive

\[
(1_B,0_N),
\]

whose boundary is exactly \(\lambda\). Its cyclic edge units are \((1,1,1)\), so the primitive returns identically around the occurrence atlas.

## Hostile basis test

The relation basis was changed by

\[
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix}.
\]

Using the same fixed Bockstein generator and the transported beta coordinates, the chain residual remains zero on both transformed relations. The construction therefore does not depend on selecting the convenient root-visible relation as a permanent basis vector.

## Narrow theorem

The source gamma-normal cell is not merely rank-compatible with the conductor defect. It supplies the differential of a genuine specialization target complex and exactifies exactly the failed sheet-evaluation direction:

\[
H^0(D)=S_4/\operatorname{im}\lambda,
\qquad
\dim H^0(D)=3.
\]

This closes the algebraic conductor-descent problem for the frozen degree-six packet at the checked generic finite-field points.

It does not prove that a physical integration cycle pairs nontrivially with all three descended classes, nor does it extend the result through soft or discriminant support.

## Next falsifier

Transport the rank-three descended target under the Gauss–Manin connection and test whether \(\operatorname{im}\lambda\) is horizontal. If the exact boundary is not connection-stable, the fiberwise cone does not define a coefficient local system. If it is stable, compute the induced rank-three connection and its intrinsic support.

## Artifacts

- `research/benincasa/checkers/check_rank26_conductor_specialization_cone_homology.py`
- `research/benincasa/results/rank26-conductor-specialization-cone-homology.json`
- `research/benincasa/results/rank26-conductor-specialization-cone-homology-p31957.json`

Ledger sequence claim: `seqclaim-7922d158a751dfee259a5fc9`.
