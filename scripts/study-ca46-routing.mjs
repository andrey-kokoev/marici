import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {bindCa46ConnectedPaths} from '../examples/isotope-wiring/core/connected-path-trial.mjs';
import {buildDeterministicRouting} from '../examples/isotope-wiring/core/deterministic-routing.mjs';
const context=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],context);
const d=JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().Ca46)),svg=context.IsotopeWiring.renderSVG(d,{interactive:true}),b=bindCa46ConnectedPaths(d,svg),r=buildDeterministicRouting(b);
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(r,null,2)+'\n');
console.log(JSON.stringify({definitionId:r.definitionId,status:r.status,rule:r.rule,counts:r.counts,checks:r.checks,PEroundtripLengths:[...new Set(r.PEroutes.map(p=>p.fullStateReturn))].sort((a,b)=>a-b),firstPEVertexReturnLengths:[...new Set(r.PEroutes.map(p=>p.firstVertexReturn))].sort((a,b)=>a-b),example:r.PEroutes[0],frameReturn:r.frameReturn,limitation:r.limitation},null,2));
