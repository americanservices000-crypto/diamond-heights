import streamlit as st

st.set_page_config(
    page_title="Diamond Heights Real Estate",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling: Luxury Black & Gold Theme with Clean Cards
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
    
    .property-card {
        background-color: #1e1e1e;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        margin-bottom: 35px;
        border: 1px solid #332d11;
        overflow: hidden;
        transition: transform 0.2s;
    }
    
    .property-card:hover {
        border-color: #d4af37;
    }
    
    .property-content {
        padding: 20px;
    }
    
    .property-title {
        font-size: 20px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
    }
    
    .property-location {
        font-size: 14px;
        color: #a0a0a0;
        margin-bottom: 12px;
    }
    
    .property-price {
        font-size: 22px;
        font-weight: 700;
        color: #2ecc71;
        margin-bottom: 15px;
    }
    
    .specs-row {
        display: flex;
        gap: 10px;
        margin-bottom: 15px;
        flex-wrap: wrap;
    }
    
    .spec-badge {
        background-color: #2a2a2a;
        padding: 6px 14px;
        border-radius: 12px;
        font-size: 13px;
        color: #d4af37;
        font-weight: 600;
        border: 1px solid #443810;
        display: inline-flex;
        align-items: center;
        gap: 5px;
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
        padding: 12px 22px;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        z-index: 9999;
        font-weight: bold;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 15px;
    }
    .floating-whatsapp:hover {
        color: white;
    }
    
    .social-icon-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px;
        border-radius: 12px;
        color: white;
        font-weight: bold;
        text-decoration: none;
        font-size: 14px;
        width: 100%;
        gap: 8px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
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
            "details": "شقة بحرية بالكامل، قريبة من الخدمات الرئيسية، الدور الثالث، إضاءة طبيعية ممتازة ومسجلة.",
            "status": "متاح",
            "images": [
                "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800",
                "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800",
                "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800",
                "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800"
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
            "rooms": "مساحة مفتوحة",
            "baths": "1 حمام",
            "details": "محل تجاري حيوي في منطقة تجارية نشطة، واجهة زجاجية عريضة، يصلح لجميع النشاطات.",
            "status": "متاح",
            "images": [
                "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800",
                "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=800",
                "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=800"
            ]
        }
    ]

WHATSAPP_NUMBER = "201030464219"

# Floating WhatsApp
st.markdown(f"""
    <a href="https://wa.me/{WHATSAPP_NUMBER}?text=مرحباً، أود الاستفسار عن عقارات Diamond Heights" target="_blank" class="floating-whatsapp">
        💬 واتساب مباشر
    </a>
""", unsafe_allow_html=True)

