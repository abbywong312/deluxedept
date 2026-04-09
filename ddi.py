import React, { useState, useMemo } from 'react';
import { PlusCircle, History, LayoutDashboard, Package, Search, ArrowRight, LogOut, Plus } from 'lucide-react';

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

  // 1. EXACT ITEM DEFINITIONS (25 Items)
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
    { id: 207, name: 'Non-woven bag', category: 'POSM' },
    { id: 208, name: 'Augusto Tequila Ice Bucket UK Version', category: 'POSM' },
    { id: 209, name: 'Augusto Tequila Ice Bucket US Version', category: 'POSM' },
    { id: 210, name: 'Augusto Tequila Glorifier UK Version', category: 'POSM' },
    { id: 211, name: 'Augusto Tequila Glorifier US Version', category: 'POSM' },
    { id: 212, name: 'Zhongshan Ho Crafts Gold Pin', category: 'POSM' },
    { id: 213, name: 'Zhongshan Ho Crafts Silver Pin', category: 'POSM' },
    { id: 214, name: 'Augusto Crystal Cabalito', category: 'POSM' },
    { id: 215, name: 'Veyron Giftbox Blister', category: 'POSM' },
    { id: 301, name: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', category: 'Accessories' },
    { id: 302, name: 'Augusto Tequila Reposado - Gold Stopper', category: 'Accessories' },
    { id: 303, name: 'Augusto Tequila Reposado - Gold Triangle', category: 'Accessories' },
    { id: 304, name: 'Augusto Neck Collar - Gold Medium Thread - Screw', category: 'Accessories' }
  ]);

  // 2. FULL RESTORED TRANSACTIONS (33 Records from all your instructions & screenshots)
  const [transactions, setTransactions] = useState([
    // Tres Mujeres Reposado
    { id: 't1', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 17, location: 'Office', user: 'System' },
    { id: 't2', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 156, location: 'Worldex', user: 'System' },
    { id: 't3', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Reposado Bottle 750ml 40.8%', amount: 1198, location: 'San Tai', user: 'System' },

    // Tres Mujeres Joven
    { id: 't4', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 13, location: 'Office', user: 'System' },
    { id: 't5', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 36, location: 'Worldex', user: 'System' },
    { id: 't6', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Tres Mujeres - Augusto Tequila Joven Bottle 750ml 40.8%', amount: 491, location: 'San Tai', user: 'System' },

    // LC Augusto Reposado (Hex)
    { id: 't7', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 4, location: 'Office', user: 'System' },
    { id: 't8', date: '2026-04-09', activity: 'Initial Balance', itemName: 'LC Augusto Reposado 750ml 40.8% w/ Hex Giftbox (Repackaged)', amount: 173, location: 'Worldex', user: 'System' },

    // Cofraida YOS
    { id: 't9', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 2, location: 'Office', user: 'System' },
    { id: 't10', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Cofraida - Augusto Reposado Full - in YOS Giftbox', amount: 54, location: 'Worldex', user: 'System' },

    // Giftboxes
    { id: 't11', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto VIP Giftbox w/2 Glasses', amount: 294, location: 'Worldex', user: 'System' },
    { id: 't12', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Reposado Giftbox w/2 Glasses', amount: 162, location: 'Worldex', user: 'System' },

    // Shakers
    { id: 't13', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 23, location: 'Office', user: 'System' },
    { id: 't14', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Black)', amount: 141, location: 'Worldex', user: 'System' },
    { id: 't15', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 21, location: 'Office', user: 'System' },
    { id: 't16', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Shaker (Copper)', amount: 117, location: 'Worldex', user: 'System' },

    // Cigar Cutters
    { id: 't17', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Black Cigar Cutter', amount: 98, location: 'Office', user: 'System' },
    { id: 't18', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Dali Technology Copper Cigar Cutter', amount: 102, location: 'Office', user: 'System' },

    // Pins
    { id: 't19', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Zhongshan Ho Crafts Gold Pin', amount: 8, location: 'Office', user: 'System' },
    { id: 't20', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Zhongshan Ho Crafts Silver Pin', amount: 182, location: 'Office', user: 'System' },

    // Bags & Pouches & Caps
    { id: 't21', date: '2026-04-09', activity: 'Initial Balance', itemName: 'SDM Asia Black Cap', amount: 29, location: 'Office', user: 'System' },
    { id: 't22', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Small Pouch', amount: 797, location: 'Office', user: 'System' },
    { id: 't23', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Non-woven bag', amount: 1050, location: 'Worldex', user: 'System' },

    // Bar Tools (Ice Buckets & Glorifiers)
    { id: 't24', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Ice Bucket UK Version', amount: 26, location: 'Worldex', user: 'System' },
    { id: 't25', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Ice Bucket US Version', amount: 16, location: 'Worldex', user: 'System' },
    { id: 't26', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Glorifier UK Version', amount: 14, location: 'Worldex', user: 'System' },
    { id: 't27', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Glorifier US Version', amount: 19, location: 'Worldex', user: 'System' },
    { id: 't28', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Crystal Cabalito', amount: 3, location: 'Office', user: 'System' },
    { id: 't29', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Veyron Giftbox Blister', amount: 2, location: 'Worldex', user: 'System' },

    // Accessories
    { id: 't30', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Neck Collar-Small - Screw', amount: 2448, location: 'Office', user: 'System' },
    { id: 't31', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Stopper', amount: 1320, location: 'Worldex', user: 'System' },
    { id: 't32', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Tequila Reposado - Gold Triangle', amount: 728, location: 'Office', user: 'System' },
    { id: 't33', date: '2026-04-09', activity: 'Initial Balance', itemName: 'Augusto Neck Collar - Gold Medium Thread - Screw', amount: 348, location: 'Office', user: 'System' },
  ]);

  // 3. Logic: Calculate Stock Totals
  const stockSummary = useMemo(() => {
    const summary = {};
    items.forEach(item => {
      summary[item.name.trim()] = { 
        total: 0, 
        details: { 'Office': 0, 'Worldex': 0, 'San Tai': 0 }, 
        category: item.category 
      };
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

  const handleAction = (e) => {
    e.preventDefault();
    const now = new Date().toISOString().split('T')[0];
    const qty = parseInt(formData.amount) || 0;
    const finalLocation = formData.location === 'Other' ? formData.customLocation : formData.location;

    if (formMode === 'newitem') {
        const name = formData.itemName.trim();
        if(!name) return;
        setItems(prev => [...prev, { id: Date.now(), name, category: formData.newCategory }]);
        if(qty !== 0) {
            setTransactions(prev => [{ id: Date.now(), date: now, activity: 'Initial Entry', itemName: name, amount: qty, location: finalLocation || 'Office', user: user }, ...prev]);
        }
    } else if (formMode === 'transfer') {
        setTransactions(prev => [
            { id: Date.now() + 1, date: now, activity: `Transfer to ${formData.toLocation}`, itemName: formData.itemName, amount: -qty, location: formData.fromLocation, user: user },
            { id: Date.now() + 2, date: now, activity: `Transfer from ${formData.fromLocation}`, itemName: formData.itemName, amount: qty, location: formData.toLocation, user: user },
            ...prev
        ]);
    } else {
        setTransactions(prev => [{ id: Date.now(), date: now, activity: formData.activity || (qty > 0 ? 'Stock In' : 'Stock Out'), itemName: formData.itemName, amount: qty, location: finalLocation || 'Office', user: user }, ...prev]);
    }
    setFormData({ ...formData, amount: '', activity: '', customLocation: '' });
    setActiveTab('summary');
  };

  if (!user) {
    return (
      <div className="min-h-screen bg-[#1a1c2e] flex items-center justify-center p-6">
        <div className="bg-white rounded-[2rem] shadow-2xl w-full max-w-sm p-10 space-y-8 text-center">
            <div className="w-20 h-20 bg-indigo-50 rounded-3xl flex items-center justify-center mx-auto text-indigo-600 shadow-inner">
                <Package size={40} />
            </div>
            <div>
                <h1 className="text-3xl font-black text-slate-800 tracking-tight">Augusto</h1>
                <p className="text-slate-400 text-sm font-bold mt-1">Inventory System</p>
            </div>
          <form onSubmit={handleLogin} className="space-y-4 text-left">
            <div className="space-y-1">
                <label className="text-xs font-black text-slate-400 uppercase ml-2">Email Address</label>
                <input type="email" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl text-sm focus:ring-2 focus:ring-indigo-500 outline-none transition-all" value={loginEmail} onChange={e => setLoginEmail(e.target.value)} required />
            </div>
            <div className="space-y-1">
                <label className="text-xs font-black text-slate-400 uppercase ml-2">Password</label>
                <input type="password" className="w-full p-4 bg-slate-50 border border-slate-100 rounded-2xl text-sm focus:ring-2 focus:ring-indigo-500 outline-none transition-all" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
            </div>
            {loginError && <p className="text-rose-500 text-xs font-bold text-center bg-rose-50 py-2 rounded-xl border border-rose-100">{loginError}</p>}
            <button type="submit" className="w-full bg-indigo-600 text-white font-black py-4 rounded-2xl shadow-xl hover:bg-indigo-700 active:scale-[0.98] transition-all mt-4 tracking-widest text-sm uppercase">Login</button>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#f8fafc] flex flex-col pb-28 text-slate-900 font-sans">
      <header className="bg-indigo-700 text-white p-6 shadow-xl flex justify-between items-center sticky top-0 z-50 rounded-b-[2rem]">
        <div className="flex items-center gap-3">
          <div className="bg-white/20 p-2 rounded-xl"><Package size={22} /></div>
          <h1 className="text-xl font-black tracking-tighter">Augusto Inventory</h1>
        </div>
        <button onClick={() => setUser(null)} className="p-3 bg-white/10 rounded-2xl hover:bg-white/20 transition-all shadow-lg active:scale-90"><LogOut size={20} /></button>
      </header>

      <main className="p-4 max-w-2xl mx-auto w-full">
        {activeTab === 'summary' && (
          <div className="space-y-8 animate-in fade-in duration-500">
            <div className="flex flex-col gap-2">
              <h2 className="text-2xl font-black text-slate-800">Stock Overview</h2>
              <div className="relative">
                <Search size={16} className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400" />
                <input type="text" placeholder="Search Item Name..." className="w-full pl-12 pr-6 py-4 bg-white border border-slate-100 rounded-3xl text-sm shadow-sm outline-none focus:ring-2 focus:ring-indigo-500" onChange={(e) => setSearchTerm(e.target.value)} />
              </div>
            </div>

            {['FG', 'POSM', 'Accessories'].map(cat => {
              const catItems = items.filter(i => i.category === cat && i.name.toLowerCase().includes(searchTerm.toLowerCase()));
              if (catItems.length === 0) return null;
              return (
                <div key={cat} className="space-y-4">
                  <div className="flex items-center justify-between px-2">
                    <span className="text-xs font-black text-slate-400 uppercase tracking-[0.2em]">{cat === 'FG' ? 'Finished Goods' : cat === 'POSM' ? 'Materials' : 'Accessories'}</span>
                    <span className="text-xs font-bold text-slate-300 uppercase">Total / Location</span>
                  </div>
                  <div className="grid gap-4">
                    {catItems.map(item => {
                      const data = stockSummary[item.name] || { total: 0, details: {} };
                      return (
                        <div key={item.id} className="bg-white p-6 rounded-[2rem] shadow-sm border border-slate-50 hover:shadow-md transition-all group">
                          <div className="flex justify-between items-start mb-4">
                            <span className="text-[15px] font-bold text-slate-700 leading-tight pr-8 group-hover:text-indigo-600 transition-colors">{item.name}</span>
                            <span className={`font-mono font-black text-2xl ${data.total > 0 ? 'text-indigo-600' : 'text-slate-200'}`}>{data.total}</span>
                          </div>
                          <div className="flex flex-wrap gap-2 pt-2 border-t border-slate-50 mt-2">
                            {['Office', 'Worldex', 'San Tai'].map(loc => {
                              const qty = data.details[loc] || 0;
                              const isActive = qty > 0;
                              return (
                                <div key={loc} className={`px-4 py-2 rounded-xl text-xs font-black border transition-all ${isActive ? 'bg-indigo-50 border-indigo-100 text-indigo-600 shadow-sm' : 'bg-slate-50 border-transparent text-slate-300'}`}>
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
          <div className="space-y-6 animate-in slide-in-from-bottom-8 duration-300">
            <div className="flex bg-white p-1.5 rounded-3xl shadow-sm border border-slate-100">
              <button onClick={() => setFormMode('inout')} className={`flex-1 py-4 rounded-[1.2rem] text-xs font-black transition-all ${formMode === 'inout' ? 'bg-indigo-600 text-white shadow-xl' : 'text-slate-400 hover:text-slate-600'}`}>In / Out</button>
              <button onClick={() => setFormMode('transfer')} className={`flex-1 py-4 rounded-[1.2rem] text-xs font-black transition-all ${formMode === 'transfer' ? 'bg-indigo-600 text-white shadow-xl' : 'text-slate-400 hover:text-slate-600'}`}>Transfer</button>
              <button onClick={() => { setFormMode('newitem'); setFormData({...formData, itemName: ''}) }} className={`flex-1 py-4 rounded-[1.2rem] text-xs font-black transition-all ${formMode === 'newitem' ? 'bg-indigo-600 text-white shadow-xl' : 'text-slate-400 hover:text-slate-600'}`}>New Item</button>
            </div>

            <form onSubmit={handleAction} className="bg-white p-8 rounded-[2.5rem] shadow-2xl space-y-8 border border-slate-50">
              {formMode === 'newitem' ? (
                <div className="space-y-4">
                  <div className="space-y-1">
                    <label className="text-xs font-black text-slate-400 uppercase ml-2 tracking-widest">Item Name</label>
                    <input type="text" className="w-full p-5 bg-slate-50 border border-slate-200 rounded-3xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="Enter new item name..." value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})} required />
                  </div>
                  <div className="grid grid-cols-3 gap-3">
                    {['FG', 'POSM', 'Accessories'].map(c => (
                      <button key={c} type="button" onClick={() => setFormData({...formData, newCategory: c})} className={`py-4 rounded-2xl text-xs font-black border transition-all ${formData.newCategory === c ? 'bg-indigo-100 border-indigo-200 text-indigo-600 shadow-inner' : 'bg-white text-slate-400 border-slate-100'}`}>{c}</button>
                    ))}
                  </div>
                </div>
              ) : (
                <div className="space-y-1">
                  <label className="text-xs font-black text-slate-400 uppercase ml-2 tracking-widest">Select Product</label>
                  <select className="w-full p-5 bg-slate-50 border border-slate-200 rounded-3xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none appearance-none" value={formData.itemName} onChange={e => setFormData({...formData, itemName: e.target.value})}>
                    {items.map(i => <option key={i.id} value={i.name}>{i.name}</option>)}
                  </select>
                </div>
              )}

              {formMode === 'transfer' ? (
                <div className="flex items-center gap-4 bg-slate-50 p-6 rounded-[2rem] border border-slate-100 relative">
                  <div className="flex-1">
                    <label className="text-[10px] font-black text-slate-400 uppercase mb-2 block">From</label>
                    <select className="w-full p-3 bg-white border border-slate-200 rounded-2xl text-xs font-black shadow-sm outline-none" value={formData.fromLocation} onChange={e => setFormData({...formData, fromLocation: e.target.value})}>
                      {['Office', 'Worldex', 'San Tai'].map(l => <option key={l} value={l}>{l}</option>)}
                    </select>
                  </div>
                  <div className="w-10 h-10 bg-indigo-600 rounded-full flex items-center justify-center text-white shadow-lg mt-4 shrink-0"><ArrowRight size={18} /></div>
                  <div className="flex-1">
                    <label className="text-[10px] font-black text-slate-400 uppercase mb-2 block">To</label>
                    <select className="w-full p-3 bg-white border border-slate-200 rounded-2xl text-xs font-black shadow-sm outline-none" value={formData.toLocation} onChange={e => setFormData({...formData, toLocation: e.target.value})}>
                      {['Office', 'Worldex', 'San Tai'].map(l => <option key={l} value={l}>{l}</option>)}
                    </select>
                  </div>
                </div>
              ) : (
                <div className="space-y-1">
                  <label className="text-xs font-black text-slate-400 uppercase ml-2 tracking-widest">Select Location</label>
                  <div className="grid grid-cols-4 gap-3">
                    {['Office', 'Worldex', 'San Tai', 'Other'].map(l => (
                      <button key={l} type="button" onClick={() => setFormData({...formData, location: l})} className={`py-4 rounded-2xl text-xs font-black border transition-all ${formData.location === l ? 'bg-indigo-600 text-white shadow-xl' : 'bg-white text-slate-400 border-slate-100 hover:border-indigo-200'}`}>{l}</button>
                    ))}
                  </div>
                  {formData.location === 'Other' && (
                    <input type="text" className="w-full p-4 mt-3 bg-slate-50 border border-indigo-200 rounded-2xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="Enter custom location..." value={formData.customLocation} onChange={e => setFormData({...formData, customLocation: e.target.value})} required />
                  )}
                </div>
              )}

              <div className="grid grid-cols-2 gap-6">
                <div className="space-y-1">
                  <label className="text-xs font-black text-slate-400 uppercase ml-2 tracking-widest">Quantity</label>
                  <input type="number" className="w-full p-5 bg-slate-50 border border-slate-200 rounded-3xl text-2xl font-black font-mono focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="0" value={formData.amount} onChange={e => setFormData({...formData, amount: e.target.value})} required={formMode !== 'newitem'} />
                </div>
                <div className="space-y-1">
                  <label className="text-xs font-black text-slate-400 uppercase ml-2 tracking-widest">Remarks</label>
                  <input type="text" className="w-full p-5 bg-slate-50 border border-slate-200 rounded-3xl text-sm font-bold focus:ring-2 focus:ring-indigo-500 outline-none" placeholder="Optional" value={formData.activity} onChange={e => setFormData({...formData, activity: e.target.value})} />
                </div>
              </div>

              <button type="submit" className="w-full bg-indigo-600 text-white font-black py-6 rounded-[1.5rem] shadow-[0_20px_40px_-15px_rgba(79,70,229,0.4)] hover:bg-indigo-700 active:scale-95 transition-all uppercase tracking-[0.2em] text-sm">
                Confirm Transaction
              </button>
            </form>
          </div>
        )}

        {activeTab === 'history' && (
          <div className="space-y-6 animate-in fade-in duration-500">
            <h2 className="text-2xl font-black text-slate-800">Recent Logs</h2>
            <div className="grid gap-4">
              {transactions.map(tx => (
                <div key={tx.id} className="bg-white p-6 rounded-[2rem] shadow-sm border border-slate-50 flex items-center justify-between group">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="px-3 py-1 rounded-xl text-[10px] font-black bg-indigo-50 text-indigo-700 uppercase tracking-tighter border border-indigo-100">{tx.location}</span>
                      <span className="text-xs text-slate-400 font-bold">{tx.date}</span>
                    </div>
                    <div className="text-md font-black text-slate-700">{tx.activity}</div>
                    <div className="text-xs text-slate-400 mt-1 italic leading-tight">{tx.itemName}</div>
                  </div>
                  <div className={`font-mono font-black text-xl pl-6 ${tx.amount > 0 ? 'text-emerald-500' : 'text-rose-500'}`}>
                    {tx.amount > 0 ? `+${tx.amount}` : tx.amount}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <nav className="fixed bottom-0 left-0 right-0 bg-white/80 backdrop-blur-xl border-t border-slate-100 flex justify-around p-6 shadow-[0_-10px_40px_rgba(0,0,0,0.05)] z-50 rounded-t-[3rem]">
        <button onClick={() => setActiveTab('summary')} className={`flex flex-col items-center gap-2 transition-all ${activeTab === 'summary' ? 'text-indigo-600' : 'text-slate-300 hover:text-slate-400'}`}>
          <LayoutDashboard size={24} /><span className="text-xs font-black uppercase tracking-widest">Home</span>
        </button>
        <button onClick={() => setActiveTab('add')} className="relative -mt-16 group">
          <div className={`p-6 rounded-[2rem] shadow-2xl ring-[12px] ring-[#f8fafc] active:scale-90 transition-all ${activeTab === 'add' ? 'bg-indigo-600 text-white' : 'bg-slate-400 text-white group-hover:bg-slate-500'}`}>
            <Plus size={36} strokeWidth={3} />
          </div>
        </button>
        <button onClick={() => setActiveTab('history')} className={`flex flex-col items-center gap-2 transition-all ${activeTab === 'history' ? 'text-indigo-600' : 'text-slate-300 hover:text-slate-400'}`}>
          <History size={24} /><span className="text-xs font-black uppercase tracking-widest">Logs</span>
        </button>
      </nav>
    </div>
  );
};

export default App;
