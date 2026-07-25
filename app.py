import streamlit as st

st.set_page_config(
    page_title="AEGEAN HEIGHTS Real Estate",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling: Luxury Black & Gold Theme with Floating WhatsApp
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    /* Luxury Black & Gold Background */
    .stApp {
        background-color: #0f0f0f;
        color: #e5e5e5;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #141414;
        border-left: 1px solid #d4af37;
    }
    
    /* Property Card Style (Black & Gold Theme) */
    .property-card {
        background-color: #1a1a1a;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(212, 175, 55, 0.15);
        margin-bottom: 25px;
        border: 1px solid #333;
        overflow: hidden;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
    }
    
    @media(max-width: 768px) {
        .property-card {
            flex-direction: column;
        }
    }
    
    .card-image {
        width: 35%;
        object-fit: cover;
        min-height: 220px;
    }
    
    .card-content {
        width: 65%;
        padding: 20px;
    }
    
    @media(max-width: 768px) {
        .card-image, .card-content {
            width: 100%;
        }
    }
    
    .property-title {
        font-size: 18px;
        font-weight: 700;
        color: #d4af37;
        margin-bottom: 8px;
    }
    
    .property-location {
        font-size: 14px;
        color: #aaa;
        margin-bottom: 10px;
    }
    
    .property-price {
        font-size: 20px;
        font-weight: 700;
        color: #f39c12;
        margin-bottom: 12px;
    }
    
    .specs-container {
        display: flex;
        gap: 8px;
        margin-bottom: 12px;
        flex-wrap: wrap;
    }
    
    .spec-badge {
        background-color: #262626;
        padding: 5px 10px;
        border-radius: 6px;
        font-size: 12px;
        color: #d4af37;
        font-weight: 600;
        border: 1px solid #444;
    }
    
    h1, h2, h3 {
        color: #d4af37 !important;
        font-weight: 700;
    }
    
    /* Floating WhatsApp Button */
    .floating-whatsapp {
        position: fixed;
        bottom: 25px;
        left: 25px;
        background-color: #25D366;
        color: white;
        border-radius: 50px;
        padding: 12px 20px;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        z-index: 9999;
        font-weight: bold;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 15px;
        transition: transform 0.2s;
    }
    .floating-whatsapp:hover {
        transform: scale(1.05);
        color: white;
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
            "details": "شقة بحرية قريبة من الخدمات الرئيسية.",
            "status": "متاح",
            "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800"
        },
        {
            "id": "DH-002",
            "title": "محل تجاري واجهة واسعة",
            "category": "تجاري وإداري",
            "type": "محلات",
            "location": "الإسكندرية • لوران",
            "price": "7,000 ج.م / شهرياً",
            "area": "80 م²",
            "rooms": "مساحة مفتوحة",
            "baths": "1 حمام",
            "details": "محل تجاري حيوي يصلح لجميع النشاطات.",
            "status": "متاح",
            "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800"
        }
    ]

WHATSAPP_NUMBER = "201030464219"

