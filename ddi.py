import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題，並使用寬版面以適應 Desktop
st.set_page_config(page_title="Augusto Inventory System", layout="wide")

# React + Tailwind 前端代碼
react_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { margin: 0; background-color: #f1f5f9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        /* 自定義滾動條以美化 Desktop 顯示 */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useMemo } = React;

        // 圖標庫
        const Icon = ({ name, size = 20, className = "" }) => {
            const icons = {
                package: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>,
                search: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>,
                logout: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg>,
                history: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/></svg>,
                home: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>,
                plus: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>,
                arrowRight: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>,
                user: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            };
            return icons[name] || null;
        };

        const App = () => {
            const [user, setUser] = useState(null);
            const [loginEmail, setLoginEmail] = useState('');
            const [loginPassword, setLoginPassword] = useState('');
            const [loginError, setLoginError] = useState('');
            const [activeTab, setActiveTab] = useState('summary');
            const [searchTerm, setSearchTerm] = useState('');

            const authorizedUsers = [
                { email: 'damith@deluxedept.com', password: 'Augusto1901' },
                { email: 'eddie@deluxedept.com', password: 'Augusto1901' },
                { email: 'abby@deluxedept.com', password: 'Augusto1901' }
            ];

            // 1. 所有貨品清單
            const [items, setItems] = useState([
                { id: 101, name: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', category: 'FG' },
                { id: 102, name: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', category: 'FG' },
                { id: 103, name: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', category: 'FG' },
                { id: 104, name: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', category: 'FG' },
                { id: 105, name: 'Augusto VIP Giftbox w/2 Glasses', category: 'FG' },
                { id: 106, name: 'Augusto Reposado Giftbox w/2 Glasses', category: 'FG' },
                { id: 201, name: 'Augusto Tequila Shaker (Black)', category: 'POSM' },
                { id: 202, name: 'Augusto Tequila Shaker (Copper)', category: 'POSM' },
                { id: 203, name: 'Dali Technology Black Cigar Cutter', category: 'POSM' },
                { id: 204, name: 'Dali Technology Copper Cigar Cutter', category: 'POSM' },
                { id: 205, name: 'SDM Asia Black Cap', category: 'POSM' },
                { id: 206, name: 'Small Pouch', category: 'POSM' },
                { id: 207, name: 'SDM Asia Green T-shirt (S/M/L/XL)', category: 'POSM' },
                { id: 208, name: 'SDM Asia Black T-shirt (S/M/L/XL)', category: 'POSM' },
                { id: 209, name: 'SDM Asia Green Hoodie (S/M/L/XL)', category: 'POSM' },
                { id: 210, name: 'SDM Asia Grey Hoodie (S/M/L/XL)', category: 'POSM' },
                { id: 211, name: 'Augusto Crystal Cabalito', category: 'POSM' },
                { id: 301, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
                { id: 302, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
                { id: 303, name: 'Augusto Tequila Joven - Silver Stopper', category: 'Accessories' },
                { id: 304, name: 'Augusto Tequila Joven - Silver Triangle', category: 'Accessories' },
                { id: 305, name: 'Augusto Neck Collar (Gold/Silver)', category: 'Accessories' }
            ]);

            // 2. 初始庫存紀錄 (保留精確數值)
            const [transactions, setTransactions] = useState([
                { id: 't1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
                { id: 't2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 156, location: 'Worldex', user: 'System' },
                { id: 't3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' },
                { id: 't4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 13, location: 'Office', user: 'System' },
                { id: 't5', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 36, location: 'Worldex', user: 'System' },
                { id: 't6', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 491, location: 'San Tai', user: 'System' },
                { id: 't7', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 4, location: 'Office', user: 'System' },
                { id: 't8', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
                { id: 't9', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 2, location: 'Office', user: 'System' },
                { id: 't10', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 54, location: 'Worldex', user: 'System' },
                { id: 't11', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto VIP Giftbox w/2 Glasses', amount: 294, location: 'Worldex', user: 'System' },
                { id: 't12', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Reposado Giftbox w/2 Glasses', amount: 162, location: 'Worldex', user: 'System' },
                { id: 't13', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 23, location: 'Office', user: 'System' },
                { id: 't14', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 141, location: 'Worldex', user: 'System' },
                { id: 't15', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 21, location: 'Office', user: 'System' },
                { id: 't16', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 117, location: 'Worldex', user: 'System' },
                { id: 't17', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Black Cigar Cutter', amount: 98, location: 'Office', user: 'System' },
                { id: 't18', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Copper Cigar Cutter', amount: 102, location: 'Office', user: 'System' },
                { id: 't19', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Zhongshan Ho Crafts Gold Pin', amount: 8, location: 'Office', user: 'System' },
                { id: 't20', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Zhongshan Ho Crafts Silver Pin', amount: 182, location: 'Office', user: 'System' },
                { id: 't21', date: '2026-04-09', activity: 'Initial Balance', itemName: 'SDM Asia Black Cap', amount: 29, location: 'Office', user: 'System' },
                { id: 't22', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Small Pouch', amount: 797, location: 'Office', user: 'System' },
                { id: 't28', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Crystal Cabalito', amount: 3, location: 'Office', user: 'System' },
                { id: 't30', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Stopper', amount: 1320, location: 'Worldex', user: 'System' },
            ]);

            // 3. 庫存計算
            const stockSummary = useMemo(() => {
                const summary = {};
                items.forEach(item => {
                    summary[item.name.trim()] = { total: 0, details: {}, category: item.category };
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

            // 4. 表單狀態 (包含恢復的 customLocation 和 formMode)
            const [formMode, setFormMode] = useState('inout'); // 'inout', 'transfer', 'newitem'
            const [formData, setFormData] = useState({ 
                activity: '', 
                itemName: items[0].name, 
                amount: '', 
                location: 'Office', 
                customLocation: '', 
                fromLocation: 'Worldex', 
                toLocation: 'Office', 
                newCategory: 'FG'
            });

            const handleLogin = (e) => {
                e.preventDefault();
                const found = authorizedUsers.find(u => u.email === loginEmail && u.password === loginPassword);
                if (found) { setUser(found.email); setLoginError(''); } 
                else { setLoginError('Invalid email or password'); }
            };

            // 5. 處理表單提交 (核心恢復：支援新增貨品與自訂地點)
            const handleAction = (e) => {
                e.preventDefault();
                const now = new Date().toISOString().split('T')[0];
                const qty = parseInt(formData.amount) || 0;
                
                // 判斷最終地點：如果是 Other，則使用 customLocation
                const finalLoc = formData.location === 'Other' ? formData.customLocation.trim() : formData.location;

                if (formMode === 'newitem') {
                    const name = formData.itemName.trim();
                    if(!name) return;
                    
                    // 避免重複新增
                    if(items.some(i => i.name.toLowerCase() === name.toLowerCase())) {
                        alert("Item already exists!");
                        return;
                    }

                    // 新增至清單
                    setItems(prev => [...prev, { id: Date.now(), name, category: formData.newCategory }]);
                    
                    // 如果有填數量，則新增初始紀錄
                    if(qty !== 0) {
                        setTransactions(prev => [{ 
                            id: Date.now(), date: now, activity: 'Initial Entry', itemName: name, amount: qty, location: finalLoc || 'Office', user: user 
                        }, ...prev]);
                    }
                } else if (formMode === 'transfer') {
                    if(qty <= 0) { alert("Quantity must be greater than 0"); return; }
                    if(formData.fromLocation === formData.toLocation) { alert("Source and Destination cannot be the same"); return; }
                    
                    setTransactions(prev => [
                        { id: Date.now()+1, date: now, activity: "Transfer to " + formData.toLocation, itemName: formData.itemName, amount: -qty, location: formData.fromLocation, user: user },
                        { id: Date.now()+2, date: now, activity: "Transfer from " + formData.fromLocation, itemName: formData.itemName, amount: qty, location: formData.toLocation, user: user },
                        ...prev
                    ]);
                } else {
                    // 一般入庫/出庫
                    setTransactions(prev => [{ 
                        id: Date.now(), date: now, activity: formData.activity || (qty > 0 ? "Stock In" : "Stock Out"), itemName: formData.itemName, amount: qty, location: finalLoc || 'Office', user: user 
                    }, ...prev]);
                }
                
                // 重置表單
                setFormData({ ...formData, amount: '', activity: '', customLocation: '', itemName: formMode === 'newitem' ? items[0].name : formData.itemName });
                setActiveTab('summary');
            };

            if (!user) {
                return (
                    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-4 sm:p-6 font-sans">
                        <div className="bg-white rounded-[2rem] shadow-2xl w-full max-w-md p-8 sm:p-10 space-y-8">
                            <div className="text-center">
                                <div className="w-20 h-20 bg-indigo-50 rounded-[1.5rem] flex items-center justify-center mx-auto text-indigo-600 mb-6 shadow-sm"><Icon name="package" size={40} /></div>
                                <h1 className="text-3xl font-black text-slate-800 tracking-tight">Augusto</h1>
                                <p className="text-slate-400 text-sm font-bold mt-2 uppercase tracking-widest">Inventory System</p>
                            </div>
                            <form onSubmit={handleLogin} className="space-y-4">
                                <div className="space-y-1">
                                    <label className="text-[10px] font-bold text-slate-400 uppercase ml-2">Email Address</label>
                                    <input type="email" placeholder="Email" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl text-sm focus:ring-2 focus:ring-indigo-500 outline-none transition-all" value={loginEmail} onChange={e => setLoginEmail(e.target.value)} required />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-[10px] font-bold text-slate-400 uppercase ml-2">Password</label>
                                    <input type="password" placeholder="Password" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl text-sm focus:ring-2 focus:ring-indigo-500 outline-none transition-all" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
                                </div>
                                {loginError && <p className="text-rose-500 text-xs font-bold text-center bg-rose-50 p-3 rounded-xl border border-rose-100">{loginError}</p>}
                                <button type="submit" className="w-full bg-indigo-600 text-white font-black py-4 rounded-2xl shadow-lg hover:bg-indigo-700 transition-all mt-6 uppercase tracking-widest text-sm">Login</button>
                            </form>
                        </div>
                    </div>
                );
            }

            return (
                <div className="min-h-screen bg-slate-50 flex flex-col font-sans pb-24 md:pb-0">
                    {/* Header: Adaptable for Desktop & Mobile */}
                    <header className="bg-indigo-700 text-white p-4 sm:p-6 shadow-lg flex justify-between items-center sticky top-0 z-50">
                        <div className="flex items-center gap-3">
                            <div className="bg-white/20 p-2 rounded-xl hidden sm:block"><Icon name="package" size={24} /></div>
                            <h1 className="text-lg sm:text-2xl font-black tracking-tight">Augusto Inventory</h1>
                        </div>
                        <div className="flex items-center gap-4">
                            <div className="text-right hidden sm:block">
                                <div className="text-[10px] text-indigo-200 font-bold uppercase tracking-wider">Logged in as</div>
                                <div className="text-sm font-black">{user.split('@')[0].toUpperCase()}</div>
                            </div>
                            <button onClick={() => setUser(null)} className="p-2 sm:p-3 bg-white/10 rounded-xl hover:bg-white/20 transition-all"><Icon name="logout" size={20} /></button>
                        </div>
                    </header>

                    <div className="flex-1 flex flex-col md:flex-row max-w-7xl mx-auto w-full">
                        {/* Sidebar Desktop Navigation */}
                        <aside className="hidden md:flex flex-col w-64 p-6 gap-2 border-r border-slate-200 bg-white min-h-[calc(100vh-80px)]">
                            <button onClick={() => setActiveTab('summary')} className={"flex items-center gap-3 p-4 rounded-2xl font-black transition-all " + (activeTab === 'summary' ? "bg-indigo-50 text-indigo-600" : "text-slate-500 hover:bg-slate-50")}>
                                <Icon name="home" /> <span>Overview</span>
                            </button>
                            <button onClick={() => setActiveTab('add')} className={"flex items-center gap-3 p-4 rounded-2xl font-black transition-all " + (activeTab === 'add' ? "bg-indigo-600 text-white shadow-lg shadow-indigo-200" : "text-slate-500 hover:bg-slate-50")}>
                                <Icon name="plus" /> <span>Manage Stock</span>
                            </button>
                            <button onClick={() => setActiveTab('history')} className={"flex items-center gap-3 p-4 rounded-2xl font-black transition-all " + (activeTab === 'history' ? "bg-indigo-50 text-indigo-600" : "text-slate-500 hover:bg-slate-50")}>
                                <Icon name="history" /> <span>Activity Logs</span>
                            </button>
                        </aside>

                        {/* Main Content Area */}
                        <main className="flex-1 p-4 sm:p-8 w-full overflow-y-auto">
                            {activeTab === 'summary' && (
                                <div className="space-y-6 animate-in fade-in duration-300">
                                    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                        <h2 className="text-2xl sm:text-3xl font-black text-slate-800">Stock Overview</h2>
                                        <div className="relative w-full sm:w-72">
                                            <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"><Icon name="search" size={18} /></div>
                                            <input type="text" placeholder="Search Item Name..." className="w-full pl-12 pr-6 py-3 sm:py-4 bg-white border border-slate-200 rounded-full text-sm font-medium shadow-sm outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all" onChange={(e) => setSearchTerm(e.target.value)} />
                                        </div>
                                    </div>

                                    {['FG', 'POSM', 'Accessories'].map(cat => {
                                        const catItems = items.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
                                        if (catItems.length === 0) return null;
                                        return (
                                            <div key={cat} className="space-y-4">
                                                <div className="flex items-center gap-4 py-2">
                                                    <h3 className="text-xs font-black text-slate-400 uppercase tracking-widest">{cat === 'FG' ? 'Finished Goods' : cat === 'POSM' ? 'Materials' : 'Accessories'}</h3>
                                                    <div className="h-px bg-slate-200 flex-1"></div>
                                                </div>
                                                
                                                {/* 網格系統：桌面端為多欄，手機端單欄 */}
                                                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 sm:gap-6">
                                                    {catItems.map(item => {
                                                        const data = stockSummary[item.name] || { total: 0, details: {} };
                                                        return (
                                                            <div key={item.id} className="bg-white p-5 sm:p-6 rounded-3xl shadow-sm border border-slate-100 hover:shadow-md transition-shadow flex flex-col h-full">
                                                                <div className="flex justify-between items-start mb-4 gap-4">
                                                                    <span className="text-[15px] font-bold text-slate-700 leading-snug">{item.name}</span>
                                                                    <span className={"font-mono font-black text-2xl " + (data.total > 0 ? "text-indigo-600" : "text-slate-300")}>{data.total}</span>
                                                                </div>
                                                                
                                                                <div className="mt-auto pt-4 border-t border-slate-50 flex flex-wrap gap-2">
                                                                    {Object.entries(data.details).map(([loc, qty]) => (
                                                                        <div key={loc} className={"px-3 py-1.5 rounded-xl text-[11px] font-bold border transition-colors " + (qty !== 0 ? "bg-indigo-50 border-indigo-100 text-indigo-700" : "bg-slate-50 border-slate-100 text-slate-400")}>
                                                                            {loc}: {qty}
                                                                        </div>
                                                                    ))}
                                                                    {Object.keys(data.details).length === 0 && <span className="text-[11px] font-bold text-slate-400 px-2 py-1 bg-slate-50 rounded-xl">No record</span>}
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
                                <div className="space-y-6 max-w-3xl mx-auto">
                                    <div className="flex bg-white p-1.5 rounded-2xl shadow-sm border border-slate-200">
                                        {['inout', 'transfer', 'newitem'].map(m => (
                                            <button key={m} onClick={() => setFormMode(m)} className={"flex-1 py-3 sm:py-4 rounded-[1rem] text-[11px] sm:text-xs font-black uppercase tracking-wider transition-all " + (formMode === m ? "bg-indigo-600 text-white shadow-md" : "text-slate-500 hover:bg-slate-50")}>
                                                {m === 'inout' ? 'Stock In/Out' : m === 'transfer' ? 'Transfer' : 'New Item'}
                                            </button>
                                        ))}
                                    </div>

                                    <form onSubmit={handleAction} className="bg-white p-6 sm:p-10 rounded-3xl shadow-xl border border-slate-100 space-y-6 sm:space-y-8">
                                        {/* 模塊：貨品選擇與新增 */}
                                        <div className="space-y-4">
                                            {formMode === 'newitem' ? (
                                                <div className="grid grid-cols-1 gap-4">
                                                    <div className="space-y-2">
                                                        <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest">New Item Name</label>
                                                        <input type="text" className="w-full p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-2xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none transition-all" placeholder="Enter Full Name..." value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})} required />
                                                    </div>
                                                    <div className="space-y-2">
                                                        <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest">Category</label>
                                                        <div className="grid grid-cols-3 gap-2 sm:gap-4">
                                                            {['FG', 'POSM', 'Accessories'].map(c => (
                                                                <button key={c} type="button" onClick={() => setFormData({...formData, newCategory: c})} className={"py-3 sm:py-4 rounded-xl text-xs font-black border transition-all " + (formData.newCategory === c ? "bg-indigo-50 border-indigo-200 text-indigo-700 shadow-sm" : "bg-white border-slate-200 text-slate-500 hover:border-indigo-300")}>{c}</button>
                                                            ))}
                                                        </div>
                                                    </div>
                                                </div>
                                            ) : (
                                                <div className="space-y-2">
                                                    <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest">Select Product</label>
                                                    <select className="w-full p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-2xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                                                        {items.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                                                    </select>
                                                </div>
                                            )}
                                        </div>

                                        {/* 模塊：地點選擇 */}
                                        <div className="space-y-4 pt-4 border-t border-slate-100">
                                            {formMode === 'transfer' ? (
                                                <div className="flex flex-col sm:flex-row items-center gap-4 bg-slate-50 p-5 rounded-2xl border border-slate-200">
                                                    <div className="w-full flex-1">
                                                        <label className="text-[10px] font-black text-slate-400 uppercase mb-2 block">From</label>
                                                        <select className="w-full p-3 bg-white border border-slate-200 rounded-xl text-sm font-bold outline-none" value={formData.fromLocation} onChange={e => setFormData({...formData, fromLocation: e.target.value})}>
                                                            {['Office', 'Worldex', 'San Tai', 'Other'].map(l => <option key={l} value={l}>{l}</option>)}
                                                        </select>
                                                    </div>
                                                    <div className="w-10 h-10 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 sm:mt-6 shrink-0 rotate-90 sm:rotate-0"><Icon name="arrowRight" size={18} /></div>
                                                    <div className="w-full flex-1">
                                                        <label className="text-[10px] font-black text-slate-400 uppercase mb-2 block">To</label>
                                                        <select className="w-full p-3 bg-white border border-slate-200 rounded-xl text-sm font-bold outline-none" value={formData.toLocation} onChange={e => setFormData({...formData, toLocation: e.target.value})}>
                                                            {['Office', 'Worldex', 'San Tai', 'Other'].map(l => <option key={l} value={l}>{l}</option>)}
                                                        </select>
                                                    </div>
                                                </div>
                                            ) : (
                                                <div className="space-y-3">
                                                    <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest">Location</label>
                                                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-4">
                                                        {['Office', 'Worldex', 'San Tai', 'Other'].map(l => (
                                                            <button key={l} type="button" onClick={() => setFormData({...formData, location: l})} className={"py-3 sm:py-4 rounded-xl text-xs font-black border transition-all " + (formData.location === l ? "bg-indigo-600 text-white shadow-md border-indigo-600" : "bg-white text-slate-500 border-slate-200 hover:border-indigo-300")}>{l}</button>
                                                        ))}
                                                    </div>
                                                    {/* Other 自訂地點輸入框 */}
                                                    {formData.location === 'Other' && (
                                                        <input type="text" className="w-full p-4 sm:p-5 mt-2 bg-indigo-50 border border-indigo-200 rounded-2xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none placeholder:text-indigo-300 text-indigo-900 transition-all animate-in slide-in-from-top-2" placeholder="Enter custom location name..." value={formData.customLocation} onChange={e => setFormData({...formData, customLocation: e.target.value})} required />
                                                    )}
                                                </div>
                                            )}
                                        </div>

                                        {/* 模塊：數量與備註 */}
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 pt-4 border-t border-slate-100">
                                            <div className="space-y-2">
                                                <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest">Quantity</label>
                                                <input type="number" className="w-full p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-2xl text-2xl font-black font-mono focus:ring-2 focus:ring-indigo-500 outline-none transition-all" placeholder="0" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required={formMode !== 'newitem'} />
                                            </div>
                                            <div className="space-y-2">
                                                <label className="text-[11px] font-black text-slate-400 uppercase tracking-widest">Remarks</label>
                                                <input type="text" className="w-full p-4 sm:p-5 bg-slate-50 border border-slate-200 rounded-2xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none transition-all placeholder:font-medium" placeholder="Optional notes..." value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                                            </div>
                                        </div>

                                        <button type="submit" className="w-full bg-indigo-600 text-white font-black py-5 sm:py-6 rounded-2xl shadow-lg hover:bg-indigo-700 active:scale-[0.98] transition-all uppercase tracking-widest text-sm">
                                            {formMode === 'newitem' ? 'Create Item & Update Stock' : 'Confirm Transaction'}
                                        </button>
                                    </form>
                                </div>
                            )}

                            {activeTab === 'history' && (
                                <div className="space-y-6 animate-in fade-in duration-300">
                                    <h2 className="text-2xl sm:text-3xl font-black text-slate-800">History Logs</h2>
                                    <div className="grid gap-3 sm:gap-4">
                                        {transactions.slice(0, 50).map(tx => (
                                            <div key={tx.id} className="bg-white p-4 sm:p-6 rounded-3xl shadow-sm border border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4 group hover:border-indigo-100 transition-colors">
                                                <div className="flex-1 min-w-0">
                                                    <div className="flex items-center gap-3 mb-2">
                                                        <span className="px-3 py-1 rounded-xl text-[10px] font-black bg-indigo-50 text-indigo-700 uppercase tracking-wider">{tx.location}</span>
                                                        <span className="text-[11px] text-slate-400 font-bold">{tx.date}</span>
                                                    </div>
                                                    <div className="text-sm sm:text-base font-black text-slate-800 truncate">{tx.activity}</div>
                                                    <div className="text-xs text-slate-500 mt-1 truncate">{tx.itemName}</div>
                                                </div>
                                                <div className="flex items-center justify-between sm:flex-col sm:items-end gap-2">
                                                    <div className={"font-mono font-black text-xl sm:text-2xl " + (tx.amount > 0 ? "text-emerald-500" : "text-rose-500")}>
                                                        {tx.amount > 0 ? "+" + tx.amount : tx.amount}
                                                    </div>
                                                    <div className="text-[10px] bg-slate-50 px-2 py-1 rounded-lg text-slate-400 font-black border border-slate-100">
                                                        ID: {tx.user.split('@')[0].toUpperCase()}
                                                    </div>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}
                        </main>
                    </div>

                    {/* Mobile Bottom Navigation (Hidden on Desktop) */}
                    <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-white/90 backdrop-blur-xl border-t border-slate-200 p-4 flex justify-around items-center z-50 rounded-t-3xl shadow-[0_-10px_40px_rgba(0,0,0,0.05)] pb-6">
                        <button onClick={() => setActiveTab('summary')} className={"flex flex-col items-center gap-1 transition-all " + (activeTab === 'summary' ? "text-indigo-600 scale-110" : "text-slate-400")}>
                            <Icon name="home" size={24} /><span className="text-[10px] font-black uppercase">Home</span>
                        </button>
                        <button onClick={() => setActiveTab('add')} className="relative -mt-10">
                            <div className={"p-4 rounded-2xl shadow-xl active:scale-90 transition-all " + (activeTab === 'add' ? "bg-indigo-600 text-white" : "bg-slate-700 text-white")}>
                                <Icon name="plus" size={28} />
                            </div>
                        </button>
                        <button onClick={() => setActiveTab('history')} className={"flex flex-col items-center gap-1 transition-all " + (activeTab === 'history' ? "text-indigo-600 scale-110" : "text-slate-400")}>
                            <Icon name="history" size={24} /><span className="text-[10px] font-black uppercase">Logs</span>
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

# 在 Streamlit 渲染 HTML (調整高度以適合新版式)
components.html(react_code, height=1000, scrolling=True)
