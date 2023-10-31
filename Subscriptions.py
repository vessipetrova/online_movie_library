class Subscription:
    def __init__(self, __subscription_id, __subscription_type, price):
        self.__subscription_id = __subscription_id
        self.__subscription_type = __subscription_type
        self.price = price

    def __str__(self):
        return f"Subscription ID: {self.__subscription_id}\n" \
               f"Subscription Type: {self.__subscription_type}\n" \
               f"Price: {self.price}\n"

    def __eq__(self, other):
        return self.__subscription_id == other.subscription_id

    def __ne__(self, other):
        return self.__subscription_id != other.subscription_id
