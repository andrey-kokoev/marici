import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {studyNeutronCoherence} from '../examples/isotope-wiring/core/neutron-space-coherence.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true})),result=studyNeutronCoherence(model);
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,counts:result.comparison.counts,actual:result.actual.status,flatControl:result.flatControl.status,twistedControl:result.twistedControl.status,failedLocalComparisons:result.twistedControl.walks.filter(w=>w.id.startsWith('local-comparison:')&&w.status==='refuted').map(w=>w.id),criterion:result.comparison.criterion,conclusion:result.conclusion},null,2));
