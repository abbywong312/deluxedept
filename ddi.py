import React, { useState, useMemo } from 'react';
import { PlusCircle, History, LayoutDashboard, Package, Search, ArrowRightLeft, ArrowRight, ArrowUp, Calendar, LogIn, LogOut, User } from 'lucide-react';

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

  // Item definitions
  const initialItems = [
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
    { id: 207, name: 'Augusto Tequila Ice Bucket UK Version', category: 'POSM' },
    { id: 208, name: 'Augusto Tequila Ice Bucket US Version', category: 'POSM' },
    { id: 209, name: 'Augusto Tequila Glorifier UK Version', category: 'POSM' },
    { id: 210, name: 'Augusto Tequila Glorifier US Version', category: 'POSM' },
    { id: 211, name: 'Zhongshan Ho Crafts And Gifts Co Gold Pin', category: 'POSM' },
    { id: 212, name: 'Zhongshan Ho Crafts And Gifts Co Silver Pin', category: 'POSM' },
    { id: 301, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
    { id: 302, name: 'Augusto Tequila Reposado - Gold Neck Collar-Small', category: 'Accessories' },
    { id: 303, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
    { id: 304, name: 'Augusto Neck Collar - Gold Medium Thread', category: 'Accessories' }
  ];

  // Initial Transaction Data based on latest screenshots
  const [transactions, setTransactions] = useState([
    // Office Stock
    { id: 'o1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
    { id: 'o2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 13, location: 'Office', user: 'System' },
    { id: 'o3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Black Cigar Cutter', amount: 98, location: 'Office', user: 'System' },
    { id: 'o4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Copper Cigar Cutter', amount: 102, location: 'Office', user: 'System' },
    { id: 'o5', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Small Pouch', amount: 797, location: 'Office', user: 'System' },
    { id: 'o6', date: '2026-04-09', activity: 'Initial Balance', itemName: 'SDM Asia Black Cap', amount: 29, location: 'Office', user: 'System' },

    // Worldex Stock
    { id: 'w1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
    { id: 'w2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 54, location: 'Worldex', user: 'System' },
    { id: 'w3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 156, location: 'Worldex', user: 'System' },
    { id: 'w4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 36, location: 'Worldex', user: 'System' },
    { id: 'w5', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto VIP Giftbox w/2 Glasses', amount: 294, location: 'Worldex', user: 'System' },
    { id: 'w6', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Reposado Giftbox w/2 Glasses', amount: 162, location: 'Worldex', user: 'System' },
    { id: 'w7', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Stopper', amount: 1320, location: 'Worldex', user: 'System' },
    { id: 'w8', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 141, location: 'Worldex', user: 'System' },
    { id: 'w9', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 117, location: 'Worldex', user: 'System' },

    // San Tai Stock
    { id: 'st1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' },
    { id: 'st2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 491, location: 'San Tai', user: 'System' },
  ]);

  const stockSummary = useMemo(() => {
    const summary = {};
    initialItems.forEach(item => { summary[item.name] = { total: 0, office: 0, worldex: 0, sanTai: 0 }; });
    transactions.forEach(tx => {
      if (summary[tx.itemName]) {
        summary[tx.itemName].total += tx.amount;
        if (tx.location === 'Worldex') summary[tx.itemName].worldex += tx.amount;
        else if (tx.location === 'San Tai') summary[tx.itemName].sanTai += tx.amount;
        else if (tx.location === 'Office') summary[tx.itemName].office += tx.amount;
      }
    });
    return summary;
  }, [transactions]);

  const [formMode, setFormMode] = useState('inout'); 
  const [formData, setFormData] = useState({ activity: '', itemName: initialItems[0].name, amount: '', location: 'Office', fromLocation: 'Worldex', toLocation: 'Office' });

  const handleLogin = (e) => {
    e.preventDefault();
    const found = authorizedUsers.find(u => u.email === loginEmail && u.password === loginPassword);
    if (found) { setUser(found.email); setLoginError(''); } 
    else { setLoginError('Invalid email or password'); }
  };

  const handleAddTransaction = (e) => {
    e.preventDefault();
    const now = new Date().toISOString().split('T')[0];
    const amount = parseInt(formData.amount);
    if (!amount || isNaN(amount)) return;

    if (formMode === 'transfer') {
      const txOut = { id: `tf-${Date.now()}-out`, date: now, activity: `Transfer to ${formData.toLocation}`, itemName: formData.itemName, amount: -amount, location: formData.fromLocation, user: user };
      const txIn = { id: `tf-${Date.now()}-in`, date: now, activity: `Transfer from ${formData.fromLocation}`, itemName: formData.itemName, amount: amount, location: formData.toLocation, user: user };
      setTransactions([txOut, txIn, ...transactions]);
    } else {
      const newTx = { id: Date.now(), date: now, activity: formData.activity || (amount > 0 ? 'Stock In' : 'Stock Out'), itemName: formData.itemName, amount: amount, location: formData.location, user: user };
      setTransactions([newTx, ...transactions]);
    }
    setFormData({ ...formData, activity: '', amount: '' });
    setActiveTab('history');
  };

  if (!user) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center p-6 text-slate-900">
        <div className="bg-white rounded-3xl shadow-2xl w-full max-w-sm p-8 space-y-6">
          <div className="text-center">
            <div className="inline-flex p-4 bg-indigo-50 rounded-2xl text-indigo-600 mb-4"><Package size={40} /></div>
            <h1 className="text-2xl font-black text-slate-800">Augusto Inventory</h1>
            <p className="text-slate-400 text-sm mt-1">Please log in to continue</p>
          </div>
          <form onSubmit={handleLogin} className="space-y-4">
            <input type="email" placeholder="Email" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-sm" value={loginEmail} onChange={e => setLoginEmail(e.target.value)} required />
            <input type="password" placeholder="Password" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-sm" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
            {loginError && <p className="text-rose-500 text-xs font-bold text-center">{loginError}</p>}
            <button type="submit" className="w-full bg-indigo-600 text-white font-bold py-4 rounded-2xl shadow-lg hover:bg-indigo-700 transition">Login</button>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col pb-24 text-slate-900">
      <header className="bg-indigo-700 text-white p-5 shadow-lg sticky top-0 z-30 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <Package size={22} className="text-indigo-200" />
          <h1 className="text-lg font-black tracking-tight">Augusto Inventory</h1>
        </div>
        <button onClick={() => setUser(null)} className="p-2 bg-white/10 rounded-xl hover:bg-white/20 transition"><LogOut size={18} /></button>
      </header>

      <main className="flex-1 p-4 max-w-2xl mx-auto w-full">
        {activeTab === 'summary' && (
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-black text-slate-800">Inventory Overview</h2>
              <div className="relative">
                <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                <input type="text" placeholder="Search..." className="pl-9 pr-4 py-2 border border-slate-200 rounded-full bg-white text-xs w-36 focus:ring-2 focus:ring-indigo-500 outline-none" onChange={(e) => setSearchTerm(e.target.value)} />
              </div>
            </div>

            {['FG', 'POSM', 'Accessories'].map(cat => {
              const items = initialItems.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
              if (items.length === 0) return null;
              return (
                <div key={cat} className="bg-white rounded-3xl shadow-sm border border-slate-200 overflow-hidden mb-6">
                  <div className="bg-slate-50 px-5 py-3 font-black text-slate-400 text-[10px] uppercase tracking-widest border-b border-slate-100 flex justify-between">
                    <span>{cat === 'FG' ? 'Finished Goods (FG)' : cat === 'POSM' ? 'Materials (POSM)' : 'Accessories'}</span>
                    <span>Total / Distribution</span>
                  </div>
                  <div className="divide-y divide-slate-50">
                    {items.map(item => {
                      const data = stockSummary[item.name];
                      return (
                        <div key={item.id} className="p-5 hover:bg-slate-50/50">
                          <div className="flex justify-between items-start mb-3">
                            <span className="text-sm font-bold text-slate-800 leading-snug flex-1 pr-6">{item.name}</span>
                            <span className={`font-mono font-black text-xl ${data.total <= 0 ? 'text-slate-300' : 'text-indigo-600'}`}>{data.total}</span>
                          </div>
                          <div className="flex flex-wrap gap-2">
                            {[
                                {label: 'Office', key: 'office'},
                                {label: 'Worldex', key: 'worldex'},
                                {label: 'San Tai', key: 'sanTai'}
                            ].map(loc => (
                                <div key={loc.key} className={`px-2 py-1 rounded-lg text-[10px] font-bold border ${data[loc.key] > 0 ? 'bg-indigo-50 border-indigo-100 text-indigo-600' : 'bg-slate-50 border-slate-100 text-slate-300'}`}>
                                    {loc.label}: {data[loc.key]}
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
          <div className="space-y-4">
            <div className="flex bg-white p-1 rounded-2xl shadow-sm border border-slate-200">
              <button onClick={() => setFormMode('inout')} className={`flex-1 py-3 rounded-xl text-xs font-black transition ${formMode === 'inout' ? 'bg-indigo-600 text-white' : 'text-slate-400'}`}>
                Stock In / Out
              </button>
              <button onClick={() => setFormMode('transfer')} className={`flex-1 py-3 rounded-xl text-xs font-black transition ${formMode === 'transfer' ? 'bg-indigo-600 text-white' : 'text-slate-400'}`}>
                Warehouse Transfer
              </button>
            </div>

            <form onSubmit={handleAddTransaction} className="bg-white p-6 rounded-3xl shadow-xl space-y-6 border border-slate-100">
              {formMode === 'transfer' ? (
                <div className="flex items-center gap-2 bg-slate-50 p-4 rounded-2xl border border-slate-100">
                  <select className="flex-1 p-2 bg-white border border-slate-200 rounded-xl text-xs font-bold" value={formData.fromLocation} onChange={e => setFormData({...formData, fromLocation: e.target.value})}>
                    {['Office', 'Worldex', 'San Tai'].map(loc => <option key={loc} value={loc}>{loc}</option>)}
                  </select>
                  <ArrowRight className="text-indigo-400" size={16} />
                  <select className="flex-1 p-2 bg-white border border-slate-200 rounded-xl text-xs font-bold" value={formData.toLocation} onChange={e => setFormData({...formData, toLocation: e.target.value})}>
                    {['Office', 'Worldex', 'San Tai'].map(loc => <option key={loc} value={loc}>{loc}</option>)}
                  </select>
                </div>
              ) : (
                <div className="grid grid-cols-3 gap-2">
                  {['Office', 'Worldex', 'San Tai'].map(loc => (
                    <button key={loc} type="button" onClick={() => setFormData({...formData, location: loc})} className={`py-3 rounded-xl text-[10px] font-black transition border ${formData.location === loc ? 'bg-indigo-600 text-white' : 'bg-white text-slate-400 border-slate-200'}`}>{loc}</button>
                  ))}
                </div>
              )}

              <div>
                <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1">Select Item</label>
                <select className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl text-sm" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                  {initialItems.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                </select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="col-span-1">
                  <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1">Quantity</label>
                  <input type="number" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl font-mono text-xl font-black" placeholder="0" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required />
                </div>
                <div className="col-span-1">
                  <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1">Notes</label>
                  <input type="text" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl text-sm" placeholder="Optional" value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                </div>
              </div>

              <button type="submit" className="w-full bg-indigo-600 text-white font-black py-4 rounded-2xl shadow-lg active:scale-95 transition">Update Stock</button>
            </form>
          </div>
        )}

        {activeTab === 'history' && (
          <div className="space-y-4">
            <h2 className="text-xl font-black text-slate-800">Transaction History</h2>
            <div className="space-y-3">
              {transactions.map(tx => (
                <div key={tx.id} className="bg-white p-5 rounded-3xl shadow-sm border border-slate-200">
                  <div className="flex justify-between items-center mb-2">
                    <div className="flex items-center gap-2">
                      <span className="px-2 py-0.5 rounded-lg text-[9px] font-black bg-blue-100 text-blue-700 uppercase">{tx.location}</span>
                      <span className="text-[10px] text-slate-400 font-bold">{tx.date}</span>
                    </div>
                    <div className={`font-mono font-black text-sm ${tx.amount > 0 ? 'text-emerald-600' : 'text-rose-600'}`}>{tx.amount > 0 ? '+' : ''}{tx.amount}</div>
                  </div>
                  <div className="flex justify-between items-end">
                    <div>
                      <div className="font-bold text-slate-800 text-sm">{tx.activity}</div>
                      <div className="text-[11px] text-slate-500 mt-1">{tx.itemName}</div>
                    </div>
                    <div className="text-[9px] bg-slate-50 px-2 py-1 rounded-lg text-slate-400 font-bold border border-slate-100">
                      BY: {tx.user.split('@')[0].toUpperCase()}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 flex justify-around p-4 shadow-2xl z-40 pb-8">
        <button onClick={() => setActiveTab('summary')} className={`flex flex-col items-center gap-1 ${activeTab === 'summary' ? 'text-indigo-600' : 'text-slate-300'}`}>
          <LayoutDashboard size={20} /><span className="text-[9px] font-black uppercase">Summary</span>
        </button>
        <button onClick={() => setActiveTab('add')} className="relative -mt-12">
          <div className="p-4 rounded-full bg-indigo-600 text-white shadow-xl ring-4 ring-white active:scale-90 transition">
            <PlusCircle size={32} />
          </div>
        </button>
        <button onClick={() => setActiveTab('history')} className={`flex flex-col items-center gap-1 ${activeTab === 'history' ? 'text-indigo-600' : 'text-slate-300'}`}>
          <History size={20} /><span className="text-[9px] font-black uppercase">History</span>
        </button>
      </nav>
    </div>
  );
};

export default App;
