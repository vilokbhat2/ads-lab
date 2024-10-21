'''Design a HashTable to store the information about students from various institutions of an 
University. University can have maximum 100 institutes and each institute can run 
maximum of 100 programs. It is required to store data of students for 100 years. Take 
registration number of student as key to store at appropriate location. 
Example: Registration number 241057001 gives information about year of admission, 
institution and program within the institution. 24 represents Year, 10 represents institute 
(MSIS) and 57 represents program (AIML).
It is required that student data should be stored in hierarch like institution, program and 
year. 
Provide following additional methods:
Count number of unique institutions
Count total number of programs under each institution
Count number of programs running under given institute in a given year.
Count total number of students in given institute.'''

class UniversityHashTable:
    def __init__(self):
        self.university = {}

    def add_student(self, registration_number, year, institute, program, student_data):
        """
        Add a student to the hash table.

        :param registration_number: string, e.g., "241057001"
        :param year: integer, 1-100
        :param institute: string, e.g., "MSIS"
        :param program: string, e.g., "AIML"
        :param student_data: object with attributes: `year`, `institute`, `program`, and other relevant student information
        """
        if year not in self.university:
            self.university[year] = {}
        if institute not in self.university[year]:
            self.university[year][institute] = {}
        if program not in self.university[year][institute]:
            self.university[year][institute][program] = {}
        self.university[year][institute][program][registration_number] = student_data

    def count_unique_institutions(self):
        """
        Count the number of unique institutions.

        :return: integer, number of unique institutions
        """
        return len(set(institute for year in self.university.values() for institute in year.keys()))

    def count_programs_per_institution(self, institute):
        """
        Count the total number of programs under a given institution.

        :param institute: string, e.g., "MSIS"
        :return: integer, total number of programs under the institution
        """
        return sum(len(programs) for year in self.university.values() for programs in [year.get(institute, {})])

    def count_programs_per_institute_per_year(self, institute, year):
        """
        Count the number of programs running under a given institute in a given year.

        :param institute: string, e.g., "MSIS"
        :param year: integer, 1-100
        :return: integer, number of programs running under the institute in the year
        """
        return len(self.university.get(year, {}).get(institute, {}))

    def count_students_per_institute(self, institute):
        """
        Count the total number of students in a given institute.

        :param institute: string, e.g., "MSIS"
        :return: integer, total number of students in the institute
        """
        return sum(len(students) for year in self.university.values() for students in [year.get(institute, {})])

    def get_student_data(self, registration_number):
        """
        Get the student data for a given registration number.

        :param registration_number: string, e.g., "241057001"
        :return: object with attributes: `year`, `institute`, `program`, and other relevant student information
        """
        for year, institutes in self.university.items():
            for institute, programs in institutes.items():
                for program, students in programs.items():
                    if registration_number in students:
                        return students[registration_number]
        return None

    def __str__(self):
        """
        Return a string representation of the hash table.

        :return: string, representation of the hash table
        """
        return str(self.university)

university = UniversityHashTable()

university.add_student("241057001", 24, "MSIS", "AIML", {"name": "John Doe", "major": "Computer Science"})
university.add_student("241057002", 24, "MSIS", "AIML", {"name": "Jane Doe", "major": "Mathematics"})
university.add_student("241058001", 24, "ECE", "Robotics", {"name": "Bob Smith", "major": "Electrical Engineering"})

print("Unique institutions:", university.count_unique_institutions())
print("Programs under MSIS:", university.count_programs_per_institution("MSIS"))
print("Programs under MSIS in 24:", university.count_programs_per_institute_per_year("MSIS", 24))
print("Students in MSIS:", university.count_students_per_institute("MSIS"))

student_data = university.get_student_data("241057001")
print("Student data:", student_data)

# class StudentHashTable:
#     def __init__(self):
#         self.data = {}

#     def _parse_registration_number(self, reg_no):
#         year = int(str(reg_no)[:2])
#         institution = int(str(reg_no)[2:4])
#         program = int(str(reg_no)[4:6])
#         return year, institution, program

#     def add_student(self, reg_no, name, phone, address):
#         year, institution, program = self._parse_registration_number(reg_no)
#         if institution not in self.data:
#             self.data[institution] = {}
#         if program not in self.data[institution]:
#             self.data[institution][program] = {}
#         if year not in self.data[institution][program]:
#             self.data[institution][program][year] = []
#         self.data[institution][program][year].append({
#             'reg_no': reg_no,
#             'name': name,
#             'phone': phone,
#             'address': address
#         })

#     def count_unique_institutions(self):
#         return len(self.data)

#     def count_programs_per_institution(self):
#         return {institution: len(programs) for institution, programs in self.data.items()}

#     def count_programs_in_year(self, institution, year):
#         if institution not in self.data:
#             return 0
#         count = 0
#         for program in self.data[institution].values():
#             if year in program:
#                 count += 1
#         return count

#     def count_students_in_institution(self, institution):
#         if institution not in self.data:
#             return 0
#         count = 0
#         for program in self.data[institution].values():
#             for year_students in program.values():
#                 count += len(year_students)
#         return count

# # Example usage:
# hash_table = StudentHashTable()
# hash_table.add_student(241057001, 'John Doe', '1234567890', '123 Main St')
# hash_table.add_student(241057002, 'Jane Smith', '0987654321', '456 Elm St')
# hash_table.add_student(251057003, 'Alice Johnson', '5555555555', '789 Oak St')

# print("Unique institutions:", hash_table.count_unique_institutions())
# print("Programs per institution:", hash_table.count_programs_per_institution())
# print("Programs in institution 10 in year 24:", hash_table.count_programs_in_year(10, 24))
# print("Total students in institution 10:", hash_table.count_students_in_institution(10))