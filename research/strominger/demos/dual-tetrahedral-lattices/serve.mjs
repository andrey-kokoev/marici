// Loopback preview exposes only this experiment's named assets.
import {createServer} from 'node:http';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const here=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(here,'../../../..'),out=path.join(root,'research/strominger/results/dual-tetrahedral-lattices');
const assets=new Map([['/',[path.join(here,'index.html'),'text/html; charset=utf-8']],['/index.html',[path.join(here,'index.html'),'text/html; charset=utf-8']],['/model.mjs',[path.join(here,'model.mjs'),'text/javascript; charset=utf-8']],['/app.mjs',[path.join(here,'app.mjs'),'text/javascript; charset=utf-8']],['/dual-tetrahedral.png',[path.join(out,'dual-tetrahedral.png'),'image/png']]]);
const server=createServer(async(req,res)=>{const asset=assets.get(new URL(req.url,'http://127.0.0.1').pathname);if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end();return;}if(!asset){res.writeHead(404);res.end();return;}try{const data=await readFile(asset[0]);res.writeHead(200,{'Content-Type':asset[1],'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(req.method==='HEAD'?undefined:data);}catch{res.writeHead(404);res.end();}});
server.listen(0,'127.0.0.1',async()=>{const url=`http://127.0.0.1:${server.address().port}/`;await mkdir(out,{recursive:true});await writeFile(path.join(out,'server-info.json'),JSON.stringify({url,image:url+'dual-tetrahedral.png',pid:process.pid,started_at:new Date().toISOString()},null,2)+'\n');console.log(JSON.stringify({url,image:url+'dual-tetrahedral.png',scope:'loopback-only named experiment assets'}));});
