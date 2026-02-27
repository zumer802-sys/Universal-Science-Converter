import streamlit as st

st.set_page_config(page_title="Universal Science Converter", page_icon="⚗️")
st.title("⚗️ Universal Science Converter")
st.subheader("Convert units across Chemistry, Physics, Math, and Biology")

# --------------------
# HELPER FUNCTIONS
# --------------------
def convert_units(value, from_unit, to_unit, unit_dict):
    return value * unit_dict[from_unit] / unit_dict[to_unit]

# -------------------------
# SIDEBAR
# -------------------------
category = st.sidebar.selectbox(
    "Select Category",
    ["Chemistry", "Physics", "Math", "Biology"]
)

# -------------------------
# CHEMISTRY
# -------------------------
if category == "Chemistry":
    st.header("🧪 Chemistry Conversions")
    chem_choice = st.selectbox(
        "Select Chemistry Conversion",
        ["Mass", "Volume", "Moles"]
    )

    # MASS
    if chem_choice == "Mass":
        units = {
            "Ton (t)":1e6, "kg":1e3, "g":1, "mg":1e-3,
            "µg":1e-6, "ng":1e-9, "pg":1e-12
        }
        val = st.number_input("Value:", min_value=0.0)
        u1 = st.selectbox("From", list(units.keys()))
        u2 = st.selectbox("To", list(units.keys()))
        if st.button("Convert Mass"):
            r = convert_units(val, u1, u2, units)
            st.success(f"{val} {u1} = {r:.12g} {u2}")

    # VOLUME
    elif chem_choice == "Volume":
        units = {
            "m³":1000, "L":1, "mL":1e-3, "µL":1e-6, "nL":1e-9
        }
        val = st.number_input("Value:", min_value=0.0)
        u1 = st.selectbox("From", list(units.keys()))
        u2 = st.selectbox("To", list(units.keys()))
        if st.button("Convert Volume"):
            r = convert_units(val, u1, u2, units)
            st.success(f"{val} {u1} = {r:.12g} {u2}")

    # MOLES
    elif chem_choice == "Moles":
        units = {
            "mol":1, "mmol":1e-3, "µmol":1e-6, "nmol":1e-9, "pmol":1e-12
        }
        val = st.number_input("Value:", min_value=0.0)
        u1 = st.selectbox("From", list(units.keys()))
        u2 = st.selectbox("To", list(units.keys()))
        if st.button("Convert Moles"):
            r = convert_units(val, u1, u2, units)
            st.success(f"{val} {u1} = {r:.12g} {u2}")

# -------------------------
# PHYSICS
# -------------------------
elif category == "Physics":
    st.header("⚡ Physics Conversions")
    phys = st.selectbox("Type", ["Length", "Time", "Speed", "Force", "Energy"])
        
    if phys == "Length":
        units = {"km":1e3, "m":1, "cm":1e-2, "mm":1e-3, "µm":1e-6, "nm":1e-9}
    elif phys == "Time":
        units = {"h":3600, "min":60, "s":1, "ms":1e-3, "µs":1e-6}
    elif phys == "Speed":
        units = {"m/s":1, "km/h":1000/3600, "mph":1609.34/3600}
    elif phys == "Force":
        units = {"N":1, "dyne":1e-5, "kgf":9.80665}
    else:
        units = {"J":1, "kJ":1e3, "cal":4.184, "kcal":4184}

    val = st.number_input("Value", min_value=0.0)
    u1 = st.selectbox("From", list(units.keys()))
    u2 = st.selectbox("To", list(units.keys()))
    if st.button("Convert Physics"):
        r = convert_units(val, u1, u2, units)
        st.success(f"{val} {u1} = {r:.12g} {u2}")

# -------------------------
# MATH
# -------------------------
elif category == "Math":
    st.header("📐 Math Conversions")
    m = st.selectbox("Type", ["Angle", "Area", "Volume", "Temperature"])

    if m == "Angle":
        units = {"°":1, "rad":3.14159265359/180, "gon":0.9}
    elif m == "Area":
        units = {"m²":1, "km²":1e6, "cm²":1e-4, "ha":1e4}
    elif m == "Volume":
        units = {"m³":1, "L":1e-3, "mL":1e-6}
    else:
        units = None

    val = st.number_input("Value", min_value=0.0)
    if m != "Temperature":
        u1 = st.selectbox("From", list(units.keys()))
        u2 = st.selectbox("To", list(units.keys()))
        if st.button("Convert Math"):
            r = convert_units(val, u1, u2, units)
            st.success(f"{val} {u1} = {r:.12g} {u2}")
    else:
        from_u = st.selectbox("From", ["C", "F", "K"])
        to_u = st.selectbox("To", ["C", "F", "K"])
        if st.button("Convert Temperature"):
            if from_u == "C":
                c = val
            elif from_u == "F":
                c = (val - 32)*5/9
            else:
                c = val - 273.15
            if to_u == "C":
                res = c
            elif to_u == "F":
                res = (c*9/5)+32
            else:
                res = c + 273.15
            st.success(f"{val} {from_u} = {res:.2f} {to_u}")

# -------------------------
# BIOLOGY
# -------------------------
elif category == "Biology":
    st.header("🧬 Biology Conversions")
    bio_choice = st.selectbox("Type", ["Mass", "Volume", "Concentration"])

    if bio_choice == "Mass":
        units = {"g":1, "mg":1e-3, "µg":1e-6, "ng":1e-9, "pg":1e-12}
    elif bio_choice == "Volume":
        units = {"L":1, "mL":1e-3, "µL":1e-6, "nL":1e-9}
    else:
        units = {"M":1, "mM":1e-3, "µM":1e-6, "nM":1e-9}

    val = st.number_input("Value", min_value=0.0)
    u1 = st.selectbox("From", list(units.keys()))
    u2 = st.selectbox("To", list(units.keys()))
    if st.button("Convert Biology"):
        r = convert_units(val, u1, u2, units)
        st.success(f"{val} {u1} = {r:.12g} {u2}")