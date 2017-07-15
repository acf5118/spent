import re
import csv


class Purchase:

    def __init__(self, date, description, amount):
        """
        :param date:
        :type: str
        :param description:
        :type: str
        :param amount:
        :type: float
        :return:
        :rtype:
        """

        self.date = date
        self.description = description
        self.amount = amount
        self.name = ""
        self.convert()

    def __repr__(self):
        """
        :return: string representation: e.g Purchase(03/11, TacoBell, 8.67)
        :rtype: str
        """
        return "Purchase(%s, %s, %s)" % (self.date, self.description, self.amount)

    def __eq__(self, other):
        if isinstance(other, Purchase):
            return self.description == self.description
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__repr__())

    def convert(self):
        if "TACO" in self.description:
            self.name = "Taco Bell"
        elif "MICROSOFT" in self.description:
            self.name = "Xbox"
        elif "MCDONALD'S" in self.description:
            self.name = "McDonald's"
        elif "WEGMAN" in self.description:
            self.name = "Wegmans"

class ChaseTextToData:
    def __init__(self, filename_):
        self.filename = filename_
        self.file = open(filename_)
        self.year = "2017"
        self.items = []
        self.purchases = []
        self.item_dict = {}

    def date_search(self, line):
        return re.search(r'(\d+/\d+/\d+)', line)

    def new_balance(self, line):
        if "New Balance:" in line:
            self.new_balance_ = float(line.split()[-1].replace("$", "").replace(",", ""))
            print(self.new_balance_)
            return True

    def purchases(self, line):
        if "PURCHASE" in line:
            for item in self.file:
                if (self.year + " Totals") in item:
                    return True
                if item.strip() == "":
                    continue
                row = item.split()
                if not re.search(r'(\d+/\d+)', row[0]):
                    continue
                #print(row)
                description = ""
                for i in range(1, len(row) - 1):
                    description += row[i] + " "
                #print(row[-1])
                self.purchases.append(Purchase(row[0], description, row[-1]))
            return True
        return False

    def return_false(self, line):
        return False

    def run(self):
        condition = [ChaseTextToData.date_search,
                     ChaseTextToData.new_balance,
                     ChaseTextToData.purchases,
                     ChaseTextToData.return_false]

        condition_count = 0
        for line in self.file:
            if (condition[condition_count](self, line)):
                condition_count += 1

        self.charges = []
        date_name = ""

        for item in self.purchases:
            #print(item.date + " " + item.description + " " + item.amount)
            if float(item.amount) >= 500:
                continue
            k = ""
            if item.name == "":
                k = item.description
            else:
                k = item.name
            print("k is: " + k)
            if k in self.item_dict:
                self.item_dict[k] += float(item.amount)
            else:
                self.item_dict[k] = float(item.amount)
        """
        charge_index = 0
        self.data = re.compile(r'(\d+/\d+)').split(date_name)


        with open("test2.csv", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for i in range(1,len(self.data) - 1, 2):
                tmp = []
                tmp.append(self.data[i])
                tmp.append(self.data[i+1])
                tmp.append(self.charges[charge_index])
                writer.writerow(tmp)
                charge_index += 1
        """
