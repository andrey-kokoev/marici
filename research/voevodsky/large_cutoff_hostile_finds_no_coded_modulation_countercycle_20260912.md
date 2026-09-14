# Large-cutoff hostile finds coded-modulation countercycles

## Question

Does one shell-index-coded or scale-coded modulation remain injective on larger arithmetic cycle spaces?

## Claim boundary

No. The finite discovery through cutoff 480 fails by cutoff 960 when the full consecutive-prime catalogue is included. Exact rational countercycles survive both ordinary incidence and the coded modulated incidence. Therefore neither single code is a complete route-residue measurement.

## Rank hostile

For a diagonal code \(D\), detection on cycle space is equivalent to full column rank of

\[
\begin{pmatrix}
\partial\\
\partial D
\end{pmatrix}.
\]

Sparse elimination over two large prime moduli gives matching ranks:

| cutoff | edges | cycle dimension | shell-code deficiency | scale-code deficiency |
|---:|---:|---:|---:|---:|
| 960 | 279 | 45 | 1 | 1 |
| 1920 | 563 | 95 | 5 | 5 |
| 3840 | 1136 | 203 | 16 | 16 |
| 7680 | 2287 | 426 | 40 | 40 |

Failure over both moduli motivated exact rational extraction at cutoff 960. Exact nullspace calculation confirms one-dimensional kernels for both codes.

## Exact residuals

The shell-coded countercycle has support on twelve edges using the shells

\[
(2,3),\quad(3,5),\quad(5,7)
\]

and scales among \(6,10,14,15,21,25,35\). Its coefficients are integral, including the pattern \(1,-1,-1,-2,1,2,1,2,-2,\ldots\). Direct exact multiplication verifies both

\[
\partial z=0
\qquad\text{and}\qquad
\partial D_{\rm shell}z=0.
\]

The scale-coded countercycle has ten-edge support over the same three shells, with rational coefficients including

\[
1,-10/7,-9/4,3/7,75/28,5/4,1,\ldots.
\]

It likewise satisfies both exact kernel equations. The complete witnesses are recorded in `research/voevodsky/results/coded_modulation_countercycles.json`.

## Correction

Withdraw the suggestion that one fixed shell code or one fixed scale code may detect the completed residue. Their success through cutoff 480 was a finite truncation effect compounded by restricting the shell list in the earlier census. Coarse modulation families may still be jointly faithful, but one scalar-coded intervention is not.

## Experimental consequence

The cheapest four-edge rectangle remains useful as an initial apparatus test, but passing it does not establish complete residue sensitivity. A viable measurement must use multiple independently recorded modulation channels or a richer joint code whose kernel is tested against the growing countercycle family.

## Disposition

The strongest hostile produced explicit counterevidence rather than an unbounded theorem. Next work should determine the minimum number and type of shell/scale channels needed as cutoff grows. This packet does not prove any fixed finite family suffices on the unbounded completion.
