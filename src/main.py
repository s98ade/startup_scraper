from scraper import su100_scraper # for now only su100; have to combine into one file


if __name__ == "__main__":
    url = "https://startup100.net/"
    scraper = su100_scraper.Scraper(url)
    scraper.scrape()