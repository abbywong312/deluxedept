import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題
st.set_page_config(page_title="Augusto Inventory System", layout="wide")

# 包含 React 與 Tailwind 的前端應用程式
react_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { margin: 0; background-color: #f1f5f9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useMemo } = React;

        const Icon = ({ name, size = 20, className = "" }) => {
            const icons = {
                package: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>,
                search: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>,
                logout: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg>,
                history: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/></svg>,
                home: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>,
                plus: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>
            };
            return icons[name] || null;
        };

        const App = () => {
            const [user, setUser] = useState(null);
            const [loginUsername, setLoginUsername] = useState('');
            const [loginPassword, setLoginPassword] = useState('');
            const [loginError, setLoginError] = useState('');
            const [activeTab, setActiveTab] = useState('summary');
            const [searchTerm, setSearchTerm] = useState('');

            const authorizedUsers = [
                { username: 'damith', passwordHash: 'QXVndXN0bzE5MDE=' },
                { username: 'eddie', passwordHash: 'QXVndXN0bzE5MDE=' },
                { username: 'abby', passwordHash: 'QXVndXN0bzE5MDE=' }
            ];

            // 補全所有項目清單
            const [items, setItems] = useState([
                // FG
                { id: 101, name: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', category: 'FG' },
                { id: 102, name: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', category: 'FG' },
                { id: 103, name: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', category: 'FG' },
                { id: 104, name: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', category: 'FG' },
                { id: 105, name: 'Augusto VIP Giftbox w/2 Glasses', category: 'FG' },
                // POSM
                { id: 201, name: 'SDM Asia Green T-shirt (S/M/L/XL)', category: 'POSM' },
                { id: 202, name: 'SDM Asia Black T-shirt (S/M/L/XL)', category: 'POSM' },
                { id: 203, name: 'SDM Asia Green Hoodie (S/M/L/XL)', category: 'POSM' },
                { id: 204, name: 'SDM Asia Grey Hoodie (S/M/L/XL)', category: 'POSM' },
                { id: 205, name: 'SDM Asia Black Cap', category: 'POSM' },
                { id: 206, name: 'SDM Asia Purple Cap', category: 'POSM' },
                { id: 207, name: 'Dali Tech. Black Cigar Cutter', category: 'POSM' },
                { id: 208, name: 'Bingyi Black Shaker 700ml', category: 'POSM' },
                // Accessories
                { id: 301, name: 'Augusto Joven Silver Neck Collar-Small', category: 'Accessories' },
                { id: 302, name: 'Augusto Joven Silver Stopper', category: 'Accessories' },
                { id: 303, name: 'Augusto Joven Silver Triangle', category: 'Accessories' },
                { id: 304, name: 'Augusto Reposado Gold Neck Collar-Small', category: 'Accessories' },
                { id: 305, name: 'Augusto Reposado Gold Stopper', category: 'Accessories' },
                { id: 306, name: 'Augusto Reposado Gold Triangle', category: 'Accessories' }
            ]);

            // 真實數據交易紀錄
            const [transactions, setTransactions] = useState([
                { id: 't1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
                { id: 't2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
                { id: 't3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' }
            ]);

            const stockSummary = useMemo(() => {
                const summary = {};
                items.forEach(item => {
                    summary[item.name] = { total: 0, details: { 'Office': 0, 'Worldex': 0, 'San Tai': 0 }, category: item.category };
                });
                transactions.forEach(tx => {
                    if (summary[tx.itemName]) {
                        summary[tx.itemName].total += tx.amount;
                        summary[tx.itemName].details[tx.location] = (summary[tx.itemName].details[tx.location] || 0) + tx.amount;
                    }
                });
                return summary;
            }, [transactions, items]);

            const [formData, setFormData] = useState({ activity: '', itemName: items[0].name, amount: '', location: 'Office' });

            const handleLogin = (e) => {
                e.preventDefault();
                const found = authorizedUsers.find(u => u.username === loginUsername.toLowerCase() && u.passwordHash === btoa(loginPassword));
                if (found) setUser(found.username); else setLoginError('Invalid credentials');
            };

            const handleAction = (e) => {
                e.preventDefault();
                const qty = parseInt(formData.amount) || 0;
                setTransactions([{ id: Date.now(), date: new Date().toISOString().split('T')[0], activity: formData.activity || (qty > 0 ? "Stock In" : "Stock Out"), itemName: formData.itemName, amount: qty, location: formData.location, user: user }, ...transactions]);
                setActiveTab('summary');
                setFormData({ ...formData, amount: '' });
            };

            if (!user) {
                return (
                    <div className="min-h-screen bg-[#5b58f5] flex items-center justify-center p-4">
                        <div className="bg-white rounded-[32px] shadow-2xl w-full max-w-sm p-10 space-y-8">
                            <div className="text-center">
                                <div className="w-20 h-20 bg-[#eff2fe] rounded-2xl flex items-center justify-center mx-auto text-[#5b58f5] mb-4 shadow-sm">
                                    <Icon name="package" size={40} />
                                </div>
                                <h1 className="text-2xl font-black text-slate-800 tracking-tight uppercase">Augusto Portal</h1>
                            </div>
                            <form onSubmit={handleLogin} className="space-y-4">
                                <input type="text" placeholder="Username" className="w-full p-4 bg-slate-50 border-2 border-slate-100 rounded-2xl font-bold focus:border-[#5b58f5] outline-none transition-all" value={loginUsername} onChange={e => setLoginUsername(e.target.value)} required />
                                <input type="password" placeholder="Password" className="w-full p-4 bg-slate-50 border-2 border-slate-100 rounded-2xl font-bold focus:border-[#5b58f5] outline-none transition-all" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
                                {loginError && <p className="text-rose-500 text-xs font-bold text-center uppercase tracking-wider">{loginError}</p>}
                                <button type="submit" className="w-full bg-[#5b58f5] text-white font-black py-4 rounded-2xl hover:bg-indigo-700 transition-all shadow-lg shadow-indigo-200 uppercase tracking-widest text-sm">Login</button>
                            </form>
                        </div>
                    </div>
                );
            }

            return (
                <div className="min-h-screen bg-[#f8fafc] flex flex-col font-sans">
                    <header className="bg-[#5b58f5] text-white p-5 shadow-lg flex justify-between items-center sticky top-0 z-50">
                        <div className="flex items-center gap-3">
                            <div className="bg-white/20 p-2 rounded-lg"><Icon name="package" size={20} /></div>
                            <h1 className="text-lg font-black tracking-tighter uppercase">Augusto Inventory</h1>
                        </div>
                        <button onClick={() => setUser(null)} className="p-2 bg-white/10 rounded-xl hover:bg-rose-500 transition-all"><Icon name="logout" size={20} /></button>
                    </header>

                    <main className="flex-1 p-4 sm:p-6 w-full max-w-4xl mx-auto pb-32">
                        {activeTab === 'summary' && (
                            <div className="space-y-8">
                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                    <h2 className="text-2xl font-black text-slate-800 tracking-tight">庫存概覽 / STOCK OVERVIEW</h2>
                                    <div className="relative w-full sm:w-72">
                                        <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"><Icon name="search" size={18} /></div>
                                        <input type="text" placeholder="Search items..." className="w-full pl-12 pr-4 py-3.5 bg-white border border-slate-200 rounded-2xl text-sm font-bold shadow-sm outline-none focus:ring-2 focus:ring-[#5b58f5]" onChange={(e) => setSearchTerm(e.target.value)} />
                                    </div>
                                </div>

                                {['FG', 'POSM', 'Accessories'].map(category => {
                                    const filtered = items.filter(i => i.category === category && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
                                    if (filtered.length === 0) return null;

                                    return (
                                        <section key={category} className="bg-white rounded-[32px] p-6 shadow-sm border border-slate-100 overflow-hidden">
                                            <div className="flex items-center justify-between mb-6 pb-2 border-b border-slate-50">
                                                <h3 className="text-xs font-black text-[#5b58f5] uppercase tracking-[0.2em]">{category === 'FG' ? '成品 / Finished Goods' : category === 'POSM' ? '促銷品 / POSM' : '配件 / Accessories'}</h3>
                                                <span className="text-[10px] font-black text-slate-300 uppercase tracking-widest text-right">TOTAL / LOCATION</span>
                                            </div>

                                            <div className="divide-y divide-slate-50">
                                                {filtered.map(item => {
                                                    const data = stockSummary[item.name];
                                                    return (
                                                        <div key={item.id} className="py-6 flex flex-col gap-4">
                                                            <div className="flex justify-between items-start gap-4">
                                                                <span className="text-[14px] font-bold text-slate-700 leading-tight">{item.name}</span>
                                                                <span className={"text-2xl font-black " + (data.total > 0 ? "text-[#5b58f5]" : "text-slate-200")}>{data.total}</span>
                                                            </div>
                                                            <div className="flex flex-wrap gap-2">
                                                                {['Office', 'Worldex', 'San Tai'].map(loc => {
                                                                    const qty = data.details[loc] || 0;
                                                                    return (
                                                                        <div key={loc} className={"px-3 py-1.5 rounded-xl text-[10px] font-black transition-all border " + (qty > 0 ? "bg-indigo-50 border-indigo-100 text-indigo-600 shadow-sm" : "bg-slate-50 border-transparent text-slate-300")}>
                                                                            {loc}: {qty}
                                                                        </div>
                                                                    );
                                                                })}
                                                            </div>
                                                        </div>
                                                    );
                                                })}
                                            </div>
                                        </section>
                                    );
                                })}
                            </div>
                        )}

                        {activeTab === 'add' && (
                            <div className="max-w-xl mx-auto py-4">
                                <form onSubmit={handleAction} className="bg-white p-8 rounded-[32px] shadow-xl border border-slate-50 space-y-8">
                                    <h2 className="text-xl font-black text-slate-800 tracking-tight uppercase border-b pb-4">New Entry / 新增紀錄</h2>
                                    <div className="space-y-4">
                                        <div className="space-y-2">
                                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Select Product</label>
                                            <select className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl text-sm font-bold focus:border-[#5b58f5] outline-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                                                {items.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                                            </select>
                                        </div>
                                        <div className="space-y-2">
                                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Location</label>
                                            <div className="grid grid-cols-3 gap-2">
                                                {['Office', 'Worldex', 'San Tai'].map(l => (
                                                    <button key={l} type="button" onClick={() => setFormData({...formData, location: l})} className={"py-3 rounded-xl text-[10px] font-black border transition-all " + (formData.location === l ? "bg-[#5b58f5] text-white border-[#5b58f5]" : "bg-white text-slate-500 border-slate-200")}>{l}</button>
                                                ))}
                                            </div>
                                        </div>
                                        <div className="space-y-2">
                                            <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Quantity (+ In / - Out)</label>
                                            <input type="number" placeholder="0" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl text-2xl font-black focus:border-[#5b58f5] outline-none" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required />
                                        </div>
                                    </div>
                                    <button type="submit" className="w-full bg-[#5b58f5] text-white font-black py-5 rounded-2xl uppercase tracking-[0.2em] text-xs shadow-lg shadow-indigo-100 hover:scale-[1.02] active:scale-[0.98] transition-all">Confirm Transaction</button>
                                </form>
                            </div>
                        )}
                        
                        {activeTab === 'history' && (
                            <div className="space-y-6">
                                <h2 className="text-2xl font-black text-slate-800 tracking-tight">紀錄 / LOGS</h2>
                                <div className="space-y-3">
                                    {transactions.map(tx => (
                                        <div key={tx.id} className="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 flex items-center justify-between gap-4">
                                            <div className="flex-1">
                                                <div className="text-[10px] font-black text-slate-400 uppercase tracking-widest mb-1">{tx.date} • {tx.location}</div>
                                                <div className="text-sm font-bold text-slate-700 leading-tight">{tx.itemName}</div>
                                                <div className="text-[9px] font-bold text-[#5b58f5] mt-1">{tx.activity} by {tx.user}</div>
                                            </div>
                                            <div className={"text-lg font-black " + (tx.amount > 0 ? "text-emerald-500" : "text-rose-500")}>
                                                {tx.amount > 0 ? `+${tx.amount}` : tx.amount}
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}
                    </main>

                    <nav className="fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-xl border-t border-slate-200 p-4 flex justify-around items-center z-50 pb-8 px-8">
                        <button onClick={() => setActiveTab('summary')} className={"flex flex-col items-center gap-1.5 transition-all " + (activeTab === 'summary' ? "text-[#5b58f5] scale-110" : "text-slate-300")}>
                            <Icon name="home" size={26} /><span className="text-[8px] font-black uppercase tracking-widest">HOME</span>
                        </button>
                        <button onClick={() => setActiveTab('add')} className="relative -mt-12 group">
                            <div className="p-3 rounded-full bg-indigo-50 group-hover:bg-indigo-100 transition-all"><div className="p-4 rounded-full bg-[#5b58f5] text-white shadow-xl shadow-indigo-200 group-hover:rotate-90 transition-all duration-300"><Icon name="plus" size={28} /></div></div>
                        </button>
                        <button onClick={() => setActiveTab('history')} className={"flex flex-col items-center gap-1.5 transition-all " + (activeTab === 'history' ? "text-[#5b58f5] scale-110" : "text-slate-300")}>
                            <Icon name="history" size={26} /><span className="text-[8px] font-black uppercase tracking-widest">LOGS</span>
                        </button>
                    </nav>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

# 在 Streamlit 渲染 HTML
components.html(react_code, height=950, scrolling=True)
