__author__ = 'asafliv'


class UserClass():
    def __init__(self, name):
        self.user_sum = None
        self.user_requests_counter = 0
        self.user_name = name

    def new_number(self, number):
        self.user_requests_counter += 1
        self.user_sum += number

    def get_avg(self):
        if self.user_requests_counter == 0:
            return None
        return self.user_sum / self.user_requests_counter
