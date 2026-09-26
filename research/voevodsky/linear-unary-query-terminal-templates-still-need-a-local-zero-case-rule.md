# Linear unary-query terminal templates still need a local zero-case rule

Fresh `check_unary_query_terminal_erasure.py` checks linear boundary templates: `Q--NIL` produces one BOOL at the OUT wire and ERASE on the opposite unary head; `ERASE--UNIT` advances along the remaining tail and `ERASE--NIL` disappears. An ABSTRACT evaluator passes 4,225 (count,k) cases 0..64, using `2*min(count,k)` interior phases and `abs(count-k)+1` erasures.

A key gap is now visible: when BOTH unary heads are NIL, the abstract evaluator gives priority to budget exhaustion (answer true, notably 0>=0). A count-phase Q agent sees its own count NIL first; its active-pair rule cannot inspect the other budget head simultaneously. The local terminal templates therefore DO NOT implement this priority as written. They are not a complete interaction net, and the 4,225 evaluations must not be presented as net execution. Local linearity alone does not imply the right Boolean result.

Next build a phase protocol that always checks budget-NIL before count-NIL, including after each count/budget consumption, with explicit principal-port rewires. Test 0>=0, count=0/k>0, and count>0/k=0 at the graph level before claiming completion. Nima E/E_B interpretation remains unestablished.
