import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# Your endpoints
BASE_URL = "http://127.0.0.1:8000"
INDEX_URL = BASE_URL + "/"
POST_URL  = BASE_URL + "/RC_info"

# The payload you want every request to send
PAYLOAD = {"text": "JH10BK5078"}

def init_session():
    """Hit the index page to get a valid CSRF cookie."""
    sess = requests.Session()
    # This GET must render a template with {% csrf_token %}, so Django sets the cookie
    resp = sess.get(INDEX_URL)
    resp.raise_for_status()
    return sess

def make_request(session, idx):
    """Send one POST and return (idx, status, response-or-error)."""
    # grab the CSRF token
    csrftoken = session.cookies.get("csrftoken", "")
    headers = {
        "Content-Type":  "application/json",
        "X-CSRFToken":   csrftoken,
        "Referer":       INDEX_URL,
    }

    try:
        resp = session.post(POST_URL, 
                             headers=headers, 
                             data=json.dumps(PAYLOAD),
                             timeout=10)
        resp.raise_for_status()
        return idx, resp.status_code, resp.json()
    except Exception as e:
        # if it's an HTTPError, capture its status code
        code = None
        if hasattr(e, 'response') and e.response is not None:
            code = e.response.status_code
        return idx, code, str(e)

def main():
    session = init_session()

    # tune max_workers to your machine; too many threads can overwhelm things
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [
            executor.submit(make_request, session, i)
            for i in range(1, 101)
        ]
        for future in as_completed(futures):
            idx, status, result = future.result()
            print(f"[#{idx:03d}] → status={status!s}, result={result!r}")

if __name__ == "__main__":
    main()
