# Eraser noninterference and conditional semantic preservation

This is a mathematical argument under the unified finite typed-forest invariant; not a claim that universal invariant closure has been machine verified.

## Directed ownership lemma

A query's actual support/budget path enters each data node at its principal port and leaves through its auxiliary, ending at NIL or (support only) a COPY auxiliary. An eraser's actual tail follows the same orientation. Two paths from distinct consumer ports cannot first merge at a data principal: that would require two wires at that principal. If one path starts inside the other, its head principal already has the predecessor wire, again excluding a second consumer wire. Finite acyclicity rules out repeated traversal. Thus actual non-original tails owned by different consumers are disjoint. This also separates the two tails of a Q_B/Q_S: their distinct consumer ports cannot merge.

An eraser cannot consume an original node: its admitted principal types require COPIED data; the original suffix has COPY.p as its only head consumer and original predecessor edges thereafter. Hence erasing a copied branch does not change the original suffix. Two semantic support interpretations MAY share original nodes after virtually expanding distinct COPY outputs. This is read-only interpretive sharing, not two physical consumer wires, and must not be confused with disjointness of actual copied tails.

## Rule equations

Write M(s,k) for out-of-range-false membership, s for a virtual support word and k for the remaining budget.

* Q_B--K: M(s,k+1) becomes Q_S(s,k), whose denotation is M(s,k+1).
* Q_B--N: M(s,0) becomes Q_R(s).
* Q_S--B_b: M(b::s,k+1)=M(s,k), the denotation of the new Q_B.
* Q_S--N: M([],k+1)=false, independent of the erased budget.
* Q_R--B_b: M(b::s,0)=b. Q_R--N: M([],0)=false. The spawned support eraser has no output denotation.
* COPY--B_b: each old virtual suffix b::s becomes a materialized B_b followed by the new COPY suffix s, preserving every query's interpreted word. COPY--N replaces an empty virtual suffix by NIL. This applies independently to any already materialized prefixes leading to either auxiliary.
* E--B/K/N: directed ownership excludes the consumed data from any live query's actual paths; original ownership excludes it from shared virtual suffixes. Advancing or removing the eraser therefore preserves both channel denotations. The same separation shows a Q transition does not alter the other channel's meaning.

The cases cover fifteen typed rules after expanding bit choices and eraser data types. At construction each channel denotes M(w,i) or M(w,j). Induction along any finite sequence of invariant-preserving reductions therefore preserves those values. If such a sequence reaches two BOOL--OUT components, the Booleans are the desired answers. This partial-correctness statement does not itself guarantee existence of a terminal state, domain closure, or confluence. Those use the separate structural, rank and diamond arguments.

Next integrate constructor establishment and all-rule structural closure with these semantic equations into a single reviewable theorem, explicitly including allocator state and restricting inputs to finite words/nonnegative indices. Use a proof-obligation table rather than replacing missing universal checks with the bounded result counts.
