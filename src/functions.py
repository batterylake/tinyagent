import json
import requests
from bs4 import BeautifulSoup

# Weather Example
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

# ReAct Wikipedia Example

# Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.

# def clean_str(p):
#   return p.encode().decode("unicode-escape").encode("latin1").decode("utf-8")

# def search(entity):
#     entity_ = entity.replace(" ", "+")
#     search_url = f"https://en.wikipedia.org/w/index.php?search={entity_}"
#     response_text = requests.get(search_url).text
#     soup = BeautifulSoup(response_text, features="html.parser")
#     result_divs = soup.find_all("div", {"class": "mw-search-result-heading"})
#     if result_divs:  # mismatch
#       result_titles = [clean_str(div.get_text().strip()) for div in result_divs]
#       search(result_titles[0])
#     else:
#       page = [p.get_text().strip() for p in soup.find_all("p") + soup.find_all("ul")]
#       if any("may refer to:" in p for p in page):
#         search(entity)
#       else:
#         return '\n'.join(page)