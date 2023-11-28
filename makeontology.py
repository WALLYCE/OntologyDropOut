from owlready2 import *
import csv
from decimal import Decimal
from owlready2 import sync_reasoner_hermit
from owlready2 import get_ontology, sync_reasoner
import matplotlib.pyplot as plt
from rdflib import Graph

os.environ["JAVA_OPTS"] = "-Xmx8G"


onto = get_ontology("ontology.rdf").load()


with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        Student = onto.Student

        new_student = Student()

        


        new_student.label.append(row['ID'])
        new_student.AdmissionYear = int(row['YEARADMISSION'])

        if row['SEMESTERADMISSION'] in '2':
            new_student.AdmissionSemester = 3
        else:
             new_student.AdmissionSemester = 1
        

        if 'ATI' in row['ID']:
            Status = onto.Active
            new_status = Status()
            new_status.label.append('Student_Active_'+row['ID'])
            new_student.StudentHasStatus = new_status;
        elif 'CON' in row['ID']:
            Status = onto.Completed
            new_status = Status()
            new_status.label.append('Student_Completed_'+row['ID'])
            new_student.StudentHasStatus = new_status;
        else:
            Status = onto.Withdrawn
            new_status = Status()
            new_status.label.append('Student_Withdrawn_'+row['ID'])
            new_student.StudentHasStatus = new_status;
        

        #DEFINE O SEXO DO ALUNO
        if row['GENDER'] in 'M':
            Gender = onto.Male
            new_gender = Gender()
            new_gender.label.append('Student_Male_'+row['ID'])
            new_student.StudentHasGender = new_gender
        elif row['GENDER'] in 'F':
            Gender = onto.Female
            new_gender = Gender()
            new_gender.label.append('Student_Female_'+row['ID'])
            new_student.StudentHasGender = new_gender
        else:
            Gender = onto.Undertemined
            new_gender = Gender()
            new_gender.label.append('Student_Undertemined_'+row['ID'])
            new_student.StudentHasGender = new_gender
      #DEFINE A NACIONALIDADE DO ALUNO
        if row['NATIVITY'] in '1':
            Nativity = onto.JuizdeForaNative
            new_nativity = Nativity()
            new_nativity.label.append('Student_JuizDeForaNative_'+row['ID'])
            new_student.StudentHasNativity = new_nativity
        else:
            Nativity = onto.NonJuizdeForaNative
            new_nativity = Nativity()
            new_nativity.label.append('Student_NonJuizDeForaNative_'+row['ID'])
            new_student.StudentHasNativity  = new_nativity


       #DEFINE O METODO DE INGRESSO DO ALUNO
        if row['QUOTA'] in '1':
            AdmissionType = onto.Quota
            new_admission = AdmissionType()
            new_admission.label.append('Student_Quota_'+row['ID'])
            new_student.StudentHasAdmissionType = new_admission
        else:
            AdmissionType = onto.NonQuota
            new_admission = AdmissionType()
            new_admission.label.append('Student_NonQuota__'+row['ID'])
            new_student.StudentHasAdmissionType = new_admission


       #DEFINE SE ALUNO JA RECEBEUBOLSAOUAE
        if row['STUDENTASSISTANCE'] in '1':
            Assistance = onto.Received
            new_assistance = Assistance()
            new_assistance.label.append('Student_ReceivedAssistance_'+row['ID'])
            new_student.StudentReceivedStudentAssistance = new_assistance
        else:
            Assistance = onto.NotReceived
            new_assistance = Assistance()
            new_assistance.label.append('Student_NotReceivedAssistance_'+row['ID'])
            new_student.StudentReceivedStudentAssistance = new_assistance

        #DEFINE ETHNICITY DO ALUNO
        if row['ETHNICITY'] in 'BLACK':
            Ethnicity = onto.Black
            new_ethnicity =  Ethnicity()
            new_ethnicity.label.append('Student_Ethinicity_Black_'+row['ID'])
            new_student.StudentHasEthnicity = new_ethnicity
        elif row['ETHNICITY'] in 'WHITE':
            Ethnicity = onto.White
            new_ethnicity = Ethnicity()
            new_ethnicity.label.append('Student_Ethinicity_White_'+row['ID'])
            new_student.StudentHasEthnicity = new_ethnicity
        elif row['ETHNICITY'] in 'YELLOW':
            Ethnicity = onto.Yellow
            new_ethnicity = Ethnicity()
            new_ethnicity.label.append('Student_Ethinicity_Yellow_'+row['ID'])
            new_student.StudentHasEthnicity = new_ethnicity
        elif row['ETHNICITY'] in 'BROWN':
            Ethnicity = onto.Brown
            new_ethnicity = Ethnicity()
            new_ethnicity.label.append('Student_Ethinicity_Brown_'+row['ID'])
            new_student.StudentHasEthnicity = new_ethnicity
        elif row['ETHNICITY'] in 'INDIGENOUS':
            Ethnicity = onto.Indigenous
            new_ethnicity = Ethnicity()
            new_ethnicity.label.append('Student_Ethinicity_Indigenous_'+row['ID'])
            new_student.StudentHasEthnicity = new_ethnicity
        else:
            Ethnicity = onto.Unknown
            new_ethnicity = Ethnicity()
            new_ethnicity.label.append('Student_Ethinicity_Unknown_'+row['ID'])
            new_student.StudentHasEthnicity = new_ethnicity

