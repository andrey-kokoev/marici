# A finite witnessed history-to-interval bridge

## Frozen scope

Active SCC obligation: source forward realization and operation/composition compatibility, before metric selection or continuum completion. This proves a selected-history graph/path isomorphism and a declared controlled WG specialization. It does not prove all of WG-I1 or that an existing native WG successor already selects these operations.

Sources: `nnmhv_coherence_paths.py` defines the actual immutable history records and terminal spinor interpreter; `check_nnmhv_type_a_root_bridge.py` supplies the selected-component interval dictionary. The prior causal-diamond checker declares endpoint-extension moves independently. We now specify and compare their full-record lifts. No Hamiltonian or metric enters this construction.

## Source and declared operations

Fix an integer n >= 6 and m=n-5. Let H_n be exactly the compiler records with branch left-nested, outer first endpoint 2 and inner first endpoint 3. Inspection of the compiler gives precisely

    h_n(b1,b2) = (n, (2,b1), (3,b2), left-nested, (b1,2), U),
    5 <= b2 <= b1 <= n-1,
    U = (upper replacement (2,b1)) if b2=b1, otherwise empty.

These bounds follow from the compiler's minimum gap two. Every field, including the prefix and boundary replacement, is fixed by n,b1,b2. This is not true of arbitrary histories outside H_n.

Declare two partial source operations by editing endpoint labels and rebuilding the entire compiler-defined record:

    L h_n(b1,b2) = h_n(b1,b2-1), provided b2>5;
    R h_n(b1,b2) = h_n(b1+1,b2), provided b1<n-1.

Both operations are explicit new specializations on existing source records, not an assertion that regrouping already changes endpoints. Each transition retains its input, move tag and output. They are legal source records by the displayed inequalities. R changes the prefix; either move from a diagonal record removes its former upper replacement. Keeping either stale field is not an admitted source update.

## Object and edge isomorphism: all n

Let I_m={(i,j):1<=i<=j<=m}, with labelled edges

    L:(i,j)->(i-1,j) if i>1;
    R:(i,j)->(i,j+1) if j<m.

Define

    F(h_n(b1,b2))=(b2-4,b1-4),
    G(i,j)=h_n(j+4,i+4).

The inequalities prove both maps are well typed. Substitution gives FG=id and GF=id on complete source records, not only endpoints, because the record fields have the unique forms above. The operation domains coincide: b2>5 iff i>1, and b1<n-1 iff j<m. Direct substitution proves

    F(Lh)=L(Fh),   F(Rh)=R(Fh).

Thus F is an isomorphism of the two directed labelled graphs. This is an all-n algebraic proof; finite enumeration below is regression verification, not its justification.

## Retained paths, composition and the square

Take free path categories, retaining every edge tag and intermediate record. Apply F or G componentwise to a path. Empty paths are preserved; concatenation is preserved literally; the two maps remain mutually inverse. Associativity and units follow from sequence concatenation. No comparison of amplitudes or quotient by endpoints is used.

Where both moves exist, LR and RL end at h_n(b1+1,b2-1). Complete terminal records and their interpreted spinors agree. Their intermediate records and words differ. Consequently their equality is an endpoint comparison cell, not equality of retained paths. Passing to the thin interval-containment poset would erase this distinction and is NOT faithful on histories.

In particular, this theorem uses extension paths, not adjacent-root addition [i,j]+[j+1,k]=[i,k]. Those are different typed operations; no equivalence between them is assumed.

## Explicit controlled WG

A state is (h,w), where w is a finite L/R word admissible from h. If w=a w', the generator returns (a h,w') with witness (h,a,a h). On the empty word it returns the same state with an explicitly idle witness. This is total on the admissible-word type: admissibility of w implies admissibility of its tail at a h. The interval version uses the same word, and (h,w)->(Fh,w) intertwines both generators and their witnesses. Induction on word length yields correspondence of generated finite histories; arbitrary finite iteration after exhaustion adds matching idle witnesses, not additional interval growth.

This instantiates the state/relation/generator interface described in `typed-generator-layer-2.md`. No fresh Agda elaboration is claimed. The control word is supplied input, not a discovered autonomous schedule, physical time or selection of the user's rung phases. Recovery here retains the input witness; the destructive tail operation alone is not claimed reversible.

## Hostiles and exact tests

The standard-library checker imports the actual source compiler and compares every selected record and move for n=6..15. It enumerates every admissible move word for n=6..9, checks path reconstruction, all split compositions, both generator routes and idle witnesses, and tests full-record LR/RL endpoint equality.

Controls reject a stale upper replacement, stale prefix, an excluded source branch, an out-of-domain move and the attempt to erase LR/RL history. The source digest and all tested counts are retained in `results/wg-interval-operation-bridge.json`.

## Consequence for the holography net

Completed at written finite-theorem scope: a dictionary, full-record source lifts, labelled graph/path isomorphism, endpoint square and controlled WG realization. It is an admissible candidate for the bounded dictionary and operation-square tasks, subject to separate review.

Still missing: selection of L/R by the intended native WG law; identification with its rung schedule; a source-defined continuous endpoint action; metric/sign/scale selection; a convergent continuum realization; physical interpretation; full AdS and dS spacetimes and quantum dictionaries. Diagonal intervals remain finite source records with nontrivial boundary replacement; the continuum expression 4 du dv/(v-u)^2 is singular there. No metric is introduced or extended across that locus by this proof.

WG-I1, WG-G1/G2 and M0 remain open. Merely presenting this finite construction as a WG does not discharge their stronger source-selection and geometry requirements.
