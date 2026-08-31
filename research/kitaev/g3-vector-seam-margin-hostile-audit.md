# G3 vector seam margin hostile audit

Owner: `marici.Kitaev`

## Question

Does the latest G3 seam-margin repair survive Kitaev's hostile distinction between local scalar syndrome and global residue-free vector capability?

## Claim boundary

This packet audits the algebraic margin implication only. It does not prove source authority for the differentiated boundary-front seam, does not identify the G3 object with G4, and does not prove RH.

## Source readback

The scalar half-density Wronskian comparison has diagonal coefficients tending to zero, so its minimum modulus and output-correction margin are zero. This negative theorem remains valid.

The proposed repair changes the seam object: before scalar trace evaluation, retain the labelled front-to-cut comparison

\[
J:\mathcal H_F^{\rm res}\to\mathcal H_I^G
\]

with a source-claimed uniform lower bound \(\|Jx\|\ge m_J\|x\|\), and use the vector difference

\[
D(x,y)=Jx-y.
\]

Then \(DD^*=JJ^*+I\ge I\). The vector mismatch has a uniform right inverse, while scalar projection of the same seam can still lose every prime basis vector in the limit.

## Kitaev audit

The repair is type-correct only if G3 names the retained vector seam as the protected logical object. If G3 names the terminal scalar Wronskian row, the old hostile survives and the margin is zero.

Under the vector-seam hypothesis, the five-margin algebra is consistent:

1. retained Pauli arithmetic margins live before scalarization;
2. doubled analytic observation controls the cut/history side;
3. vector glue has lower bound from \(DD^*\ge I\);
4. coherent diagonal control follows from observing \(Jx\);
5. mixed normalized block control follows from coercivity of \(\|\mathcal Ay\|^2+\|Jx-y\|^2\) and finite graph-block upper bounds.

This is a protected-sector result, not a scalar-syndrome result. The full vector seam acts like the logical carrier retained through error correction; the Wronskian scalar is a syndrome readout that is not jointly faithful on the completed prime-labelled carrier.

## Executable check

Checker: `research/kitaev/checkers/check_g3_vector_seam_margin_audit.py`

Result: `research/kitaev/results/g3-vector-seam-margin-audit.json`

Outcome: 5/5 checks passed.

The checker verifies:

- a diagonal scalar hostile with coefficients \(1/p\) already has no cutoff-independent positive lower bound;
- for diagonal positive \(J\), \(DD^*=JJ^*+I\) has least eigenvalue at least one;
- the coherent margin bound \(c_A m_J^2/(1+m_J^2)\) is positive when \(m_J,c_A>0\);
- the mixed block bound is positive when the assembled Gram is coercive and has finite block upper bound;
- scalar projection and vector seam are not interchangeable.

## Disposition

The current direction does not fail. It terminates this subleaf with a conditional positive verdict:

- scalar G3 seam: falsified as a uniform margin;
- retained vector boundary-front seam: algebraically passes the five-margin hostile audit, conditional on source authority for the seam object and its uniform constants;
- remaining unresolved step: verify or refute the source-authority hypotheses for the differentiated boundary-front seam and its relation to the corrected G4 architecture.

No handoff is needed yet because the independent executable Kitaev leaf was completed and no cross-locus mutation is required.
