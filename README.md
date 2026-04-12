# AI Travel Assistant

This project is a full-stack AI-powered travel assistant application consisting of a Python Flask backend and an Angular frontend.

## Prerequisites

- Python 3.8 or higher
- Node.js 18 or higher
- npm (comes with Node.js)
- Git

## Backend Setup

### Installation

1. Navigate to the backend directory:
   ```
   cd my-travel-assistant-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Copy the `.env` file and update the API keys:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `GOOGLE_API_KEY`: Your Google API key
   - `TAVILY_API_KEY`: Your Tavily API key
   - `LANGSMITH_API_KEY`: Your Langsmith API key (optional for tracing)
   - `AWS_BEARER_TOKEN_BEDROCK`: Your AWS Bedrock API key

   **Note:** Never commit your actual API keys to version control. Use placeholder values or environment variables.

### Running the Backend

1. Ensure the virtual environment is activated.
2. Run the Flask application:
   ```
   python app.py
   ```
   The backend will start on `http://localhost:5000` (default Flask port).

## Frontend Setup

### Installation

1. Navigate to the frontend directory:
   ```
   cd my-travel-assistant-frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

### Configuration

The frontend is configured to communicate with the backend at `http://localhost:5000`. If you need to change this, update the API endpoints in `src/app/chat.service.ts`.

### Running the Frontend

1. Start the development server:
   ```
   npm start
   ```
   or
   ```
   ng serve --open
   ```
   The frontend will start on `http://localhost:4200` and open in your browser.

### Building for Production

To build the frontend for production:
```
npm run build
```
The build artifacts will be stored in the `dist/` directory.

## Usage

1. Start the backend server.
2. Start the frontend development server.
3. Open your browser to `http://localhost:4200`.
4. Interact with the AI travel assistant through the chat interface.

## Project Structure

- `my-travel-assistant-backend/`: Python Flask backend
  - `app.py`: Main Flask application
  - `chatbot.py`: AI chatbot logic
  - `requirements.txt`: Python dependencies
  - `.env`: Environment variables (API keys)
- `my-travel-assistant-frontend/`: Angular frontend
  - `src/app/`: Angular components and services
  - `package.json`: Node.js dependencies and scripts

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test thoroughly.
5. Submit a pull request.

## License

This project is licensed under the MIT License.