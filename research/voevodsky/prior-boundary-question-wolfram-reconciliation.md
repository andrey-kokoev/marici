# Prior boundary-question and Wolfram reconciliation

Actor: marici.Voevodsky. Date: 2026-10-06. Source and graph search; no fresh compilation or new theorem claimed.

## Correction to the recent discussion

The prior work already explains how a question arises from a retained construction: abstract the missing evidence arguments of its rule boundary. The recent suggestions to invent arbitrary predicates P and Q omitted this mechanism. There is also a checked bridge from the rich constructor to the historical four-step table presentation; substituting a weaker four-edge-family graph and analyzing its limitations does not audit that construction.

## Located explanation and implementations

1. `research/nima/boundary-generated-questions.md`, sections "One boundary, an operation, and a question" and "Transformation, coherence, and retained distinctions". For complete packages a,b, the comparison question is the missing-evidence type K(a,b) = Sigma(e : El(a) equivalent to El(b)) [e(value(a)) = value(b)]. These are exactly the arguments needed by compare-rule. Its Boolean question is double negation of K; the actual filler and boundary are retained separately. For an already formed rule r, its premise question is the dependent product of derivations of its indexed inputs. `BoundaryGeneratedQuestions.agda` implements `question`, `Application.perform`, `Premises`, `extend-boundary`, and transport. This determines a question from a specified rule boundary; it does not choose the rule signature.

2. `research/nima/native-table-equivalence.md`. All eight constructor forms and twelve rule schemas have an independently implemented typed recursive-table presentation. Complete packages, rules, ports and retained closures are compared, not only truth values. `IndexedConstructorTables.agda` connects this presentation to the actual table cycle. `NativeTableRegression.agda` imports the actual boundary Filler and independently constructs NAND via native E/P; the operation agrees definitionally with the earlier joint-refutation operation.

3. `research/nima/fibration-constructor-equivalence.md`, "The Boolean law is exercised through the bridge". NAND is realized as sections of empty fibers over the joint-input domain. Its equivalence with joint refutation transports the complete Wolfram word to double negation, with the same stability boundary. This is already an operation-level construction/readout bridge, not merely an abstract assertion that some future interpretation might exist.

4. `research/nima/adapters/four-channel/PRIOR-WORK.md`. The historical schedule is [L,S,T] -> [S[L,T]] -> [L,T,S] -> [T[L,S]] -> [L,S,T], retaining fiber witnesses and using reversed unpacking. The generic OO/OR/RO/RR signature is explicitly not identified with it. Ledger 4305's four first-return paths are another distinct interface; selecting it on the basis of "four channels" was not justified.

5. `research/nima/wolfram-axiom-associahedral-carrier-comparison.md`. This is an explicit prior proposal relating Wolfram's nesting to the seven-leaf Catalan/associahedral sector. It records 132 tree shapes and the 4+2+1 label multiplicities. It also records that the Marici slot pattern (x,y,x,z,x,y,x) and Wolfram pattern (p,q,r,p,p,r,p) differ, and marks the proof-rewrite/cell/quotient comparisons as unconstructed. This is an explanation proposal, not a checked selection theorem.

## What the inspected definitions settle

The existing boundary mechanism supplies a principled source for questions. The rich native table construction already carries both comparison fillers and NAND operations. These facts should be reused before introducing new Boolean predicates or graph shadows.

The narrower question is which actual sequence of rule boundaries supplies the three inputs to the Wolfram expression and produces its specific syntax. In `NativeTableRegression.agda`, the table Wolfram word is explicitly defined, then `wolfram-double` and `wolfram-stable` invoke the prior Boolean theorems. That module verifies the interpretation of the word, not its selection by tetrahedral completion. The inspected associahedral note itself leaves its labelled comparison open. This search therefore does not establish the exact tetrahedron-to-nesting selector, nor establish that no such explanation exists elsewhere.

## Search coverage

Searched research and ledger Markdown for Wolfram, NAND, boundary-generated questions, nesting and the referenced constructor bridges; inspected their Agda definitions and the prior-work reconciliation. Queried the epistemic graph for Wolfram (27 matching entities over two pages). Relevant historical events include `ev-000000015543-5f45dfe7-c2b1-498d-995a-8daf8f3650a5` (indexed NAND), `ev-000000015584-f3cd96a3-ad7d-4f4b-86a8-420c42e9cd3a` (fiber/section interpretation), and `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (joint-refutation universal property). Graph admission is provenance, not theorem verification.

No new claim of absence, equivalence of all four-channel usages, or formula discovery follows. The next source-level task is to follow the retained boundary rule sequence in the rich table presentation, not restart from anonymous tetrahedral vertices.
