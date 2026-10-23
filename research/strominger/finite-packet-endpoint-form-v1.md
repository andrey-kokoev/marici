# The source endpoint Green form evaluated on the finite packet

## Result

The first nontrivial analytical term is now evaluated on the [five-packet encoder](finite-observer-encoder-v1.md): the source's signed endpoint Green pairing. All25 polarized entries are exact, and its native signed readout agrees at both E exits.

**18 checks pass.** This evaluates one specific analytical term—not the full regular/mixed/cutoff residual or a face homotopy.

## Source equation and actual packet values

The [joint-graph source](../voevodsky/the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md) gives, with pairing linear in its first argument,

    E_end(g,h) = beta(h)* sigma_x beta(g),
    beta(g) = (m_g(i/2),m_g(-i/2)),
    sigma_x = [0 1; 1 0].

For our declared packet, `beta(p_j)=(2^j,2^(-j))`. Therefore the coefficient matrix is exactly

    G_ij = 2^(i-j) + 2^(j-i),  i,j=0,...,4,
    E_end(g,h) = a_h* G a_g.

No synthetic residual samples or numerical quadrature have been inserted. The candidate's Mellin normalization and packet calibration remain explicit assumptions of this comparison.

## The sign matters

The nonzero eigenvalues of G are `421/16` and `-261/16`; its signature is `(1 positive,1 negative,3 zero)`.

A concrete packet is

    g = 3 p_0 - 2 p_1,
    beta(g)=(-1,2),
    E_end(g,g)=-4.

Its positive endpoint norm squared is5, not-4. Thus the source endpoint form cannot be identified with the ordinary positive norm of the two native E coordinates.

The kernel has the three independent coefficient vectors

    (2,-5,2,0,0),
    (0,2,-5,2,0),
    (0,0,2,-5,2).

Those directions remain visible in the retained complementary packet data. They are not erased because the endpoint form cannot see them.

## Native witness

Let J be the actual native electron contrast frame. The source endpoint term is represented at an E exit by the8x8 signed readout

    Q_end = J sigma_x J*.

The checker verifies:

- endpoint readers in all14 packet presentations reproduce the analytical endpoint pair;
- at both E exits, these readers equal the existing native contrast reader on **all44 field coordinates**, not just prepared states;
- the explicit signed readout pulls back to all25 entries of G under the candidate encoder.

This does not change native transport or replace its positive prepared-field norm with an indefinite norm. It installs a signed analytical **observable** on the existing carrier.

An ideal balanced two-mode Hadamard followed by the difference of the two output powers realizes sigma_x. That is an exact mode/readout identity, not evidence of a prepared or calibrated apparatus. A negative value of the signed observable is not a negative probability.

The form alone is also insensitive to a simultaneous swap of the two endpoint labels. The ordered endpoint readers must therefore remain part of the witness; matching this scalar form is weaker than matching the complete labelled endpoint pair.

## Scope and next gate

The positive-E-norm identification fails, but the **signed** endpoint comparison succeeds. This is not a positivity theorem, not a refutation of the signed realization, and not an analytical tetrahedral filler.

Next evaluate the remaining regular/mixed and physical cutoff terms with their actual regulator placements and domains. A cutoff remainder cannot be supplied by the endpoint term alone, by a decay-order budget, or by the encoder's injectivity. The candidate may still fail that stronger comparison.

```sh
python research/strominger/checkers/check_finite_packet_endpoint_form.py
```

- [Endpoint matrix, signed native readout and explicit witnesses](results/finite-packet-endpoint-form.json).
- [Verification receipt](results/finite-packet-endpoint-form-verification.json).
