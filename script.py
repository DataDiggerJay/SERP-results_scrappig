import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

# Step 1: Set up Google Sheets API
# - Create a service account in Google Cloud Console.
# - Share your Google Sheet with the service account email.
# - Download the JSON credentials file and place it in your project directory.

# Authenticate and open the spreadsheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet by title or URL
sheet = client.open("Your Google Sheet Name").sheet1  # Adjust accordingly

# Step 2: Define configuration variables
HEADER_ROW = 1
START_ROW = 2107  # Change this if you want to start at a different row
NUM_ROWS = 80  # Number of rows to process

# Get headers and find "Search Query" column
headers = sheet.row_values(HEADER_ROW)
try:
    query_col_index = headers.index("Search Query") + 1  # Convert to 1-based index
except ValueError:
    raise Exception("Column with header 'Search Query' not found.")

# Define result column indexes
result_col_start_index = query_col_index + 1  # First result column
num_results = 2  # Default is 2, but you can change it (see below for how to get more)

# Fetch queries from the sheet
queries = sheet.col_values(query_col_index)[START_ROW - 1: START_ROW - 1 + NUM_ROWS]

# Step 3: Fetch search results from SerpAPI
# - Go to https://serpapi.com/
# - Sign up and generate an API key
# - Store your API key securely (e.g., use environment variables or a .env file)
SERP_API_KEY = "your_api_key_here"  # Replace with your SerpAPI key

for i, query in enumerate(queries):
    row_index = START_ROW + i

    # Skip empty queries
    if not query.strip():
        continue

    # Check if the row is already processed
    processed = any(sheet.cell(row_index, result_col_start_index + j).value for j in range(num_results))
    if processed:
        print(f"Skipping row {row_index} (already processed).")
        continue

    # Skip queries containing certain domains
    if any(domain in query for domain in ["blogspot.com", "medium.com", "blogger.com"]):
        print(f"Skipping row {row_index} (contains undesired domain: {query}).")
        continue

    # Prepare API request
    url = f"https://serpapi.com/search.json?engine=google&q={requests.utils.quote(query)}&api_key={SERP_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        results = response.json()

        # Extract search results (change num_results to get more results)
        top_results = results.get("organic_results", [])[:num_results]

        # Write results to the sheet
        for j, result in enumerate(top_results):
            sheet.update_cell(row_index, result_col_start_index + j, result.get("link", ""))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching results for row {row_index}: {e}")

print("Processing complete.")
