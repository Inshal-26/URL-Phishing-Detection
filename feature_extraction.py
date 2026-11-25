
import re
from urllib.parse import urlparse


def extract_features(url):
    url = str(url).strip()

    if not url or url.lower() == "nan":
        url = "unknown"

    if not url.lower().startswith(("http://", "https://")):
        url = "http://" + url

    try:
        parsed = urlparse(url)
    except ValueError:
        parsed = urlparse("http://unknown")

    hostname = parsed.hostname or ""
    path = parsed.path or ""
    query = parsed.query or ""
    fragment = parsed.fragment or ""

    parts = hostname.split(".") if hostname else []
    tld = parts[-1].lower() if len(parts) > 1 else ""

    suspicious_words = [
        "login", "verify", "account", "update",
        "secure", "bank", "signin", "confirm",
        "password", "payment", "wallet"
    ]

    shortening_services = [
        "bit.ly", "tinyurl.com", "goo.gl",
        "t.co", "ow.ly", "is.gd", "buff.ly"
    ]

    try:
        has_port = int(parsed.port is not None)
    except ValueError:
        has_port = 0

    num_subdomains = max(0, len(parts) - 2)

    path_clean = path.strip("/")

    path_depth = (
        len(path_clean.split("/"))
        if path_clean else 0
    )

    return {
        "url_length": len(url),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_digits": sum(c.isdigit() for c in url),
        "has_https": int(url.lower().startswith("https://")),
        "has_ip": int(bool(
            re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", hostname)
        )),
        "has_at_symbol": int("@" in url),
        "special_chars": sum(not c.isalnum() for c in url),
        "path_length": len(path),
        "num_subdomains": num_subdomains,
        "num_query_parameters": len(query.split("&")) if query else 0,
        "fragment_length": len(fragment),
        "path_depth": path_depth,
        "has_shortening_service": int(
            any(service in hostname for service in shortening_services)
        ),
        "has_suspicious_word": int(
            any(word in url.lower() for word in suspicious_words)
        ),
        "has_extra_slashes": int("//" in url.split("://", 1)[-1]),
        "is_long_url": int(len(url) > 75),
        "has_www": int("www" in hostname),
        "num_underscores": url.count("_"),
        "num_percent": url.count("%"),
        "has_port": has_port,
        "has_digits_in_hostname": int(any(c.isdigit() for c in hostname)),
        "num_dots_hostname": hostname.count("."),
        "has_suspicious_tld": int(tld in ["xyz", "top", "click", "zip", "tk"]),
        "has_many_subdomains": int(num_subdomains > 2),
        "has_deep_path": int(path_depth > 3)
    }
