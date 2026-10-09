const http = require('http');
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '../docs');
const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'application/javascript; charset=utf-8','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.webp':'image/webp','.ttf':'font/ttf','.txt':'text/plain; charset=utf-8','.xml':'application/xml'};
http.createServer((req,res) => {
  let pathname;
  try {pathname = decodeURIComponent(new URL(req.url,'http://localhost').pathname);} catch {res.writeHead(400);return res.end();}
  let file = path.resolve(root, '.'+pathname);
  if (!file.startsWith(root+path.sep) && file !== root) {res.writeHead(403);return res.end();}
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file,'index.html');
  fs.readFile(file,(err,data) => {if (err) {res.writeHead(404);return res.end('Not found');} res.writeHead(200,{'Content-Type':types[path.extname(file)]||'application/octet-stream'});res.end(data);});
}).listen(4173,'127.0.0.1',()=>console.log('Local: http://127.0.0.1:4173'));
