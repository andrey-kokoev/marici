# 954 — Only Two Branch Factors Are Pullbacks of the Transition Determinant

## Exact additive-lattice test

Use the common conserved coordinate lattice

\[
(s_{12},s_{13},s_{14},s_{23},s_{24},s_{34},s_{25},s_{35},s_{45})
\]

and impose only the frozen branch normals

\[
s_{14}=0,qquad s_{23}=0,qquad
s_{235}=s_{23}+s_{25}+s_{35}=0.
\]

Two sine divisors are identified only when their additive channel vectors
agree up to sign and this normal sublattice.

## Result

Among the eight branch monomials in Entry 949, exactly two match channels in
the determinant divisor of Entry 905's transition (T):

\[
A_2B_{24}\longleftrightarrow s_{124},
\qquad
A_3B_{34}\longleftrightarrow s_{134}.
\]

The remaining six do not match any transition-divisor channel under the
frozen normal relations:

\[
A_2, A_3, ZA_2, ZA_2B_{24}, A_3/Z, A_3B_{34}/Z.
\]

Therefore

\[
\boxed{
\operatorname{div}\det T
\text{ alone does not pull back to the branch Fitting divisor.}
}
\]

## Interpretation

This is not a coherence obstruction.  The pivot factors (A_2,A_3), for
example, cancel from (det T) by construction even though they remain in the
individual block and dense kernels.  The comparison identity

\[
K_{\rm block}T=K_{\rm dense}
\]

distributes valuations among all three matrices.  Determinant support of the
basis transition cannot recover that matrix-level distribution.

The four (Z)-dependent factors likewise require actual row/column residue
transport, not divisor matching.

## Consequence

The support-level de Rham--Betti test has reached its limit.  Neither equality
nor failure can be inferred from total valuations or transition divisors.
The next object is the labelled matrix residue of the full comparison
identity at the (s_{14},s_{23},s_{235}) flag.

## Next falsifier

Construct

\[
\operatorname{gr}_{s_{235}}
\operatorname{gr}_{s_{23}}
\operatorname{gr}_{s_{14}}
(K_{\rm block}T-K_{\rm dense})
\]

with ordered normal orientation.  Verify the identity entrywise and compare
its six source columns with the branch maximal-minor lattice.  A nonzero
graded defect is the first legitimate coherence obstruction.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_branch_dense_channel_match.rs`;
- packet:
  `research/benincasa/string-six-point-branch-dense-channel-match.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_branch_dense_channel_match`;
- allocator claim:
  `seqclaim-ce8fbad10aef95e7b4e0b018`.
- epistemic event:
  `ev-000000000571-8e93405d-389c-4057-82c6-03142225ba4c`.
