import React, { useState, useMemo } from 'react';
import { PlusCircle, History, LayoutDashboard, Package, Search, ArrowRightLeft, ArrowRight, ArrowUp, Calendar, LogIn, LogOut, User } from 'lucide-react';

const App = () => {
  const [user, setUser] = useState(null);
  const [loginEmail, setLoginEmail] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [loginError, setLoginError] = useState('');
  
  const [activeTab, setActiveTab] = useState('summary');
  const [searchTerm, setSearchTerm] = useState('');

  // Authorized Users
  const authorizedUsers = [
    { email: 'damith@deluxedept.com', password: 'Augusto1901' },
    { email: 'eddie@deluxedept.com', password: 'Augusto1901' },
    { email: 'abby@deluxedept.com', password: 'Augusto1901' }
  ];

  // Item List (English)
  const initialItems = [
    // --- FG (Finished Goods) ---
    { id: 1021, name: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', category: 'FG' },
    { id: 104, name: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', category: 'FG' },
    { id: 106, name: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', category: 'FG' },
    { id: 109, name: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', category: 'FG' },
    { id: 110, name: 'Augusto VIP Giftbox w/ 2 Glasses', category: 'FG' },
    { id: 111, name: 'Augusto Reposado Giftbox w/ 2 Glasses', category: 'FG' },
    
    // --- POSM ---
    { id: 17, name: 'SDM Asia Black Cap', category: 'POSM' },
    { id: 25, name: 'Small Pouch', category: 'POSM' },
    { id: 28, name: 'Non-woven bag', category: 'POSM' },
    { id: 23, name: 'Augusto Tequila Shaker (Black)', category: 'POSM' },
    { id: 24, name: 'Augusto Tequila Shaker (Copper)', category: 'POSM' },
    { id: 29, name: 'Augusto Tequila Ice Bucket (UK Version)', category: 'POSM' },
    { id: 30, name: 'Augusto Tequila Ice Bucket (US Version)', category: 'POSM' },
    { id: 31, name: 'Augusto Tequila Glorifier (UK Version)', category: 'POSM' },
    { id: 32, name: 'Augusto Tequila Glorifier (US Version)', category: 'POSM' },
    { id: 33, name: 'Veyron Giftbox Blister', category: 'POSM' },
    { id: 401, name: 'Dali Technology Black Cigar Cutter', category: 'POSM' },
    { id: 402, name: 'Dali Technology Copper Cigar Cutter', category: 'POSM' },
    { id: 431, name: 'Zhongshan Ho Crafts Gold Pin', category: 'POSM' },
    { id: 432, name: 'Zhongshan Ho Crafts Silver Pin', category: 'POSM' },
    { id: 45, name: 'Augusto Crystal Cabalito', category: 'POSM' },

    // --- Accessories ---
    { id: 204, name: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', category: 'Accessories' },
    { id: 205, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
    { id: 206, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
    { id: 208, name: 'Augusto Neck Collar - Gold Medium Thread - Screw', category: 'Accessories' },
  ];

  // Transactions (Including initial balances)
  const [transactions, setTransactions] = useState([
    // --- San Tai ---
    { id: 'st1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' },
    { id: 'st2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 491, location: 'San Tai', user: 'System' },

    // --- Worldex ---
    { id: 'w1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
    { id: 'w2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto VIP Giftbox w/ 2 Glasses', amount: 294, location: 'Worldex', user: 'System' },
    { id: 'w3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Reposado Giftbox w/ 2 Glasses', amount: 162, location: 'Worldex', user: 'System' },
    { id: 'w4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 54, location: 'Worldex', user: 'System' },
    { id: 'w5', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 156, location: 'Worldex', user: 'System' },
    { id: 'w6', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 36, location: 'Worldex', user: 'System' },
    { id: 'w7', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Non-woven bag', amount: 1050, location: 'Worldex', user: 'System' },
    { id: 'w8', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Stopper', amount: 1320, location: 'Worldex', user: 'System' },
    { id: 'w9', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 141, location: 'Worldex', user: 'System' },
    { id: 'w10', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 117, location: 'Worldex', user: 'System' },
    { id: 'w11', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Ice Bucket (UK Version)', amount: 26, location: 'Worldex', user: 'System' },
    { id: 'w12', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Ice Bucket (US Version)', amount: 16, location: 'Worldex', user: 'System' },
    { id: 'w13', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Glorifier (UK Version)', amount: 14, location: 'Worldex', user: 'System' },
    { id: 'w14', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Glorifier (US Version)', amount: 19, location: 'Worldex', user: 'System' },
    { id: 'w15', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Veyron Giftbox Blister', amount: 2, location: 'Worldex', user: 'System' },

    // --- Office (Corrected Figures) ---
    { id: 'o1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 4, location: 'Office', user: 'System' },
    { id: 'o2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 2, location: 'Office', user: 'System' },
    { id: 'o3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 23, location: 'Office', user: 'System' },
    { id: 'o4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 21, location: 'Office', user: 'System' },
    { id: 'o5', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Black Cigar Cutter', amount: 98, location: 'Office', user: 'System' },
    { id: 'o6', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Copper Cigar Cutter', amount: 102, location: 'Office', user: 'System' },
    { id: 'o7', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Zhongshan Ho Crafts Gold Pin', amount: 8, location: 'Office', user: 'System' },
    { id: 'o8', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Zhongshan Ho Crafts Silver Pin', amount: 182, location: 'Office', user: 'System' },
    { id: 'o9', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Small Pouch', amount: 797, location: 'Office', user: 'System' },
    { id: 'o10', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Crystal Cabalito', amount: 3, location: 'Office', user: 'System' },
    { id: 'o11', date: '2026-04-09', activity: 'Initial Balance', itemName: 'SDM Asia Black Cap', amount: 29, location: 'Office', user: 'System' },
    { id: 'o12', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
    { id: 'o13', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 13, location: 'Office', user: 'System' },
    { id: 'o14', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', amount: 2448, location: 'Office', user: 'System' },
    { id: 'o15', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Neck Collar - Gold Medium Thread - Screw', amount: 348, location: 'Office', user: 'System' },
    { id: 'o16', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Triangle', amount: 728, location: 'Office', user: 'System' },
  ]);

  const stockSummary = useMemo(() => {
    const summary = {};
    initialItems.forEach(item => { 
      summary[item.name] = { total: 0, office: 0, worldex: 0, sanTai: 0 }; 
    });
    
    transactions.forEach(tx => {
      if (summary[tx.itemName]) {
        summary[tx.itemName].total += tx.amount;
        if (tx.location === 'Worldex') summary[tx.itemName].worldex += tx.amount;
        else if (tx.location === 'San Tai') summary[tx.itemName].sanTai += tx.amount;
        else if (tx.location === 'Office') summary[tx.itemName].office += tx.amount;
      }
    });
    return summary;
  }, [transactions, initialItems]);

  const [formMode, setFormMode] = useState('inout'); 
  const [formData, setFormData] = useState({
    activity: '',
    itemName: initialItems[0].name,
    amount: '',
    location: 'Office',
    fromLocation: 'Worldex',
    toLocation: 'Office'
  });

  const handleLogin = (e) => {
    e.preventDefault();
    const found = authorizedUsers.find(u => u.email === loginEmail && u.password === loginPassword);
    if (found) {
      setUser(found.email);
      setLoginError('');
    } else {
      setLoginError('Invalid email or password');
    }
  };

  const handleAddTransaction = (e) => {
    e.preventDefault();
    const now = new Date().toISOString().split('T')[0];
    const amount = parseInt(formData.amount);
    if (!amount || isNaN(amount)) return;

    if (formMode === 'transfer') {
      const txFrom = {
        id: `tf-${Date.now()}-out`,
        date: now,
        activity: `Transfer Out (To ${formData.toLocation})`,
        itemName: formData.itemName,
        amount: -amount,
        location: formData.fromLocation,
        user: user
      };
      const txTo = {
        id: `tf-${Date.now()}-in`,
        date: now,
        activity: `Transfer In (From ${formData.fromLocation})`,
        itemName: formData.itemName,
        amount: amount,
        location: formData.toLocation,
        user: user
      };
      setTransactions([txFrom, txTo, ...transactions]);
    } else {
      const newTx = {
        id: Date.now(),
        date: now,
        activity: formData.activity || (amount > 0 ? 'Stock In' : 'Stock Out'),
        itemName: formData.itemName,
        amount: amount,
        location: formData.location,
        user: user
      };
      setTransactions([newTx, ...transactions]);
    }

    setFormData({ ...formData, activity: '', amount: '' });
    setActiveTab('history');
  };

  if (!user) {
    return (
      <div className="min-h-screen bg-indigo-900 flex items-center justify-center p-6">
        <div className="bg-white rounded-3xl shadow-2xl w-full max-w-sm p-8 space-y-6">
          <div className="text-center space-y-2">
            <div className="inline-flex p-4 bg-indigo-100 rounded-2xl text-indigo-600 mb-2">
              <Package size={32} />
            </div>
            <h1 className="text-2xl font-black text-slate-800">Augusto Stock</h1>
            <p className="text-slate-400 text-sm">Please sign in to continue</p>
          </div>
          
          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <input 
                type="email" 
                placeholder="Email Address" 
                className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-sm"
                value={loginEmail}
                onChange={e => setLoginEmail(e.target.value)}
                required
              />
            </div>
            <div>
              <input 
                type="password" 
                placeholder="Password" 
                className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-sm"
                value={loginPassword}
                onChange={e => setLoginPassword(e.target.value)}
                required
              />
            </div>
            {loginError && <p className="text-rose-500 text-xs font-bold text-center">{loginError}</p>}
            <button type="submit" className="w-full bg-indigo-600 text-white font-bold py-4 rounded-2xl shadow-lg hover:bg-indigo-700 active:scale-95 transition">
              Sign In
            </button>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans pb-24 text-slate-900 leading-relaxed">
      {/* Header */}
      <div className="bg-indigo-700 text-white p-5 shadow-lg sticky top-0 z-30 flex justify-between items-center">
        <h1 className="text-xl font-bold flex items-center gap-2">
          <Package size={24} /> Augusto
        </h1>
        <div className="flex items-center gap-4">
          <div className="text-[10px] text-right hidden sm:block">
            <div className="font-bold opacity-60 uppercase">Signed in as</div>
            <div className="font-mono">{user}</div>
          </div>
          <button onClick={() => setUser(null)} className="p-2 bg-white/10 rounded-lg hover:bg-white/20 transition">
            <LogOut size={18} />
          </button>
        </div>
      </div>

      <main className="flex-1 p-4 max-w-2xl mx-auto w-full">
        {activeTab === 'summary' && (
          <div className="space-y-6 animate-in fade-in duration-300">
            <div className="flex items-center justify-between">
              <h2 className="text-lg font-extrabold text-indigo-900">Inventory Overview</h2>
              <div className="relative">
                <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                <input 
                  type="text" 
                  placeholder="Search..." 
                  className="pl-9 pr-4 py-2 border border-slate-200 rounded-full bg-white text-xs w-32 focus:ring-2 focus:ring-indigo-500 outline-none shadow-sm transition-all focus:w-48"
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
            </div>

            {['FG', 'POSM', 'Accessories'].map(cat => {
              const items = initialItems.filter(i => 
                i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase())
              );
              if (items.length === 0) return null;

              return (
                <div key={cat} className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                  <div className="bg-slate-50 px-4 py-2 font-bold text-slate-500 text-[10px] uppercase tracking-widest border-b border-slate-100 flex justify-between">
                    <span>{cat === 'FG' ? 'Finished Goods' : cat === 'POSM' ? 'POSM' : 'Accessories'}</span>
                    <span>Total / Distribution</span>
                  </div>
                  <div className="divide-y divide-slate-100">
                    {items.map(item => {
                      const data = stockSummary[item.name];
                      return (
                        <div key={item.id} className="p-4 hover:bg-slate-50/50 transition">
                          <div className="flex justify-between items-start mb-2">
                            <span className="text-sm font-bold text-slate-800 leading-tight flex-1 pr-4">{item.name}</span>
                            <span className={`font-mono font-black text-lg ${data.total === 0 ? 'text-slate-300' : 'text-indigo-600'}`}>
                              {data.total}
                            </span>
                          </div>
                          <div className="flex flex-wrap gap-2 text-[10px] font-bold">
                            <span className={`px-2 py-1 rounded border ${data.office > 0 ? 'bg-blue-50 text-blue-600 border-blue-100' : 'bg-slate-50 text-slate-300 border-slate-100'}`}>Office: {data.office}</span>
                            <span className={`px-2 py-1 rounded border ${data.worldex > 0 ? 'bg-amber-50 text-amber-600 border-amber-100' : 'bg-slate-50 text-slate-300 border-slate-100'}`}>Worldex: {data.worldex}</span>
                            <span className={`px-2 py-1 rounded border ${data.sanTai > 0 ? 'bg-emerald-50 text-emerald-600 border-emerald-100' : 'bg-slate-50 text-slate-300 border-slate-100'}`}>San Tai: {data.sanTai}</span>
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
          <div className="space-y-4 animate-in slide-in-from-bottom-4 duration-300">
             <div className="flex bg-white p-1 rounded-2xl shadow-sm border border-slate-200">
              <button onClick={() => setFormMode('inout')} className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-xs font-bold transition ${formMode === 'inout' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400'}`}>
                <ArrowUp size={14} /> In / Out
              </button>
              <button onClick={() => setFormMode('transfer')} className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-xs font-bold transition ${formMode === 'transfer' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400'}`}>
                <ArrowRightLeft size={14} /> Warehouse Transfer
              </button>
            </div>

            <form onSubmit={handleAddTransaction} className="bg-white p-6 rounded-3xl shadow-xl space-y-5 border border-slate-100">
              {formMode === 'transfer' ? (
                <div className="grid grid-cols-7 gap-2 items-center bg-slate-50 p-4 rounded-2xl border border-dashed border-slate-200">
                  <div className="col-span-3 text-center">
                    <label className="block text-[10px] font-bold text-slate-400 uppercase mb-1">From</label>
                    <select className="w-full p-2 bg-white border border-slate-200 rounded-lg text-xs font-bold shadow-sm" value={formData.fromLocation} onChange={e => setFormData({...formData, fromLocation: e.target.value})}>
                      {['Office', 'Worldex', 'San Tai'].map(loc => <option key={loc} value={loc} disabled={loc === formData.toLocation}>{loc}</option>)}
                    </select>
                  </div>
                  <div className="col-span-1 flex justify-center text-indigo-400"><ArrowRight size={20} /></div>
                  <div className="col-span-3 text-center">
                    <label className="block text-[10px] font-bold text-slate-400 uppercase mb-1">To</label>
                    <select className="w-full p-2 bg-white border border-slate-200 rounded-lg text-xs font-bold shadow-sm" value={formData.toLocation} onChange={e => setFormData({...formData, toLocation: e.target.value})}>
                      {['Office', 'Worldex', 'San Tai'].map(loc => <option key={loc} value={loc} disabled={loc === formData.fromLocation}>{loc}</option>)}
                    </select>
                  </div>
                </div>
              ) : (
                <div className="flex gap-2 text-center">
                  {['Office', 'Worldex', 'San Tai'].map(loc => (
                    <button key={loc} type="button" onClick={() => setFormData({...formData, location: loc})} className={`flex-1 py-3 rounded-xl text-xs font-bold transition ${formData.location === loc ? 'bg-indigo-600 text-white shadow-md' : 'bg-slate-100 text-slate-400'}`}>{loc}</button>
                  ))}
                </div>
              )}

              <div>
                <label className="block text-[11px] font-bold text-slate-400 uppercase mb-2">Item Name</label>
                <select className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm outline-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                  {['FG', 'POSM', 'Accessories'].map(category => (
                    <optgroup key={category} label={category} className="font-bold text-indigo-600">
                      {initialItems.filter(item => item.category === category).map(item => <option key={item.id} value={item.name}>{item.name}</option>)}
                    </optgroup>
                  ))}
                </select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className={formMode === 'transfer' ? 'col-span-2' : 'col-span-1'}>
                  <label className="block text-[11px] font-bold text-slate-400 uppercase mb-2">Quantity</label>
                  <input type="number" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl font-mono text-xl outline-none" placeholder="0" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required />
                </div>
                {formMode === 'inout' && (
                  <div className="col-span-1">
                    <label className="block text-[11px] font-bold text-slate-400 uppercase mb-2">Note / Reason</label>
                    <input type="text" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm outline-none" placeholder="Refill / Sale" value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                  </div>
                )}
              </div>

              <button type="submit" className="w-full bg-indigo-600 text-white font-bold py-4 rounded-2xl shadow-lg active:scale-95 transition">Submit Record</button>
            </form>
          </div>
        )}

        {activeTab === 'history' && (
          <div className="space-y-4 animate-in fade-in duration-300">
            <h2 className="text-lg font-extrabold text-indigo-900 flex items-center gap-2"><History size={18} /> Transaction Logs</h2>
            <div className="space-y-3">
              {transactions.map(tx => (
                <div key={tx.id} className="bg-white p-4 rounded-2xl shadow-sm border border-slate-200 flex flex-col gap-2 relative overflow-hidden">
                  <div className="flex justify-between items-center">
                    <div className="flex items-center gap-2">
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${
                        tx.location === 'Worldex' ? 'bg-amber-100 text-amber-600' : 
                        tx.location === 'San Tai' ? 'bg-emerald-100 text-emerald-600' : 'bg-blue-100 text-blue-600'
                      }`}>{tx.location}</span>
                      <span className="text-[10px] text-slate-400 font-medium"><Calendar size={10} className="inline mr-1" />{tx.date}</span>
                    </div>
                    <div className={`font-mono font-black text-sm ${tx.amount > 0 ? 'text-emerald-600' : 'text-rose-600'}`}>{tx.amount > 0 ? '+' : ''}{tx.amount}</div>
                  </div>
                  <div className="flex justify-between items-end">
                    <div>
                      <div className="font-bold text-slate-800 text-sm leading-tight">{tx.activity}</div>
                      <div className="text-[11px] text-slate-500 font-medium mt-1">{tx.itemName}</div>
                    </div>
                    <div className="flex items-center gap-1 text-[9px] bg-slate-50 px-2 py-1 rounded-md text-slate-400 font-bold border border-slate-100">
                      <User size={10} /> {tx.user}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      {/* Nav */}
      <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 flex justify-around p-3 shadow-2xl z-40">
        <button onClick={() => setActiveTab('summary')} className={`flex flex-col items-center gap-1 ${activeTab === 'summary' ? 'text-indigo-600' : 'text-slate-400'}`}>
          <LayoutDashboard size={20} /><span className="text-[9px] font-bold">Summary</span>
        </button>
        <button onClick={() => setActiveTab('add')} className="relative -mt-10">
          <div className="p-4 rounded-full bg-indigo-600 text-white shadow-xl ring-4 ring-white"><PlusCircle size={28} /></div>
        </button>
        <button onClick={() => setActiveTab('history')} className={`flex flex-col items-center gap-1 ${activeTab === 'history' ? 'text-indigo-600' : 'text-slate-400'}`}>
          <History size={20} /><span className="text-[9px] font-bold">Logs</span>
        </button>
      </nav>
    </div>
  );
};

export default App;
