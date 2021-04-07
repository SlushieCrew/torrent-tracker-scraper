# if __name__ == "__main__":
# import scraper

# scraper = scraper.Scraper(
# trackers=["udp://bt2.archive.org:6969/annouce"],
# infohashes=["73C36F980F5B1A40348678036575CCC1E0BB0E4E",],
# timeout=5,
# )
# results = scraper.scrape()
# for result in results:
# print(result)

import scraper
import json

scraper = scraper.Scraper(
    infohashes=[
        "9bb80eaa0c2d384013784a8e2117d235e2de1073",
    ]
)
results = scraper.scrape()
# for result in results:
print (results)
    # print(json.dumps(json.loads(results), indent=4, sort_keys=True))
