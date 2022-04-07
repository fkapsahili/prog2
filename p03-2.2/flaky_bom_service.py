"""
INFPROG2 P03 - Online Data
Author: Fabio Kapsahili
"""

"""
2.1 "Flaky BOM service"

A BOM service is typically used in production scenarios, e.g. in
construction of automobiles. The BOM represents the total cost of all parts of the
assembled product.

The task is to query it in your code without your code ever crashing while producing the
correct result. In a first preparation step, use the service’s interface to request the data
without any parameters.

You will see that sometimes, the request will fail, and you will need to handle that in a smart way.

The service has a simple HTTP GET interface: http://160.85.252.148
"""


import requests
import time


class Bom:
    """
    The BOM class.
    """

    def __init__(self):
        """
        The constructor.
        """
        self.url = "http://160.85.252.148"
        self.wait_time = 1

    def fetch_bom(self, params=None):
        """
        Retrieves the BOM.
        Try to retrieve the latest online data and return the response.
        If the request fails, try again with an exponential backoff.
        """
        try:
            response = requests.request("GET", self.url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                self.__wait_for_next_request()
                return self.fetch_bom()
        except requests.exceptions.RequestException:
            self.__wait_for_next_request()
            return self.fetch_bom()

    def __wait_for_next_request(self):
        """
        Wait for the next request.
        Avoid a Too Many Requests HTTP error.
        """
        print("Retrying... Waiting for {} seconds".format(self.wait_time))
        self.wait_time *= 2
        time.sleep(self.wait_time)


def main():
    """
    The main function.
    """
    bom = Bom()
    print(bom.fetch_bom())


if __name__ == "__main__":
    main()
