'use client';
import { useState } from 'react';

export default function DiamondHeightsProfessionalApp() {
  // محفظة العقارات الاحترافية (بناءً على طلباتك السابقة)
  const [properties, setProperties] = useState([
    {
      id: 'DH-001',
      title: 'شقة ملكية تشطيب Ultra Lux',
      category: 'سكني',
      type: 'شقق',
      location: 'الإسكندرية • لوران',
      price: 4500000,
      priceStr: '4,500,000 ج.م',
      area: '220 م²',
      rooms: '4 غرف',
      baths: '3 حمام',
      details: 'تشطيب هندسي خاص، إطلالة مفتوحة، أمن وحراسة 24/7.',
      views: 342,
      images: [
        'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
        'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800'
      ]
    },
    {
      id: 'DH-002',
      title: 'مكتب تجاري إداري واجهة زجاجية',
      category: 'تجاري وإداري',
      type: 'مكاتب',
      location: 'الإسكندرية • سموحة',
      price: 25000,
      priceStr: '25,000 ج.م / شهرياً',
      area: '150 م²',
      rooms: 'مفتوح (Open Space)',
      baths: '2 حمام',
      details: 'موقع حيوي جداً على الشارع الرئيسي، مجهز بالكامل بالتكييفات المركزية.',
      views: 189,
      images: [
        'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800'
      ]
    }
  ]);

  // طلبات العملاء (فورم "مش لاقي عقارك" بالبادجت والمواصفات)
  const [clientRequests, setClientRequests] = useState([
    { name: 'محمد علي', phone: '01011112222', budget: 'من 4 لـ 6 ملايين', req: 'شقة في سموحة أو لوران 3 غرف' }
  ]);

  const [activeTab, setActiveTab] = useState('catalog');
  const [adminAuth, setAdminAuth] = useState(false);
  const [passInput, setPassInput] = useState('');
  const WHATSAPP_NUMBER = "201030464219";

  // حقول فورم "مش لاقي عقارك"
  const [reqName, setReqName] = useState('');
  const [reqPhone, setReqPhone] = useState('');
  const [reqDetails, setReqDetails] = useState('');
  const [reqBudget, setReqBudget] = useState('');
  const [submittedReq, setSubmittedReq] = useState(false);

  // حقول إضافة عقار جديد من لوحة الإدارة
  const [newTitle, setNewTitle] = useState('');
  const [newCat, setNewCat] = useState('سكني');
  const [newPrice, setNewPrice] = useState('');
  const [newLoc, setNewLoc] = useState('الإسكندرية • البيطاش');
  const [newArea, setNewArea] = useState('');
  const [newRooms, setNewRooms] = useState('');
  const [newDetails, setNewDetails] = useState('');

  // عداد النقرات والتفاعل
  const handleViewProperty = (id) => {
    setProperties(properties.map(p => p.id === id ? { ...p, views: p.views + 1 } : p));
  };

  // حذف عقار نهائياً
  const handleDeleteProperty = (id) => {
    setProperties(properties.filter(p => p.id !== id));
  };

  return (
    <div style={{ backgroundColor: '#0b0b0b', color: '#f3f4f6', minHeight: '100vh', fontFamily: 'Cairo, sans-serif', direction: 'rtl' }}>
      
      {/* الشريط العلوي الفخم */}
      <header style={{ borderBottom: '1px solid #262626', padding: '16px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', backgroundColor: '#121212', position: 'sticky', top: 0, zIndex: 1000 }}>
        <div>
          <h1 style={{ color: '#d4af37', fontSize: '20px', fontWeight: 'bold', margin: 0 }}>DIAMOND HEIGHTS</h1>
          <p style={{ color: '#888', fontSize: '11px', margin: 0 }}>Real Estate Management & Consultancy</p>
        </div>
        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <button onClick={() => setActiveTab('catalog')} style={{ background: activeTab === 'catalog' ? '#d4af37' : 'transparent', color: activeTab === 'catalog' ? '#000' : '#fff', border: '1px solid #d4af37', padding: '8px 14px', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold', fontSize: '13px' }}>الكتالوج</button>
          <button onClick={() => setActiveTab('request')} style={{ background: activeTab === 'request' ? '#d4af37' : 'transparent', color: activeTab === 'request' ? '#000' : '#fff', border: '1px solid #d4af37', padding: '8px 14px', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold', fontSize: '13px' }}>مش لاقي عقارك؟</button>
          <button onClick={() => setActiveTab('admin')} style={{ background: activeTab === 'admin' ? '#d4af37' : 'transparent', color: activeTab === 'admin' ? '#000' : '#fff', border: '1px solid #d4af37', padding: '8px 14px', borderRadius: '8px', cursor: 'pointer', fontWeight: 'bold', fontSize: '13px' }}>حساب الإدارة</button>
        </div>
      </header>

      <main style={{ maxWidth: '1100px', margin: '0 auto', padding: '30px 20px' }}>

        {/* 1. قسم الكتالوج الاحترافي */}
        {activeTab === 'catalog' && (
          <div>
            <div style={{ textAlign: 'center', marginBottom: '40px' }}>
              <h2 style={{ color: '#d4af37', fontSize: '28px', marginBottom: '10px' }}>محفظة العقارات الفاخرة</h2>
              <p style={{ color: '#aaa', fontSize: '14px' }}>نخبة العقارات السكنية والتجارية المصممة خصيصاً لتلبي تطلعاتكم الاستثمارية.</p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '24px' }}>
              {properties.map((prop) => (
                <div key={prop.id} style={{ backgroundColor: '#161616', borderRadius: '14px', border: '1px solid #2a2a2a', overflow: 'hidden', boxShadow: '0 10px 30px rgba(0,0,0,0.5)' }}>
                  <div style={{ position: 'relative' }}>
                    <img src={prop.images[0]} alt={prop.title} style={{ width: '100%', height: '220px', objectFit: 'cover' }} />
                    <span style={{ position: 'absolute', top: '12px', right: '12px', backgroundColor: '#d4af37', color: '#000', padding: '4px 10px', borderRadius: '6px', fontSize: '12px', fontWeight: 'bold' }}>{prop.id}</span>
                  </div>
                  
                  <div style={{ padding: '20px' }}>
                    <div style={{ fontSize: '13px', color: '#888', marginBottom: '6px' }}>📍 {prop.location}</div>
                    <h3 style={{ fontSize: '18px', fontWeight: 'bold', color: '#fff', marginBottom: '10px' }}>{prop.title}</h3>
                    <div style={{ fontSize: '20px', fontWeight: 'bold', color: '#2ecc71', marginBottom: '14px' }}>{prop.priceStr}</div>
                    
                    <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', flexWrap: 'wrap' }}>
                      <span style={{ backgroundColor: '#222', padding: '4px 8px', borderRadius: '6px', fontSize: '12px', color: '#d4af37', border: '1px solid #333' }}>🛏️ {prop.rooms}</span>
                      <span style={{ backgroundColor: '#222', padding: '4px 8px', borderRadius: '6px', fontSize: '12px', color: '#d4af37', border: '1px solid #333' }}>🛁 {prop.baths}</span>
                      <span style={{ backgroundColor: '#222', padding: '4px 8px', borderRadius: '6px', fontSize: '12px', color: '#d4af37', border: '1px solid #333' }}>📐 {prop.area}</span>
                    </div>

                    <p style={{ fontSize: '13px', color: '#bbb', lineHeight: '1.5', marginBottom: '20px' }}>{prop.details}</p>

                    <a 
                      href={`https://wa.me/${WHATSAPP_NUMBER}?text=مرحباً، مهتم بالاستفسار عن العقار رقم ${prop.id} (${prop.title})`} 
                      target="_blank" 
                      onClick={() => handleViewProperty(prop.id)}
                      style={{ display: 'block', textAlign: 'center', backgroundColor: '#25D366', color: '#fff', padding: '12px', borderRadius: '8px', textDecoration: 'none', fontWeight: 'bold', fontSize: '14px', boxShadow: '0 4px 12px rgba(37,211,102,0.3)' }}
                    >
                      💬 التواصل المباشر عبر واتساب
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* 2. فورم طلبات العملاء (مش لاقي طلبك) */}
        {activeTab === 'request' && (
          <div style={{ maxWidth: '600px', margin: '0 auto', backgroundColor: '#161616', padding: '30px', borderRadius: '16px', border: '1px solid #2a2a2a' }}>
            <h2 style={{ color: '#d4af37', fontSize: '24px', marginBottom: '10px', textAlign: 'center' }}>مش لاقي طلبك على الموقع؟</h2>
            <p style={{ color: '#aaa', fontSize: '13px', textAlign: 'center', marginBottom: '25px' }}>اكتب لنا المواصفات الدقيقة والبادجت الخاصة بك، وفريق المبيعات سيقوم بتوفير العقار المناسب فوراً.</p>

            {submittedReq ? (
              <div style={{ backgroundColor: '#1e3323', border: '1px solid #2ecc71', padding: '20px', borderRadius: '10px', textAlign: 'center', color: '#2ecc71' }}>
                تم إرسال طلبك بنجاح وسيتواصل معك فريق إدارة المبيعات في أسرع وقت!
              </div>
            ) : (
              <form onSubmit={(e) => {
                e.preventDefault();
                setClientRequests([...clientRequests, { name: reqName, phone: reqPhone, budget: reqBudget, req: reqDetails }]);
                setSubmittedReq(true);
              }}>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '13px', marginBottom: '6px', color: '#ccc' }}>الاسم الكريم</label>
                  <input type="text" required value={reqName} onChange={(e) => setReqName(e.target.value)} style={{ width: '100%', padding: '12px', borderRadius: '8px', backgroundColor: '#222', border: '1px solid #444', color: '#fff' }} placeholder="أدخل اسمك" />
                </div>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '13px', marginBottom: '6px', color: '#ccc' }}>رقم الهاتف (واتساب)</label>
                  <input type="text" required value={reqPhone} onChange={(e) => setReqPhone(e.target.value)} style={{ width: '100%', padding: '12px', borderRadius: '8px', backgroundColor: '#222', border: '1px solid #444', color: '#fff' }} placeholder="010xxxxxxxx" />
                </div>
                <div style={{ marginBottom: '15px' }}>
                  <label style={{ display: 'block', fontSize: '13px', marginBottom: '6px', color: '#ccc' }}>الميزانية المتوقعة (البادجت)</label>
                  <input type="text" required value={reqBudget} onChange={(e) => setReqBudget(e.target.value)} style={{ width: '100%', padding: '12px', borderRadius: '8px', backgroundColor: '#222', border: '1px solid #444', color: '#fff' }} placeholder="مثال: من 4 لـ 6 ملايين ج.م" />
                </div>
                <div style={{ marginBottom: '20px' }}>
                  <label style={{ display: 'block', fontSize: '13px', marginBottom: '6px', color: '#ccc' }}>مواصفات العقار المطلوب (المنطقة، المساحة، الغرف...)</label>
                  <textarea rows="4" required value={reqDetails} onChange={(e) => setReqDetails(e.target.value)} style={{ width: '100%', padding: '12px', borderRadius: '8px', backgroundColor: '#222', border: '1px solid #444', color: '#fff' }} placeholder="اكتب تفاصيل طلبك بدقة..."></textarea>
                </div>
                <button type="submit" style={{ width: '100%', backgroundColor: '#d4af37', color: '#000', padding: '14px', borderRadius: '8px', fontWeight: 'bold', border: 'none', cursor: 'pointer', fontSize: '15px' }}>إرسال الطلب لفريق المبيعات</button>
              </form>
            )}
          </div>
        )}

        {/* 3. حساب الإدارة والداش بورد الاحترافية */}
        {activeTab === 'admin' && (
          <div>
            {!adminAuth ? (
              <div style={{ maxWidth: '400px', margin: '40px auto', backgroundColor: '#161616', padding: '30px', borderRadius: '16px', border: '1px solid #2a2a2a', textAlign: 'center' }}>
                <h2 style={{ color: '#d4af37', marginBottom: '20px' }}>تسجيل دخول الإدارة</h2>
                <input type="password" placeholder="أدخل كلمة مرور المشرف" value={passInput} onChange={(e) => setPassInput(e.target.value)} style={{ width: '100%', padding: '12px', marginBottom: '15px', backgroundColor: '#222', border: '1px solid #444', color: '#fff', borderRadius: '8px' }} />
                <button onClick={() => { if(passInput === '1234') setAdminAuth(true); else alert('كلمة المرور خطأ (تجريبي: 1234)'); }} style={{ width: '100%', backgroundColor: '#d4af37', color: '#000', padding: '12px', borderRadius: '8px', fontWeight: 'bold', border: 'none', cursor: 'pointer' }}>دخول الداش بورد</button>
              </div>
            ) : (
              <div>
                <h2 style={{ color: '#d4af37', marginBottom: '25px' }}>لوحة التحكم وتحليلات الترافيك (Dashboard)</h2>
                
                {/* إحصائيات سريعة */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px', marginBottom: '30px' }}>
                  <div style={{ backgroundColor: '#161616', padding: '20px', borderRadius: '12px', border: '1px solid #2a2a2a' }}>
                    <div style={{ color: '#888', fontSize: '13px' }}>إجمالي العقارات المعروضة</div>
                    <div style={{ fontSize: '28px', fontWeight: 'bold', color: '#d4af37', marginTop: '5px' }}>{properties.length}</div>
                  </div>
                  <div style={{ backgroundColor: '#161616', padding: '20px', borderRadius: '12px', border: '1px solid #2a2a2a' }}>
                    <div style={{ color: '#888', fontSize: '13px' }}>إجمالي النقرات وتفاعل الزوار</div>
                    <div style={{ fontSize: '28px', fontWeight: 'bold', color: '#2ecc71', marginTop: '5px' }}>{properties.reduce((acc, p) => acc + p.views, 0)} نقرة</div>
                  </div>
                  <div style={{ backgroundColor: '#161616', padding: '20px', borderRadius: '12px', border: '1px solid #2a2a2a' }}>
                    <div style={{ color: '#888', fontSize: '13px' }}>طلبات العملاء الجدد (مش لاقي عقارك)</div>
                    <div style={{ fontSize: '28px', fontWeight: 'bold', color: '#3498db', marginTop: '5px' }}>{clientRequests.length} طلبات</div>
                  </div>
                </div>

                {/* تحليل الزائرين جغرافياً والمحافظات */}
                <div style={{ backgroundColor: '#161616', padding: '20px', borderRadius: '12px', border: '1px solid #2a2a2a', marginBottom: '30px' }}>
                  <h3 style={{ color: '#fff', fontSize: '16px', marginBottom: '15px' }}>🗺️ تحليلات وتوزيع الزائرين حسب المحافظات:</h3>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px', fontSize: '14px' }}>
                    <div style={{ backgroundColor: '#222', padding: '12px', borderRadius: '8px' }}>📍 الإسكندرية (البيطاش / لوران / سموحة): <b style={{ color: '#d4af37' }}>78%</b></div>
                    <div style={{ backgroundColor: '#222', padding: '12px', borderRadius: '8px' }}>📍 القاهرة الكبرى: <b style={{ color: '#d4af37' }}>15%</b></div>
                    <div style={{ backgroundColor: '#222', padding: '12px', borderRadius: '8px' }}>📍 محافظات أخرى ومستثمرين خارجياً: <b style={{ color: '#d4af37' }}>7%</b></div>
                  </div>
                </div>

                {/* استعراض طلبات العملاء */}
                <div style={{ backgroundColor: '#161616', padding: '20px', borderRadius: '12px', border: '1px solid #2a2a2a', marginBottom: '30px' }}>
                  <h3 style={{ color: '#fff', fontSize: '16px', marginBottom: '15px' }}>📋 متابعة طلبات العملاء الواردة:</h3>
                  {clientRequests.map((req, idx) => (
                    <div key={idx} style={{ backgroundColor: '#222', padding: '12px', borderRadius: '8px', marginBottom: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                      <div>
                        <div style={{ fontWeight: 'bold', color: '#d4af37' }}>{req.name} - {req.phone}</div>
                        <div style={{ fontSize: '13px', color: '#ccc' }}>البادجت: {req.budget} | الطلب: {req.req}</div>
                      </div>
                      <a href={`https://wa.me/20${req.phone.replace(/^0/, '')}`} target="_blank" style={{ backgroundColor: '#25D366', color: '#fff', padding: '6px 12px', borderRadius: '6px', fontSize: '12px', textDecoration: 'none', fontWeight: 'bold' }}>مراسلة العميل</a>
                    </div>
                  ))}
                </div>

                {/* إضافة وحذف العقارات بضغط زر */}
                <div style={{ backgroundColor: '#161616', padding: '20px', borderRadius: '12px', border: '1px solid #2a2a2a' }}>
                  <h3 style={{ color: '#fff', fontSize: '16px', marginBottom: '15px' }}>⚙️ إدارة وحذف العقارات الحالية:</h3>
                  {properties.map((prop) => (
                    <div key={prop.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', backgroundColor: '#222', padding: '12px', borderRadius: '8px', marginBottom: '10px' }}>
                      <div>
                        <span style={{ color: '#d4af37', fontWeight: 'bold', marginLeft: '10px' }}>{prop.id}</span>
                        <span style={{ color: '#fff' }}>{prop.title}</span>
                        <span style={{ color: '#2ecc71', marginRight: '15px', fontSize: '13px' }}>({prop.views} نقرة)</span>
                      </div>
                      <button onClick={() => handleDeleteProperty(prop.id)} style={{ backgroundColor: '#e74c3c', color: '#fff', border: 'none', padding: '6px 14px', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '12px' }}>حذف العقار</button>
                    </div>
                  ))}
                </div>

              </div>
            )}
          </div>
        )}

      </main>
    </div>
  );
}
