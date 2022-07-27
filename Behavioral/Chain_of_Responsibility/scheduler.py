from abc import ABC, abstractmethod

"""
The goal is to rank the option classes from 0 - 10
The last step of the process is to fill the schedule with the highest ranking option
"""

# Class & Rank
options = {'Art': 0, 'Math': 0, 'English': 0, 'History': 0, 'Geography': 0, 'Physics': 0}
optionsData = {'Art': 0, 'Math': 0, 'English': 0, 'History': 0, 'Geography': 0, 'Physics': 0}
schedule = {"Name": [None, None, None, None, None]}


class ScheduleHandler(ABC):
    @abstractmethod
    def set_next_chain(self, next):
        pass

    @abstractmethod
    def calculate(self):
        pass


class Student:
    def __init__(self):
        # General Info
        self.name = "Alex Joslin"
        # Required
        self.requiredSubjects = ["Math", "Physics"]
        # Wanted
        self.wantedSubjects = ["Art", "English", "Geography"]
        # Skills
        self.ArtSkill = 0
        self.MathSkill = 5
        self.EnglishSkill = 2
        self.HistorySkill = 0
        self.GeographySkill = 1
        self.PhysicsSkill = 0
        # Interests
        self.ArtInterest = 8
        self.MathInterest = 5
        self.EnglishInterest = 7
        self.HistoryInterest = 2
        self.GeographyInterest = 5
        self.PhysicsInterest = 0
        # Challenge
        self.challengeDesired = 7


class GeneralInfo:
    next_calculation = None

    def set_next_calculation(self, next_calc):
        self.next_calculation = next_calc

    def calculate(self, student):
        schedule[student.name] = schedule.pop("Name")
        self.next_calculation.calculate(student)


class Required:
    next_calculation = None

    def set_next_calculation(self, next_calc):
        self.next_calculation = next_calc

    def calculate(self, student):
        for subject in student.requiredSubjects:
            options[subject] = 100
        self.next_calculation.calculate(student)


class Wanted:
    next_calculation = None

    def set_next_calculation(self, next_calc):
        self.next_calculation = next_calc

    def calculate(self, student):
        for subject in student.wantedSubjects:
            options[subject] += 5
        self.next_calculation.calculate(student)


class Skills:
    next_calculation = None

    def set_next_calculation(self, next_calc):
        self.next_calculation = next_calc

    def calculate(self, student):
        challenge = student.challengeDesired
        sub_skills = {"Art": student.ArtSkill, "Math": student.MathSkill,
                     "English": student.EnglishSkill, "History": student.HistorySkill,
                     "Geography": student.GeographySkill, "Physics": student.PhysicsSkill}
        sub_difficulty = {"Art": 1, "Math": 2, "English": 2,
                          "History": 2, "Geography": 1, "Physics": 3}
        for subject in sub_skills:
            options[subject] += challenge + sub_difficulty[subject] - sub_skills[subject] + challenge-5
        self.next_calculation.calculate(student)


class Interests:
    next_calculation = None

    def set_next_calculation(self, next_calc):
        self.next_calculation = next_calc

    def calculate(self, student):
        sub_interests = {"Art": student.ArtInterest, "Math": student.MathInterest,
                         "English": student.EnglishInterest, "History": student.HistoryInterest,
                         "Geography": student.GeographyInterest, "Physics": student.PhysicsInterest}
        for subject in sub_interests:
            options[subject] += sub_interests[subject]
        self.next_calculation.calculate(student)


class TrimesterSchedule:
    name = None

    def calculate(self, student):
        self.name = student.name
        subject_list = list(options.items())
        subject_list.sort(key=lambda x: x[1], reverse=True)
        for i in range(0, 5):
            schedule[student.name][i] = subject_list[i][0]
        self.show()

    @staticmethod
    def show():
        name, classes = list(schedule.items())[0]
        print("-"*25 + "Schedule" + "-"*25)
        print("Student: " + name)
        print("Classes: " + str(classes))


genIfo = GeneralInfo()
required = Required()
wanted = Wanted()
skill = Skills()
interest = Interests()
triSchedule = TrimesterSchedule()

genIfo.set_next_calculation(required)
required.set_next_calculation(wanted)
wanted.set_next_calculation(skill)
skill.set_next_calculation(interest)
interest.set_next_calculation(triSchedule)

genIfo.calculate(Student())
print(options)
