import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {solveTetrahedralDepths} from '../examples/isotope-wiring/core/tetrahedral-depth-constraints.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true})),full=buildStackedFullInterface(model);
let fixedProjectionControl;try{solveTetrahedralDepths(full);fixedProjectionControl={status:'realizable'};}catch(e){if(!e.message.startsWith('Fixed projection prevents contact'))throw e;fixedProjectionControl={status:'refuted',reason:e.message};}
const result={...solveTetrahedralDepths(full,{allowContactTranslation:true}),fixedProjectionControl};
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,fixedProjectionControl,counts:result.counts,relations:result.relations,allPositiveControl:result.allPositiveControl,firstSolution:result.solutions[0]&&{signs:result.solutions[0].signs,centerDepths:result.solutions[0].centerDepths,projectedTranslations:result.solutions[0].projectedTranslations,components:result.solutions[0].components},limits:result.limits},null,2));
