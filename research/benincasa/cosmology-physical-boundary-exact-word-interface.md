# Exact boundary words now have descriptor-coefficient interfaces

The physical exact boundary solver now serializes every source coefficient with
its source-family kind and row index. Each index was resolved to its typed
source descriptor at the corresponding ambient degree.

| ambient degree | targets | exact source terms |
|---:|---:|---:|
| 12 | 48 | 2,532 |
| 14 | 60 | 3,896 |
| 16 | 72 | 5,626 |

Descriptor-coefficient digests are recorded in the interface receipt. This
repairs the prior projection defect: exact words can now be transported and
compared rather than represented only by ranks and denominator maxima.

Direct/composite rational coherence is not yet tested. The next operation must
apply the already established boundary-coordinate transport, preserving the
distinction between target matching and source-word equality, and compare the
direct A12-to-A16 correction with the A12-to-A14-to-A16 composite.
