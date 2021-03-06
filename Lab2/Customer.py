class Customer:
    def __init__(self):
        self.dict = {}

    def create(self, customerCode, customerName, address, creditLimit, country):
        # Adds the new customer record to customers object (dictionary). 
        # Returns dictionary {"Is Error": ___, "Error Message": _____} 
        # Check customer code in products object
        if customerCode in self.dict:
            return {'Is Error': True, 'Error Message': "Customer code '{}' already exists. Cannot Create. ".format(customerCode)}
        else:
            self.dict[customerCode] = {"Name" : customerName,"Address" : address,"Credit Limit" : creditLimit,"Country" : country}
        return {'Is Error': False, 'Error Message': ""}

    def read(self, customerCode):
        # Finds the customer code in customers object and returns 1 record in dictionary form. 
        # To return error message + data a tuple returned:  of ({"Is Error": ___, "Error Message": _____}, {<customer data>}) 
        #  where the first one is error message related, and second one is the data.
        if customerCode in self.dict:
            retCustomer = self.dict[customerCode]
        else:
            return ({'Is Error': True, 'Error Message': "Customer Code '{}' not found. Cannot Read.".format(customerCode)},{})

        return ({'Is Error': False, 'Error Message': ""},retCustomer)

    def update(self, customerCode, newCustomerName, newAddress, newCreditLimit, newCountry):
        # Finds the customer code in customers object and then changes the values to the new ones. 
        # Returns dictionary {"Is Error": ___, "Error Message": _____}.
        if customerCode in self.dict:
            self.dict[customerCode]["Name"] = newCustomerName
            self.dict[customerCode]["Address"] = newAddress
            self.dict[customerCode]["Credit Limit"] = newCreditLimit
            self.dict[customerCode]["Country"] = newCountry
        else:
            return {'Is Error': True, 'Error Message': "Customer Code '{}' not found. Cannot Update.".format(customerCode)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, customerCode):
        # Finds the customer code in customers object and removes it from the dictionary.
        # Returns dictionary {"Is Error": ___, "Error Message": _____}. 
        if customerCode in self.dict:
            del self.dict[customerCode]

        else:
            return {'Is Error': True, 'Error Message': "Customer Code '{}' not found. Cannot Delete".format(customerCode)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        # Will dump all customers data and return 1 dictionary as output.
        return (self.dict)

