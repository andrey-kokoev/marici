# Continue past the conditional channel: source closure and all-face dressing

## Two checks that the earlier construction still needed

We did not stop at assigning a charge-compatible auxiliary. We tested whether it could be extracted from the retained carrier, and whether the response ordering depended on selecting favorable contacts.

### Source-only elimination does not create the added interaction

For every tested contact w, let R(t)=<w,(K+tI)^(-1)w> and h00=<w,Kw>. Actual elimination of the remaining source modes gives

    Sigma(-t)=h00+t-1/R(t).

Every contact overlaps the coherent zero mode, so R(t) has a positive-residue 1/t pole. Consequently

    Sigma(0)=h00,
    h00-Sigma(0)=0.

The source's contact term and self-energy cancel exactly at the coherent ground state. Merely renaming retained modes as an auxiliary does not yield the independently supplied gap and exchange law of the preceding candidate. The zero ground energy is preserved by exact elimination.

This applies the existing Schur-response method rather than proposing another charging mechanism. It identifies a real missing interaction, not an overlooked algebraic reduction.

### Arbitrary shared-edge contacts do not have a universal ordering

We compared 18 actual proton shared edges with seven belt representatives, covering 126 contact pairs under the retained Hamiltonians:

- 78 have an exact positive-polynomial certificate that the proton response is larger for every positive argument;
- 40 have exact rational counterexamples to that ordering;
- 8 remain uncertified by the current certificate and sample tests.

The earlier result for the explicitly marked proton AB/BA and belt cross-face bridge remains correct. It must not be promoted to a statement about arbitrary contacts. All six proton **cross-face** contacts compared with the selected belt cross-face bridge do pass the global certificate.

These comparisons hold the Hamiltonians fixed and vary the physical probe location. They are not a relabelling of both Hamiltonian and probe together.

## A whole-geometry contact rule

The next construction uses all cross-face interfaces, rather than a selected pair. An actual shared edge is cross-face when its two small triangles have different parent-face labels.

Both carriers have **six** such interfaces:

- the proton's six contacts cover all twelve small triangles;
- the belt's six contacts cover twelve of its eighteen small triangles.

For the belt, three of these edges lie between the previously chosen paired sectors. They must be included in a whole-geometry field contact even though they were not among the 21 within-group formation seams. The formation Hamiltonian is not changed; this is a different list of external contact addresses.

Declare equal phase and equal strength at all six normalized contacts. This is one coherent field profile, not six independent occupation registers. The six contact vectors have disjoint support, so their sum has squared norm six on both carriers. Equal phase and strength are interaction inputs; geometry supplies the addresses and modes, not the physical field preparation.

## Exact reduction of the coherent profile

For the proton, the normalized sum is exactly its coherent return vector. Its normalized response is

    R_p(t)=1/t.

For the belt, the sum lies in exactly two source eigenmodes:

    a=4485/3292,
    r=2386/4485,
    R_b(t)=r/t+(1-r)/(t+a).

The first component is the coherent mode. The other is a face-even collective excitation. The checker verifies this support directly against the full 36-dimensional Hamiltonian, not merely against a fitted two-level matrix.

For the unnormalized equal-per-contact coupling, both responses acquire the same factor six. Therefore

    6 R_p(t)-6 R_b(t)
      = (6297/1646)/[t(t+4485/3292)] > 0.

The ordering is now an elementary exact identity for the specified all-face profile. It does not depend on choosing one favorable cross-face contact or giving the two particles different numbers of contact couplings.

## The resulting internal-channel model

Reuse the previously declared charge-compatible internal auxiliary, common gap Delta and common coupling g per contact. Its binding shifts satisfy

    Delta+x_p=6g^2/x_p,
    Delta+x_b=6g^2[r/x_b+(1-r)/(x_b+a)].

Thus x_p>x_b, and with a shared bare offset mu>x_p,

    E_b-E_p=x_p-x_b>0.

The proton shift is a quadratic root. The belt shift is the unique positive solution of

    x^3+(Delta+a)x^2+(Delta*a-6g^2)x-6g^2*r*a=0.

For the unfitted control Delta=g=1/2, x_p=1 exactly and x_b is approximately 0.809292454971. Taking common mu=2 keeps both sectors above the empty reference; the difference is approximately 0.190707545029 in the common unit.

This number is not a mass prediction. No electron normalization is supplied, and these parameters were not chosen from measured masses.

## What has been narrowed

The candidate's structural distinction is now explicit: the same coherent all-face interaction addresses the entire proton return, but only a two-mode combination of the belt. The stronger proton dressing leaves the belt higher under the shared auxiliary law.

However, the source-only elimination check proves that this auxiliary law is **not already hidden in the retained constraint Hamiltonian**. It still requires a physically supplied internal excitation or field interaction. The preceding charge assignment makes such a coupling consistent; it does not establish that nature supplies it.

The next needed evidence is therefore a source-supported interacting field/action fixing the common internal channel, its coherent profile and energy scale. Further rearrangement of the present positive constraint operator cannot replace that evidence. No claim is made that all other physical completions fail.

## Artifacts and checks

    python research/voevodsky/checkers/check_contact_source_closure.py
    python research/voevodsky/checkers/check_all_face_contact.py

Results:

- `research/voevodsky/results/contact_source_closure.json`
- `research/voevodsky/results/all_face_contact.json`

The first retains exact counterexamples, unresolved pairs and source-only Schur limits. The second retains every cross-face address, exact spectral weights and a rational interval for the illustrative cubic root.
