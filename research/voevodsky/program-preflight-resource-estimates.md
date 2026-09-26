# Reusable preflight estimates

`program_preflight.preflight(bits,instructions)` validates and normalizes finite inputs into a frozen PreparedProgram, retaining reusable tuple operands and computing bounds without graph allocation or expansion of unary integers. To execute after inspecting estimates, pass plan.bits and plan.instructions to ProgramRuntime. Do not reuse consumed original generators. PreparedProgram is a convenience record, not a trusted admission token; directly constructing one does not bypass runtime validation.

The exact postcompile initial live-node count starts at len(bits)+4. Per instruction add: member i+3, add i+2, union len(v)+2, ifadd i+t+f+5, scan c+F+4. Temporary replaced placeholders are excluded; constructor peak and total constructor allocations are NOT bounded by this field.

Rewrite estimate starts with one gate per instruction. Support-length bounds propagate as in the resource envelope. Union uses2min(n,m)+2, a monotone upper bound even when the exact branch at n=m costs one less. Conditional insertion maximizes2k+l as2max(t,f)+min(t,f). Scan uses the established conservative envelope. Monotonicity in the input-length upper bound gives induction across mixed instructions. Peak live agents are bounded by initial+2*rewrite_bound; execution fresh names by4*rewrite_bound. These are logical graph quantities, not bytes or time.

All777 bounded mixed runs satisfy exact initial node count and dominance for rewrites, live peak, execution allocations and final length. One-shot nested operands remain reusable. A scan with cursor=fuel=10^12 is estimated arithmetically without allocating its unary chains; this is not a recommendation to execute it. The updated fresh14-suite closure passes.

Input normalization still consumes finite iterables and materializes words/programs before estimating, so the utility cannot protect against huge or infinite input streams. No limit is enforced automatically. A caller may decline execution based on estimates; constructor memory and Python heap costs still require separate consideration.

Next highest-value obligation: derive constructor peak/allocation bounds including GC/GS placeholder replacement, so preflight does not imply protection at precisely the largest up-front allocation boundary. Instrument add/fresh during compilation and distinguish logical graph peak from tuple materialization. Do not add policy limits until their covered resource quantity is explicit.
