# Login Automation Solution

## Project Overview
Automated login validation using Python, pytest, and requests with secure credential handling and full git integration.

## Setup Instructions
1. Install Python 3.11.
2. Clone this repository.
3. Copy `.env.template` to `.env` and fill in your LOGIN_URL, LOGIN_EMAIL, LOGIN_PASSWORD.
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration Steps
- Store your credentials in a `.env` file (never commit secrets).
- Use environment variables for sensitive data.

## Usage Guidelines
- Run tests:
   ```sh
   pytest Tests/login_test.py --maxfail=1 --disable-warnings -v
   ```
- Test results are displayed in the console. Use `pytest --junitxml=results.xml` for CI integration.

## Maintenance Procedures
- Update scripts in `Tests/` for new test cases.
- Update `.env.template` if new variables are required.
- Keep dependencies in `requirements.txt` up to date.

## Repository Structure
- `Tests/login_test.py`: Login automation test script
- `.env.template`: Example environment variable setup
- `README.md`: This documentation
- `requirements.txt`: Python dependencies
- `login_test.metadata.json`: Metadata for DevOps integration

## Security Best Practices
- Never commit `.env` files or secrets.
- Use environment variables and CI/CD secret management.
- Review code for hardcoded credentials before merging.

## Extending Automation
- Add new test cases to `Tests/`.
- Modularize test logic for scalability.
- Integrate with GitHub Actions for automated CI/CD.
