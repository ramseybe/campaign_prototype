# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='About Us', page_icon=':bar_chart:', layout='wide')

# Title
st.title('About Us')

# Content
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = st.columns(14)
# c1.image()
# c2.image()
# c3.image()
# c4.image(Image.open('images/solana-logo.png'))
# c5.image(Image.open('images/avalanche-logo.png'))
# c6.image(Image.open('images/cosmos-logo.png'))
# c7.image(Image.open('images/near-logo.png'))
# c8.image(Image.open('images/flow-logo.png'))
# c9.image(Image.open('images/thorchain-logo.png'))
# c10.image(Image.open('images/osmosis-logo.png'))
# c11.image(Image.open('images/gnosis-logo.png'))
# c12.image(Image.open('images/optimism-logo.png'))
# c13.image(Image.open('images/arbitrum-logo.png'))
# c14.image(Image.open('images/axelar-logo.png'))
st.subheader("Why we did it")
st.write(
    """
    Every election cycle, there are thousands of competitive races that lack financial information that voters could find whether it is on the federal, state, or local level. As a result, the goal of the website is to provide voters with not only the finance for each candidates’ campaigns but allow users to narrow down the campaigns that need money the most. We believe that through this idea, voters will have more access to this information which will allow them to have more choices to vote for. Additionally, candidates who have more funding tend to have more recognition which may affect the voter’s pool of choice. We hope that through this website, candidates with less funding can be made more aware to the voting population.
    """
)

st.subheader('Methodology')
st.write(
    """
    The website currently allows users to select political issues that are important to them. These issues include Gun Control, Public or Private healthcare, Immigration (DACA), Access to Abortion, and Severity of Climate change. After selection, profiles of 2022 House of Representative candidates are shown to the user. The order presented is sorted based off a combination of shared ideologies and closest race, based upon fivethirtyeight.org. After the user finds a candidate, they will have the option to continue to the candidate's website and support them.
    """
)

# st.subheader('Future Works')
# st.write(
#     """
#     This tool is a work in progress and will continue to be developed moving forward. Adding other blockchains,
#     more KPIs and metrics, optimizing the code in general, enhancing the UI/UX of the tool, and more importantly,
#     improving the data pipeline by utilizing [**Flipside ShroomDK**](https://sdk.flipsidecrypto.xyz/shroomdk) are
#     among the top priorities for the development of this app. Feel free to share your feedback, suggestions, and
#     also critics with me.
#     """
# )

# c1, c2, c3 = st.columns(3)
# with c1:
#     st.info('**Data Analyst: [@AliTslm](https://twitter.com/AliTslm)**')
# with c2:
#     st.info('**GitHub: [@alitaslimi](https://github.com/alitaslimi)**')
# with c3:
#     st.info('**Data: [Flipside Crypto](https://flipsidecrypto.xyz)**')
