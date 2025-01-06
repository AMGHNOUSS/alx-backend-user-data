
# 0x01. Basic authentication

Project done during **Full Stack Software Engineering studies** at **ALX School**. It aims to learn about: 
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Technologies
* Scripts written in Bash 5.1.16
* Tested on Ubuntu 20.04 LTS
* Python 3.11.9

## Files

| Filename | Description |
| -------- | ----------- |
| `README.md` | 0. Simple-basic-API |
| `api/v1/app.py, api/v1/views/index.py` | 1. Error handler: Unauthorized |
| `api/v1/app.py, api/v1/views/index.py` | 2. Error handler: Forbidden |
| `api/v1/auth, api/v1/auth/__init__.py, api/v1/auth/auth.py` | 3. Auth class |
| `api/v1/auth/auth.py` | 4. Define which routes don't need authentication |
| `api/v1/app.py, api/v1/auth/auth.py` | 5. Request validation! |
| `api/v1/app.py, api/v1/auth/basic_auth.py` | 6. Basic auth |
| `api/v1/auth/basic_auth.py` | 7. Basic - Base64 part |
| `api/v1/auth/basic_auth.py` | 8. Basic - Base64 decode |
| `api/v1/auth/basic_auth.py` | 9. Basic - User credentials |
| `api/v1/auth/basic_auth.py` | 10. Basic - User object |
| `api/v1/auth/basic_auth.py` | 11. Basic - Overload current_user - and BOOM! |
| `api/v1/auth/basic_auth.py` | 12. Basic - Allow password with ":" |
| `api/v1/auth/auth.py` | 13. Require auth with stars |
