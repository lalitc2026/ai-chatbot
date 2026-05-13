# AI Travel Assistant

This project is a full-stack AI-powered travel assistant application consisting of a Python Flask backend and an Angular frontend. The backend application leverages the LangChain and LangGraph frameworks.

## Salient Features

- Trip itinerary generation and travel planning assistance
- Flight search powered by Travel MCP Server integration
- Tavily Search integration for general search
- AI tools and dynamic models for agentic decision-making
- Summarization middleware for concise response generation
- External MCP Server connectivity via MCP client
- User chat memory management for better conversational continuity

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

1. Create the `.env` file and update the API keys as needed:
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

```
ai-chatbot/
├── README.md
├── my-travel-assistant-backend/
│   ├── app.py                          # Main Flask application
│   ├── chatbot.py                      # AI chatbot logic
│   ├── dynamic_model_middleware.py     # Dynamic model middleware
│   ├── flight_search.py                # Flight search functionality
│   ├── web_search.py                   # Web search integration
│   └── requirements.txt                # Python dependencies
└── my-travel-assistant-frontend/
    ├── angular.json                    # Angular configuration
    ├── package.json                    # Node.js dependencies and scripts
    ├── tsconfig.json                   # TypeScript configuration
    ├── tsconfig.app.json               # Application-specific TypeScript config
    └── src/
        ├── index.html                  # Main HTML file
        ├── main.ts                     # Angular bootstrap file
        ├── polyfills.ts                # Angular polyfills
        ├── styles.scss                 # Global styles
        ├── app/
        │   ├── app.component.html      # Root component template
        │   ├── app.component.scss      # Root component styles
        │   ├── app.component.ts        # Root component logic
        │   ├── app.module.ts           # Root module
        │   └── chat.service.ts         # Chat service for API communication
        └── environments/
            ├── environment.ts          # Development environment config
            └── environment.prod.ts     # Production environment config
```

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test thoroughly.
5. Submit a pull request.

## License

This project is licensed under the MIT License.