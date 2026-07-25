
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Diamond Heights Real Estate", page_icon="🏠", layout="wide")

st.markdown('''
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #1F4E78; }
    .stButton>button { background-color: #1F4E78; color: white; border-radius: 5px; }
    </style>
''', unsafe_allow_html=True)

st.title("🏠 Diamond Heights Real Estate")
st.markdown("### دليلك لأرقى العقارات والفرص الاستثمارية")

@st.cache_data
def load_data():
    data = {
        'الكود': ['DH-001', 'DH-002', 'DH-003', 'DH-004'],
        'النوع الرئيسي': ['سكني', 'تجاري', 'سكني', 'تجاري'],
        'النوع الفرعي': ['شقة', 'محل', 'فيلا', 'مكتب'],
        'المنطقة': ['البيطاش', 'لوران', 'برج العرب', 'البيطاش'],
        'السعر': [1500000, 7000, 5500000, 3200000],
        'المساحة': [120, 80, 400, 250],
        'الغرف': [3, 1, 6, 5],
        'الحالة': ['متاح', 'متاح', 'متاح', 'مباع'],
        'الصورة': [
            'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2',
            'https://images.unsplash.com/photo-1582063289852-62e3ba2747f8',
            'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9',
            'https://images.unsplash.com/photo-1497366216548-37526070297c'
        ],
        'التفاصيل': ['شقة سوبر لوكس بحرية', 'محل تجاري حيوي', 'فيلا بحديقة خاصة', 'مقر إداري فخم']
    }
    return pd.DataFrame(data)

df = load_data()

menu = st.sidebar.radio("القائمة الرئيسية", ["🏠 كتالوج العقارات", "ℹ️ عن الشركة", "🔐 لوحة الإدارة (Admin)"])

if menu == "🏠 كتالوج العقارات":
    st.markdown("## 📋 كتالوج الوحدات العقارية")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        main_type = st.selectbox("التصنيف الرئيسي", ["الكل", "سكني", "تجاري"])
    with col2:
        areas = ["الكل"] + list(df['المنطقة'].unique())
        selected_area = st.selectbox("المنطقة", areas)
    with col3:
        status_filter = st.selectbox("الحالة", ["الكل", "متاح", "مباع"])
        
    filtered_df = df.copy()
    if main_type != "الكل":
        filtered_df = filtered_df[filtered_df['النوع الرئيسي'] == main_type]
    if selected_area != "الكل":
        filtered_df = filtered_df[filtered_df['المنطقة'] == selected_area]
    if status_filter != "الكل":
        filtered_df = filtered_df[filtered_df['الحالة'] == status_filter]
        
    for index, row in filtered_df.iterrows():
        with st.container():
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(row['الصورة'], use_column_width=True)
            with c2:
                st.subheader(f"{row['النوع الفرعي']} - {row['المنطقة']}")
                st.write(f"**الكود:** {row['الكود']} | **المساحة:** {row['المساحة']} م² | **السعر:** {row['السعر']:,} جنيه")
                st.write(f"**التفاصيل:** {row['التفاصيل']}")
                
                if row['الحالة'] == 'متاح':
                    st.success(f"الحالة: {row['الحالة']}")
                else:
                    st.error(f"الحالة: {row['الحالة']}")
                    
                wa_text = f"مرحباً، مهتم بالعقار رقم {row['الكود']} في {row['المنطقة']} بسعر {row['السعر']}"
                st.markdown(f"[💬 تواصل للحجز أو الاستعلام عبر واتساب](https://wa.me/201000000000?text={wa_text})", unsafe_allow_html=True)
            st.divider()

elif menu == "ℹ️ عن الشركة":
    st.markdown("## 🏢 عن شركة Diamond Heights")
    st.write("نحن في Diamond Heights نقدم لك أرقى الخيارات العقارية (سكني، إداري، تجاري). نلتزم بالاحترافية، الشفافية، ومستوى خدمة يليق بعملائنا.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("⭐ عقارات متميزة ومختارة بعناية")
    with col2:
        st.info("📍 مواقع استراتيجية وحيوية")
    with col3:
        st.info("🤝 شفافية كاملة وأمان في التعاقد")

elif menu == "🔐 لوحة الإدارة (Admin)":
    st.markdown("## 🔐 تسجيل دخول الإدارة")
    password = st.text_input("كلمة مرور الأدمن", type="password")
    
    if password == "1234":
        st.success("تم تسجيل الدخول بنجاح كـ Admin!")
        
        tab1, tab2 = st.tabs(["📊 إدارة العقارات", "📈 التحليلات"])
        
        with tab1:
            st.subheader("إضافة عقار جديد")
            with st.form("add_form"):
                new_code = st.text_input("كود العقار")
                new_main = st.selectbox("التصنيف الرئيسي", ["سكني", "تجاري"])
                new_sub = st.text_input("النوع الفرعي (شقة، محل، إلخ)")
                new_area = st.text_input("المنطقة")
                new_price = st.number_input("السعر", min_value=0)
                new_size = st.number_input("المساحة (م²)", min_value=0)
            
                new_status = st.selectbox("الحالة", ["متاح", "مباع"])
                new_img = st.text_input("رابط الصورة")
                new_desc = st.text_area("التفاصيل الإضافية")
                
                submit = st.form_submit_button("إضافة العقار")
                if submit:
                    st.success(f"تم إضافة العقار {new_code} بنجاح!")
                    
            st.subheader("قائمة العقارات الحالية")
            st.dataframe(df)
            
        with tab2:
            st.subheader("📊 لوحة تحليلات المشاهدات")
            st.metric(label="إجمالي المشاهدات", value="1,240 زيارة")
            st.metric(label="مشاهدات اليوم", value="45 زيارة")
            st.bar_chart(df.set_index('الكود')['المساحة'])
    elif password != "":
        st.error("كلمة المرور غير صحيحة!")
