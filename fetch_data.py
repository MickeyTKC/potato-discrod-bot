from fetch import commodity, crypto, currency, fintech, indices, ndx100, spx500, us_sectors

def fetch_data():
    fetch_list = [commodity, crypto, currency, fintech, indices, ndx100, spx500, us_sectors]
    for item in fetch_list:
        print(f"Fetching data for {item.file_path}")
        item.fetch_data()
        
if __name__ == "__main__":
    fetch_data()