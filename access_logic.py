class Object:
    # Class Attribute as defined as a Constant. Shared by all instances of the class
    SECURITY_LEVELS = {"Top Secret": 4, "Secret": 3, "Confidential": 2, "Unclassified": 1}

    def __init__(self, classification_name, object_categories):
        # Initialize Each Object instance. Accepts classification name and sub-category
        # to initialize each document.
        self.classification_name = classification_name
        self.classification_level = Object.SECURITY_LEVELS.get(self.classification_name)
        self.obj_cats = object_categories


class Subject:
    # Class Attribute: Dictionary to map clearance to a number. Defined as a Class constant.
    CLEARANCE_LEVELS = {"Top Secret": 4, "Secret": 3, "Confidential": 2, "Unclassified": 1}
    DAYS = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}

    def __init__(self, clearance_name, subject_categories, access_day, access_time):
        # Class accepts clearance level and set of categories
        self.clearance_name = clearance_name
        self.clearance_level = Subject.CLEARANCE_LEVELS.get(self.clearance_name)
        self.day = access_day
        self.day_num = Subject.DAYS.get(self.day)
        self.categories = subject_categories
        self.time = int(access_time)

    def can_read(self, object):
        if object.classification_level <= self.clearance_level and object.obj_cats.issubset(self.categories):
            # Note: BLP "Simple Property" -> No Read Up. Subject >= Object being read.

            if self.day_num <= 5 and ("Regular Faculty" in self.categories or "Adjunct Faculty" in
                                      self.categories or "Staff" in self.categories):
                # Faculty and Staff can read Monday-Friday
                return True

            elif "Undergrad Student" in self.categories:
                # Students can read any day at any time
                return True

            elif "Graduate Student" in self.categories and "Staff" not in self.categories:
                # Students (including graduate level) can read any day at any time, unless also Staff.
                return True

            else:
                return False

        else:
            return False

    def can_write(self, object):
        if self.clearance_level <= object.classification_level and self.categories.issubset(object.obj_cats):
            # Note: BLP "Star Property" -> No Write Down. Subject <= Object.

            if "Undergrad Student" in self.categories or "Graduate Student" in self.categories or "Staff" in self.categories:

                if self.day_num <= 5 and 800 <= self.time <= 1700:
                    # Students and staff can only write Monday-Friday 8:00AM to 5:00PM
                    return True

                else:
                    return False

            elif "Adjunct Faculty" in self.categories:
                if self.day_num <= 5:
                    # Adjunct faculty can only write Monday-Friday (anytime).
                    return True

                else:
                    return False

            elif "Regular Faculty" in self.categories and "Staff" not in self.categories:
                # Regular Faculty can write any day any time, so long as not also Staff.
                return True

            else:
                return False

        else:
            return False



