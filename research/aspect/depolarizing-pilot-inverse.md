# Depolarizing optical pilot and the boundary of inversion

## Tomography can identify a channel without supplying a physical inverse

Represent polarization states by Bloch or normalized Stokes vectors. Freeze an
isotropic depolarizing pilot with parameter `p=1/2`, so every polarization
vector contracts by `1-p=1/2` while total intensity remains unchanged.

A spanning set of horizontal, vertical, diagonal, and circular probes
identifies this contraction. On exact records in the channel image, multiplying
the polarization vector by two reconstructs the input.

But that algebraic inverse is not a physical channel on arbitrary records.
A valid observed vector of length `3/4` is mapped to length `3/2`, outside the
polarization state ball. Noise, model mismatch, or an independently generated
output state can therefore produce a nonphysical reconstructed state.

## Exact injectivity can be uselessly fragile

At `p=99/100`, the channel remains linearly injective on polarization vectors,
but its inverse gain is `100`. Exact rank survives while operational recovery
collapses.

At complete depolarization, every probe maps to the same zero polarization
vector. No system-only inverse exists. Access to a retained environment or a
coherent dilation may change the experimental domain, but that is a new port,
not post-processing of the depolarized output.

## Instrument consequences

The process-tomography record should report:

- the calibrated channel family;
- contraction singular values and their uncertainty;
- the compatible image set for observed records;
- whether a reconstructed state remains physical;
- regularization or projection used when it does not.

Projecting an unphysical inverse estimate back onto the state ball may be a
useful estimator, but it is not exact recovery and can bias the scientific
contrast.

This extends the pilot hierarchy: scalar gain inversion, Jones-operator
inversion, and noisy quantum-channel inference are different constructors.

## Claim boundary

The checker treats exact unital isotropic depolarization. Anisotropic Mueller
action, nonunital loss, finite-sample tomography, environment access, and
regularized inference remain open.

## Verification

```text
python research/aspect/checkers/check_depolarizing_pilot_inverse.py
```
