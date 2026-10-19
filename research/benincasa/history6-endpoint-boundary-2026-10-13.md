# History 6 endpoint coefficient and scoped boundary extraction — iteration 1

Freshly read owning endpoint evaluator/history compiler and the current F6 corner witness. History 6 has outer pair (2,6), inner pair (3,6), prefix (6,2), xi path (8,6,2), lower endpoint (2), transported upper endpoint (8,2,6). Omitting precisely the upper update replaces it by external endpoint (6).

Write k(u)=epsilon*u^T, A(u)=det[k(u),lambda5], and S(u)=xi*x23*adjugate(x36)*k(u). The source evaluator makes its eta linear form independent of the boundary spinors. Only A and one denominator sandwich depend on the upper endpoint, hence

    c6 = A(u0)*S(ut)/(A(ut)*S(u0)),
    F0 = c6*Ft,   Ft-F0 = (1-c6)*Ft.

This is a general rational endpoint identity on the declared localization, not a fitted normalization. In the existing momentum-conserving one-parameter family:

    c6(t) = (t+3)(t+12)(35t²+488t+1674)
            / ((10t²+162t+571)(20t²+261t+723)).

Exact fixtures t=0,1,2 give 20088/137611, 28561/186493, 7812/49555. All inner sparse polynomial coefficients scale by c6; the eta2/eta3 selector gives K0=c6*K and B22=(1-c6)*K. Full outer/transported/untransported prefactors, eta coefficients and denominator factors are retained in the receipt. The reduced numerator and denominator are coprime; the denominator is squarefree with four simple slice poles. These slice divisors are not physical-facet classifications. All original generalized-R denominators, A(ut)*S(u0), and <23> must remain nonzero despite reduced cancellations.

## Boundary extraction actually established

Use the proposed coefficient-valued relative differential-form module over fixed external spinor data, with the prior positive bosonized Z treated as **independent base data**. Define omega0=c6*omegaF and omegaB22=(1-c6)*omegaF. The local differential pushforward E_dR is the actual CZ branch pushforward, extended linearly over this external coefficient field; its corner map is the CZ corner pushforward on source six-forms. This changes neither form degree nor the earlier frozen orientation.

For b2 then b4 residues, target normal order Y1268 then Y1235, c6 has no chart/normal dependence in this relative module. The existing source, mixed and target residue squares therefore tensor by c6 and 1-c6. Six product-base fixture tests (three spinor fixtures times two positive Z fixtures) verify all three routes for both proposed forms, their recombination to the transported density, and nonzero orientation-flip defects.

If D is the earlier F6 corner density, the retained residual after replacing F6 by omega0 alone is (c6-1)*D, nonzero at every test. Adding omegaB22 restores zero. This is the externally weighted split of the local transported cancellation, **not** the original weighted nine-to-sector theorem. If a later extraction makes c6 a target-normal function with a pole, residue(c*omega) requires Laurent cross terms: for c=cm/z+c0 and omega=(wm/z+w0)dz, the residue is cm*w0+c0*wm, not c0*wm.

A restricted named-generator top map to Ft and its scalar component reproduces K0/B22. No boundary-superfunction/component extraction, spinor-to-bosonized external-base identification, ordinary unit canonical admission or global BCFW anchor has been constructed. The six relative differential squares cannot supply those maps.

## Continuation and verification

Next nonredundant executable test: scan history6 F0 against the owning ordinary rational A-H seed library, retaining the Ft positive control and full nonunit ratio (not merely its fermionic cell key). In parallel, a source-authorized link from spinor coefficient data to bosonized boundary extraction is still needed before physical/weighted promotion.

Checker: `checkers/check_history6_endpoint_boundary.py`.
Receipt: `results/history6_endpoint_boundary.json`.
Initial scientific algebra passed but receipt serialization failed because a SymPy degree Integer was not JSON-serializable; converting that field to int fixed the output, and the fresh complete rerun passed. This was an output failure, not a discarded scientific candidate.

Attached only as precursor evidence, with successor pins v28; all scientific node verdicts stay unchanged. No completion/no-continuation stop condition holds for the physical boundary extraction objective.