# Floating WhatsApp Button visible all the time
st.markdown(f"""
    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=مرحباً، أود الاستفسار عن خدمات وعقارات شركة AEGEAN HEIGHTS" target="_blank" class="floating-whatsapp">
        💬 تواصل معنا واتساب
    </a>
""", unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='text-align: center; color: #d4af37;'>AEGEAN HEIGHTS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #aaa;'>للإستثمار العقاري وإدارة الأملاك</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio("القائمة الرئيسية", ["🔍 كتالوج العقارات", "🏢 عن الشركة", "⚙️ لوحة الإدارة (Admin)"])

if menu == "🔍 كتالوج العقارات":
    st.markdown("<h1 style='text-align: center;'>الكتالوج العقاري المتميز</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>تصفح أفضل العقارات السكنية والتجارية في الإسكندرية</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        cat_filter = st.selectbox("التصنيف الرئيسي", ["الكل", "سكني", "تجاري وإداري"])
    
    with col2:
        if cat_filter == "سكني":
            type_options = ["الكل", "شقق", "فيلل", "شاليهات"]
        elif cat_filter == "تجاري وإداري":
            type_options = ["الكل", "مكاتب", "أدوار إدارية", "محلات", "أراضي"]
        else:
            type_options = ["الكل", "شقق", "فيلل", "شاليهات", "مكاتب", "أدوار إدارية", "محلات", "أراضي"]
        
        type_filter = st.selectbox("نوع العقار", type_options)

    with col3:
        alex_locations = [
            "الكل", "البيطاش", "العجمي", "سموحة", "لوران", "ميامي", 
            "المنتزه", "سيدي بشر", "كليوباترا", "محطة الرمل", "الابراهيمية", "سبورتنج", "المندرة"
        ]
        location_filter = st.selectbox("منطقة الإسكندرية", alex_locations)

    st.markdown("<br>", unsafe_allow_html=True)

    filtered_props = st.session_state.properties
    if cat_filter != "الكل":
        filtered_props = [p for p in filtered_props if p["category"] == cat_filter]
    if type_filter != "الكل":
        filtered_props = [p for p in filtered_props if p["type"] == type_filter]
    if location_filter != "الكل":
        filtered_props = [p for p in filtered_props if location_filter in p["location"]]

    if not filtered_props:
        st.info("لا توجد عقارات مطابقة لخيارات البحث الحالية.")
    else:
        for prop in filtered_props:
            wa_msg = f"مرحباً، مهتم بالعقار ({prop['title']} - الكود: {prop['id']} - بسعر: {prop['price']})"
            wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(' ', '%20')}"
            fb_share = f"https://www.facebook.com/sharer/sharer.php?u=https://ge.com&quote={wa_msg.replace(' ', '%20')}"
            
            st.markdown(f"""
            <div class="property-card">
                <img src="{prop['image']}" class="card-image">
                <div class="card-content">
                    <div class="property-title">{prop['title']}</div>
                    <div class="property-location">📍 {prop['location']}</div>
                    <div class="property-price">{prop['price']}</div>
                    
                    <div class="specs-container">
                        <div class="spec-badge">🛏️ {prop['rooms']}</div>
                        <div class="spec-badge">🛁 {prop['baths']}</div>
                        <div class="spec-badge">📐 {prop['area']}</div>
                        <div class="spec-badge">🏷️ {prop['id']}</div>
                    </div>
                    
                    <p style="color: #ccc; font-size: 13px; margin-bottom: 12px;">{prop['details']}</p>
                    
                    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                        <a href="{wa_link}" target="_blank" style="background-color: #25D366; color: white; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: bold;">💬 واتساب</a>
                        <a href="{fb_share}" target="_blank" style="background-color: #1877F2; color: white; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: bold;">📘 مشاركة فيس بوك</a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif menu == "🏢 عن الشركة":
    st.markdown("<h1>عن شركة AEGEAN HEIGHTS</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #1a1a1a; padding: 25px; border-radius: 16px; border: 1px solid #333;">
        <h3 style="color: #d4af37;">ريادتنا في سوق العقارات</h3>
        <p style="color: #ccc;">نحن في <b>AEGEAN HEIGHTS</b> نتميز بتقديم أفضل الفرص العقارية السكنية والتجارية في أرقى مناطق الإسكندرية.</p>
        <br>
        <p style="color: #d4af37;"><b>للتواصل المباشر:</b> راسلنا عبر الواتساب على الرقم: <b>+201030464219</b></p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "⚙️ لوحة الإدارة (Admin)":
    st.markdown("<h1>لوحة الإدارة والتحكم</h1>", unsafe_allow_html=True)
    password = st.text_input("أدخل كلمة مرور المشرف (Admin Password):", type="password")
    
    if password == "1234":
        st.success("تم تسجيل الدخول بنجاح للمدير!")
        
        tab1, tab2 = st.tabs(["➕ إضافة عقار جديد", "🗑️ إدارة العقارات الحالية"])
        
        with tab1:
            st.subheader("إضافة عقار جديد للكتالوج")
            with st.form("add_prop_form"):
                p_title = st.text_input("عنوان العقار")
                p_cat = st.selectbox("التصنيف الرئيسي", ["سكني", "تجاري وإداري"])
                p_type = st.selectbox("نوع العقار", ["شقق", "فيلل", "شاليهات", "محلات", "مكاتب"])
                p_loc_name = st.selectbox("منطقة الإسكندرية", ["البيطاش", "العجمي", "سموحة", "لوران", "ميامي", "المنتزه", "سيدي بشر"])
                p_loc = f"الإسكندرية • {p_loc_name}"
                p_price = st.text_input("السعر (مثال: 1,500,000 ج.م)")
                p_area = st.text_input("المساحة (مثال: 120 م²)")
                p_rooms = st.text_input("عدد الغرف", value="3 غرف")
                p_baths = st.text_input("عدد الحمامات", value="1 حمام")
                p_details = st.text_area("تفاصيل العقار")
                p_image = st.text_input("رابط صورة العقار (Image URL)")
                
                submit_btn = st.form_submit_button("إضافة العقار")
                
                if submit_btn:
                    new_id = f"DH-{len(st.session_state.properties) + 1:03d}"
                    new_property = {
                        "id": new_id,
                        "title": p_title,
                        "category": p_cat,
                        "type": p_type,
                        "location": p_loc,
                        "price": p_price,
                        "area": p_area,
                        "rooms": p_rooms,
                        "baths": p_baths,
                        "details": p_details,
                        "status": "متاح",
                        "image": p_image if p_image else "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800"
                    }
                    st.session_state.properties.append(new_property)
                    st.success("تمت إضافة العقار بنجاح!")
        
        with tab2:
            st.subheader("حذف العقارات")
            if not st.session_state.properties:
                st.info("لا توجد عقارات مضافة حالياً.")
            else:
                prop_ids = [p['id'] + " - " + p['title'] for p in st.session_state.properties]
                selected_to_delete = st.selectbox("اختر العقار للحذف", prop_ids)
                
                if st.button("حذف العقار المختار"):
                    target_id = selected_to_delete.split(" - ")[0]
                    st.session_state.properties = [p for p in st.session_state.properties if p['id'] != target_id]
                    st.success("تم الحذف بنجاح!")
                    st.rerun()
    elif password != "":
        st.error("كلمة المرور غير صحيحة (التجريبية: 1234)")
