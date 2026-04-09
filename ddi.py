import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題，使用寬版面適應 Desktop
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
        body { margin: 0; background-color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
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
                package: <svg width={size} height={size} className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>,
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

            // 1. 更新並拆分所有 T-shirt 和 Hoodie 的 Size (共 40 多個項目)
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
                { id: 207, name: 'SDM Asia Green T-shirt Size S', category: 'POSM' },
                { id: 208, name: 'SDM Asia Green T-shirt Size M', category: 'POSM' },
                { id: 209, name: 'SDM Asia Green T-shirt Size L', category: 'POSM' },
                { id: 210, name: 'SDM Asia Green T-shirt Size XL', category: 'POSM' },
                { id: 211, name: 'SDM Asia Black T-shirt Size S', category: 'POSM' },
                { id: 212, name: 'SDM Asia Black T-shirt Size M', category: 'POSM' },
                { id: 213, name: 'SDM Asia Black T-shirt Size L', category: 'POSM' },
                { id: 214, name: 'SDM Asia Black T-shirt Size XL', category: 'POSM' },
                { id: 215, name: 'SDM Asia Green Hoodie Size S', category: 'POSM' },
                { id: 216, name: 'SDM Asia Green Hoodie Size M', category: 'POSM' },
                { id: 217, name: 'SDM Asia Green Hoodie Size L', category: 'POSM' },
                { id: 218, name: 'SDM Asia Green Hoodie Size XL', category: 'POSM' },
                { id: 219, name: 'SDM Asia Grey Hoodie Size S', category: 'POSM' },
                { id: 220, name: 'SDM Asia Grey Hoodie Size M', category: 'POSM' },
                { id: 221, name: 'SDM Asia Grey Hoodie Size L', category: 'POSM' },
                { id: 222, name: 'SDM Asia Grey Hoodie Size XL', category: 'POSM' },
                { id: 223, name: 'Augusto Crystal Cabalito', category: 'POSM' },
                { id: 224, name: 'Non-woven bag', category: 'POSM' },
                { id: 225, name: 'Augusto Tequila Ice Bucket UK Version', category: 'POSM' },
                { id: 226, name: 'Augusto Tequila Ice Bucket US Version', category: 'POSM' },
                { id: 227, name: 'Augusto Tequila Glorifier UK Version', category: 'POSM' },
                { id: 228, name: 'Augusto Tequila Glorifier US Version', category: 'POSM' },
                { id: 229, name: 'Zhongshan Ho Crafts Gold Pin', category: 'POSM' },
                { id: 230, name: 'Zhongshan Ho Crafts Silver Pin', category: 'POSM' },
                { id: 231, name: 'Veyron Giftbox Blister', category: 'POSM' },
                { id: 301, name: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', category: 'Accessories' },
                { id: 302, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
                { id: 303, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
                { id: 304, name: 'Augusto Neck Collar - Gold Medium Thread - Screw', category: 'Accessories' },
                { id: 305, name: 'Augusto Tequila Joven - Silver Stopper', category: 'Accessories' },
                { id: 306, name: 'Augusto Tequila Joven - Silver Triangle', category: 'Accessories' }
            ]);

            // 2. 嚴格根據截圖輸入的精確庫存紀錄
            const [transactions, setTransactions] = useState([
                { id: 't1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
                { id: 't2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
                { id: 't3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' },
                { id: 't4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Crystal Cabalito', amount: 3, location: 'Office', user: 'System' }
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

            const [formMode, setFormMode] = useState('inout'); 
            const [formData, setFormData] = useState({ 
                activity: '', itemName: items[0].name, amount: '', location: 'Office', customLocation: '', fromLocation: 'Worldex', toLocation: 'Office', newCategory: 'FG'
            });

            const handleLogin = (e) => {
                e.preventDefault();
                const found = authorizedUsers.find(u => u.email === loginEmail && u.password === loginPassword);
                if (found) { setUser(found.email); setLoginError(''); } 
                else { setLoginError('Invalid email or password'); }
            };

            const handleAction = (e) => {
                e.preventDefault();
                const now = new Date().toISOString().split('T')[0];
                const qty = parseInt(formData.amount) || 0;
                const finalLoc = formData.location === 'Other' ? formData.customLocation.trim() : formData.location;

                if (formMode === 'newitem') {
                    const name = formData.itemName.trim();
                    if(!name) return;
                    if(items.some(i => i.name.toLowerCase() === name.toLowerCase())) { alert("Item already exists!"); return; }
                    setItems(prev => [...prev, { id: Date.now(), name, category: formData.newCategory }]);
                    if(qty !== 0) {
                        setTransactions(prev => [{ id: Date.now(), date: now, activity: 'Initial Entry', itemName: name, amount: qty, location: finalLoc || 'Office', user: user }, ...prev]);
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
                    setTransactions(prev => [{ id: Date.now(), date: now, activity: formData.activity || (qty > 0 ? "Stock In" : "Stock Out"), itemName: formData.itemName, amount: qty, location: finalLoc || 'Office', user: user }, ...prev]);
                }
                setFormData({ ...formData, amount: '', activity: '', customLocation: '', itemName: formMode === 'newitem' ? items[0].name : formData.itemName });
                setActiveTab('summary');
            };

            if (!user) {
                return (
                    <div className="min-h-screen bg-[#6366f1] flex items-center justify-center p-4 font-sans">
                        <div className="bg-white rounded-3xl shadow-2xl w-full max-w-sm p-8 space-y-6 text-center">
                            <div className="w-16 h-16 bg-indigo-50 rounded-2xl flex items-center justify-center mx-auto text-indigo-600 mb-2"><Icon name="package" size={32} /></div>
                            <h1 className="text-2xl font-black text-slate-800 tracking-tight">Augusto Inventory</h1>
                            <form onSubmit={handleLogin} className="space-y-3">
                                <input type="email" placeholder="Email" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-xl text-sm focus:ring-2 focus:ring-indigo-500 outline-none" value={loginEmail} onChange={e => setLoginEmail(e.target.value)} required />
                                <input type="password" placeholder="Password" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-xl text-sm focus:ring-2 focus:ring-indigo-500 outline-none" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
                                {loginError && <p className="text-rose-500 text-xs font-bold">{loginError}</p>}
                                <button type="submit" className="w-full bg-indigo-600 text-white font-bold py-4 rounded-xl shadow-lg hover:bg-indigo-700 transition-all uppercase tracking-widest text-sm">Login</button>
                            </form>
                        </div>
                    </div>
                );
            }

            return (
                <div className="min-h-screen bg-[#e2e8f0] flex flex-col font-sans pb-24">
                    {/* Header */}
                    <header className="bg-[#6366f1] text-white p-4 sm:p-5 shadow-md flex justify-between items-center sticky top-0 z-50">
                        <div className="flex items-center gap-2">
                            <Icon name="package" size={24} />
                            <h1 className="text-xl font-black tracking-tight">Augusto Inventory</h1>
                        </div>
                        <button onClick={() => setUser(null)} className="p-2 bg-white/10 rounded-xl hover:bg-white/20 transition-all"><Icon name="logout" size={20} /></button>
                    </header>

                    <main className="flex-1 p-4 sm:p-6 w-full max-w-4xl mx-auto">
                        {activeTab === 'summary' && (
                            <div className="space-y-6 animate-in fade-in duration-300">
                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-2">
                                    <h2 className="text-2xl sm:text-3xl font-black text-slate-800">庫存概覽 / Stock Overview</h2>
                                    <div className="relative w-full sm:w-64">
                                        <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"><Icon name="search" size={16} /></div>
                                        <input type="text" placeholder="搜尋 / Search..." className="w-full pl-10 pr-4 py-3 bg-white border border-slate-200 rounded-full text-sm font-medium shadow-sm outline-none focus:ring-2 focus:ring-indigo-500" onChange={(e) => setSearchTerm(e.target.value)} />
                                    </div>
                                </div>

                                {['FG', 'POSM', 'Accessories'].map(cat => {
                                    const catItems = items.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
                                    if (catItems.length === 0) return null;
                                    return (
                                        <div key={cat} className="bg-transparent mb-8">
                                            {/* 單欄列表的 Header */}
                                            <div className="flex items-center justify-between px-2 pb-3 mb-2 border-b border-slate-300">
                                                <span className="text-xs font-black text-slate-500 uppercase tracking-widest">{cat === 'FG' ? '成品 / FINISHED GOODS' : cat === 'POSM' ? '宣傳品 / POSM' : '配件 / ACCESSORIES'}</span>
                                                <span className="text-xs font-black text-slate-400 uppercase tracking-widest">總數及位置 / TOTAL / LOCATION</span>
                                            </div>
                                            
                                            {/* 單欄列表內容 (完全按照截圖) */}
                                            <div className="bg-transparent flex flex-col">
                                                {catItems.map((item, index) => {
                                                    const data = stockSummary[item.name] || { total: 0, details: {} };
                                                    const isLast = index === catItems.length - 1;
                                                    return (
                                                        <div key={item.id} className={"py-5 px-2 flex flex-col gap-2 " + (isLast ? "" : "border-b border-slate-300")}>
                                                            <div className="flex justify-between items-start">
                                                                <span className="text-[15px] sm:text-[17px] font-bold text-slate-800 leading-snug pr-4">{item.name}</span>
                                                                <span className={"font-black text-2xl sm:text-3xl " + (data.total > 0 ? "text-indigo-600" : "text-slate-300")}>{data.total}</span>
                                                            </div>
                                                            <div className="flex flex-wrap gap-2 mt-1">
                                                                {['Office', 'Worldex', 'San Tai'].map(loc => {
                                                                    const qty = data.details[loc] || 0;
                                                                    const isActive = qty > 0;
                                                                    return (
                                                                        <div key={loc} className={"px-3 py-1.5 rounded-full text-xs font-bold transition-colors " + (isActive ? "bg-indigo-100 text-indigo-700" : "bg-slate-200 text-slate-400")}>
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
                                <div className="flex bg-white p-1.5 rounded-2xl shadow-sm border border-slate-200">
                                    {['inout', 'transfer', 'newitem'].map(m => (
                                        <button key={m} onClick={() => setFormMode(m)} className={"flex-1 py-3 text-[11px] sm:text-xs font-black uppercase tracking-wider rounded-xl transition-all " + (formMode === m ? "bg-indigo-600 text-white shadow-md" : "text-slate-500 hover:bg-slate-50")}>
                                            {m === 'inout' ? 'Stock In/Out' : m === 'transfer' ? 'Transfer' : 'New Item'}
                                        </button>
                                    ))}
                                </div>

                                <form onSubmit={handleAction} className="bg-white p-6 sm:p-10 rounded-3xl shadow-md border border-slate-100 space-y-6">
                                    {formMode === 'newitem' ? (
                                        <div className="space-y-4">
                                            <div className="space-y-2">
                                                <label className="text-xs font-bold text-slate-500 uppercase">New Item Name</label>
                                                <input type="text" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="Enter Full Name..." value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})} required />
                                            </div>
                                            <div className="space-y-2">
                                                <label className="text-xs font-bold text-slate-500 uppercase">Category</label>
                                                <div className="grid grid-cols-3 gap-2">
                                                    {['FG', 'POSM', 'Accessories'].map(c => (
                                                        <button key={c} type="button" onClick={() => setFormData({...formData, newCategory: c})} className={"py-3 rounded-xl text-xs font-bold border transition-all " + (formData.newCategory === c ? "bg-indigo-50 border-indigo-200 text-indigo-700" : "bg-white border-slate-200 text-slate-500 hover:border-indigo-300")}>{c}</button>
                                                    ))}
                                                </div>
                                            </div>
                                        </div>
                                    ) : (
                                        <div className="space-y-2">
                                            <label className="text-xs font-bold text-slate-500 uppercase">Select Product</label>
                                            <select className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                                                {items.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                                            </select>
                                        </div>
                                    )}

                                    <div className="space-y-4 pt-4 border-t border-slate-100">
                                        {formMode === 'transfer' ? (
                                            <div className="flex flex-col sm:flex-row items-center gap-4 bg-slate-50 p-4 rounded-xl border border-slate-200">
                                                <div className="w-full flex-1">
                                                    <label className="text-xs font-bold text-slate-500 uppercase mb-2 block">From</label>
                                                    <select className="w-full p-3 bg-white border border-slate-200 rounded-lg text-sm font-bold outline-none" value={formData.fromLocation} onChange={e => setFormData({...formData, fromLocation: e.target.value})}>
                                                        {['Office', 'Worldex', 'San Tai', 'Other'].map(l => <option key={l} value={l}>{l}</option>)}
                                                    </select>
                                                </div>
                                                <div className="w-8 h-8 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 sm:mt-6 shrink-0 rotate-90 sm:rotate-0"><Icon name="arrowRight" size={16} /></div>
                                                <div className="w-full flex-1">
                                                    <label className="text-xs font-bold text-slate-500 uppercase mb-2 block">To</label>
                                                    <select className="w-full p-3 bg-white border border-slate-200 rounded-lg text-sm font-bold outline-none" value={formData.toLocation} onChange={e => setFormData({...formData, toLocation: e.target.value})}>
                                                        {['Office', 'Worldex', 'San Tai', 'Other'].map(l => <option key={l} value={l}>{l}</option>)}
                                                    </select>
                                                </div>
                                            </div>
                                        ) : (
                                            <div className="space-y-3">
                                                <label className="text-xs font-bold text-slate-500 uppercase">Location</label>
                                                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                                    {['Office', 'Worldex', 'San Tai', 'Other'].map(l => (
                                                        <button key={l} type="button" onClick={() => setFormData({...formData, location: l})} className={"py-3 rounded-xl text-xs font-bold border transition-all " + (formData.location === l ? "bg-indigo-600 text-white border-indigo-600" : "bg-white text-slate-500 border-slate-200 hover:border-indigo-300")}>{l}</button>
                                                    ))}
                                                </div>
                                                {formData.location === 'Other' && (
                                                    <input type="text" className="w-full p-4 mt-2 bg-indigo-50 border border-indigo-200 rounded-xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none text-indigo-900 placeholder:text-indigo-300" placeholder="Enter custom location name..." value={formData.customLocation} onChange={e => setFormData({...formData, customLocation: e.target.value})} required />
                                                )}
                                            </div>
                                        )}
                                    </div>

                                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-4 border-t border-slate-100">
                                        <div className="space-y-2">
                                            <label className="text-xs font-bold text-slate-500 uppercase">Quantity</label>
                                            <input type="number" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-xl font-black font-mono focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="0" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required={formMode !== 'newitem'} />
                                        </div>
                                        <div className="space-y-2">
                                            <label className="text-xs font-bold text-slate-500 uppercase">Remarks</label>
                                            <input type="text" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none placeholder:font-medium" placeholder="Optional notes..." value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                                        </div>
                                    </div>

                                    <button type="submit" className="w-full bg-indigo-600 text-white font-black py-5 rounded-xl shadow-md hover:bg-indigo-700 active:scale-[0.98] transition-all uppercase tracking-widest text-sm">
                                        {formMode === 'newitem' ? 'Create Item & Update Stock' : 'Confirm Transaction'}
                                    </button>
                                </form>
                            </div>
                        )}

                        {activeTab === 'history' && (
                            <div className="space-y-6 animate-in fade-in duration-300 max-w-2xl mx-auto">
                                <h2 className="text-2xl sm:text-3xl font-black text-slate-800">History Logs</h2>
                                <div className="grid gap-3">
                                    {transactions.slice(0, 50).map(tx => (
                                        <div key={tx.id} className="bg-white p-5 rounded-2xl shadow-sm border border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                            <div className="flex-1 min-w-0">
                                                <div className="flex items-center gap-3 mb-2">
                                                    <span className="px-2.5 py-1 rounded-md text-[10px] font-black bg-indigo-50 text-indigo-700 uppercase tracking-wider">{tx.location}</span>
                                                    <span className="text-[11px] text-slate-400 font-bold">{tx.date}</span>
                                                </div>
                                                <div className="text-sm font-black text-slate-800 truncate">{tx.activity}</div>
                                                <div className="text-xs text-slate-500 mt-1 truncate">{tx.itemName}</div>
                                            </div>
                                            <div className="flex items-center justify-between sm:flex-col sm:items-end gap-2">
                                                <div className={"font-mono font-black text-xl " + (tx.amount > 0 ? "text-emerald-500" : "text-rose-500")}>
                                                    {tx.amount > 0 ? "+" + tx.amount : tx.amount}
                                                </div>
                                                <div className="text-[10px] bg-slate-50 px-2 py-1 rounded border border-slate-100 text-slate-400 font-bold">
                                                    ID: {tx.user.split('@')[0].toUpperCase()}
                                                </div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        )}
                    </main>

                    {/* Bottom Navigation */}
                    <nav className="fixed bottom-0 left-0 right-0 bg-[#e2e8f0]/90 backdrop-blur-md border-t border-slate-300 p-4 flex justify-around items-center z-50 shadow-[0_-5px_20px_rgba(0,0,0,0.05)] pb-6">
                        <button onClick={() => setActiveTab('summary')} className={"flex flex-col items-center gap-1 transition-all " + (activeTab === 'summary' ? "text-indigo-700 scale-110" : "text-slate-500 hover:text-indigo-400")}>
                            <Icon name="home" size={24} /><span className="text-[10px] font-black uppercase tracking-wider">概覽 / HOME</span>
                        </button>
                        <button onClick={() => setActiveTab('add')} className="relative -mt-8">
                            <div className="p-4 rounded-full shadow-lg bg-indigo-400/50 backdrop-blur-sm flex items-center justify-center border-4 border-[#e2e8f0]">
                                <div className={"p-3 rounded-full shadow-inner transition-all " + (activeTab === 'add' ? "bg-indigo-600 text-white" : "bg-[#818cf8] text-white hover:bg-indigo-500")}>
                                    <Icon name="plus" size={24} />
                                </div>
                            </div>
                        </button>
                        <button onClick={() => setActiveTab('history')} className={"flex flex-col items-center gap-1 transition-all " + (activeTab === 'history' ? "text-indigo-700 scale-110" : "text-slate-500 hover:text-indigo-400")}>
                            <Icon name="history" size={24} /><span className="text-[10px] font-black uppercase tracking-wider">歷史 / LOGS</span>
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

# 在 Streamlit 渲染 HTML (調整高度)
components.html(react_code, height=950, scrolling=True)
