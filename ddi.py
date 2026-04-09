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

  // Data synchronized from uploaded screenshots
  const initialItems = [
    // --- FG (Finished Goods) ---
    { id: 101, name: 'Cofradia - Augusto Reposado Full - in Cartons of 6 w/Hex Giftbox', category: 'FG' },
    { id: 102, name: 'Cofradia - Augusto Reposado Full - w/Hex Giftbox', category: 'FG' },
    { id: 103, name: 'Cofradia - Augusto Reposado Full - Sample Use Only', category: 'FG' },
    { id: 104, name: 'Cofradia - Augusto Reposado Full - in YOS Giftbox', category: 'FG' },
    { id: 105, name: 'Tres Mujeres - Augusto Reposado Bottle 750ml - Hong Kong - in small cartons of 6 bottle', category: 'FG' },
    { id: 106, name: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8% - Hong Kong', category: 'FG' },
    { id: 107, name: 'Tres Mujeres - Augusto Reposado Joven 750ml - Hong Kong - in small cartons of 6 bottle', category: 'FG' },
    { id: 108, name: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8% - Hong Kong', category: 'FG' },
    { id: 109, name: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', category: 'FG' },
    { id: 110, name: 'Augusto VIP Giftbox w/2 Glasses - Cofradia May \'24', category: 'FG' },
    { id: 111, name: 'Augusto Reposado Giftbox w/2 Glasses', category: 'FG' },

    // --- POSM ---
    { id: 201, name: 'SDM Asia Green T-shirt Size S/M/L/XL', category: 'POSM' },
    { id: 202, name: 'SDM Asia Black T-shirt Size S/M/L/XL', category: 'POSM' },
    { id: 203, name: 'SDM Asia Green Hoodie Size S/M/L/XL', category: 'POSM' },
    { id: 204, name: 'SDM Asia Grey Hoodie Size S/M/L/XL', category: 'POSM' },
    { id: 205, name: 'SDM Asia Black Cap', category: 'POSM' },
    { id: 206, name: 'SDM Asia Purple Cap', category: 'POSM' },
    { id: 207, name: 'Zhongshan Ho Crafts And Gifts Co Gold Pin', category: 'POSM' },
    { id: 208, name: 'Zhongshan Ho Crafts And Gifts Co Silver Pin', category: 'POSM' },
    { id: 209, name: 'Dali Technology Black Cigar Cutter', category: 'POSM' },
    { id: 210, name: 'Dali Technology Copper Cigar Cutter', category: 'POSM' },
    { id: 211, name: 'Bingyi Industrial Black Shaker 700ml', category: 'POSM' },
    { id: 212, name: 'Bingyi Industrial Copper Shaker 700ml', category: 'POSM' },
    { id: 213, name: 'Augusto Tequila Ice Bucket UK Version', category: 'POSM' },
    { id: 214, name: 'Augusto Tequila Ice Bucket US Version', category: 'POSM' },
    { id: 215, name: 'Augusto Tequila Glorifier UK Version', category: 'POSM' },
    { id: 216, name: 'Augusto Tequila Glorifier US Version', category: 'POSM' },
    { id: 217, name: 'Small Pouch', category: 'POSM' },
    { id: 218, name: 'Non-woven bag', category: 'POSM' },
    { id: 219, name: 'Augusto Crystal Cabalito', category: 'POSM' },
    { id: 220, name: 'Veyron Giftbox Blister', category: 'POSM' },

    // --- Accessories ---
    { id: 301, name: 'Augusto Tequila Joven - Silver Neck Collar-Small', category: 'Accessories' },
    { id: 302, name: 'Augusto Tequila Joven - Silver Stopper', category: 'Accessories' },
    { id: 303, name: 'Augusto Tequila Joven - Silver Triangle', category: 'Accessories' },
    { id: 304, name: 'Augusto Tequila Reposado - Gold Neck Collar-Small', category: 'Accessories' },
    { id: 305, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
    { id: 306, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
    { id: 307, name: 'Augusto Neck Collar - Gold Medium Thread', category: 'Accessories' },
  ];

  const [transactions, setTransactions] = useState([
    // --- Office Initial (From Screenshot 2, 4, 5) ---
    { id: 'o1', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Crystal Cabalito', amount: 3, location: 'Office', user: 'System' },
    { id: 'o2', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Bingyi Industrial Black Shaker 700ml', amount: 23, location: 'Office', user: 'System' },
    { id: 'o3', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Bingyi Industrial Copper Shaker 700ml', amount: 21, location: 'Office', user: 'System' },
    { id: 'o4', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Dali Technology Black Cigar Cutter', amount: 98, location: 'Office', user: 'System' },
    { id: 'o5', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Dali Technology Copper Cigar Cutter', amount: 102, location: 'Office', user: 'System' },
    { id: 'o6', date: '2026-04-09', activity: 'Balance Forward', itemName: 'SDM Asia Black Cap', amount: 29, location: 'Office', user: 'System' },
    { id: 'o7', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Small Pouch', amount: 797, location: 'Office', user: 'System' },
    { id: 'o8', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Zhongshan Ho Crafts And Gifts Co Gold Pin', amount: 8, location: 'Office', user: 'System' },
    { id: 'o9', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Zhongshan Ho Crafts And Gifts Co Silver Pin', amount: 182, location: 'Office', user: 'System' },
    { id: 'o10', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Cofradia - Augusto Reposado Full - w/Hex Giftbox', amount: 4, location: 'Office', user: 'System' },
    { id: 'o11', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Cofradia - Augusto Reposado Full - in YOS Giftbox', amount: 2, location: 'Office', user: 'System' },
    { id: 'o12', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8% - Hong Kong', amount: 13, location: 'Office', user: 'System' },
    { id: 'o13', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8% - Hong Kong', amount: 17, location: 'Office', user: 'System' },
    { id: 'o14', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Reposado - Gold Neck Collar-Small', amount: 2448, location: 'Office', user: 'System' },
    { id: 'o15', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Neck Collar - Gold Medium Thread', amount: 348, location: 'Office', user: 'System' },
    { id: 'o16', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Reposado - Gold Triangle', amount: 728, location: 'Office', user: 'System' },

    // --- Worldex Initial (From Screenshot 8) ---
    { id: 'w1', date: '2026-04-09', activity: 'Balance Forward', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },
    { id: 'w2', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto VIP Giftbox w/2 Glasses - Cofradia May \'24', amount: 294, location: 'Worldex', user: 'System' },
    { id: 'w3', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Reposado Giftbox w/2 Glasses', amount: 162, location: 'Worldex', user: 'System' },
    { id: 'w4', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Cofradia - Augusto Reposado Full - in YOS Giftbox', amount: 54, location: 'Worldex', user: 'System' },
    { id: 'w5', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8% - Hong Kong', amount: 36, location: 'Worldex', user: 'System' },
    { id: 'w6', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8% - Hong Kong', amount: 156, location: 'Worldex', user: 'System' },
    { id: 'w7', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Non-woven bag', amount: 1050, location: 'Worldex', user: 'System' },
    { id: 'w8', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Reposado - Gold Stopper', amount: 1320, location: 'Worldex', user: 'System' },
    { id: 'w9', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Ice Bucket UK Version', amount: 26, location: 'Worldex', user: 'System' },
    { id: 'w10', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Ice Bucket US Version', amount: 16, location: 'Worldex', user: 'System' },
    { id: 'w11', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Glorifier UK Version', amount: 14, location: 'Worldex', user: 'System' },
    { id: 'w12', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Augusto Tequila Glorifier US Version', amount: 19, location: 'Worldex', user: 'System' },
    { id: 'w13', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Bingyi Industrial Black Shaker 700ml', amount: 141, location: 'Worldex', user: 'System' },
    { id: 'w14', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Bingyi Industrial Copper Shaker 700ml', amount: 117, location: 'Worldex', user: 'System' },
    { id: 'w15', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Veyron Giftbox Blister', amount: 2, location: 'Worldex', user: 'System' },

    // --- San Tai Initial (From Screenshot 9) ---
    { id: 'st1', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8% - Hong Kong', amount: 1198, location: 'San Tai', user: 'System' },
    { id: 'st2', date: '2026-04-09', activity: 'Balance Forward', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8% - Hong Kong', amount: 491, location: 'San Tai', user: 'System' },
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
  }, [transactions, initialItems]);

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
      <div className="min-h-screen bg-slate-900 flex items-center justify-center p-6">
        <div className="bg-white rounded-3xl shadow-2xl w-full max-w-sm p-8 space-y-6">
          <div className="text-center">
            <div className="inline-flex p-4 bg-indigo-50 rounded-2xl text-indigo-600 mb-4"><Package size={40} /></div>
            <h1 className="text-2xl font-black text-slate-800">Augusto Stock</h1>
            <p className="text-slate-400 text-sm mt-1">Inventory Management System</p>
          </div>
          <form onSubmit={handleLogin} className="space-y-4">
            <input type="email" placeholder="Email Address" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-sm" value={loginEmail} onChange={e => setLoginEmail(e.target.value)} required />
            <input type="password" placeholder="Password" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-sm" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
            {loginError && <p className="text-rose-500 text-xs font-bold text-center">{loginError}</p>}
            <button type="submit" className="w-full bg-indigo-600 text-white font-bold py-4 rounded-2xl shadow-lg hover:bg-indigo-700 active:scale-95 transition">Sign In</button>
          </form>
          <div className="pt-4 border-t border-slate-100 text-[10px] text-slate-400 text-center uppercase tracking-widest font-bold">Internal Use Only</div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col pb-24 text-slate-900">
      <header className="bg-indigo-700 text-white p-5 shadow-lg sticky top-0 z-30 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <Package size={22} className="text-indigo-200" />
          <h1 className="text-lg font-black tracking-tight">Augusto</h1>
        </div>
        <div className="flex items-center gap-4">
          <div className="text-right hidden sm:block">
            <div className="text-[9px] font-bold opacity-60 uppercase">User</div>
            <div className="text-xs font-mono font-bold">{user}</div>
          </div>
          <button onClick={() => setUser(null)} className="p-2 bg-white/10 rounded-xl hover:bg-white/20 transition"><LogOut size={18} /></button>
        </div>
      </header>

      <main className="flex-1 p-4 max-w-2xl mx-auto w-full">
        {activeTab === 'summary' && (
          <div className="space-y-6 animate-in fade-in duration-300">
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-black text-slate-800">Inventory</h2>
              <div className="relative">
                <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                <input type="text" placeholder="Search items..." className="pl-9 pr-4 py-2 border border-slate-200 rounded-full bg-white text-xs w-36 focus:ring-2 focus:ring-indigo-500 outline-none shadow-sm transition-all focus:w-48" onChange={(e) => setSearchTerm(e.target.value)} />
              </div>
            </div>

            {['FG', 'POSM', 'Accessories'].map(cat => {
              const items = initialItems.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
              if (items.length === 0) return null;
              return (
                <div key={cat} className="bg-white rounded-3xl shadow-sm border border-slate-200 overflow-hidden">
                  <div className="bg-slate-50 px-5 py-3 font-black text-slate-400 text-[10px] uppercase tracking-[0.2em] border-b border-slate-100 flex justify-between">
                    <span>{cat === 'FG' ? 'Finished Goods' : cat === 'POSM' ? 'POSM' : 'Accessories'}</span>
                    <span>Stock Levels</span>
                  </div>
                  <div className="divide-y divide-slate-50">
                    {items.map(item => {
                      const data = stockSummary[item.name];
                      return (
                        <div key={item.id} className="p-5 hover:bg-slate-50/50 transition">
                          <div className="flex justify-between items-start mb-3">
                            <span className="text-sm font-bold text-slate-800 leading-snug flex-1 pr-6">{item.name}</span>
                            <span className={`font-mono font-black text-xl ${data.total <= 0 ? 'text-slate-300' : 'text-indigo-600'}`}>{data.total}</span>
                          </div>
                          <div className="flex flex-wrap gap-2">
                            {['Office', 'Worldex', 'San Tai'].map(loc => {
                              const val = data[loc.toLowerCase().replace(' ', 'T')];
                              return (
                                <div key={loc} className={`px-2.5 py-1 rounded-lg text-[10px] font-bold border ${val > 0 ? 'bg-indigo-50 border-indigo-100 text-indigo-600' : 'bg-slate-50 border-slate-100 text-slate-300'}`}>
                                  {loc}: {val}
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
          <div className="space-y-4 animate-in slide-in-from-bottom-4 duration-300">
            <div className="flex bg-white p-1.5 rounded-2xl shadow-sm border border-slate-200">
              <button onClick={() => setFormMode('inout')} className={`flex-1 flex items-center justify-center gap-2 py-3.5 rounded-xl text-xs font-black transition-all ${formMode === 'inout' ? 'bg-indigo-600 text-white shadow-lg' : 'text-slate-400 hover:bg-slate-50'}`}>
                <ArrowUp size={14} /> IN / OUT
              </button>
              <button onClick={() => setFormMode('transfer')} className={`flex-1 flex items-center justify-center gap-2 py-3.5 rounded-xl text-xs font-black transition-all ${formMode === 'transfer' ? 'bg-indigo-600 text-white shadow-lg' : 'text-slate-400 hover:bg-slate-50'}`}>
                <ArrowRightLeft size={14} /> TRANSFER
              </button>
            </div>

            <form onSubmit={handleAddTransaction} className="bg-white p-8 rounded-[2rem] shadow-xl space-y-6 border border-slate-100">
              {formMode === 'transfer' ? (
                <div className="flex items-center gap-3 bg-slate-50 p-4 rounded-2xl border border-slate-100">
                  <div className="flex-1">
                    <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1 tracking-wider text-center">Source</label>
                    <select className="w-full p-3 bg-white border border-slate-200 rounded-xl text-xs font-bold" value={formData.fromLocation} onChange={e => setFormData({...formData, fromLocation: e.target.value})}>
                      {['Office', 'Worldex', 'San Tai'].map(loc => <option key={loc} value={loc}>{loc}</option>)}
                    </select>
                  </div>
                  <ArrowRight className="text-indigo-400 mt-5" size={20} />
                  <div className="flex-1">
                    <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1 tracking-wider text-center">Destination</label>
                    <select className="w-full p-3 bg-white border border-slate-200 rounded-xl text-xs font-bold" value={formData.toLocation} onChange={e => setFormData({...formData, toLocation: e.target.value})}>
                      {['Office', 'Worldex', 'San Tai'].map(loc => <option key={loc} value={loc}>{loc}</option>)}
                    </select>
                  </div>
                </div>
              ) : (
                <div className="grid grid-cols-3 gap-2">
                  {['Office', 'Worldex', 'San Tai'].map(loc => (
                    <button key={loc} type="button" onClick={() => setFormData({...formData, location: loc})} className={`py-3.5 rounded-xl text-[10px] font-black transition-all border ${formData.location === loc ? 'bg-indigo-600 text-white border-indigo-600 shadow-md' : 'bg-white text-slate-400 border-slate-200 hover:border-indigo-300'}`}>{loc.toUpperCase()}</button>
                  ))}
                </div>
              )}

              <div>
                <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1 tracking-wider">Select Item</label>
                <select className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl text-sm font-medium outline-none focus:ring-2 focus:ring-indigo-500 appearance-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                  {['FG', 'POSM', 'Accessories'].map(cat => (
                    <optgroup key={cat} label={cat} className="font-bold">
                      {initialItems.filter(i => i.category === cat).map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                    </optgroup>
                  ))}
                </select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className={formMode === 'transfer' ? 'col-span-2' : 'col-span-1'}>
                  <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1 tracking-wider">Quantity</label>
                  <input type="number" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl font-mono text-2xl font-black outline-none focus:ring-2 focus:ring-indigo-500" placeholder="0" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required />
                </div>
                {formMode === 'inout' && (
                  <div className="col-span-1">
                    <label className="block text-[10px] font-bold text-slate-400 uppercase mb-2 ml-1 tracking-wider">Note</label>
                    <input type="text" className="w-full p-4 bg-slate-50 border border-slate-200 rounded-2xl text-sm outline-none focus:ring-2 focus:ring-indigo-500" placeholder="e.g. Sale" value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                  </div>
                )}
              </div>

              <button type="submit" className="w-full bg-indigo-600 text-white font-black py-4.5 rounded-2xl shadow-xl shadow-indigo-100 hover:bg-indigo-700 active:scale-[0.98] transition-all tracking-widest text-sm">UPDATE INVENTORY</button>
            </form>
          </div>
        )}

        {activeTab === 'history' && (
          <div className="space-y-4 animate-in fade-in duration-300">
            <h2 className="text-xl font-black text-slate-800">History Logs</h2>
            <div className="space-y-3">
              {transactions.map(tx => (
                <div key={tx.id} className="bg-white p-5 rounded-3xl shadow-sm border border-slate-200 hover:border-indigo-200 transition">
                  <div className="flex justify-between items-center mb-2">
                    <div className="flex items-center gap-2">
                      <span className={`px-2 py-0.5 rounded-lg text-[9px] font-black uppercase tracking-wider ${tx.location === 'Worldex' ? 'bg-amber-100 text-amber-700' : tx.location === 'San Tai' ? 'bg-emerald-100 text-emerald-700' : 'bg-blue-100 text-blue-700'}`}>{tx.location}</span>
                      <span className="text-[10px] text-slate-400 font-bold"><Calendar size={10} className="inline mr-1" />{tx.date}</span>
                    </div>
                    <div className={`font-mono font-black text-sm ${tx.amount > 0 ? 'text-emerald-600' : 'text-rose-600'}`}>{tx.amount > 0 ? '+' : ''}{tx.amount}</div>
                  </div>
                  <div className="flex justify-between items-end">
                    <div>
                      <div className="font-bold text-slate-800 text-sm">{tx.activity}</div>
                      <div className="text-[11px] text-slate-500 font-medium mt-1 leading-tight">{tx.itemName}</div>
                    </div>
                    <div className="flex items-center gap-1.5 text-[9px] bg-slate-50 px-2.5 py-1.5 rounded-xl text-slate-400 font-black border border-slate-100">
                      <User size={10} /> {tx.user.split('@')[0].toUpperCase()}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <nav className="fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-md border-t border-slate-200 flex justify-around p-4 shadow-2xl z-40 pb-8">
        <button onClick={() => setActiveTab('summary')} className={`flex flex-col items-center gap-1.5 transition-all ${activeTab === 'summary' ? 'text-indigo-600 scale-110' : 'text-slate-300'}`}>
          <LayoutDashboard size={20} /><span className="text-[9px] font-black uppercase tracking-tighter">Stock</span>
        </button>
        <button onClick={() => setActiveTab('add')} className="relative -mt-12">
          <div className="p-5 rounded-full bg-indigo-600 text-white shadow-2xl ring-8 ring-slate-50 shadow-indigo-200 active:scale-90 transition-all">
            <PlusCircle size={30} />
          </div>
        </button>
        <button onClick={() => setActiveTab('history')} className={`flex flex-col items-center gap-1.5 transition-all ${activeTab === 'history' ? 'text-indigo-600 scale-110' : 'text-slate-300'}`}>
          <History size={20} /><span className="text-[9px] font-black uppercase tracking-tighter">Logs</span>
        </button>
      </nav>
    </div>
  );
};

export default App;
