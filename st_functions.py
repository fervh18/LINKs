import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">', unsafe_allow_html=True)

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

    elif icon == 'spotify':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-success btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="green" class="bi bi-spotify" viewBox="0 0 16 16">
                    <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.669 11.055a.532.532 0 0 1-.73.176 6.531 6.531 0 0 0-6.078-.37.532.532 0 0 1-.442-.97 7.595 7.595 0 0 1 7.064.43.532.532 0 0 1 .186.734zm.993-2.014a.665.665 0 0 1-.91.22 8.717 8.717 0 0 0-8.122-.494.665.665 0 1 1-.554-1.21 10.048 10.048 0 0 1 9.353.57.665.665 0 0 1 .233.914zm.112-2.055a.797.797 0 0 1-1.09.264 10.892 10.892 0 0 0-10.15-.6.797.797 0 1 1-.64-1.462 12.389 12.389 0 0 1 11.526.686.797.797 0 0 1 .354 1.112z"/>
                </svg>  
                {label}
            </a>
        </p>'''

  


    elif icon == 'applemusic':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-dark btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="red" class="bi bi-apple" viewBox="0 0 16 16">
                    <path d="M11.07 1.93a3.37 3.37 0 0 1-1.003 2.59 3.1 3.1 0 0 1-2.332 1.086h-.014a3.41 3.41 0 0 1-.014-.507A3.288 3.288 0 0 1 9.588 1.5c.566 0 1.096.197 1.482.43zm1.494 4.573c-.036-.034-1.307-.72-2.727-.236-1.144.384-1.892 1.413-2.233 2.077-.307.6-.829 1.617-.285 2.788.524 1.125 1.717 2.496 2.984 2.455 1.17-.034 1.627-.753 3.063-.753 1.42 0 1.826.753 3.042.722 1.264-.03 2.07-1.194 2.591-2.317.454-.973.639-1.922.651-1.974-.015-.007-1.692-.64-1.707-2.527-.016-1.576 1.226-2.319 1.283-2.35-.706-1.02-1.805-1.134-2.18-1.148-1.094-.087-2.144.637-2.703.637-.557 0-1.424-.617-2.347-.599a4.456 4.456 0 0 0-3.591 2.042C6.395 7.2 6.217 8.167 6.234 8.2c-.01.01-1.224.458-1.236 1.793-.012 1.273.973 2.27 1.608 2.869.51.492 1.113.959 1.908.939.747-.02 1.033-.49 2.031-.49 1.002 0 1.257.49 2.041.476.818-.014 1.334-.49 1.847-.99.581-.56.793-1.13.803-1.155-.02-.01-1.476-.559-1.492-2.206-.015-1.433 1.002-2.144 1.052-2.176-.601-.85-1.529-1.057-1.852-1.071z"/>
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
