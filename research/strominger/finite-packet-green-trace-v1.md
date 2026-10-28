# A mixed value–flux trace calculation on the finite packet

## Result

The source Volterra/value–flux law is now evaluated for two explicitly chosen weighted inputs from the [compact observer packet](finite-observer-encoder-v1.md). Five seam matrices give125 exact polarized entries and70 native presentation/seam pullback checks. **17 checks pass.**

Two nonzero packets invisible to **both** Mellin endpoints have a nonzero calibrated seam pairing. Thus endpoint agreement alone loses actual trace information; the retained complement is necessary.

This is a source trace subproblem. It is not yet the full physical mixed polarization, Connes cutoff remainder, or an analytical face filler.

## Source law and declared lift

The [joint-graph source](../voevodsky/the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md) provides

    H(q)(u) = integral_{-infinity}^u q,
    Gamma_a H(q) = (0, integral q, integral_{-infinity}^a q, q(a)),
    omega((M,J),(Mtilde,Jtilde)) = J Mtilde - M Jtilde.

Its displayed orientation is **complex bilinear**. It must not silently be treated as the Hermitian endpoint form evaluated in the preceding step.

For our declared lift, apply this law separately to

    q_sigma(h)(u) = exp(sigma*u/2) h(u), sigma=+1,-1,

and take their direct-sum seam pairing. Both inputs are smooth and compact. Their right-end integrals are exactly the packet's two Mellin endpoints. Identification of this chosen lift with the entire intended semilocal mixed polarization remains an additional gate.

## Exact calculation without inventing partial integrals

At seam `a=k delta`, only packet p_k has nonzero flux. For each sign,

    A J_sigma(p_j) = 2^(sigma*k) delta_jk,
    M_sigma(p_j) = 2^(sigma*j) if j<k,
                  0 if j>k,
                  2^(sigma*k) theta_sigma if j=k.

The weighted half-packet integrals theta_plus and theta_minus are not set to1/2 or approximated. Their coefficients cancel identically in the alternating pairing.

Define W_k by

    A Omega_k(g,h) = a_h^T W_k a_g.

For j<k its only nonzero entries are

    (W_k)_(j,k) = 2^(j+k) + 2^(-(j+k)),
    (W_k)_(k,j) = -(W_k)_(j,k).

All other entries vanish. These formulas use the same positive, source-defined normalization A as the encoder. Seams k=0,...,4 are settings on a fixed packet—not five evolution stages.

## A comparison that endpoints cannot see

Take coefficient vectors

    u = (2,-5,2,0,0),
    v = (0,2,-5,2,0).

Both endpoint pairs are `(0,0)`. Nevertheless,

    A Omega_1(u,v) = -10.

The source Green trace therefore cannot factor through the two endpoint values alone. The zero packet pair has the same endpoint data but zero pairing.

Reversing the value–flux orientation gives+10. Multiplying the second packet by i multiplies this bilinear pairing by i; using an adjoint instead of a transpose would give the opposite phase. Both conventions are tested explicitly.

## Native comparison and a finite observation certificate

The candidate decoder D_a gives the native bilinear readout

    D_a^T W_k D_a / A.

All70 presentation/seam pullbacks reproduce the computed packet matrices. The normalized decoders D_a U_a coincide on the entire44-coordinate root field, giving pairwise native covariance in factored form. This is not a new physical coupling or a measured detector.

There is also an exact finite observation certificate: use probe p_1 at seam delta to recover coefficient0, and probe p_0 at seams delta,2delta,3delta,4delta to recover coefficients1 through4. The resulting diagonal observation matrix is invertible.

That means **two fixed probe packet types, four seam settings and five readings**. It does not mean that two arbitrary graph-node probes select a unique coherence complex or that a hardware implementation has been constructed.

## Next gate

Bind the intended physical cutoff and Fourier-conjugate cutoff, their placements and common domains. Establish whether this weighted Volterra lift is the required mixed polarization. Then evaluate the regular/mixed/cutoff comparison on the finite packet, with controlled errors wherever exact formulas are unavailable.

Do not replace the physical cutoff by a seam selector, add this bilinear form to the Hermitian endpoint term without a declared polarization, or infer a higher filler from exact reconstruction.

```sh
python research/strominger/checkers/check_finite_packet_green_trace.py
```

- [Frozen trace-lift contract](contracts/finite-packet-green-trace.v1.json).
- [Seam matrices, invisible pair and observation inverse](results/finite-packet-green-trace.json).
- [Verification receipt](results/finite-packet-green-trace-verification.json).
