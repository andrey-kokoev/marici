# Augmentation--control normal-frame candidate

## Source-derived waveforms

Grothendieck's finite Fourier seam packet already supplies two canonical
optical waveforms at label cutoff `N`:

- the normalized flat augmentation comb `Omega/sqrt(N)`;
- the zero-frequency control pulse `e_0`.

The unitary finite Fourier transform exchanges them exactly. No waveform is
chosen from observed seam data.

## Exact rank floor

Their normalized Gram matrix is

`[[1, 1/sqrt(N)], [1/sqrt(N), 1]]`.

Its eigenvalues are

`1 plus or minus 1/sqrt(N)`.

For every nontrivial cutoff `N>=2`, the pair has rank two. More strongly, its
smallest Gram eigenvalue has the uniform lower bound

`1 - 1/sqrt(2)`.

This gives the 3+4+3 tomograph its first explicit source-derived normal-rank
floor. The cutoff `N=1` is the exact hostile: augmentation and control
coincide and the frame collapses to rank one.

## Optical realization

One channel is a phase-flat frequency comb over all `N` labels. The other is
the isolated zero-frequency bin. Direct powers and their plus/minus
interference recover the two-by-two Gram matrix. Applying the discrete Fourier
network must swap the two measured waveforms.

The apparatus can therefore test both rank two and the claimed Fourier role
exchange with the same source packet.

## Exact boundary of the result

This establishes finite anchor-frame rank, not a compatible state frame in
the completion. The normalized augmentation comb is non-Cauchy under growing
cutoffs and belongs naturally to the continuous dual. The
remaining theorem must show that the augmentation--control frame maps into the
analytic seam as a rigged state--covector correspondence.

The uniform finite Gram floor does not prevent completion escape. It records
finite separation only.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_augmentation_control_normal_frame.py
```
