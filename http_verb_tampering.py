import argparse
import requests

methods = [
    'HEAD', 'GET', 'POST', 'TRACE', 'TRACK', 'OPTIONS', 'INDEX', 'CONNECT', 'PUT',
    'VERSION-CONTROL', 'PATCH', 'DELETE', 'COPY', 'MOVE', 'CHECKIN', 'CHECKOUT',
    'LINK', 'LOCK', 'MKCOL', 'NOEXISTE', 'ORDERPATCH', 'PROPFIND', 'PROPPATCH',
    'REPORT', 'SEARCH', 'SHOWMETHOD', 'SPACEJUMP', 'TEXTSEARCH', 'UNCHECKOUT',
    'UNLINK', 'UNLOCK', 'BAMBOOZLE'
]

sensitive_keywords = [
    "password", "credit card", "social security", "SSN", "bank account", "login", "username", "secret"
]


def get_options():
    parser = argparse.ArgumentParser(
        description="This Python script can be used for HTTP verb tampering to bypass forbidden access, "
                    "and for HTTP methods enumeration to find dangerous enabled methods like PUT",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbosity",
        action="count",
        default=0,
        help="verbosity level (-v for verbose, -vv for debug)",
    )

    options = parser.parse_args()
    return options


def test_method(url, method):
    headers = {}
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        allow_redirects=False,
    )
    return method, response.status_code, response.headers


def main(options):
    url = input("Enter the target URL: ")

    for method in methods:
        prompt = f"Do you want to test the method '{method}'? (y/n): "
        choice = input(prompt)
        if choice.lower() != "y":
            continue

        print(f"\nTesting method: {method}\n")

        result = test_method(url, method)
        print(f"Method: {result[0]}")
        print(f"Status Code: {result[1]}")
        print("Headers:")
        for header, value in result[2].items():
            print(f"{header}: {value}")

        # Check if any sensitive keywords are present in the response body
        response_body = result[2].get("Response-Body", "")
        for keyword in sensitive_keywords:
            if keyword.lower() in response_body.lower():
                print(f"\nSensitive information may have been disclosed with {method} {url}:")
                print(response_body)
                break

        print("\n" + "=" * 60 + "\n")


if __name__ == '__main__':
    options = get_options()
    main(options)
