# User Management API

A FastAPI-based user management service for handling user data and preferences.

## Prerequisites

- Python 3.8 or higher
- Git
- [uv](https://docs.astral.sh/uv/) for dependency management.


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NYLCloud/ai-engineer-interview.git
   cd ai-engineer-assessment
   ```

2. **Create and activate a virtual environment**
    If uv is not already installed, run the following command and restart the terminal
    ```
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    Create virtual environment
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   uv sync --extra dev
   ```

4. **Set up environment variables**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Ask tech lead for development environment values to connect to development resources

## Running the Application

Start the development server:
```bash
uvicorn src.main:app --reload
```

The application will be available at:
- API: `http://localhost:8000`
- Documentation: `http://localhost:8000/docs`

### Running Tests

```bash
PYTHONPATH=src pytest
```

### Code Quality

```bash
# Code formatting
black .

# Linting
ruff check .

# Type checking
PYTHONPATH=src mypy .
```
---

# Assessment Information
Our intern Dave was feeling particularly creative last Friday afternoon and decided to "improve" the codebase. Let's just say his enthusiasm exceeded his experience. Your mission, should you choose to accept it, is to clean up Dave's masterpiece and make it production-ready. Good luck! 🫡

## Your Tasks

### Add a Health Check Endpoint
Add a `/health` endpoint that returns the application status and database connectivity. This endpoint should:
- Return a 200 status with basic app info when healthy
- Include database connection status
- Handle any connection failures gracefully

### Update User Email Validation  
Modify the create user endpoint to validate email addresses before saving. Requirements:
- Ensure email format is valid before creating users (a valid email will end with @gmail.com, @yahoo.com, or @newyorklife.com)
- Return appropriate error messages for invalid emails
- Update the user model to include proper validation

### Task 3: Request Logging Middleware
Add middleware to log all incoming requests with user info and response times. The middleware should:
- Log request method, path, and timestamp
- Include response time and status code
- Use proper logging instead of print statements


## Evaluation Criteria

- **Code Quality**: How well can you identify and improve code structure and readability?
- **Problem Solving**: Can you systematically identify and resolve issues in existing code?
- **Data Validation**: How do you ensure robust and reliable API data handling?
- **Architecture**: Can you recognize and address design patterns that don't scale?
- **Testing**: How do you validate that your changes work and don't break existing functionality?
- **Professional Workflow**: Do you follow industry best practices for development and deployment?

## Troubleshooting

**Application won't start?**
- Are your environment variables properly loaded? Check what values are being read.
- Is your virtual environment activated and dependencies installed correctly?
- What do the application logs tell you about startup issues?
- Are there any import errors or missing modules?
- Are you ensuring relative or absolute imports?

**Tests failing?**
- Do the test routes match the actual API endpoints in your application?
- Are you running tests with the correct Python path configuration?
- What specific assertions are failing and why might that be?
- Do the test failures indicate real issues in your implementation?

**Code quality tools reporting errors?**
- What patterns do you see in the linting errors? Are there systematic issues?
- How do type checking errors guide you toward missing type annotations?
- Are there unused imports or dead code that should be cleaned up?
- Do the tool outputs suggest architectural improvements?

**Unexpected application behavior?**
- What happens when you test edge cases like missing data or invalid inputs?
- How does the application handle concurrent requests or database operations?
- Are there any console outputs or logs that indicate inefficient patterns?
- What would happen if this application were deployed in a containerized environment?

**Having trouble with specific endpoints?**
- How does the data flow from request to response in your endpoints?
- What validation and error handling exists at each step?
- Are you properly handling different data types and formats?
- How would you debug a request that returns unexpected results?