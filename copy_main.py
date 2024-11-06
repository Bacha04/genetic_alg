from teacher import Teacher
from group import Group

import time
import random
from numpy.random import rand
from numpy.random import randint
from collections import defaultdict

#constants
n_iter = 100
n_pop = 100
n_classes = 4
r_cross = 0.9
r_mut = 0.1

days = [
	"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
]

subjects = [
	'IS','IS_prac' , 'SDMP','SDMP_prac' , 'IT','IT_prac' , 'DMT','DMT_prac' , 'MMS','MMS_prac' , 'English'
]

teachers = [
	Teacher(name="Tkachenko", subjects=["SDMP", "IT"], max_hours=80),
	Teacher(name="Voloshyn", subjects=["DMT_prac"], max_hours=80),
	Teacher(name="Shyshatska", subjects=["IT_prac"], max_hours=80),
	Teacher(name="Polyshcuk", subjects=["SDMP_prac"], max_hours=80),
	Teacher(name="Trotsenko", subjects=["MMS_prac"], max_hours=160),
	Teacher(name="Taranukha", subjects=["IS"], max_hours=80),
	Teacher(name="Bashnyakov", subjects=["IS_prac"], max_hours=80),
	Teacher(name="Zinko", subjects=["IS_prac"], max_hours=80),
	Teacher(name="Korobova", subjects=["DMT"], max_hours=160),
    Teacher(name="Korolov", subjects=["MMS"], max_hours=160),
	Teacher(name="Krasovska", subjects=["English"], max_hours=80)
]

