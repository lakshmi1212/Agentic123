# Login Automation Solution

## Project Overview
Automated Python pytest script for secure login validation with requests, robust error handling, documentation, and automated git deployment. Ready for DevOps pipelines.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/lakshmi1212/Agentic123.git
   cd Agentic123
   ```
2. **Install Python 3.11** (required version).
3. **Create and activate a virtual environment**:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure environment variables**:
   - Copy `.env.template` to `.env` and fill in your actual credentials.
   - Export variables or use a tool like `python-dotenv`.

## Configuration Steps
- Set the following variables in your environment:
  - `LOGIN_URL`: Login API endpoint URL
  - `LOGIN_EMAIL`: Email for authentication
  - `LOGIN_PASSWORD`: Password for authentication

## Usage Guidelines
- Run the tests:
  ```bash
  pytest Tests/login_test.py --maxfail=1 --disable-warnings -v
  ```
- Results will appear in the terminal. For advanced reporting, integrate with JUnit or HTML plugins as needed.

## Maintenance Procedures
- Update scripts and tests in `Tests/` as needed.
- Never commit real secrets to the repository.
- Update dependencies in `requirements.txt` and metadata as required.
- Extend tests by adding new pytest functions in `Tests/login_test.py`.

## Troubleshooting
- Ensure all environment variables are set and valid.
- Check network connectivity to the login URL.
- Review logs for error messages and failed assertions.

## Security Notice
- Credentials are parameterized via environment variables for security.
- No secrets are hardcoded.
- .env files should be excluded from version control (see .gitignore).

## CI/CD Integration
- Recommended: Add GitHub Actions workflow to automate testing on push/PR.

## Contact
For support, open an issue in the repository.
