import pandas as pd
import googlemaps

# Replace with your own Google Maps API key
gmaps = googlemaps.Client(key='AIzaSyCl7yPcnmda506d_zUDj89bgFEij0fdfUU')

# Load the businesses from the construtoras.xlsx file
df = pd.read_excel('construtoras.xlsx', sheet_name='Sheet1')

# Create an empty DataFrame to store the addresses
address_df = pd.DataFrame(columns=['Business', 'Address'])

# Loop through each business and get its address
for i in range(len(df)):
    business = df.iloc[i]['Business']
    geocode_result = gmaps.geocode(business)
    if geocode_result:
        address = geocode_result[0]['formatted_address']
        address_df = address_df.append({'Business': business, 'Address': address}, ignore_index=True)
    else:
        address_df = address_df.append({'Business': business, 'Address': 'Not found'}, ignore_index=True)

# Export the addresses to a new file
address_df.to_excel('address.xlsx', index=False)
