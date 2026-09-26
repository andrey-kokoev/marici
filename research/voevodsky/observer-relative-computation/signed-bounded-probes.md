# Calibrated finite probes recover interval-certified signed paths

`agda/ObserverSignedBounded.agda` uses a period-(2B+1) cover calibrated by B forward turns. A finite slot k (0≤k≤2B) denotes the ACTUAL comparison path inverse(power B) followed by power k. Its integer classifier is proved to be -B+k. The lower endpoint is the inverse B-turn path; the centre cancels to reflexivity.

Actual transport of the calibrated state through an offset path returns its original slot. This uses inverse-transport cancellation, not absolute winding. The bounded observation map is an equivalence with both roundtrips; decoding reconstructs the represented path.

More generally, Bounded(B,p) is mere existence of an interval slot whose path equals p. Such a truncated certificate suffices for faithful recovery of p. No chosen representation is extracted from the truncation: the observed state determines the decoder, and loop setness permits elimination into its correctness equality. Equal observed states therefore imply equal paths for any two interval-certified inputs.

## Exact scope

This supplies signed finite-probe recovery with an explicit interval-representation certificate. A separate automatic conversion from an ordinary numerical inequality on the signed integer classifier to that certificate has NOT been proved here. In particular, no claim is made that the current code automatically finds a sufficient common bound for every arbitrary pair of loops.

The classifier inverse law and positive-power classifier agreement are also checked in this module. Direction here remains comparison orientation, not physical time or permission to reverse an admitted machine run. The earlier unbounded finite-family obstruction is unchanged.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-signed-bounded.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Construct interval admission from signed integer bounds, rather than requiring a supplied representation certificate. Provide sufficient common-bound construction for compared loops and use the checked calibrated decoder to establish finite pairwise separation for general signed comparisons. Keep the bound's dependence on the inputs explicit.
