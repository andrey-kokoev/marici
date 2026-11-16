import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {studyDiagramFrameReturn} from '../examples/isotope-wiring/core/diagram-path-trial.mjs';
const html=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8'),context=vm.createContext({});
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
const definition=JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().Ca46)),svg=context.IsotopeWiring.renderSVG(definition,{interactive:true,standalone:false});
const result=studyDiagramFrameReturn(definition,svg);
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({definitionId:definition.id,counts:result.binding.counts,unassigned:result.unassigned.status,planarControl:result.planarControl.status,twistedControl:result.twistedControl.status,status:result.status,residuals:result.binding.residuals,conclusion:result.conclusion},null,2));
// Successful experiment execution is not verification of Ca46.
if(result.unassigned.status!=='unknown'||result.planarControl.status!=='verified'||result.twistedControl.status!=='refuted')process.exitCode=1;
