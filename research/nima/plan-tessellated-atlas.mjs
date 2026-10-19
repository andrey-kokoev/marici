import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {dirname} from 'node:path';
import {compileTessellatedAtlas} from './tessellated-atlas.mjs';
import {planExecution,replayExecution,completeAndPlan} from './atlas-execution-plans.mjs';
const usage='node research/nima/plan-tessellated-atlas.mjs (--request request.json | --replay plan.json) [--output result.json]';
try{
 const args=process.argv.slice(2),options={};for(let i=0;i<args.length;i++){if(args[i]==='--help'){console.log(usage);process.exit(0);}if(!['--request','--replay','--output'].includes(args[i])||!args[i+1])throw Error(usage);options[args[i].slice(2)]=args[++i];}
 if(!!options.request===!!options.replay)throw Error(usage);let result;
 if(options.replay){const saved=JSON.parse(readFileSync(options.replay)),plan=saved.plan??saved,c=compileTessellatedAtlas({maxOrigin:plan.maxOrigin,mode:plan.mode});result=replayExecution(c,plan);}
 else{const request=JSON.parse(readFileSync(options.request));if(!Number.isInteger(request.maxOrigin)||request.maxOrigin<0)throw Error('Invalid maxOrigin');const c=compileTessellatedAtlas({maxOrigin:request.maxOrigin,mode:request.mode??'experimental-terminal-PE'});result=request.target?planExecution(c,request.start,request.target,request.execution):completeAndPlan(c,request.start,{closure:request.closure,execution:request.execution});}
 const text=JSON.stringify(result,null,2)+'\n';if(options.output){mkdirSync(dirname(options.output),{recursive:true});writeFileSync(options.output,text);}else process.stdout.write(text);
 if(result.status==='incomplete')process.exitCode=2;else if(!['planned','pass'].includes(result.status))process.exitCode=3;
}catch(e){console.error(e.message);process.exitCode=1;}