#ADICIONANDO AS COURSESUBJECTS
with open('history.csv', newline='', encoding='utf-8') as csvfile:
    # Crie um leitor CSV
    reader = csv.DictReader(csvfile, delimiter=';')
    CourseSubject = onto.CourseSubject
    for row in reader:
        for courseSubject in CourseSubject.instances():
            if row['COURSESUBJECT'].replace(' ', '_') in courseSubject.label:
                break
        else:
            new_courseSubject = CourseSubject()
            new_courseSubject.label.append(row['COURSESUBJECT'].replace(' ', '_'))



with open('history.csv', newline='', encoding='utf-8') as csvfile:
    # Crie um leitor CSV
    reader = csv.DictReader(csvfile, delimiter=';')
    Student = onto.Student
    CourseSubject = onto.CourseSubject
    Grade = onto.Grade
    for row in reader:
        existing_student = None
        for student in Student.instances():
            if row['ID'] in student.label:
                existing_student = student
                break
        existing_coursesub = None
        for coursesubject in CourseSubject.instances():
            if row['COURSESUBJECT'].replace(' ', '_') in coursesubject.label:
                existing_coursesub = coursesubject
                break
        new_grade = Grade()
        new_grade.label.append('Grade_'+row['ID']+'_'+row['COURSESUBJECT'].replace(' ', '_')+'_'+row['YEARINCOURSE']+'-'+row['SEMESTERINCOURSE'])
        new_grade.GradeValue = row['GRADEVALUE'].replace(' ', '')
        new_grade.YearInCourse = int(row['YEARINCOURSE'])
        new_grade.SemesterInCourse = int(row['SEMESTERINCOURSE'])
        new_grade.CreditsInCourse = int(row['CREDITSINCOURSE'])
        existing_student.StudentObtainedGrade.append(new_grade)
        new_grade.GradeBelongsToCourseSubject= existing_coursesub


Student = onto.Student

for student in Student.instances():
    Grades = onto.Grade
    count = 0
    points = 0
    totalPoints = 0
    period = 0
    academic_performance = 0
    for grade in Grades.instances():
        if grade.GradeBelongsToStudent == student:
            if (period < ((grade.YearInCourse - student.AdmissionYear) * 2 +(student.AdmissionSemester - grade.SemesterInCourse) + 1)):
                period = (grade.YearInCourse - student.AdmissionYear)*2 +((student.AdmissionSemester - grade.SemesterInCourse) + 1)
            if(grade.GradeValue.isdigit()):
                points += float(grade.GradeValue) * float(grade.CreditsInCourse);
                count +=float(grade.CreditsInCourse);
            else:
                if grade.GradeValue in 'RI':
                   count +=float(grade.CreditsInCourse);
    if(count!=0):
        academic_performance = (points)/count
    ##calcula desempenho
    if academic_performance < 60:
        Performance = onto.Insufficient
        new_performance = Performance()
        new_performance.label.append('Student_AcademicPerformance_Insufficient_'+student.label.first())
        student.StudentHasAcademicPerformance = new_performance;
    elif academic_performance >= 60 and academic_performance <= 70:
        Performance = onto.Regular
        new_performance = Performance()
        new_performance.label.append('Student_AcademicPerformance_Regular_'+student.label.first())
        student.StudentHasAcademicPerformance = new_performance;
    elif academic_performance > 70 and academic_performance <= 80:
        Performance = onto.Good
        new_performance = Performance()
        new_performance.label.append('Student_AcademicPerformance_Good_'+student.label.first())
        student.StudentHasAcademicPerformance = new_performance;
    else:
        Performance = onto.Excellent
        new_performance = Performance()
        new_performance.label.append('Student_AcademicPerformance_Excellent_'+student.label.first())
        student.StudentHasAcademicPerformance = new_performance;
    ##calcula period de evasao

    if 'EVA' in student.label.first():
        if period <= 3:
            Period = onto.FirstToThird
            new_period = Period()
            new_period.label.append('Student_DropOut_Period_1_3'+student.label.first())
            student.StudentDroppedOutInPeriod = new_period
        elif period >= 4 and period <= 7:
            Period = onto.FourthToSeventh
            new_period = Period()
            new_period.label.append('Student_DropOut_Period_4_7'+student.label.first())
            student.StudentDroppedOutInPeriod = new_period
        else:
            Period = onto.EighthOrGreater
            new_period = Period()
            new_period.label.append('Student_DropOut_Period_8_Greater'+student.label.first())
            student.StudentDroppedOutInPeriod = new_period

onto.save(file="ontologyCompleted.rdf")





