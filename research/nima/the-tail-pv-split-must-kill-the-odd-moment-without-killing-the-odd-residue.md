# The tail/PV split must kill the odd moment without killing the odd residue

## Correction to the zero-trace criterion

The endpoint-kernel theorem for Schur elimination remains valid, but it applies only to coordinates that are genuinely auxiliary. The primitive principal-value channel contains two odd coordinates with different constructor roles:

- an odd moment producing the non-summable algebraic tail;
- an odd residue carrying reciprocal orientation.

Treating both as one auxiliary tail and requiring the full endpoint trace to vanish is too strong. It removes the divergent moment, but it also erases the orientation that the Adams edge must retain.

The minimal typed boundary space is therefore not merely an endpoint pair. It has the decomposition

[
E_{mathrm{ret}}
=
E_{mathrm{wall}}oplus E_{mathrm{res}},
qquad
N_{mathrm{elim}}
=
N_{mathrm{mom}}oplus N_{mathrm{bulk},0}.
]

Here (E_{mathrm{res}}) is the retained odd residue, (N_{mathrm{mom}}) is the removable odd moment, and (N_{mathrm{bulk},0}) is ordinary zero-trace bulk.

## Selective regularization

Let (T_{mathrm{mom}}) and (T_{mathrm{res}}) be the independently typed moment and residue ports. A source-authorized moment lift (L_{mathrm{mom}}) would define

[
R_{mathrm{PV}}
=
I-L_{mathrm{mom}}T_{mathrm{mom}}.
]

The required identities are

[
T_{mathrm{mom}}R_{mathrm{PV}}=0,
qquad
T_{mathrm{res}}R_{mathrm{PV}}=T_{mathrm{res}}.
]

The first cancels the algebraic primitive tail before prime aggregation. The second proves that this cancellation does not identify reciprocal orientations.

Thus the relevant incidence law for the Schur-eliminated space is

[
T_{mathrm{ret}}J_{mathrm{elim}}=0,
qquad
T_{mathrm{ret}}
=
T_{mathrm{wall}}oplus T_{mathrm{res}},
]

not the statement that every PV coordinate has zero trace.

## Jet interpretation

In the frozen three-coordinate jet frame, the roles are

[
(	ext{even wall/overlap}, 	ext{odd moment}, 	ext{odd residue}).
]

The needed coherencer acts as the odd subtraction

[
(0,-1,0)
]

while preserving the residual coordinate

[
(0,0,1).
]

An even counterterm cannot cancel the odd moment. Full reciprocal negation cancels both odd coordinates and therefore destroys the Adams orientation. This isolates the odd moment-jet coherencer as the unique viable source location already identified by the primitive PV audit.

## Consequence for the Schur theorem

Once the selective coherencer exists, the earlier endpoint lower-bound theorem applies unchanged to the enlarged retained trace:

[
A-CD^{dagger}C^{*}
ge
T_{mathrm{ret}}^{*}T_{mathrm{ret}}.
]

The eliminated moment and zero-trace bulk cannot consume retained wall or residue energy because their incidence into (E_{mathrm{ret}}) is zero after the authorized subtraction.

Without that coherencer, however, the first Adams edge is still undefined. One cannot infer the required kernel law from scalar PV cancellation, and one cannot declare the full tail auxiliary without losing the reciprocal odd port.

## Completion gates

The source theorem must prove:

1. (L_{mathrm{mom}}) is constructed before prime aggregation;
2. (T_{mathrm{mom}}L_{mathrm{mom}}=I) on the removable moment line;
3. (T_{mathrm{res}}L_{mathrm{mom}}=0);
4. the regularized remainder has exponential, or otherwise summable, prime decay;
5. the retained residue observer has a cutoff-uniform lower frame bound;
6. all identities survive rigged closure and reciprocal reflection.

The decisive hostile has exact cancellation of the primitive (L^{-1}) moment but also sends the odd residue to zero. It produces a convergent unoriented scalar packet, not a typed Adams edge.

## Status

Event 10159 did not close the tail/PV incidence gate. It reduced the positivity part to a kernel theorem. The source audit now sharpens that kernel theorem: eliminate only the odd moment and genuine zero-trace bulk; retain the odd residue as boundary data. The earliest missing constructor is the source-derived odd moment-jet coherencer with residue preservation.
