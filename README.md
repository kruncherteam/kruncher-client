# Kruncher Client

![Kruncher Logo](https://kruncher.ai/images/brand/header-logo.svg)

Kruncher Client is a Python library for interacting with [Kruncher](https://kruncher.ai) data, allowing users to seamlessly access and analyze structured information.

Kruncher is a cutting-edge Data & AI platform designed to streamline investment processes for venture capitalists, incubators, and business angels. It transforms complex data into actionable insights, enhancing decision-making. 

Register to [kruncher.ai](https://kruncher.ai) and create new project and analysis of documents and company!
Contact us at [info@kruncher.ai](mailto:info@kruncher.ai) to explore how Kruncher can elevate your investment strategy.

---

## 📚 Google Colab Demo

You can explore the Kruncher Client with our interactive Google Colab notebook:

[Open in Google Colab](https://colab.research.google.com/drive/1XQv0EyXnjN8XKHKJOiTtiCHnVykzpcmY?usp=sharing)

---

## 🚀 Installation

To install the `kruncherclient` library, use pip:

```bash
pip install kruncherclient
```
---

## 🔑 API Key Setup

To use the Kruncher API, an API key is required. Follow these steps to obtain it:

1. Log in to your account on [kruncher.ai](https://kruncher.ai) with an **owner/admin** account.
2. Navigate to **Settings**.
3. Go to **Integrations**.
4. Copy the `KRUNCHER_API_KEY` and store it securely.

Save it in a `.env` file within your project directory:

```ini
KRUNCHER_API_KEY=your_api_key_here
```

Or set it as an environment variable:

```bash
export KRUNCHER_API_KEY=your_api_key_here
```

---

## 📖 Usage

To use the `KruncherClient`, either pass the API key directly when initializing the client or ensure it is set in your environment variables.

### ✅ Basic Example

```python
from kruncher import KruncherClient

# Initialize the client with the API key
client = KruncherClient(api_key='your_api_key_here')

# Alternatively, if the API key is set in the .env file, initialize without arguments
client = KruncherClient()

# Fetch projects
projects_json = client.get_projects(page=0)
print(projects_json)

# Fetch projects as a DataFrame
projects_df = client.get_projects_df_full(page=0)
print(projects_df)

# Fetch analysis details
analysis_id = 'your_analysis_id_here'
analysis_details = client.get_analysis_detail(analysis_id=analysis_id)
print(analysis_details)

# Fetch analysis details as json object containing different pre-built dataframes
analysis_detail_df = get_analysis_detail_df(analysis_id=analysis_id)
print(analysis_detail_df)

# Fetch analysis details as complete dataframe row with 200+ datapoints
analysis_df_full = get_analysis_df_full(analysis_id=analysis_id)
print(analysis_df_full)

```

---

## 📌 Features

- 🔍 **Retrieve projects** from Kruncher API.
- 📊 **Fetch projects as a DataFrame** for easy analysis.
- 📈 **Get analysis details** using an `analysis_id`.
- 🔒 **Secure API key storage** via `.env` file or environment variables.

---

## ❓ Need Help?

For any issues, feel free to reach out:

- 📧 **Support**: [info@kruncher.ai](mailto:info@kruncher.ai)
- 🛠 **GitHub Issues**: [Report Issues](https://github.com/your-repo/issues)

Enjoy using `kruncherclient`! 🚀

