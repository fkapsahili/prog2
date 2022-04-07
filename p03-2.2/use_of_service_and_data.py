"""
INFPROG2 P03 - Online Data
Author: Fabio Kapsahili
"""

"""
2.2 "Use of service and data"

Write a script, potentially extending your experimental code above, that queries the
BOM service (with a GET request) in a way that
(1) upon no/invalid response, the query is resubmitted with exponential backoff
waiting time in between requests to avoid server overload;
(2) material records with missing or invalid cost are ignored;
(3) wrongly encoded umlauts are repaired.
The script should output a tabular BOM with ordered valid materials including the total
sum at the end, calculated by you, like this:
MAT1 | COST1
MAT2 | COST2
-----+----------
SUM | TOTALCOST

If possible, use OOP to encapsulate the entire validation and robustness logic.
"""


from flaky_bom_service import Bom


class MaterialTable:
    """
    The MaterialTable class.
    """

    def __init__(self):
        """
        The constructor.
        """
        self.bom = Bom()
        self.materials = []

    def get_materials(self):
        """
        Retrieves the materials.
        """
        bom_data = self.bom.fetch_bom()
        if bom_data is not None and type(bom_data) is dict:
            for name, cost in bom_data.items():
                if cost is not None and type(cost) is int:
                    self.materials.append({"name": name, "cost": cost})

    def repair_umlauts(self):
        for material in self.materials:
            material["name"] = material["name"].replace("\u00c3\u00a4", "ä")
            material["name"] = material["name"].replace("\u00c3\u00bc", "ü")
            material["name"] = material["name"].replace("\u00c3\u00b6", "ö")
            material["name"] = material["name"].replace("\u00c3\u00a9", "é")
            material["name"] = material["name"].replace("\u00c3\u00a0", " ")
            material["name"] = material["name"].replace("\u00c3\u00a8", "è")
            material["name"] = material["name"].replace("\u00c3\u00a1", "á")

    def print_materials(self):
        """
        Prints the materials.
        """
        for material in self.materials:
            print("{:<15} {:<5} {:<15}".format(material["name"], "|", material["cost"]))
        print("-" * 15 + "-+-" + "-" * 15)
        print("{:<15} {:<5} {:<15}".format("SUM", "|", self.get_total_cost()))

    def get_total_cost(self):
        """
        Calculates the total cost.
        """
        total_cost = 0
        for material in self.materials:
            total_cost += material["cost"]
        return total_cost

    def order_materials(self):
        """
        Orders the materials.
        """
        self.materials.sort(key=lambda x: x["name"])


def main():
    """
    The main function.
    """
    materials = MaterialTable()
    materials.get_materials()
    materials.repair_umlauts()
    materials.order_materials()
    materials.print_materials()


if __name__ == "__main__":
    main()
