def find_common_skills(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        print("Invalid input: Both inputs must be sets.")
        return
    common_skills = set1 & set2
    if common_skills:
        print("Common Skills:", common_skills)
    else:
        print("No common skills found.")
student1_skills = {"Python", "SQL", "C++", "HTML"}
student2_skills = {"Java", "Python", "HTML", "CSS"}
find_common_skills(student1_skills, student2_skills)