import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    if icon == 'youtube':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-danger btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="black" class="bi bi-youtube" viewBox="0 0 16 16">
                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                </svg>  
                {label}
            </a>
        </p>'''

   elif icon == 'applemusic':
    button_code = f'''
    <p>
        <a href="{url}" class="btn btn-outline-dark btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8.018 2.014c-.401.047-.795.104-1.182.182-.27.058-.464.303-.464.578v14.658a1.833 1.833 0 0 1-.182.793c-.17.379-.456.707-.818.95a3.57 3.57 0 0 1-2.278.603c-.63-.052-1.188-.238-1.602-.547a1.9 1.9 0 0 1-.701-.955 2.05 2.05 0 0 1 .174-1.4c.287-.582.842-1.061 1.596-1.369a4.03 4.03 0 0 1 1.55-.297c.383.02.772.076 1.167.17V7.232a17.97 17.97 0 0 1 1.068-.305 23.6 23.6 0 0 1 2.018-.407c.676-.11 1.332-.172 1.968-.18a3.23 3.23 0 0 1 1.857.464c.546.332.88.837.973 1.448.057.37.08.718.07 1.044-.016.447-.084.898-.197 1.355a6.07 6.07 0 0 1-.772 1.76 5.19 5.19 0 0 1-1.63 1.53 6.62 6.62 0 0 1-2.013.756v4.072a1.83 1.83 0 0 1-.184.793c-.172.38-.457.707-.818.951a3.57 3.57 0 0 1-2.278.603c-.63-.052-1.188-.238-1.602-.547a1.9 1.9 0 0 1-.7-.956 2.05 2.05 0 0 1 .173-1.399c.287-.583.842-1.062 1.596-1.37a4.03 4.03 0 0 1 1.55-.296c.384.019.772.076 1.167.17v-5.47c.008-.572.31-1.007.73-1.325a2.91 2.91 0 0 1 1.122-.504c.408-.098.788-.174 1.14-.226.086-.013.17-.028.254-.043a.087.087 0 0 0 .07-.082.089.089 0 0 0-.095-.085c-.373.012-.744.04-1.113.085a14.4 14.4 0 0 0-1.675.309 6.91 6.91 0 0 0-.88.287V2.682a.622.622 0 0 0-.722-.617z"/>
            </svg>
            {label}
        </a>
    </p>'''

   

    else:
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-secondary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''

    return button_code
