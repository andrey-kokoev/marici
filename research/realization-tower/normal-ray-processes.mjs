import {sulfur32Process} from './sulfur-32-process.mjs';
import {ruthenium98Process} from './ruthenium-98-process.mjs';
import {singleOctahedralProcess} from './single-octahedral-process.mjs';
import {nativeBridgeProcess} from './native-bridge-process.mjs';
import {signedOctahedralProcess} from './signed-octahedral-process.mjs';
import {trimParentHalfStep} from './p-first-parent-trim.mjs';
import {presentCentralBelt} from './central-belt-layout.mjs';
import {neutronBeltProcess} from './neutron-belt-process.mjs';
import {doubleEsd7RuleProcess} from './double-esd7-process.mjs';
import {cellFibrationProcess} from './cell-fibration-process.mjs';
import {pairContextProcess} from './pair-context-process.mjs';
import {unsplitOctahedronProcess} from './unsplit-octahedron-process.mjs';
import {foldedFibrationProcess} from './fibration-folded-process.mjs';
import {centerInterfaceProcess} from './center-interface-process.mjs';
import {retainedPbProcess} from './retained-pb-process.mjs';
import {procedureState} from './normal-ray-procedure.mjs';
import {pairedRayProcess} from './paired-ray-process.mjs';
import {diamondConstruction} from './diamond-construction.mjs';

export const processes=Object.freeze([
 Object.freeze({id:'ruthenium-98',name:'5-side oct',description:'Native five-edge octahedron: 245 cells. Full 80-fibre P/E fibration with explicit opposite-face N channels, coherence groups and retained boundary-lift seams; Geometry and Lattice remain separate views.'}),
 Object.freeze({id:'sulfur-32',name:'Sulfur-32',description:'Edge-three octahedron with a candidate global periodic fibration: 16 N channels, four wires each, reversible 2×2 P|E ports. All geometric records retained.'}),
 Object.freeze({id:'single-octahedral',name:'Single octahedron — edge 7, no belt',description:'One native P/E-symmetric octahedral sector with ±P/±N/±E boundary ports. No second parent, inherited belt or bridge.'}),
 Object.freeze({id:'native-octahedral-bridge',name:'Octahedral pair — native grown bridge',description:'Common-lattice parents connected by all shortest shared-face paths: 49 added cells, two shared N terminals, no point-only links. Explicit geometric growth rule, not derived transport dynamics.'}),
 Object.freeze({id:'signed-octahedral-belt',name:'Octahedral pair + belt — ±P / ±N / ±E',description:'Two P/E-symmetric native octahedral parents joined by the existing extended belt at opposite signed E ports. Boundary-port labels are distinct from cell roles; no transport law inferred.'}),
 Object.freeze({id:'neutron-belt',name:'Neutron interior — annular belt',description:'Verified six-cone carrier with three opposite-circulation pairs; two cap cones excluded. Separate inspection, no parent-cell assignments.'}),
 Object.freeze({id:'double-esd7',name:'Double ESD7 — opposing P fronts',description:'Original face-glued ESD7 pair, unfolded with full wiring. Start from opposite −P/+P tips; passing-front filling rules will be defined independently.'}),
 Object.freeze({id:'cell-fibration',name:'Cell-level fibration',description:'Whole-cell growth on folded k=7. Central quartets: two N and two non-N; add only N or P. Layer-3 gaps: N. Copy quartets to opposite faces, then colours into paired interior cells.'}),
 Object.freeze({id:'pair-context-7x4',name:'P/E pair — 7×4 contexts',description:'28 positions of a 2×2 bank: seven native endpoint-face contexts, four confirmed in-place flow reversals. N is the mixed interface witness; no new layer filling.'}),
 Object.freeze({id:'unsplit-octahedron',name:'Unsplit octahedron',description:'One whole octahedral cell. Inspect both sides of its eight faces before choosing a subdivision or assigning particle paths.'}),
 Object.freeze({id:'fibration-12x12',name:'12x12 fibration',description:'5134 folded onto 2134: 119 tetrahedra and 56 whole octahedra. Distinct −P/+P flow occurrences and both polarity sheets share one geometry. No internal octahedral cuts or artificial P/E face splits.'}),
 Object.freeze({id:'from-center-cell',name:'From center cell — interface expansion',description:'Actual esd7 cells: central P, P/E/N/N boundary, then two typed arrow cells per branch, joined by complete triangular faces. No reflected or scaled cells. Further layer filling remains open.'}),
 Object.freeze({id:'retained-construction',name:'Process 4 — seed-first assembly',description:'Start from one central seed. Grow the k=7 carrier through complete shared faces, retaining all four branch histories and shared incidences. No completed Pb layout is loaded. Particle bindings remain a separate gate.'}),
 Object.freeze({id:'diamond-construction',name:'Process 3 — diamond rules',description:'Clean reconstruction: geometric center P and three P branches where orientation is unique; the V₁-side neighbor remains unresolved. E is surface-only. Ambiguous centers/branches are reported rather than guessed.'}),
 Object.freeze({id:'edge-ray',name:'Process 1 — edge-ray experiment',description:'Saved experimental construction, including the four-cell lateral split. Not a validated rule set.'}),
 Object.freeze({id:'new-construction',name:'Process 2 — new construction',description:'E at V₁. Cast ray₁₃ to P, ray₃₂ to N, then ray₂₁ back to E. Each ray is k units long.'}),
]);
export function processState(id,k,step,branch=1,options={}){
 if(id==='ruthenium-98')return ruthenium98Process(k,step);
 if(id==='sulfur-32')return sulfur32Process(k,step,{...options,sulfurDirection:branch===3?'E|P':'P|E'});
 if(id==='single-octahedral')return singleOctahedralProcess(k,step,options);
 if(id==='native-octahedral-bridge')return nativeBridgeProcess(k,step,options);
 if(id==='signed-octahedral-belt')return signedOctahedralProcess(k,step,options);
 if(id==='neutron-belt')return neutronBeltProcess(k,0);
 if(id==='double-esd7'){const p=doubleEsd7RuleProcess(k,options.doubleRules??[],options.internalElectronSelf??false,options.seamBelts);if(!options.rimAssembly)return p;const belt=presentCentralBelt(p);return options.parentHalfStepTrim?trimParentHalfStep(belt):belt;}
 if(id==='cell-fibration')return cellFibrationProcess(k,step);
 if(id==='pair-context-7x4')return pairContextProcess(k,step);
 if(id==='unsplit-octahedron')return unsplitOctahedronProcess(k,step);
 if(id==='fibration-12x12')return foldedFibrationProcess(k,step,options);
 if(id==='from-center-cell')return centerInterfaceProcess(k,step);
 if(id==='retained-construction')return retainedPbProcess(k,step);
 if(id==='diamond-construction')return diamondConstruction(k,step);
 if(id==='edge-ray')return procedureState(k,step,branch);
 if(id==='new-construction')return pairedRayProcess(k,step);
 throw Error(`Unknown construction process: ${id}`);
}
