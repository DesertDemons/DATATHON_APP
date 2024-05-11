# # import streamlit as st
# # import pandas as pd
# # import requests
# # from bs4 import BeautifulSoup
# # import plotly.express as px

# # def scrape_data(url):
# #     try:
# #         response = requests.get(url)
# #         if response.status_code == 200:
# #             soup = BeautifulSoup(response.text, 'html.parser')
# #             table = soup.find('table')  # Simplified: Assumes first table is desired one
# #             if table:
# #                 df = pd.read_html(str(table))[0]
# #                 df.to_csv('downloaded_data.csv', index=False)
# #                 return df, "Data scraped and saved successfully."
# #             else:
# #                 return None, "No table found on the page."
# #         else:
# #             return None, f"Failed to retrieve the page, status code: {response.status_code}"
# #     except Exception as e:
# #         return None, str(e)

# # def load_data():
# #     uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
# #     if uploaded_file is not None:
# #         try:
# #             df = pd.read_csv(uploaded_file, skiprows=6,)
# #             return df
# #         except Exception as e:
# #             st.error(f"Failed to load data: {str(e)}")
# #             return pd.DataFrame()  # Return an empty DataFrame on failure

# # def display_data(df):
# #     if df is not None:
# #         st.write(df)
# #         if st.button('Show Summary Statistics'):
# #             st.write(df.describe())
# #         options = list(df.columns)
# #         column = st.selectbox("Which column do you want to plot?", options)
# #         plot_type = st.selectbox("Select plot type", ['Histogram', 'Line', 'Box Plot'])
# #         if plot_type == 'Histogram':
# #             fig = px.histogram(df, x=column)
# #             st.plotly_chart(fig)
# #         elif plot_type == 'Line':
# #             fig = px.line(df, x=df.index, y=column)
# #             st.plotly_chart(fig)
# #         elif plot_type == 'Box Plot':
# #             fig = px.box(df, y=column)
# #             st.plotly_chart(fig)

# # def main():
# #     st.title("WHO Data Analysis App")
# #     st.subheader("Provide the URL of a webpage to scrape for data or upload a CSV file.")
    
# #     url = st.text_input("Enter the URL of the webpage:")
# #     if url:
# #         df, message = scrape_data(url)
# #         st.success(message)
# #         display_data(df)
# #     else:
# #         df = load_data()
# #         display_data(df)

# # if __name__ == "__main__":
# #     main()


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# def load_data(uploaded_file):
#     if uploaded_file is not None:
#         try:
#             if uploaded_file.name.endswith('.csv'):
#                 df = pd.read_csv(uploaded_file)
#             elif uploaded_file.name.endswith('.xlsx'):
#                 df = pd.read_excel(uploaded_file)
#             else:
#                 st.error("Unsupported file format")
#                 return None
#             return df
#         except Exception as e:
#             st.error(f"Error loading data: {e}")
#             return None
#     return None

# def display_data(df):
#     if df is not None:
#         st.write(df)
#         try:
#             st.write("Basic Descriptive Statistics:")
#             st.write(df.describe())
#         except Exception as e:
#             st.error(f"Error in generating statistics: {e}")

#         try:
#             st.write("Correlation Matrix:")
#             corr_matrix = df.corr()
#             st.write(corr_matrix)
#             fig = px.imshow(corr_matrix)
#             st.plotly_chart(fig)
#         except Exception as e:
#             st.error(f"Error in generating correlation matrix: {e}")

# def plot_custom_charts(df):
#     if df is not None:
#         try:
#             chart_type = st.selectbox("Select the type of chart:", ['Scatter', 'Line', 'Bar', 'Histogram'])
#             columns = df.columns.tolist()
#             x_axis = st.selectbox("Select X axis variable:", columns)
#             y_axis = st.selectbox("Select Y axis variable:", columns)

#             if chart_type == 'Scatter':
#                 fig = px.scatter(df, x=x_axis, y=y_axis)
#             elif chart_type == 'Line':
#                 fig = px.line(df, x=x_axis, y=y_axis)
#             elif chart_type == 'Bar':
#                 fig = px.bar(df, x=x_axis, y=y_axis)
#             elif chart_type == 'Histogram':
#                 fig = px.histogram(df, x=x_axis)
            
#             st.plotly_chart(fig)
#         except Exception as e:
#             st.error(f"Error in generating plot: {e}")

# def main():
#     st.title("Interactive Data Analysis App")
#     uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

#     df = load_data(uploaded_file)
#     display_data(df)
#     plot_custom_charts(df)

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open('your_model.pkl', 'rb'))

# Setting up the title and description
st.title('Total Departure Prediction Tool')
st.write('This tool predicts the "Total Departure" based on tourism and transportation data. Please input the required features.')

# Creating user input fields
year = st.number_input('Year', min_value=2000, max_value=2050, value=2021)
country = st.text_input('Country')
total = st.number_input('Total')
air = st.number_input('Air')
water = st.number_input('Water')
land = st.number_input('Land')
inbound_tourism_expenditure = st.number_input('Inbound Tourism Expenditure in the Country')
inbound_travel = st.number_input('Inbound Travel')
inbound_passenger_transport = st.number_input('Inbound Passenger Transport')
outbound_tourism_expenditure = st.number_input('Outbound Tourism Expenditure in the Country')
outbound_travel = st.number_input('Outbound Travel')
outbound_passenger_transport = st.number_input('Outbound Passenger Transport')

# Prediction button
if st.button('Predict Total Departure'):
    # Collect inputs into a dataframe
    input_df = pd.DataFrame([[year, country, total, air, water, land,
                              inbound_tourism_expenditure, inbound_travel,
                              inbound_passenger_transport, outbound_tourism_expenditure,
                              outbound_travel, outbound_passenger_transport]],
                            columns=['Year', 'Country', 'Total', 'Air', 'Water', 'Land',
                                     'Inbound Tourism expenditure in the country', 'Inbound Travel',
                                     'Inbound Passenger transport',
                                     'Outbound Tourism expenditure in the country', 'Outbound Travel',
                                     'Outbound Passenger transport'])
    # Make prediction
    prediction = model.predict(input_df)
    st.write(f'Predicted Total Departure: {prediction[0]}')

# Optional: Add explanations or further analysis
st.write('This prediction can help identify areas where infrastructure improvements are necessary to enhance tourism facilities usage.')
