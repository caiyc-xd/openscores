// Service Worker：缓存站点静态资源（alphaTab 引擎、Bravura 字体、音色库 FluidR3_GM.sf3、样式等），
// 使「打开本地谱」在首次在线访问后，断网也能渲染并播放。
// 仅作渐进增强：注册/缓存失败都不影响基本功能。
const CACHE = 'openscores-static-v3';

// 预缓存清单（含 14MB 音色库）：首次联网访问页面即后台下载并缓存，
// 之后即使断网也能播放；无需先打开乐谱文件。
const PRECACHE = [
  './',
  './index.html',
  './player.html',
  './library.html',
  './my-score.html',
  './style.css',
  './player/alphaTab.min.js',
  './player/navfix.js',
  // 14MB 音色库不在此预缓存：改由页面用 CDN 优先拉取并写入同一缓存，规避 GitHub Pages 慢带宽
  './licenses/Bravura-OFL-1.1.txt',
  './licenses/FluidR3Mono_GM-MIT.txt',
  './licenses/alphaTab-MPL-2.0.txt'
];

self.addEventListener('install', () => { self.skipWaiting(); });

self.addEventListener('activate', (event) => {
  // 清理旧缓存并接管页面（快速完成，不阻塞）
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
  // 后台预缓存：逐项缓存，避免 addAll 因单个资源失败而整批不缓存
  caches.open(CACHE).then(c => Promise.allSettled(PRECACHE.map(u => c.add(u)))).catch(() => {});
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // 仅处理同站资源

  if (req.mode === 'navigate') {
    // 页面：网络优先，离线回退到缓存（保证线上更新可见，且断网仍能打开）
    event.respondWith(
      fetch(req).then((r) => {
        const c = r.clone();
        caches.open(CACHE).then(ca => ca.put(req, c)).catch(() => {});
        return r;
      }).catch(() => caches.match(req).then(m => m || caches.match('./index.html')))
    );
    return;
  }

  // 静态资源：缓存优先（含 14MB 音色库、字体、脚本），离线可用
  event.respondWith(
    caches.match(req).then((m) => {
      if (m) return m;
      return fetch(req).then((r) => {
        if (r && (r.ok || r.type === 'opaque')) {
          const c = r.clone();
          caches.open(CACHE).then(ca => ca.put(req, c)).catch(() => {});
        }
        return r;
      }).catch(() => m);
    })
  );
});
