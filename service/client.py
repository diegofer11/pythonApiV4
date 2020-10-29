""" Class representing a client """


class Client:
    """ Class representing a client """

    def __init__(
        self,
        name,
        last_name,
        doc_id,
        ):
        self.name = name
        self.last_name = last_name
        self.doc_id = doc_id
        self.preexistence = []

    def add_preexistence(self, n_preexistence):
        """ add preexistance to a client """
        self.preexistence.append(n_preexistence)
        return len(self.preexistence) - 1

    def get_preexistence(self, p_index):
        """ get a preexiste given an index """
        if p_index >= len(self.preexistence):
            return 'There is no such preexistence'

    def get_all_preexistence(self):
        """ get all preexistence from a client """
        return self.preexistence

    def remove_preexistence(self, n_preexistence):
        """ remove preexistence from index """
        self.preexistence.pop(n_preexistence)
        return len(self.preexistence) - 1

    def get_formatted_name(self):
        """ return formated client name """
        return self.name + ' ' + self.last_name


if __name__ == '__main__':
    client_instance = Client('uno', 'dos', '113565')
    print ('User Abbas has been added with id ',
           client_instance.get_formatted_name())
