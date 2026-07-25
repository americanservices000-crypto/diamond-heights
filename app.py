import streamlit as st

st.set_page_config(
    page_title="AEGEAN HEIGHTS Real Estate",
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
    
    .main {
        background-color: #f4f6f9;
    }
    
    .property-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(31, 78, 120, 0.1);
        margin-bottom: 20px;
        border-right: 5px solid #1F4E78;
    }
    
    .stButton>button {
        background-color: #1F4E78;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        border: none;
        padding: 10px;
    }
    
    .stButton>button:hover {
        background-color: #16365c;
        color: white;
    }
    
    h1, h2, h3 {
        color: #1F4E78;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

if 'properties' not in st.session_state:
    st.session_state.properties = [
        {
            "id": "DH-001",
            "title": "شقة سكنية مميزة",
            "category": "سكني",
            "type": "شقق",
            "location": "البيطاش",
            "price": "1,500,000 جنيه",
            "area": "120 م²",
            "details": "شقة سوبر لوكس بحرية قريبة من الخدمات الرئيسية.",
            "status": "متاح",
            "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600"
        },
        {
            "id": "DH-002",
            "title": "محل تجاري حيوي",
            "category": "تجاري وإداري",
            "type": "محلات",
            "location": "لوران",
            "price": "7,000 جنيه / شهرياً",
            "area": "80 م²",
            "details": "محل تجاري واجهة واسعة يصلح لجميع النشاطات التجارية.",
            "status": "متاح",
            "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600"
        }
    ]

st.sidebar.markdown("<h2 style='text-align: center; color: #1F4E78;'>AEGEAN HEIGHTS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #666;'>للإستثمار العقاري وإدارة الأملاك</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio("القائمة الرئيسية", ["🔍 كتالوج العقارات", "🏢 عن الشركة", "⚙️ لوحة الإدارة (Admin)"])

WHATSAPP_NUMBER = "201030464219"

if menu == "🔍 كتالوج العقارات":
    st.markdown("<h1 style='text-align: center;'>الكتالوج العقاري المتميز</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>تصفح أفضل العقارات السكنية والتجارية في الإسكندرية</p>", unsafe_allow_html=True)
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
        filtered_props = [p for p in filtered_props if p["location"] == location_filter]

    if not filtered_props:
        st.info("لا توجد عقارات مطابقة لخيارات البحث الحالية. جرب تغيير فلاتر البحث.")
    else:
        for prop in filtered_props:
            with st.container():
                st.markdown(f"""
                <div class="property-card">
                    <h3>{prop['title']} - {prop['location']}</h3>
                    <p><b>التصنيف:</b> {prop['category']} / {prop['type']} | <b>الكود:</b> {prop['id']}</p>
                    <p><b>المساحة:</b> {prop['area']} | <b>السعر:</b> {prop['price']}</p>
                    <p><b>التفاصيل:</b> {prop['details']}</p>
                    <p style="color: #27ae60; font-weight: bold;">الحالة: {prop['status']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                col_img, col_btn = st.columns([1, 1])
                with col_img:
                    if prop['image']:
                        st.image(prop['image'], use_container_width=True)
                with col_btn:
                    st.markdown("<br>", unsafe_allow_html=True)
                    wa_message = f"مرحباً، مهتم بالعقار ({prop['title']} - الكود: {prop['id']} - بسعر: {prop['price']}) وأود الاستفسار عنه."
                    wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={wa_message.replace(' ', '%20')}"
                    st.markdown(f"""
                        <a href="{wa_link}" target="_blank">
                            <button style="background-color: #25D366; color: white; padding: 12px; border-radius: 8px; border: none; width: 100%; font-weight: bold; cursor: pointer; font-size: 16px;">
                                💬 تواصل عبر الواتساب
                            </button>
                        </a>
                    """, unsafe_allow_html=True)
                st.markdown("---")

elif menu == "🏢 عن الشركة":
    st.markdown("<h1>عن شركة AEGEAN HEIGHTS</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(31, 78, 120, 0.1);">
        <h3>ريادتنا في سوق العقارات</h3>
        <p>نحن في <b>AEGEAN HEIGHTS</b> نتميز بتقديم أفضل الفرص العقارية السكنية والتجارية في أرقى مناطق الإسكندرية. هدفنا هو تسهيل رحلة البحث للعملاء وتقديم خيارات استثمارية آمنة ومدروسة بعناية فائقة.</p>
        <br>
        <h4>خدماتنا:</h4>
        <ul>
            <li>تسويق وإدارة العقارات السكنية (شقق، فيلل، شاليهات).</li>
            <li>توفير المقرات الإدارية والتجارية (مكاتب، محلات، أراضي).</li>
            <li>استشارات عقارية احترافية تلبي تطلعات المستثمرين.</li>
        </ul>
        <br>
        <p><b>للتواصل المباشر:</b> اتصل بنا أو راسلنا عبر الواتساب على الرقم: <b>+201030464219</b></p>
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
                p_title = st.text_input("عنوان العقار (مثال: شقة بحرية تشطيب لوكس)")
                p_cat = st.selectbox("التصنيف الرئيسي", ["سكني", "تجاري وإداري"])
                
                if p_cat == "سكني":
                    p_type = st.selectbox("نوع العقار", ["شقق", "فيلل", "شاليهات"])
                else:
                    p_type = st.selectbox("نوع العقار", ["مكاتب", "أدوار إدارية", "محلات", "أراضي"])
                
                p_loc = st.selectbox("منطقة الإسكندرية", [
                    "البيطاش", "العجمي", "سموحة", "لوران", "ميامي", 
                    "المنتزه", "سيدي بشر", "كليوباترا", "محطة الرمل", "الابراهيمية", "سبورتنج", "المندرة"
                ])
                p_price = st.text_input("السعر (مثال: 1,500,000 جنيه أو 7,000 جنيه / شهرياً)")
                p_area = st.text_input("المساحة (مثال: 120 م²)")
                p_details = st.text_area("تفاصيل العقار والمميزات")
                p_status = st.selectbox("حالة العقار", ["متاح", "تم البيع", "تم الإيجار"])
                p_image = st.text_input("رابط صورة العقار (Image URL)", placeholder="https://...")
                
                submit_btn = st.form_submit_button("إضافة العقار للمنصة")
                
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
                        "details": p_details,
                        "status": p_status,
                        "image": p_image if p_image else "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600"
                    }
                    st.session_state.properties.append(new_property)
                    st.success(f"تمت إضافة العقار برقم الكود '{new_id}' بنجاح!")
        
        with tab2:
            st.subheader("حذف أو تعديل العقارات")
            if not st.session_state.properties:
                st.info("لا توجد عقارات مضافة حالياً.")
            else:
                prop_ids = [p['id'] + " - " + p['title'] for p in st.session_state.properties]
                selected_to_delete = st.selectbox("اختر العقار للحذف", prop_ids)
                
                if st.button("حذف العقار المختار"):
                    target_id = selected_to_delete.split(" - ")[0]
                    st.session_state.properties = [p for p in st.session_state.properties if p['id'] != target_id]
                    st.success("تم حذف العقار بنجاح! قم بتحديث الصفحة لمشاهدة التغييرات.")
                    st.rerun()
    elif password != "":
        st.error("كلمة المرور غير صحيحة. (كلمة المرور الافتراضية للتجربة هي: 1234)")