st.sidebar.markdown("<h2 style='text-align: center; color: #d4af37;'>Diamond Heights</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #aaa;'>Diamond Heights Real Estate</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio("القائمة الرئيسية", ["🔍 كتالوج العقارات", "🏢 عن الشركة", "⚙️ لوحة الإدارة (Admin)"])

if menu == "🔍 كتالوج العقارات":
    st.markdown("<h1 style='text-align: center;'>كتالوج العقارات - Diamond Heights</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #aaa;'>ابحث عن عقارك المفضل في أرقى مناطق الإسكندرية</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        cat_filter = st.selectbox("التصنيف", ["الكل", "سكني", "تجاري وإداري"])
    with col2:
        type_filter = st.selectbox("النوع", ["الكل", "شقق", "فيلل", "محلات", "مكاتب"])
    with col3:
        loc_filter = st.selectbox("المنطقة", ["الكل", "البيطاش", "العجمي", "سموحة", "لوران", "ميامي"])

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
        for prop in filtered_props:
            with st.container():
                st.markdown('<div class="property-card">', unsafe_allow_html=True)
                
                # Image Gallery Tabs (Clean native Streamlit tabs to flip between 4-5 images seamlessly)
                if 'images' in prop and prop['images']:
                    img_tabs = st.tabs([f"📷 صورة {i+1}" for i in range(len(prop['images']))])
                    for i, tab in enumerate(img_tabs):
                        with tab:
                            st.image(prop['images'][i], use_container_width=True)

                st.markdown('<div class="property-content">', unsafe_allow_html=True)
                st.markdown(f"""
                    <div class="property-title">{prop['title']}</div>
                    <div class="property-location">📍 {prop['location']}</div>
                    <div class="property-price">{prop['price']}</div>
                    
                    <div class="specs-row">
                        <div class="spec-badge">🛏️ {prop['rooms']}</div>
                        <div class="spec-badge">🛁 {prop['baths']}</div>
                        <div class="spec-badge">📐 {prop['area']}</div>
                        <div class="spec-badge">🏷️ {prop['id']}</div>
                    </div>
                    
                    <div style="background-color: #141414; padding: 15px; border-radius: 12px; border: 1px solid #333; margin-bottom: 15px;">
                        <p style="color: #ccc; font-size: 14px; margin: 0;"><b>تفاصيل العقار:</b><br>{prop['details']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Social Media Icon Buttons (No messy text labels)
                wa_msg = f"مرحباً Diamond Heights، مهتم بالعقار ({prop['title']} - الكود: {prop['id']} - بسعر: {prop['price']})"
                wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_msg.replace(' ', '%20')}"
                fb_share = f"https://www.facebook.com/sharer/sharer.php?u=https://ge.com&quote={wa_msg.replace(' ', '%20')}"
                tg_share = f"https://t.me/share/url?url=https://ge.com&text={wa_msg.replace(' ', '%20')}"
                inst_link = f"https://instagram.com"

                b1, b2, b3, b4 = st.columns(4)
                with b1:
                    st.markdown(f'<a href="{wa_link}" target="_blank" class="social-icon-btn" style="background-color: #25D366;">💚 واتساب</a>', unsafe_allow_html=True)
                with b2:
                    st.markdown(f'<a href="{fb_share}" target="_blank" class="social-icon-btn" style="background-color: #1877F2;">💙 فيسبوك</a>', unsafe_allow_html=True)
                with b3:
                    st.markdown(f'<a href="{tg_share}" target="_blank" class="social-icon-btn" style="background-color: #0088cc;">✈️ تليجرام</a>', unsafe_allow_html=True)
                with b4:
                    st.markdown(f'<a href="{inst_link}" target="_blank" class="social-icon-btn" style="background-color: #E1306C;">📸 انستجرام</a>', unsafe_allow_html=True)
                
                st.markdown('</div></div>', unsafe_allow_html=True)

elif menu == "🏢 عن الشركة":
    st.markdown("<h1>عن شركة Diamond Heights Real Estate</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 25px; border-radius: 16px; border: 1px solid #332d11;">
        <h3 style="color: #d4af37;">ريادتنا في سوق العقارات</h3>
        <p style="color: #ccc;">نحن في <b>Diamond Heights Real Estate</b> نتميز بتقديم أفضل الفرص العقارية السكنية والتجارية في أرقى مناطق الإسكندرية.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "⚙️ لوحة الإدارة (Admin)":
    st.markdown("<h1>لوحة الإدارة والتحكم - Diamond Heights</h1>", unsafe_allow_html=True)
    password = st.text_input("كلمة مرور المشرف:", type="password")
    
    if password == "1234":
        st.success("تم تسجيل الدخول بنجاح!")
        with st.form("add_prop"):
            p_title = st.text_input("عنوان العقار")
            p_cat = st.selectbox("التصنيف", ["سكني", "تجاري وإداري"])
            p_type = st.selectbox("النوع", ["شقق", "فيلل", "محلات", "مكاتب"])
            p_loc = st.text_input("المنطقة", value="الإسكندرية • البيطاش")
            p_price = st.text_input("السعر", value="1,500,000 ج.م")
            p_area = st.text_input("المساحة", value="120 م²")
            p_rooms = st.text_input("الغرف", value="3 غرف")
            p_baths = st.text_input("الحمامات", value="1 حمام")
            p_details = st.text_area("التفاصيل والوصف")
            
            img1 = st.text_input("رابط الصورة 1", value="https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=800")
            img2 = st.text_input("رابط الصورة 2", value="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800")
            img3 = st.text_input("رابط الصورة 3 (اختياري)", value="")
            img4 = st.text_input("رابط الصورة 4 (اختياري)", value="")
            
            if st.form_submit_button("إضافة العقار"):
                new_id = f"DH-{len(st.session_state.properties) + 1:03d}"
                imgs = [img1, img2]
                if img3: imgs.append(img3)
                if img4: imgs.append(img4)
                
                st.session_state.properties.append({
                    "id": new_id, "title": p_title, "category": p_cat, "type": p_type,
                    "location": p_loc, "price": p_price, "area": p_area, "rooms": p_rooms,
                    "baths": p_baths, "details": p_details, "images": imgs
                })
                st.success("تمت الإضافة بنجاح!")
    elif password != "":
        st.error("كلمة المرور خطأ (تجريبي: 1234)")
