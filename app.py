import streamlit as st

st.set_page_config(
    page_title="Diamond Heights Real Estate",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    .stApp {
        background-color: #121212;
        color: #f1f1f1;
    }
    
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-left: 1px solid #d4af37;
    }
    
    /* تصميم الكارت بشكل نظيف ومتناسق تماماً */
    .property-card {
        background-color: #1e1e1e;
        border-radius: 12px;
        border: 1px solid #332d11;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    
    .property-title {
        font-size: 16px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    .property-location {
        font-size: 13px;
        color: #a0a0a0;
        margin-bottom: 8px;
    }
    
    .property-price {
        font-size: 17px;
        font-weight: 700;
        color: #2ecc71;
        margin-bottom: 10px;
    }
    
    .property-details {
        font-size: 13px;
        color: #ccc;
        margin-bottom: 12px;
        line-height: 1.5;
    }
    
    .specs-container {
        display: flex;
        gap: 8px;
        margin-bottom: 12px;
        flex-wrap: wrap;
    }
    
    .spec-badge {
        background-color: #2a2a2a;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        color: #d4af37;
        font-weight: 600;
        border: 1px solid #443810;
    }
    
    h1, h2, h3 {
        color: #d4af37 !important;
        font-weight: 700;
    }
    
    .floating-whatsapp {
        position: fixed;
        bottom: 25px;
        left: 25px;
        background-color: #25D366;
        color: white;
        border-radius: 50px;
        padding: 10px 20px;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        z-index: 9999;
        font-weight: bold;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 14px;
    }
    .floating-whatsapp:hover {
        color: white;
    }
    
    .whatsapp-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        border-radius: 8px;
        background-color: #25D366;
        color: white;
        text-decoration: none;
        font-weight: bold;
        font-size: 13px;
        gap: 8px;
        width: 100%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    .whatsapp-btn:hover {
        color: white;
        background-color: #20ba5a;
    }
    </style>
""", unsafe_allow_html=True)

if 'properties' not in st.session_state:
    st.session_state.properties = [
        {
            "id": "DH-001",
            "title": "شقة سكنية مميزة تشطيب سوبر لوكس",
            "category": "سكني",
            "type": "شقق",
            "location": "الإسكندرية • البيطاش",
            "price": "1,500,000 ج.م",
            "area": "120 م²",
            "rooms": "3 غرف",
            "baths": "1 حمام",
            "details": "شقة بحرية بالكامل، قريبة من الخدمات الرئيسية، الدور الثالث.",
            "images": [
                "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600",
                "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600"
            ]
        },
        {
            "id": "DH-002",
            "title": "محل تجاري واجهة واسعة",
            "category": "تجاري وإداري",
            "type": "محلات",
            "location": "الإسكندرية • لوران",
            "price": "7,000 ج.م / شهرياً",
            "area": "80 م²",
            "rooms": "مفتوح",
            "baths": "1 حمام",
            "details": "محل تجاري حيوي في منطقة تجارية نشطة، واجهة زجاجية.",
            "images": [
                "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600",
                "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=600"
            ]
        },
        {
            "id": "DH-003",
            "title": "فيلا مستقلة بحمام سباحة",
            "category": "سكني",
            "type": "فيلل",
            "location": "الإسكندرية • العجمي",
            "price": "4,200,000 ج.م",
            "area": "350 م²",
            "rooms": "5 غرف",
            "baths": "4 حمام",
            "details": "فيلا فاخرة تشطيب خاص مع حديقة واسعة وجراج.",
            "images": [
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600",
                "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600"
            ]
        }
    ]

WHATSAPP_NUMBER = "201030464219"

st.markdown(f"""
    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=مرحباً، أود الاستفسار عن عقارات Diamond Heights Real Estate" target="_blank" class="floating-whatsapp">
        💬 واتساب
    </a>
""", unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='text-align: center; color: #d4af37;'>Diamond Heights</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #aaa;'>Real Estate Management</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio("القائمة الرئيسية", ["🔍 كتالوج العقارات", "🏢 عن الشركة", "⚙️ لوحة الإدارة (Admin)"])

if menu == "🔍 كتالوج العقارات":
    st.markdown("<h1 style='text-align: center; font-size: 26px;'>كتالوج العقارات - Diamond Heights Real Estate</h1>", unsafe_allow_html=True)
    st.markdown("---")

    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        cat_filter = st.selectbox("التصنيف", ["الكل", "سكني", "تجاري وإداري"])
    with col_f2:
        type_filter = st.selectbox("النوع", ["الكل", "شقق", "فيلل", "محلات"])
    with col_f3:
        loc_filter = st.selectbox("المنطقة", ["الكل", "البيطاش", "العجمي", "لوران"])

    st.markdown("<br>", unsafe_allow_html=True)

    filtered_props = st.session_state.properties
    if cat_filter != "الكل":
        filtered_props = [p for p in filtered_props if p["category"] == cat_filter]
    if type_filter != "الكل":
        filtered_props = [p for p in filtered_props if p["type"] == type_filter]
    if loc_filter != "الكل":
        filtered_props = [p for p in filtered_props if loc_filter in p["location"]]

    if not filtered_props:
        st.info("لا توجد عقارات مطابقة لبحثك.")
    else:
        cols = st.columns(3)
        for idx, prop in enumerate(filtered_props):
            col = cols[idx % 3]
            with col:
                # فتح حاوية الكارت الموحدة
                st.markdown('<div class="property-card">', unsafe_allow_html=True)
                
                # عرض الصور بشكل نظيف داخل الـ container الطبيعي
                if 'images' in prop and prop['images']:
                    for img in prop['images']:
                        st.image(img, use_container_width=True)
                
                # تفاصيل العقار داخل نفس الكارت بانتظام
                st.markdown(f"""
                    <div class="property-title">{prop['title']}</div>
                    <div class="property-location">📍 {prop['location']}</div>
                    <div class="property-price">{prop['price']}</div>
                    
                    <div class="specs-container">
                        <span class="spec-badge">🛏️ {prop['rooms']}</span>
                        <span class="spec-badge">🛁 {prop['baths']}</span>
                        <span class="spec-badge">📐 {prop['area']}</span>
                        <span class="spec-badge">🏷️ {prop['id']}</span>
                    </div>
                    
                    <div class="property-details">
                        {prop['details']}
                    </div>
                """, unsafe_allow_html=True)
                
                wa_msg = f"مرحباً Diamond Heights، مهتم بالعقار ({prop['title']} - كود: {prop['id']} - بسعر: {prop['price']})"
                wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(' ', '%20')}"
                
                st.markdown(f"""
                    <a href="{wa_link}" target="_blank" class="whatsapp-btn">
                        🟢 تواصل عبر واتساب (01030464219)
                    </a>
                """, unsafe_allow_html=True)
                
                # إغلاق الكارت
                st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🏢 عن الشركة":
    st.markdown("<h1>عن شركة Diamond Heights Real Estate</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 12px; border: 1px solid #332d11;">
        <p style="color: #ccc;">نحن في <b>Diamond Heights Real Estate</b> نتميز بتقديم أفضل الفرص العقارية السكنية والتجارية في الإسكندرية.</p>
        <p style="color: #d4af37;"><b>للتواصل والإدارة:</b> 01030464219</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "⚙️ لوحة الإدارة (Admin)":
    st.markdown("<h1>لوحة الإدارة والتحكم</h1>", unsafe_allow_html=True)
    password = st.text_input("كلمة مرور المشرف:", type="password")
    
    if password == "1234":
        st.success("تم تسجيل الدخول بنجاح!")
        with st.form("add_prop"):
            p_title = st.text_input("عنوان العقار")
            p_cat = st.selectbox("التصنيف", ["سكني", "تجاري وإداري"])
            p_type = st.selectbox("النوع", ["شقق", "فيلل", "محلات"])
            p_loc = st.text_input("المنطقة", value="الإسكندرية • البيطاش")
            p_price = st.text_input("السعر", value="1,500,000 ج.م")
            p_area = st.text_input("المساحة", value="120 م²")
            p_rooms = st.text_input("الغرف", value="3 غرف")
            p_baths = st.text_input("الحمامات", value="1 حمام")
            p_details = st.text_area("تفاصيل العقار", value="شقة بحرية بالكامل، قريبة من الخدمات الرئيسية.")
            
            img1 = st.text_input("رابط الصورة 1", value="https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600")
            img2 = st.text_input("رابط الصورة 2", value="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600")
            
            if st.form_submit_button("إضافة العقار"):
                new_id = f"DH-{len(st.session_state.properties) + 1:03d}"
                st.session_state.properties.append({
                    "id": new_id, "title": p_title, "category": p_cat, "type": p_type,
                    "location": p_loc, "price": p_price, "area": p_area, "rooms": p_rooms,
                    "baths": p_baths, "details": p_details, "images": [img1, img2]
                })
                st.success("تمت الإضافة بنجاح!")
    elif password != "":
        st.error("كلمة المرور خطأ (تجريبي: 1234)")
