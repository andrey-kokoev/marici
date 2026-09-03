# Nonzero exceptional linking period of the grade `-1` sewn class

## Question

Can the nonzero cohomology class be paired with an explicit algebraic cycle even though the physical positive-cut chain remains unspecified?

## Explicit cycles

On the `q_g3` component, use counterclockwise small meridians `gamma_-1` around `xi=-1` and `gamma_kappa` around `xi=kappa`, chosen in a generic chamber with `p != 0` and `kappa != -1`. For

\[
\omega_3=-\frac{d\xi}{64p^4(\kappa-\xi)(\xi+1)},
\]

execution `structured_command_execution:e_30844_1788300869163082800_10` gives

\[
\oint_{\gamma_{-1}}\omega_3
=-\frac{i\pi}{32p^4(\kappa+1)},
\qquad
\oint_{\gamma_{\kappa}}\omega_3
=\frac{i\pi}{32p^4(\kappa+1)}.
\]

Both periods are nonzero generically and their sum vanishes, as required by the homology relation between the two finite meridians on the punctured projective line.

## Sheet and orientation tests

Reversing the exceptional square-root sheet multiplies the form and both periods by `-1`. Reversing a meridian orientation does the same. Thus the period detects the previously fixed positive-sheet orientation rather than only absolute nonvanishing.

## Typed conclusion

This is an explicit algebraic linking-cycle pairing. It proves that the grade `-1` sewn class has nonzero period capability on the exceptional wall. It does not identify either meridian with the physical positive-cut chain. Such an identification requires a source-derived homology or relative-chain map, not equality of nonzero periods.

## Strongest falsification attempt

The class could have been nonexact yet pair trivially with the simplest local cycles. Exact residue evaluation rejects that possibility. The surviving alternative is that the physical positive-cut chain lies in a distinct homology class or in the kernel of this cohomology class.

## Disposition

The grade `-1` sewn class has explicit nonzero positive-sheet linking periods with controlled orientation and sheet reversal. Physical positive-cut pairing remains blocked only at the missing chain-identification map.

## Evidence

- `research/nima/checkers/check_grade1_exceptional_linking_period.py`
- `research/nima/qG12-grade1-positive-sheet-residue-comparison.md`
- `research/nima/qG12-grade-minus-one-sewn-cech-class.md`
