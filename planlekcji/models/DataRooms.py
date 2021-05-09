class OneCell:
    def __init__(self, teacher, school_class, subject):
        self.teacher = teacher
        self.school_class = school_class
        self.subject = subject

    def __repr__(self):
        return 'Teacher: ' + self.teacher + '\n' + ' School class: ' + self.school_class + ' Subject: ' + self.subject


# one_cell_list - list of 5 element 0 - means Monday, 1 means Tuesday
class DataRoom:
    def __init__(self, hour, one_cell_list):
        self.hour = hour
        self.one_cell_list = one_cell_list

    def __repr__(self):
        list_of_cells = ''
        for oc in self.one_cell_list:
            list_of_cells += str(oc) + '\n'
        return 'Hour: ' + str(self.hour) + '\n' + list_of_cells
