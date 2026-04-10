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
        body { margin: 0; background-color: #e5e7eb; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useMemo } = React;

        const Icon = ({ name, size = 20, className = "" }) => {
            const icons = {
                package: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>,
                search: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>,
                logout: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg>,
                history: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/></svg>,
                home: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>,
                plus: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>,
                arrowRight: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
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

            const [items, setItems] = useState([
                { id: 101, name: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', category: 'FG' },
                { id: 102, name: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', category: 'FG' },
                { id: 103, name: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', category: 'FG' },
                { id: 104, name: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', category: 'FG' },
                { id: 105, name: 'Augusto VIP Giftbox w/2 Glasses', category: 'FG' }
            ]);

            // 嚴格根據截圖：Tres Mujeres 總數 1215 (Office 17 + San Tai 1198)
            const [transactions, setTransactions] = useState([
                { id: 't1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
                { id: 't2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
                { id: 't3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' }
            ]);

            const stockSummary = useMemo(() => {
                const summary = {};
                items.forEach(item => {
                    summary[item.name.trim()] = { total: 0, details: { 'Office': 0, 'Worldex': 0, 'San Tai': 0 }, category: item.category };
                });
                transactions.forEach(tx => {
                    const name = tx.itemName.trim();
                    if (summary[name]) {
                        summary[name].total += tx.amount;
                        summary[name].details[tx.location] = (summary[name].details[tx.location] || 0) + tx.amount;
                    }
                });
                return summary;
            }, [transactions, items]);

            const [formMode, setFormMode] = useState('inout'); 
            const [formData, setFormData] = useState({ 
                activity: '', itemName: items[0].name, amount: '', location: 'Office', customLocation: '', fromLocation: 'Worldex', toLocation: 'Office', newCategory: 'FG'
            });

            const handleLogin = (e) => {
                e.preventDefault();
                const found = authorizedUsers.find(u => 
                    u.username.toLowerCase() === loginUsername.trim().toLowerCase() && 
                    u.passwordHash === btoa(loginPassword)
                );
                if (found) { setUser(found.username); setLoginError(''); } else { setLoginError('Invalid username or password'); }
            };

            const handleAction = (e) => {
                e.preventDefault();
                const now = new Date().toISOString().split('T')[0];
                const qty = parseInt(formData.amount) || 0;
                const finalLoc = formData.location === 'Other' ? formData.customLocation.trim() : formData.location;

                if (formMode === 'newitem') {
                    const name = formData.itemName.trim();
                    setItems(prev => [...prev, { id: Date.now(), name, category: formData.newCategory }]);
                    if(qty !== 0) setTransactions(prev => [{ id: Date.now(), date: now, activity: 'Initial Entry', itemName: name, amount: qty, location: finalLoc || 'Office', user: user }, ...prev]);
                } else if (formMode === 'transfer') {
                    setTransactions(prev => [
                        { id: Date.now()+1, date: now, activity: "Transfer to " + formData.toLocation, itemName: formData.itemName, amount: -qty, location: formData.fromLocation, user: user },
                        { id: Date.now()+2, date: now, activity: "Transfer from " + formData.fromLocation, itemName: formData.itemName, amount: qty, location: formData.toLocation, user: user },
                        ...prev
                    ]);
                } else {
                    setTransactions(prev => [{ id: Date.now(), date: now, activity: formData.activity || (qty > 0 ? "Stock In" : "Stock Out"), itemName: formData.itemName, amount: qty, location: finalLoc || 'Office', user: user }, ...prev]);
                }
                setActiveTab('summary');
            };

            if (!user) {
                return (
                    <div className="min-h-screen bg-[#5b58f5] flex items-center justify-center p-4">
                        <div className="bg-white rounded-[24px] shadow-2xl w-full max-w-sm p-8 pb-10 space-y-6">
                            <div className="text-center mt-2 mb-8">
                                <div className="w-16 h-16 bg-[#eff2fe] rounded-[16px] flex items-center justify-center mx-auto text-[#5b58f5] mb-4">
                                    <Icon name="package" size={32} />
                                </div>
                                <h1 className="text-2xl font-black text-slate-800 tracking-tight">Augusto Inventory</h1>
                            </div>
                            <form onSubmit={handleLogin} className="space-y-4">
                                <input 
                                    type="text" 
                                    placeholder="Username" 
                                    className="w-full p-4 bg-white border-2 border-slate-100 rounded-xl text-sm font-bold text-slate-700 placeholder:text-slate-400 focus:border-[#5b58f5] focus:ring-0 outline-none transition-all" 
                                    value={loginUsername} 
                                    onChange={e => setLoginUsername(e.target.value)} 
                                    required 
                                />
                                <input 
                                    type="password" 
                                    placeholder="Password" 
                                    className="w-full p-4 bg-[#f8fafc] border-2 border-transparent rounded-xl text-sm font-bold text-slate-700 placeholder:text-slate-400 focus:bg-white focus:border-[#5b58f5] outline-none transition-all" 
                                    value={loginPassword} 
                                    onChange={e => setLoginPassword(e.target.value)} 
                                    required 
                                />
                                {loginError && <p className="text-rose-500 text-xs font-bold text-center">{loginError}</p>}
                                <div className="pt-2">
                                    <button type="submit" className="w-full bg-[#5b58f5] text-white font-bold py-4 rounded-xl hover:bg-indigo-700 transition-all uppercase tracking-widest text-sm">
                                        LOGIN
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                );
            }

            return (
                <div className="min-h-screen bg-[#e5e7eb] flex flex-col font-sans pb-24">
                    <header className="bg-[#5b58f5] text-white p-5 shadow-sm flex justify-between items-center sticky top-0 z-50">
                        <div className="flex items-center gap-2">
                            <Icon name="package" size={20} />
                            <h1 className="text-lg font-black tracking-tight">Augusto Inventory</h1>
                        </div>
                        <button onClick={() => setUser(null)} className="p-2 bg-white/10 rounded-lg hover:bg-white/20 transition-all"><Icon name="logout" size={18} /></button>
                    </header>

                    <main className="flex-1 p-4 sm:p-6 w-full max-w-4xl mx-auto">
                        {activeTab === 'summary' && (
                            <div className="space-y-6">
                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
                                    <h2 className="text-2xl font-black text-slate-800">庫存概覽 / Stock Overview</h2>
                                    <div className="relative w-full sm:w-64">
                                        <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"><Icon name="search" size={16} /></div>
                                        <input type="text" placeholder="搜尋 / Search..." className="w-full pl-10 pr-4 py-3 bg-white border border-slate-200 rounded-full text-sm font-medium shadow-sm outline-none focus:ring-2 focus:ring-[#5b58f5]" onChange={(e) => setSearchTerm(e.target.value)} />
                                    </div>
                                </div>

                                {['FG'].map(cat => {
                                    const catItems = items.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
                                    return (
                                        <div key={cat} className="bg-[#f3f4f6] rounded-3xl p-4 sm:p-6 shadow-sm mb-6 border border-slate-200">
                                            <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-300 px-2">
                                                <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest">成品 / FINISHED GOODS</span>
                                                <span className="text-[10px] font-black text-slate-400 uppercase tracking-widest text-right">總數及位置 / TOTAL /<br/>LOCATION</span>
                                            </div>
                                            
                                            <div className="flex flex-col">
                                                {catItems.map((item, index) => {
                                                    const data = stockSummary[item.name] || { total: 0, details: {} };
                                                    const isLast = index === catItems.length - 1;
                                                    return (
                                                        <div key={item.id} className={"py-5 px-2 flex flex-col " + (isLast ? "" : "border-b border-slate-300")}>
                                                            <div className="flex justify-between items-start mb-3">
                                                                <span className="text-[15px] font-bold text-slate-700 leading-snug pr-4">{item.name}</span>
                                                                <span className={"font-black text-2xl " + (data.total > 0 ? "text-[#5b58f5]" : "text-slate-300")}>{data.total}</span>
                                                            </div>
                                                            <div className="flex flex-wrap gap-2">
                                                                {['Office', 'Worldex', 'San Tai'].map(loc => {
                                                                    const qty = data.details[loc] || 0;
                                                                    const isActive = qty > 0;
                                                                    return (
                                                                        <div key={loc} className={"px-3 py-1 rounded-full text-[10px] font-bold transition-colors " + (isActive ? "bg-indigo-100 text-indigo-700" : "bg-slate-200 text-slate-400")}>
                                                                            {loc}: {qty}
                                                                        </div>
                                                                    );
                                                                })}
                                                            </div>
                                                        </div>
                                                    );
                                                })}
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        )}

                        {activeTab === 'add' && (
                            <div className="space-y-6 max-w-2xl mx-auto">
                                <form onSubmit={handleAction} className="bg-white p-6 sm:p-8 rounded-3xl shadow-sm border border-slate-100 space-y-6">
                                    <div className="space-y-2">
                                        <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Select Product</label>
                                        <select className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm font-bold focus:border-[#5b58f5] outline-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                                            {items.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                                        </select>
                                    </div>
                                    <div className="space-y-3">
                                        <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Location</label>
                                        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                            {['Office', 'Worldex', 'San Tai'].map(l => (
                                                <button key={l} type="button" onClick={() => setFormData({...formData, location: l})} className={"py-3 rounded-xl text-[10px] font-black border transition-all " + (formData.location === l ? "bg-[#5b58f5] text-white" : "bg-white text-slate-500 border-slate-200")}>{l}</button>
                                            ))}
                                        </div>
                                    </div>
                                    <div className="space-y-2">
                                        <label className="text-[10px] font-black text-slate-400 uppercase tracking-widest">Quantity</label>
                                        <input type="number" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-xl font-black focus:border-[#5b58f5] outline-none" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required />
                                    </div>
                                    <button type="submit" className="w-full bg-[#5b58f5] text-white font-black py-4 rounded-xl uppercase tracking-widest text-xs">Confirm</button>
                                </form>
                            </div>
                        )}
                    </main>

                    <nav className="fixed bottom-0 left-0 right-0 bg-[#e5e7eb]/90 backdrop-blur-md border-t border-slate-300 p-4 flex justify-around items-center z-50 pb-6">
                        <button onClick={() => setActiveTab('summary')} className={"flex flex-col items-center gap-1 " + (activeTab === 'summary' ? "text-[#5b58f5]" : "text-slate-400")}>
                            <Icon name="home" size={24} /><span className="text-[9px] font-black uppercase">概覽 / HOME</span>
                        </button>
                        <button onClick={() => setActiveTab('add')} className="relative -mt-10">
                            <div className="p-3 rounded-full bg-[#c7d2fe]/50"><div className="p-3 rounded-full bg-[#5b58f5] text-white"><Icon name="plus" size={24} /></div></div>
                        </button>
                        <button onClick={() => setActiveTab('history')} className={"flex flex-col items-center gap-1 " + (activeTab === 'history' ? "text-[#5b58f5]" : "text-slate-400")}>
                            <Icon name="history" size={24} /><span className="text-[9px] font-black uppercase">歷史 / LOGS</span>
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
