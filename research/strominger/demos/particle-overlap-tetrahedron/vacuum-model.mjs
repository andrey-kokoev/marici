// Empty structured-space candidate. R (realization) indexes levels, not time.
// Delta is an explicit exploratory parameter, not a derived transition law.
export {isotopeStructureData,isotopeStructureIds} from './isotope-structure-data.mjs';

export const axisNames = ['a', 'b', 'c'];
export const axisColors = [0xf6b75a, 0x66cfff, 0xf19ad0];
const radians = degrees => degrees * Math.PI / 180;

export const roleAssignments = {MMC: ['M', 'M', 'C'], CCM: ['C', 'C', 'M']};
export function axisLabel(axis, sign) {
  if (sign !== 1 && sign !== -1) throw new RangeError('Axis sign must be +1 or -1');
  return axis.role + (sign === 1 ? '+' : '-');
}

export function frameAt(level, {turn = 60, initialAngle = 0, spacing = 1.1, assignment = 'MMC'} = {}) {
  if (!Number.isInteger(level)) throw new TypeError('R level must be an integer');
  if (!Object.hasOwn(roleAssignments, assignment)) throw new RangeError('Assignment must be the global XOR choice MMC or CCM');
  if (![turn, initialAngle, spacing].every(Number.isFinite) || spacing <= 0) throw new RangeError('Invalid frame parameters');
  const angle = initialAngle + level * turn;
  const effectiveAssignment = level % 2 === 0 ? assignment : (assignment === 'MMC' ? 'CCM' : 'MMC');
  const axes = axisNames.map((name, i) => {
    const theta = radians(angle + i * 120);
    const roles = i < 2 ? ['M', 'C'] : ['C', 'M'];
    return {name, roles, role: roleAssignments[effectiveAssignment][i], color: axisColors[i], direction: [Math.cos(theta), 0, Math.sin(theta)]};
  });
  return {level, angle, assignment: effectiveAssignment, referenceAssignment: assignment, origin: [0, level * spacing, 0], axes};
}

export function latticePatch(radius = 3) {
  if (!Number.isInteger(radius) || radius < 1 || radius > 8) throw new RangeError('Patch radius must be an integer from 1 to 8');
  const sites = [], lookup = new Map();
  for (let q = -radius; q <= radius; q++) for (let r = -radius; r <= radius; r++) {
    if (Math.max(Math.abs(q), Math.abs(r), Math.abs(q-r)) > radius) continue;
    lookup.set(`${q},${r}`, sites.length); sites.push([q,r]);
  }
  const edges = [];
  for (let i = 0; i < sites.length; i++) {
    const [q,r] = sites[i];
    for (const [dq,dr] of [[1,0],[0,1],[1,1]]) {
      const j = lookup.get(`${q+dq},${r+dr}`);
      if (j !== undefined) edges.push([i,j]);
    }
  }
  return {radius, sites, edges};
}

export function pointInFrame(frame, [q,r]) {
  const [a,b] = frame.axes.map(axis => axis.direction);
  return frame.origin.map((v,i) => v + q*a[i] + r*b[i]);
}

export function makeSpace({halfLevels = 3, radius = 3, turn = 60, initialAngle = 0, spacing = 1.1, assignment = 'MMC'} = {}) {
  if (!Number.isInteger(halfLevels) || halfLevels < 1 || halfLevels > 5) throw new RangeError('Level extent must be an integer from 1 to 5');
  const patch = latticePatch(radius);
  const frames = Array.from({length: 2*halfLevels+1}, (_,i) => {
    const frame = frameAt(i-halfLevels, {turn, initialAngle, spacing, assignment});
    return {...frame, points: patch.sites.map(p => pointInFrame(frame,p))};
  });
  return {frames, patch, normalAxis: {name: 'R', meaning: 'realization'}, parameters: {halfLevels, radius, turn, initialAngle, spacing, assignment},
    transition: 'theta[n+1] = theta[n] + turn; role[n+1] = swap_MC(role[n]); R[n] = n * spacing',
    occupants: [], scope: 'Empty frame-linked lattice candidate with alternating 2+1 C/M role assignments from one R=0 reference choice; no particle transitions.'};
}
