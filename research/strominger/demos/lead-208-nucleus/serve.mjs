// Loopback-only preview. Only these explicitly named assets are exposed.
import {createServer} from 'node:http';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../../../..');
const out=path.join(root,'research/strominger/results/lead-208-nucleus');
const assets=new Map([
 ['/',[path.join(here,'index.html'),'text/html; charset=utf-8']],
 ['/index.html',[path.join(here,'index.html'),'text/html; charset=utf-8']],
 ['/lead-208.png',[path.join(out,'lead-208.png'),'image/png']],
 ['/lead-208-mobile.png',[path.join(out,'lead-208-mobile.png'),'image/png']],
]);
const server=createServer(async(req,res)=>{
 const pathname=new URL(req.url,'http://127.0.0.1').pathname;
 if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end();return;}
 const asset=assets.get(pathname);
 if(!asset){res.writeHead(404,{'Content-Type':'text/plain'});res.end('Not found');return;}
 try{const bytes=await readFile(asset[0]);res.writeHead(200,{'Content-Type':asset[1],'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(req.method==='HEAD'?undefined:bytes);}
 catch{res.writeHead(404);res.end('Not found');}
});
server.listen(0,'127.0.0.1',async()=>{
 const address=server.address(),url=`http://127.0.0.1:${address.port}/`;
 await mkdir(out,{recursive:true});
 await writeFile(path.join(out,'server-info.json'),JSON.stringify({url,image:url+'lead-208.png',host:'127.0.0.1',pid:process.pid,started_at:new Date().toISOString()},null,2)+'\n');
 console.log(JSON.stringify({url,image:url+'lead-208.png',scope:'loopback-only; four explicit assets'}));
});
