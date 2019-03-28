import csv

acceptableGrades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "IP"]

class Report():
    courseList = []
    numCourses = 0
    totalCredits = 0
    creditsInProgress = 0
    gpa = 0.00

    def __init__(self, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            count = 0
            for row in csv_reader:
                if count == 0:
                    count += 1
                else:
                    name = row[0]
                    department = row[1]
                    number = row[2]
                    hours = int(row[3])
                    grade = row[4]
                    course = Course(name, department, number, hours, grade)
                    self.courseList.append(course)
                    self.totalCredits += hours
                    self.numCourses += 1
                    count += 1
        self.calculateGPA()

    def displayAllCourses(self):
        for course in self.courseList:
            print("")
            course.displayCourse()
        print("")

    def calculateCredits(self):
        totalCredits = 0
        creditsInProgress = 0
        for course in self.courseList:
            if course.grade == "IP":
                creditsInProgress += course.hours
            else:
                totalCredits += course.hours
        self.totalCredits = totalCredits
        self.creditsInProgress = creditsInProgress

    def printCredits(self):
        print("Total number of credits taken: " + str(self.totalCredits))
        print("Number of credits in progress: " + str(self.creditsInProgress))
        print("")

    def calculateGPA(self):
        gpa = 0.0
        gradePoint = 0.0
        self.calculateCredits()
        for course in self.courseList:
            if course.grade == "A+" or course.grade == "A":
                gradePoint += (4.0 * course.hours)
            elif course.grade == "A-":
                gradePoint += (3.67 * course.hours)
            elif course.grade == "B+":
                gradePoint += (3.33 * course.hours)
            elif course.grade == "B":
                gradePoint += (3.0 * course.hours)
            elif course.grade == "B-":
                gradePoint += (2.67 * course.hours)
            elif course.grade == "C+":
                gradePoint += (2.33 * course.hours)
            elif course.grade == "C":
                gradePoint += (2.00 * course.hours)
            elif course.grade == "C-":
                gradePoint += (1.67 * course.hours)
            elif course.grade == "D+":
                gradePoint += (1.33 * course.hours)
            elif course.grade == "D":
                gradePoint += (1.00 * course.hours)
            elif course.grade == "D-":
                gradePoint += (0.67 * course.hours)

        gpa = gradePoint / self.totalCredits
        self.gpa = gpa

    def printGPA(self):
        print("Current cumulative GPA: "+ ('%.2f' % self.gpa))
        print("")

    def addCourse(self, course):
        self.courseList.append(course)
        self.calculateGPA()
        self.calculateCredits()

    def removeCourseByName(self, name):
        count = 0
        lengthBefore = len(self.courseList)
        for course in self.courseList:
            if name == course.name:
                removed = self.courseList.pop(count)
                break
            else:
                count += 1
        lengthAfter = len(self.courseList)
        if(lengthBefore != lengthAfter):
            self.calculateGPA()
            self.calculateCredits()
            print("Removed the first entry of " + removed.name)
            print("")
        else:
            print("Could not find an entry with the specified course name!")
            print("")

    def removeCourseByNumber(self, department, number):
        count = 0
        lengthBefore = len(self.courseList)
        for course in self.courseList:
            if department == course.department and number == course.number:
                removed = self.courseList.pop(count)
                break
            else:
                count += 1
        lengthAfter = len(self.courseList)
        if(lengthBefore != lengthAfter):
            self.calculateGPA()
            self.calculateCredits()
            print("Removed the first entry of " + removed.department + " " + removed.number)
            print("")
        else:
            print("Could not find an entry with the specified course information!")
            print("")

    def changeGradeByName(self, name, newGrade):
        count = 0
        for grade in acceptableGrades:
            if newGrade == grade:
                for course in self.courseList:
                    if name == course.name:
                        oldGrade = course.grade
                        course.grade = newGrade
                        break
                    else:
                        count += 1
                if count == len(self.courseList) and newGrade != course.grade:
                    print("Could not find an entry with the specified course name!")
                    print("")
                    break
                else:
                    self.calculateGPA()
                    print("Changed the grade of " + name + " from " + oldGrade + " to " + newGrade + "!")
                    print("")
                    break
        print("Invalid grade!")
        print("")

    def changeGradeByNumber(self, department, number, newGrade):
        count = 0
        for grade in acceptableGrades:
            if newGrade == grade:
                for course in self.courseList:
                    if department == course.department and number == course.number:
                        oldGrade = course.grade
                        course.grade = newGrade
                        break
                    else:
                        count += 1
                if count == len(self.courseList) and newGrade != course.grade:
                    print("Could not find an entry with the specified course information!")
                    print("")
                else:
                    self.calculateGPA()
                    print("Changed the grade of " + department + " " + number + " from " + oldGrade + " to " + newGrade + "!")
                    print("")
        print("Invalid grade!")
        print("")

class Course():
    name = ""
    department = ""
    number = ""
    hours = 0
    grade = ""

    # parameterized constructor
    def __init__(self, name, department, number, hours, grade):
        self.name = name
        self.department = department
        self.number = number
        self.hours = hours
        self.grade = grade

    def displayCourse(self):
        print("Course Name: " + self.name)
        print("Department: " + self.department)
        print("Course Number: " + self.number)
        print("Credit Hours: " + str(self.hours))
        print("Grade Received: " + self.grade)

# firstClass = Course("TEST COURSE1", "ECE", "000", 0, "A+")
# secondClass = Course("TEST COURSE2", "ECE", "001", 0, "A+")

myReport = Report("data.txt")
# myReport.courseList.append(firstClass)
# myReport.courseList.append(secondClass)
# myReport.displayReport()

# myReport.displayAllCourses()
# myReport.calculateGPA()
# myReport.printGPA()
# myReport.printCredits()

# myReport.removeCourseByName("CALCULUS I")
# myReport.removeCourseByNumber("ECE", "330")
# myReport.changeGradeByName("CALCULUS I", "G")
# myReport.changeGradeByNumber("ECE", "330", "RIP")
# myReport.printGPA()

def printOpening():
    print("***************************************************")
    print("*              Academic History Report            *")
    print("*               made by: Jaehyun Kim              *")

def printOptions():
    print("***************************************************")
    print("*   Please choose one of the following options:   *")
    print("*   (all responses must be given in lower-case)   *")
    print("***************************************************")
    print("*            r: view academic history             *")
    print("***************************************************")

printOpening()
printOptions()
userInput = raw_input()
while userInput != "q":
    if userInput == "r":
        myReport.displayAllCourses()
    printOptions()
    userInput = raw_input()
