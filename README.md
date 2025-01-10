# rag_test

## Description

**rag_test** just a basic rag code for easy implementation whenever necessary, if you find useful dont heistate to star and use it 😉. It includes scripts for data ingestion, configuration management, and application deployment. This repository serves as a foundation for building and deploying RAG (Retrievel Augmented Generation).

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/harvind-here/rag_test.git
   cd rag_test
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Configure Environment Variables**

   Create a `.env` file in the root directory and add the necessary environment variables. Example:

   ```env
   DATABASE_URL=your_database_url
   GROQ_API_KEY=your_secret_key
   ```


2. **Run Database Setup**

   I used Docker Qdrant repo for storing embedded data locally, You can go and store in other DB websites like Chroma, Qdrant cloud, etc... if you want. To do what I did check this url             
   "https://hub.docker.com/r/qdrant/qdrant"  or run this command if you have docker desktop,

   ```bash
   docker pull qdrant/qdrant
   ```

## Usage

1. **Start the Application**

   ```bash
   python app.py
   ```

2. **Ingest Data**

   To ingest data using the `db_config.py` script:

   ```bash
   python db_config.py
   ```

3. **Access the Application**

   Once the application is running, navigate to `http://localhost:6333` in your web browser [adjust the port as necessary]. I used the docker Qdrant repo for hosting and serving the embedded database locally.
## Configuration

- **app.py**: Main application script.
- **db_config.py**: Database configuration settings.
- **ingest.py**: Data ingestion script.
- **raft_state.json**: Maintains the state for raft consensus [if applicable].
- **c:/Users/harvi/Codebases/aiui/athenai-new/app.py**: Additional application script.
- **c:/Users/harvi/Codebases/aiui/athenai-new/config/settings.py**: Configuration settings for the application.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**
