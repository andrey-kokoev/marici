# WET matching-domain correction

## Defect

WP511 is an executable instrument on two local WET coefficient rays declared
at 160 GeV. WP516 instead supplies fourteen propagating poles between
0.0120565 GeV and 4.94626 GeV. Comparing the algebraic zero-momentum source
coefficient directly with WP511's likelihood does not define the missing
threshold matching and running map.

All fourteen poles lie below the declared WET coordinate scale. This does not
mean a low-energy effective description is impossible. It means that the
specific composition

    propagating source poles
      -> WET coefficient at 160 GeV
      -> DeltaM_s

has an undeclared first arrow. The source must be transported through its
finite propagators and thresholds before the WET instrument can act.

## Exact audit

The checker reads the matching scale from WP511's admitted-domain declaration
and compares it with the complete WP516 mass list:

- matching coordinate: 160 GeV;
- lightest pole: 0.0120565 GeV;
- heaviest pole: 4.94626 GeV;
- poles below the matching coordinate: 14 of 14;
- declared source-to-WET threshold constructor: none.

The formal ratio \(b/a=1/400\) remains below WP515's contact-coordinate upper
bound. That statement is algebraically true but carries no source-instrument
compatibility authority.

## Disposition

WP516--WP518 retain their source-model mass spectrum, mass-basis vertices,
current residues, and partial-width calculations. Their former
\(B_s\)-compatible label is withdrawn.

- State domain: WP516's propagating fourteen-pole source packet.
- Instrument domain: WP511's two WET coefficient rays at 160 GeV.
- First nonfaithful arrow: source pole packet to undeclared threshold matching
  and running to the WET coordinate.
- Classification: instrument-domain criticism; neither selector nor
  rigidifier.
- Smallest exact falsifier: all fourteen source poles lie below 5 GeV while
  the instrument coordinate is declared at 160 GeV, with no named interface
  constructor.

Restoring the claim requires finite-momentum \(\Delta B=2\) exchange, legal
threshold matching for each pole, running to the hadronic domain, and a fresh
evaluation of the calibrated \(\Delta M_s\) likelihood. Until then WP515's
bound cannot certify WP516's source point.
