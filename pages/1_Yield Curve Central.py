import streamlit as st
import datetime 
import pandas as pd
import altair as alt
from utils import date_filter_format

min_date = datetime.date(1990, 1, 2)
today = datetime.date.today()

st.set_page_config(
    page_title = "Welcome to Yield Curve Central", 
    page_icon=":chart_with_upwards_trend:", 
    layout = "wide"
)

########################## Read in Data ##########################

df = pd.read_parquet("./data/yield_curve_historical_rates_MASTER.parquet")

########################## Introduction ##########################

url = "https://github.com/walkerhughes/yieldcentral/tree/main"
st.write('#### :wave: Welcome to Yield Curve Central!\n')
st.write('###### Start exploring below or check out the [GitHub](%s)' % url)

vix_url = "http://vixcentral.com/"
st.write("Inspired by [VixCentral.com](%s), Yield Curve Central is a one-stop solution for your analysis of US Treasury interest rates. Data is scraped daily directly \
         from the US Treasury and processed for easy and robust analysis." % vix_url)

st.write('The US Treasury yield curve plots the interest rates of US Government bonds of different tenures over time. Studying the yield curve can give \
         insights into the time-value of money and the level of perceived risk in the economy. The Federal Reserve Bank affects the interest rates seen \
         here through their Federal Funds Rate, which is set every 3 months at their FOMC meetings. This overnight interest rate sets the tone for longer dated \
         interest in the economy. Since the Fed meets in 3-month intervals to determine short-term rates, their effect on the yield curve is \
         mostly felt in the yields tenured 3 months or less. Longer term yields are affected by another important factor called the \'term premium\'. \
         Directly measuring an interest rate\'s term premium can be tricky, but analyzing the yield curve and the spreads between yields of different tenures \
         can help elucidate how the aggregate economy views the riskiness of debt.\n\n\n')

########################## Plotting On Date ##########################

plot_date = st.date_input(
  label = ':chart_with_upwards_trend: Pick a date to start plotting historical interest rates below', 
  max_value = today, 
  value = datetime.date(2024, 3, 28),
  format = "MM-DD-YYYY"
)

plot_date_cleaned = date_filter_format(plot_date)

df_filtered = df[df["Date"] == plot_date_cleaned].copy() 

df_filtered = df_filtered.drop(columns=["2 Yr - 10 Yr", "2 Yr - 30 Yr", "10 Yr - 30 Yr"])

# st.write("Here's the Yield Curve on ", plot_date)

st.dataframe(df_filtered, use_container_width = True, hide_index = True)

to_plot = df_filtered.melt().iloc[1: ].rename(columns={"variable": "Tenure", "value": "Yield"}).reset_index()

chart = alt.Chart(to_plot).mark_line().encode(
    x=alt.X('Tenure', sort = to_plot.Tenure.values),
    y='Yield', 
    tooltip = ["Tenure", "Yield"]
)

st.altair_chart(chart, use_container_width = True)

########################## Plotting Over Time ##########################

st.write("##### :point_down: Pick a range to plot interest rates and common spreads over time")

start_date = st.date_input(
  label = ":spiral_calendar_pad: Start Date", 
  min_value = min_date, 
  max_value = today,
  value = today - datetime.timedelta(days = 18*31),
  format = "MM-DD-YYYY"
)

end_date = st.date_input(
  label = ":spiral_calendar_pad: End Date", 
  min_value = min_date, 
  max_value = today, 
  value = datetime.date(2024, 3, 28),
  format = "MM-DD-YYYY"
)

start_date_cleaned = date_filter_format(start_date) 
end_date_cleaned = date_filter_format(end_date) 

time_series = df[(df["Date"] >= start_date_cleaned) & (df["Date"] <= end_date_cleaned)].copy()

# plotting months

mo_1 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('1 Mo', sort=time_series.Date.values),
)

mo_2 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('2 Mo', sort=time_series.Date.values),
)

mo_3 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('3 Mo', sort=time_series.Date.values),
)

mo_6 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('6 Mo', sort=time_series.Date.values),
)

# plotting years 

year_1 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('1 Yr', sort=time_series.Date.values),
)

year_2 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('2 Yr', sort=time_series.Date.values),
)

year_5 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('5 Yr', sort=time_series.Date.values),
)

year_7 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('7 Yr', sort=time_series.Date.values),
)

year_10 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('10 Yr', sort=time_series.Date.values),
)

year_20 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('20 Yr', sort=time_series.Date.values),
)

year_30 = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('30 Yr', sort=time_series.Date.values),
)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([
    "1 Month", 
    "2 Month", 
    "3 Month", 
    "6 Month", 
    "1 Year", 
    "2 Year", 
    "5 Year", 
    "7 Year", 
    "10 Year", 
    "20 Year", 
    "30 Year"
  ])

with tab1:
    st.altair_chart(mo_1, use_container_width=True)
with tab2:
    st.altair_chart(mo_2, use_container_width=True)
with tab3:
    st.altair_chart(mo_3, use_container_width=True)
with tab4:
    st.altair_chart(mo_6, use_container_width=True)
with tab5:
    st.altair_chart(year_1, use_container_width=True)
with tab6:
    st.altair_chart(year_2, use_container_width=True)
with tab7:
    st.altair_chart(year_5, use_container_width=True)
with tab8:
    st.altair_chart(year_7, use_container_width=True)
with tab9:
    st.altair_chart(year_10, use_container_width=True)
with tab10:
    st.altair_chart(year_20, use_container_width=True)
with tab11:
    st.altair_chart(year_30, use_container_width=True)

########################## Plotting Yield Spreads ##########################

st.write("Visualizing the differences between interest rates can also be informative. It's not uncommon to hear folks talk about the \'inverting yield curve\' \
         when there is fear of an economic downturn. This generally refers to a short term interest rate like the 3 Month or 2 Year rate being higher than \
         a longer term rate, like the 10 Year rate. \n\n")

st.write("##### :chart_with_upwards_trend: Check out some common yield curve spreads for the date range selected above")

two_ten = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('2 Yr - 10 Yr', sort=time_series.Date.values),
)

two_thirty = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('2 Yr - 30 Yr', sort=time_series.Date.values),
)

ten_thirty = alt.Chart(time_series).mark_line().encode(
    x='Date',
    y=alt.Y('10 Yr - 30 Yr', sort=time_series.Date.values),
)

tab1, tab2, tab3 = st.tabs([
    "2 Yr - 10 Yr", 
    "2 Yr - 30 Yr", 
    "10 Yr - 30 Yr", 
])

with tab1:
    st.altair_chart(two_ten, use_container_width=True)
with tab2:
    st.altair_chart(two_thirty, use_container_width=True)
with tab3:
    st.altair_chart(ten_thirty, use_container_width=True)
