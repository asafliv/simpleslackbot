__author__ = 'asafliv'

from userdata import UserClass


class UsersDict:
    def __init__(self):
        self.users_dict = {}

    def is_new_user(self, name_to_check):
        '''
        checks if the user name name_to_check is already created in our data
        :param name_to_check:
        :return:
        '''
        for user in self.users_dict.iterkeys():
            if user.name == name_to_check:
                return False
        return True

    def add_new_user(self, name):
        '''
        Checks if the user name is already created and if not creates it
        :param name:
        :return:
        '''
        if not self.is_new_user(name):
            return
        new_user = UserClass(name)
        self.users_dict[name] = new_user
        print("New user named: %s was identified!!!" % name)

    def get_specific_user_avg(self, user_name):
        '''
        Returns the user_name current avg
        :param user_name: the user to get the avg for
        :return:
        '''
        user_object = self.users_dict.get(user_name, None)
        if user_object is None:
            return "no user with this name!"
        return user_object.get_avg()

    def get_all_users_avg_string(self):
        '''
        returns all the users AVG
        :return:
        '''
        all_users_avg = 0
        if not self.users_dict:
            return "No users yet! come back one year!"
        for user_object in self.users_dict.itervalues():
            all_users_avg += user_object.get_avg
        return all_users_avg / len(self.users_dict)
