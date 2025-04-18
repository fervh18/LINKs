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
                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
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

    elif icon == 'applemusic':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-dark btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" viewBox="0 0 384 512" fill="currentColor">
                    <path d="M318.7 268.7c-24.4 0-54.4 16.3-71.6 39.1-11.4 15.6-21.4 39.6-14.3 62.9 3.7 12.3 16.5 28.2 30.4 28.7 13.5.4 21.2-4.2 32.6-10.3 11.2-6 21.5-12.3 33.6-12 11.2.3 22 5.7 28.4 14.6l.2.3c.2.3 1.3 2.1 3 5.3 1.9 3.5 2.7 4.9 3.5 6.9 3.3 8.3 5.2 19.2 4.3 30.4-2.2 26.8-15.8 52.2-40.2 71.3-21.8 16.6-49.2 24.5-75.5 21.7-32.5-3.5-62.6-21.7-81.2-49.6-19.4-29.1-24.2-69.4-12.4-103.6 11.1-32.2 34.2-59.6 64-76.7 27.4-15.8 56.3-20.6 74.7-20.6 2.8 0 5.4.1 7.7.3 1.8.2 3.6.4 5.3.7l2.5.3c.5.1.8.1 1.1.2 1.2.2 2.4.5 3.5.7l.5.1c2.6.6 4.8 1.1 6.8 1.6.1 0 .1 0 .1.1h.1l.1.1c-.1.3-.3.6-.4.9-7.6 19.6-23.9 29.1-38.9 29.1z"/>
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
