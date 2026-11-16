# Equivariant history admission: exact obstructions and the tour-induced cover

## Source and scope

The source is the directed four-vertex occurrence set

\[E(Q)=\{AB,BC,CA,AD,DB,BA\}.\]

Each symbol is a distinct generator; `AB` and `BA` are not inverse histories. The actual source automorphism is \(s=(AB)(CD)\), and \(H=\langle s\rangle\) has order two. The two global triangle permutations generate \(G=A_4\). Their action on vertices is not an action on the six primitive occurrence generators. The results below analyze precise *extensions* of that source; they are not new native Agda derivations.

Sources: [actual seed](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/ActualSeedEndpointTable.agda), [free-history separation](https://github.com/andrey-kokoev/marici/blob/main/research/nima/agda/SeedSeamPathComparisonBoundary.agda), [native automorphism](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/agda/NativeExtensionFamilyAudit.agda), and [two source Euler tours](https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-typed-execution-and-spectral-windows.md).

## Theorem A: no strict primitive-disjoint complementary path pair

An unordered complementary pair of Hamiltonian paths on the four vertices partitions the six undirected edges of \(K_4\). The native source contains only five undirected supports, lacking \(CD\). Any endpoint-correct expansion of the missing edge requires at least two primitive occurrences; all five others require at least one each. At least seven primitive uses are necessary, while only six distinct native occurrence generators exist. Therefore no such expansion can use each primitive occurrence at most once across the complete pair.

This is a resource/no-reuse theorem, not a prohibition on replaying an occurrence or providing a fresh execution-event ID for each replay.

## Theorem B: universal free equivariant occurrence extension

The induced graph over the original vertex set has occurrence set

\[E^\uparrow=G\times_H E(Q),\qquad [gh,e]=[g,h(e)].\]

Its edge \([g,e]\) runs from \(g\operatorname{src}(e)\) to \(g\operatorname{tgt}(e)\); \(G\) acts by left multiplication. For every \(G\)-equivariant edge system \(Y\) over these vertices and every \(H\)-equivariant endpoint-preserving map \(f:E(Q)\to Y\), there is a unique \(G\)-equivariant extension

\[[g,e]\longmapsto g f(e).\]

This is the standard induction adjunction, here checked on exact finite occurrences. It has \(12\cdot6/2=36\) occurrence records arranged as six source sheets. Every ordered pair of distinct vertices is covered by three records. The 36 records form three \(G\)-orbits of twelve, each meeting the original six records in exactly two elements. An equivariant section choosing one record over each ordered pair occupies a single orbit and therefore cannot include all six original records.

The graph with one directed edge per pair (twelve total) is a quotient of this free object. That quotient is injective on the six original edges, but merges three transformed ancestry alternatives over each pair. Thus 36 is the free **transported-provenance** count, not an absolute minimum for arbitrary equivariant graph extensions.

## Theorem C: an unoriented six-state family has no equivariant directed lift

Let \(\mathcal D\) be the six *unordered* pairs of complementary Hamiltonian paths on \(K_4\). The \(A_4\)-action is transitive and \(\mathcal D\simeq G/H\). The two \(H\)-fixed decompositions are, with reverse path orientation suppressed,

\[\{ACDB,CBAD\},\qquad\{ADCB,CABD\}.\]

Let \(\widetilde{\mathcal D}\) additionally orient each of the two paths. This is a 24-element \(G\)-set, with four oriented lifts per undirected decomposition. The reflection \(s\) reverses **each** constituent path of each \(H\)-fixed undirected decomposition. Therefore \(\widetilde{\mathcal D}^{H}=\varnothing\), so

\[\operatorname{Hom}_G(G/H,\widetilde{\mathcal D})\simeq\widetilde{\mathcal D}^{H}=\varnothing.\]

The 24 directed-pair records have exactly two free \(G\)-orbits of twelve each. Each orbit projects two-to-one onto \(\mathcal D\). Consequently a two-sheeted cover \(G\to G/H\) is the smallest transitive equivariant carrier permitting directed representatives. An independent orientation mark that breaks \(H\) is the alternative.

## Theorem D: the two native Euler tours already carry this double-cover structure

Among cyclic directed walks that traverse every primitive occurrence **exactly once**, there are precisely two source words:

\[\tau_0=AB\ BC\ CA\ AD\ DB\ BA,\qquad
  \tau_1=AB\ BA\ AD\ DB\ BC\ CA.\]

They are interchanged by \(s\) modulo cyclic rotation. Thus their set \(T(Q)\) is a free transitive \(H\)-set. Inducing it gives

\[\widetilde X=G\times_H T(Q),\qquad |\widetilde X|=12,\]

which is a free transitive \(G\)-set with a natural twofold projection \(\widetilde X\to G/H\). Its deck involution is the inherited interchange of the two tours and commutes with \(G\).

Fixing one tour and choosing an oriented lift of one of the two \(H\)-fixed undirected decompositions produces an equivariant map from \(\widetilde X\) onto one of the two regular \(G\)-orbits of \(\widetilde{\mathcal D}\). There are exactly \(2\cdot4=8\) such rooted maps that factor over one of the six-state coset identifications.

For each, expand each oriented macro incidence into its unique shortest native word within the corresponding transported source sheet. This gives an exact \(G\)-equivariant full-history record, including macro cut positions. Each path **pair** expands to nine primitive occurrence uses, from six distinct transported source records. Three uses are repetitions. Hence the construction preserves history records but does not produce strict primitive-occurrence disjointness.

The complete-tour task, free induction, and chosen initial tour-to-path-pair correspondence are **explicit construction inputs**. The source does not prove a unique selection of them as native WG tasks or laws. Both \(H\)-fixed decompositions have minimal total primitive shortest-history length nine, so this simple cost does not resolve their twofold ambiguity.

## Theorem E: bounded ordered-event signatures cannot recover every history

Let \(V\) be the free integer module on the six primitive occurrence symbols, let \(I\) be the positive-degree ideal of the completed tensor algebra, and define

\[S(e_1\cdots e_m)=\prod_{i=1}^m(1+X_{e_i}).\]

This is multiplicative under concatenation, and the equality of signatures modulo \(I^{k+1}\) is preserved by pre- and post-composition. It is covariant under the actual seed reflection, which permutes the six symbols.

Take the actual based loops \(X=AB\,BA\), \(Y=AD\,DB\,BA\), and recursively define

\[P_0=X,\ Q_0=Y,\qquad P_{n+1}=P_nQ_n,\quad Q_{n+1}=Q_nP_n.\]

Both words return from \(A\) to \(A\), end with `BA`, and are distinct because their first primitive occurrences are `AB` and `AD`. Put \(U_n=S(P_n),V_n=S(Q_n)\). The identity

\[U_nV_n-V_nU_n=(U_n-V_n)(V_n-1)-(V_n-1)(U_n-V_n)\]

proves inductively that \(S(P_n)-S(Q_n)\in I^{n+1}\). Thus the degree-\(\le n\) signatures agree for every \(n\), although the raw words differ and the terminal-reader WG comparator accepts them.

This bound is sharp: project the occurrence variables `AB` and `AD` to noncommuting variables \(a,b\), and all other variables to zero. For \(n\ge1\), the coefficient of \(a^n b\) in \(S(P_n)-S(Q_n)\) equals

\[(-1)^{n-1}2^{(n-1)(n-2)/2}\ne0.\]

To prove the formula, note the first-degree common part of \(U_n,V_n\) is \(2^{n-1}(a+b)\), there are no pure-\(a\) differences, and the displayed commutator recurrence multiplies this coefficient by \(-2^{n-1}\). The base coefficient at \(n=1\) is one.

The *full* untruncated signature is faithful on finite positive words: its first-degree term gives the word length, and the top degree equal to that length contains the unique complete ordered word monomial. This is a source-defined faithful observation, not a new path equality or comparison filler. Any fixed truncation fails on sufficiently long histories.

## Admission boundary

These results establish three independent gates:

1. **Primitive resource:** direct complementarity of original occurrences is impossible without issuing new independent incidence resources or changing the meaning of disjointness.
2. **Orientation:** selecting directed histories equivariantly over the six-state quotient is impossible; the source-tour-induced double cover is a conditional remedy.
3. **Comparison:** no bounded signature-order refinement makes terminal-reader acceptance equivalent to equality of raw histories. A full faithful observer preserves the distinction but does not construct the desired higher comparison cell.

The remaining native WG task is to justify an operation that issues fresh macro-incidence identities or retains controlled reuse, and to derive a **particular** tour-to-path-bundle correspondence together with its boundary comparison law. Merely declaring the target to be a complementary-path family is not a derivation of Ramsey complementarity.

## Verification

The sibling checker `marici_history_admission_obstruction.py` uses only the Python standard library. It checks the group and induced graph, all oriented-pair orbits, both Euler tours and their inherited involution, the eight full-history equivariant maps, source occurrence counts and shortest-route costs, and signature collisions through depth six. These are independent finite checks. The universal properties and all-depth signature claims above are proved by the displayed arguments; no new Agda compilation is claimed.
