# Response amplitudes remain supplied preparation data

## Source audit

The shared-leg matrix checker explicitly sets d=2I, x_i=I+(i/3)H and
y_j=I+(j/5)K. These are declared rational evaluation fixtures. Their coefficients
are not calculated from the comparison witnesses or the137-slot count.

The actual retained comparison series in `RetainedComparisonSeries.agda` starts
with a supplied field v and iterates its pullback by a supplied equivalence f:

    coefficient f zero v = v,
    coefficient f (suc n) v = pull f (coefficient f n v).

This defines transport of amplitude data, not preparation of v. Zero input stays
zero; rescaling the input rescales the transported coefficients.

The existing [native scalar amplitude benchmark](native-scalar-fiber-amplitude.md)
does provide a concrete weighted amplitude operation, but explicitly takes its
coupling, propagators and kinematics from a specified field theory. It is not a
source derivation of the137-slot matrix coefficients. Importing those weights
would be a separate physical model choice.

## A finite control with the actual topology

Keep the same shared legs, reference2I, all137 slots and the109 formal mixed
relations. In the arrow block use

    x_i = I+alpha*(i-5)H,
    y_j = I+beta*(j-5)K,

and keep the state composites at I. All primitive legs and composites have
determinant one. For every alpha,beta, centering makes the total comparison mean
I and the fixed-reference residual mean -I. Meanwhile a named rectangle reads

    alpha*beta*i*j*K*H.

The choices alpha=1/3 and alpha=-1/3, with beta=1/5, have identical mean response
and identical total squared Frobenius residual cost22978/45, but opposite nonzero
mixed responses. The Frobenius cost is a declared test observable, not an
identified physical energy. Doubling alpha also changes the mixed-response scale
while preserving the reference and mean.

These are not merely passive frame versions of the same named slot. The
normalized base-slot traces tr(d^-1 C) are11/6 and1/6 in the sign-reflected
fixtures. Such traces are invariant under a simultaneous passive transport of
reference and response. The formal typed witnesses remain the same expressions;
their evaluated response data change as expected.

## Conclusion

The current source supplies comparison witnesses, ordered composition, retained
families and transport of a supplied field. Those do not yet determine amplitude
preparation. Even the first mean plus one scalar cost does not select the sign
of a mixed response in this checked nondegenerate family.

A faithful packet adapter does not close this gap: it preserves the separate
amplitude and equivalence inputs without deriving their relationship. No new
normalization, groupoid representation or averaging identity should be promoted
to an amplitude-generation law on this evidence.

The next substantive input must be an explicit preparation/evolution operation
and its action with the retained witnesses. Until then, keep the matrix values
labelled as test fixtures rather than physical predictions. This bounded
obstruction does not exclude another source constructor elsewhere or a future
physical restriction that selects a smaller amplitude sector.

## Verification

    python research/nima/checkers/check_response_amplitude_source_gate.py
    python research/aspect/scc/scc.py check nima-response-amplitude-source-gate

Exact source-definition checks, supplied-field transport, determinant-one legs,
all rectangle identities, fixed means/reference, same-cost sign reflection,
normalized trace separation and mixed-response rescaling. Result:
`research/nima/results/response-amplitude-source-gate.json`.
