
# Google Sheets Search Query Processor

## 📖 Overview
This project automates the process of fetching top search results from Google based on search queries stored in a Google Sheet. It utilizes **SerpAPI** for search results and **Google Sheets API** for reading and writing data.

## 🚀 Features
- Reads search queries from a Google Sheet.
- Fetches top search results using **SerpAPI**.
- Stores the results in adjacent columns in the same sheet.
- Skips already processed rows and unwanted domains.
- Configurable to retrieve more than 2 results.

## 📋 Requirements
- Python 3.7+
- A **Google Cloud** service account with Sheets API enabled.
- A **SerpAPI** key.

## 📂 Installation

1. **Clone this repository**:
   ```sh
   git clone https://github.com/DataDiggerJay/SERP-results_scrappig
   cd your-repo
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 🔑 Setup

### **1. Enable Google Sheets API**
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project (or use an existing one).
- Enable **Google Sheets API** and **Google Drive API**.
- Create a **service account**, download the JSON key file, and place it in your project folder.

### **2. Share Your Google Sheet**
- Open your Google Sheet.
- Share it with the service account email found in the JSON file.

### **3. Get a SerpAPI Key**
- Sign up at [SerpAPI](https://serpapi.com/).
- Generate an API key and store it securely.

## ⚙️ Configuration
- Update the `fetch_search_results.py` script:
  ```python
  SERP_API_KEY = "your_api_key_here"  # Replace with your actual API key
  ```
- Update the Google Sheets credentials file path:
  ```python
  creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
  ```
- Modify `START_ROW` and `NUM_ROWS` to process specific rows in the sheet.

## 🏃‍♂️ Running the Script
Execute the script with:
```sh
python fetch_search_results.py
```

## 🛠️ Customization
### **To get more than 2 results**
Modify the `num_results` variable in `fetch_search_results.py`:
```python
num_results = 5  # Fetch 5 results instead of 2
```
Ensure your Google Sheet has enough columns to store additional results.

## 🤝 Contributing
Feel free to submit **pull requests** or open **issues** for improvements.

## 📜 License
This project is licensed under the **MIT License**.

## ✨ Author
[Your Name](https://github.com/DataDiggerJay)
```


