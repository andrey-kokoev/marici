# Fuel scanner phase theorem and public completion

Status: written proof against freshly read `fuel_scanner.py`, supported by bounded tests, not formal Python verification. Inputs are constructor-generated complete binary words, unary cursor and unary fuel, with fresh allocation and valid linear wiring. Arbitrary imported states and unrestricted loops are excluded.

## Boundary invariant

FUEL owns three disjoint complete chains: support w at s, cursor K^c N at u, remaining fuel K^f N at p. Its r,o,c continuations lead to distinct passive RET/OUTCOME/ACK roots. There are no other operation-owned agents at this boundary. The constructor establishes this invariant, with an outcome still pending.

For f>0, FUEL--K consumes one fuel cell and instantiates exactly triple-cursor preparation. START holds the support and residual fuel passively; its principal waits for preparation DONE. Cutting its query/insertion/cursor/acknowledgment peers to leaves gives the proved preparation component. START--DONE can therefore release COPY/QB only with three complete disjoint cursor chains. One is consumed as the query budget; TEST holds the other two and the fuel passively.

TEST's principal waits for query DONE, not the Boolean. Cutting TEST.s,b,p gives the acknowledged single-query interfaces. Its NIL argument implies complete retained support and no query/COPY/EA work at TEST--DONE. That rule promotes the Boolean to CHOOSE.p, consuming completion first. CHOOSE--FALSE creates one ABc with the saved budget; NEXT owns its result/acknowledgment continuations and retains the other cursor and fuel. The insertion cut lemma gives complete updated support and exhausted insertion work at NEXT--DONE. NEXT allocates one K before the retained cursor and recreates FUEL, restoring the invariant with add(c,w), c+1 and f-1. It does not duplicate the residual fuel or cache a host cursor value.

All these cuts are justified by passive auxiliary peers and distinct linear endpoints; no whole-net forest assumption is used. Only the query component admits concurrent internal redexes; its termination argument already covers their order.

## Terminal phases

FUEL--N consumes the zero-fuel NIL, returns support and publishes EXHAUSTED. EA consumes the cursor, including its NIL; FINISH waits for this DONE, then SEAL consumes the private TOKEN and emits final DONE. Nothing else remains.

CHOOSE--TRUE consumes the internal query Boolean, returns support and publishes FOUND. EA erases the saved insertion budget; CLEAN consumes that DONE and launches EA on the retained cursor; DRAIN consumes its DONE and launches EA on residual fuel; FINISH consumes the last cleanup DONE; SEAL consumes TOKEN and emits final DONE. Each cleanup target is a complete finite chain, and each is consumed exactly once. Intermediate acknowledgments cannot reach public ACK because their outside peer is the next private phase principal. Therefore final ACK implies all cursor copies, fuel, controllers and private tokens are gone.

The final components are precisely RET plus returned word/NIL, OUTCOME plus FOUND/EXHAUSTED, and ACK plus DONE. Total live agents = n_final+6. The outcome and root identities remain immutable after publication.

## Termination and cost

Each nonterminal cycle decreases remaining fuel by one. Between boundaries, preparation, query and insertion terminate by their isolated arguments; terminal cleanup is a finite serial composition. Hence every maximal actual-rewrite sequence terminates after at most initial fuel queries and updates. This is runtime recurrence with fixed control rules, not a theorem of unbounded termination or arbitrary branch programs.

For current word length n, cursor c, positive fuel f (residual r=f-1):

* False cycle back to FUEL: 2n+5c+14 rewrites.
* True terminal path including cleanup: 2n+5c+r+18 rewrites.
* Zero-fuel terminal path: c+4 rewrites.

The false sum is FUEL1 + preparation(2c+4) + START1 + query(2n+c+3) + TEST1 + CHOOSE1 + insertion(2c+2) + NEXT1. The true sum replaces insertion/NEXT with erasures(c+1,c+1,r+1) and CLEAN/DRAIN/FINISH/SEAL4. Sum per visited boundary to obtain total cost. The105-fixture regression now checks this exact formula and still passes5720 total rewrites.

## Observation contract

`observe()` returns outcome=None while pending, then FOUND or EXHAUSTED; complete is independent and requires ACK--DONE. Word is None until complete, even if RET already holds the returned chain. Both outcomes are deliberately published before cleanup. Two prefix witnesses leave EA pending after outcome publication, then observe16 terminal cleanup rewrites in total; observations do not mutate the net. Thus neither outcome tag licenses early reuse of the whole runtime.

## Next scope

The standalone scanner now has a written phase/cost theorem and public observation contract. The next valuable composition obligation is embedding its final support/ACK into a strict successor gate, with the outcome retained separately and cleanup deliberately delayed. That tests whether the recurrent controller has the same contextual completion interface as finite straight-line instructions. No arbitrary loop-body generalization is needed yet.
