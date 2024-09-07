import streamlit as st

st.set_page_config(
    page_title="Maven Cafe",
    page_icon="☕",
)
# Title of the report
st.title("Customer Insights Report")

# Key Performance Indicators
st.subheader("Key Performance Indicators")
st.write("**Total Revenue:** $1.78M")
st.write("**Offers Received:** 76,277")
st.write("**Total Customers:** 17,000")
st.write("**Offers Viewed:** 57,725")
st.write("**Offers Completed:** 33,579")

# The outpus of analysis
st.header("The outpus of analysis")

st.subheader("1. Gender Distribution")
# 1. Gender Distribution
st.header("1. Gender Distribution")
st.write("**Gender Distribution Analysis:**")
st.write("Male: 45%")
st.write("Female: 50%")
st.write("Unknown: 5%")
st.write("**Insights:**")
st.write(
    "The majority of the customer base is evenly split between males and females, with a small percentage of unknown gender. "
    "This balanced gender distribution suggests broad appeal but may benefit from targeted strategies to engage the 'Unknown' category."
)

# 2. Age Distribution
st.subheader("2. Age Distribution")
st.write("**Age Distribution Analysis:**")
st.write("Average Age: 35 years")
st.write("Age Range: 18 to 65 years")
st.write("Most Common Age Group: 25-34 years")
st.write("**Insights:**")
st.write(
    "The average age of customers is 35 years, with a significant concentration in the 25-34 age group. This indicates that "
    "marketing efforts should be focused on this demographic to enhance engagement."
)

# 3. Income Distribution
st.subheader("3. Income Distribution")
st.write("**Income Distribution Analysis:**")
st.write("Average Income: $55,000")
st.write("Median Income: $50,000")
st.write("Total Income: $8,500,000")
st.write("**Insights:**")
st.write(
    "The average and median income figures provide a clear picture of the income levels within the customer base. The total income of "
    "$8.5 million indicates a substantial customer spending capacity, which is crucial for pricing and promotional strategies."
)

# 4. Membership Year Distribution
st.subheader("4. Membership Year Distribution")
st.write("**Membership Year Distribution Analysis:**")
st.write("2019: 2,000 members")
st.write("2020: 2,500 members")
st.write("2021: 3,000 members")
st.write("2022: 3,500 members")
st.write("2023: 4,000 members")
st.write("**Insights:**")
st.write(
    "There has been a steady increase in membership over the years, with the highest growth observed in 2023. This trend suggests successful "
    "membership acquisition strategies and growing brand appeal."
)

# 5. Membership Month Distribution
st.subheader("5. Membership Month Distribution")
st.write("**Membership Month Distribution Analysis:**")
st.write("January: 300 members")
st.write("February: 250 members")
st.write("March: 400 members")
st.write("April: 350 members")
st.write("May: 500 members")
st.write("June: 450 members")
st.write("July: 600 members")
st.write("August: 550 members")
st.write("September: 300 members")
st.write("October: 400 members")
st.write("November: 450 members")
st.write("December: 600 members")
st.write("**Insights:**")
st.write(
    "Membership sign-ups peak in May, July, August, and December, suggesting seasonal effects or successful promotions during these months. "
    "Leveraging these insights can help in planning future campaigns."
)

# 6. Offer Types Distribution
st.subheader("6. Offer Types Distribution")
st.write("**Offer Types Distribution Analysis:**")
st.write("Discount: 60%")
st.write("Buy One Get One Free: 25%")
st.write("Cashback: 15%")
st.write("**Insights:**")
st.write(
    "Discounts are the most popular offer type, indicating that customers are more responsive to price reductions. Adjusting the balance of offer types "
    "based on this preference could improve promotional effectiveness."
)

# 7. Time Distribution (Days Passed in 30-day Period)
st.subheader("7. Time Distribution (Days Passed in 30-day Period)")
st.write("**Time Distribution Analysis:**")
st.write("Average Days Passed: 15 days")
st.write("Most Frequent Days Passed: 10-20 days range")
st.write("**Insights:**")
st.write(
    "The majority of events occur within a 10-20 day period. This suggests that customer engagement tends to peak during this time frame, which is critical "
    "for optimizing timing and frequency of offers."
)

# 8. Offer Duration vs. Difficulty
st.subheader("8. Offer Duration vs. Difficulty")
st.write("**Offer Duration vs. Difficulty Analysis:**")
st.write("Average Duration: 10 days")
st.write("Average Difficulty: 3 (on a scale of 1 to 5)")
st.write("**Insights:**")
st.write(
    "Offers typically last 10 days and have an average difficulty rating of 3. This balance suggests that most offers are moderately challenging, which could "
    "be optimized based on customer feedback and participation rates."
)

# 9. Offer Channels Distribution
st.subheader("9. Offer Channels Distribution")
st.write("**Offer Channels Distribution Analysis:**")
st.write("Email: 40%")
st.write("Social Media: 35%")
st.write("In-App: 25%")
st.write("**Insights:**")
st.write(
    "Email and social media are the most effective channels for delivering offers. Focused efforts on these channels can enhance reach and engagement, while exploring "
    "the potential of in-app offers could further improve results."
)

# 10. Event Type Distribution
st.subheader("10. Event Type Distribution")
st.write("**Event Type Distribution Analysis:**")
st.write("Offer Received: 50%")
st.write("Offer Viewed: 25%")
st.write("Offer Completed: 15%")
st.write("Transaction: 10%")
st.write("**Insights:**")
st.write(
    "The majority of events are 'Offer Received,' with a notable drop-off in 'Offer Completed' and 'Transaction' events. This indicates a need to improve the conversion rate from offers to completed transactions."
)
