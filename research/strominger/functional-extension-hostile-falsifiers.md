# Twelve hostile tests delimit the functional-completion theorem

1. **Scalar projection.** `p^4-q^4` has ridge kernels, while the paired spin
   symbol is elliptic. A scalar chart equation cannot replace the bundle map.
2. **Localization.** Multiplying a ridge solution by a compact cutoff creates
   a nonzero boundary source.
3. **Flat finite energy.** An `L2(R2)` Fourier function supported on four lines
   is zero; nonzero ridge waves are extended or distributional.
4. **Global low modes.** The paired sphere multiplier genuinely vanishes at
   `l=2,3,4`; ellipticity does not remove finite-dimensional smooth kernels.
5. **Energy-only no-go.** Smooth low modes admit finite-news-energy histories,
   so energy alone cannot exclude them.
6. **Endpoint-only no-go.** A returning magnetic pulse has zero endpoint
   memory but nonzero news history.
7. **Scalar-source overreach.** Positive `T_uu` constructs electric modes but
   not magnetic parity; magnetic construction requires coexact `T_uA`.
8. **Finite-puncture extrapolation.** No finite atomic packet is a pure smooth
   low harmonic, but weak-* atomic closure can converge to one.
9. **Topology smear.** Atomic measures cannot converge to a smooth density in
   total variation; calling weak-* closure a TV completion is false.
10. **Collision normalization.** Derivative jets and `(1,-3,2)` require
    diverging variation norm; bounded flux does not acquire them.
11. **Conservation shortcut.** Translation and global angular charges occupy
    `l<=1`; they do not remove the `l=2,3,4` kernel.
12. **Contour completion.** Puncture residues and grade-three downstream
    contours miss smooth low modes; 21 pre-readout harmonic ports restore them.

## Surviving claim

After all attacks:

- the local scalar characteristic locus supplies no localized global kernel;
- the global paired operator has exactly the smooth `l=2,3,4` kernel;
- finite energy and smooth hard-flux completion admit that kernel;
- finite point packets and bounded-TV atomic closure do not contain pure low
  modes;
- weak-* Radon completion does;
- a strong no-magnetic endpoint condition removes endpoint records but not
  returning histories;
- 21 magnetic harmonic ports are necessary and sufficient for complete
  grade-three faithfulness.

## Evidence

`checkers/functional_extension_hostile_falsifiers.py` realizes all twelve
countermodels and their repairs with exact symbolic gates.
