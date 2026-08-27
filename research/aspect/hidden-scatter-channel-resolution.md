# Resolution of hidden optical scatter channels

## Three different claims

Energy accounting distinguishes three levels:

- a closure residual proves that measured channels are incomplete;
- total scatter collection quantifies the omitted power;
- angular, polarization, temporal, or spectral resolution attributes that
  power among hidden channels.

The first two do not imply the third.

## Exact closure hostile

Freeze reflected, transmitted, and absorbed powers as `16/25`, `1/4`, and
`3/50`. Their deficit is `1/20`. An integrating sphere can collect that total,
but the record is compatible with all three frozen decompositions

```text
(3/100, 2/100)
(1/100, 4/100)
(0,     5/100).
```

The total-loading row `(1,1)` has rank one on the two hidden scatter channels.
The data certify missing power but neither its multiplicity nor its locus.

## Smallest separating port

Add one calibrated left-minus-right angular contrast. The two loading rows are

```text
total:    (1,  1)
contrast: (1, -1).
```

They have rank two. For total `1/20` and contrast `1/100`, the channels recover
as `3/100` and `2/100`.

A segmented integrating sphere, Fourier-plane camera, or balanced pair of
angular collectors can implement this port. Its calibration must specify the
angular loading before the desired decomposition is observed.

## More detectors can still mean rank one

Two electronics chains viewing the same integrating-sphere carrier have
proportional loading rows and remain rank one. They improve fault detection
and precision, not physical attribution.

Likewise, a wavelength scan separates two scatter mechanisms only when their
independently derived spectral signatures are nonproportional. Repeated samples
of a common spectral shape are temporal or spectral copies of one loading, not
new source information.

## Claim boundary

The checker assumes exactly two nonnegative hidden channels, exact normalized
power balance, and declared angular or spectral loadings. Unknown additional
channels, aperture loss, calibration uncertainty, and continuous scatter
distributions reopen the compatible set.

## Verification

```text
python research/aspect/checkers/check_hidden_scatter_channel_resolution.py
```