groups = [
    Group(group_name="TTP41", people_num=17, subjects_hours={"IT": 2,"IT_prac": 0 , "IS": 1,"IS_prac": 0, "SDMP": 3,"SDMP_prac": 0, "English": 1, "MMS": 1, "MMS_prac": 0,"DMT": 1,"DMT_prac": 0},),
	Group(group_name="TTP41_1", people_num=9, subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	Group(group_name="TTP41_2", people_num=8, subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	
    Group(group_name="TTP42", people_num=17, subjects_hours={"IT": 2,"IT_prac": 0 , "IS": 1,"IS_prac": 0, "SDMP": 3,"SDMP_prac": 0, "English": 1, "MMS": 1, "MMS_prac": 0,"DMT": 1,"DMT_prac": 0}),
	Group(group_name="TTP42_1", people_num=9, subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	Group(group_name="TTP42_2", people_num=9, subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),

	Group(group_name="TK41", people_num=17, subjects_hours={"IT": 2,"IT_prac": 0 , "IS": 1,"IS_prac": 0, "SDMP": 3,"SDMP_prac": 0, "English": 1, "MMS": 1, "MMS_prac": 0,"DMT": 1,"DMT_prac": 0}),
	Group(group_name="TK41_1", people_num=11,  subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	Group(group_name="TK41_2", people_num=12,  subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	
    Group(group_name="MI41", people_num=17, subjects_hours={"IT": 2,"IT_prac": 0 , "IS": 1,"IS_prac": 0, "SDMP": 3,"SDMP_prac": 0, "English": 1, "MMS": 1, "MMS_prac": 0,"DMT": 1,"DMT_prac": 0}),
	Group(group_name="MI41_1", people_num=8,  subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	Group(group_name="MI41_2", people_num=7,  subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),

	Group(group_name="MI42", people_num=17, subjects_hours={"IT": 2,"IT_prac": 0 , "IS": 1,"IS_prac": 0, "SDMP": 3,"SDMP_prac": 0, "English": 1, "MMS": 1, "MMS_prac": 0,"DMT": 1,"DMT_prac": 0}),
	Group(group_name="MI42_1", people_num=12,  subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2}),
	Group(group_name="MI42_2", people_num=13,  subjects_hours={"IT": 0,"IT_prac": 2 , "IS": 1,"IS_prac": 2, "SDMP": 3,"SDMP_prac": 2, "English": 0, "MMS": 0, "MMS_prac": 2,"DMT": 0,"DMT_prac": 2})
]


def generate_population():
	population = list()
	for _ in range(n_pop):
		schedule = generate_schedule()
		population.append(schedule)
	return population


def generate_schedule():
    schedule = list()
    occupied_slots = set()  # Множина для відстеження зайнятих слотів (день, пара, група)

    for group in groups:
        for subject, hours in group.subjects_hours.items():
            for _ in range(1, hours + 1):
                cell = dict()
                
                # Генеруємо унікальний слот
                while True:
                    day = random.choice(days)
                    lesson = randint(1, n_classes + 1)
                    slot = (day, lesson, group.group_name)
                    
                    # Перевіряємо, чи слот зайнятий
                    if slot not in occupied_slots:
                        occupied_slots.add(slot)  # Позначаємо слот як зайнятий
                        cell["Day"] = day
                        cell["Lesson"] = lesson
                        cell["Group"] = group
                        cell["Subject"] = subject
                        cell["Teacher"] = get_random_teacher(subject)
                        schedule.append(cell)
                        break  # Виходимо з циклу, коли знайдений вільний слот

    return schedule


def get_random_teacher(subject):
    eligible_teachers = [teacher for teacher in teachers if subject in teacher.subjects]
    if eligible_teachers:
        return random.choice(eligible_teachers)
    else:
        return None


def crossover(p1, p2):
	c1, c2 = p1.copy(), p2.copy()
	pt = randint(1, len(p1)-2)
	c1 = p1[:pt] + p2[pt:]
	c2 = p2[:pt] + p1[pt:]
	return [c1, c2]


def selection(pop, scores):
	selection_ix = randint(len(pop))
	selection_iy = randint(len(pop))
	if scores[selection_ix] > scores[selection_iy]:
		return pop[selection_ix]
	else:
		return pop[selection_iy]


def mutation(schedule):
    occupied_slots = set((lesson["Day"], lesson["Lesson"], lesson["Group"].group_name) for lesson in schedule)
    
    for lesson in schedule:
        if rand() < r_mut:
            while True:
                # Генеруємо новий день і номер пари
                day = random.choice(days)
                lesson_num = randint(1, n_classes + 1)
                slot = (day, lesson_num, lesson["Group"].group_name)
                
                # Перевіряємо, чи слот зайнятий
                if slot not in occupied_slots:
                    # Видаляємо початковий слот, якщо він існує в occupied_slots
                    initial_slot = (lesson["Day"], lesson["Lesson"], lesson["Group"].group_name)
                    if initial_slot in occupied_slots:
                        occupied_slots.remove(initial_slot)
                    
                    # Оновлюємо заняття та позначаємо новий слот як зайнятий
                    lesson["Day"] = day
                    lesson["Lesson"] = lesson_num
                    occupied_slots.add(slot)
                    break  # Виходимо з циклу, коли знайдений вільний слот
    return schedule

def genetic_algorithm(objective, n_iter, n_pop):
	pop = generate_population()
	best, best_eval = pop[0], objective(pop[0])
	for gen in range(n_iter):
		print("Gen:", gen)
		scores = [objective(c) for c in pop]
		for i in range(n_pop):
			if scores[i] > best_eval:
				best, best_eval = pop[i], scores[i]
		print("Current best score:", best_eval)
		if best_eval >= 0.99:
			break
		new_population = []
		while len(new_population) < n_pop:
			p1 = selection(pop, scores)
			p2 = selection(pop, scores)
			if rand() <= r_mut:
				child1 = mutation(p1)
				child2 = mutation(p2)
			else:
				child1, child2 = crossover(p1, p2)
			new_population.append(child1)
			new_population.append(child2)
		pop = new_population
	return [best, best_eval]


def accurate(schedule):
	def_teachers = defaultdict(dict)
	for i in range(len(schedule)):
		subject = schedule[i]["Subject"]
		teacher = schedule[i]["Teacher"]
		if teacher is not None:
			def_teachers[teacher][subject] = def_teachers[teacher].get(subject, 0) + 1
	teachers = dict(def_teachers)
	return ((teachers_accurate(teachers)) + calculate_fitness(schedule)) / 2


def teachers_accurate(teachers):
	score = 0
	for teacher, subjects_hours in teachers.items():
		total_hours = sum(subjects_hours.values())
		if total_hours <= teacher.max_hours:
			score += 1
	return score / len(teachers)


def calculate_fitness(schedule):
    conflicts = 0
    lessons_count = {}
    for lesson in schedule:
        key_g = (lesson["Day"], lesson["Lesson"], lesson["Group"])
        lessons_count[key_g] = lessons_count.get(key_g, 0) + 1
    for count in lessons_count.values():
        if count >= 1:
            conflicts += count - 1
    return 1.0 / (conflicts + 1.0)


def main():
    best, score = genetic_algorithm(accurate, n_iter, n_pop)
    print("Done. Best: ", score)
    time.sleep(3)
    
    day_order = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
    
    sorted_schedule = sorted(best, key=lambda x: (x["Group"].group_name, day_order[x["Day"]], x["Lesson"]))
    
    for entry in sorted_schedule:
        if entry["Teacher"] is not None:  # Перевірка на наявність вчителя
           print(entry["Day"], entry["Lesson"], entry["Group"].group_name, entry["Teacher"].name, entry["Subject"])
        else:
           print(entry["Day"], entry["Lesson"], entry["Group"].group_name, "No teacher assigned", entry["Subject"])


if __name__ == '__main__':
	main()