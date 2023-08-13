import requests
import sys
print('./1-hbtn_header.py https://intranet.hbtn.io')
def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        return
    
    url = sys.argv[1]
    response = request.get(url)

    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")
    else:
        print(f"Request to {url} failed with status code {response.status_code}.")

if __name__ == "__main__":
    main()