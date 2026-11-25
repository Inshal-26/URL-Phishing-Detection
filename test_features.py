from feature_extraction import extract_features


url = "https://www.google.com/search?q=test"

features = extract_features(url)

print("Number of features:", len(features))

print("\nExtracted Features:")

for name, value in features.items():
    print(name, "=", value)