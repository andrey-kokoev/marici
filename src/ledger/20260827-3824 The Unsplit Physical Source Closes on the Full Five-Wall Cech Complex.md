# 3824 — The Unsplit Physical Source Closes on the Full Five-Wall Čech Complex

## Correction to the three-wall packet

Entry 648 established closure on the three shared walls and the vanishing of
the mixed `g23`–`g31` double residue. The rank-26 Boolean profile shows that
the full marked geometry also contains four finite shared–occurrence corners.
Those corners must be retained before claiming closure of the five-wall
object.

## Frozen source form

The source-unsplit residue factor is

```text
(q_g23+q_g31)
---------------------------------------------- da wedge db.
q_g1 q_g2 q_g3 q_g23 q_g31 sqrt(K)
```

Use the wall orientations and ordered corner residues of Entry 3819.

## Exact corner audit

All eight finite wall pairs were evaluated at three generic rational
kinematic points.

- The three shared–shared corners have nonzero ordered residues whose two
  orders cancel.
- The four shared–occurrence corners also have nonzero ordered residues. They
  were absent from the earlier three-wall packet, but their two residue orders
  cancel with the source-fixed orientation.
- At the occurrence–occurrence corner,

  ```text
  q_g23=q_g31=0
  ```

  makes the unsplit numerator vanish. Both ordered double residues are zero.

At every nonzero corner, the remaining marked denominators and `K` are
nonzero, so none of the cancellations is a hidden zero-over-zero identity.
Thus the complete pair-incidence differential vanishes on the source packet.

## Result

The unsplit physical source defines a closed algebraic class on the complete
five-wall Čech complex. The missing four mixed corners do not create an
obstruction; they provide nonzero but mutually compatible incidence data.

This closure does not make the two occurrence periods individually physical.
The primary regulator theorem still leaves their separate boundary values
hierarchy-dependent. The canonical datum is the unsplit five-wall cocycle,
not a five-component physical winding vector.

The next readout gate should therefore pair the source relative chain with
this closed cocycle as one object. It must not first assign independent
physical periods to `g23` and `g31`.

## Artifacts

- `research/benincasa/checkers/check_rank26_full_source_five_wall_cech_closure.py`
- `research/benincasa/results/rank26-full-source-five-wall-cech-closure.json`

Allocator claim: `seqclaim-3aaf80c76b25294661c3b890`.
