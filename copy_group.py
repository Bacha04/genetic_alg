class Group:
    def __init__(self, group_name, people_num, subjects_hours):
        self.group_name = group_name
        self.people_num = people_num
        self.subjects_hours = subjects_hours

    def __str__(self):
        return f"Group(group_name={self.group_name}, people_num={self.people_num}, subjects_hours={self.subjects_hours})"
