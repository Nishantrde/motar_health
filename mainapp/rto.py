import requests
from fake_useragent import UserAgent


def fetch_carinfo(rc_number: str):
    base = "https://www.carinfo.app"
    details_path = f"/rc-details/{rc_number}"
    session = requests.Session()
    session.headers.update({
        "User-Agent": UserAgent().random,
        "Cookie": "deviceId=612907; city=Delhi; cityId=10084; _gcl_au=1.1.1683445272.1749177623; _ga=GA1.1.40683801.1749177623; _clck=8ii65o%7C2%7Cfwj%7C0%7C1983; cto_bundle=9Onvo191NUk2ZFlJcVYyek9KUWxpUkZmdk4lMkZ6RnoydTF6bVJxcEVtVVdJY0x0N0I3cDNMZyUyRnRRYVRSZjZNWU5COGw5UlQ1aHJObkZHSTAwQlUxRmpqWkNzVWd3clJnWUxKTEdqbFpXNWlhOEFxUllwaVUwcCUyRmNpNXRSVEVQRTBtRnlXT01mY2ZIWEVaaW1mVCUyRjZ3YlclMkJSTUdnJTNEJTNE; session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..4J0-5gcsi4XU5MnW.mg2Y20LfDEdwcavy-0vQwSSuIqeUet3y8dNQQ2hyVydBFysK8NSnjbUOYFV4vys9BXUdw6s762mn8DOxttY0ip21QzfxbgL71jZPwMwOhrF3R03Wu2a2JHPwoiLihnwgvtNAC4SMxGMWc1GpObeu_2BKSmpte9K7OlYwLqJufEtd5xom7TzqdzOeNfp--7ibTrw0QwJ7K7szPOb5u15ELhTQVo4bMFDmEzMpu_PgoHee7all1DeCirQzdvVHXn6NEJ6_OkHqJ1HGhQbeeKyvusakimvg5-GZhu27Ue4xDFfhqjClK-eFenzh902a9Ui9N9eu7_u8yOGNL7-bFF1oW31qR5hRq65ygWwQDGpOOn9GHp2iP4avSGt7EtaK4ly-6yj_N0uerWZVrVRzE7UtjF5O8vZfCPkxLwhJgy9SRkHmYmSMi6iNwVc.3yQ7I0Y9iBsTSWlJsrhsEw; _ga_9YYJPTBWLK=GS2.1.s1749192117$o4$g1$t1749192118$j59$l0$h905164356; _clsk=lcufyq%7C1749192120192%7C1%7C0%7Ck.clarity.ms%2Fcollect"
    })

    # 1) Hit the landing page first (in case they drop cookies)
    landing = session.get(base)
    # Optionally check landing.status_code == 200

    # 2) Now request the actual RC details
    resp = session.get(base + details_path)
    if resp.status_code == 200:
        return resp.text
    else:
        raise RuntimeError(
            f"Failed to fetch RC details: status={resp.status_code}, URL={resp.url}"
        )

if __name__ == "__main__":
    try:
        html = fetch_carinfo("JH10BK5078")
        print("Fetched HTML (first 500 chars):\n", html)
        with open("fl.html", "w", encoding="utf-8") as f:
             f.write(html)
    except Exception as e:
        print("Error:", e)



        
