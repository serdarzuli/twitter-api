# 📢 Twitter API Data Fetcher

🚀 **Real-time Twitter data fetching & analysis with Python!**

## **🔍 Overview**
This project provides an optimized and secure way to interact with the **Twitter API**, allowing users to:
- Fetch **recent tweets** based on keywords or hashtags
- Analyze **user mentions** and interactions
- Retrieve **user details and tweet engagement data**
- Perform **asynchronous API requests** for **faster performance**

This project is designed using **clean code principles**, follows **best practices**, and ensures **secure API key management**.

---
## **📂 Project Structure**
```bash
twitter-api/
│── app/
│   ├── twitter_service.py    # Handles Twitter API operations
│   ├── config.py             # API configuration & secure settings
│
│── tests/
│   ├── test_twitter_service.py # API tests
│
│
│── README.md                  # Project documentation
│── run.py                     # Main application file
│── .env                       # Secure API key storage
│── .gitignore                 # Ignore sensitive files
```

---
## **⚙️ Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/twitter-api.git
cd twitter-api
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**
Create a `.env` file in the root directory and add your **Twitter API Bearer Token**:
```
TWITTER_BEARER_TOKEN=your_secret_token_here
```

### **4️⃣ Run the Application**
```bash
python run.py
```

---
## **📌 Features**
✅ **Real-time Twitter Search** – Fetch tweets based on keywords or hashtags.  
✅ **Asynchronous API Calls** – `aiohttp` ensures faster data retrieval.  
✅ **User Info & Mention Analysis** – Track user interactions and mentions.  
✅ **Secure API Key Management** – Credentials stored safely using `.env`.  
✅ **Modular & Scalable Code** – Clean and maintainable structure.  

---
## **📜 Usage Examples**

### **🔍 Fetch Recent Tweets**
```python
async def search_recent_tweets(self, query: str) -> dict:
    url = f"{self.base_url}/tweets/search/recent"
    params = {"query": query, "tweet.fields": "author_id"}
    return await self._send_request(url, params)
```
```python
from app.twitter_service import TwitterService
import asyncio

async def main():
    twitter = TwitterService()
    query = "from:twitterdev -is:retweet OR #twitterdev"
    tweets = await twitter.search_recent_tweets(query)
    print(tweets)

if __name__ == "__main__":
    asyncio.run(main())
```

---
## **✅ Running Tests**
We use **pytest** for testing API calls.
```bash
pytest tests/
```
Example test case:
```python
@pytest.mark.asyncio
async def test_search_recent_tweets():
    twitter = TwitterService()
    query = "from:twitterdev -is:retweet"
    response = await twitter.search_recent_tweets(query)
    
    assert isinstance(response, dict)
    assert "data" in response
```

---
## **🤝 Contributing**
Contributions are welcome! Feel free to **fork the repo**, create a branch, and submit a pull request.

---
## **📜 License**
This project is open-source and available under the **MIT License**.

