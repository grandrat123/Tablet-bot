<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Tablet Bot - Health Chain</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <!-- Firebase SDKs -->
    <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-bom.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore-bom.js"></script>
    <style>
        body { background-color: #0b0e11; color: white; -webkit-tap-highlight-color: transparent; }
        .mining-animate { animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .5; } }
    </style>
</head>
<body class="font-sans antialiased overflow-hidden">
    <div id="app" class="flex flex-col min-h-screen">
        <!-- Header -->
        <div class="p-4 bg-[#151a21] border-b border-slate-800 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <div class="w-10 h-10 bg-green-500 rounded-xl flex items-center justify-center">⚡</div>
                <div>
                    <h1 class="text-sm font-bold">Tablet Bot</h1>
                    <span class="text-[10px] text-green-500 font-bold">LIVE</span>
                </div>
            </div>
            <div class="text-right">
                <p id="balance" class="text-lg font-mono font-bold">0.0000</p>
                <p class="text-[10px] text-slate-500 font-bold">HC BALANCE</p>
            </div>
        </div>

        <!-- Main Mining Area -->
        <div class="flex-1 flex flex-col items-center justify-center p-6">
            <div class="relative w-64 h-64 flex items-center justify-center mb-10">
                <div id="progress-circle" class="absolute inset-0 rounded-full border-[10px] border-slate-800"></div>
                <button id="mine-btn" class="z-10 w-48 h-48 bg-green-600 rounded-full shadow-2xl flex flex-col items-center justify-center active:scale-95 transition-transform border-4 border-green-400">
                    <span class="text-4xl mb-2">⛏️</span>
                    <span class="font-bold">START MINING</span>
                </button>
            </div>

            <div class="w-full grid grid-cols-2 gap-4">
                <div class="bg-[#151a21] p-4 rounded-2xl border border-slate-800 text-center">
                    <p class="text-[10px] text-slate-500 mb-1">DAILY RATE</p>
                    <p class="font-bold">0.50 HC</p>
                </div>
                <div class="bg-[#151a21] p-4 rounded-2xl border border-slate-800 text-center">
                    <p class="text-[10px] text-slate-500 mb-1">STATUS</p>
                    <p id="status-text" class="font-bold text-yellow-500 uppercase">IDLE</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Simple mock logic for demonstration. 
        // Real logic would connect to Firebase as shown in previous responses.
        let balance = 0;
        let isMining = false;
        const btn = document.getElementById('mine-btn');
        const balEl = document.getElementById('balance');
        const statusEl = document.getElementById('status-text');

        btn.onclick = () => {
            if (isMining) return;
            isMining = true;
            statusEl.innerText = "MINING...";
            statusEl.classList.replace('text-yellow-500', 'text-green-500');
            btn.classList.add('mining-animate');
            btn.innerHTML = <span class="text-4xl mb-2">⚡</span><span class="font-bold">MINING...</span>;
            
            setInterval(() => {
                balance += 0.00001;
                balEl.innerText = balance.toFixed(5);
            }, 1000);
        };

// Initialize Telegram
        if (window.Telegram && window.Telegram.WebApp) {
            window.Telegram.WebApp.ready();
            window.Telegram.WebApp.expand();
        }
    </script>
</body>
</html>
