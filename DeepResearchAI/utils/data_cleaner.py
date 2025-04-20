def clean_data(raw_data):
    print("[🧹] Cleaning data...")
    cleaned = []
    for item in raw_data:
        if item:
            cleaned.append(item.replace('\n', ' ').strip())
    return cleaned
