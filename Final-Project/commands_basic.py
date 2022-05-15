def make_request(ENDPOINT, PARAMS):
    import http.client
    import json

    SERVER = 'rest.ensembl.org'

    URL = SERVER + ENDPOINT + PARAMS

    print(f"\nConnecting to server: {URL}\n")

    conn = http.client.HTTPConnetion(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("Error! Unable to connect to the server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json-loads(data1)

    return data1