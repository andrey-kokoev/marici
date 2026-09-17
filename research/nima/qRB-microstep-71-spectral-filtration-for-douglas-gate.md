# qRB microstep 71: spectral filtration for the Douglas gate

Prior research provides a packet-natural filtration for the bounded phase-energy operator `A`.

Choose finite-rank projections `P_n` inside spectral cells of mesh `delta_n` tending to zero. Then

$$
\|[A,P_n]\|\le2\delta_n,
\qquad
\|[|A|,P_n]\|\le2\delta_n.
$$

For the compressed operator `A_n=P_nAP_n`,

$$
\bigl\||A_n|-P_n|A|P_n\bigr\|\le2\delta_n.
$$

Thus packetwise Jordan parts converge to the global target `|A|` along this filtration. This removes the arbitrary-compression defect from the Douglas test.

It does not prove the required dominations of the positive and negative parts by the Tate and reference Grams. It supplies the correct packet sequence on which those inequalities should be tested.

Status: packet-natural filtration available; global Douglas domination remains open.
