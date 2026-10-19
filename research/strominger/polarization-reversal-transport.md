# Polarization transport under paired reversal

## Result

The existing two-mode plane admits a norm-preserving reversal that exchanges its circular modes:

    x_plus -> -i x_minus,
    x_minus -> i x_plus.

Two reversals give identity. Moving the cut preserves polarization unchanged; changing first-two/last-two composition applies this reversal when the histories and source owners are matched.

Twenty output maps and an arbitrary complex polarization superposition are checked exactly: **163 checks pass**.

## Resolve the earlier transpose defect

Let U be the six-by-two real mode embedding, G=diag(3,1) its existing invariant metric, and K the endpoint continuation. Its C3 spectral projector is

    P=(K^2+2K^3-K^5)/2.

The counting pairing fixes the dual embedding

    V=P^T U (U^T U)^-1,
    V^T U=I.

Using the retained plane metric gives its Riesz embedding W=V G:

    W^T U=G,
    K^T W=W T^-1.

Thus reversing incidence naturally requires the left/right identification W, not the raw occurrence permutation of U. After applying the history correspondence J, the target mode coordinates satisfy

    J W=U M,
    M=[[0,-1],[-3,0]].

The raw metric pullback is M^T G M=3G. The positive normalization fixed by the same metric gives

    R=M/sqrt(3),
    R^dagger G R=G,
    R^2=I.

This normalization is part of the constructed polarization identification. The raw occurrence permutation alone remains non-isometric on the original right-mode plane; it is not silently declared repaired.

## Jones and Stokes form

In the orthonormal coordinates q=sqrt(3)a, p=b,

    (q,p) -> (-p,-q),
    Jones matrix = [[0,-1],[-1,0]].

Circular vectors (1,+i) and (1,-i) exchange with phases -i and +i. Every complex superposition retains its norm.

With

    S0=|q|^2+|p|^2,
    S1=|q|^2-|p|^2,
    S2=2 Re(conj(q)p),
    S3=2 Im(conj(q)p),

reversal gives

    (S0,S1,S2,S3) -> (S0,-S1,S2,-S3).

So intensity is preserved and handedness reverses. This is an exact polarization law on the constructed seed plane. It does not reinterpret the earlier defect as lost intensity or substitute fresh target eigenvectors for transported data.

## Verification

```sh
uv run --with sympy python research/strominger/checkers/check_polarization_reversal_transport.py
```

Result: `research/strominger/results/polarization_reversal_transport.json`.
The result retains each of the twenty maps, dual/Riesz embeddings, metric scales, spectral-projector identities and source hashes.
