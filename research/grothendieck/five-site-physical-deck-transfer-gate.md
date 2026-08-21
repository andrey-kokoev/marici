# Five-site physical deck-transfer gate

## Verdict

The unnormalized fiber sum

\[
 (\phi_!f)(h)=\sum_{\phi(g)=h}f(g)
\]

is the canonical algebraic covariant operation on finite deck-function algebras.  The
frozen five-site source, however, does **not** yet admit it as a physical readout
transfer.

## Exact obstruction

The five-site Kummer cover has deck group \(G=(C_2)^5\).  In sheet bases the
coefficient--Betti pairing is

\[
 \langle e_g,\Gamma_h\rangle=\delta_{g,h},
\]

and simultaneous deck transport preserves this pairing exactly.  The physical
source chain is the chamber-selected vector \(\Gamma_+=\Gamma_0\), not an invariant
cycle.  Its orbit trace \(\sum_g\Gamma_g\) pairs with every \(e_h\) as 1, producing
31 mismatches with the selected delta readout.  The normalized average pairs as
\(1/32\) on every sheet and produces 32 mismatches.  Thus neither trace nor average
is the same observable.

This does not contradict the rank-32 finite pushforward of the intrinsic Kummer
connection.  That construction packages the cover as a coefficient local system on
the base; it does not supply a physical transfer between deck groups for an
arbitrary homomorphism \(\phi:G\to H\).

## Admission boundary

To cross the gate one needs a source-derived geometric map of covers inducing
\(\phi\), together with a relative-cycle trace/Gysin operation whose orientation,
support, multiplicity, endpoint regularization, and chain normalization are fixed.
Until that datum is present, fiber-sum transfer remains algebraically canonical but
physically untyped.  This is a present-source obstruction, not an impossibility
theorem for future constructions.

## Reproduction

Run:

```powershell
python research/grothendieck/checkers/five_site_physical_deck_transfer_gate.py
```

The exact certificate is written to
`research/grothendieck/results/five-site-physical-deck-transfer-gate.json`.
