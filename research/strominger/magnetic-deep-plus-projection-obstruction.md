# Deep plus projection is not finite-window in the raw Hall coordinates

The consecutive-depth preferred carrier has a stable algebraic basis:

[
{(a,-):age 0}cup{(a,+):ain P_{g,q}},
]

with a finite plus cap (P_{g,q}). Stability of this basis does not imply
continuity of the quotient map from the original two-branch presentation.

Exact rational elimination was extended through depth (42). For each omitted
plus column, the table records the number of nonzero preferred-basis
coordinates, their maximum absolute coefficient, and their (ell^1) sum.

| ((g,q,a)) | support | max coefficient | (ell^1) sum |
|---|---:|---:|---:|
| ((6,3,18)) | 24 | (1187019/17680) | (8246273/48620) |
| ((6,3,30)) | 36 | (12265863/17290) | (1289628031/752115) |
| ((6,3,42)) | 48 | (1173961791/335920) | (214827035499/25479532) |
| ((6,8,18)) | 20 | (2771703/272) | (197647573/7480) |
| ((6,8,30)) | 32 | (18578703/6118) | (661950617/99484) |
| ((6,8,42)) | 44 | (77311377/5168) | (10569851/323) |
| ((6,13,18)) | 15 | (112176) | (90986689/374) |
| ((6,13,30)) | 27 | (6727589/18676) | (47975890977461/25878772920) |
| ((6,13,42)) | 39 | (27995451/15776) | (865649747631469/98923068816) |

In each audited family the support count grows exactly by one when the omitted
depth grows by one after the cap. Thus a discarded deep plus column does not
reduce inside a fixed reflection window. The maximum coefficient is not
monotone, but both the displayed maxima and the (ell^1) sums become large.

This falsifies the strongest naive completion claim:

> A cutoff-stable Hall carrier automatically gives a cutoff-uniform quotient
> projection in the raw coefficient norm.

What survives is more precise. The carrier inclusions are eventually literal
and neighboring finite-cap chart exchanges stabilize, but the projection from
the original two-branch packet is a growing-support triangular operator. Its
continuity can only be asserted after a source-derived graph norm or weight is
specified and shown to dominate that operator.

This is the magnetic analogue of the adjoint-topology warning from the theta
sector. Formal doubling or algebraic basis reduction can preserve rank while
changing the incidence event being represented. The completion theorem must
therefore retain three separately typed objects:

1. the source presentation and its relation submodule;
2. the stable Hall carrier;
3. a source-authorized topology in which the quotient projection and allowed
   chart transitions are bounded.

The next proof target is to derive the deep-plus relation recursively from the
unipotent source transfer and compute its weighted operator character. Raw
finite-support coordinates already rule out an unweighted finite-window
descent.
