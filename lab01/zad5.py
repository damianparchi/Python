class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.quiz_scores = []  #wyniki quizow
        self.total_score = 0  #wynik
        self.il_quizow = 0  #liczba quizów do sredniej

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def add_quiz(self, score):
        #dodawanie wyniku z quizu do listy i zaktualizowanie całkowitego wyniku
        self.quiz_scores.append(score)
        self.total_score += score
        self.il_quizow  += 1

    def get_total_score(self):
        return self.total_score

    def get_average_score(self):
        if self.il_quizow  == 0:
            return 0
        return self.total_score / self.il_quizow 

student1 = Student("Damian", "Kowalski")
student2 = Student("Jan", "Rybak")
student3 = Student("Michał", "Markowski")

student1.add_quiz(30)
student1.add_quiz(23)
student1.add_quiz(70)

student2.add_quiz(16)
student2.add_quiz(25)
student2.add_quiz(85)

student3.add_quiz(36)
student3.add_quiz(55)
student3.add_quiz(50)

print(f"Student {student1.get_name()}: wynik: {student1.get_total_score()}, średnia aryt. wyniku: {student1.get_average_score()}")
print(f"Student {student2.get_name()}: wynik: {student2.get_total_score()}, średnia aryt. wyniku: {student2.get_average_score()}")
print(f"Student {student3.get_name()}: wynik: {student3.get_total_score()}, średnia aryt. wyniku: {student3.get_average_score()}")
