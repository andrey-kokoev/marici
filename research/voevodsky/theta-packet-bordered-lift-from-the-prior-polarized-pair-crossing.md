# Theta packet bordered lift from the prior polarized-pair crossing

## Existing constructor located

`the-polarized-pair-kernel-has-a-canonical-linear-crossing-to-the-bordered-radial-response.md` constructs a continuous map on smooth ordered theta pairs with shell labels. It produces correlation, shell-endpoint, Wronskian, and Laplace channels together. Its Hermitian lane conjugates the second slot; the analytic-transpose lane retains two unconjugated slots.

This supplies a domain-correct alternative to treating interval indicators as Sobolev vectors. A shell is retained as an integration label, and its boundary terms are included explicitly. The smooth pair is differentiated before shell integration.

## Fifteen explicit shell lifts

Set phi=Phi_1, A_i=log a_i, B_i=log b_i for the existing fifteen intervals. Define

    h_i(s) = integral_(A_i)^(B_i) phi(v) phi(v+s) dv,
    e_i(s) = [phi(B_i)phi(B_i+s)-phi(A_i)phi(A_i+s)]/2,
    w_i(s) = integral_(A_i)^(B_i)
                [phi'(v)phi(v+s)-phi(v)phi'(v+s)] dv,
    alpha_i = h_i(0).

The source is the finite direct sum, over shell labels i, of the smooth pair phi tensor phi in the earlier pair carrier. Both pair lanes agree on these real elementary pairs; complex coefficient extension and subsequent sesquilinear pairings must retain their declared variance.

The local product rule gives

    integral_(A_i)^(B_i) d_v[phi(v)phi(v+s)] dv = 2e_i(s),
    h_i'(s) = e_i(s) - w_i(s)/2.

Thus w_i=2e_i-2h_i' exactly. All these functions and their derivatives decay superexponentially on s>=0. Define the bordered column

    b_i = (alpha_i,h_i,e_i,w_i),
    B_border e_i^coordinate = b_i.

Here e_i^coordinate is the coordinate basis vector, distinct from the endpoint function e_i(s). The correlation projection p satisfies p B_border=H.

The earlier crossing includes oriented half-density transport when starting from a differently normalized radial pair. Here phi is already the completed atom used by H; no additional label or half-density factor is inserted. Comparison with an independently normalized arithmetic source still requires its normalization map.

## Source-backed multipoint lift

At degrees r=2,4 define

    F_border,r = B_border^(tensor r) K_r,
    F_border = F_border,2 direct-sum F_border,4.

Tensor products may be taken in the finite spans of the bordered columns, or in the earlier projective carriers where the operations are continuous. The finite construction requires no infinite-label completion.

There are exact observation identities

    p^(tensor r) F_border,r = H^(tensor r) K_r,
    (p^(tensor 2) direct-sum p^(tensor 4)) F_border = F.

This is a concrete lift through the prior pair-to-border construction. No new arbitrary source coordinate is needed for this factorization.

For every tensor slot j, its correlation, endpoint, and Wronskian components satisfy the same linear differential identity. Therefore every source packet satisfies all slotwise Stokes relations simultaneously. The relations are compatible because operations on distinct tensor slots commute.

## Laplace channels and mixed relations

Let R_i,E_i,W_i be the Laplace transforms of h_i,e_i,w_i. They are entire in z, by superexponential decay. Integration by parts gives

    z R_i(z)-alpha_i = E_i(z)-W_i(z)/2.

Tensoring yields, for each slot j,

    z_j R_(all slots) - alpha_(slot j) R_(remaining slots)
      = E_(slot j) R_(remaining slots)
        - (1/2) W_(slot j) R_(remaining slots),

understood as linear operators on the same signature tensor. It is valid termwise and hence for every route combination. It does not assert factorization of a general route combination into products of its marginals.

The earlier combined readout R+2E can consequently be applied in each selected slot, with its original fixed coefficients. Applying it defines that prior readout on this packet; identifying it with any independently specified arithmetic return remains a separate equality.

## Shell refinement coherence

For A<C<B, every channel obeys

    b_[A,B] = b_[A,C] + b_[C,B].

For h and w this is integral additivity; for e it is cancellation of the intermediate endpoint, and for alpha it follows at s=0. Laplace transforms and all parameter derivatives preserve these identities.

Thus the bordered lift commutes with event segmentation and further subdivision of the same shells. Repeated subdivisions commute strictly by finite additivity. This establishes an actual source comparison for refinement, without defining it through an inverse of F.

Prime insertion also changes route incidence and translates selected shell pieces. Its identification with the earlier arithmetic successor requires those additional source operations. Shell refinement alone does not establish that identification.

## Parity consequence

With Z=K/2 and K_2 Z=0,

    F_border,2 Z = 0.

The entire two-point bordered response, including every endpoint and Wronskian component obtained by this same columnwise lift, annihilates the six parity channels. Tensor-slot derivatives, Laplace jets, and any linear readout of these bordered two-point data also annihilate them.

Thus adding these specific boundary channels at degree two cannot recover the parity sector. The four-point lift retains that sector: projecting back to the already faithful combined theta observation proves injectivity of F_border on the four-prime packet. This uses the prior finite atom-independence theorem and the invertible selected signature matrix M.

No improvement of output-noise constants is claimed. Such a statement requires a specified norm on the additional measured channels and an actual measurement model for them.

## Status of the full signed form

The preceding Green-domain audit correctly excluded zero-extended step functions from an ordinary H1 graph. The present lift bypasses that specific obstruction by using the earlier smooth pair-plus-shell source and its boundary channels.

A pullback of the complete regular-plus-endpoint Green form still needs a declared form on these tensorized bordered carriers. The archived faithful-joint-graph semantics in `aspect-v4-accepts-the-faithful-joint-graph-and-leaves-only-evans-return-placement-open.md` explicitly allows independently sourced forms to be retained together and treats single-metric descent as optional. That archived status does not itself identify a form on this new packet.

The concrete progress is the bordered source lift, its exact observation projection, slotwise Stokes identities, shell-refinement naturality, and the two-point parity annihilation theorem. These follow from the existing pair crossing and the actual signature map; a chosen tensor Green metric is unnecessary for them.
