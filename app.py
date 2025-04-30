import streamlit as st


# Function to calculate tax
def calculate_tax(property_value, base_tax_rate, override_percentage):
    base_tax = (property_value / 1000) * base_tax_rate
    override_increase = base_tax * (override_percentage / 100)
    new_tax = base_tax + override_increase
    return new_tax


# Streamlit App Layout
st.title("Massachusetts Property 2.5 Override Calculator")

# User inputs
town = st.text_input("Enter your town:", value="Winchendon")
address = st.text_input("Enter your address:")

# Property value (could be fetched from an API or entered manually)
property_value = st.number_input(
    "Enter the property value (in $):", min_value=1, value=350000
)

override_percentage = st.number_input(
    "Enter the Prop 2.5 Override Percentage:", min_value=0, max_value=100, value=6
)

# Base tax rate (this could be dynamic, fetching values based on the town)
base_tax_rate = 1.2  # Placeholder value, could be dynamically assigned

# Button to calculate the tax
if st.button("Calculate Tax"):
    # Perform the calculation
    new_tax = calculate_tax(property_value, base_tax_rate, override_percentage)

    # Display the result
    st.write(
        f"The estimated additional real estate tax for {address} in {town} is: ${new_tax:,.2f}"
    )
