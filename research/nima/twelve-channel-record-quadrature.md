# Retained-record return to a twelve-relationship quadrature port

## Result and authority boundary

A conditional, norm-preserving readout adapter now connects the four-component carrier to the twelve directed relationships of a four-state graph. With an explicitly supplied quadrature convention, its coherent sum has exactly the proposed form

    A_outer = 12 + i*eta,
    eta = sqrt(12)*s,

where s is the carrier's scalar coefficient. Under the existing feedback update, s_next=(C L t)_0, so a previously unread scalar record can supply the imaginary contribution. No gain or preparation is fitted to a mass value.

The graph and metrics determine the normalization within the declared common-mode plus gradient port construction. They do NOT determine that this is the physical readout, that common imaginary response is admissible, or which state to prepare. In particular eta remains seed-dependent. This is a concrete candidate adapter, not a source-authorized proton model.

A decisive control is retained: if reciprocal arrow amplitudes must be complex conjugates, the common imaginary component is forbidden and eta=0. The interpretation of these arrow responses therefore matters.

## Inputs kept distinct

- `four-packet-record-feedback.md` supplies the unchanged conservative map on x=(s,q,p,z) and a sixteen-coefficient record t. Write x=(s,v), v=(q,p,z).
- `four-packet-complex-response.md` supplies the cycle's 60/120-degree phase sectors and establishes that phase alone does not change an amplitude magnitude.
- `proton-electron-shared-state-comparison-hypothesis.md` supplies the twelve directed relationships of four states and the nominal 153-slot inner comparison count. It does not supply complex transition amplitudes or a physical mass readout.

The adapter below identifies the scalar coefficient with a common arrow response and the three remaining coefficients with tetrahedral potential contrasts. This identification is new and explicit; the existing Clifford product is not itself an endpoint-packet multiplication theorem.

## Construct the relative port from incidence

Let the four labels be 0,1,2,3 and E={(i,j):i!=j}. Use the tetrahedral contrast frame

    H = (1/2) * [[ 1, 1, 1],
                 [ 1,-1,-1],
                 [-1, 1,-1],
                 [-1,-1, 1]].

Then H^T H=I_3 and H^T 1=0. The four potentials are u=Hv. Define the twelve-by-three difference map

    (Dv)_ij = u_j-u_i.

Directly from complete-graph incidence,

    D^T D=8 I_3,   1^T D=0.

Consequently G=D/sqrt(8) embeds the three contrasts isometrically in the reversal-odd arrow space. Their sum over all twelve arrows vanishes. Relative differences alone cannot give a nonzero aggregate eta; the reversal partners cancel.

## Add the scalar port with its forced normalization

The constant unit vector of the twelve-arrow space is c=1/sqrt(12). It is orthogonal to every column of G. Define

    W(s,v)=c*s+Gv.

W^T W=I_4, so this is an isometry, with no adjustable coefficient once these metrics and ports are chosen. The constant line is invariant under every vertex permutation; the gradient sector transforms with the standard three-dimensional contrast representation. The checker verifies readout covariance under all 24 relabellings. This does not assert full permutation covariance of the earlier chosen cycle R.

There are other possible arrow-space embeddings of the triplet. The gradient choice is specifically selected by endpoint differences and reversal oddness; this is not a uniqueness theorem for all possible physical couplings.

## Declare the quadrature readout

Use a supplied real baseline of one per arrow and put W x in the orthogonal imaginary quadrature:

    a_ij = 1 + i*[s/sqrt(12) + (u_j-u_i)/sqrt(8)].

The choice of an external phase reference that calls this response imaginary is additional readout data. It is not extracted merely by naming the Clifford bivector i, and this real-to-quadrature adapter is not claimed to be a complex-linear intertwiner of the previously constructed K. The prior phase calculation alone does not authorize this adapter.

Summing the twelve channels gives

    sum_E a_ij = 12 + i*sqrt(12)*s.

