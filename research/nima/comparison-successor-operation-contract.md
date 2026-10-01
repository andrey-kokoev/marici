# Consolidated comparison-successor operation contract

## Scope and source authority

The stated architecture promotes each retained family to one fresh label and
keeps all its members (docs/system-characteristics.md, software architecture).
The fibration reconstruction theorem concerns record presentations. The typed
137-slot assembly supplies maps, a direct reference and matrix responses.

Those sources do not select a physical active-reference update law. This contract
separates source-defined operations from conditional constructions and supplies
one finite candidate protocol for testing the latter. The carrier's S4 symmetry
justifies relabelling; interpreting permutations as active interventions with
history held fixed is an additional, explicit choice.

## State and operation ledger

Retain actual maps, d and any return r; typed witnesses u,v,W; comparison
histories; labelled member records; a declared readout; and the scope of any
admission/cost policy. No metric or inverse is inferred from a label count.

| Operation | Rule | Status and required input |
|---|---|---|
| Re-present retained records | Label/from/to indexing with exact reconstruction | Checked record semantics; field selector retained |
| Passive frame change | Transport maps, witnesses and any metric together | Conditional on a typed representation of the relabelling |
| Fixed-frame comparison | C_new=C2*r*C1, with recorded reference correction and higher witnesses | Checked DG construction; return/unit data required |
| Witnessed reference substitution | Select an existing comparison/family anchor; keep actual maps fixed and version witnesses using its reference-change witness | Checked fixed-domain operation; selection and physical reference-mask policy remain inputs |
| Protected active frame request g | C'=g*C, d'=g*d, r'=r*g^-1, keep u,v fixed | Separate candidate operation; must pass the admission equations below |
| Permitted history edit | Preserve declared readouts and unit/triangle equations; retain parents and cost | Checked policy; permissions and metric are inputs |
| Family promotion | One fresh label per declared group, all members retained | Selected architecture; grouping keys and next endpoints still required |
| Uniform family admission | A common request must pass every retained member | Candidate joint-action policy; permissions intersect |
| Independent carrier copying/pairing | Explicit extra operand constructor | Separate model choice; never inferred from fresh labelling |

The conservative protocol rejects an unsupported or incompletely specified
operation. The constructions below do not silently supply missing next-level
endpoint maps or a physical schedule.

## Protected active requests: admission and update law

Assume a coherent weak return

    delta(u)=r*d-1_A, delta(v)=d*r-1_B,
    delta(W)=d*u-v*d.

Take a closed invertible g:B->B. With u,v protected, admission requires

    [g,delta(v)]=0,
    [g,v]=delta(K_g)

for a degree-two certificate K_g in the allowed filler space. With full filler
support these conditions are necessary and sufficient for a new triangle.
A constructive update is

    W_new=g*W+K_g*d.

Indeed its boundary is g*d*u-v*g*d. Conversely, if a new triangle exists, set
T=[g,v] and Q=W_new-g*W. Then delta(Q)=T*d and

    K_g=Q*r+T*v

has boundary T. This uses delta(v)=d*r-1_B and closedness of T.

Certificates update under the same operation:

    K_(h*g)=h*K_g+K_h*g,
    K_(g^-1)=-g^-1*K_g*g^-1.

The exact checker verifies two active steps, their direct composite and inverse
return, keeping unit histories fixed. A history edit v->v+delta(Z) changes a
certificate to K_g+[g,Z] and preserves the admission profile in the full-support
frame. Restricting support or adding a budget gate can change that conclusion.

### Important refinement of the preceding counterexample

The singular-reference fixture used to exhibit14 invisible coherent-history
directions has H1(End B)=0. Its closed unit-history edits therefore share this
full-support admission profile. The earlier accept/reject counterexample used
a different zero-differential complex with nontrivial degree-one homology.
Those results must not be conflated. Closed history can affect admission through
its nontrivial class, or through separately declared support/readout/cost gates.

## Finite carrier candidate: an exact admission summary

Represent S4 on two graded copies of the four-label vector space, with zero
differential. Let d=r=I and u=v be a diagonal degree-one witness with values
w_0,...,w_3. A protected active permutation admits exactly when it preserves
those values:

    H_w={g in S4 : g*w=w}.

This is the stabilizer of the partition into equal-value blocks. Testing all
256 histories with values in{0,1,2,3} yields15 admission profiles, corresponding
to the15 partitions of four labels. The subgroup order is the product of the
factorials of the block sizes.

The exact summary for this candidate protocol consists of the observed map data
and H_w. Its update rules are:

- an admitted protected active step leaves H_w unchanged;
- a passive permutation p sends H_w to p*H_w*p^-1;
- rejection leaves the state unchanged;
- a uniform request on a retained family uses the intersection of member profiles.

Equal profiles give equal future admissions under these rules. Distinct profiles
have a separating one-step permutation. Thus the profile is a minimal admission
summary relative to this request family, though it does not summarize metric
cost or arbitrary additional history observations.

## Family promotion applied twice

Under the uniform all-members policy,

    H_F = intersection over members m of H_m.

Intersection is associative and covariant under passive relabelling. It is
therefore compatible with retaining, flattening and regrouping families.

Four point-marked histories each have a six-element stabilizer. Group them in
two declared pairs, assign one fresh label to each, then repeat that pairing
constructor on the two family records. Permission-group sizes are6 at the leaves,
2 in each first family, and1 in the final family. Every original member is
recoverable and direct versus staged admission agrees.

The pairing schedule is an explicit finite fixture, not the original incoming-
fibre endpoint rule. This derives a compositional permission field for promoted
families, while leaving their next from/to fields as an open contract item.
Intersection narrows permissions; no independent-factor or gauge multiplicity
doubling follows from it.

## Reference substitution resolves one part of the choice

[Witnessed reference substitution](witnessed-reference-reanchoring.md) now supplies
a data-supported operation distinct from passive relabelling and frozen-history
intervention. Selecting a retained comparison or promoted-family anchor holds
actual maps fixed and uses its existing witness to version the comparison,
unit and triangle records. Parents are retained, and two changes agree with a
direct change. Thus history retention alone does not require frozen current
witnesses. The fixed-domain operation preserves mixed rectangles; selecting the
total mean as reference makes the mean residual zero. A physical reference and
any exclusion-mask update need their own selection rule.

## Next decision

For the separate protected-permutation protocol, the remaining choice is explicit: are reference permutations
only passive presentation changes, or also protected active interventions?
If the latter are selected, specify the candidate request family and whether a
family receives a uniform request or independently chosen member requests. The
uniform choice has the checked intersection law above. Neither a proposal
probability nor physical resource normalization has been selected.

## Verification

    python research/nima/checkers/check_weak_return_admission_law.py
    python research/nima/checkers/check_admission_profile_protocol.py

Exact DG certificate transport and its converse, composition and inversion,
H1 scope check; all256 finite histories,15 profiles, subgroup laws, two-request
active/passive controls, separating requests, two retained promotion rounds,
profile-intersection associativity and relabelling covariance.
