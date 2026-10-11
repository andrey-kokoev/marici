# Bank mixing reduces to a hidden readout and a three-stage return

## Compare source operations, not fitted rotations

Keep the selected positive exchange, the carrier half-turn R=Ad_J and port C fixed. Compare two bank operations from the same Clifford multiplication:

    L_J = Ad_J tensor I,
    L_e1 = Ad_e1 tensor I.

Their left-factor signs are (1,-1,-1,1) and (1,1,-1,-1). The latter is checked directly from the existing product, not introduced as numerical fit data. Both are orthogonal involutions with C L C^T=0 and both pass the existing ordinary/twisted tetrahedral response test.

## Common observable dynamics

For any such mixer, define

    a=Ct,  b=CLt.

Substitution into the already selected exchange gives

    x'=b,
    a'=Rx,
    b'=a.

The last identity follows from L^2=I and CLC^T=0; the second from CC^T=I. Thus the observed dynamics is

    (x,a,b) -> (b,Rx,a),
    x_(n+3)=R x_n.

Its initial carrier sequence is determined by x, CLt and Ct. With the supplied R^2=I, it returns after six steps. These are traversal stages, not a derived physical clock.

The full bank splits orthogonally as

    t=C^T a + L C^T b + k,
    Ck=CLk=0.

The residual evolves as k'=Lk and never reaches these ports under the fixed schedule. The observed state has twelve dimensions and the retained residual eight. This is a concrete realization of the prior four-packet decomposition, now used to locate the selection question rather than introduce another coupling.

## Explicit equivalence of the two tested mixers

Within each fixed Clifford product-index fiber k=i xor j, interchange the left coefficient indices 1 and 3, leaving 0 and 2 fixed. Set the new right index to preserve k, and compensate by the old/new multiplication signs. This gives a signed permutation B satisfying

    B^2=I, B^T B=I, CB=C,
    B L_e1=L_J B.

On the whole state S=diag(I4,B) intertwines the full updates and fixes the observation (x,Ct). The ordinary/twisted fixture banks are fixed by B. A general bank that separates the laws in fixed coordinates ceases to separate them when the adapter is transported consistently.

As before, this is a numerical coordinate equivalence. It may mix the separately interpreted tensor factors. It does not automatically authorize interchanging typed source edges, or establish a physical gauge policy.

## Sharpened remaining question

For a tetrahedral package P and a chosen bank adapter E(P), the responsive datum is

    b(P)=C L E(P).

The next useful selection problem is to justify this hidden readout from the retained witnesses, with its coordinate transformations and declared observations, rather than fit another closure factor. In the successful fixture, E(P) is the ordered two-edge matrix tensor and b(P) distinguishes ordinary from twisted even when CE(P) agrees.

This calculation does not prove that every admissible mixer belongs to the tested equivalence class. Its normal form assumes an orthogonal involution with zero compressed port CLC^T; those conditions are not derived universally from WG. The adapter, metric, carrier R and physical scale likewise remain explicit inputs. No gravitational coefficient is obtained.

## Verification

`python research/nima/checkers/check_bank_mixing_normal_form.py` passed with exact rational conjugation, full matrix intertwining, observable recurrence, rank, conservation and fixture-response checks. Results: `results/bank-mixing-normal-form.json` with source digests.

No prior dynamics implementation was modified. No ledger entry, commit or publication is claimed.
