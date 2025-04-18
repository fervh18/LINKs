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
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                    <path d="M8.051 1.999h.089c..."/>  <!-- usa tu path original completo acá -->
                </svg>  
                {label}
            </a>
        </p>'''
    
    elif icon == 'spotify':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-success btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-spotify" viewBox="0 0 16 16">
                    <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.669 11.055a.532.532 0 0 1-.73.176 6.531 6.531 0 0 0-6.078-.37.532.532 0 0 1-.442-.97 7.595 7.595 0 0 1 7.064.43.532.532 0 0 1 .186.734zm.993-2.014a.665.665 0 0 1-.91.22 8.717 8.717 0 0 0-8.122-.494.665.665 0 1 1-.554-1.21 10.048 10.048 0 0 1 9.353.57.665.665 0 0 1 .233.914zm.112-2.055a.797.797 0 0 1-1.09.264 10.892 10.892 0 0 0-10.15-.6.797.797 0 1 1-.64-1.462 12.389 12.389 0 0 1 11.526.686.797.797 0 0 1 .354 1.112z"/>
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
