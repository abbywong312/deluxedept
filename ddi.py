import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題
st.set_page_config(page_title="Augusto Inventory System", layout="wide")

# React + Tailwind + Lucide HTML
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
        body { margin: 0; background-color: #f8fafc; font-family: sans-serif; }
        .lucide { width: 20px; height: 20px; vertical-align: middle; }
    </style>
</head>
<body>
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useMemo } = React;

        const Icon = ({ name, size = 20 }) => {
            const icons = {
                package: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg>,
                search: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>,
                logout: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg>,
                history: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/></svg>,
                home: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>,
                plus: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>,
                arrow: <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
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

            const [items] = useState([
                { id: 1, name: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', category: 'FG' },
                { id: 2, name: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', category: 'FG' },
                { id: 3, name: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', category: 'FG' },
                { id: 4, name: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', category: 'FG' },
                { id: 5, name: 'Augusto VIP Giftbox w/2 Glasses', category: 'FG' },
                { id: 6, name: 'Augusto Reposado Giftbox w/2 Glasses', category: 'FG' },
                { id: 7, name: 'Augusto Tequila Shaker (Black)', category: 'POSM' },
                { id: 8, name: 'Augusto Tequila Shaker (Copper)', category: 'POSM' },
                { id: 9, name: 'Dali Technology Black Cigar Cutter', category: 'POSM' },
                { id: 10, name: 'Dali Technology Copper Cigar Cutter', category: 'POSM' },
                { id: 11, name: 'SDM Asia Black Cap', category: 'POSM' },
                { id: 12, name: 'Small Pouch', category: 'POSM' },
                { id: 13, name: 'Non-woven bag', category: 'POSM' },
                { id: 14, name: 'Augusto Tequila Ice Bucket UK Version', category: 'POSM' },
                { id: 15, name: 'Augusto Tequila Ice Bucket US Version', category: 'POSM' },
                { id: 16, name: 'Augusto Tequila Glorifier UK Version', category: 'POSM' },
                { id: 17, name: 'Augusto Tequila Glorifier US Version', category: 'POSM' },
                { id: 18, name: 'Zhongshan Ho Crafts Gold Pin', category: 'POSM' },
                { id: 19, name: 'Zhongshan Ho Crafts Silver Pin', category: 'POSM' },
                { id: 20, name: 'Augusto Crystal Cabalito', category: 'POSM' },
                { id: 21, name: 'Veyron Giftbox Blister', category: 'POSM' },
                { id: 22, name: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', category: 'Accessories' },
                { id: 23, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
                { id: 24, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
                { id: 25, name: 'Augusto Neck Collar - Gold Medium Thread - Screw', category: 'Accessories' }
            ]);

            const [transactions, setTransactions] = useState([
                // Tres Mujeres Reposado
                { id: 't1', date: '2026-04-09', activity: 'Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office' },
                { id: 't2', date: '2026-04-09', activity: 'Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 156, location: 'Worldex' },
                { id: 't3', date: '2026-04-09', activity: 'Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai' },
                // Tres Mujeres Joven
                { id: 't4', date: '2026-04-09', activity: 'Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 13, location: 'Office' },
                { id: 't5', date: '2026-04-09', activity: 'Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 36, location: 'Worldex' },
                { id: 't6', date: '2026-04-09', activity: 'Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 491, location: 'San Tai' },
                // LC Augusto Hex
                { id: 't7', date: '2026-04-09', activity: 'Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 4, location: 'Office' },
                { id: 't8', date: '2026-04-09', activity: 'Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex' },
                // Cofraida YOS
                { id: 't9', date: '2026-04-09', activity: 'Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 2, location: 'Office' },
                { id: 't10', date: '2026-04-09', activity: 'Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 54, location: 'Worldex' },
                // Giftboxes
                { id: 't11', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto VIP Giftbox w/2 Glasses', amount: 294, location: 'Worldex' },
                { id: 't12', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Reposado Giftbox w/2 Glasses', amount: 162, location: 'Worldex' },
                // Shakers
                { id: 't13', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 23, location: 'Office' },
                { id: 't14', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 141, location: 'Worldex' },
                { id: 't15', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 21, location: 'Office' },
                { id: 't16', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 117, location: 'Worldex' },
                // Cutters & Pins
                { id: 't17', date: '2026-04-09', activity: 'Balance', itemName: 'Dali Technology Black Cigar Cutter', amount: 98, location: 'Office' },
                { id: 't18', date: '2026-04-09', activity: 'Balance', itemName: 'Dali Technology Copper Cigar Cutter', amount: 102, location: 'Office' },
                { id: 't19', date: '2026-04-09', activity: 'Balance', itemName: 'Zhongshan Ho Crafts Gold Pin', amount: 8, location: 'Office' },
                { id: 't20', date: '2026-04-09', activity: 'Balance', itemName: 'Zhongshan Ho Crafts Silver Pin', amount: 182, location: 'Office' },
                // Bags & Pouch
                { id: 't21', date: '2026-04-09', activity: 'Balance', itemName: 'SDM Asia Black Cap', amount: 29, location: 'Office' },
                { id: 't22', date: '2026-04-09', activity: 'Balance', itemName: 'Small Pouch', amount: 797, location: 'Office' },
                { id: 't23', date: '2026-04-09', activity: 'Balance', itemName: 'Non-woven bag', amount: 1050, location: 'Worldex' },
                // Bar Tools
                { id: 't24', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Ice Bucket UK Version', amount: 26, location: 'Worldex' },
                { id: 't25', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Ice Bucket US Version', amount: 16, location: 'Worldex' },
                { id: 't26', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Glorifier UK Version', amount: 14, location: 'Worldex' },
                { id: 't27', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Glorifier US Version', amount: 19, location: 'Worldex' },
                { id: 't28', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Crystal Cabalito', amount: 3, location: 'Office' },
                { id: 't29', date: '2026-04-09', activity: 'Balance', itemName: 'Veyron Giftbox Blister', amount: 2, location: 'Worldex' },
                // Accessories
                { id: 't30', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', amount: 2448, location: 'Office' },
                { id: 't31', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Reposado - Gold Stopper', amount: 1320, location: 'Worldex' },
                { id: 't32', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Tequila Reposado - Gold Triangle', amount: 728, location: 'Office' },
                { id: 't33', date: '2026-04-09', activity: 'Balance', itemName: 'Augusto Neck Collar - Gold Medium Thread - Screw', amount: 348, location: 'Office' }
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
                const finalLoc = formData.location === 'Other' ? formData.customLocation : formData.location;

                if (formMode === 'transfer') {
                    setTransactions(prev => [
                        { id: Date.now()+1, date: now, activity: "Transfer to " + formData.toLocation, itemName: formData.itemName, amount: -qty, location: formData.fromLocation },
                        { id: Date.now()+2, date: now, activity: "Transfer from " + formData.fromLocation, itemName: formData.itemName, amount: qty, location: formData.toLocation },
                        ...prev
                    ]);
                } else {
                    setTransactions(prev => [{ id: Date.now(), date: now, activity: formData.activity || (qty > 0 ? "In" : "Out"), itemName: formData.itemName, amount: qty, location: finalLoc }, ...prev]);
                }
                setFormData({ ...formData, amount: '', activity: '' });
                setActiveTab('summary');
            };

            if (!user) {
                return (
                    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-6">
                        <div className="bg-white rounded-[2rem] shadow-2xl w-full max-w-sm p-10 space-y-8">
                            <div className="text-center">
                                <div className="w-16 h-16 bg-indigo-50 rounded-2xl flex items-center justify-center mx-auto text-indigo-600 mb-4"><Icon name="package" size={32} /></div>
                                <h1 className="text-2xl font-black text-slate-800 tracking-tight">Augusto</h1>
                            </div>
                            <form onSubmit={handleLogin} className="space-y-4">
                                <input type="email" placeholder="Email" className="w-full p-4 bg-slate-50 border rounded-xl" value={loginEmail} onChange={e => setLoginEmail(e.target.value)} required />
                                <input type="password" placeholder="Password" className="w-full p-4 bg-slate-50 border rounded-xl" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
                                {loginError && <p className="text-rose-500 text-xs text-center font-bold">{loginError}</p>}
                                <button type="submit" className="w-full bg-indigo-600 text-white font-black py-4 rounded-xl shadow-lg hover:bg-indigo-700 uppercase tracking-widest text-sm transition-all">Login</button>
                            </form>
                        </div>
                    </div>
                );
            }

            return (
                <div className="min-h-screen bg-slate-50 flex flex-col pb-28 text-slate-900 font-sans">
                    <header className="bg-indigo-700 text-white p-6 shadow-xl flex justify-between items-center sticky top-0 z-50 rounded-b-[2rem]">
                        <div className="flex items-center gap-3"><Icon name="package" /><h1 className="text-xl font-black">Augusto Inventory</h1></div>
                        <button onClick={() => setUser(null)} className="p-3 bg-white/10 rounded-xl"><Icon name="logout" /></button>
                    </header>

                    <main className="p-4 max-w-2xl mx-auto w-full">
                        {activeTab === 'summary' && (
                            <div className="space-y-6">
                                <div className="relative">
                                    <div className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"><Icon name="search" size={16} /></div>
                                    <input type="text" placeholder="Search..." className="w-full pl-12 pr-6 py-4 bg-white border border-slate-100 rounded-3xl text-sm shadow-sm outline-none focus:ring-2 focus:ring-indigo-500" onChange={(e) => setSearchTerm(e.target.value)} />
                                </div>
                                {['FG', 'POSM', 'Accessories'].map(cat => {
                                    const catItems = items.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
                                    if (catItems.length === 0) return null;
                                    return (
                                        <div key={cat} className="space-y-4">
                                            <h3 className="text-[10px] font-black text-slate-400 uppercase tracking-widest px-2">{cat}</h3>
                                            <div className="grid gap-3">
                                                {catItems.map(item => {
                                                    const data = stockSummary[item.name];
                                                    return (
                                                        <div key={item.id} className="bg-white p-5 rounded-[1.5rem] shadow-sm border border-slate-50">
                                                            <div className="flex justify-between items-start mb-3">
                                                                <span className="text-xs font-bold text-slate-700 leading-tight pr-4">{item.name}</span>
                                                                <span className={"font-mono font-black text-xl " + (data.total > 0 ? "text-indigo-600" : "text-slate-200")}>{data.total}</span>
                                                            </div>
                                                            <div className="flex flex-wrap gap-2">
                                                                {['Office', 'Worldex', 'San Tai'].map(loc => (
                                                                    <div key={loc} className={"px-3 py-1 rounded-lg text-[9px] font-black border " + (data.details[loc] > 0 ? "bg-indigo-50 border-indigo-100 text-indigo-600" : "bg-slate-50 border-transparent text-slate-300")}>
                                                                        {loc}: {data.details[loc]}
                                                                    </div>
                                                                ))}
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
                            <div className="space-y-6">
                                <div className="flex bg-white p-1 rounded-2xl shadow-sm border border-slate-100">
                                    {['inout', 'transfer'].map(m => (
                                        <button key={m} onClick={() => setFormMode(m)} className={"flex-1 py-3 rounded-xl text-[10px] font-black uppercase " + (formMode === m ? "bg-indigo-600 text-white" : "text-slate-400")}>{m}</button>
                                    ))}
                                </div>
                                <form onSubmit={handleAction} className="bg-white p-8 rounded-[2rem] shadow-2xl space-y-6">
                                    <div className="space-y-1">
                                        <label className="text-[10px] font-black text-slate-400 uppercase">Product</label>
                                        <select className="w-full p-4 bg-slate-50 border rounded-xl text-sm" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>{items.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}</select>
                                    </div>
                                    <div className="grid grid-cols-2 gap-4">
                                        <input type="number" className="w-full p-4 bg-slate-50 border rounded-xl text-sm font-mono" placeholder="Qty" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required />
                                        <input type="text" className="w-full p-4 bg-slate-50 border rounded-xl text-sm" placeholder="Remark" value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                                    </div>
                                    <button type="submit" className="w-full bg-indigo-600 text-white font-black py-4 rounded-xl shadow-lg uppercase text-xs tracking-widest">Confirm</button>
                                </form>
                            </div>
                        )}

                        {activeTab === 'history' && (
                            <div className="space-y-3">
                                <h2 className="text-xl font-black text-slate-800">History</h2>
                                {transactions.slice(0, 50).map(tx => (
                                    <div key={tx.id} className="bg-white p-4 rounded-2xl shadow-sm border border-slate-50 flex items-center justify-between">
                                        <div className="flex-1 min-w-0">
                                            <div className="flex items-center gap-2 mb-1"><span className="text-[9px] font-black px-2 py-0.5 bg-indigo-50 text-indigo-600 rounded border border-indigo-100">{tx.location}</span><span className="text-[9px] text-slate-400">{tx.date}</span></div>
                                            <div className="text-xs font-black text-slate-700 truncate">{tx.itemName}</div>
                                        </div>
                                        <div className={"font-mono font-black text-md pl-4 " + (tx.amount > 0 ? "text-emerald-500" : "text-rose-500")}>
                                            {tx.amount > 0 ? "+" + tx.amount : tx.amount}
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </main>

                    <nav className="fixed bottom-0 left-0 right-0 bg-white/90 backdrop-blur-xl border-t p-6 flex justify-around items-center z-50 rounded-t-[2.5rem] shadow-2xl">
                        <button onClick={() => setActiveTab('summary')} className={activeTab === 'summary' ? "text-indigo-600" : "text-slate-300"}><Icon name="home" /></button>
                        <button onClick={() => setActiveTab('add')} className="p-5 bg-indigo-600 text-white rounded-[1.5rem] shadow-xl -mt-12 border-4 border-white"><Icon name="plus" size={28} /></button>
                        <button onClick={() => setActiveTab('history')} className={activeTab === 'history' ? "text-indigo-600" : "text-slate-300"}><Icon name="history" /></button>
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

# 渲染
components.html(react_code, height=900, scrolling=True)