Here the imaginary contribution comes from the scalar/common port, not from a failure of gradient cancellation. The nominal inner factor gives the conditional coherent response

    A_total = 153*(12+i*sqrt(12)*s),
    |A_total|² = 153²*(144+12*s²).

Choosing its modulus, real part or squared modulus as a physical quantity remains a separate decision. Multiplying coherent amplitude by the old resource count 153 is a test convention, not a derived equivalence of resource, energy and amplitude.

## Budget and back-action

Because the baseline is in the real quadrature and W is isometric,

    sum_E |a_ij|² = 12 + ||x||².

Under the unchanged feedback update,

    x_next = C L t,
    t_next = C^T R x + (I-C^T C)Lt,

we therefore have the exact readout accounting identity

    sum_E |a_ij,next|² + ||t_next||²
      = 12 + ||x||² + ||t||².

This is a coordinate/readout identity, not proof that a measurement can copy out this budget without disturbance. The real baseline itself is supplied, with budget twelve. No unaccounted creation of imaginary amplitude occurs: carrier/record exchange redistributes the existing variable budget.

The squared magnitude of the coherent sum is NOT the sum of squared channel magnitudes:

    |sum_E a_ij|² = 144+12*s²,
    12*sum_E |a_ij|² - |sum_E a_ij|² = 12*||v||².

Thus interpreting the coherent reading as total stored energy would require another physical rule. The overall budget remains conserved even when the coherent outer reading changes.

## Actual return of a previously invisible scalar record

Prepare x=0 and t=L C^T e_0. Then Ct=0: the old multiplication port cannot see the record. One feedback step gives x_next=e_0, t_next=0. Hence eta changes from zero to sqrt(12) while variable budget one transfers from bank to carrier.

By contrast t=L C^T e_1 returns a contrast. It increases the resolved channel budget but produces no aggregate imaginary response because the opposite arrows cancel. This separates common-mode return from generic nonzero record feedback.

For the one-time squared preparation t=R(x) tensor x used in the preceding trial,

    C L t = mu(x tensor x)/2,
    s_next = (s²+q²+p²-z²)/2,
    eta_next = sqrt(3)*(s²+q²+p²-z²).

This is an exact state-dependent formula, not a universal number. Preparing alpha times the hidden scalar record gives eta_next=sqrt(12)*alpha. Changing the input scale of a squared preparation changes its eta quadratically. No selected initial amplitude has been derived.

A balanced fixed preparation x=e_0, t=C^T e_0+L C^T e_0 gives a persistent nonzero eta. All scalar rescalings of this preparation also persist, so it does not select a particle mass.

## Reciprocal-conjugacy control

Swapping endpoints gives

    a_ji = 1+i*[s/sqrt(12)-(u_j-u_i)/sqrt(8)],
    conjugate(a_ij) = 1-i*[s/sqrt(12)+(u_j-u_i)/sqrt(8)].

These are equal exactly when s=0. Therefore if the twelve channels are required to be off-diagonal entries of a Hermitian response matrix, this proposed common imaginary port is inadmissible. A common phase-referenced response of directed comparison records might have a different reversal law, but that law must be specified rather than inferred from the edge count.

## Verification

    python research/nima/checkers/check_twelve_channel_record_quadrature.py

Fresh exact checks pass for the contrast and arrow Gram identities, 256 rational carrier samples, all 24 vertex relabellings, scalar and contrast return controls, conserved carrier/record/channel accounting, coherent versus incoherent readings, reciprocal-conjugacy conditions, seed scaling and five preparations through three retained advances. Fourth advances are refused by the existing retention gate.

Artifact: `results/twelve-channel-record-quadrature.json`. No observed mass, numerical fit, phase adjustment, new damping or new feedback dynamics is used.

## Next decision

Specify what the twelve complex quantities represent and their reversal/measurement law. If conjugate reciprocity is required, this adapter cannot supply eta. If a common imaginary port is admissible, the next unresolved input is the source-selected preparation and physical readout that would determine eta and convert a budget to a mass. The existence of the adapter alone settles neither.
