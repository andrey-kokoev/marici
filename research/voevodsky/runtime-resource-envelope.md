# Logical runtime resource envelope

The combined signature audit now records agent creation counts for all57 legal rule templates: each deletes exactly two distinct agents and creates at most four. Thus for a valid execution after compilation, live agents A(t)<=A(0)+2t. Every runtime fresh-name allocation in the inspected templates supplies one of those created agents, so allocator high-water increase is at most4t. These bounds concern completed rewrite states; allocating the replacement after deleting its pair does not exceed the same envelope. They exclude constructor normalization/placeholder allocations and Python bookkeeping memory.

For standalone scan with initial word length n, cursor c and fuel F, let C=c+F and N=max(n,C). Every visited positive-fuel boundary has cursor<=C, word length<=N, residual fuel<=F. The established exact costs give the conservative schedule-independent bound T<=F(2N+5C+F+18)+C+4, also valid for F=0 and early FOUND. Consequently peak agents<=A0+2T and runtime fresh names<=4T. This is intentionally loose; it is a finite input-derived envelope, not a tight space theorem.

For mixed programs, propagate upper word lengths instruction by instruction (member unchanged; add max(n,i+1); union max(n,m); ifadd max(n,t+1,f+1); scan max(n,c+F)), sum the component cost bounds plus one release per instruction, then use the same envelope with the actual postcompile A0. Pending operands and previously published results are already included in A0 or runtime allocations. No claim that a host step budget limits compilation memory follows.

Fresh measurement covers eight mixed runs with cursor0/16 and fuel0/8/32/64. Largest:135 initial agents,375 peak,90 final,22607 rewrites and45169 runtime fresh names. All per-step +2/+4 envelopes hold. Empirical peak375 is far below the loose bound45349; do not present the envelope as a measured memory prediction. Results are in `results/runtime-resources.json`.

Neither node counts nor unary fuel bound Python heap bytes, allocator internals, input-iterator work, or wall time. Dictionary/audit scans and growing identifier strings add host costs. The API remains no resource sandbox.

Next turn should turn the conservative input-derived formulas into an executable preflight estimate for already validated finite program values, compare estimated rewrite/agent bounds with actual runs, and explicitly separate estimation from enforcement. This provides a useful client decision before compilation without pretending a step budget protects constructor memory.
