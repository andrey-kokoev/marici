import { z } from "zod";
import { inspectColorBalance } from "./color-balance.js";
import { type DiagramDocument } from "../schemas/document.js";
import { type LogicalCoordinate, type LogicalPoint } from "../schemas/layout.js";
import {
  RouteResultSchema,
  type ActiveColor,
  type RouteResult,
  type RouteStep,
  type Turn,
} from "../schemas/traversal.js";

const FractionSchema = z.strictObject({ n: z.bigint(), d: z.bigint().positive() });
type Fraction = z.infer<typeof FractionSchema>;
function fraction(value: LogicalCoordinate): Fraction {
  return typeof value === "number"
    ? { n: BigInt(value), d: 1n }
    : { n: BigInt(value.numerator), d: BigInt(value.denominator) };
}
function subtract(a: Fraction, b: Fraction): Fraction {
  return { n: a.n * b.d - b.n * a.d, d: a.d * b.d };
}
function multiply(a: Fraction, b: Fraction): Fraction {
  return { n: a.n * b.n, d: a.d * b.d };
}
// Exact model arithmetic. Screen coordinates never enter routing.
// Authored red/blue classes govern eligibility, not angular ranking or CSS colors.
function turn(a: LogicalPoint, b: LogicalPoint, c: LogicalPoint, d: LogicalPoint): string {
  const ix = subtract(fraction(b.x), fraction(a.x)),
    iy = subtract(fraction(b.y), fraction(a.y));
  const ox = subtract(fraction(d.x), fraction(c.x)),
    oy = subtract(fraction(d.y), fraction(c.y));
  if ((ix.n === 0n && iy.n === 0n) || (ox.n === 0n && oy.n === 0n)) return "degenerate";
  const cross = subtract(multiply(ix, oy), multiply(iy, ox));
  if (cross.n < 0n) return "left";
  if (cross.n > 0n) return "right";
  const x = multiply(ix, ox),
    y = multiply(iy, oy);
  return x.n * y.d + y.n * x.d > 0n ? "straight" : "reverse";
}
export function traceRoute(
  document: DiagramDocument,
  startId: string,
  initialTurn: Turn = document.policy.status === "alternating"
    ? document.policy.initialTurn
    : "left",
  reverse = false,
): RouteResult {
  const steps: RouteStep[] = [];
  const colorBalance = inspectColorBalance(document);
  const styles = new Map(document.layout.edges.map((value) => [value.edgeId, value]));
  const coloredEdges = document.graph.edges.filter((edge) => {
    const color = styles.get(edge.id)?.color;
    return color === "red" || color === "blue";
  });
  const visitedColored = new Set<string>();
  let activeColor: ActiveColor | null = null;
  const remaining = () => coloredEdges.filter((edge) => !visitedColored.has(edge.id));
  const finish = (
    status: RouteResult["status"],
    message: string,
    candidates: RouteResult["candidates"] = [],
  ) =>
    RouteResultSchema.parse({
      document: { documentId: document.id, revision: document.revision },
      policyVersion: document.policy.status === "alternating" ? document.policy.version : null,
      initialTurn,
      activeColor,
      colorBalance,
      remainingColoredEdges: remaining()
        .map((edge) => edge.id)
        .sort(),
      steps,
      status: status === "completed" && !colorBalance.balanced ? "invalid-color-balance" : status,
      message: !colorBalance.balanced
        ? `Invalid color balance: ${colorBalance.red} red, ${colorBalance.blue} blue; counts must be equal. ${status === "completed" ? "All colored edges were traversed, but the diagram is not valid." : message}`
        : message,
      candidates,
    });
  if (document.policy.status !== "alternating")
    return finish("unresolved", document.policy.questions.join(" "));
  if (document.graph.edges.some((edge) => edge.direction === "unresolved"))
    return finish("unresolved", "Edge directions are unresolved.");
  const start = document.graph.edges.find((edge) => edge.id === startId);
  if (
    start === undefined ||
    (reverse && start.direction !== "both" && start.direction !== "undirected")
  )
    return finish("invalid-start", "Choose an existing edge and an allowed explicit direction.");
  const placements = new Map(
    document.layout.vertices.map((value) => [value.vertexId, value.position]),
  );
  let current: RouteStep = {
    edgeId: start.id,
    from: start.direction === "to-from" || reverse ? start.to : start.from,
    to: start.direction === "to-from" || reverse ? start.from : start.to,
    pendingTurn: initialTurn,
  };
  const seen = new Set<string>();
  while (true) {
    const color = styles.get(current.edgeId)?.color;
    if (color === "red" || color === "blue") {
      activeColor = color;
      visitedColored.add(current.edgeId);
    }
    // Switch before choosing an exit, not after entering the first edge of the
    // next color. Green travel retains this phase, including its ranking priority.
    const unvisited = remaining();
    let phaseChanged = false;
    if (
      activeColor !== null &&
      unvisited.length > 0 &&
      !unvisited.some((edge) => styles.get(edge.id)?.color === activeColor)
    ) {
      phaseChanged = true;
      activeColor = activeColor === "red" ? "blue" : "red";
      current = {
        ...current,
        pendingTurn: current.pendingTurn === "left" ? "right" : "left",
      };
    }
    const key = JSON.stringify([
      current.edgeId,
      current.from,
      current.to,
      current.pendingTurn,
      activeColor,
      [...visitedColored].sort(),
    ]);
    if (seen.has(key))
      return finish(
        "repeated-state",
        "Stopped before repeating an edge/direction/turn/color/visited-set state.",
      );
    seen.add(key);
    steps.push(current);
    const style = styles.get(current.edgeId),
      source = placements.get(current.from),
      end = placements.get(current.to);
    if (style === undefined || source === undefined || end === undefined)
      return finish("degenerate-geometry", "Missing authored placement.");
    const edge = document.graph.edges.find((value) => value.id === current.edgeId);
    if (edge === undefined) return finish("invalid-start", "Missing edge.");
    const forward = current.from === edge.from;
    const incoming =
      style.via.length === 0 ? source : forward ? style.via[style.via.length - 1] : style.via[0];
    if (incoming === undefined) return finish("degenerate-geometry", "Missing incoming tangent.");
    if (turn(incoming, end, incoming, end) === "degenerate")
      return finish("degenerate-geometry", "Zero-length incoming tangent.");
    if (coloredEdges.length > 0 && visitedColored.size === coloredEdges.length)
      return finish("completed", "Completed: every red and blue edge visited exactly once.");
    const phaseRemaining = remaining().filter(
      (value) => styles.get(value.id)?.color === activeColor,
    );
    const choices: RouteStep[] = [];
    let degenerate = false;
    let extremeExit: LogicalPoint | null = null;
    let bestScore = -2;
    let bestPriority = -1;
    for (const next of document.graph.edges) {
      if (next.id === current.edgeId) continue;
      const nextColor = styles.get(next.id)?.color;
      if (nextColor === "red" || nextColor === "blue") {
        if (visitedColored.has(next.id)) continue;
        if (phaseRemaining.length > 0 && nextColor !== activeColor) continue;
      }
      const outbound = next.from === current.to && next.direction !== "to-from";
      const inbound = next.to === current.to && next.direction !== "from-to";
      if (!outbound && !inbound) continue; // Incidence by IDs only.
      const nextTo = outbound ? next.to : next.from,
        target = placements.get(nextTo),
        nextStyle = styles.get(next.id);
      if (target === undefined || nextStyle === undefined) {
        degenerate = true;
        continue;
      }
      const exit =
        nextStyle.via.length === 0
          ? target
          : outbound
            ? nextStyle.via[0]
            : nextStyle.via[nextStyle.via.length - 1];
      if (exit === undefined) {
        degenerate = true;
        continue;
      }
      const kind = turn(incoming, end, end, exit);
      if (kind === "degenerate") {
        degenerate = true;
        continue;
      }
      if (kind === "reverse") continue;
      const candidate: RouteStep = {
        edgeId: next.id,
        from: current.to,
        to: nextTo,
        pendingTurn:
          // The color transition already flipped the preference. Do not
          // immediately flip it back while entering the phase's first exit.
          kind === "straight" || phaseChanged
            ? current.pendingTurn
            : current.pendingTurn === "left"
              ? "right"
              : "left",
      };
      // One signed angular order over all eligible non-reversing exits.
      // Signs order angles across zero; cross-products order angles within a sign.
      // Never reverse the comparison merely because all exits lie on the other side.
      // Continue straight on green before leaving the connector for a colored
      // arrow. Own-color arrows outrank turn preference, including immediately
      // after a phase switch. Arrowheads and visit-once remain eligibility guards.
      const priority =
        color === "green" && nextColor === "green" && kind === "straight"
          ? 2
          : activeColor !== null && nextColor === activeColor
            ? 1
            : 0;
      const angleSign = kind === "left" ? -1 : kind === "right" ? 1 : 0;
      const score = angleSign * (current.pendingTurn === "left" ? -1 : 1);
      const farther =
        extremeExit === null ? current.pendingTurn : turn(end, extremeExit, end, exit);
      if (
        priority > bestPriority ||
        (priority === bestPriority &&
          (score > bestScore || (score === bestScore && farther === current.pendingTurn)))
      ) {
        choices.length = 0;
        choices.push(candidate);
        extremeExit = exit;
        bestScore = score;
        bestPriority = priority;
      } else if (priority === bestPriority && score === bestScore && farther === "straight") {
        choices.push(candidate); // Distinct edges on the same extreme ray remain a genuine tie.
      }
    }
    if (degenerate)
      return finish("degenerate-geometry", "An incident exit has no defined tangent.");
    if (choices.length > 1)
      return finish(
        "ambiguous",
        "Stopped: distinct edges share the same extreme continuation ray.",
        choices.map((value) => value.edgeId).sort(),
      );
    const next = choices[0];
    if (next === undefined)
      return finish(
        "no-continuation",
        phaseRemaining.length > 0
          ? `Stopped: no eligible non-reversing continuation; unvisited ${activeColor} edges: ${phaseRemaining
              .map((value) => value.id)
              .sort()
              .join(", ")}.`
          : "Stopped: no eligible non-reversing continuation.",
      );
    current = next;
  }
}
