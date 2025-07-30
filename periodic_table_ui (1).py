
import streamlit as st

def render_periodic_table(elemen_periodik):
    selected = st.session_state.get("selected_elements", [])

    cols = st.columns(18)
    for unsur in elemen_periodik:
        col = cols[unsur["posisi"]["x"] - 1]
        if unsur["simbol"] in selected:
            btn = col.button(unsur["simbol"], key=unsur["simbol"], help=unsur["nama"])
        else:
            btn = col.button(unsur["simbol"], key=unsur["simbol"], help=unsur["nama"])

        if btn:
            if unsur["simbol"] in selected:
                selected.remove(unsur["simbol"])
            elif len(selected) < 2:
                selected.append(unsur["simbol"])
            st.session_state["selected_elements"] = selected
            st.experimental_rerun()

    return selected
