# 587 — The Literal Top Packet Is Regular on Generic Quartic-Zero Fibers

## Hard-to-vary claim

If \(\mathcal Q=0\) is object-level support or a pole divisor of the literal proper-top Gauss--Manin packet, then generic nonsoft specialization to \(\mathcal Q=0\) must change a deletion rank, destroy localization/connection descent, or make the canonical proper-top connection singular.

## Frozen specialization

Work over \(\mathbb F_{32003}\) with

\[
\gamma=5,qquad
\text{ambient degree }9,qquad
\text{pole depths }(2,2).
\]

Search the source quartic

\[
\mathcal Q=4AB-(A+B-E^2)^2
\]

for points satisfying

\[
\mathcal Q=0,qquad ABE\neq0.
\]

Three independently found fibers are

\[
\begin{array}{c|c|c|c}
(x,y,z)&A&B&E\\
\hline
(2,4,8364)&2066&2098&8370\\
(2,5,12859)&5629&5669&12866\\
(2,8,6068)&14865&14929&6078
\end{array}
\]

in \(\mathbb F_{32003}\).

## Result

At all three fibers, the complete deletion-rank vector remains

\[
\boxed{(7,8,8,9,16,18,18,21)}.
\]

The face span and proper quotient remain

\[
\dim B=20,qquad
\dim(H_{111}/B)=1.
\]

Both kinematic derivatives descend to finite scalar connections on the literal generator:

\[
\begin{array}{c|c}
(x,y,z)&(A_x,A_y)\\
\hline
(2,4,8364)&(31322,31384)\\
(2,5,12859)&(24477,10292)\\
(2,8,6068)&(6296,7394)
\end{array}
\]

The boundary components remain nonzero. The localization maps and connection naturality tests also remain valid at the first fully audited quartic-zero point.

## Narrow conclusion

\[
\boxed{
\mathcal Q=0
\text{ is neither object-level support nor a pole divisor of the literal proper-top packet}
}
\]

on the tested generic nonsoft fibers.

Together with Entries 526, 528, 584, and 585, this excludes:

- Fitting support of the conic candidate;
- a canonical scalar connection on that candidate;
- diagonal half-logarithmic transport of the physical proper-top line;
- rank degeneration or literal-frame connection singularity of the top packet.

The surviving hypothesis is narrower:

\[
\mathcal Q
\text{ belongs to supported relative-chain/Gysin data or to an extension visible only after imposing the physical chain.}
\]

No new carrier divisor is indicated.

## Scope

Finite-field regularity at three points is a hostile finite falsifier, not a proof of scheme-theoretic extension across the entire quartic divisor. Integral normalization and physical-chain compatibility remain open.

## Next falsifier

Construct the physical relative integration-chain boundary map into the flat rank-twenty-one packet and test whether its supported cokernel, regulator, or Gysin extension acquires \(\mathcal Q\)-support while the ambient packet remains regular.

## Artifacts

- `research/benincasa/marici-gm/src/bin/generic_q_zero_point.rs`
- `research/benincasa/marici-gm/src/bin/generic_q_pole_twisted_derham_rank.rs`
- `research/benincasa/q-zero-literal-top-regularity-audit.json`
