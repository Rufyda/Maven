import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast

# Streamlit app configuration
st.set_page_config(
    page_title="Maven Cafe",
    page_icon="☕",
)

# Load the CSV files
customers_df = pd.read_csv('customers.csv')
events_df = pd.read_csv('events.csv')
offers_df = pd.read_csv('offers.csv')

# Convert became_member_on to datetime and extract month and year
customers_df['became_member_on'] = pd.to_datetime(customers_df['became_member_on'], format='%Y%m%d')
customers_df['membership_year'] = customers_df['became_member_on'].dt.year
customers_df['membership_month'] = customers_df['became_member_on'].dt.month

# Handle missing values in 'gender' and 'income'
customers_df['gender'].fillna('Unknown', inplace=True)
customers_df['income'].fillna(0, inplace=True)  # Fill missing income with 0

# Cleaning the events data: Extract the offer id, amount, and reward from the value column
def extract_event_details(value):
    try:
        value_dict = ast.literal_eval(value)
        return value_dict.get('offer id', None), value_dict.get('amount', None), value_dict.get('reward', None)
    except (ValueError, SyntaxError):
        return None, None, None

events_df['offer_id'], events_df['amount'], events_df['reward'] = zip(*events_df['value'].apply(extract_event_details))
events_df.drop(columns=['value'], inplace=True)

# Convert time from hours to days
events_df['days_passed'] = events_df['time'] / 24

# Set up the Streamlit dashboard
st.title('Customer Insights Dashboard')

# Metrics calculation
total_customers = customers_df['customer_id'].nunique()
offers_received = events_df[events_df['event'] == 'offer received'].shape[0]
total_revenue = events_df[events_df['event'] == 'transaction']['amount'].sum()
offers_viewed = events_df[events_df['event'] == 'offer viewed'].shape[0]
offers_completed = events_df[events_df['event'] == 'offer completed'].shape[0]

# Convert total revenue to millions
total_revenue_million = total_revenue / 1_000_000
# Display KPIs
st.subheader('Key Performance Indicators')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric(label="Total Revenue", value=f"${total_revenue_million:,.2f}M")
with col2:
    st.metric(label="Offers Received", value=offers_received)
with col3:
    st.metric(label="Total Customers", value=total_customers)
with col4:
    st.metric(label="Offers Viewed", value=offers_viewed)
with col5:
    st.metric(label="Offers Completed", value=offers_completed)

# Sidebar for filtering
st.sidebar.header('Filter Options')
gender_filter = st.sidebar.multiselect('Gender', options=customers_df['gender'].unique(), default=customers_df['gender'].unique())
offer_type_filter = st.sidebar.multiselect('Offer Type', options=offers_df['offer_type'].unique(), default=offers_df['offer_type'].unique())
year_filter = st.sidebar.multiselect('Membership Year', options=customers_df['membership_year'].unique(), default=customers_df['membership_year'].unique())

# Apply filters to customers and offers
filtered_customers_df = customers_df[
    (customers_df['gender'].isin(gender_filter)) &
    (customers_df['membership_year'].isin(year_filter))
]
filtered_offers_df = offers_df[offers_df['offer_type'].isin(offer_type_filter)]

# Merge filtered event data with filtered customers data
filtered_events_with_customers = pd.merge(events_df, filtered_customers_df, on='customer_id', how='inner')

# Merge filtered event data with offer data
merged_df = pd.merge(filtered_events_with_customers, filtered_offers_df, on='offer_id', how='left')

# Calculate Income Statistics
average_income = f"${filtered_customers_df['income'].mean():,.2f}"
median_income = f"${filtered_customers_df['income'].median():,.2f}"
total_income = f"${filtered_customers_df['income'].sum():,.2f}"

# Customer Demographics: Gender Distribution (Pie Chart)
st.subheader('Gender Distribution')
gender_counts = filtered_customers_df['gender'].value_counts()
fig, ax = plt.subplots()
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set1'), startangle=90)
ax.axis('equal')
ax.set_title('Gender Distribution')
st.pyplot(fig)

# Customer Demographics: Age Distribution
st.subheader('Age Distribution')
fig, ax = plt.subplots()
sns.histplot(filtered_customers_df['age'].dropna(), kde=True, bins=30, color='brown', ax=ax)
ax.set_title('Age Distribution')
st.pyplot(fig)

# Customer Demographics: Income Distribution
st.subheader('Income Distribution')
fig, ax = plt.subplots()
sns.histplot(filtered_customers_df['income'], kde=True, bins=30, color='green', ax=ax)
ax.set_title('Income Distribution')
st.pyplot(fig)

# Membership Analysis: Membership Year Distribution
st.subheader('Membership Year Distribution')
fig, ax = plt.subplots()
sns.countplot(x='membership_year', data=filtered_customers_df, palette='Set1', ax=ax)
ax.set_title('Membership Year Distribution')
st.pyplot(fig)

# Membership Analysis: Membership Month Distribution
st.subheader('Membership Month Distribution')
fig, ax = plt.subplots()
sns.countplot(x='membership_month', data=filtered_customers_df, palette='Set1', ax=ax)
ax.set_title('Membership Month Distribution')
st.pyplot(fig)

# Offer Effectiveness: Offer Types Distribution
st.subheader('Offer Types Distribution')
fig, ax = plt.subplots()
sns.countplot(x='offer_type', data=merged_df, palette='Set1', ax=ax)
ax.set_title('Offer Types Distribution')
st.pyplot(fig)

# Visualize the Time Distribution (days passed in the 30-day period)
st.subheader('Time Distribution (Days Passed in 30-day Period)')
fig, ax = plt.subplots()
sns.histplot(filtered_events_with_customers['days_passed'], kde=True, bins=30, color='purple', ax=ax)
ax.set_title('Time Distribution over 30 Days')
ax.set_xlabel('Days Passed')
ax.set_ylabel('Event Count')
st.pyplot(fig)

# Offer Duration vs Difficulty Visualization
st.subheader('Offer Duration vs. Difficulty')
offers_with_durations = pd.merge(filtered_offers_df, filtered_events_with_customers, on='offer_id', how='inner')
fig, ax = plt.subplots()
sns.scatterplot(x='duration', y='difficulty', data=offers_with_durations, hue='offer_type', palette='Set1', ax=ax)
ax.set_title('Offer Duration vs. Difficulty (Filtered by Offer Type, Gender, Year)')
ax.set_xlabel('Offer Duration (Days)')
ax.set_ylabel('Offer Difficulty')
st.pyplot(fig)

# Channel Distribution Visualization
st.subheader('Offer Channels Distribution')
offers_df['channels'] = offers_df['channels'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
exploded_offers_df = offers_df.explode('channels')
offers_with_channels = pd.merge(exploded_offers_df, filtered_events_with_customers, on='offer_id', how='inner')
fig, ax = plt.subplots()
sns.countplot(x='channels', data=offers_with_channels, hue='offer_type', palette='Set1', ax=ax)
ax.set_title('Offer Channels Distribution (Filtered by Offer Type, Gender, Year)')
st.pyplot(fig)

# Event Type Distribution connected with all filters
st.subheader('Event Type Distribution (Filtered by Offer Type, Gender, Year)')
fig, ax = plt.subplots()
sns.countplot(x='event', data=filtered_events_with_customers, palette='Set1', ax=ax)
ax.set_title('Event Type Distribution (Filtered by Offer Type, Gender, Year)')
ax.set_xlabel('Event Type')
ax.set_ylabel('Count')
st.pyplot(fig)
